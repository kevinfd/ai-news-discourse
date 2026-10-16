---
id: "b7f6f503206b41b5"
title: "Quartermaster 1.7 update now lets you run llama.cpp's new decision models (/v1/systemone) with a playground tab"
url: "https://reddit.com/r/LocalLLaMA/comments/1x53ob3/quartermaster_17_update_now_lets_you_run"
link: "https://reddit.com/r/LocalLLaMA/comments/1x53ob3/quartermaster_17_update_now_lets_you_run"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T17:54:13Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["OneMoreName1"]
language: "en"
summary: "Quartermaster (my local inference manager: one server that swaps llama.cpp, image, audio and video models in and out of VRAM) can now help you server and manage decision models: Auto-discovered. Drop a decision GGUF (Kev, OpenJev, Laya, ...) in your models folder and it gets its own config entry, sized for VRAM like everything else. Playground tab. Write a prompt, ask one question, pick the…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 144
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x53ob3/quartermaster_17_update_now_lets_you_run/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Quartermaster 1.7 update now lets you run llama.cpp's new decision models (/v1/systemone) with a playground tab

Reddit · OneMoreName1 · 2026-10-13

Quartermaster (my local inference manager: one server that swaps llama.cpp, image, audio and video models in and out of VRAM) can now help you server and manage decision models: Auto-discovered. Drop a decision GGUF (Kev, OpenJev, Laya, ...) in your models folder and it gets its own config entry, sized for VRAM like everything else. Playground tab. Write a prompt, ask one question, pick the answer shape, hit Run. Each option gets a probability bar. Useful for quick testing Model browser. A Decision tab finds them on Hugging Face. Same API, proxied. POST /v1/systemone goes through Quartermaster's scheduler and API keys, so it swaps in next to your chat model like any other request. Needs a llama.cpp new enough to have /v1/systemone (upstream b11361+; Quartermaster will warn about older builds). Project info: https://quartermaster-labs.github.io/Quartermaster/ Release: https://github.com/Quartermaster-Labs/Quartermaster/releases/tag/v1.7.0 Happy to hear what people are using these for.
