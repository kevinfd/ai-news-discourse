---
id: "418ae447f600fa7e"
title: "Announcing new ways to customize models with SageMaker AI, without managing GPUs"
url: "https://aws.amazon.com/blogs/machine-learning/announcing-new-ways-to-customize-models-with-sagemaker-ai-without-managing-gpus"
link: "https://aws.amazon.com/blogs/machine-learning/announcing-new-ways-to-customize-models-with-sagemaker-ai-without-managing-gpus"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-22T18:00:04Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Pooja Karadgi"]
language: "en"
summary: "Companies getting real results from AI aren’t only using foundation models (FMs) off the shelf. They’re customizing open-weight models using post-training techniques such as reinforcement learning. A model trained on your business context, product catalog, or clinical vocabulary will be more accurate for your task and cost less to run. When you build agents, your data, workflows, evaluations,…"
tags: ["Amazon SageMaker AI", "Announcements", "Intermediate (200)"]
orgs: ["Amazon", "Anthropic", "Microsoft"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 1031
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Announcing new ways to customize models with SageMaker AI, without managing GPUs

AWS Machine Learning Blog · Pooja Karadgi · 2026-10-22

Artificial Intelligence
Announcing new ways to customize models with SageMaker AI, without managing GPUs
Companies getting real results from AI aren’t only using foundation models (FMs) off the shelf. They’re customizing open-weight models using post-training techniques such as reinforcement learning. A model trained on your business context, product catalog, or clinical vocabulary will be more accurate for your task and cost less to run. When you build agents, your data, workflows, evaluations, and success criteria also shape how the model behaves.
However, model customization is difficult. You must choose the right technique, set up and manage GPU infrastructure, and, for agents, build environments for multi-turn reinforcement learning. We launched Amazon SageMaker AI serverless model customization to solve these challenges, and today, we’re expanding it with the general availability launch of training sessions.
With training sessions you get control over the post-training logic without managing the underlying infrastructure. You write and coordinate the training loop, including custom loss functions or reward signals. SageMaker AI handles GPU allocation, distributed execution, fault recovery, and checkpoint storage.
Customize without the hassles of infrastructure management
With SageMaker AI serverless model customization, you don’t choose instance types, manage clusters, or write distributed training configuration.
We didn’t want to limit you. You can use techniques such as SFT, DPO, RLVR, RLAIF, or multi-turn RL. You can choose how much of the model to update with Low-Rank Adaptation (LoRA) or full fine-tuning and chain techniques together through continuous customization.
We didn’t want you to waste time. Our SageMaker AI training sessions cookbook provides examples and use cases, along with model customization agent skills. You describe your use case, and the agent handles data prep, technique choice, training, evaluation, and deployment. The agent works where you work, in SageMaker Studio, Kiro, Claude Code, Codex, or GitHub Copilot.
        “We adopted SageMaker AI Serverless Training Sessions to build a healthcare claim-denial triage model, and the experience validated the platform from day one. The low-level API surface, direct control over the forward and backward passes, sampling, and the optimizer step gave our scientists the fine-grained control they need to pursue reinforcement learning on a demanding, accuracy-critical use case. Training Sessions gives us the right primitives to push toward production-grade performance.”
— Rob Gontarek, Senior Vice President, Data Science, ImagineSoftware
Write your own post-training loop
One important shift in agent training is toward multi-turn reinforcement learning. For example, an agent that books travel, triages support tickets, or runs a multi-step research task needs several rounds of interaction before you can judge whether it reached the right outcome.
However, the training loop can get complicated quickly. You may train the model on one set of infrastructure, run inference on another to generate responses, score those responses, and feed the results into the next update. Each stage needs different compute, and connecting them across separate tools and clusters adds work.
SageMaker AI already offers multi-turn RL as a managed, serverless technique. But we heard from customers who wanted to define their own loss functions, shape reward signals, or RL stages in one loop. Training sessions give you that flexibility.
        “With SageMaker AI Serverless Training Sessions, we fine-tuned gpt-oss-20b for agentic, multi-turn tool calling against our Amazon Neptune knowledge graph — and the platform handled the infrastructure for us. Setup just worked, with no manual tuning and no out-of-memory wrangling. Checkpoint-and-resume was a standout: resuming from an exact step was completely reliable. It gave our developers the flexibility they wanted while taking the operational burden off their plate.”
— Nitin Wagh, CEO, Karini AI
How it works
Your code runs the training loop and reward function in your environment and connects the agent to its tools or simulators. The training session performs the GPU-heavy work: a sampler generates responses, and a trainer calculates gradients and updates the model weights. The exact sequence depends on the algorithm you write.
For example, let’s look at Group Relative Policy Optimization (GRPO) implementation. GRPO is a reinforcement learning method that generates several responses to the same prompt, scores them, and uses their relative performance to update the model. One pass through the loop works like this:
- Sample responses – Your loop asks the sampler to generate several responses for each prompt using the current model.
- Score them – Your reward function scores each response in your environment using a verifier, reward model, or test harness.
- Update the model – Your loop sends the scores back to the trainer. forward_backward() uses them to calculate gradients, and optim_step() applies the update to the model weights.
- Refresh and repeat – Your loop asks the session to refresh the sampler with the updated weights, then starts the next batch. Your code repeats these steps until training is complete.
You pay for the tokens SageMaker AI processes. The meter stops while your reward function scores a batch in your environment, and there is no capacity to reserve.
Keep control of your data and models
Each session uses an AWS Identity and Access Management (IAM) execution role that you create, and you can add your own AWS Key Management Service (AWS KMS) key and virtual private cloud (VPC) configuration. Your data stays in your own Amazon Simple Storage Service (Amazon S3) buckets in the AWS Region that you choose, and your checkpoints land there too.
We don’t use your data or your customized weights to train another model. Before deployment, you can evaluate the model for accuracy, bias, and safety. After you deploy, you can apply guardrails and monitor it with Amazon CloudWatch.
You can keep using the governance processes your teams already have.
Get started today
Write your own training loop on SageMaker AI serverless model customization training sessions, available today with support for gpt-oss-20b, gemma-4-31B-it, Qwen3.6-27B, and Qwen3.8-27B.
Two ways to get started:
- In your IDE: Install the SageMaker Python SDK (on Linux or macOS with Python 3.10 to 3.12), clone the cookbook, and start developing.
- In SageMaker Studio: Launch a ready-to-use AI development environment in under 20 seconds. Sign in, open a notebook, connect your coding agent (Kiro, Claude Code, Codex, or Copilot), download the agent skills and cookbook, and you’re ready to begin.
Resources
Training sessions documentation
