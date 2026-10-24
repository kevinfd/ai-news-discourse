---
id: "7f5e01c18a0e4cda"
title: "ReVolta 0.1.2: DFlash speculative decoding running on 4× V100"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdqgps/revolta_012_dflash_speculative_decoding_running"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdqgps/revolta_012_dflash_speculative_decoding_running"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T21:21:54Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Major_Ingenuity_6364"]
language: "en"
summary: "Quick release post. I maintain ReVolta, a vLLM fork (through 1Cat-vLLM) that keeps my home server useful — 4× V100 32GB PCIe, no NVLink. Today's 0.1.2 adds DFlash2 speculative decoding on SM70. I haven't seen DFlash running on Volta anywhere else, so this may be the first one out there. The drafter is incoai's DFlash2 checkpoint: it drafts an 8-token block from the target's hidden states and the…"
tags: ["r/LocalLLaMA"]
orgs: ["China", "Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 241
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdqgps/revolta_012_dflash_speculative_decoding_running/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# ReVolta 0.1.2: DFlash speculative decoding running on 4× V100

Reddit · Major_Ingenuity_6364 · 2026-10-23

Quick release post. I maintain ReVolta, a vLLM fork (through 1Cat-vLLM) that keeps my home server useful — 4× V100 32GB PCIe, no NVLink. Today's 0.1.2 adds DFlash2 speculative decoding on SM70. I haven't seen DFlash running on Volta anywhere else, so this may be the first one out there. The drafter is incoai's DFlash2 checkpoint: it drafts an 8-token block from the target's hidden states and the target verifies in one pass. Model is Qwen3.8 Flash-Next (AWQ), 512K context, FP8 KV with CPU offload, TP4 + DCP2. Some numbers, greedy with 512-token replies: DFlash2 MTP4 1 request, English code 201 tok/s 163 1 request, English reasoning 195 163 1 request, Chinese 85–101 100–105 8 requests, mixed 331 357 The KV pool gets about 10% bigger too, up to 1.27M tokens. Where it doesn't help: Chinese is slower than plain MTP (the drafter was trained on English, acceptance is worse), 8 concurrent requests are a bit slower, and on replays of my real agent sessions it's basically a wash. So MTP stays the default and DFlash is opt-in. I kept it because single-stream English/code is what I run most of the day. The rest of 0.1.2 is mostly fixes — tool calling, the Anthropic messages endpoint, and large images getting resized instead of eating the whole token budget. If anyone else is still running V100s, I'd be interested in numbers from an NVLink box. GitHub: https://github.com/Leonccaa/ReVolta Release notes: https://github.com/Leonccaa/ReVolta/releases/tag/v0.1.2 Drafter: https://huggingface.co/incoai/Qwen3.8-Flash-Next-DFlash2
