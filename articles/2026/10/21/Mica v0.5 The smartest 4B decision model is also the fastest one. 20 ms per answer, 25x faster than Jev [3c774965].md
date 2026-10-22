---
id: "3c7749650af0375d"
title: "Mica v0.5: The smartest 4B decision model is also the fastest one. 20 ms per answer, 25x faster than Jev"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbw3oy/mica_v05_the_smartest_4b_decision_model_is_also"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbw3oy/mica_v05_the_smartest_4b_decision_model_is_also"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T19:00:21Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Top-Evidence174"]
language: "en"
summary: "I'm sharing Mica v0.5, the follow-up to Mica v0.1. It's 4B and runs on one consumer GPU. On speed, it takes 19.8 ms per decision at 256 tokens and about 1.2 s at 32k on a single RTX 6000 Ada. That's up to 3.8x faster than the other 4B judges I measured, 12 to 19x faster than Perplexity's 27B decider, and 25 to 340x faster than the API decision models. On top of the optimizations described on HF,…"
tags: ["r/LocalLLaMA"]
orgs: ["Microsoft", "Perplexity", "Nvidia", "Apple", "AMD"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 345
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbw3oy/mica_v05_the_smartest_4b_decision_model_is_also/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Mica v0.5: The smartest 4B decision model is also the fastest one. 20 ms per answer, 25x faster than Jev

Reddit · Top-Evidence174 · 2026-10-21

I'm sharing Mica v0.5, the follow-up to Mica v0.1. It's 4B and runs on one consumer GPU. On speed, it takes 19.8 ms per decision at 256 tokens and about 1.2 s at 32k on a single RTX 6000 Ada. That's up to 3.8x faster than the other 4B judges I measured, 12 to 19x faster than Perplexity's 27B decider, and 25 to 340x faster than the API decision models. On top of the optimizations described on HF, Mica Fast makes long inputs about 1.4 to 1.5x faster again. On accuracy, it gets 84/111 on JevBench Hard, the best of any 4B model I could find (only Microsoft's 9B Decision-1 is higher). On JDI it scores 58.8, ahead of every 9B and 35B model I tested. One honest note: the top 4B models on JDI are all benchmark-focused, and at least one of them was trained on nothing but benchmark-style data. To compete I did train on data from the same areas the benchmarks cover, but nothing contaminated, and most of the effort went into how it does on real work. That part comes from 200+ real use cases people posted on Reddit, Twitter and elsewhere. A few things I cared about. If you shuffle the answer options it still picks the same answer 97.3% of the time. It can hold back too, so if you set a threshold it tells you when it isn't sure instead of guessing. It handles yes/no, multiple choice, and scores from 2 to 255 levels, with inputs up to 32k tokens. If you have an NVIDIA card I'd go with the INT8 version, since it's the fastest. On the same GPU it runs about 2 to 2.7x faster than the Q8_0 GGUF on llama.cpp. GGUF files (BF16, Q8_0, IQ4_XS) are there for AMD, Apple and CPU. It runs on 8 GB cards and up, and it's Apache-2.0. HF: https://huggingface.co/sky7350/Mica-v0.5-4B GitHub: https://github.com/akivet/Mica Happy to answer questions, and I'd really like to hear where it breaks. If you're looking forward to v1.0, I'm a broke student and any tip helps: https://ko-fi.com/micakiv
