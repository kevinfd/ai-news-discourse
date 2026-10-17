---
id: "53162a5fc64dddbd"
title: "I don't get the qwen 3.8 flash next hype"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7uf15/i_dont_get_the_qwen_38_flash_next_hype"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7uf15/i_dont_get_the_qwen_38_flash_next_hype"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T22:48:28Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["wgaca2"]
language: "en"
summary: "My experience is based on running Qwen 3.8 Flash Next UD-Q4_K_XL on 4x 3090's Compared directly to Qwen 3.8 27b Q8 it is not even close. To add to this, strata results were even worse than llama.cpp even thought generation speeds were faster. I left 1 run for 4 hours in strata and it did not produce a playable exe. After that all runs were capped per 1 hour on the first prompt As you can see…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 254
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7uf15/i_dont_get_the_qwen_38_flash_next_hype/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I don't get the qwen 3.8 flash next hype

Reddit · wgaca2 · 2026-10-16

My experience is based on running Qwen 3.8 Flash Next UD-Q4_K_XL on 4x 3090's Compared directly to Qwen 3.8 27b Q8 it is not even close. To add to this, strata results were even worse than llama.cpp even thought generation speeds were faster. I left 1 run for 4 hours in strata and it did not produce a playable exe. After that all runs were capped per 1 hour on the first prompt As you can see there were 2 bugs in the 27b 1st prompt completion. It fixed both of them on it's own during the second prompt. The bugs were: Gameplay controls still worked while paused. Gameplay controls still worked after game over. The local prompts are running through deepseek's harness. I am not showing screenshots of the output game as it is mostly the same from all models with slight visual differences and that is not really the point here. Exact prompts: Prompt 1: Build a Windows Tetris game with keyboard controls, scoring, increasing difficulty, and pause/restart. Deliver a standalone .exe that runs without installation. Prompt 2: Add local two-player mode with side-by-side boards and separate controls (WASD and arrow keys). The last player standing wins. Deliver the updated standalone .exe. And yes, i realize that comparing q8 model to q4 model is stupid, but so many people here claim that qwen 3.8 fn even at q3 is better than the 27b model (or at least as good) and so fast and good with strata that i had to check it.
