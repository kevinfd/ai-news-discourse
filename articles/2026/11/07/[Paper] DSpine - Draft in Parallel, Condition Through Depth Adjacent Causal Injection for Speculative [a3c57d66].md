---
id: "a3c57d66c8a9167a"
title: "[Paper] DSpine - Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding - tencent"
url: "https://reddit.com/r/LocalLLaMA/comments/1xq9hf6/paper_dspine_draft_in_parallel_condition_through"
link: "https://reddit.com/r/LocalLLaMA/comments/1xq9hf6/paper_dspine_draft_in_parallel_condition_through"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T15:48:50Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["pmttyji"]
language: "en"
summary: "Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the flow of predecessor information to successors. Our analysis of DFlash shows that early positions…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 222
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xq9hf6/paper_dspine_draft_in_parallel_condition_through/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] DSpine - Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding - tencent

Reddit · pmttyji · 2026-11-07

Parallel speculative drafting generates multiple candidates in one backbone pass, but independent token selection can produce inconsistent continuations that shorten the accepted prefix. Existing methods mostly leave conditional decoding to a lightweight module after the backbone, which limits the flow of predecessor information to successors. Our analysis of DFlash shows that early positions already form recoverable predictions in shallow layers, and that accurate adjacent predecessors help successors more when they enter earlier. We therefore propose DSpine, a drafter with causal conditioning injection throughout the backbone: at every layer, gated adjacent injection writes each predecessor's predicted feature into its successor, so the causal conditioning chain unfolds over network depth while all positions update in parallel. A unified transfer space built from the target model's output embeddings unifies layer-wise injection with predecessor-conditioned decoding, and layer-wise output-embedding supervision promotes the formation of predicted features in shallow layers. Fused kernels and a transition cache execute both efficiently in parallel within SGLang. Across seven math, code, and chat benchmarks, DSpine achieves the longest acceptance length at both temperatures on Qwen3-4B and Qwen3-8B. At temperature zero on Qwen3-8B, it raises the seven-benchmark mean from DFlash's 3.77 to 4.82 (+27.8%); in SGLang serving tests, it delivers 23.3% higher throughput than DFlash on average . arXiv : https://arxiv.org/abs/2609.36173 PDF : https://arxiv.org/pdf/2609.36173 GitHub : https://github.com/Tencent/DSpine HuggingFace : https://huggingface.co/collections/tencent/dspine Project : https://dspine-project.github.io/
