---
id: "6382c7f4f5236be2"
title: "35 domain-expert LoRAs on a MoE (Qwen3.6-35B-A3B) trained with MLX on one Mac Studio — what worked, what didn't, all Apache-2.0"
url: "https://reddit.com/r/LocalLLaMA/comments/1xqw6fr/35_domainexpert_loras_on_a_moe_qwen3635ba3b"
link: "https://reddit.com/r/LocalLLaMA/comments/1xqw6fr/35_domainexpert_loras_on_a_moe_qwen3635ba3b"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T11:18:48Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Holiday_Poetry_5133"]
language: "en"
summary: "Over the last months I trained 35 domain-expert LoRA adapters on Qwen3.6-35B-A3B (native MoE, 256 experts, 3B active) with MLX on a Mac Studio M3 Ultra 512 GB, BF16, no quantization during training. Everything is public: adapters, datasets, per-domain configs, router, training scripts. Things I learned the hard way: - Fusing a MoE LoRA into 8-bit produced garbage; only runtime BF16 adapter…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple"]
topics: ["models & research"]
content_source: "post"
word_count: 205
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqw6fr/35_domainexpert_loras_on_a_moe_qwen3635ba3b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 35 domain-expert LoRAs on a MoE (Qwen3.6-35B-A3B) trained with MLX on one Mac Studio — what worked, what didn't, all Apache-2.0

Reddit · Holiday_Poetry_5133 · 2026-11-08

Over the last months I trained 35 domain-expert LoRA adapters on Qwen3.6-35B-A3B (native MoE, 256 experts, 3B active) with MLX on a Mac Studio M3 Ultra 512 GB, BF16, no quantization during training. Everything is public: adapters, datasets, per-domain configs, router, training scripts. Things I learned the hard way: - Fusing a MoE LoRA into 8-bit produced garbage; only runtime BF16 adapter hot-swap was usable. Serving = one base loaded once + adapters swapped per request (~2 s). - A small MiniLM router over 34 domains tops out around top-1 46 %, top-3 70 % on my eval. Routing is the weak link, not the adapters. - On an independent audit bench, the base 35B model beat most of my specialist adapters. Only one domain (HTML/CSS) clearly gained. I now route almost everything to the base. Publishing a negative result felt more useful than hiding it. - `mx.random.normal` is not bit-exact across Apple GPU generations (M1 vs M3+). Reported upstream, docs PR merged in ml-explore/mlx last week. Repos: github.com/hypneum-lab/micro-kiki (adapters + router), github.com/ailiance/ailiance-mac-tuner (training stack, archived). HF: huggingface.co/hypneum-lab Question for the sub: has anyone gotten domain LoRAs to beat a strong MoE base at the 30B scale without full-parameter training? I'd like to compare routers.
