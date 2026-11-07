---
id: "07d818390a9f9232"
title: "[Paper] D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding"
url: "https://reddit.com/r/LocalLLaMA/comments/1xq1y0y/paper_d3d_decoupled_diffusion_drafting_for"
link: "https://reddit.com/r/LocalLLaMA/comments/1xq1y0y/paper_d3d_decoupled_diffusion_drafting_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T09:00:23Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["pmttyji"]
language: "en"
summary: "Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 327
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xq1y0y/paper_d3d_decoupled_diffusion_drafting_for/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

Reddit · pmttyji · 2026-11-07

Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with auxiliary autoregressive supervision to achieve long accepted prefixes without target hidden states. This independence lets D3D draft successor blocks during verification in one packed pass, enabling asynchronous speculative decoding. We progressively prune layers according to their effect on acceptance length to reduce the cost of packed drafting. Removing five of 36 layers retains over 99% of mean acceptance length across three benchmarks with Qwen3-8B as the target. Across seven benchmarks, D3D averages 5.00× and 5.71× decoding speedup with Qwen3-8B and Qwen3-32B targets, compared with 4.03× and 3.67× for DFlash. On GSM8K with Qwen3-32B, speedup reaches 7.48× . arXiv : https://arxiv.org/abs/2611.06425 PDF : https://arxiv.org/pdf/2611.06425 GitHub : https://github.com/fudan-generative-vision/D3D 🤗 Model Zoo Browse the D3D collection → The D3D collection contains six Qwen3-derived draft checkpoints. These checkpoints are draft models , not replacements for their target models. p denotes pruning; 24D and 31D denote retained transformer-layer counts. Target verifier Draft family Layers D3D checkpoint Qwen3-8B 1.7B 28 D3D-1.7B-8B Qwen3-8B 8B 36 D3D-8B-8B Qwen3-8B Pruned 8B 31 D3D-31D-p8B-8B Qwen3-32B 1.7B 28 D3D-1.7B-32B Qwen3-32B 8B 36 D3D-8B-32B Qwen3-32B Pruned 1.7B 24 D3D-24D-p1.7B-32B 📚 Training Data All corpora use Open-PerfectBlend prompts. See each dataset card for generation settings, statistics, and download instructions. Released models and datasets are grouped in the D3D collection . Corpus Target Model Samples Dataset PerfectBlend: Qwen3.8-27B Thinking Qwen3.8-27B 1,417,675 PerfectBlend-Qwen3.8-27B-Thinking PerfectBlend: Qwen3-4B Thinking (Greedy) Qwen3-4B 1,420,909 PerfectBlend-Qwen3-4B-Thinking-Greedy PerfectBlend: Qwen3-4B NoThink (Greedy) Qwen3-4B 1,420,908 PerfectBlend-Qwen3-4B-NoThink-Greedy PerfectBlend: Qwen3-4B NoThink (Sampling) Qwen3-4B 1,420,909 PerfectBlend-Qwen3-4B-NoThink-Sampling PerfectBlend: Qwen3-8B NoThink (Greedy) Qwen3-8B 1,420,908 PerfectBlend-Qwen3-8B-NoThink-Greedy PerfectBlend: Qwen3-8B NoThink (Sampling) Qwen3-8B 1,420,909 PerfectBlend-Qwen3-8B-NoThink-Sampling PerfectBlend: Qwen3-32B NoThink (Sampling) Qwen3-32B 1,420,500 PerfectBlend-Qwen3-32B-NoThink-Sampling PerfectBlend: Gemma-4-12B-IT (Greedy) Gemma-4-12B-IT 1,420,898 PerfectBlend-Gemma-4-12B-IT-Greedy PerfectBlend: Gemma-4-31B-IT (Greedy) Gemma-4-31B-IT 1,420,903 PerfectBlend-Gemma-4-31B-IT-Greedy
