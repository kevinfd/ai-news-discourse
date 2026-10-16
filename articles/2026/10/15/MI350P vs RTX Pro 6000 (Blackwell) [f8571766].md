---
id: "f85717663625d379"
title: "MI350P vs RTX Pro 6000 (Blackwell)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x68fml/mi350p_vs_rtx_pro_6000_blackwell"
link: "https://reddit.com/r/LocalLLaMA/comments/1x68fml/mi350p_vs_rtx_pro_6000_blackwell"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T01:06:48Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Txt8aker"]
language: "en"
summary: "For anyone interested, I've been doing some kernel and tuning optimization for AMD because it was performing abysmal out of the box. But the effort was worth it as I was able to more than 2x its performance out of the box (the card is extremely new and there are almost no GEMM table and supports yet). (due to both using separate models and environmental factors input token can have ~3% less…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD", "Nvidia"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 430
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x68fml/mi350p_vs_rtx_pro_6000_blackwell/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# MI350P vs RTX Pro 6000 (Blackwell)

Reddit · Txt8aker · 2026-10-15

For anyone interested, I've been doing some kernel and tuning optimization for AMD because it was performing abysmal out of the box. But the effort was worth it as I was able to more than 2x its performance out of the box (the card is extremely new and there are almost no GEMM table and supports yet). (due to both using separate models and environmental factors input token can have ~3% less tokens for AMD to decode despite effort to keep them as close as possible). Just to keep things short and concise, I did a varying tests of small input c=8, medium input c=20, and long input c=1. Everything was done in cold state (no kv-cache at start). And I think there is more performance to unlock for MI350P as below benchmark was performed when I was only able to unlock 50% mem utilization (currently inference is still heavily bounded by compute because of missing GEMM tuning config) Model used: AMD: amd/Qwen3.8-27B-Quark-AWQ-MXFP4 Nvidia: unsloth/Qwen3.8-27B-NVFP4 (Small) 3k-input, 8 user comparison, 100 prompts AMD: Total input tokens: 288653 Total generated tokens: 75000 Nvidia: Total input tokens: 300000 Total generated tokens: 75000 AMD MI350P RTX Pro 6000 AMD vs RTX Output throughput 889 tok/s 596 tok/s 1.49x Time per output token (median) 7.2 ms 10.3 ms 1.42x faster Time to first token (median) 200 ms 392 ms 1.96x faster Draft tokens per step / accepted per step MTP 2 / 2.36 MTP 3 / 3.04 RTX accepts more per step but is still slower (AMD slowed down @ more than MTP 2) (Medium) 50k-input, 20 user comparison, 20 prompts AMD: Total input tokens: 965153 Total generated tokens: 10000 Nvidia: Total input tokens: 1000000 Total generated tokens: 10000 AMD MI350P RTX Pro 6000 AMD vs RTX Output throughput 130.6 tok/s 50.4 tok/s 2.59x Time per output token (median) 73.8 ms 182.7 ms 2.48x faster Time to first token (median) 34.5 s 97.2 s 2.81x faster Accepted tokens per step MTP 2 / 2.42 MTP 3 / 2.69 RTX accepts more per step but is still slower (Large) 200k-input, 1 user comparison, 5 prompts AMD Total input tokens: 962033 Total generated tokens: 25000 NVIDIA Total input tokens: 2000000 Total generated tokens: 25000 AMD MI350P RTX Pro 6000 AMD vs RTX Output throughput 79.8 tok/s 45.1 tok/s 1.77x Time per output token (median) 5.94 ms (about 168 tok/s) 8.02 ms (about 125 tok/s) 1.35x faster Time to first token (median) 34.3 s 70.5 s 2.05x faster Accepted tokens per step MTP 2 / 2.92 MTP 3 / 3.79 RTX gets 30% more tokens per step
