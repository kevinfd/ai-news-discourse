---
id: "75632769443e0e3d"
title: "[Paper] FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention"
url: "https://reddit.com/r/LocalLLaMA/comments/1xasztg/paper_flashmask3_efficient_and_expressive"
link: "https://reddit.com/r/LocalLLaMA/comments/1xasztg/paper_flashmask3_efficient_and_expressive"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T14:02:52Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Long-context training of large language and multimodal models couples structured attention masks (document, prefix-LM, share-question, sliding-window, block-sparse) with multi-node context parallelism, making the mask a dominant bottleneck. FlashMask's column-wise sparse mask compresses them from O(n2) to O(n) via four query-axis boundary vectors, covering broad structured patterns. Implemented…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure", "business & funding"]
content_source: "post"
word_count: 240
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xasztg/paper_flashmask3_efficient_and_expressive/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention

Reddit · pmttyji · 2026-10-20

Long-context training of large language and multimodal models couples structured attention masks (document, prefix-LM, share-question, sliding-window, block-sparse) with multi-node context parallelism, making the mask a dominant bottleneck. FlashMask's column-wise sparse mask compresses them from O(n2) to O(n) via four query-axis boundary vectors, covering broad structured patterns. Implemented for Ampere GPUs, it neither exploits FlashAttention-3's TMA/WGMMA warp-specialized pipeline on Hopper nor supports distribution. The column-wise sparse mask is indexed by key positions but stores query-axis interval boundaries. Under any multi-chunk context-parallel assignment, it reduces per-rank mask localization to a provably zero-communication \emph{clip--shift--max} on the boundary vectors, compatible with the single-GPU kernel. FlashMask-3 introduces a mask-aware Hopper kernel with three-role warp specialization atop FlashAttention-3's TMA/WGMMA pipeline, plus a mask-aware distributed extension: zero-communication mask localization, a sparsity-aware load balancer (HCC-IPO), and a mask-aware compute-communication overlap with mask-driven communication pruning, whose forward all-gather uses topology-aware hierarchical routing. On a single H100 across 12 masks at 4K--128K context, it improves achieved TFLOPs over FlashMask, FlexAttention, and MagiAttention by 45--141%, 34--71%, and 2--44%. At context-parallel degrees 4--32 with 8K sequence per device, it attains 31--75% compute-communication overlap efficiency and improves throughput over Megatron-Core CP ring, Megatron-Core CP all-gather, and MagiAttention by 1.80×--3.71×, 1.71×--2.92×, and 1.09×--1.46×. In end-to-end training of a 118B-A14B MoE at 128K on 128 H100 GPUs, it raises throughput by 7.3--11.0% over a Dual Chunk all-gather baseline, with attention forward+backward 24.5--44.9% faster. arXiv : https://arxiv.org/abs/2610.17901 PDF : https://arxiv.org/pdf/2610.17901 GitHub : https://github.com/PaddlePaddle/FlashMask Project : https://enigmatisms.github.io/flashmask-3/
