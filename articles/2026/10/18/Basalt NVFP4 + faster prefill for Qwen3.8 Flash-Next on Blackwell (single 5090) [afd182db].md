---
id: "afd182dbe6098854"
title: "Basalt: NVFP4 + faster prefill for Qwen3.8 Flash-Next on Blackwell (single 5090)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8piwz/basalt_nvfp4_faster_prefill_for_qwen38_flashnext"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8piwz/basalt_nvfp4_faster_prefill_for_qwen38_flashnext"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T00:26:36Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["jesdga95"]
language: "en"
summary: "Basalt: Qwen 3.8 FN NVFP4, single 5090 Hi guys, so I finally got a RAM upgrade and have been working on the top two pain points from Basalt: NVFP4 support and faster prefill. NVFP4: Basalt runs NVFP4 natively now, a new .basalt pack keeps stock NVIDIA experts and stores the dense layers as Q6_K. Numbers for a 5090 (400w) + 128 GB of DDR5 RAM, single stream: - struct: 304 tok/s - prose: 183 tok/s…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Alibaba"]
topics: ["chips & infrastructure", "business & funding"]
content_source: "post"
word_count: 162
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8piwz/basalt_nvfp4_faster_prefill_for_qwen38_flashnext/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Basalt: NVFP4 + faster prefill for Qwen3.8 Flash-Next on Blackwell (single 5090)

Reddit · jesdga95 · 2026-10-18

Basalt: Qwen 3.8 FN NVFP4, single 5090 Hi guys, so I finally got a RAM upgrade and have been working on the top two pain points from Basalt: NVFP4 support and faster prefill. NVFP4: Basalt runs NVFP4 natively now, a new .basalt pack keeps stock NVIDIA experts and stores the dense layers as Q6_K. Numbers for a 5090 (400w) + 128 GB of DDR5 RAM, single stream: - struct: 304 tok/s - prose: 183 tok/s - w/ peer gpu (5060 Ti): struct 479 / prose 239 Quality vs Q8_0 (100 chunks): PPL 3.308 (Q8_0: 3.286), KLD 0.068, 91.5% same top-1. Prefill: 8,582 tok/s on a 64K prompt (7.6s to first token). Against Infernix on the same NVFP4 weights and same box it's up to 1.3x on decode and 1.6x on prefill. Also merged a bunch of stability and performance fixes over the last week, coming up next Unsloth Q4 + Q8 (near lossless) tuning. Give it a try: Repo: github.com/jesdga95/basalt HF: huggingface.co/jesdga/Qwen3.8-Flash-Next-Basalt
