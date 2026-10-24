---
id: "fd09ced9a968ce5d"
title: "Swift-1.5 QFN iq2_xxs (strata, 64k ctx) vs Swift-1.5 27B q4_k_l (llama.cpp, 128k ctx)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdfy9c/swift15_qfn_iq2_xxs_strata_64k_ctx_vs_swift15_27b"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdfy9c/swift15_qfn_iq2_xxs_strata_64k_ctx_vs_swift15_27b"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T14:41:43Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["mailto_devnull"]
language: "en"
summary: "My daily driver: ukisai/Swift-1.5-Qwen3.8-27B-GGUF, Q4_K_L, 128k context, llama.cpp The model I want to switch to: ukisai/Swift-1.5-Qwen3.8-Flash-Next-GGUF, IQ2_XXS, 64k context, Strata I got pi to properly pass the thinking levels to QFN: \"thinkingLevelMap\": { \"off\": \"none\", \"minimal\": \"low\", \"low\": \"low\", \"medium\": \"medium\", \"high\": \"high\", \"xhigh\": \"high\", \"max\": \"high\" } So I set it to…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 227
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdfy9c/swift15_qfn_iq2_xxs_strata_64k_ctx_vs_swift15_27b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Swift-1.5 QFN iq2_xxs (strata, 64k ctx) vs Swift-1.5 27B q4_k_l (llama.cpp, 128k ctx)

Reddit · mailto_devnull · 2026-10-23

My daily driver: ukisai/Swift-1.5-Qwen3.8-27B-GGUF, Q4_K_L, 128k context, llama.cpp The model I want to switch to: ukisai/Swift-1.5-Qwen3.8-Flash-Next-GGUF, IQ2_XXS, 64k context, Strata I got pi to properly pass the thinking levels to QFN: "thinkingLevelMap": { "off": "none", "minimal": "low", "low": "low", "medium": "medium", "high": "high", "xhigh": "high", "max": "high" } So I set it to medium . I tried giving it a task for work and it just. wouldn't. code. — it spun endlessly thinking of just one more thing to check. The reasoning traces even had the hallmark "I've thought long enough, time to code the fix", followed by another round of discovery. Even with reasoning off , it would just spam tool calls instead of writing. So I gave up for now and booted up 27B again. It did some poking around, and started writing the fix a couple minutes later. Some potential causes: Strata set up a lower context (64k vs 128k), and so it was reasoning a lot and then compacting. Possibly medium is passed in but qwen still acts like xhigh with the second guessing. Swift-1.5 is supposed to prevent this kind of wheel spinning, but it's obviously not working. vs. llama.cpp, I have froggeric's template used which defaults to medium Also I'm using IQ2_XXS, so the low quant might be to blame. Maybe this is just what Qwen Flash Next is like. Thoughts?
