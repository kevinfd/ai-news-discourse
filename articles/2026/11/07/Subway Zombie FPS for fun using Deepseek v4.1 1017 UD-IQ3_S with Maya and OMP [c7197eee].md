---
id: "c7197eee8cdd8240"
title: "Subway Zombie FPS for fun using Deepseek v4.1 1017 UD-IQ3_S with Maya and OMP"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpyp07/subway_zombie_fps_for_fun_using_deepseek_v41_1017"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpyp07/subway_zombie_fps_for_fun_using_deepseek_v41_1017"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T05:38:22Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["MLDataScientist"]
language: "en"
summary: "inspired by Bijan Bowen's video - Subway FPS test . Hardware details: RTX 5090, 256GB DDR4 3200Mhz 8 channel, AMD EPYC 7532 CPU (32 core). Software: backend is Maya 1.1.55, harness is OMP v18.17.0. Model quant: Deepseek v4.1 1017 UD-IQ3_S latest UD3.1 quant from Unsloth. My prompt was very simple: I want you to create a single html file with a detailed subway station 3d scene, fps controls,…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: ["models & research"]
content_source: "post"
word_count: 157
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpyp07/subway_zombie_fps_for_fun_using_deepseek_v41_1017/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Subway Zombie FPS for fun using Deepseek v4.1 1017 UD-IQ3_S with Maya and OMP

Reddit · MLDataScientist · 2026-11-07

inspired by Bijan Bowen's video - Subway FPS test . Hardware details: RTX 5090, 256GB DDR4 3200Mhz 8 channel, AMD EPYC 7532 CPU (32 core). Software: backend is Maya 1.1.55, harness is OMP v18.17.0. Model quant: Deepseek v4.1 1017 UD-IQ3_S latest UD3.1 quant from Unsloth. My prompt was very simple: I want you to create a single html file with a detailed subway station 3d scene, fps controls, zombie enemies, tracers, recoil, muzzle flash, high details. build it with three.js You can see at the end of the video some token stats. In short, total generated tokens were 180k. The model ran at 30t/s with 2k t/s PP at 10k context but then went down to ~20 t/s near 180k context. Note that stock llama.cpp only reaches 10t/s TG and 120t/s PP. This model and harness tools are amazing. Just a year ago we could not even image having such a model locally. Yet, here we are!
