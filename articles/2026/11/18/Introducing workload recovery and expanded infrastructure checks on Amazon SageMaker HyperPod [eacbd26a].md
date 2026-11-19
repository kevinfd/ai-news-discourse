---
id: "eacbd26a911f6855"
title: "Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod"
url: "https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod"
link: "https://aws.amazon.com/blogs/machine-learning/introducing-workload-recovery-and-expanded-infrastructure-checks-on-amazon-sagemaker-hyperpod"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-18T23:03:29Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Roy Allela"]
language: "en"
summary: "Large training jobs can fail even when every node looks healthy. A GPU with a subtle fault can pass its stress tests and still return wrong values. When a job stalls on an NCCL timeout, it keeps its GPUs, and Slurm still shows it as running. If a device plugin crashes on one node, the job fails with an error that never mentions the plugin. Teams usually find these problems only after the loss…"
tags: ["Amazon SageMaker HyperPod", "Announcements"]
orgs: ["Amazon", "Meta", "Nvidia"]
topics: ["jobs & society", "chips & infrastructure", "models & research", "health & science"]
content_source: "fulltext"
word_count: 4297
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod

AWS Machine Learning Blog · Roy Allela · 2026-11-18

Artificial Intelligence
Introducing workload recovery and expanded infrastructure checks on Amazon SageMaker HyperPod
Large training jobs can fail even when every node looks healthy. A GPU with a subtle fault can pass its stress tests and still return wrong values. When a job stalls on an NCCL timeout, it keeps its GPUs, and Slurm still shows it as running. If a device plugin crashes on one node, the job fails with an error that never mentions the plugin. Teams usually find these problems only after the loss diverges or the job fails, and by then the compute is spent. Each of these failures lowers goodput, the share of your cluster’s time that goes to useful training. Today, we’re introducing workload recovery and infrastructure checks on Amazon SageMaker HyperPod that catch these failures sooner and raise the goodput of your training workloads.
SageMaker HyperPod already handles nodes that report hardware faults. The health monitoring agent (HMA) watches each node for GPU errors, deep health checks test nodes during provisioning, and automatic node recovery reboots or replaces faulty hardware. These features look at one node’s hardware at a time. They can’t tell whether the GPUs train correctly, whether a job is still making progress, or whether the Kubernetes components a job depends on are working.
In this post, we walk through the three new capabilities that catch these failures. For each one, we show how to set it up and what it reports when it finds a problem:
- MultiNodeTrainingValidation is a new deep health check for HyperPod clusters orchestrated by Amazon Elastic Kubernetes Service (Amazon EKS). When HyperPod provisions an instance, or when you run the check on demand, it trains a small model on the instance and then across instances of the same type. The instance fails if the loss becomes NaN or infinite, or training doesn’t finish in time.
- The HyperPod Kubernetes Resource Monitoring Agent watches the Kubernetes layer of an EKS cluster for problems such as crash-looping device plugins, missing DaemonSets, and tainted nodes. When a job fails, it reports the pods and nodes involved as Kubernetes events and Amazon CloudWatch logs.
- Hung job detection finds Slurm jobs that have stopped making progress. An agent on each node watches the job’s output and GPU activity, or log patterns that you define. It writes an event to CloudWatch and can cancel the job so that Slurm requeues it.
Why node health alone isn’t enough
The existing HyperPod resiliency features check a single node at a time. The health monitoring agent (HMA) watches each node for GPU errors such as Xid and NVLink faults, Elastic Fabric Adapter (EFA) errors, and kernel errors. The InstanceStress deep health check runs DCGM level 4 diagnostics and tests each instance’s GPUs, GPU memory, NVLink, and EFA devices. The InstanceConnectivity check runs NCCL tests across GPU instances, or NCCOM tests on AWS Trainium. Together, these confirm that each node’s hardware works. They don’t show whether the GPUs compute correctly, whether a job is still making progress, or whether the cluster’s Kubernetes components are healthy. Three kinds of failure get past them:
- Numerical faults – A GPU can pass every hardware test and still compute wrong results. The first sign is often NaN or infinite loss in a production run. Meta attributed 6 of the 419 unexpected interruptions in its 54-day Llama 3 405B pre-training run to silent data corruption (The Llama 3 Herd of Models).
- Hung jobs – An NCCL timeout, a stalled data pipeline, or a deadlock can stop a job without ending it. The job keeps its GPUs and their memory, and Slurm reports it as running until someone checks the loss curve or the log.
- Cluster-level failures – Some failures happen in Kubernetes, not in a node’s hardware. A device plugin crash-loops, a required DaemonSet never starts on a new node, or ranks on different nodes fall out of step in an NCCL collective. HMA checks each node on its own, so it doesn’t see these problems. When the job fails, the error often doesn’t say which pod or node caused it.
Solution overview
Each capability covers a different point in a training run. MultiNodeTrainingValidation runs when instances are provisioned, or on demand, and confirms that their GPUs train correctly. Hung job detection runs alongside each Slurm job and catches a job that has stopped making progress. The HyperPod Kubernetes Resource Monitoring Agent watches the cluster continuously and, when a job fails, reports the pods and nodes that were involved. The following table summarizes the three.
Hung job detection is new for Slurm clusters. On EKS clusters, HyperPod already detects hung jobs that run through the HyperPod training operator, and Ray Train jobs get hang detection by default. We describe both options in the hung job detection section.
Each capability targets a different source of lost goodput. Scheduling goodput is the share of time that all the resources a job needs are available. Runtime goodput is the share of that time in which the job makes forward progress. Program goodput is the share of the hardware’s peak performance that the job gets. The following table shows the effect of each capability.
Consider a pre-training job running on 32 ml.p5.48xlarge instances (256 NVIDIA H100 GPUs). If the job hangs at 1:00 AM and no one notices until 9:00 AM, it wastes 256 instance-hours or 2,048 GPU-hours. At the SageMaker HyperPod on-demand price of approximately $66 per instance-hour in US East (N. Virginia), the hang costs about $16,900. With a 15-minute hung job detection rule, HyperPod cancels the stalled job and Slurm requeues it. The hang costs about $530 instead, saving approximately $16,400.
Validate training correctness with the MultiNodeTrainingValidation deep health check
The MultiNodeTrainingValidation deep health check trains a fixed, known-good workload, first on each instance and then across instances. It catches GPUs that pass InstanceStress and InstanceConnectivity but produce NaN or infinite loss once they train together. If an instance fails, HyperPod labels it as failed and, with automatic node recovery turned on, reboots or replaces it. When the check runs during provisioning, this happens before your jobs can use the instance.
How it works
MultiNodeTrainingValidation adds two tests to the deep health check run:
- Tiny Megatron test: A short Megatron-LM training run on all GPUs of each instance.
- Megatron test: The same workload across instances of the same type, communicating over EFA.
Either test fails an instance if the training loss becomes NaN or infinite, or if training doesn’t finish within the time limit. The workload is fixed, so a failure points to the hardware rather than to a model or code change.
The following table shows how it fits with the other deep health checks.
Prerequisites
You need the following:
- An Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS.
- An instance group of a supported EFA-enabled NVIDIA GPU instance type, such as ml.p5.48xlarge. The Megatron test runs across instances of the same type.
Turn on MultiNodeTrainingValidation for an instance group
HyperPod runs deep health checks when it creates or updates instances. To include MultiNodeTrainingValidation, add it to OnStartDeepHealthChecks in the instance group configuration that you pass to create-cluster or update-cluster. We turned on all three checks:
To confirm the setting, run the following command:
The output lists the three checks:
Run MultiNodeTrainingValidation on demand
You can also check instances that are already in the cluster, for example before a long pre-training run. Use the StartClusterHealthCheck API:
To check specific instances instead of the whole group, add "InstanceIds": [...] to the configuration.
Check the results
HyperPod writes one line per test to the DeepHealthCheckResults/<id> log stream in your cluster’s CloudWatch log group, /aws/sagemaker/Clusters/<cluster-name>/<cluster-id>. Here’s the stream from our run on two ml.p5.48xlarge instances. TINY_MEGATRON and MEGATRON are the two MultiNodeTrainingValidation tests:
When the run finishes, each instance carries the result as a node label:
For the training details, read /var/log/aws/clusters/sagemaker-deep-health-check.log on the instance, for example through an AWS Systems Manager session. On the instance that ran rank 0, the log ends with a summary of the Megatron test:
The other instance’s log has a line for every iteration, with the loss and a running count of NaN iterations:
In our run, the loss fell from 11.57 to 3.62 over 300 iterations, with no NaN or skipped iterations, at about 507 milliseconds per iteration on 16 H100 GPUs.
How long MultiNodeTrainingValidation takes
On our two-node cluster, the full deep health check took 1 hour 28 minutes after the instances finished their lifecycle scripts. DCGM level 4 diagnostics took most of that. The two MultiNodeTrainingValidation tests added about 8 minutes. Instances can’t take workloads until the checks finish, so plan for this additional time when you add capacity.
Keep in mind that MultiNodeTrainingValidation tests the hardware with a fixed reference workload. A pass means the instances trained that workload correctly. It doesn’t guarantee that your own job will converge. We recommend running it on new capacity, on replacement instances, and before long pre-training runs.
Catch cluster-level failures with the HyperPod Kubernetes Resource Monitoring Agent
HMA watches the hardware on each node, but many failures that stop a training job happen in Kubernetes. A device plugin can crash-loop until its node stops offering GPUs to the scheduler, or a taint can evict a job’s pods. The job error rarely names the pod or node involved, so engineers piece together what happened from kubectl output, per-rank logs, and timestamps.
The HyperPod Kubernetes Resource Monitoring Agent watches these resources from one place in the cluster. When something breaks, it tells you what changed and which nodes, pods, and jobs are affected. It reports through Kubernetes events and structured CloudWatch logs. The agent only reports. It doesn’t reboot nodes or restart jobs, because the cause might be in the workload. HMA and HyperPod node recovery still handle hardware faults, and the HyperPod training operator still handles job restarts.
How the agent works
The agent runs as a single pod per cluster in the aws-hyperpod namespace and prefers CPU nodes, so it doesn’t use GPU capacity. It watches the following:
- Nodes: The agent reports these changes: 
         
  - Condition changes such as NotReady or memory, disk, or PID pressure.
  - Fewer allocatable GPUs or EFA devices.
  - Lost NVIDIA capability labels.
  - Added, changed, or removed taints.
  - Missing HyperPod labels.
- Critical infrastructure pods: DaemonSet pods in kube-system, aws-hyperpod, and kubeflow, plus the training operator’s controller. The agent reports crash loops, restarts, container errors, and pods that stay not ready.
- DaemonSets: Required DaemonSets that are missing or have no available pods, rollouts that stall, and pods running on nodes that no longer allow them.
- Training jobs: HyperPodPyTorchJob, Kubeflow PyTorchJob (v1), and Kubeflow TrainJob (v2). When a job fails, the agent records the failure reason with the job’s pods and nodes.
- NCCL communication: For jobs that opt in, the state of the job’s NCCL communicators, read from NCCL’s built-in reliability, availability, and serviceability (RAS) subsystem.
The agent reports what it finds in two places:
- Kubernetes events on the affected node, pod, DaemonSet, or job. A Warning event marks a problem and a Normal event marks its recovery. You read them with kubectl get events and kubectl describe.
- Structured JSON logs in the cluster’s CloudWatch log group, which keep the history after Kubernetes events expire.
The following table lists the events you’re most likely to see.
For the full list of events, see the documentation.
Prerequisites
You need the following:
- A SageMaker HyperPod cluster orchestrated by Amazon EKS.
- For an existing cluster, kubectl and Helm access to the cluster, and the HyperPod Helm chart from the sagemaker-hyperpod-cli repository.
- NCCL 2.24 or later in the training container, if you want to monitor NCCL communication.
Install and verify the agent
If your cluster already uses the HyperPod Helm chart, apply the agent’s custom resource definition (CRD) first, because Helm doesn’t install CRDs during an upgrade. Then upgrade the release with the agent turned on:
The upgrade also moves the other HyperPod components in the chart, such as HMA and the device plugins, to the chart’s current versions. To see what will change first, run the same command with --dry-run=server.
Check that the agent is running and that its health report exists:
The health report lists the HyperPod components that the agent tracks, such as HMA, and when their status last changed:
By default, HMA is the only required DaemonSet. If your cluster uses the device plugins from the HyperPod Helm chart, add them so that the agent reports a missing plugin. Also add the namespaces where your training jobs run, so that it can link pod failures to their jobs. Each list replaces its default, so keep the default entries. Save the following as krma-values.yaml:
Then apply it:
See what the agent reports
To see how the HyperPod Kubernetes Resource Monitoring Agent handles an infrastructure failure, we deployed a small DaemonSet into aws-hyperpod, pinned it to one node, and made it exit a few seconds after starting. It behaves like a crash-looping device plugin without touching the real one. Within seconds, the agent raised events on the pod and the DaemonSet:
Next, we ran a two-node HyperPodPyTorchJob and made one rank exit during training. The agent raised a TrainingJobFailed event on the job:
It also wrote the failure to CloudWatch with the pods and nodes involved, so you don’t need to look them up from the job’s pod list:
The agent writes these logs to the cluster log group, /aws/sagemaker/Clusters/<cluster-name>/<cluster-id>, in streams named SageMakerClusterMonitoringAgent/<instance-group>/<instance-id>. It starts a new stream when it moves to another node, so filter by the stream prefix. For sample queries, see the documentation.
Monitor NCCL communication for a job
NCCL 2.24 and later include the reliability, availability, and serviceability (RAS) subsystem, a small listener in each NCCL process that reports the state of the job’s communicators. For jobs that opt in, the agent reads this report from every pod every 30 seconds.
By default, NCCL binds the RAS listener to localhost inside the pod, where the agent can’t reach it. To opt a job in, you bind the listener to the pod IP instead. That makes port 28028 reachable on the pod network, which NVIDIA’s documentation notes has security implications. Before you turn it on, apply a Kubernetes NetworkPolicy that allows TCP port 28028 only from the agent’s pod and still allows traffic between the job’s own pods. The agent’s documentation includes an example policy. Then set NCCL_RAS_ADDR in the training container:
To confirm the setting, turn on NCCL debug logging with NCCL_DEBUG=INFO and NCCL_DEBUG_SUBSYS=INIT,RAS. Each rank then logs the address RAS listens on:
If the address is ::1 or 127.0.0.1, NCCL_RAS_ADDR isn’t set and the agent can’t reach the listener.
For each monitored job, the agent combines the per-pod results into a job-level state. The job is healthy when every pod returns a valid report, degraded when only some do, and unhealthy when none do. Unhealthy usually means the training processes have stopped.
The agent logs a summary after each polling cycle. In a run on two ml.p5.48xlarge instances, every cycle reported both training pods healthy, 30 seconds apart:
The agent also writes each RAS report to CloudWatch, so you can spot communicator problems while the job is still running. In our test, we made one rank of a two-node job stop calling all_reduce. The report from the next polling cycle showed the communicator out of step and named the rank, GPU, process, and node that had fallen behind:
Rank 1 is one operation behind rank 0, so start with rank 1’s GPU on node 10.0.2.22.
Detect and recover hung jobs on HyperPod Slurm clusters
A training job can hang without exiting. An NCCL timeout, a stalled data pipeline, or a deadlock can leave the job holding its GPUs while Slurm still shows it as running. It stays that way until someone notices that the loss or the log has stopped changing. Teams that run Slurm often build their own watchdog scripts and alarms to catch these jobs, and then need to maintain them.
Today, we’re launching hung job detection for SageMaker HyperPod Slurm clusters. It finds these jobs, writes an event to CloudWatch, and can cancel a hung job so that Slurm puts it back in the queue. You turn it on for each job with an environment variable that points to a small rules file. It needs no changes to your training scripts or containers, and it works with PyTorch, TensorFlow, JAX, and custom scripts.
How hung job detection works
Hung job detection runs as an agent on every node and is off by default. The agent watches only jobs that set the HYPERPOD_HANG_RULES environment variable to the path of a rules file. The rules file decides how the agent detects a hang:
- Default detection watches the job’s standard output and GPU activity. It declares a hang when the output stops for an extended period while the GPUs sit idle but still hold memory. That’s what a rendezvous hang looks like, when one node fails and the others wait at a barrier. It also declares a hang when the output stops for a longer period, whatever the GPUs are doing. In our test, the first case fired 15 minutes after the job’s last output.
- Custom rules watch your log for regular expressions that you choose. A progress rule declares a hang when a line such as your training step message doesn’t appear within its timeout. An error rule declares a hang as soon as a line such as an NCCL error appears. Custom rules replace default detection for that job.
When the agent declares a hang, it writes a HANG_DETECTED event to CloudWatch. If the rules file sets the action to cancel, the agent also cancels the job and Slurm requeues it. With the default action, notify, the agent writes the event and leaves the job running.
Hung job detection is separate from auto-resume, which restarts jobs that exit after a hardware failure. Auto-resume handles jobs that crash and hung job detection handles jobs that keep running without making progress.
On HyperPod clusters orchestrated by Amazon EKS, HyperPod already detects hung jobs in two cases. The HyperPod training operator checks the logs of each HyperPodPyTorchJob against rules in the job specification and restarts the job when it hangs. The same rules can also restart a job whose throughput drops or whose loss spikes. You don’t need Ray for this. For Ray Train jobs, HyperPod hung job detection for Ray watches every worker by default, with no changes to your code.
Prerequisites
You need the following:
- A SageMaker HyperPod cluster orchestrated by Slurm.
- A HyperPod Slurm AMI released on or after November 10, 2026, which includes hung job detection. Clusters created on or after that date already have it. To check an existing cluster without updating it, run srun --help on a cluster node. If the output lists --no-hang-detection, the cluster supports hung job detection. If it doesn’t, update the cluster software first. The update replaces each instance’s root volume, so back up anything stored there before you update.
- A rules file that every compute node in the job can read at the same path. The agent reads the file from that path on each node. Shared storage such as Amazon FSx for Lustre or Amazon Elastic File System (Amazon EFS) is a straightforward option. To keep rules files in Amazon Simple Storage Service (Amazon S3), copy them to the same path on every node, for example in your lifecycle script. If you plan to use a directory such as /opt/slurm, first confirm that it’s shared across nodes rather than local to each one.
Turn on hung job detection
Create a rules file on shared storage. The smallest valid file turns on default detection:
The agent uses whatever rules file a job points to and doesn’t check who owns it. Anyone who can edit the file, or replace it in its directory, can change detection for every job that uses it, including making the agent cancel those jobs. The chmod 600 in the example keeps a personal rules file private to its owner. For a file that a team shares, use chmod 644 so the team can read it and only its maintainer can edit it. In both cases, make the parent directory writable only by its owner so nobody can swap the file.
Then point the job at the rules file when you submit it:
To use one rules file for many jobs, you can also set HYPERPOD_HANG_RULES in a shell profile or a site-wide profile script.
When a monitored job starts, the first lines of its output show that the agent registered it:
These lines also appear when the rules file is invalid, so check CloudWatch for a CONFIG_ERROR event too, as described in the next section.
Add custom rules to track training progress
Default detection can’t catch a job that keeps its GPUs busy without making progress, so we recommend at least one rule that watches for your training steps or epochs. The following rules file cancels the job if no epoch finishes for 45 minutes, or as soon as an NCCL error appears:
The fields work as follows:
- Set enabled to true on each rule. Rules are off by default.
- start_timeout_minutes is how long the job can run before the pattern first appears. Set it longer than the time your job needs to load the model, compile, and restore a checkpoint.
- timeout_minutes is how long the pattern can stay absent after that. Set it longer than the biggest normal gap, including checkpoint saves and evaluation.
- stop_pattern turns the rule off when it matches, so work after training ends isn’t flagged.
- fault_on_match marks an error pattern. One match means the job is hung.
By default, the agent reads the job’s Slurm output file. To watch a different file, set monitoring.log_file. To cut false positives, set metric_evaluation_data_points on a rule so that several 10-second checks in a row must fail before the agent declares a hang. A rules file can have up to 20 rules and be up to 1 MB.
Start with "action": "notify" while you tune timeouts and patterns, and switch to cancel once the events match real hangs.
View hung job detection events in CloudWatch
HyperPod writes detection events from the controller node to the cluster’s CloudWatch log group, /aws/sagemaker/Clusters/<cluster-name>/<cluster-id>, in the stream SageMakerHangJobDetectionEvents/<controller-instance-group>/<controller-instance-id>. Events for every job land in this stream, whichever node the job ran on. To find the events for one job, filter by its job ID:
We tested each detection method on a HyperPod Slurm cluster with two ml.p5.48xlarge instances. The first test job allocated GPU memory and then stopped producing output. Default detection flagged it 15 minutes after its last output:
The layer field shows which method fired: signal_evaluator for default detection, or pattern_evaluator for a custom rule. In a second test, a progress rule with a 2-minute timeout fired 2 minutes after the job’s last step. In a third, an error rule fired about one second after the job printed an NCCL error line. Because that rules file used cancel, the agent also wrote a HANG_ACTION_TAKEN event with the action Slurm took (we’ve left out the time, level, and msg fields):
Slurm put the job back in the queue, and the requeued run started about 2.5 minutes later. sacct shows both runs:
Slurm requeues a job up to the cluster’s MaxBatchRequeue limit, which was 5 on our cluster. A job submitted with #SBATCH --no-requeue reported "action": "cancel" instead and stayed canceled. With notify, there’s no HANG_ACTION_TAKEN event. The agent follows HANG_DETECTED with a record that says Hang notification sent, no automatic action taken.
If a rules file is missing or invalid, the agent doesn’t monitor the job and writes a CONFIG_ERROR event instead. Here’s the event for a rules file with a JSON syntax error:
The job ran to completion without monitoring, and nothing appeared in sbatch, squeue, or the job’s output. Test a new rules file with a short job and check for this event before you use it for production jobs.
With notify, the job keeps running until someone acts on the event. To get an alert, create a CloudWatch metric filter for HANG_DETECTED events and an alarm that notifies an Amazon Simple Notification Service (Amazon SNS) topic:
Turn off hung job detection
To turn off detection for a job that would otherwise inherit HYPERPOD_HANG_RULES, add --no-hang-detection to srun, or to sbatch to cover every step in the job. To turn it off for every job that uses a rules file, set "enabled": false in the file. Running jobs keep their current settings, and the change applies to jobs you submit afterward.
Conclusion
Node health is essential to reliable distributed training, but it does not provide a complete picture of workload health. MultiNodeTrainingValidation detects instances that pass hardware diagnostics but produce invalid training results. The HyperPod Kubernetes Resource Monitoring Agent connects Kubernetes infrastructure failures to the jobs, pods, and nodes involved. Hung job detection identifies Slurm jobs that remain active after they stop making progress and can return them to the queue automatically.
Together, these capabilities help you detect failures earlier, shorten investigations, and raise goodput by reducing the GPU time spent on workloads that can’t make useful progress. Use MultiNodeTrainingValidation when adding or revalidating capacity, run the HyperPod Kubernetes Resource Monitoring Agent continuously on supported Amazon EKS clusters, and begin hung job detection in notify mode before you switch to automatic cancellation. To get started, see the SageMaker HyperPod resiliency documentation for Amazon EKS and the hung job detection documentation for Slurm. To learn more, visit the Amazon SageMaker HyperPod product page.
