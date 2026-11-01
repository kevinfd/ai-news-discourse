---
id: "634f0c4d11e904ba"
title: "Please tell me Qwen3.8-Flash-Next can be made to be better than this"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkjrdl/please_tell_me_qwen38flashnext_can_be_made_to_be"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkjrdl/please_tell_me_qwen38flashnext_can_be_made_to_be"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T19:56:22Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["rm-rf-rm"]
language: "en"
summary: "I was quite excited with how well QFN did with some coding and adjacent tasks (like evaluating OSS repos, downloading and running models etc.). Using it for more general research is starting to show that it isnt actually very intelligent and gets lost in its own maze seemingly. Here's a recent example to a simple question: \"Have humans always slept for a huge amount of time at once, like eight…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 197
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkjrdl/please_tell_me_qwen38flashnext_can_be_made_to_be/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Please tell me Qwen3.8-Flash-Next can be made to be better than this

Reddit · rm-rf-rm · 2026-10-31

I was quite excited with how well QFN did with some coding and adjacent tasks (like evaluating OSS repos, downloading and running models etc.). Using it for more general research is starting to show that it isnt actually very intelligent and gets lost in its own maze seemingly. Here's a recent example to a simple question: "Have humans always slept for a huge amount of time at once, like eight hours at once, or been multiple sleep sessions through the day from like the early modern civilization?" The verbosity and dense way of writing is too much (feels like a lot of Opus 5 distillation) Setup: pi with pi-web-access extension llama.cpp, UD_Q4_K_M with MTP. --temp 1 --top-p 0.95 --top-k 20 --min-p 0.00 --presence-penalty 0 --repeat-penalty 1.0 Minimal AGENTS.md, mostly focused on sw related tasks Chat session: https://share.jotbird.com/radiant-bold-desert-wind TL;DR: forgetting the complexity of the first question, the responses to simple follow ups: "Are there logical inconsistencies inside your response?", "Why did this happen?" and "So how do we fix this so that it never happens again?" are** not only massive essays, but each "uncovers more" stuff. To the point I have lost faith in what QFN is saying**.
