---
id: "f5b85121619c1f6e"
title: "Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs"
url: "https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions"
link: "https://aws.amazon.com/blogs/machine-learning/write-your-own-training-loop-without-managing-gpus-with-amazon-sagemaker-training-sessions"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-22T18:00:01Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Nicolas Jourdan"]
language: "en"
summary: "Fine-tuning a large language model (LLM) today usually forces a tradeoff between training loop control and operational simplicity. With fully managed services you select a base model, provide data and hyperparameters, and the service owns everything else, which works well when a standard, prepackaged recipe fits your problem. Less managed services give you more control, but you also manage more…"
tags: ["Advanced (300)", "Amazon SageMaker AI", "Announcements"]
orgs: ["Amazon", "OpenAI"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "agents & coding"]
content_source: "fulltext"
word_count: 2203
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs

AWS Machine Learning Blog · Nicolas Jourdan · 2026-10-22

Artificial Intelligence
Write your own training loop — without managing GPUs — with Amazon SageMaker training session APIs
Fine-tuning a large language model (LLM) today usually forces a tradeoff between training loop control and operational simplicity. With fully managed services you select a base model, provide data and hyperparameters, and the service owns everything else, which works well when a standard, prepackaged recipe fits your problem. Less managed services give you more control, but you also manage more of the underlying infrastructure and training frameworks. Sometimes a standard recipe isn’t enough: you need a custom loss or data curriculum for supervised fine-tuning (SFT), your own preference optimization, a reinforcement learning (RL) reward function, or an alignment algorithm published last week. As soon as you need to shape the training procedure yourself, you take on that infrastructure work to gain algorithmic freedom.
Today, serverless model customization in Amazon SageMaker AI expands with training session APIs, which remove that tradeoff by drawing the abstraction boundary one level lower. Instead of abstracting away the algorithm, they abstract away the compute. Operations like forward_backward(), optim_step(), and sample() become SageMaker API calls that you compose into whatever procedure your technique requires: SFT, preference optimization, RL, or something new. The calls target a live, stateful session, so the model stays loaded on the GPUs across steps, and you drive as many calls as you need against it. The service handles runtime setup, distributed execution, gradient synchronization, fault recovery, tenant isolation, and the operations of running GPUs at scale. You write the training loop, and SageMaker AI runs the infrastructure.
Alongside the service, we’re releasing the SageMaker training sessions cookbook, a set of ready-to-run SFT and RL recipes that you can use as blueprints for your own training loops.
In this post, we introduce the programming model and the three SDK clients, and show where training session APIs fit among the model training and customization options in SageMaker AI. We then take apart a minimal RL loop on grade-school math problems (GSM8K) to show how the operations fit together and finish with a real-world workload from the cookbook: reinforcement learning on competitive programming problems, where generated code is graded by running it against unit tests.
What are SageMaker AI training session APIs?
With SageMaker AI training session APIs, you can drive a live, GPU-backed session from your own Python process on your local machine. You call the operations, and SageMaker AI runs them on managed accelerators loaded with your chosen base model plus your Low-Rank Adaptation (LoRA) adapter. There’s no config file describing the whole job up front and no cluster creation step. You control what happens at each step, interactively, from code, so you can iterate and debug quickly.
The division of responsibilities looks like this:
The API is organized around three clients in the SageMaker Python SDK, created in sequence. A ServiceClient holds the platform-level settings (execution role, model package group, Amazon Simple Storage Service (Amazon S3) output location, and optionally an AWS Key Management Service (AWS KMS) key and virtual private cloud (VPC) configuration, which you can also override per session) and starts a session. The ServiceClient instantiates a TrainingClient (training and checkpointing operations such as forward, forward_backward, optim_step, and save_weights_for_sampler), which in turn instantiates a SamplingClient (sample and compute_logprobs, for generation and scoring during rollouts and evaluation). Each API call maps to one operation in your loop. An active session also serves an OpenAI-compatible chat completions endpoint, so existing OpenAI client code can sample from it.
For reinforcement learning, the loop has a characteristic shape. The following figure shows one training step and where each part runs: the steps in green call APIs on service-managed GPUs, and the steps in purple, your loop control and reward logic, run on your machine.
Each step loads a batch of prompts and (1) samples from the current model on the GPU. Your Python code then (2) scores those outputs: a verifier, a reward-model call, a test harness, anything you can express in code. (3) forward_backward and optim_step turn the scores into a gradient update on the GPU, and (4) save_weights_and_get_sampling_client() refreshes the sampler so the next step draws from the updated model.
You own the data, the loop control, and the reward; SageMaker AI runs the GPU-bound sampling, gradient, and checkpoint operations. The same primitives cover supervised fine-tuning (SFT) and other LLM training techniques. For SFT, drop the sampling and reward steps and call forward_backward with a cross_entropy loss over labeled examples.
Who is this for and where does it fit within Amazon SageMaker AI?
Training session APIs are the right starting point when you need fast iteration cycles and algorithmic freedom, such as a custom loss, a new RL reward signal, or a multi-stage pipeline, but don’t want to provision or operate GPU infrastructure yourself.
Usage is billed per token processed, so you’re charged only for the compute your loop consumes. If your reward function takes 10 seconds to score a batch on your machine, no GPU time is billed while it runs. Compared with hourly GPU billing, this has two practical advantages. First, there’s no idle-GPU cost: reward computation, data loading, logging, and debugging happen off the clock, and you’re billed only when you call a GPU-bound operation. Second, cost scales with your dataset and generation volume, not with wall-clock time or cluster size, which makes spend easier to forecast and experiments easier to compare. The savings over reserving GPUs for the full session can be significant for workloads with heavy local computation, such as complex reward models, multi-tool agentic rollouts, or human-in-the-loop evaluation.
Training session APIs are built for teams whose work is defined by the training algorithm, not only the dataset. Because you compose the loop yourself, the same primitives support supervised fine-tuning (SFT) with a cross_entropy loss over labeled data, reinforcement learning with ppo, importance_sampling, or cispo (GRPO, PPO, and other group-relative methods), and custom objectives, such as preference optimization or distillation, built from the same pieces. They fit:
- Post-training and alignment researchers implementing RL methods (GRPO, PPO, importance-sampling variants), custom advantage estimators, or new objectives.
- Teams doing supervised fine-tuning or preference optimization who need a non-standard loss, a data curriculum, or a multi-stage pipeline that config-driven recipes don’t express.
- Agentic and multi-turn RL builders who need custom rollout logic, reward shaping, and curricula.
- Machine learning (ML) engineers who’ve outgrown config-driven fine-tuning but don’t want to own the operational burden of GPU clusters.
- Researchers porting existing training-loop code, since the operation-based programming model maps directly onto loops written against low-level forward_backward, optim_step, and sample APIs.
The supported base models and the AWS Regions where each is available are listed in the training session APIs documentation.
Where training session APIs fit within Amazon SageMaker AI
Training session APIs sit at a distinct point among the model customization options in SageMaker AI: substantially more control over the training algorithm than fully managed Serverless Model Customization, and far less operational ownership than training on Amazon SageMaker Training Jobs or Amazon SageMaker HyperPod.
Anatomy of a training loop: GRPO on math problems
This section takes apart a minimal reinforcement learning loop to show how the operations fit together. The task is GSM8K, a benchmark of roughly 8,500 grade-school math word problems, each with a single numeric answer, as in the following example:
        Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? → 72
We train a LoRA adapter for OpenAI’s GPT-OSS 20B with Group Relative Policy Optimization (GRPO): for each question the model generates several responses, each response is scored for correctness, and responses that beat the group’s average are reinforced. The complete, runnable example is in the Amazon SageMaker examples repository.
Before you open a session, complete the prerequisites in the documentation.
Open a session
Create a session, then get the tokenizer and a SamplingClient from it:
Define the reward and the advantage
The task-specific logic is two short functions that run on your machine:
The loop
Each step follows the four stages shown in Figure 2. draw, build_prompt, and build_training_datum are short helpers in the sample:
Three details make this loop work:
Operations return futures. Every GPU-bound call returns an APIFuture immediately: the request is queued and sent by a background submitter, and .result() waits for the value. The loop submits all of a step’s sampling requests before waiting on any of them, so the whole batch generates concurrently. Training operations run in the order you call them, so optim_step can be submitted before forward_backward has finished.
The datum carries everything the loss needs. build_training_datum packs the prompt and response tokens, the per-token logprobs from sample(), the advantage, and a weights mask that keeps the prompt out of the loss.
Checkpoints are model packages. Every save registers a version in your model package group, including the per-step sampler refresh in the loop above. After training, two more saves add a merged model for deployment and a resumable state with weights and optimizer.
To resume, start a new session from the latest checkpoint with create_training_client_from_state_with_optimizer.
A running session counts against your concurrent-session quota until you call stop() or it expires, so stop it when you finish, including in error paths, or open the client in a with block. The merged checkpoint deploys to a real-time endpoint. To serve checkpoints as LoRA adapters instead, see the cookbook’s deployment notebook.
In our run of the sample, 10 training steps on 40 problems took held-out accuracy from 56 percent to 75 percent.
A real-world workload: RL on competitive programming
GSM8K keeps the mechanics visible, but a production RL workload adds more: longer generations, multi-turn interaction, an external grader, and enough throughput to keep the GPUs busy. The SageMaker training sessions cookbook packages that engineering into reusable training loops built on the same operations. For a new RL task you write an environment: what the model sees, how its answer is scored, and whether it gets another turn. The cookbook handles batching, chat templates, advantage estimation, overlapped sampling and training, validation, checkpointing with resume, and per-step metrics, and records each run’s configuration so it can be repeated. The code_rl recipe uses it to train a model on competitive programming problems.
The task. Problems come from the DeepCoder dataset (PrimeIntellect, TACO, and LiveCodeBench for training; Codeforces and LiveCodeBench for testing). The model writes a Python solution, which runs against the problem’s unit tests in a SandboxFusion container on your machine. The reward is 1 when all tests pass and 0 otherwise, with a 0.1 penalty when the response contains no code block.
Multi-turn tool use. With two turns, the model can call a check_solution tool, read the test results, and revise its answer before the final grade. The tool calls and results are rendered in the model’s native chat format, so the model is trained on the same token format it uses at inference.
What the recipe adds to the minimal loop:
- Overlapped sampling and training: Rollout workers keep generating while the trainer runs a step. A group of responses sampled from an older policy is used if it’s at most k steps old and requeued otherwise, and the cispo loss corrects for the policy difference.
- Streamed gradient computation: forward_backward is submitted in sub-batches as groups finish, instead of once per step.
- Held-out validation, checkpoint resume, and per-step metrics, optionally published to SageMaker managed MLflow.
We trained a LoRA adapter (rank 32) for GPT-OSS 20B for 50 steps, each with 128 problems and 8 responses per problem, using two turns and a staleness bound of k=3. Training reward rose from 0.46 to 0.60, and accuracy on 200 held-out test problems rose from 40 percent to 50.5 percent.
To run it, start the sandbox and launch the recipe:
The cookbook has more recipes on the same structure including supervised fine-tuning on chat datasets (Tulu 3, UltraChat), RL on GSM8K at full scale, and KTO preference alignment from binary feedback. Each recipe README lists its commands, hyperparameters, and expected metrics.
Conclusion
SageMaker AI training session APIs move the abstraction boundary down to the training operation: you write the training loop in Python on your own machine, and the service runs it on managed GPUs, handling model and LoRA loading, distributed execution, fault recovery, and checkpointing. A complete GRPO loop comes down to four operations, sample, forward_backward, optim_step, and save_weights_and_get_sampling_client, with the reward and advantage logic in your own code. The same operations scale to multi-turn, tool-using RL with sandboxed grading, as the Code RL recipe shows.
Custom rewards, agentic rollouts, step-by-step debugging, and new published techniques all use the same programming model: the algorithm stays in your loop, and SageMaker AI runs the GPUs.
To get started:
- Pick a recipe from the SageMaker training sessions cookbook, such as Code RL.
- Run the GSM8K example from the Amazon SageMaker examples repository and swap in your own reward function.
- Read the training session APIs documentation for prerequisites, quotas, Regions, supported models, and the API reference.
Acknowledgements
Thanks to Arun Nagarajan, Xichao Wang, and Shruti Sharma for their contributions and guidance for this post.
