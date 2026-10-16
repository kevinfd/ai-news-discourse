---
id: "7cbf8a98b43c9e67"
title: "New model from Telperion: Qwen3.8-27B-MLA & Qwen3.8-27B-GLA-g2. 4x smaller KV cache, smarter, and more efficient reasoning."
url: "https://reddit.com/r/LocalLLaMA/comments/1x5wcnz/new_model_from_telperion_qwen3827bmla"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5wcnz/new_model_from_telperion_qwen3827bmla"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T16:47:46Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["fulgencio_batista"]
language: "en"
summary: "Hello! We've been busy at Telperion with a lot of experimental research (more coming soon). Today, we're announcing the release of our latent attention variants of Qwen3.8-27B. Our latent attention variants (quants calibrated to FP8 KV cache) compress the KV cache by 4×, enabling a near 4× increase in maximum context on consumer hardware or a near 4× increase in concurrency on server hardware.…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5wcnz/new_model_from_telperion_qwen3827bmla/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# New model from Telperion: Qwen3.8-27B-MLA & Qwen3.8-27B-GLA-g2. 4x smaller KV cache, smarter, and more efficient reasoning.

Reddit · fulgencio_batista · 2026-10-14

Hello! We've been busy at Telperion with a lot of experimental research (more coming soon). Today, we're announcing the release of our latent attention variants of Qwen3.8-27B. Our latent attention variants (quants calibrated to FP8 KV cache) compress the KV cache by 4×, enabling a near 4× increase in maximum context on consumer hardware or a near 4× increase in concurrency on server hardware. These variants demonstrate great performance, with a statistically distinguishable increase (+6.58%) in SWE performance on our MLA variant, in addition to using upwards of 20% fewer reasoning tokens. Due to the memory downsides of serving MLA on multi-GPU devices, we produced a grouped latent variant using two groups, enabling 4× KV compression for dual GPU users. Model SWE-bench Verified (zero-shot, toolless, n > 1500) Mean Output Tokens KV Compression (TP = 1, TP = 2) Qwen3.8-27B 39.5% — — Qwen3.8-27B-MLA 42.1% 0.88× 4.00×, 2.28× Qwen3.8-27B-GLA-g2 39.4% 0.86× 4.00×, 4.00× We have fantastic recipes for post-training quantization and have produced quantized versions that exceed equivalently sized .gguf quants in fidelity. Our models have an easy to install vLLM plugin . Quant Memory (including MTP head and vision encoder) Increase in top-1 disagreement (lower is better) BF16 55.7GB — FP8 31.5GB 0.06% INT4 22.9GB 0.17% EXL3-4.0bwp* 17.2GB 0.46% *EXL3 requires a custom vLLM plugin to run. The plugin has been verified on RTX PRO 6000s, H100s, and 2× RTX 5060Ti 16GB. We do not believe in gatekeeping ideas or research. As a result we will be open sourcing our method soon. This method requires zero-retraining, and is compatible with almost any model that uses grouped query attention or similar variants. Finally, we plan to make an improved version 2, with a full benchmark suite when we get more compute. We will also be making sparse latent attention variants of Qwen4-27B when released. What models would you like to see with latent attention? For those interested in following our research, learning/doing research, or getting on contact, feel free to join our discord server .
