---
id: "82d64a92245352bb"
title: "askmdb: My new project where I fine-tuned Qwen models to build a MongoDB CLI assistant - turn plain-language questions into MongoDB queries"
url: "https://reddit.com/r/LocalLLaMA/comments/1xtfvct/askmdb_my_new_project_where_i_finetuned_qwen"
link: "https://reddit.com/r/LocalLLaMA/comments/1xtfvct/askmdb_my_new_project_where_i_finetuned_qwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T11:55:54Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["AlternativeEnough352"]
language: "en"
summary: "I built askmdb to help people finding the right query for turn plain-language questions into MongoDB queries . For example, you type askmdb \"top 5 customers by spending this year\" , and the app returns the query. A small fine-tuned model writes an aggregate pipeline and a one-line explanation, and nothing runs until you confirm. It's one Linux binary with llama.cpp and the official MongoDB C…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "chips & infrastructure", "business & funding", "products & launches"]
content_source: "post"
word_count: 470
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xtfvct/askmdb_my_new_project_where_i_finetuned_qwen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# askmdb: My new project where I fine-tuned Qwen models to build a MongoDB CLI assistant - turn plain-language questions into MongoDB queries

Reddit · AlternativeEnough352 · 2026-11-11

I built askmdb to help people finding the right query for turn plain-language questions into MongoDB queries . For example, you type askmdb "top 5 customers by spending this year" , and the app returns the query. A small fine-tuned model writes an aggregate pipeline and a one-line explanation, and nothing runs until you confirm. It's one Linux binary with llama.cpp and the official MongoDB C driver built in. No Python, no server, no API keys. EVERYTHING run in local. My test, results on 500 test questions in English and Spanish, over synthetic databases the training never saw. Every model is Q4_K_M on the same llama.cpp. A question counts as correct only if the predicted pipeline returns the same result as the reference when it runs. No other model grades the answers, I tested a few models; Model GGUF Correct Accuracy askmdb-9b (GPU) 5.6 GB 458 91.6% askmdb-4b (GPU) 2.7 GB 448 89.6% askmdb-2b 1.3 GB 434 86.8% askmdb-0.8b (CPU) 529 MB 418 83.6% Qwen3.5-9B, stock 5.7 GB 239 47.8% Gemma 4 E4B-it, stock 5.0 GB 227 45.4% Gemma 4 E2B-it, stock 3.1 GB 221 44.2% Qwen3.5-0.8B, stock 530 MB 33 6.6% On a desktop CPU with 8 threads, the 0.8B answers in 1.18 s (median) once the schema is cached. The first question against a new database takes about 3 s aprox. The app also works with GPU. The model doesn't decide what's safe because its deterministic C++. A verifier walks the whole pipeline, sub-pipelines included, against a whitelist. A $out hidden inside a $facet is blocked in every mode. BUT connect with a read-only database user to be sure. Most important lesson: my first version got stuck at 68.6% with 10k examples. I grouped the failures by sub-cause instead of looking at the overall score. Of the 50 test questions that needed a type conversion, it got exactly 1 right. The dataset had zero examples with $convert , although 297 of the 330 training schemas had fields that mix numbers and strings. My generator had been quietly avoiding them. I added 3,000 examples aimed at those failures (850 of them with $convert ), then 2,000 more, and kept the same recipe and hyperparameters. Result: 343 → 418 correct. Always is the same: the dataset is the most important thing when it comes to train models. Training and evaluation took about 14 USD of rented RTX 5090 GPU (~12 GPU-hours). The code is MIT. The models are Apache-2.0 GGUFs that also work with plain llama.cpp :). Has anyone managed to make a sub-1B model good at multi-collection joins ( $lookup )? That's where mine fails most, and I'd love to hear what worked for you, because I tried many things withouth success. Links Full write-up (process, charts and dead ends): https://manuelgs.com/en/blog/askmdb-case-study/ Code: https://github.com/manuelgscom/askmdb Models (0.8B to 9B, Q4_K_M): https://huggingface.co/collections/manuelgscom/askmdb
