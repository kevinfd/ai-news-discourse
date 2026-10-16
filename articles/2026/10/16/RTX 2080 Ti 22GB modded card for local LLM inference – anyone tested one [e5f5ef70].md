---
id: "e5f5ef7051be8fac"
title: "RTX 2080 Ti 22GB modded card for local LLM inference – anyone tested one?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x786l8/rtx_2080_ti_22gb_modded_card_for_local_llm"
link: "https://reddit.com/r/LocalLLaMA/comments/1x786l8/rtx_2080_ti_22gb_modded_card_for_local_llm"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T05:50:23Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Dave86ch"]
language: "en"
summary: "Title: I'm building a small local AI server to validate a project I've developed. The application currently runs Qwen 9B and the server will only be used for an initial pilot with a few users. I have to provide the hardware myself, so I'm trying to keep the initial investment as low as possible. I found these modified RTX 2080 Ti 22GB cards on Alibaba and I'm considering one as a cheap way to…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 281
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x786l8/rtx_2080_ti_22gb_modded_card_for_local_llm/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# RTX 2080 Ti 22GB modded card for local LLM inference – anyone tested one?

Reddit · Dave86ch · 2026-10-16

Title: I'm building a small local AI server to validate a project I've developed. The application currently runs Qwen 9B and the server will only be used for an initial pilot with a few users. I have to provide the hardware myself, so I'm trying to keep the initial investment as low as possible. I found these modified RTX 2080 Ti 22GB cards on Alibaba and I'm considering one as a cheap way to get >20GB of VRAM. Seller specifications: - RTX 2080 Ti - 22GB VRAM (modified from the original 11GB) - 352-bit memory bus - 14 Gbps memory - 250W TDP - 8+8 pin power - blower-style cooler The seller also sent me a stress-test video. nvidia-smi recognizes the cards as RTX 2080 Ti with 22,528 MiB VRAM. They are running gpu_burn at 100% utilization, around 200–245W and roughly 69–74°C. My main goal isn't gaming performance. I need reasonably reliable CUDA inference for Qwen 9B, probably quantized, with enough VRAM for a decent context/KV cache and a few concurrent users. I'm aware that these are unofficial VRAM-modified cards, so my concerns are: - Long-term reliability of the 22GB memory modification - CUDA / llama.cpp / Ollama / vLLM compatibility - Whether all 22GB is actually stable under LLM workloads - Driver or compute capability limitations from Turing - Whether buying one of these is worth the risk compared with paying significantly more for a 24GB RTX 3090 Has anyone here actually used a 22GB RTX 2080 Ti for LLM inference? If so, what models/runtime did you use and how stable has it been? For a low-budget pilot rather than a production server, would you consider this a reasonable compromise?
