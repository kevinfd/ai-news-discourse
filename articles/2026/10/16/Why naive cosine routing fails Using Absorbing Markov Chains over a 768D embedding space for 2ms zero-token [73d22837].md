---
id: "73d22837648446ef"
title: "Why naive cosine routing fails: Using Absorbing Markov Chains over a 768D embedding space for <2ms zero-token intent triage (before waking the LLM)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7l0ct/why_naive_cosine_routing_fails_using_absorbing"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7l0ct/why_naive_cosine_routing_fails_using_absorbing"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T16:34:18Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["inawhole"]
language: "en"
summary: "What you're looking at: When routing support tickets, agent tool calls, or classification queries, direct cosine similarity (cos(q, option)) gets easily baited by surface keywords. Example alert says: \"Checkout payment webhook failed due to replica WAL lock.\" Naive cosine sees \"Checkout payment\" and routes straight to B: Billing & Stripe (red dashed line). Instead of jumping \"as the crow flies,\"…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 220
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7l0ct/why_naive_cosine_routing_fails_using_absorbing/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Why naive cosine routing fails: Using Absorbing Markov Chains over a 768D embedding space for <2ms zero-token intent triage (before waking the LLM)

Reddit · inawhole · 2026-10-16

What you're looking at: When routing support tickets, agent tool calls, or classification queries, direct cosine similarity (cos(q, option)) gets easily baited by surface keywords. Example alert says: "Checkout payment webhook failed due to replica WAL lock." Naive cosine sees "Checkout payment" and routes straight to B: Billing & Stripe (red dashed line). Instead of jumping "as the crow flies," our Semantic Triage engine projects the query onto a 60-node domain manifold (Q) and solves an Absorbing Markov Chain (B = (I - Q)^-1 * R) directly on the GPU in <0.05ms. The random walk steps through Idempotency Key -> Replica Write -> WAL Lock and absorbs cleanly into A: Core Database (86%) without waking the LLM. JevBench Results Tier 0 (AMC + EmbeddingGemma2) Avg: 22ms p50 - 11 items 4.58% (11/11) 100.00% Tier 1 (Gemma4 26B A4B) Avg: 42ms p50 - 188 items 78.33% (172/188) 91.49% Tier 2 (Gemma4 + CoT) Avg: 1,560ms p50 - 41 items 17.08% (31/41) 75.61% 4-Tier Cascade (Gevva0) Avg: 46ms p50 (308ms mean) - 240 items 100.0% (214/240) 89.17% Note on Tier 0 latency: ~1.5ms on short prompts with cached/static candidates (Suite 650: 76/76 at 100% precision) vs. ~22ms when embedding unseen dynamic options on 400-token contexts. Tripwires: Guard 1: Negation & Syntax Guard 2: Manifold Proximity (OOD) Guard 3: Entropy & Margin Gate
