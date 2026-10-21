---
id: "eda1c638dd5e5a8b"
title: "Geezuz kernel: Qwen3.8-27B at 190 tok/s (620~ tok/s at 8 requests) on two 3090s"
url: "https://reddit.com/r/LocalLLaMA/comments/1xaslfk/geezuz_kernel_qwen3827b_at_190_toks_620_toks_at_8"
link: "https://reddit.com/r/LocalLLaMA/comments/1xaslfk/geezuz_kernel_qwen3827b_at_190_toks_620_toks_at_8"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T13:46:29Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["OhGeeLIVE"]
language: "en"
summary: "Geezuz, its fast! Qwen3.8-27B, two RTX 3090s power-limited to 280 W, plain PCIe, no NVLink, at 0 Context: (tests showing results with context are found on the next table) Requests Q4_K_M Q8_0 1 request 190 tok/s 143 tok/s 8 requests at once (total) 622 tok/s 610 tok/s llama.cpp's fastest two-GPU setup did about 100 tok/s on the same prompts. This did 164 on average and 214 on code, at the same…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 373
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xaslfk/geezuz_kernel_qwen3827b_at_190_toks_620_toks_at_8/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Geezuz kernel: Qwen3.8-27B at 190 tok/s (620~ tok/s at 8 requests) on two 3090s

Reddit · OhGeeLIVE · 2026-10-20

Geezuz, its fast! Qwen3.8-27B, two RTX 3090s power-limited to 280 W, plain PCIe, no NVLink, at 0 Context: (tests showing results with context are found on the next table) Requests Q4_K_M Q8_0 1 request 190 tok/s 143 tok/s 8 requests at once (total) 622 tok/s 610 tok/s llama.cpp's fastest two-GPU setup did about 100 tok/s on the same prompts. This did 164 on average and 214 on code, at the same output quality (KL divergence against llama.cpp). It's a fork of L-Forster's single-GPU megakernel from open-jet , where the whole forward pass runs as one persistent CUDA kernel. My fork splits it across two cards, which sync and exchange partial results directly over PCIe, and decodes up to 8 requests in one cycle with tensor-core paths for Q4_K, Q5_K, Q6_K and Q8_0. The model drafts its next tokens with its own MTP head, and verifying 5 drafted tokens costs almost the same as generating 1, because the weights are only read once per pass. Comes with an OpenAI-compatible server (shared KV pool, prefix cache) and a prebuilt tarball for RTX 30 cards. Compiling takes almost 60Gb of ram. And about 55 minutes on a 5800x CPU or around 30 minutes on a 9800x3d. Repo, every benchmark and the build-by-build changelog: https://github.com/ohgeebtw/geezuz-qwen3.8-27b-dual-gpu My next target for this week is beating vLLM at 8 parallel requests, where it still leads by about 15 %. Speed vs llama.cpp and vLLM (total tok/s, 2x RTX 3090 (280w), TP2, greedy, 4 MTP drafts, 512 tokens per request) Context, parallel requests Geezuz Q4_K_M llama.cpp Q4_K_M vLLM GPTQ int4 Geezuz Q8_0 llama.cpp Q8_0 vLLM FP8 10K, 1 159 95 104 124 87 88 10K, 2 235 160 243 213 150 223 10K, 4 389 254 404 355 223 396 10K, 8 550 312 576 519 324 595 60K, 1 143 91 113 119 93 103 60K, 2 195 134 208 193 119 188 60K, 4 289 181 323 284 159 doesn't fit llama.cpp b10246 (same GGUF, tensor split), vLLM 0.31.0. Same settings for all engines, none tuned. Measured on an earlier build with 8-bit KV on all three engines; fp16 KV run will follow soon. If you have a couple 4090s or 5090s, I would love to see your numbers!
