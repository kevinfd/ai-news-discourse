---
id: "37fb69c1eab9d21c"
title: "Qwen3.8 27b hitting 6,645 tok/s on prefill and 316 tok/s decode peak on Saber"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpicjz/qwen38_27b_hitting_6645_toks_on_prefill_and_316"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpicjz/qwen38_27b_hitting_6645_toks_on_prefill_and_316"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T17:15:13Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["whodoneit1"]
language: "en"
summary: "I know what you are thinking \"another inference engine?\", yeah there has been a flood of them I feel now. I have been running this for over a month now and I have been on the fence to even release it, but I decided to as I took a different approach that others currently available. Saber is a inference engine built in Rust targeting AMD R9700 GPU's. It currently supports TP 1, 2 or 4 and Qwen 3.8…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "AMD"]
topics: ["products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 125
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpicjz/qwen38_27b_hitting_6645_toks_on_prefill_and_316/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8 27b hitting 6,645 tok/s on prefill and 316 tok/s decode peak on Saber

Reddit · whodoneit1 · 2026-11-06

I know what you are thinking "another inference engine?", yeah there has been a flood of them I feel now. I have been running this for over a month now and I have been on the fence to even release it, but I decided to as I took a different approach that others currently available. Saber is a inference engine built in Rust targeting AMD R9700 GPU's. It currently supports TP 1, 2 or 4 and Qwen 3.8 27b and Flash next. Anyways here are the BetterBench results for Qwen3.8 27b, flash next is very fast also. Saber beats existing available engines on both 27b and flash next. BetterBench Qwen 3.8 27b Unsloth NVFP4 Results https://github.com/GGZ14/saber-engine https://x.com/bkuyper AMD Ryzen 9900X Taichi X870E 64GB RAM 2xR9700
