---
id: "e628a44b17595b6f"
title: "Does grammar-constrained decoding hurt small or quantized models?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xxrhm3/does_grammarconstrained_decoding_hurt_small_or"
link: "https://reddit.com/r/LocalLLaMA/comments/1xxrhm3/does_grammarconstrained_decoding_hurt_small_or"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T14:59:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["bye_ella"]
language: "en"
summary: "Asked about DSL vs JSON tool calls in r/LLMDevs a couple of days ago, and one answer kept coming up: for small models just use JSON, training volume matters. That got me thinking about the constraint itself. With GBNF or a JSON schema you can force any model to produce valid output, even a 3B at Q4. However, there was a paper a while ago showing that strict format restrictions can make reasoning…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 190
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xxrhm3/does_grammarconstrained_decoding_hurt_small_or/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Does grammar-constrained decoding hurt small or quantized models?

Reddit · bye_ella · 2026-11-16

Asked about DSL vs JSON tool calls in r/LLMDevs a couple of days ago, and one answer kept coming up: for small models just use JSON, training volume matters. That got me thinking about the constraint itself. With GBNF or a JSON schema you can force any model to produce valid output, even a 3B at Q4. However, there was a paper a while ago showing that strict format restrictions can make reasoning worse, since the model is forced away from the tokens it actually wanted Searched first: there’s the thread about grammar constraints sending Qwen3-VL into repetition loops, and the one on how quantization hits different capabilities, but nothing comparing accuracy with vs without constraints on small quants. So for people running small local models: have you measured accuracy with and without constraints on the same task? does it worsen at lower quants? does letting the model firstly think freely and constraining only the final answer fix most of it? Looking for real numbers or experience, not promoting anything. English isn’t my first language, so I used an LLM to help with the wording. Question and thoughts are mine.
