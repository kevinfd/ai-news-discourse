---
id: "ec886a92fa12a05a"
title: "Deploy frontier AI models on AWS Trainium with SGLang-Neuron"
url: "https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron"
link: "https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-12T22:03:34Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Alex Nails"]
language: "en"
summary: "Today, Amazon announced that SGLang-Neuron is publicly available and can be accessed through an AWS Deep Learning Container, released by RadixArk in collaboration with Annapurna Labs. With SGLang-Neuron, you can serve models and generate reinforcement learning (RL) rollouts with SGLang on AWS Trainium using the same SGLang interface you use today. Trainium is a portfolio of AWS AI chips that…"
tags: ["Advanced (300)", "Amazon EC2", "Announcements", "AWS Trainium"]
orgs: ["Amazon"]
topics: ["models & research", "chips & infrastructure", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 434
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Deploy frontier AI models on AWS Trainium with SGLang-Neuron

AWS Machine Learning Blog · Alex Nails · 2026-11-12

Artificial Intelligence
Deploy frontier AI models on AWS Trainium with SGLang-Neuron
Today, Amazon announced that SGLang-Neuron is publicly available and can be accessed through an AWS Deep Learning Container, released by RadixArk in collaboration with Annapurna Labs. With SGLang-Neuron, you can serve models and generate reinforcement learning (RL) rollouts with SGLang on AWS Trainium using the same SGLang interface you use today. Trainium is a portfolio of AWS AI chips that delivers strong economics for AI training and inference at scale. Now, running SGLang on Trainium follows the SGLang workflow you already know: you launch models through SGLang’s server interface and invoke the endpoint using the same generation APIs. Underneath that interface, SGLang-Neuron runs on native PyTorch. With its out-of-tree plugin design, Trainium support and SGLang core develop independently and iterate faster.
How SGLang runs on Trainium
SGLang-Neuron is an out-of-tree plugin that connects SGLang with AWS Trainium. Installing the plugin registers the neuron platform through SGLang’s plugin entry points, and setting SGLANG_PLATFORM=neuron selects it when the server starts. SGLang core continues to provide the API server, request lifecycle, RadixAttention, and prefix-cache bookkeeping. The plugin implements the Trainium-specific models, attention, mixture of experts (MoE), and the graph runner.
TorchNeuron registers Trainium as a native PyTorch device. SGLang-Neuron uses standard PyTorch operations for the model execution path and incorporates kernels written with the Neuron Kernel Interface (NKI) for performance. It compiles these operations and kernels into executable programs using torch.compile, which the graph runner prepares and executes during serving.
SGLang-Neuron also supports PD disaggregation. In this configuration, a prefill server computes the prompt KV cache and transfers it to a decode server using NIXL over Elastic Fabric Adapter (EFA). The decode server then generates the remaining tokens. Each server still uses SGLang’s scheduler and request lifecycle, while the plugin manages the Trainium execution and KV-cache transfer path.
Serving models on AWS Trainium using SGLang-Neuron
To follow this walkthrough, you use a Trainium3 Amazon Elastic Compute Cloud (Amazon EC2) instance with a pytorch-inference-sglang-neuronx container. Here are the steps:
- Start the container.
- Launch the SGLang model server inside the container.
- Send a request to the model server.
For additional information, please see the SGLang-Neuron getting started guide for setup instructions, and explore the repository documentation for supported models, features, and validated configurations.
Conclusion
SGLang-Neuron brings SGLang’s familiar serving workflow to AWS Trainium through native PyTorch. You can get started by launching the SGLang-Neuron container and following the quickstart to serve a supported model. Try it with your workloads, contribute through the project repository, and share feedback to help shape future model and feature support.
