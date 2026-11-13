---
id: "e8865732ed08b037"
title: "4xR9700 & EXL3 HW/SW tips: DS4.1F (2.25bpw) pp 6.1k, c1 96-165, c16 259 tok/s | QFN (4.05bpw) pp 9.8k, c16 1100 tok/s"
url: "https://reddit.com/r/LocalLLaMA/comments/1xv2jst/4xr9700_exl3_hwsw_tips_ds41f_225bpw_pp_61k_c1"
link: "https://reddit.com/r/LocalLLaMA/comments/1xv2jst/4xr9700_exl3_hwsw_tips_ds41f_225bpw_pp_61k_c1"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T08:30:37Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["mikoskinen"]
language: "en"
summary: "I've been testing and optimizing Radiance for 4xR9700 on EPYC Rome platform (tp4), focusing on EXL3 for DS 4.1 Flash (2.25) and Qwen Flash Next (4.05). The goal has been to optimize this setup (both hardware and software) for Claude Code usage, so it may not be the fastest for 1 user interactive usage. Also the focus has been to provide \"exact\" results, so output is byte-identical to each…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Alibaba", "AMD"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 582
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xv2jst/4xr9700_exl3_hwsw_tips_ds41f_225bpw_pp_61k_c1/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 4xR9700 & EXL3 HW/SW tips: DS4.1F (2.25bpw) pp 6.1k, c1 96-165, c16 259 tok/s | QFN (4.05bpw) pp 9.8k, c16 1100 tok/s

Reddit · mikoskinen · 2026-11-13

I've been testing and optimizing Radiance for 4xR9700 on EPYC Rome platform (tp4), focusing on EXL3 for DS 4.1 Flash (2.25) and Qwen Flash Next (4.05). The goal has been to optimize this setup (both hardware and software) for Claude Code usage, so it may not be the fastest for 1 user interactive usage. Also the focus has been to provide "exact" results, so output is byte-identical to each model's reference engine. I'm quite happy with the improvements and with the end results and I think I will leave the optimizations to current point because there's not obvious new improvements in the pipeline. Instead of releasing a fork of Radiance, I hope maintainers of inference engines can use the work to improve their products. So to save time and effort, there's a GitHub repo that shows all the things that were tested and what worked and what didn't. Repo also contains more hardware optimization tips for 4xR9700 & EPYC Rome setups: https://github.com/mikoskinen/r9700-exact-serving It would be great if someone could figure out ways to improve C8 decode performance for Deepseek. And maybe someone can break the 10k tok/s barrier on QFN.. Note: all the testing, profiling, coding was done by Opus. I just pointed it to new resources like Reddit posts, repositories etc. Hardware: 4x AMD Radeon AI PRO R9700, PCIe 4.0 x16 AMD EPYC 7302P (Rome) on ASRock Rack ROMED8-2T 512 GB DDR4-2933 (8x 64 GB) Radiance fork + radiance-exl3 plugin, tensor parallel over all 4 cards Results: Here's some of the highlights from the results (stock 300 W per card, decode = tok/s summed over all users, prefill = one cold prompt): DS4.1F (2.25bpw) 1 user: 96 tok/s prose, 165 tok/s code 4 / 8 / 16 users: 176 / 208 / 259 tok/s prefill: 3,740 tok/s at 16k (TTFT 4.2 s), 6,020 at 64k (TTFT 10.9 s), 6,140 at 128k (TTFT 21.4 s) QFN (4.05bpw) 1 user: 269 tok/s 4 / 8 / 16 users: 619 / 831 / 1,094 tok/s prefill: 9,540 tok/s at 16k (TTFT 1.7 s), 9,810 at 64k (TTFT 6.7 s), 9,710 at 128k (TTFT 13.5 s) At my everyday 210 W / -50 mV setting these are about 5-9 % lower (DS 237 and QFN ~1,030 tok/s at 16 users). The following is AI's view on the most important optimization tips: Software optimizations: DS4.1F only needs half of its layers for most of the prompt: the upper 20 of 40 layers act as a decoder that reads just the end of the prompt, so prefill runs them only for the tail. 136k cold prompt went from 50.5 s to 33.3 s (-34 %), and with the other changes 128k now takes 21 s (6,140 tok/s). Interleaved push in the exact 4-card all-reduce: a 42 MB all-reduce went from 3.4 to 2.5 ms (-27 %) QFN prefill splits the hyper-connection stages across the 4 cards: +5.7 % Hardware optimizations: Same-size DIMMs in one interleave set: mixed 32/64 GB sticks made Rome split memory into 2-channel regions. 8x 64 GB took CPU read bandwidth from 35.9 to 104 GB/s and 2-card host-to-GPU copies from 45 to 55 GB/s. Check the memory address map after any DIMM change (a CPU swap from 7282 to 7302P did nothing). One GPU per IO-die quadrant: risers so no two cards share a root port. 4-card host-to-GPU copies went from 61 to 105 GB/s. Deep CPU C-states off and the performance governor: this removed a random ~16 % slowdown. Hope this helps.
