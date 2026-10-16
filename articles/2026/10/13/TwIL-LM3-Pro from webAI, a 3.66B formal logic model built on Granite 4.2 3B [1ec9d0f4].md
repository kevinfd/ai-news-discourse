---
id: "1ec9d0f4c120946a"
title: "TwIL-LM3-Pro from webAI, a 3.66B formal logic model built on Granite 4.2 3B"
url: "https://reddit.com/r/LocalLLaMA/comments/1x502mt/twillm3pro_from_webai_a_366b_formal_logic_model"
link: "https://reddit.com/r/LocalLLaMA/comments/1x502mt/twillm3pro_from_webai_a_366b_formal_logic_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T15:42:08Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["CommonMinimum587"]
language: "en"
summary: "Been digging into this one for the last few days. 3.66B model built on IBM’s Granite 4.2 3B, post-trained only for formal logic. Entailment checking, rule induction, Lean proof critique. Not a general assistant. Recipe is LoRA SFT + checkpoint merging + RL against a programmatic verifier. Same recipe apparently lifted VibeThinker-3B from 37.4 to 54.1 on their logic score, so it’s not tied to one…"
tags: ["r/LocalLLaMA"]
orgs: ["IBM"]
topics: ["models & research"]
content_source: "post"
word_count: 318
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x502mt/twillm3pro_from_webai_a_366b_formal_logic_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# TwIL-LM3-Pro from webAI, a 3.66B formal logic model built on Granite 4.2 3B

Reddit · CommonMinimum587 · 2026-10-13

Been digging into this one for the last few days. 3.66B model built on IBM’s Granite 4.2 3B, post-trained only for formal logic. Entailment checking, rule induction, Lean proof critique. Not a general assistant. Recipe is LoRA SFT + checkpoint merging + RL against a programmatic verifier. Same recipe apparently lifted VibeThinker-3B from 37.4 to 54.1 on their logic score, so it’s not tied to one base. Headline numbers from the model card: Logic composite: 55.4 (vs 43.1 Granite base, 42.2 original TwIL-LM3, 41.2 VibeThinker-3B, 53.4 Qwen3-8B) Strict multiple choice logic: 41% vs 17% for the next model BBH logic: 95.4%Card itself calls the Qwen3-8B gap sampling noise, so effectively a tie against a model more than twice the size. Where it loses: gpt-oss-120b is still ahead on rule induction, entailment, and Lean formalization. General benchmarks average 79.0 (vs 81.0 VibeThinker-3B, 84.9 Qwen3-8B). It thinks long on logic tasks (~1,900 tokens/answer) and about a quarter of answers hit the length cap, so budget accordingly. The CPU story is where it got interesting for me. webAI published a benchmark showing it at ~10.5 tok/s on a CPU-only Xeon (15 GiB RAM, no GPU), 98x faster than Qwen3.8-27B on the same hardware. Size delta explains a lot of it, but if you’re running CPU-only that’s the real headlineRunning it: Q4_K_M GGUF is 2.09 GiB, runs on CPU or 4 GB VRAM. Q5/Q6/Q8 up to 3.63 GiB. Ollama, LM Studio, llama.cpp all supported, model card has the commands. Keep temp at 0 to match their numbers, 2048+ token budget so the thinking doesn’t get truncated. Their scores are BF16, Q4 isn’t benchmarked yet. Still want to test it on policy rules with exceptions and as a checker step in an agent pipeline before anything acts. Anyone else running it yet? Curious how Q4 holds up against the BF16 numbers, and whether the long thinking got in the way. Model card: https://huggingface.co/webAI-Official/TwIL-LM3-Pro
