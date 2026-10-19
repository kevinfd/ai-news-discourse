---
id: "5891a90cc110226e"
title: "Qwen 3.8 Flash Next optimized for two CMP 170hx GPUs"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9iufz/qwen_38_flash_next_optimized_for_two_cmp_170hx"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9iufz/qwen_38_flash_next_optimized_for_two_cmp_170hx"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T00:29:52Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["dead-fish"]
language: "en"
summary: "I've been working on optimizing Qwen 3.8 Flash Next on my local setup with two CMP 170HX cards and finally got to a place where I feel like the results are worth sharing. Both cards are running over PCIe Gen2 x4 - no x16 mod or TP2. The setup uses the W4A16 AutoRound checkpoint, a patched vLLM, pipeline parallelism and native MTP speculative decoding. The n-gram table is memory-mapped from NVMe…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 250
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9iufz/qwen_38_flash_next_optimized_for_two_cmp_170hx/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen 3.8 Flash Next optimized for two CMP 170hx GPUs

Reddit · dead-fish · 2026-10-19

I've been working on optimizing Qwen 3.8 Flash Next on my local setup with two CMP 170HX cards and finally got to a place where I feel like the results are worth sharing. Both cards are running over PCIe Gen2 x4 - no x16 mod or TP2. The setup uses the W4A16 AutoRound checkpoint, a patched vLLM, pipeline parallelism and native MTP speculative decoding. The n-gram table is memory-mapped from NVMe but everything else fits on the two GPUs. Decode throughput by concurrency — aggregate tok/s, not per-user speed: Concurrent requests Code JSON Prose 1 226 198 157 2 363 320 212 4 560 537 385 8 840 873 567 At eight concurrent code requests, the measured per-request decode rate was 116 tok/s, with 231 ms to first token. A few other results: - 6,300–7,100 tok/s prefill on 4k–64k prompts; about 5,900 tok/s at 128k. - Prose decode held up from 158 tok/s at 4k context to 142 tok/s at 128k. - HumanEval: 157/164 (95.7%) and GSM8K: 1,271/1,319 (96.4%), both in chat mode with thinking off. - Uses a full 262,144-token window For throughput, I used the sparkDash protocol: greedy decoding, thinking off, fixed 400-token outputs, and medians of three runs, not the best run. The long-context decode checks are an addition to that protocol. This is faster than any published 2x CMP 170hx recipe I've found so I wanted to share with the community. These cards are flying :) Full recipe, pinned Docker image, patches, and detailed results: https://github.com/AlexBrandes/cmp170hx-qwen38-flash-next
