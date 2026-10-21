---
id: "024117bbf0cda68d"
title: "DeepSeek-V4.1-Flash (UD-Q4_K_XL) on 4x 3090 + EPYC: 12 → 25 tok/s prose, 39 tok/s code."
url: "https://reddit.com/r/LocalLLaMA/comments/1xas9h8/deepseekv41flash_udq4_k_xl_on_4x_3090_epyc_12_25"
link: "https://reddit.com/r/LocalLLaMA/comments/1xas9h8/deepseekv41flash_udq4_k_xl_on_4x_3090_epyc_12_25"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T13:32:26Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["C0smo777"]
language: "en"
summary: "Hi all, just wanted to share some benchmarks. I got Unsloth's UD-Q4_K_XL quant of DeepSeek-V4.1-Flash-1017 running and spent some time tuning it. Some of what I found isn't in the guide, so here are my notes. Hardware EPYC 9575F (64 cores / 128 threads) 768 GB DDR5 4x RTX 3090 (96 GB VRAM total) Software llama.cpp built from PR #30817. Mainline and ik_llama.cpp can't load this model yet. The…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 522
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xas9h8/deepseekv41flash_udq4_k_xl_on_4x_3090_epyc_12_25/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# DeepSeek-V4.1-Flash (UD-Q4_K_XL) on 4x 3090 + EPYC: 12 → 25 tok/s prose, 39 tok/s code.

Reddit · C0smo777 · 2026-10-20

Hi all, just wanted to share some benchmarks. I got Unsloth's UD-Q4_K_XL quant of DeepSeek-V4.1-Flash-1017 running and spent some time tuning it. Some of what I found isn't in the guide, so here are my notes. Hardware EPYC 9575F (64 cores / 128 threads) 768 GB DDR5 4x RTX 3090 (96 GB VRAM total) Software llama.cpp built from PR #30817. Mainline and ik_llama.cpp can't load this model yet. The DSpark drafter, Q8_0 (8 GB), for speculative decoding Final command llama-server -m DeepSeek-V4.1-Flash-1017-UD-Q4_K_XL-00001-of-00009.gguf \ -c 65536 -fa on --jinja --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \ -t 64 -tb 64 \ --load-mode none --lazy-mode off \ -ub 2048 -b 4096 \ --fit on --fit-target 4096,4096,4096,7168 \ -md dspark-DeepSeek-V4.1-Flash-1017-Q8_0.gguf \ --spec-type draft-dspark --spec-draft-n-max 3 -ngld 99 Results All numbers are tokens per second, one request at a time, thinking off. Each row is a single run, so they're noisy. Run Change Essay Code 8K prompt (prefill / gen) 32K prompt (prefill / gen) A Unsloth example flags 12.6 17.5 173 / 16.2 177 / 7.5 B + whole model in RAM 20.4 17.3 190 / 18.7 200 / 16.9 C + -ub 2048 17.0 19.4 254 / 16.1 276 / 19.7 D + DSpark, one thread per physical core 24.6 39.3 326 / 20.6 363 / 25.4 Notes 1. Load the whole model into RAM if it fits. Use --load-mode none --lazy-mode off instead of the guide's mmap/lazy flags. 32K gen went from 7.5 to about 17 tok/s. Load time goes from 20 seconds to about 4 minutes. 2. One thread per physical core. If your gen speed jumps around between runs, check that your threads aren't doubling up on cores. 3. -ub 2048 makes prompt processing about 35% faster at no cost. -ub 4096 was faster again (about 300 to 345 tok/s), but --fit then put about 6 GB less of the model on one GPU, and generation often fell to 10 to 12 tok/s. 4. DSpark speeds up code a lot and prose very little. On code, about 80% of its guesses were accepted, which roughly doubles the speed. On prose only about 30% were accepted, and it's sometimes a bit slower. I mostly use the model for code, so I keep DSpark on. Problems I hit ** --fit can't size the DSpark drafter.** It logs failed to measure the memory of the extra model, fitting without it and fills the GPUs with the main model. The drafter then fails with cudaMalloc failed: out of memory . The drafter needs about 2.5 GB on GPU0 and about 5.1 GB on the last GPU. --fit-target 5120 on every GPU failed, and so did 2048,2048,2048,10240 . 4096,4096,4096,7168 works. ** --fit gives up if you also pass --override-tensor .** The guide's example includes -ot per_layer_token_embd.weight=CPU . Used with --fit , it gives tensor_buft_overrides already set by user , and llama.cpp falls back to its default layout. Leave out the -ot . The drafter file didn't download with the model shards. hf download --include silently skipped it because it sits at the top level of the repo. Downloading it by its exact filename worked.
