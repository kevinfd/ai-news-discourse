---
id: "e86a87f3e04452b0"
title: "Clover 2: dense 27.8B base + 7 LoRA experts routed per token, not a static merge, weights public"
url: "https://reddit.com/r/LocalLLaMA/comments/1xyb7jw/clover_2_dense_278b_base_7_lora_experts_routed"
link: "https://reddit.com/r/LocalLLaMA/comments/1xyb7jw/clover_2_dense_278b_base_7_lora_experts_routed"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T04:35:28Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["bakatristan"]
language: "en"
summary: "Disclosure: I’m with the team that built this. Wanted to share something a little different from the usual finetune drop. Clover 2 keeps a base model and 7 trained LoRA adapters (roleplay, general assistant, security, math, long-document, efficiency, knowledge) separate at inference time. A trained router picks the right expert(s) per token live, with a null slot that falls back to plain base…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 192
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyb7jw/clover_2_dense_278b_base_7_lora_experts_routed/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Clover 2: dense 27.8B base + 7 LoRA experts routed per token, not a static merge, weights public

Reddit · bakatristan · 2026-11-17

Disclosure: I’m with the team that built this. Wanted to share something a little different from the usual finetune drop. Clover 2 keeps a base model and 7 trained LoRA adapters (roleplay, general assistant, security, math, long-document, efficiency, knowledge) separate at inference time. A trained router picks the right expert(s) per token live, with a null slot that falls back to plain base when nothing specialized applies. So it’s not a merged blend, the model actually makes a decision at every token. Real benchmark gains over the untouched base: meaningful jumps on GSM8K/MATH-500/GSM-Hard, a solid bump on LongBench-v2, and a measurable drop in generic AI-writing tics on creative writing specifically. Everything’s public: base model, all 7 adapters in standard PEFT format, the trained router, and the vLLM plugin to run it with the real per-token behavior: https://huggingface.co/kitaniai/clover-2 Heads up if you’re planning to self-host: no GGUF yet, the hybrid attention architecture’s llama.cpp support is still bleeding-edge. vLLM is the supported path right now. If anyone wants to try it, it's free for the next week at https://kitani.ai/ , with no card required. We also support ZDR and have a clear privacy policy.
