---
id: "005484e05b9e6189"
title: "Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod"
url: "https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod"
link: "https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T23:30:03Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Siddharth Senger"]
language: "en"
summary: "Silent data corruption (SDC) happens when hardware, such as a GPU, returns a wrong but plausible number and raises no error. In distributed training, the wrong number can flow into the gradients and weights of every replica. Loss can still look normal for hours, and by the time a team notices an unexplained divergence or a weaker model, the compute is spent. It happens at scale: during a 54-day…"
tags: ["Advanced (300)", "Amazon SageMaker HyperPod", "Technical How-to"]
orgs: ["Amazon", "Meta", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "products & launches"]
content_source: "fulltext"
word_count: 4655
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod

AWS Machine Learning Blog · Siddharth Senger · 2026-11-11

Artificial Intelligence
Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
Silent data corruption (SDC) happens when hardware, such as a GPU, returns a wrong but plausible number and raises no error. In distributed training, the wrong number can flow into the gradients and weights of every replica. Loss can still look normal for hours, and by the time a team notices an unexplained divergence or a weaker model, the compute is spent. It happens at scale: during a 54-day period of Llama 3 405B pre-training on up to 16K H100 GPUs, Meta attributed 6 of 419 unexpected job interruptions to silent data corruption, and those were only the cases that interrupted the job and were traced to SDC.
Amazon SageMaker HyperPod already replaces nodes that report a fault: the health-monitoring agent watches for GPU errors, deep health checks stress-test nodes, and automatic node recovery swaps out bad hardware. SDC slips past all of these features, because the hardware never reports anything. Detection has to come from the training job itself.
In this post, we add three checks to a PyTorch DistributedDataParallel (DDP) training loop to detect SDC. When a check fires, we map the suspect rank to its node, contain the corruption, and have SageMaker HyperPod replace the node. Each check covers a different place where a fault can land:
- A non-finite gradient check catches NaN, Inf, and overflow in a GPU’s forward or backward pass, on the step it happens, and NaN or Inf that the gradient all-reduce introduces.
- A ring replay audit catches finite wrong values. On audit steps, every GPU recomputes a micro-batch from another node and compares the loss bit for bit and the gradients by fingerprint.
- A weight fingerprint comparison catches corruption in the optimizer step and in stored weights, by comparing every replica’s weights after the update.
We tested the checks with software-injected faults on a SageMaker HyperPod cluster with 4 ml.p5.48xlarge instances (32 NVIDIA H100 GPUs), and repeated every test on three instances, the minimum the checks need. The full code of this solution is available in the accompanying GitHub repository.
How silent data corruption happens and why the usual checks miss it
SDC comes from manufacturing defects (marginal transistors that slip past vendor screening) and silicon aging in a specific compute unit, most often a multiply-accumulate lane in a tensor core, which is exactly the hardware model training hammers. That marginal circuit computes correctly most of the time and wrong only under stress: high temperature, voltage droop, or specific operand patterns. Because the arithmetic logic path has no ECC or parity (unlike memory), the wrong result, say 4.0001 instead of 4.0000, is never flagged, and it flows through activations and gradients into every replica’s weights.
The reason it is so hard to catch is that SDC is in the compute path, and every integrity check you already have guards a different boundary:
The way to catch SDC is to check the result of the computation itself.
Solution overview
The loop has four steps. Your training job does the first two, and the last two use Kubernetes and SageMaker HyperPod features:
Step 1. Detect: Three checks in your training loop name a suspect GPU by comparing data-parallel replicas.
Step 2. Localize: On SageMaker HyperPod clusters orchestrated by Amazon Elastic Kubernetes Service (Amazon EKS), the Kubernetes node name contains the instance ID, so mapping a suspect rank to a node is a lookup.
Step 3. Contain and correlate: Stop the job, cordon the node, and look at its GPU metrics in the SageMaker HyperPod observability dashboards.
Step 4. Confirm and recover: Confirm when the alarm is ambiguous, replace the node after review, and resume from a checkpoint saved before the suspect window.
It helps to see the loop as layers, each adding something different:
Layers 1–3 are the only layers that detect silent SDC, and they live in your training code. Layer 4 turns their alarm into an instance ID, and the HyperPod layers corroborate the alarm and close the loop.
Prerequisites
To follow along, you need:
- A SageMaker HyperPod cluster orchestrated by Amazon EKS, with at least three GPU nodes. The ring audit needs three different nodes for every comparison it settles, and the weight comparison needs three copies of each weight to name the odd one out. See Orchestrating SageMaker HyperPod clusters with Amazon EKS.
- A PyTorch DDP training job in which every replica runs its own optimizer step, with a data pipeline that can rebuild any rank’s micro-batch for a given step, such as a seeded sampler.
- Checkpoints on shared storage, Amazon FSx for Lustre or Amazon Simple Storage Service (Amazon S3). Replacing a node destroys its root and secondary volumes, including anything on local NVMe.
- The SageMaker HyperPod observability add-on for the correlation step. Turn on advanced DCGM metrics if you want ECC, NVLink, and throttling counters.
- Access to the cluster through kubectl, and AWS Identity and Access Management (IAM) permissions for sagemaker:StartClusterHealthCheck and sagemaker:BatchReplaceClusterNodes. See Manually quarantine, replace, or reboot a node.
Step 1: Detect with three checks in your training loop
Data parallelism trains several copies of the model, called replicas, at the same time. Each replica trains on a different slice of the batch. After each backward pass, an all-reduce averages the replicas’ gradients, and every replica applies that same average in optimizer.step(). Here’s one weight across three replicas, with a learning rate of 0.1:
Local gradients differ, because each replica sees different data. And after the optimizer step, the weights must be identical, bit for bit.
Where a fault lands decides which check can see it. If replica 1 computes a local gradient of 4.00 instead of 0.40, the all-reduce spreads that error to every replica: all three apply the same wrong update, and their weights still match. Only replica 1’s local gradient looked different, and only before the all-reduce. If instead replica 1 corrupts a weight during or after the optimizer step, its weights no longer match the others. There’s one exception: a NaN or Inf in one replica’s weights reaches every replica through the next all-reduce, and after that the replicas agree again. A fault inside the all-reduce itself, such as a GPU that adds a partial sum wrong, also reaches every replica identically.
So compute-path faults must be caught before the optimizer step, while the bad gradient can still be discarded, and faults in the update or in stored weights after it. Finite wrong values need recompute: comparing gradient norms across replicas catches only NaN and Inf (see Why not compare local gradient norms?). That gives three checks on every DP rank, in a fixed order within each training step:
- Non-finite gradient check – Before the all-reduce, flag any rank whose local gradient is NaN or Inf. This catches values that blow up in a GPU’s forward or backward pass, on the step they happen, and names the GPU. After the all-reduce, check the reduced gradient for NaN or Inf too, before the update.
- Ring replay audit – On audit steps, before the optimizer step, every rank recomputes the micro-batch of a rank on another node. It compares the loss bit for bit and, with deterministic kernels, every parameter’s gradient fingerprint. This catches finite wrong values in the compute path.
- Weight fingerprint comparison – After the optimizer step, every N steps and before every checkpoint, compare every replica’s weight fingerprints. This catches faults in the optimizer step and in stored weights.
The code in this step is for PyTorch DDP. For tensor, pipeline, or context parallelism, see Beyond DDP.
Order of execution
Why not compare local gradient norms?
A natural first design, and the one we started with, flags a rank whose local gradient norm is more than k median absolute deviations (MADs) from the median of that step. We recorded every rank’s local gradient norm on every step of the three fault-free runs on 4 instances (22,800 steps, see Fault-free runs) on 32 H100s training a 953-million-parameter model, and the test doesn’t work:
- The healthy spread is too wide – Each rank sees different data, so healthy local norms already reached 224 MADs in the first 800 steps, and 1,240 MADs over all healthy steps.
- A quiet threshold sees nothing finite – At k = 336, 1.5 times the highest score in the first 800 healthy steps, it raised 11 false alarms in the remaining 22,000 healthy steps. And no finite fault came close: the faulty rank’s score never exceeded 6.9, even with one activation multiplied by 10,000.
Compare by fingerprint
Checks 2 and 3 compare tensors across GPUs. Sending whole tensors would cost too much, so each tensor is reduced to a fingerprint: two 64-bit sums of its raw bit patterns, one plain and one weighted by position. Any change to one or two elements of a tensor changes the fingerprint, for tensors with fewer than 2³² elements of up to 4 bytes each. That covers every weight fault we injected. Larger changes could, in principle, cancel out, so equal fingerprints are strong evidence of equal tensors, not proof. The position-weighted sum matters: in our tests, a swap of two weight values and a compensating change to two values left the plain sum unchanged, and only the weighted sum caught them.
Check 1: NaN/Inf gradients, before and after the all-reduce
A DDP communication hook records each rank’s local gradient before it’s averaged. It stores the squared norm of every gradient bucket and, on deterministic audit steps, the fingerprints of every parameter’s gradient (used by check 2). Then it passes the bucket to PyTorch’s standard all-reduce.
After backward, nonfinite_ranks gathers one scalar from every rank and returns the ranks whose local gradient norm is NaN or Inf. The first rank flagged is the faulty one. If the step were applied, the NaN would reach every rank on the next step.
train() also checks the gradient after the all-reduce. A NaN or Inf produced inside the reduction reaches every replica the same way, so the copies still match and check 3 passes them. Without this check, the NaN becomes NaN weights on every replica, and a checkpoint due on that step is saved with them and tagged as passing. clip_grad_norm_ already computes the norm of the reduced gradient, so the check adds only one one-element all-reduce per step. A finite error in the reduction still passes every check.
If you train with fp16 and a gradient scaler, exclude the overflow steps the scaler already skips. bf16 doesn’t have them.
Check 2: Ring replay, before the optimizer step
Every replica holds the same weights until optimizer.step(). So, between the backward pass and the optimizer step, any rank can recompute any other rank’s micro-batch, and with deterministic kernels it must get the same bits.
On an audit step, every rank r recomputes the micro-batch of rank r + 8: 8 positions ahead, which is one node away on p5 instances. It uses the unwrapped module, so nothing is all-reduced, and it restores the gradients, the module’s buffers, and the random-number state afterwards. A replay blocks the job no matter how many ranks do one, so auditing every rank costs the same wall-clock time as auditing one.
Each rank then appears in two comparisons: its own micro-batch, replayed by a peer, and the micro-batch it replayed for someone else.
- Both comparisons mismatch: That rank computed wrong in both, so it’s the culprit.
- Only one mismatches: Either side could be wrong. confirm settles it in place: the GPU eight positions after the target, on a third node, and the target itself replay the target’s micro-batch again. That also tells a persistent fault, which the target reproduces, from a transient one, which it doesn’t.
The confirmation is only independent if the three GPUs are on three different nodes. check_topology verifies that for every pair before training starts, from each pod’s NODE_NAME, and raises an error otherwise.
Choose the audit mode:
- Default kernels: Compare the loss only. This needs a forward pass whose loss is bitwise reproducible, which held in our tests: healthy replays matched the original loss bit for bit. Gradients can’t be compared this way, because attention’s default backward pass isn’t deterministic. This mode catches forward-pass faults that change the loss.
- Deterministic kernels (deterministic_audits=True): The whole audit step runs with deterministic algorithms and the math attention kernel. Gradient fingerprints then match too, so the audit also catches backward-only faults. An op with no deterministic implementation raises an error instead of producing a false alarm. On our model, a deterministic audit step cost 2.4 times a default one.
Never replay a suspect’s work on the suspect alone. A GPU with a persistent defect can reproduce its own wrong answer.
Check 3: Weight fingerprints, after the optimizer step
After optimizer.step(), every replica’s weights must be identical, so there’s no tolerance to tune. Each rank fingerprints every weight tensor and gathers everyone’s fingerprints.
A rank is named only when its copy of a tensor differs from a strict majority, more than half of the copies. With two copies, or a split with no strict majority, the comparison reports a disagreement without naming any rank.
Run it every N steps and on every checkpoint step. It’s the only check that runs after the update, so it’s the only one that can stop a checkpoint from being written out of a corrupted copy. In our tests, a weight corrupted right after one update was caught at the next checkpoint step, and the save didn’t happen. Without the forced check, the save went ahead from the corrupted copy, and the ring audit noticed only at the next audit, five steps later.
It costs 31.1 ms per check on a 953-million-parameter model: 2 percent of a step when it runs every 10 steps.
Put the checks in the training loop
train runs each step in the order of Figure 2 and stops at the first alarm. It decides whether a step is an audit step before the forward pass, because a deterministic comparison needs the original computation to be deterministic too. When check 1 or 2 fires, it zeros the gradients and returns without clipping or applying the update, so the bad gradient never reaches the weights or the optimizer state, and the exact state is still there for confirmation. After clipping, it checks whether the reduced gradient is NaN or Inf, and if it is, returns before the update. It saves a checkpoint only if nothing fired.
The alarm’s suspect_window is the range of steps since the last pass of the check that fired. A fault that was active on every step since it started began inside it. An intermittent fault can be older, and a fault that no check sees can be in any checkpoint, so treat the tags as a record that the checks passed at that step, not as proof that the saved state is clean.
A training script calls it like this:
The replay depends on these:
- Exact micro-batches: rebuild_batch(step, rank) must return exactly the micro-batch that rank trained on, for example from a seeded sampler.
- Same loss function: compute_loss must be the same function in training and in replay, including autocast, and any randomness inside it, such as dropout, must be seeded per step and rank.
- No collectives or output-affecting state in the model: The confirmation replay runs on only two ranks, the target and the third GPU, so a model that calls a collective inside its forward or backward pass (SyncBatchNorm, for example) hangs on an ambiguous alarm. A buffer that the forward pass both reads and updates makes a healthy replay differ.
- Deterministic setup: Set CUBLAS_WORKSPACE_CONFIG=:4096:8 before the training process starts, and make sure every op in the model has a deterministic implementation.
- Peer offset: Number DP ranks node by node, so that peer_offset equal to the GPUs per node puts every replayer on another node. check_topology refuses a layout where it doesn’t.
- Untested here: Unused parameters, gradient accumulation, BatchNorm, and forward hooks with side effects. With unused parameters, set deterministic_audits=False, which compares the loss only.
audit_every is the main cost-versus-robustness setting:
- Detection delay: A persistent finite fault is caught within audit_every steps if it also occurs in the kernels the audit runs. Deterministic audits run deterministic kernels and the math attention kernel, so a fault confined to the default kernels used on the other steps is never audited.
- Corrupted updates: Up to audit_every − 1 corrupted updates can be applied before the audit catches it. They’re inside the alarm’s suspect_window.
- One-time faults: A finite fault on a single non-audit step that doesn’t recur isn’t caught at all.
Make ckpt_every a multiple of both audit_every and check_every, so every checkpoint step is audited before its update and fingerprinted after it.
We measured the average step time end to end, over 1,000 consecutive steps per schedule, on the 953M model and 32 H100s. Every schedule with the checks also runs the weight check every 10 steps:
About 7 percentage points of each schedule’s cost don’t depend on audits: the gradient hook and the two NaN/Inf checks on every step, and the weight check every 10 steps. A reasonable starting point for production is deterministic audits every 100 steps, which cost 10 percent here. They still catch a persistent fault within 100 steps, including a backward-only one, at the price of up to 99 corrupted updates to roll back. Audit every 10 steps when you need faster detection, for example during a burn-in on new capacity or while you watch a suspect node. Measure the cost on your own model: deterministic attention uses the math kernel, whose cost grows with the square of the sequence length.
In the fault-free runs, 15,320 audit steps and 3,080 weight checks raised no alarm, which bounds the false-alarm rate at about 1 in 5,100 audit steps (95 percent confidence).
Step 2: Localize the suspect rank to a node
A rank is a logical ID. To act on it, you need the instance and the physical GPU. On HyperPod EKS, the Kubernetes node name is the instance ID with a hyperpod- prefix. Pass it to your pod with the Kubernetes downward API:
At job start, log a table that maps every rank to its node, instance, and GPU UUID:
If a job is already running without the downward API, you can map a pod to its node from outside with kubectl get pod <pod> -o jsonpath='{.spec.nodeName}'.
Step 3: Contain the damage and check the GPU metrics
When an alarm fires, stop the job first. Then stop new work from landing on the suspect node by cordoning the node while you investigate:
Then open the GPU health dashboard in the SageMaker HyperPod observability add-on, filter to the suspect node and GPU, and look at the time the alarm fired. A rise in correctable ECC errors, PCIe replays, throttling, or temperature on that GPU raises confidence that the hardware is at fault. A clean panel doesn’t clear the node: pure SDC often leaves no trace in hardware telemetry.
Step 4: Confirm, then replace the node
With the Step 1 checks running, an alarm already names a suspect GPU. When you see a symptom without an alarm, such as a loss spike, or want to rule out software before you replace anything, start with the cheap explanations. Most loss spikes aren’t SDC, and chasing SDC on a data bug wastes days:
The test that separates SDC from software is whether the problem follows the hardware:
- A reproducible failure doesn’t rule out SDC – Meta pinned a failing workload to one core and got the same wrong answer every time for specific inputs.
- Neither does a failure that starts at a software change – Google traced one incident to a correct library update that began using rarely used instructions on defective cores.
- Don’t expect the global loss to point anywhere – A forward fault first changes the faulty rank’s own loss, and the all-reduce then spreads its gradient to every replica. Per-rank checks and replays give you the locality.
Decide what the alarm means
In production, keep a human approval on every replacement until you have evidence of the checks’ precision on your own workload. Synthetic tests like ours don’t establish it.
Confirm an ambiguous alarm
A deep health check is the main tool for ambiguous alarms. Its stress tests catch faults that the hardware reports, and subtle data-dependent faults often pass. To run one on the suspect instance group:
Replace the node
When you’re ready to replace the node, you have two options. Both trigger the same SageMaker HyperPod recovery process, described in Manually quarantine, replace, or reboot a node.
If automatic node recovery is turned on, you can label the node and let SageMaker HyperPod replace it, which is convenient for automation:
To use the API instead, run:
On clusters that use Karpenter for autoscaling, BatchReplaceClusterNodes terminates the node but creates a replacement only if pending pods need one. After the replacement joins, the training job restarts through the SageMaker HyperPod training operator or the job’s restart policy, and your training script resumes from the newest checkpoint saved before the alarm’s suspect_window starts. Call find_divergent_ranks right after loading it, before the first step. Replacement destroys the node’s root and secondary volumes, so keep checkpoints on shared storage.
Automating the workflow
The manual steps are for understanding. In production, wrap them in a small controller that runs in your own cluster and account:
- Trigger: The training job reports the alarm as a Kubernetes event, a small custom resource (for example SDCReport{rank, job, step, check}), or an Amazon CloudWatch alarm on metrics such as sdc_nonfinite_grad, sdc_replay_mismatch, and sdc_divergent_tensors.
- Resolve: The controller maps rank → pod → node through the Kubernetes API, then node → instance ID by stripping the hyperpod- prefix.
- Contain: It cordons the node.
- Decide: It applies the table in Step 4. The ring audit has already confirmed ambiguous pairs in place, so the alarm carries the verdicts. For an ambiguous result, it runs one node-scoped deep health check.
- Recover: For a replacement, it asks a human to approve, then calls BatchReplaceClusterNodes, or sets the node-health label if automatic node recovery is turned on. Then it relies on the training operator and your checkpoint reload, and records every step in CloudWatch.
Build it as a lightweight Kubernetes operator, or as an Amazon EventBridge rule on the CloudWatch alarm that invokes an AWS Lambda function.
Use case: Testing the checks on SageMaker HyperPod
We ran the tests twice on one SageMaker HyperPod cluster orchestrated by Amazon EKS, using 4 and then 3 ml.p5.48xlarge instances with 8 NVIDIA H100 80GB HBM3 GPUs each, and PyTorch 2.9.0 (CUDA 13.0) from the AWS Deep Learning Containers training image. The model was a 953-million-parameter Llama-style decoder with 16 layers, a hidden size of 2,048, 16 attention heads, a 32,000-token vocabulary, and 2,048-token sequences. Each GPU processed 2 sequences per step (131,072 tokens per step on 32 GPUs), with fp32 weights, gradients, and optimizer state, and bf16 autocast for compute. We trained with AdamW at a learning rate of 3 × 10⁻⁴ after a 100-step linear warm-up, with betas of (0.9, 0.95), weight decay of 0.1, and gradient clipping at 1.0. The data was synthetic: a copy task with Zipf-distributed tokens whose first half repeats, seeded per rank and step so that any micro-batch can be rebuilt.
Fault scenarios
Faults were injected in one layer, the MLP down-projection of the eighth of 16 decoder blocks, on a chosen rank and step:
- Forward faults change the layer’s output but keep its gradient path, like a wrong multiply in the forward pass.
- Backward-only faults change the gradient of the layer’s input or weight.
- Weight faults change one GPU’s copy of the stored weight right after the optimizer step: a bit flip, a swap of two values, or a compensating change to two values.
- A persistent fault recurs in everything the faulty GPU computes, including the replays it runs for other ranks. A transient fault fires once.
Every scenario restarts from a snapshot taken after 400 warm-up steps, and step numbers count from it. Unless noted, audits ran every 10 steps with deterministic kernels, weight checks every 10 steps, and a checkpoint every 20. The table shows the 4-instance results. On 3 instances, every scenario raised the same alarm, at the same step, from the same check, naming the same ranks. Only the peer ranks changed.
Fault-free runs
To measure false alarms, we trained without faults on both cluster sizes, with three schedules each. Every schedule ran the weight check every 10 steps and saved no checkpoints, and each run’s length was fixed in minutes, so the two schedules that audit every step contribute most of the audit steps:
With 0 alarms in 15,320 audit steps, the rule of three puts a 95 percent upper bound of 3 / 15,320, about 1 in 5,100, on the false-alarm rate per audit step. The NaN/Inf checks didn’t fire on any fault-free step either. The gradient-norm analysis in Why not compare local gradient norms? uses the 4-instance runs only.
Beyond DDP
The weight comparison isn’t limited to DDP. find_divergent_ranks takes any data-parallel group, so it also applies to tensor, pipeline, and context parallelism, HSDP, and mixture of experts, which are all layouts that keep independent copies of each weight. It can’t help under ZeRO-1 or full FSDP sharding, where each shard’s update is computed on only one rank. We tested the checks and the training loop in this post only with DDP.
To use it in another layout, call find_divergent_ranks with the group that holds copies of the same shard. With only two copies, it can detect a disagreement but can’t name the faulty copy.
If you’d rather have the service check your nodes for you, SageMaker HyperPod also offers the MultiNodeTraining deep health check. It runs a short, fixed distributed training job across a batch of GPU nodes, with no code changes, and replaces nodes whose training loss turns NaN or Inf, diverges, or doesn’t finish in time. Select it alongside InstanceStress and InstanceConnectivity when you create an instance group, or run it on demand with StartClusterHealthCheck. It complements the checks in this post: use it to screen new and replacement nodes before your job lands on them, and the in-job checks to catch wrong values in your own training that never become NaN or Inf. For details, visit SageMaker HyperPod Deep Health Checks.
Clean up
To avoid ongoing charges, delete what you created for testing. If you created a HyperPod cluster, delete it with aws sagemaker delete-cluster --cluster-name <cluster-name>. That removes only the HyperPod resources. Delete the EKS cluster, its add-ons, and any Amazon FSx volumes separately, after the HyperPod cluster. See Deleting a SageMaker HyperPod cluster.
Conclusion
In this post, we showed how to detect silent data corruption in data-parallel training and how to hand a suspect node to SageMaker HyperPod for replacement. Three checks cover the three places a fault can land: a NaN/Inf check on each rank’s gradient and on the reduced gradient, a ring replay that compares every GPU’s work with a GPU on another node, and a weight fingerprint comparison after the update. Run the first two before the optimizer step, don’t apply a step that failed a check, and compare weights before every checkpoint. Node names on SageMaker HyperPod EKS clusters turn the suspect rank into an instance ID. Then quarantine the node, roll back to a checkpoint from before the suspect window, and let the node-health label or the Replace API complete the recovery.
To get started, review the SageMaker HyperPod resiliency features for Amazon EKS, and try the companion repository. To go deeper, see deep health checks and the observability add-on.
