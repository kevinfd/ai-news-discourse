---
id: "2f9a68cf549ac290"
title: "Do looped transformers save HBM traffic? Profiling weight reuse in Huginn on a B200 [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling"
link: "https://reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T16:26:12Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["2dayyy6"]
language: "en"
summary: "Do looped transformers, which reuse the same weights at every iteration, also save HBM traffic? In my new post I cover the looped architecture (Huginn), then model and measure its performance on a B200: how much data each iteration reads from memory, how long it takes, and why the shared weights usually don't stay on chip until the next iteration. A few results: - A chain of eight matmuls with…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 182
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling/"
score: null
comments: null
community: "r/MachineLearning"
---

# Do looped transformers save HBM traffic? Profiling weight reuse in Huginn on a B200 [P]

Reddit · 2dayyy6 · 2026-11-04

Do looped transformers, which reuse the same weights at every iteration, also save HBM traffic? In my new post I cover the looped architecture (Huginn), then model and measure its performance on a B200: how much data each iteration reads from memory, how long it takes, and why the shared weights usually don't stay on chip until the next iteration. A few results: - A chain of eight matmuls with one shared 72 MiB weight ran 24% faster than the same chain with eight identical copies, and read almost nothing from HBM. At 288 MiB, larger than L2, the difference disappeared. - In a full Huginn Core (teaching implementation, random weights), eight iterations took about eight times as long as one and read about eight times as much data from HBM. - Sharing saves storage, but by itself it doesn't stop the GPU from reading the weights from HBM again at every iteration. 👀Post: https://dinara-dl.github.io/posts/looped-transformer/ 🤖Code and raw Nsight Compute data: https://github.com/dinara-dl/looped-transformer I'd be curious whether anyone has tried keeping recurrent weights on chip across iterations, for example with a persistent kernel.
