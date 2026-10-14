---
id: "6f6241bfe59928b6"
title: "PSA for 3090 FE owners: Running LLMs overheats your VRAM"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4z19k/psa_for_3090_fe_owners_running_llms_overheats"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T15:02:59Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Farmadupe"]
language: "en"
summary: "https://preview.redd.it/p6i9qifyy8vh1.png?width=2069&format=png&auto=webp&s=2b1e3c7c4fc95f12f0f7d417a4d21410aebfbd35 The 3090 Founders edition has a reputation for hot VRAM. Since LLM token generation maxes out VRAM's read capacity, I checked VRAM temps with Nvidia's stock fan/power curves and discovered that VRAM hits 112C within seconds of starting token generation. The VRAM chips are only…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "business & funding"]
content_source: "post"
word_count: 234
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4z19k/psa_for_3090_fe_owners_running_llms_overheats/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# PSA for 3090 FE owners: Running LLMs overheats your VRAM

Reddit · Farmadupe · 2026-10-13

https://preview.redd.it/p6i9qifyy8vh1.png?width=2069&format=png&auto=webp&s=2b1e3c7c4fc95f12f0f7d417a4d21410aebfbd35 The 3090 Founders edition has a reputation for hot VRAM. Since LLM token generation maxes out VRAM's read capacity, I checked VRAM temps with Nvidia's stock fan/power curves and discovered that VRAM hits 112C within seconds of starting token generation. The VRAM chips are only rated for 96C in continuous use. So I benchmarked just how much you have to reduce power before the VRAM comes back in spec, and how much it slows down TG, and whether an positive clock offset (ie undervolting) would help I used qwen3.8-27b 5.1bpw, generated with thireus-gguf-tool-suite , MTP head on with two tokens predicted. (so three tokens per forwardpass). (70% acceptance rate) Conclusions Cap your card 270W and manually set the fan to 100% to prevent VRAM from overheating (If you don't want your card to scream like a banshee, the cap at 70% fan is 240W). This loses 30% throughput. I didn't plot it, but If you don't manually set the fan, the nvidia stock curves will let the vram overheat Undervolting doesn't help, as Nvidia doesn't apply the clock offset at "low" power (it only kicks in a 300W and above when your VRAM is already overheating) If you're OK with 100C sustained temps, the power cap is 290W, 104C is 328W, and 353W gives you 108C. I didn't try with MTP off, but I think it would probably be worse Hope that helps!
