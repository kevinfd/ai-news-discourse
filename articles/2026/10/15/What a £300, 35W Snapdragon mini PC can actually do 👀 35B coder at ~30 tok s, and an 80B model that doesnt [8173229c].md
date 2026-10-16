---
id: "8173229c6e0cdb6c"
title: "What a £300, 35W Snapdragon mini PC can actually do 👀: 35B coder at ~30 tok/s, and an 80B model that doesnt even fit in RAM running at 17 tok/s"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6stod/what_a_300_35w_snapdragon_mini_pc_can_actually_do"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6stod/what_a_300_35w_snapdragon_mini_pc_can_actually_do"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T18:02:21Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["WorldlyAd7946"]
language: "en"
summary: "£299.99 Lenovo IdeaCentre Mini (Snapdragon X1-26-100, 32GB, CPU only): - Qwen3.6 35B A3B coder: reads ~118 tok/s, writes 24.5, ~30 with MTP - Qwen3-Next 80B A3B: 17-18 tok/s writes with MTP How I got here... So I bought one of these boxes to test if software at work would run on ARM Windows - and then it was sitting there, but I was sufficiently impressed for the price (including taxes), that i…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 474
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6stod/what_a_300_35w_snapdragon_mini_pc_can_actually_do/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# What a £300, 35W Snapdragon mini PC can actually do 👀: 35B coder at ~30 tok/s, and an 80B model that doesnt even fit in RAM running at 17 tok/s

Reddit · WorldlyAd7946 · 2026-10-15

£299.99 Lenovo IdeaCentre Mini (Snapdragon X1-26-100, 32GB, CPU only): - Qwen3.6 35B A3B coder: reads ~118 tok/s, writes 24.5, ~30 with MTP - Qwen3-Next 80B A3B: 17-18 tok/s writes with MTP How I got here... So I bought one of these boxes to test if software at work would run on ARM Windows - and then it was sitting there, but I was sufficiently impressed for the price (including taxes), that i decided in my ADHD fuelled boredom to buy one for myself to see if cheap ARM is actually usable for local models. The GPU is an Adreno X1-45 and nothing useful runs on it for LLMs yet, and so far the NPU just sits there, so this is all CPU... llama.cpp, 512 token prompt, 8 threads (read = prompt, write = generation): - coder (Q4_0 35b-a3b): read ~118, write 24.5, with MTP 29-33 - Gemma 26B: read 134, write 29.5, (need to test MTP, I've only had the box. Then I wanted to see how far I could push it. RAM is the wall on 32GB, so I went looking at the recently released Janas (github.com/prabanta-dev/janas). It keeps a RAM cache of the MoE experts and streams the rest off the NVMe, but its x86 only. So I re-coded it for ARM: NEON kernels for every quant format, i8mm, etc, (all tested bit exact against the scalar reference code, Windows ARM64 and Linux. Will submit it as PRs on GitHub soon.) Janas, same settings: - coder: read ~60, write 17.2, with MTP 29-31 - Gemma 26B: read 115, write 23.5, with MTP 32-34 - 80B: read (TBC as I don't trust my results), plain write 9.8, with MTP 17-18 llama.cpp still wins on read and plain write, but with MTP Janas matches or beats it, and it does it in a fraction of the RAM. I then squeezed the coder's expert cache to 12GB and it still wrote at 24 tok/s - so even a 16gb snapdragon could rin 35b-a3b 👀.. And this box runs an 80B that llama.cpp cant even load! Then I thought Id try connecting the two I had access to (mine and my work's dev box) together over USB4. Work in progress, will report back - but initial results are promising and I've had a 122b qwen running already - just working on streamlining my parallel experts build. I dunno about you guys and gals, I mean I don't have extensive experience with local LLMs and I certainly haven't played with ARM before but I found this pretty surprising, and not half bad for £300 with no GPU. Happy to test stuff on it when I get chance if anyone wants more numbers... But I can't see a cheaper way rn of getting 32gb of LPDDR5 rn, and only ~35ishW of power draw... Thoughts and feedback welcome 🙃👍
