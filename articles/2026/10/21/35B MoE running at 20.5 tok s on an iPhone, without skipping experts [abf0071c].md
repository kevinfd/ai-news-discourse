---
id: "abf0071c423d56ee"
title: "35B MoE running at 20.5 tok/s on an iPhone, without skipping experts"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbmsgf/35b_moe_running_at_205_toks_on_an_iphone_without"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbmsgf/35b_moe_running_at_205_toks_on_an_iphone_without"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T13:12:08Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["GasSmooth7439"]
language: "en"
summary: "I came across OpenBMB’s engineering write-up on running large MoE models locally, and the systems work behind it is worth highlighting. Instead of shrinking the model or skipping experts, they tackled the real bottleneck: getting expert weights from flash storage to computation fast enough. OpenBMB’s MiniCPM-V 4.7 uses a technique called Lookahead Expert Scheduling (LES) to run a 35B-A3B MoE…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 185
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbmsgf/35b_moe_running_at_205_toks_on_an_iphone_without/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 35B MoE running at 20.5 tok/s on an iPhone, without skipping experts

Reddit · GasSmooth7439 · 2026-10-21

I came across OpenBMB’s engineering write-up on running large MoE models locally, and the systems work behind it is worth highlighting. Instead of shrinking the model or skipping experts, they tackled the real bottleneck: getting expert weights from flash storage to computation fast enough. OpenBMB’s MiniCPM-V 4.7 uses a technique called Lookahead Expert Scheduling (LES) to run a 35B-A3B MoE model locally without changing its actual routing or dropping experts. The key idea: predict which experts the next layer might need, preload their weights from flash storage while current computations run, and execute ready experts first. Combined with optimized weight layouts, mixed-precision quantization, and DSpark speculative decoding, LES achieves: 20.51 tok/s on iPhone 18 Pro Max 6.07× faster than the 3.38 tok/s baseline 26.7% smaller expert weights with only a 0.16-point drop across five benchmarks Around 3 GB peak memory in a low-memory configuration The implementation, including expert scheduling and DSpark integration, is open source in llama.cpp-omni . The interesting part is that LES hides memory bottlenecks without changing which experts the model actually executes. This approach could potentially work with other MoE models, too.
