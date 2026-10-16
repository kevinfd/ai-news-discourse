---
id: "4467183067847142"
title: "I tested Qwen3.8 27B KLD for 21 Models at 9 different KV quants that fit on 16GB VRAM (189 benchmarks)."
url: "https://reddit.com/r/LocalLLaMA/comments/1x6fwcd/i_tested_qwen38_27b_kld_for_21_models_at_9"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6fwcd/i_tested_qwen38_27b_kld_for_21_models_at_9"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T08:11:09Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Fancy-Snow7"]
language: "en"
summary: "I calculated KLD and perplexity for Qwen3.8 27B models that fit 16GB VRAM: See comments for the benchmarks. Reddit filters keeps deleting the post. Conclusion: q5_1/q5_1 is almost always better than q8_0/q4_0 or q4_0/q8_0. There is very little difference between q8_0/q4_0 and q4_0/q8_0 q4_0/q8_0 is sometimes better than q8_0/q4_0. So it's safer to just go q5_1/q5_1. Going up a model quant and…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 173
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6fwcd/i_tested_qwen38_27b_kld_for_21_models_at_9/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I tested Qwen3.8 27B KLD for 21 Models at 9 different KV quants that fit on 16GB VRAM (189 benchmarks).

Reddit · Fancy-Snow7 · 2026-10-15

I calculated KLD and perplexity for Qwen3.8 27B models that fit 16GB VRAM: See comments for the benchmarks. Reddit filters keeps deleting the post. Conclusion: q5_1/q5_1 is almost always better than q8_0/q4_0 or q4_0/q8_0. There is very little difference between q8_0/q4_0 and q4_0/q8_0 q4_0/q8_0 is sometimes better than q8_0/q4_0. So it's safer to just go q5_1/q5_1. Going up a model quant and running at q4_0/q4_0 is almost always better than running the quant below at f16/f16 in terms of KLD. So basically pick the highest quant you can at q4_0/q4_0. Then if you have room to spare increase KV quant. Note this applies to lower quants. If you are going from q6->q8 model quant it might be bigger gains increasing KV quant, due to diminishing gains going up model quants. Also this does not apply to other models like Gemma where you have to run f16 KV. Bonsai and swift quants are included but it does not really make sense to calculate KLD since they are finetunes and the KLD will differ significantly.
