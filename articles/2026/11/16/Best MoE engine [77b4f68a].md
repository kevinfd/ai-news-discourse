---
id: "77b4f68a8ed7ce4e"
title: "Best MoE engine?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xy0d5o/best_moe_engine"
link: "https://reddit.com/r/LocalLLaMA/comments/1xy0d5o/best_moe_engine"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T20:31:36Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["HelixTitan"]
language: "en"
summary: "I had been using Strata for about a month, and it was such a huge improvement over llama.cpp for getting it running smoothly and quickly for hardware. Overtime though, I found that the model would often mistake its own context after a compaction and really overthink things. I just started using Basalt yesterday after being hesitant to switch and set up all my providers and harnesses. Turns out…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 156
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xy0d5o/best_moe_engine/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Best MoE engine?

Reddit · HelixTitan · 2026-11-16

I had been using Strata for about a month, and it was such a huge improvement over llama.cpp for getting it running smoothly and quickly for hardware. Overtime though, I found that the model would often mistake its own context after a compaction and really overthink things. I just started using Basalt yesterday after being hesitant to switch and set up all my providers and harnesses. Turns out Basalt runs even faster, is less error prone, and the reasoning is way more on point. If you run 1 GPU, and have the 100 GB+ of VRAM, RAM, and SSD storage, you will not be disappointed in performance. I mostly care about final output speed, and I was getting 70-110 tok/s on Strata, and Basalt I was getting 110-170 toks/s output. Couldn't be happier. Same Qwen3.8 FlashNext-ud-q4_k_xl, and the NVFP4 ones (of course basalted though) Anyone else have any other experiences with other similar engines like this?
