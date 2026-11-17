---
id: "b58188404b4b6c5f"
title: "MoE Offloading update Exllamav3 on 9070XT"
url: "https://reddit.com/r/LocalLLaMA/comments/1xyhrnn/moe_offloading_update_exllamav3_on_9070xt"
link: "https://reddit.com/r/LocalLLaMA/comments/1xyhrnn/moe_offloading_update_exllamav3_on_9070xt"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:10:49Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["willeyh"]
language: "en"
summary: "This is a follow up on https://www.reddit.com/r/LocalLLaMA/comments/1xun15v/moe_and_expert_offloading_on_llama_exllamav3/ While we wait for Qwen 4, here is Qwen 3.6 35B A3B at Q4 on 9070XT 16GB with offloaded experts on DDR4 3200Mhz ram. I've been tinkering still with the config for experts offloading and found substantial gains from my previous post. While decode stayed roughly in line fro last…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 216
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyhrnn/moe_offloading_update_exllamav3_on_9070xt/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# MoE Offloading update Exllamav3 on 9070XT

Reddit · willeyh · 2026-11-17

This is a follow up on https://www.reddit.com/r/LocalLLaMA/comments/1xun15v/moe_and_expert_offloading_on_llama_exllamav3/ While we wait for Qwen 4, here is Qwen 3.6 35B A3B at Q4 on 9070XT 16GB with offloaded experts on DDR4 3200Mhz ram. I've been tinkering still with the config for experts offloading and found substantial gains from my previous post. While decode stayed roughly in line fro last time, increasing chunk size to 5120 saw prefill over 2000 t/s at all context lengths, topping at 2606 t/s @ 32K. From ~1300t/s GPU utilization increases with batch size as it allows for more parallel processing. I saw no gains over 5120. TabbyAPI's documented ideal range is 512–4096, so your miles might vary. Exllama flags like cpu_threads 6 also made a small improvement in decode. Swizzle, gdn_sub, bg_gdn and wide flags were all regressions. (only tested isolated 1by1). cpu_moe_pinned_arena caused some core dumps, and the one run I managed to complete had a small gain. Vision have been turned off and offloaded. I still have not found an .exl3 quant for the Coder version of Qwen 3.8 Flash Next, and the qfn version I can run leaves me with 8K context with almost no vram or system ram left to spare. Results and more graphs and tables are at https://github.com/willeyh-git/moe-offload-bench All engines were compiled for ROCm on my system.
