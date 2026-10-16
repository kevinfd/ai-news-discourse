---
id: "39158b2ff809fbbf"
title: "Using Absorbing Markov Chains + EmbeddingGemma 2 as a Decision Engine: ~2ms inference with 100% GTO Parity on Vegas Blackjack"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5wjps/using_absorbing_markov_chains_embeddinggemma_2_as"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5wjps/using_absorbing_markov_chains_embeddinggemma_2_as"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T16:55:08Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["inawhole"]
language: "en"
summary: "[UPDATE / RETRACTION: The \"100% GTO\" claim had a prompt-leakage bug] We patched the repo to pass strictly neutral states, here are the real, honest numbers: • Latency: Still ~2ms (ONNX + Absorbing Markov Chain). • True Zero-Shot GTO Parity: ~15% - 29% across all 340 canonical hands. **[Benefits of Tier 0 Absorbing Markov Chain + Embedding model] on JevBench, Tier 0 achieved 12 / 12 early exits…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 317
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5wjps/using_absorbing_markov_chains_embeddinggemma_2_as/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Using Absorbing Markov Chains + EmbeddingGemma 2 as a Decision Engine: ~2ms inference with 100% GTO Parity on Vegas Blackjack

Reddit · inawhole · 2026-10-14

[UPDATE / RETRACTION: The "100% GTO" claim had a prompt-leakage bug] We patched the repo to pass strictly neutral states, here are the real, honest numbers: • Latency: Still ~2ms (ONNX + Absorbing Markov Chain). • True Zero-Shot GTO Parity: ~15% - 29% across all 340 canonical hands. **[Benefits of Tier 0 Absorbing Markov Chain + Embedding model] on JevBench, Tier 0 achieved 12 / 12 early exits with 100% accuracy at 16.5 ms p50, and on Decision Index 0.3, it safely rejected 344 / 344 out-of-domain items with 0 false exits Gevva0 Cascading Decision Engine: Tier -1 · Static Rules ( <50 µs ): Hot-reloadable regex and keyword guards that run in microseconds without touching the GPU Tier 0 · Absorbing Markov Chains ( <3 ms ): Embeds queries into a 768D manifold using EmbeddingGemma-2 (740M) and solves random-walk absorption probabilities in closed form, hitting 100% accuracy on early exits with zero false exits on 344 out-of-domain items. Tier 1 · Fast-Path Logits ( ~35 ms ): Runs a single forward pass on Gemma 4 26B-A4B (MoE, 4B active) with a custom K=64 micro-head that slices the 262,144-row vocabulary down to just the 52 answer letters cutting output-head compute by 99.98% and resolving 77.9% of queries without generating a single token. Tier 2 · Hot-KV Bounded CoT ( ≤ 256 tokens ): Escalates the hardest 17.1% of requests into bounded Chain-of-Thought reasoning directly from the KV cache Tier 1 already prefilled ( reuse_kv=True ), eliminating double prompt processing and cutting long-context latency by up to 30%. Highlights: JevBench, Gevva0 beats Claude Opus 4.6 Thinking on chance-corrected intelligence ( 84.62 vs. 83.90 ) at a 44 ms median latency (vs. Opus's 4,850 ms) Decision Index 0.3, our 4B-active MoE cascade outperforms dense 27B models (like Kev 27B) at a 60 ms p50 —roughly 7× faster than 27B alternatives. 60 FPS Real-Time Game-Loop Ready (Pacman demo included) https://github.com/solvingSteve/Gevva0
