---
id: "e7eb67405c2aca6b"
title: "[Paper] Continuum Attention"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdhzi2/paper_continuum_attention"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdhzi2/paper_continuum_attention"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T15:58:43Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["pmttyji"]
language: "en"
summary: "We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 159
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdhzi2/paper_continuum_attention/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] Continuum Attention

Reddit · pmttyji · 2026-10-23

We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token boundary contributions. The gradients follow analytically from moments of order at most two, enabling parallel GPU implementations while retaining quadratic sequence complexity and the standard Transformer decoder. Compared with ordinary softmax and focal attention, CA reduces mean validation negative log likelihood by 0.0200 and 0.0480 nats per byte, respectively, winning all paired comparisons. An additional disjoint validation slice yields a 0.0457 nats per byte advantage over the strongest selected softmax baseline, with a paired 95% confidence interval. These findings motivate continuous integration as a promising attention alternative while leaving larger scale generalization open. arXiv : https://arxiv.org/abs/2610.20586 PDF : https://arxiv.org/pdf/2610.20586 GitHub : https://github.com/akhadangi/continuum-attention HuggingFace : https://huggingface.co/akhadangi/Llama3.2.1B.0.1-H
