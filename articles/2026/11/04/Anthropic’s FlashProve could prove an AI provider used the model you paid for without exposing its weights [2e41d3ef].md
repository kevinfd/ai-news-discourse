---
id: "2e41d3eff70f7607"
title: "Anthropic’s FlashProve could prove an AI provider used the model you paid for without exposing its weights"
url: "https://interestingengineering.com/ai-robotics/anthropic-flashprove-cryptographic-model-verification"
link: "https://interestingengineering.com/ai-robotics/anthropic-flashprove-cryptographic-model-verification"
source: "Interesting Engineering"
domain: "interestingengineering.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T15:58:57Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Spirited-Sir-3034"]
language: "en"
summary: "Users currently have no independent way to confirm whether an AI provider served the requested model or quietly substituted a cheaper one. FlashProve addresses this by using zero-knowledge cryptography to prove that a particular model generated a response while keeping its proprietary weights hidden. Anthropic demonstrated the open-source system on a 400-billion-parameter model, generating…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Meta", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "policy & regulation", "business & funding"]
content_source: "fulltext"
word_count: 544
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xnrvak/anthropics_flashprove_could_prove_an_ai_provider/"
score: null
comments: null
community: "r/artificial"
---

# Anthropic’s FlashProve could prove an AI provider used the model you paid for without exposing its weights

Interesting Engineering · Spirited-Sir-3034 · 2026-11-04

Anthropic has unveiled FlashProve, an open-source cryptographic system designed to verify whether an AI model actually generated a response without revealing its proprietary weights. The technology could help users, independent auditors and regulators confirm that providers are running the models they claim to serve.
The system uses zero-knowledge cryptography to generate mathematical proofs that a specific model produced given output tokens in response to a particular prompt. This could address a growing trust problem as companies increasingly rely on third-party model providers and routing services to access advanced AI systems.
Today, users have no reliable way to establish whether a response came from the model they selected or whether a provider secretly substituted a cheaper alternative. FlashProve aims to provide that assurance without requiring users to access or independently run the model.
Cryptographic proofs verify outputs
FlashProve uses a cryptographic technique called a zero-knowledge succinct non-interactive argument of knowledge (zkSNARK). It allows a provider to demonstrate that a computation was performed correctly without revealing sensitive information about the underlying model.
The system works in two stages. First, the provider publishes a cryptographic commitment to its model weights, effectively creating a fingerprint of the exact model being used while keeping the weights private.
When a user submits a request, the provider can subsequently generate a proof that the committed model produced the corresponding output tokens. Anyone with the commitment, prompt and response can verify the proof without accessing the model weights.
More from AI and Robotics
See All
Anthropic demonstrated the approach using Llama 4 Maverick, a 400-billion-parameter mixture-of-experts model. Running on a single NVIDIA H100 GPU, FlashProve generated proofs at approximately 110 tokens per second, with each proof measuring around 19 MB for a 1,024-token request.
Verification takes approximately 17 seconds using a 24-core CPU, without requiring a GPU.
Security meets practical challenges
The technology could have applications beyond checking whether customers receive the model they selected. Anthropic believes cryptographic inference proofs could help detect tampering with model responses, support independent evaluations and give regulators a way to verify which models providers are serving.
For example, a company could require a provider to demonstrate that its cybersecurity software was examined by a particular model rather than a cheaper substitute. Regulators could also use such proofs to check whether providers are serving approved models or meeting certain commitments on AI development.
However, FlashProve remains a research prototype rather than a production-ready solution. Generating proofs requires substantially more computing resources than ordinary inference. Anthropic’s measurements show that the process takes approximately 70 to 95 times the GPU time required by vLLM, a widely used open-source inference engine.
The current system also supports contexts of up to 1,024 tokens and proves an integer version of the model under greedy decoding. It does not yet cover every floating-point or sampled inference result. Additionally, it hides model weights but not the model’s architecture.
Anthropic has released the system’s executable code, technical report, protocol specification and formal verification proofs under the Apache 2.0 licence. The company said the release is intended to encourage other researchers to build on the work and improve the technology.
The research represents an early step towards making model identity and response integrity independently verifiable, potentially giving users greater confidence in the systems powering their applications.
