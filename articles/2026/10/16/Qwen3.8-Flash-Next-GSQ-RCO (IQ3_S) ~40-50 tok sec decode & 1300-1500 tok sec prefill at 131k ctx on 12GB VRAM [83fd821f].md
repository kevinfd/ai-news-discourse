---
id: "83fd821f7a5abba3"
title: "Qwen3.8-Flash-Next-GSQ-RCO (IQ3_S): ~40-50 tok/sec decode & 1300-1500 tok/sec prefill at 131k ctx on 12GB VRAM + 32GB RAM + NVME"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7sbdc/qwen38flashnextgsqrco_iq3_s_4050_toksec_decode"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7sbdc/qwen38flashnextgsqrco_iq3_s_4050_toksec_decode"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T21:18:11Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["bodhi371"]
language: "en"
summary: "I got Qwen3.8-Flash-Next-GSQ-RCO-Abliterated running at IQ3_S with just 12GB VRAM + 32GB RAM + NVME, achieving 40-50 tok/sec decode & 1300-1500 tok/sec prefill @ 131k context (44k thinking budget), on a custom fork of Strata. Don’t see IQ3_S and instantly dismiss it, this recipe uses an abliterated version of ISTADASLab’s GSQ-RCO Qwen3.8-FN, which retains ~99% of BF16. Obviously there are rough…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 150
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7sbdc/qwen38flashnextgsqrco_iq3_s_4050_toksec_decode/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8-Flash-Next-GSQ-RCO (IQ3_S): ~40-50 tok/sec decode & 1300-1500 tok/sec prefill at 131k ctx on 12GB VRAM + 32GB RAM + NVME

Reddit · bodhi371 · 2026-10-16

I got Qwen3.8-Flash-Next-GSQ-RCO-Abliterated running at IQ3_S with just 12GB VRAM + 32GB RAM + NVME, achieving 40-50 tok/sec decode & 1300-1500 tok/sec prefill @ 131k context (44k thinking budget), on a custom fork of Strata. Don’t see IQ3_S and instantly dismiss it, this recipe uses an abliterated version of ISTADASLab’s GSQ-RCO Qwen3.8-FN, which retains ~99% of BF16. Obviously there are rough edges with any quantization method but in comparison to all generic imatrix quants, this is the best quant for this model across my testing (for this hardware tier - higher precision uniform quants will perform better obviously). And to have it running at these speeds on only ~44GB combined VRAM/RAM with an SSD is kind of ridiculous. This fork has tonnes of architectural changes, all are very experimental. But the performance makes up for it. This feels like local Opus in some regards. Local AI for all. https://github.com/bodhi37/Qwen3.8-Flash-12GBRAM-32GBVRAM-SSD-Recipe https://github.com/bodhi37/strata
