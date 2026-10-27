---
id: "02d6eb57fd497014"
title: "Qwen3.8-27B Jetson Thor: 40 tok/s at FP16-level accuracy (INT4 + MTP + FlashHead)"
url: "https://embedl.com/Qwen/Qwen3.8-27B/thor?tab=run"
link: "https://embedl.com/Qwen/Qwen3.8-27B/thor?tab=run"
source: "Embedl"
domain: "embedl.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T17:56:51Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["No-Dragonfly6246"]
language: "en"
summary: "I'm on the team at Embedl that built this, and wanted to share the numbers. What's in it INT4 weights, using our own quantization, about half the error of standard AWQ FlashHead, our faster LM head: the 262k-vocab output layer is a real cost at batch 1, so it only scores the likely candidates MTP head for speculative decoding Port to TensorRT Edge-LLM (0.10.1) underneath Speed (batch 1,…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "summary"
word_count: 98
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg44nj/qwen3827b_jetson_thor_40_toks_at_fp16level/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8-27B Jetson Thor: 40 tok/s at FP16-level accuracy (INT4 + MTP + FlashHead)

Embedl · No-Dragonfly6246 · 2026-10-26

I'm on the team at Embedl that built this, and wanted to share the numbers. What's in it INT4 weights, using our own quantization, about half the error of standard AWQ FlashHead, our faster LM head: the 262k-vocab output layer is a real cost at batch 1, so it only scores the likely candidates MTP head for speculative decoding Port to TensorRT Edge-LLM (0.10.1) underneath Speed (batch 1, 2,048-token prompts from real OpenAssistant conversations, 128 out, greedy, average of 20 requests) Decode: 39.6 tok/s End-to-end: 23.6 tok/s Prompt processing: 926 tok/s Peak memory: 24.8 GiB Accuracy vs the…
