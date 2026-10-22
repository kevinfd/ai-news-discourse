---
id: "9bcd271befb9ac2a"
title: "Cosmos3-Edge in under 8 GB: VLM out now, video gen and robot policy next."
url: "https://reddit.com/r/LocalLLaMA/comments/1xbph8w/cosmos3edge_in_under_8_gb_vlm_out_now_video_gen"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbph8w/cosmos3edge_in_under_8_gb_vlm_out_now_video_gen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T14:59:11Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["No-Dragonfly6246"]
language: "en"
summary: "Hey guys, posted about optimized Cosmos Reason 2 model here a few months ago. Wanted to share a build of the latest Cosmos3 model, with even more optimizations! Huggingface and Jetson AI Lab has no Orin Nano support for Cosmos3-Edge, because the BF16 stack doesn't fit in 8 GB. It now does, INT4 quantization, along with more optimizations for speed! Device Stack Decode tok/s Orin Nano Super 8 GB…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "policy & regulation"]
content_source: "post"
word_count: 168
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbph8w/cosmos3edge_in_under_8_gb_vlm_out_now_video_gen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Cosmos3-Edge in under 8 GB: VLM out now, video gen and robot policy next.

Reddit · No-Dragonfly6246 · 2026-10-21

Hey guys, posted about optimized Cosmos Reason 2 model here a few months ago. Wanted to share a build of the latest Cosmos3 model, with even more optimizations! Huggingface and Jetson AI Lab has no Orin Nano support for Cosmos3-Edge, because the BF16 stack doesn't fit in 8 GB. It now does, INT4 quantization, along with more optimizations for speed! Device Stack Decode tok/s Orin Nano Super 8 GB Optimized 152.5 AGX Thor 128 GB Optimized 207.8 AGX Orin 64 GB BF16 vLLM 44.1 AGX Thor 128 GB BF16 vLLM 68.2 Accuracy across five VLM benchmarks is maintained (from 65.56 to 65.20). Try it in the browser or serve it locally: https://embedl.com/nvidia/cosmos3-edge/orin-nano-super For now the VLM part of the model is published; diffusion and policy part is being added very soon! Optimized peak memory for the VLM is as low as 3.3 GB! Trying a new page for pre-compiled models, since Hugging Face doesn't really support them. Let me know if something is missing to make it useful!
