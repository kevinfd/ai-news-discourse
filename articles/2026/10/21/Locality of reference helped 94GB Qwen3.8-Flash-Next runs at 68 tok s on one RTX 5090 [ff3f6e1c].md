---
id: "ff3f6e1c11a89bec"
title: "Locality of reference helped 94GB Qwen3.8-Flash-Next runs at 68 tok/s on one RTX 5090"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xbur5z/locality_of_reference_helped_94gb_qwen38flashnext"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xbur5z/locality_of_reference_helped_94gb_qwen38flashnext"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T18:11:04Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["abhishekkumar333"]
language: "en"
summary: "llama.cpp merged PR #29887 two weeks ago and I think it is the most interesting thing to land in local inference this year, so I went through the PR, the benchmarks and the review thread and wrote up how it actually works. Short version below, long version linked at the end. The problem Qwen3.8-Flash-Next at Q4_0 is 93.7 GiB, and 65.4 GiB of that is experts. It is 125B total but only 6B active:…"
tags: ["r/ArtificialInteligence"]
orgs: ["AMD"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 421
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xbur5z/locality_of_reference_helped_94gb_qwen38flashnext/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Locality of reference helped 94GB Qwen3.8-Flash-Next runs at 68 tok/s on one RTX 5090

Reddit · abhishekkumar333 · 2026-10-21

llama.cpp merged PR #29887 two weeks ago and I think it is the most interesting thing to land in local inference this year, so I went through the PR, the benchmarks and the review thread and wrote up how it actually works. Short version below, long version linked at the end. The problem Qwen3.8-Flash-Next at Q4_0 is 93.7 GiB, and 65.4 GiB of that is experts. It is 125B total but only 6B active: 512 experts per layer, the router picks 10 (plus 1 shared) per token. One expert is 3 x 2560 x 640 = 4.9M params = about 2.6 MiB at 4-bit. 10 experts x 48 layers = 480 experts per token = about 1.3 GB of weights touched per token. The observation Expert routing has locality of reference. Token N+1 mostly picks the same experts as token N. A handful of experts are hot, most are almost never touched. That is the same property your CPU cache, your OS page cache, your browser cache, every CDN and Redis allkeys-lru all rely on. The fix PR #29887 (by am17an, a port of Tether’s qvac-fabric work, merged by ggerganov on Oct 7) sets aside a slice of VRAM as an LRU cache of experts. Hit: compute from VRAM, zero bytes moved. Miss: copy that one 2.6 MiB expert over PCIe and evict the least recently used one. The log prints the hit rate at exit. Numbers from the PR description, same model file, same machine: GPU before with cache hit rate RTX 4090 24 GB 25.0 tok/s 40.7 tok/s (1.62x) 77% RTX 5090 32 GB 30.8 tok/s 67.8 tok/s (2.20x) 89% AMD R9700 32 GB (a reviewer’s card) 11.0 tok/s 27.6 tok/s 94.6% The 5090 gains more for two reasons: PCIe 5.0 halves the cost of every miss, and 32 GB means a bigger cache and fewer misses. How to use it llama-server -m Qwen3.8-Flash-Next-Q4_0.gguf -fa on -c 32768 -b 2048 -ub 2048 -cmoe --moe-cache-mib 11000 The PR author’s rule of thumb is about 10% of your expert bytes (65.4 GiB -> 6544 MiB). Env var form is LLAMA_ARG_MOE_CACHE_MIB. SGLang merged the same idea 12 days later as “paged experts” in PR #42557 The part I find most interesting is LRU , Locality of reference go back to 1960s. And i find locality of reference principle highly underrated. Full write-up with the memory math script, an expert cache simulator you can run, and the benchmark table: https://cloudmash.blog/posts/moe-expert-offload-lru-cache-consumer-gpu/ llama.cpp PR #29887, MoE expert cache: https://github.com/ggml-org/llama.cpp/pull/29887 SGLang PR #42557, paged experts: https://github.com/sgl-project/sglang/pull/42557
