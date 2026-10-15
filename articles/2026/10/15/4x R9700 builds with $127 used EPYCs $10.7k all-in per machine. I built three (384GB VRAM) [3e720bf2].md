---
id: "3e720bf25f5174f5"
title: "4x R9700 builds with $127 used EPYCs: $10.7k all-in per machine. I built three (384GB VRAM)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x67qeu/4x_r9700_builds_with_127_used_epycs_107k_allin"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T00:31:42Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["NickReese"]
language: "en"
summary: "I saw the 4x R9700 build for a 10-person startup here a few days ago and wanted to share my results, since I opted to spend most of the money on the cards. I went with a super cheap used EPYC instead of a Threadripper. In the end it came to about $10.7k per box all-in, and I built three of them for a total of 384 GB of VRAM. As a long time lurker on my other account, I'm always frustrated that…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "DeepSeek", "Samsung", "AMD"]
topics: ["business & funding", "models & research"]
content_source: "post"
word_count: 883
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x67qeu/4x_r9700_builds_with_127_used_epycs_107k_allin/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 4x R9700 builds with $127 used EPYCs: $10.7k all-in per machine. I built three (384GB VRAM)

Reddit · NickReese · 2026-10-15

I saw the 4x R9700 build for a 10-person startup here a few days ago and wanted to share my results, since I opted to spend most of the money on the cards. I went with a super cheap used EPYC instead of a Threadripper. In the end it came to about $10.7k per box all-in, and I built three of them for a total of 384 GB of VRAM. As a long time lurker on my other account, I'm always frustrated that people never show how they actually use the models, so after a lot of back and forth I decided to share the actual project they power instead of being vague. I use these to run the AI behind my business, USA Arms. We organize tens of thousands of firearms-related businesses (gun dealers, ammo dealers, ranges, etc.) and that info is always changing, so we need a system that keeps the site up to date. The models check source facts, sort out business identities, and pull out stuff like services and hours. Every answer gets verified against what the agent actually saw, and we store the documentation so bigger models can audit the work. I didn't plan to move the majority of my work to local AI until later this year, but hosted models started refusing to do normal research for my business ~2-3 weeks ago. They refused to identify a gun dealer because the license holder might be an individual, and wouldn't look at an ammo dealer's website because they can't help anyone buy ammo. Our harness just started breaking in random ways, so I'm glad I made the leap. We tested Luna 6, DeepSeek, GLM 5.3, Qwen 3.8 27B, Gemma and Inkling on our workload, along with Kimi, GLM Flash and others. GLM gave us the best results. Qwen gave us the best cost-to-performance, so that's what these run. Enough ado, into the numbers: Per box, $10,733.91 with tax and shipping (averaged over the three) 4x ASRock Radeon AI PRO R9700 Creator 32 GB (128 GB VRAM), each capped at 210 W: $7,244.58 AMD EPYC 7452, 32 cores, used: $127.17 ASRock Rack ROMED8-2T/BCM: $1,162.39 (there was a global shortage, ours came from Helsinki) 8x 16 GB DDR4-2666 ECC RDIMM, all eight channels: $860.59 SilverStone HELA 2050R Platinum: $578.92 SilverStone RM44 4U: $388.40 Samsung 990 PRO 1 TB: $254.39 ARCTIC Freezer 4U-M, 3x ARCTIC P12 Pro front, 2x Noctua NF-A8 rear, SP3 frame, paste: $117.48 The GPUs are 2/3 of the cost, but the boxes also run our CI/CD, which had become a bottleneck in my businesses. I hadn't seen anyone discuss this: they run Rust builds just fine if you tune them to prioritize inference. In our test, running builds alongside inference didn't measurably change throughput, and the builds were only 3-8% slower. Engine vLLM-Radiance 1.0.387 (vLLM 0.30.0, ROCm 7.14). Huge thanks to the Radiance folks; their R9700 work is what we run. Qwen/Qwen3.8-27B-FP8 (Qwen's official FP8 checkpoint), FP8 KV cache, the model's own MTP head with 8 draft tokens Two engines per box, TP=2 each, 8 sequences per engine, 256K max context, about 488K tokens of KV cache per engine Results , vllm bench serve , one box, 2x TP2: 1 user, MT-Bench: 53.1 tok/s, TTFT p50 125 ms 16 users, MT-Bench: 484 tok/s aggregate, about 40 tok/s per user 16 users, random 1024 in / 512 out: 623 tok/s aggregate, 837 W average for the four cards 32 users (a bench profile with max-num-seqs 32): 603 tok/s MTP depends a lot on the text. On our JSON extraction, 83% of drafts get accepted (7.6 tokens a step), vs 39% on MT-Bench (2.7 a step), so MT-Bench undersells it for structured output. Long prompts, 8 unique real-text prompts at once (4 per engine), 128 out: Context Prefill TTFT mean Decode, all 8 streams 4K 7,044 tok/s 2.8 s 271 tok/s 8K 7,495 tok/s 5.3 s 219 tok/s 16K 7,241 tok/s 11.0 s 180 tok/s 32K 6,696 tok/s 24.0 s 178 tok/s 64K 5,961 tok/s 54.4 s 171 tok/s 4x 128K (TP=4, one engine) 3,344 tok/s 100 s 130 tok/s 4x 256K (TP=4, one engine) 2,719 tok/s 242 s 135 tok/s Every prompt was unique (0% prefix cache hits). FP8 vs MXFP4 on a real workload The startup build ran MXFP4, so I had AI run that too (Radiance's fastest profile) on one box against our own graded extraction workbench: FP8: 98.0/100 correct, 4,477 validated jobs an hour MXFP4: 95.3/100, 4,819 an hour On a holdout set: FP8 94.0, MXFP4 90.0 So FP8 roughly halves the wrong answers for 2–7% less validated throughput. Sticking with FP8 was an easy call for this workload, where "false facts" that make it into the system are a real headache. For reference, our six Mac Studios (four M4 Max 128 GB, two M3 Ultra 512 GB) on MLX 8-bit scored 99/100, but at 723 an hour across all six. Plan A was buying more Macs, and keeping up would have taken at least 41 more, about $280k. I made a video of the build targeted more at beginners and people trying to move AI locally: https://youtu.be/o7k5Kj-ho-M Happy to answer questions. The first of which I expect to be how the heck were the Macs so slow, and I'm sure I'll get flamed haha.
