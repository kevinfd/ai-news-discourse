---
id: "263bfb9c36537d30"
title: "I trained a 348M-active MoE on ~11B tokens. It scores 85.5% vs Qwen2.5-1.5B's 53.3% on shuffled fact chains. GGUF + eval set — please try to break it."
url: "https://reddit.com/r/LocalLLaMA/comments/1xssj9q/i_trained_a_348mactive_moe_on_11b_tokens_it"
link: "https://reddit.com/r/LocalLLaMA/comments/1xssj9q/i_trained_a_348mactive_moe_on_11b_tokens_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T17:11:20Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Significant-Serve-58"]
language: "en"
summary: "I've been recently working a small sparse MoE, and I've got interesting results I'd like strangers to invalidate. Tldr; I train small models and got surprising results and seek invalidation. It's not a general assistant, and I'm not claiming it is. Edit: Trained on a single 5090. Maybe people wonder about that. The model has 1.17B stored parameters, roughly 348M active per token, scrath trained…"
tags: ["r/LocalLLaMA"]
orgs: ["Meta", "Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 430
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xssj9q/i_trained_a_348mactive_moe_on_11b_tokens_it/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I trained a 348M-active MoE on ~11B tokens. It scores 85.5% vs Qwen2.5-1.5B's 53.3% on shuffled fact chains. GGUF + eval set — please try to break it.

Reddit · Significant-Serve-58 · 2026-11-10

I've been recently working a small sparse MoE, and I've got interesting results I'd like strangers to invalidate. Tldr; I train small models and got surprising results and seek invalidation. It's not a general assistant, and I'm not claiming it is. Edit: Trained on a single 5090. Maybe people wonder about that. The model has 1.17B stored parameters, roughly 348M active per token, scrath trained on approx 11B tokens including SFT. As a comparison, Qwen2.5 reports up to 18T training tokens across its family, while SmolLM2-1.7B reports 11T. THE ASK A chain of relational facts ("A is taller than B", "B is taller than C", etc.), with the facts shuffled and the model asked to identify an endpoint. Depth is chain length. Each result is out of 512 questions across four families. All models received the same questions, using their native chat templates, greedy decoding, and a 16-token answer budget. RESULTS (correct out of 512) Depth 1: ConeML 487 | Qwen 481 | SmolLM2 426 | Llama 267 | Gemma 343 Depth 3: ConeML 471 | Qwen 410 | SmolLM2 221 | Llama 197 | Gemma 224 Depth 5: ConeML 438 | Qwen 273 | SmolLM2 155 | Llama 136 | Gemma 138 Depth 8: ConeML 343 | Qwen 202 | SmolLM2 102 | Llama 73 | Gemma 100 Depth 12: ConeML 240 | Qwen 105 | SmolLM2 58 | Llama 47 | Gemma 79 Depth 24: ConeML 74 | Qwen 47 | SmolLM2 21 | Llama 13 | Gemma 19 Models used for comparison: Qwen2.5-1.5B, SmolLM2-1.7B, Llama-3.2-1B, Gemma-3-1B. WHERE IT FAILS Despite the endpoint results, ConeML only scores 13.8% on interior pairwise comparisons within those chains, below the 50% two-choice reference. It also gets only 12/164 on HumanEval and 0/6 successful two-turn follow-ups. So it seems to find the ends without reliably understanding the relationships in the middle. I don't know whether this reflects a specialized learned strategy, an architectural effect, or a flaw in my testing. WHAT I'M ASKING Run the depth-5 shuffled evaluation and post your score. My FP32 reference result is 438/512 (85.5%). The Q8 GGUF is 1.25 GB and runs on CPU. The 512-question set and scorer are in the repository. I haven't tested to see if it reproduces the full FP32 result. If you get something different, find a scoring problem, or spot anything else wrong, I'd really like to know." Model: https://huggingface.co/ConeML/coneml-1.2b-experimental Earlier technical paper (base lineage, LAMBADA vs Pythia at approximately matched training positions): https://doi.org/10.5281/zenodo.23117644 Other releases: https://huggingface.co/ConeML My own bias is my largest enemy and hope to get some honest feedback.
