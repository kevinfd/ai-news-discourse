---
id: "39d6b28f08195ee2"
title: "Basalt: Fast Blackwell inference engine for Qwen 3.8 Flash Next (and how we got vision for free)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4xmxb/basalt_fast_blackwell_inference_engine_for_qwen"
link: "https://reddit.com/r/LocalLLaMA/comments/1x4xmxb/basalt_fast_blackwell_inference_engine_for_qwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T14:08:21Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["jesdga95"]
language: "en"
summary: "Dynamic vision, in action Basalt is an inference engine for 3.8 Flash Next, forked from Strata and heavily tuned for Blackwell. It supports vision, and for this to work you need to have the image encoder either in VRAM or CPU all the time, having it on VRAM takes valuable space from experts that would otherwise stay in the fast memory and CPU encoding is SLOW. After launch, u/rkfg_me brought up…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["products & launches"]
content_source: "post"
word_count: 197
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4xmxb/basalt_fast_blackwell_inference_engine_for_qwen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Basalt: Fast Blackwell inference engine for Qwen 3.8 Flash Next (and how we got vision for free)

Reddit · jesdga95 · 2026-10-13

Dynamic vision, in action Basalt is an inference engine for 3.8 Flash Next, forked from Strata and heavily tuned for Blackwell. It supports vision, and for this to work you need to have the image encoder either in VRAM or CPU all the time, having it on VRAM takes valuable space from experts that would otherwise stay in the fast memory and CPU encoding is SLOW. After launch, u/rkfg_me brought up a simple question: why keep it loaded at all? this was actually a great idea (thanks again!), so now basalt supports --vision dynamic : When idle the encoder lives in RAM, close to 0 VRAM used at load. When the image arrives, the engine uses some of the expert cache slots, uploads the encoder to VRAM (~30 ms) and encodes the image. When it's done the same slots get refilled from RAM (~60 ms). No image sent = free, no performance hit on text. The encoder uses Basalt's kernels, up to 3x as fast as llama.cpp's. Basalt repo: https://github.com/jesdga95/basalt ----- For DEVS: If you're interested to port this to your own engine, these are the commit hashes with the implementation (Basalt main branch): 9bfb90a, a704c65, efd23d9
