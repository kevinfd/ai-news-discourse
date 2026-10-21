---
id: "755680fbd7f2321f"
title: "Best VLLM setup for Qwen3.8 Flash Next on 2x5090 + 128GB of RAM?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbf4vp/best_vllm_setup_for_qwen38_flash_next_on_2x5090"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbf4vp/best_vllm_setup_for_qwen38_flash_next_on_2x5090"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T05:57:47Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["TooManyPascals"]
language: "en"
summary: "Hi all, I am running Qwen3.8-27B for a local setup with 2x5090s where the use case is mostly agentic programming. For this, VLLM is the only framework that does not trash the cache and allows for efficient use. I am currently using Qwen3.8-27B-INT6-Mixed-AutoRound from Minachist with pretty good results. But I am considering to try Flash Next on this rig, and while I've seen lots of discussions…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 124
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbf4vp/best_vllm_setup_for_qwen38_flash_next_on_2x5090/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Best VLLM setup for Qwen3.8 Flash Next on 2x5090 + 128GB of RAM?

Reddit · TooManyPascals · 2026-10-21

Hi all, I am running Qwen3.8-27B for a local setup with 2x5090s where the use case is mostly agentic programming. For this, VLLM is the only framework that does not trash the cache and allows for efficient use. I am currently using Qwen3.8-27B-INT6-Mixed-AutoRound from Minachist with pretty good results. But I am considering to try Flash Next on this rig, and while I've seen lots of discussions with different framewors, and many new vibe-coded ones, I haven't found a good balanced recipe for 2x5090s, flash-next and vllm. It seems pretty different to serve than Qwen3.8-27B where you fit everything on VRAM, so I'd like to know what are people doing. If you have experience with this kind of setup, could you share it? Thanks!
