---
id: "e17e045c673adcde"
title: "Ways to reduce frequent compaction on larger projects?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5uhme/ways_to_reduce_frequent_compaction_on_larger"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5uhme/ways_to_reduce_frequent_compaction_on_larger"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T15:37:37Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["OuterKey"]
language: "en"
summary: "I'm using Qwen 3.8 27B on an R9700 and it works great, occasionally I'll switch to Tiel-coder for rapid simple tasks. One big problem I run into that makes real projects come to a halt is that more code takes up more context, compaction becomes more and more frequent between any edits, until it gets stuck in a compaction loop not doing any useful work. I started using Q4_K_XL and Q8 kv cache,…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: []
content_source: "post"
word_count: 170
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5uhme/ways_to_reduce_frequent_compaction_on_larger/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ways to reduce frequent compaction on larger projects?

Reddit · OuterKey · 2026-10-14

I'm using Qwen 3.8 27B on an R9700 and it works great, occasionally I'll switch to Tiel-coder for rapid simple tasks. One big problem I run into that makes real projects come to a halt is that more code takes up more context, compaction becomes more and more frequent between any edits, until it gets stuck in a compaction loop not doing any useful work. I started using Q4_K_XL and Q8 kv cache, for a context of 200k tokens, which helps from my normal 100-150k, but is there a technique to ensure it works efficiently? One idea I have but never fully enforced is having the code indexed (function signatures with comments and line numbers, structs shown in full so it doesn't need a read, maybe methods listed under structs.) Or another way is to make the code extremely modular so the LLM will have a very narrow focus. I tried this but it becomes very cumbersome because other modules will also need changed, probably until each becomes mature enough?
