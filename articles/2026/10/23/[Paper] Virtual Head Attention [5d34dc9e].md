---
id: "5d34dc9ef4a151dc"
title: "[Paper] Virtual Head Attention"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdhzw3/paper_virtual_head_attention"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdhzw3/paper_virtual_head_attention"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T15:59:05Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["pmttyji"]
language: "en"
summary: "The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 303
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdhzw3/paper_virtual_head_attention/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] Virtual Head Attention

Reddit · pmttyji · 2026-10-23

The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill compute. We propose Virtual Head Attention (VHA), which simultaneously improves all three vertices through two lightweight linear operations: Q Premix applies a near-identity transformation to queries within each KV group to recover virtual head diversity from halved physical query heads, and Linear Postmix fuses inter-head features via a low-rank I+AB⊤ residual structure. Since VHA introduces no nonlinear operations, Premix can be folded into the query projection and Postmix into the output projection at inference time, reducing the model to a standard GQA-2 architecture that directly reuses all existing GQA inference optimizations. With only two KV heads, the group size in large models readily reaches 64, fully exploiting Tensor Core parallelism during decoding. Across four scales with 4K-context 50B-token pretraining, VHA consistently surpasses the standard GQA baseline at every scale (+0.05\% to +0.81\%), while reducing KV cache by 4× vs.\ GQA-8 at dense scales and 2× vs.\ GQA-4 at the MoE scale, and lowering training and prefill FLOPs by 7.9\% (1.7B, S=4096). On an industrial 30B-A3B MoE model trained on 500B tokens at 8K context, VHA outperforms both MLA and GQA-4 by +0.70\,/\,+2.60\,\% on a 12-benchmark base-model evaluation suite; in a separate matched 10B-A1B MoE comparison after long-context mid-training, VHA attains an average RULER score of 84.4 over 8K--128K versus 73.0 for GQA, while using two rather than four KV heads in the full-attention layers . Please read below items as above text's formatting is mess. arXiv : https://arxiv.org/abs/2610.17959 PDF : https://arxiv.org/pdf/2610.17959 GitHub : https://github.com/PaddlePaddle/VHA
