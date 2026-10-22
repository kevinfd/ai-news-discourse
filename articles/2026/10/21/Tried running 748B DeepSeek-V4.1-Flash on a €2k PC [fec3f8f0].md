---
id: "fec3f8f0dab00f96"
title: "Tried running 748B DeepSeek-V4.1-Flash on a €2k PC"
url: "https://reddit.com/r/LocalLLaMA/comments/1xburkx/tried_running_748b_deepseekv41flash_on_a_2k_pc"
link: "https://reddit.com/r/LocalLLaMA/comments/1xburkx/tried_running_748b_deepseekv41flash_on_a_2k_pc"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T18:11:28Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Vladowski"]
language: "en"
summary: "I bought a used PC with an RTX 3090 24 GB, 128 GB DDR4 and an Intel i9-9900X last year for under €2,000. With the release of DeepSeek-V4.1-Flash-1017 I decided to try running it on my machine. It is of course the smallest quant available (1-bit), but I was still happy to see it working at 7.2 tok/s . The answer has a physics error in it (wondering if someone can spot it), and I don't see much…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Alibaba", "Intel"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 208
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xburkx/tried_running_748b_deepseekv41flash_on_a_2k_pc/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tried running 748B DeepSeek-V4.1-Flash on a €2k PC

Reddit · Vladowski · 2026-10-21

I bought a used PC with an RTX 3090 24 GB, 128 GB DDR4 and an Intel i9-9900X last year for under €2,000. With the release of DeepSeek-V4.1-Flash-1017 I decided to try running it on my machine. It is of course the smallest quant available (1-bit), but I was still happy to see it working at 7.2 tok/s . The answer has a physics error in it (wondering if someone can spot it), and I don't see much practical use for it. Qwen models actually work pretty well on my setup. Still, it felt really nice to see a 748B parameter model running on such hardware. Here are some technical details: Unsloth UD-IQ1_S GGUF, 233 GB on disk llama.cpp built from the open PR #30817, CUDA 12.8 The 110 GB Engram table isn't loaded up front. It stays on the NVMe and only the rows the model needs are read on demand, which is how it fits. ​ llama-server -m DeepSeek-V4.1-Flash-1017-UD-IQ1_S-00001-of-00005.gguf \ -ngl 99 --n-cpu-moe 36 -ot "per_layer_token_embd.weight=CPU" \ -lm mmap -lzm on -t 10 -c 16384 --jinja \ --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \ --chat-template-kwargs '{"enable_thinking":false}' Now I only need to decide whether to keep the model or free up the disk space :)
