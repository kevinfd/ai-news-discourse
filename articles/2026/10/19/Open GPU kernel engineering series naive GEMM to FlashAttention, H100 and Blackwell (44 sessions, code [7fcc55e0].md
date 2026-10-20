---
id: "7fcc55e07b9e48ee"
title: "Open GPU kernel engineering series: naive GEMM to FlashAttention, H100 and Blackwell (44 sessions, code public) [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xa4h2g/open_gpu_kernel_engineering_series_naive_gemm_to"
link: "https://reddit.com/r/MachineLearning/comments/1xa4h2g/open_gpu_kernel_engineering_series_naive_gemm_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T18:15:18Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Winter_Mistake_3185"]
language: "en"
summary: "I'm building a free, code-first series on GPU kernel engineering and just published the intro and roadmap video. It's my own channel, and I'm posting to share the resource and get feedback on the plan, not to sell anything. Video: https://youtu.be/cibk7G-jHQw The core idea behind the series: for most ML workloads, kernel performance is a data-movement problem before it's a compute problem. Two…"
tags: ["r/MachineLearning"]
orgs: ["DeepSeek"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 277
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xa4h2g/open_gpu_kernel_engineering_series_naive_gemm_to/"
score: null
comments: null
community: "r/MachineLearning"
---

# Open GPU kernel engineering series: naive GEMM to FlashAttention, H100 and Blackwell (44 sessions, code public) [P]

Reddit · Winter_Mistake_3185 · 2026-10-19

I'm building a free, code-first series on GPU kernel engineering and just published the intro and roadmap video. It's my own channel, and I'm posting to share the resource and get feedback on the plan, not to sell anything. Video: https://youtu.be/cibk7G-jHQw The core idea behind the series: for most ML workloads, kernel performance is a data-movement problem before it's a compute problem. Two things the series builds on throughout: - The roofline model. Attainable throughput is bounded by min(peak compute, memory bandwidth x arithmetic intensity), where arithmetic intensity is FLOPs per byte moved. A kernel's position relative to the ridge point tells you whether to optimize memory access or compute. - FlashAttention as the worked example. It computes exactly the same attention as the standard implementation. The gain comes from tiling so the full N x N score matrix is never written to HBM, which cuts memory traffic. We build it live. Roadmap (44 sessions): - Foundations: CPU parallelism, GPU architecture, roofline, first CUDA kernels - Memory hierarchy - GEMM: naive kernel to optimized, profiling at every step - Tensor cores - Profiling and debugging - PyTorch integration and Triton - Attention / FlashAttention - Hopper and Blackwell: TMA, WGMMA, CUTLASS, FP8/quantization, NVFP4, multi-GPU basics, FlashAttention 4, DeepSeek's kernels, AI-written kernels, capstone project Each session is concept, live code, profile, then a check that it actually got faster against a baseline. Prerequisites are C/C++, basic linear algebra, and PyTorch. Caveats: it's in progress, and the later sessions (especially Blackwell/NVFP4) may change as the tooling does. Feedback I'd find most useful: - If you've written production kernels, what do people usually get wrong that a course should cover?
