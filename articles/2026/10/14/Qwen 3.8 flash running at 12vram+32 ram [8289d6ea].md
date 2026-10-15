---
id: "8289d6ea4f84903b"
title: "Qwen 3.8 flash running at 12vram+32 ram"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5uvjf/qwen_38_flash_running_at_12vram32_ram"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T15:52:37Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Present_Resource4022"]
language: "en"
summary: "I finished putting my Gyro-M experimental setup on GitHub: https://github.com/Gitshop77/GyroStrata Original post : https://www.reddit.com/r/LocalLLM/s/4LmgejUQH4 Running full 256K context on a 4070 Super 12GB and 32GB RAM, getting around 950–1800 tok/s prefill and 30–38 tok/s output depending on context. Note that mtp and vision are off on purpose . they were affecting speeds in many test…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 214
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5uvjf/qwen_38_flash_running_at_12vram32_ram/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen 3.8 flash running at 12vram+32 ram

Reddit · Present_Resource4022 · 2026-10-14

I finished putting my Gyro-M experimental setup on GitHub: https://github.com/Gitshop77/GyroStrata Original post : https://www.reddit.com/r/LocalLLM/s/4LmgejUQH4 Running full 256K context on a 4070 Super 12GB and 32GB RAM, getting around 950–1800 tok/s prefill and 30–38 tok/s output depending on context. Note that mtp and vision are off on purpose . they were affecting speeds in many test trials. If you have 16vram you could possibly try using MTP. Includes the Strata patches, tuned settings, model downloader, installer and launcher. MTP and vision are off. Speeds depend heavily on your CPU, SSD, RAM speed and GPU bandwidth. Don’t Expect to get similar results Against my results initially Unless you have the exact specs of my system . There’s a prompt u can give to Codex/Claude Code/etc included to tune it for your own specs. All benchmarks and setup details are in the repo. Don’t expect guarantees of fast speeds . It’s a tight fit, and I’m not sure how you are supposed to send recipes for multi-component stuff . I know in DGX Sparks recipes you can just use the same exact config since it’s the same memory and bandwidth, same goes for dual 3090 recipes and etc . So I provided a prompt for a coding agent so hopefully it tunes it well for great speeds.
