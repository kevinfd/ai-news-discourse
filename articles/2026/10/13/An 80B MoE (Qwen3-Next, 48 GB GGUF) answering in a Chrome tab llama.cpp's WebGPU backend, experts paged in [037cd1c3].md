---
id: "037cd1c37cfbc590"
title: "An 80B MoE (Qwen3-Next, 48 GB GGUF) answering in a Chrome tab: llama.cpp's WebGPU backend, experts paged in from disk"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4xjuh/an_80b_moe_qwen3next_48_gb_gguf_answering_in_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T14:04:51Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["naklitechie"]
language: "en"
summary: "Follow-up to last week's post about streaming MoE experts from disk in a browser tab. That ran on hand-written engines for two models. This week the same disk tier sits under llama.cpp's own WebGPU backend, so it works for the MoE models llama.cpp already runs, with no per-model engine. The video is one real recording in Chrome. The sped-up parts say so on screen, with a real-time clock.…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 366
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4xjuh/an_80b_moe_qwen3next_48_gb_gguf_answering_in_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# An 80B MoE (Qwen3-Next, 48 GB GGUF) answering in a Chrome tab: llama.cpp's WebGPU backend, experts paged in from disk

Reddit · naklitechie · 2026-10-13

Follow-up to last week's post about streaming MoE experts from disk in a browser tab. That ran on hand-written engines for two models. This week the same disk tier sits under llama.cpp's own WebGPU backend, so it works for the MoE models llama.cpp already runs, with no per-model engine. The video is one real recording in Chrome. The sped-up parts say so on screen, with a real-time clock. Measured in that recording (MacBook Pro M4 Pro, 24 GB): Model (GGUF) File On the GPU Load from disk Decode Qwen3-Next 80B-A3B Q4_K_M 48.4 GB 4.89 GB 48 s 2.9 tok/s (proof of concept) OLMoE 1B-7B Q4_K_M 4.2 GB 3.92 GB 5.3 s 22.4 tok/s LFM2 8B-A1B Q4_K_M 5.0 GB 3.89 GB 6.2 s 17.1 tok/s Qwen3-30B-A3B runs too (14.7 GB file). How it works. The GGUF downloads once into the browser's private storage (OPFS). The GPU holds the dense layers, the KV cache and a fixed number of expert slots per layer, sized from a GPU memory budget you pick. At each MoE layer the router's picks are read back, and any expert not in a slot is read from the OPFS file (sync access handles in workers) into the least recently used slot. The paging is a small change to ggml-webgpu: a new buffer type, slot-mapped MUL_MAT_ID shaders, and the residency logic. Correctness. With paging on and off on the same backend, replies are identical (9/9 conversations on OLMoE and LFM2; on the two big ones, which do not fit unpaged, 8 vs 32 or 16 vs 64 slots give identical replies). Against llama.cpp on Metal, 4 to 8 of 9 replies match. The misses are WebGPU-vs-Metal rounding at near-ties: against llama.cpp's CPU backend, the WebGPU path is as close as Metal is. Limits. The 80B is slow: it reads about 359 MB from disk per token. Prompt processing is still slow (last week's fair complaint). Chrome or Edge 137+ only; tested on Apple silicon only. The first load copies the whole file into browser storage. The 80B model's own answer, asked how it could run in a browser tab: "It can't." It was running in a browser tab. Try it: https://diskformer.naklitechie.com · Code: https://github.com/NakliTechie/diskformer.js ·
