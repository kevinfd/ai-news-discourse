---
id: "2db6552d4ef02522"
title: "[Paper] MemT-1.0: Towards Memory-Native Evolution"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbl751/paper_memt10_towards_memorynative_evolution"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbl751/paper_memt10_towards_memorynative_evolution"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T12:00:06Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 197
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbl751/paper_memt10_towards_memorynative_evolution/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] MemT-1.0: Towards Memory-Native Evolution

Reddit · pmttyji · 2026-10-21

Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We further introduce Mixture-of-Storage to scale native memory capacity. Following a deliberate backbone preparation, we develop a two-stage training pipeline consisting of continued pre-training and post-training, supported by 34B tokens of training data and efficient training and inference infrastructure. We release a model family comprising MemT-1.0-Nano and MemT-1.0-Flash, and conduct a comprehensive evaluation of memory and general capabilities. The results show that they outperform the parametric memory baselines on average and remain competitive with retrieval-augmented methods, while largely preserving general capabilities. At a history length of 128K tokens, MemT-1.0-Nano achieves approximately 1.86× end-to-end inference speedup and a 66× reduction in persistent storage relative to full context KV cache . By internalizing retrieved procedural experience, MemT-1.0 improves task success on agentic tasks, providing a practical step toward memory-native evolution. arXiv : https://arxiv.org/abs/2610.26825 PDF : https://arxiv.org/pdf/2610.26825 GitHub : https://github.com/MemTensor/MemT-1.0 HuggingFace : https://huggingface.co/collections/MemTensor/memt-1
