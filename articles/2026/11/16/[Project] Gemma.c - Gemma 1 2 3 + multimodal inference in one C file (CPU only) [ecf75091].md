---
id: "ecf75091a6e7b0bd"
title: "[Project] Gemma.c - Gemma 1/2/3 + multimodal inference in one C file (CPU only)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xxq01s/project_gemmac_gemma_123_multimodal_inference_in"
link: "https://reddit.com/r/LocalLLaMA/comments/1xxq01s/project_gemmac_gemma_123_multimodal_inference_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T13:58:04Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["This-Purchase-3325"]
language: "en"
summary: "Hey all, so I've been working on Gemma.c over the last couple months, it's a from-scratch inference engine for Gemma 1/2/3 in a single C file, runs Gemma 1, 2 and 3, including the multimodal ones, with fp32/fp16/bf16 weights or int8 (W8A8). No dependencies beyond libc and (optional) OpenMP are needed. You can drop images into the prompt with @image{cat.png} , and there's also @longimage{} for…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 323
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xxq01s/project_gemmac_gemma_123_multimodal_inference_in/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Project] Gemma.c - Gemma 1/2/3 + multimodal inference in one C file (CPU only)

Reddit · This-Purchase-3325 · 2026-11-16

Hey all, so I've been working on Gemma.c over the last couple months, it's a from-scratch inference engine for Gemma 1/2/3 in a single C file, runs Gemma 1, 2 and 3, including the multimodal ones, with fp32/fp16/bf16 weights or int8 (W8A8). No dependencies beyond libc and (optional) OpenMP are needed. You can drop images into the prompt with @image{cat.png} , and there's also @longimage{} for Gemma 3's pan & scan on very wide or tall images. (image decoding uses a minified stb_image embedded at the end of the file) It's CPU only and not trying to compete with llama.cpp, but I'm also trying my best to make it efficient, so it's not embarrassingly slow either. On my laptop's Core Ultra 5 225H (WSL2, gcc, 10 threads), gemma-3-1b-it INT8 does ~72 tok/s decode and ~570 tok/s prefill (10000 tokens, for 1000 tokens the prefill speed can reach ~850 tok/s), and the 4B vision model does ~20 tok/s decode. INT8 ends up about 3.5x faster than fp32 and 2x faster than fp16 for decode. (full benchmark table is in README) It has a few rough edges for now, e.g. W8A8 doesn't work for Gemma 1 (fp16 is fine), bf16 is painfully slow without AVX512-BF16, and native Windows is ~1.7x slower than WSL because of libgomp. Batching are not supported either. There's a roadmap in the README (Gemma 4, speculative decoding, an HTTP server, etc.), but no promises though :P Can't really find much free time these days. I've also put some pre-exported INT8 models on HF so you can try it without Python or torch :D Repo: link This project started as a learning attempt to understand how LLMs work end to end, inspired by llama2.c . this is the second time I post this project here :'D last time (~a month ago) my post got flagged by reddit, probably because my VPN IP was identified as spam. hopefully it can pass this time
