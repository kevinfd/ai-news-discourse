---
id: "98a63d180cc7d7ef"
title: "[Boole-32B-A2.5B-preview] 9GB 1.8-bit MoE, 565 token/s on 1 RTX 5090"
url: "https://reddit.com/r/LocalLLaMA/comments/1xv3h93/boole32ba25bpreview_9gb_18bit_moe_565_tokens_on_1"
link: "https://reddit.com/r/LocalLLaMA/comments/1xv3h93/boole32ba25bpreview_9gb_18bit_moe_565_tokens_on_1"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T09:29:51Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["d77chong"]
language: "en"
summary: "Hi r/LocalLLaMA , we're releasing Boole-32B-A2.5B-Preview, an early 1.8-bit version of Recursive's flint . With mixed-precision quantization, expert pruning, and custom kernels (kernel changes in attached figure), we made the model 9x smaller than BF16, and 2x faster than INT4. After releasing our 1-bit LLM (Boole-1.7B), we heard a lot of requests for both faster and larger MoE models - so this…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 94
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xv3h93/boole32ba25bpreview_9gb_18bit_moe_565_tokens_on_1/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Boole-32B-A2.5B-preview] 9GB 1.8-bit MoE, 565 token/s on 1 RTX 5090

Reddit · d77chong · 2026-11-13

Hi r/LocalLLaMA , we're releasing Boole-32B-A2.5B-Preview, an early 1.8-bit version of Recursive's flint . With mixed-precision quantization, expert pruning, and custom kernels (kernel changes in attached figure), we made the model 9x smaller than BF16, and 2x faster than INT4. After releasing our 1-bit LLM (Boole-1.7B), we heard a lot of requests for both faster and larger MoE models - so this is our first step in that direction. Try it out, and let us know what you'd like to see next! Weights: https://huggingface.co/precision-numerics/Boole-32B-A2.5B-Preview-GGUF Getting started: https://github.com/PrecisionNumerics/boole-demo Our llama.cpp fork: https://github.com/PrecisionNumerics/llama.cpp https://preview.redd.it/t0l4rqpxlc1i1.png?width=768&format=png&auto=webp&s=566e4617674c8a47dcd26a2c60e06e0e40a4a72e https://preview.redd.it/m1b44w2ylc1i1.png?width=768&format=png&auto=webp&s=a9625ef9811e51f833315da69cbdcf7e1871032a https://preview.redd.it/qsvvdihylc1i1.png?width=768&format=png&auto=webp&s=cd73999284597fa20689a35f4f28a97b6779b165
