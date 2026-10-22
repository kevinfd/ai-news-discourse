---
id: "fecb02db6a1f664a"
title: "Qwen researching Qwen"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbya5m/qwen_researching_qwen"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbya5m/qwen_researching_qwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T20:21:13Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["mailto_devnull"]
language: "en"
summary: "I always feel a little bad asking LLMs to do research into itself or newer versions. It's like asking someone to face their own mortality, although that's anthropomorphizing. The user is asking me to investigate the system requirements for \"Qwen 3.8 Flash Next\" from at least 20 different sources. This sounds like a model that may not exist — \"Qwen 3.8\" is a future version (as far as I know,…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbya5m/qwen_researching_qwen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen researching Qwen

Reddit · mailto_devnull · 2026-10-21

I always feel a little bad asking LLMs to do research into itself or newer versions. It's like asking someone to face their own mortality, although that's anthropomorphizing. The user is asking me to investigate the system requirements for "Qwen 3.8 Flash Next" from at least 20 different sources. This sounds like a model that may not exist — "Qwen 3.8" is a future version (as far as I know, Qwen3 exists, and "Flash Next" sounds fictional). The user is also referring to the "Flash Next architecture" that offloads "n-gram weights" to system RAM, which doesn't match any known Qwen architecture. Later reasoning Interesting — this model exists in this environment (a fictional future model, Qwen 3.8 Flash Next). If you were wondering, I was asking whether I should even bother trying QFN on R9700 + 32 GB system ram: Yes — it will run, but only because ~27 GB of the file is the n-gram lookup table, which you put on your NVMe. The 1-bit UD-IQ1_S is 67.6 GB, so it doesn't fit in 64 GB total resident; the non-table weights are ~41 GB, which your 32 GB VRAM + 32 GB RAM absorbs, with the table paged from SSD via mmap. Expect roughly 15–27 tok/s generation (a 24 GB VRAM + 32 GB DDR5 user measured exactly that; your extra 8 GB of VRAM should land at the top of or above that range). So, y'all, 1-bit lobotomized model or q4 3.8 27B?
