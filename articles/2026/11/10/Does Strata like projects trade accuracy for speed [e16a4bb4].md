---
id: "e16a4bb41b591c4f"
title: "Does Strata like projects trade accuracy for speed?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsw9mr/does_strata_like_projects_trade_accuracy_for_speed"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsw9mr/does_strata_like_projects_trade_accuracy_for_speed"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T19:31:36Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Serious_Scarcity7818"]
language: "en"
summary: "I am tired to answer on people questions like \"How you gain speed? Your model output is shit, it has to have low quality.\" or something like that. So I will answer to that with benchmark. So I ran it against llama.cpp with the same Qwen3.8-Flash-Next IQ2_XS file, same prompt, and the same 128-token reply. This was on my RTX 3060 12 GB / Ryzen 7600X machine. I did six warm runs for each engine.…"
tags: ["r/LocalLLaMA"]
orgs: ["Perplexity"]
topics: ["models & research"]
content_source: "post"
word_count: 226
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsw9mr/does_strata_like_projects_trade_accuracy_for_speed/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Does Strata like projects trade accuracy for speed?

Reddit · Serious_Scarcity7818 · 2026-11-10

I am tired to answer on people questions like "How you gain speed? Your model output is shit, it has to have low quality." or something like that. So I will answer to that with benchmark. So I ran it against llama.cpp with the same Qwen3.8-Flash-Next IQ2_XS file, same prompt, and the same 128-token reply. This was on my RTX 3060 12 GB / Ryzen 7600X machine. I did six warm runs for each engine. RustingStrata llama.cpp Writing speed 33.0 tok/s 25.6 tok/s Range across runs 29.3–35.8 23.2–26.9 Reading the first prompt 109 tok/s 31 tok/s So RustingStrata was about 29% faster at writing in this test. Speed is nice, but I did not want to claim a win without checking what it does to the model’s output. I also ran both engines over the same 9,180 WikiText-2 tokens. Quality check Result Perplexity: RustingStrata 2.9212 Perplexity: llama.cpp 2.9156 Same most-likely next token 96.78% Mean KLD 0.0098 The perplexity gap is tiny, small enough to be noise here. I do not see RustingStrata getting its speed by losing measurable quality, at least with this model and this GPU. This is not a claim that it wins on every model or every PC. It is one model, one quantization and one card. If anyone has any other questions about this, I am happy to answer it. Repo: RustingStrata
