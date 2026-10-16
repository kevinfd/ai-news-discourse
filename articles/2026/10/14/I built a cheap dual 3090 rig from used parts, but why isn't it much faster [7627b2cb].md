---
id: "7627b2cb9899de86"
title: "I built a cheap dual 3090 rig from used parts, but why isn't it much faster?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5mohk/i_built_a_cheap_dual_3090_rig_from_used_parts_but"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5mohk/i_built_a_cheap_dual_3090_rig_from_used_parts_but"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T09:25:21Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["jonejy"]
language: "en"
summary: "Hey everyone, I recently put together a local LLM machine using mostly second hand hardware. I wanted to experiment with local models for app development without spending a fortune on a new workstation. Here's the setup: • 2 x used RTX 3090 24GB • Ryzen 9 5950X • MSI B550 A PRO motherboard • 128GB DDR4 RAM • 2TB NVMe SSD • Corsair HX1200 PSU • Ubuntu 24.04 with a recent llama.cpp build Almost…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["chips & infrastructure", "models & research", "products & launches"]
content_source: "post"
word_count: 315
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5mohk/i_built_a_cheap_dual_3090_rig_from_used_parts_but/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built a cheap dual 3090 rig from used parts, but why isn't it much faster?

Reddit · jonejy · 2026-10-14

Hey everyone, I recently put together a local LLM machine using mostly second hand hardware. I wanted to experiment with local models for app development without spending a fortune on a new workstation. Here's the setup: • 2 x used RTX 3090 24GB • Ryzen 9 5950X • MSI B550 A PRO motherboard • 128GB DDR4 RAM • 2TB NVMe SSD • Corsair HX1200 PSU • Ubuntu 24.04 with a recent llama.cpp build Almost everything came from the used market. The first GPU runs at PCIe 4.0 x16, while the second is connected through a riser in the motherboard's PCI_E3 slot and runs at PCIe 3.0 x4. I installed the NVMe drive in the primary M.2 slot to keep the second GPU slot available. I've been testing Qwen3.6 35B A3B with different GGUF quantization levels and context sizes. Being able to load larger models is great, but the performance scaling hasn't been as straightforward as I expected. With quantizations that already fit on one 3090, adding the second card doesn't always help as much as I hoped. Longer contexts also make prefill take noticeably more time, and I'm still trying to separate the effects of KV cache usage, memory bandwidth and GPU communication. I haven't run a proper controlled benchmark yet, so I'm curious how much of this is down to my hardware layout and how much is just normal behavior with multi GPU inference. For everyday work I still use hosted tools like ChatGPT and Migoo, so I'm also trying to figure out which workloads are actually worth moving to local hardware rather than assuming everything should run on my own machine. For those running dual 3090s, what kind of tokens per second do you get with similar models, and which GPU split settings work best for you? Also, how do you systematically identify the bottleneck? I'd appreciate any benchmark tips or configuration advice.
