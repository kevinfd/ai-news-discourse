---
id: "e12c66b83340cc6a"
title: "Qwen Flash Next on Mac Mini is runnable without maxing out your memory - results of different memory usage for ssd streaming"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8m9rg/qwen_flash_next_on_mac_mini_is_runnable_without"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8m9rg/qwen_flash_next_on_mac_mini_is_runnable_without"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T21:51:58Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["turtleninja99"]
language: "en"
summary: "This is from my recent side project to optimise inference of QFN (edit-q4) on a Mac Mini M5 64gb. I’ve known for a while it could be somewhat resilient to using less Gib, as the majority of the work is how to load experts from SSD into memory before they are needed. The prompt processing uses a carousel buffering system which very efficiently solves for the pp side of things and it was good to…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 291
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8m9rg/qwen_flash_next_on_mac_mini_is_runnable_without/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen Flash Next on Mac Mini is runnable without maxing out your memory - results of different memory usage for ssd streaming

Reddit · turtleninja99 · 2026-10-17

This is from my recent side project to optimise inference of QFN (edit-q4) on a Mac Mini M5 64gb. I’ve known for a while it could be somewhat resilient to using less Gib, as the majority of the work is how to load experts from SSD into memory before they are needed. The prompt processing uses a carousel buffering system which very efficiently solves for the pp side of things and it was good to see it hold up near perfectly even at lower amounts of experts hot cached. The decode uses a trained prediction lookahead model to more accurately fetch experts from SSD before they are needed. This has worked very well and actually got good gains but ultimately with less experts hot this is still gonna take longer to fetch all the experts. I do still feel like there’s unlocks here but they haven’t popped into my head. Practically speaking - For people doing stuff on their box besides hosting an LLM this is an insight into how much performance you give up for hosting X additional app e.g. ~29 tks decode at max, drop down 4gb and you’re at ~26tks. - If your workload has a lot of prompt processing and that’s what you care about you can really wind down the memory usage. - I found any less than ~18gib of non-LLM server space on the box resulted in some form of swap. Not a big deal in small amounts but something to avoid if possible. It sort of depends on how the other apps behave as well as swings in memory are more where swap happens from what I’ve observed from how Mac reacts. https://github.com/skeggsguy/Flash-next-ssd Edit: I probably should say this is running Unsloth's UD-Q4_K_XL quant.
