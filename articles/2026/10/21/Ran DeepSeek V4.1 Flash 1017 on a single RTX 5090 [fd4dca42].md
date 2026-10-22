---
id: "fd4dca420a1d3a63"
title: "Ran DeepSeek V4.1 Flash 1017 on a single RTX 5090"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbqir0/ran_deepseek_v41_flash_1017_on_a_single_rtx_5090"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbqir0/ran_deepseek_v41_flash_1017_on_a_single_rtx_5090"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T15:38:12Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["jesdga95"]
language: "en"
summary: "Been working over the last few days getting DeepSeek V4.1 Flash 1017 (Unsloth UD-IQ1_S) running in Basalt (inference engine I'm developing). Specs: RTX 5090 (400W) + RTX 5060 Ti 16 GB (180W), 128 GB DDR5. Methodology: Single 243 GB file (weights + vision + drafter). Engram table on SSD. All experts (107 GiB) in RAM. 5090 as an expert cache (hottest experts) and later also tried hoding and…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 340
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbqir0/ran_deepseek_v41_flash_1017_on_a_single_rtx_5090/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ran DeepSeek V4.1 Flash 1017 on a single RTX 5090

Reddit · jesdga95 · 2026-10-21

Been working over the last few days getting DeepSeek V4.1 Flash 1017 (Unsloth UD-IQ1_S) running in Basalt (inference engine I'm developing). Specs: RTX 5090 (400W) + RTX 5060 Ti 16 GB (180W), 128 GB DDR5. Methodology: Single 243 GB file (weights + vision + drafter). Engram table on SSD. All experts (107 GiB) in RAM. 5090 as an expert cache (hottest experts) and later also tried hoding and computing some experts in the 5060 Ti for a performance boost. Prefill tested with a 6.2k-token prompt (my daily harness). Baseline was llama.cpp PR #30817 with --fit, same hardware and quant. Results: Setup Decode Prefill warm / cold llama.cpp --fit ~20 tok/s – 5090, all experts in RAM 53.6 tok/s 610 / 595 tok/s 5090 + 5060 Ti computing its own experts 63.5 tok/s 610 / 610 tok/s* Expert lookups: 66% 5090, 16% 5060 Ti, 5% copied over PCIe, 12% CPU. Also works: tool calls, images, up to 1M context (a 1M prompt takes ~26 min, ouch) Quality: no PPL/KLD yet. Greedy matches llama on all test prompts. Also even at IQ1_S the model nailed most of my regular benchmarks, and recall is well above Qwen 3.8 FN, which is expected, this is a model a few times its size (even heavily quanted). Limits: the 12% of lookups left on the CPU hurt speed badly (limited by DDR5 dual channel), speculation barely helps in my case (1.1-1.2x). Anyway, thought I'd share. This was a personal experiment to see how far I could push it, there's probably some room to get around 80ish decode and ~1000 prefill, but on my hardware it doesn't make sense to keep going when I'm already getting over 300 tok/s on 3.8 FN. Where it could potentially pay off: 96+ GB of VRAM (RTX 6000 PRO) or quad/octa channel DDR5 rigs. I did not push my experimental branch to the repo but if there's any interest let me know, I'll do it. Also interested to know if anyone else tried to do the same and found different results.
