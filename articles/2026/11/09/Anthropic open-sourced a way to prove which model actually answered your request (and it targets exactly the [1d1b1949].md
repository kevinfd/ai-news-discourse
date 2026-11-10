---
id: "1d1b1949a7c108d7"
title: "Anthropic open-sourced a way to prove which model actually answered your request (and it targets exactly the \"is my provider serving a quantized model?\" problem)"
url: "https://reddit.com/r/ClaudeAI/comments/1xrydq5/anthropic_opensourced_a_way_to_prove_which_model"
link: "https://reddit.com/r/ClaudeAI/comments/1xrydq5/anthropic_opensourced_a_way_to_prove_which_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T17:47:11Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["javimbuilds"]
language: "en"
summary: "Anthropic recently released FlashProve, a research prototype (Apache 2.0) for zero-knowledge proofs of LLM inference. The provider commits to a set of weights, its GPU generates a proof for each reply, and anyone can verify that proof on a regular CPU in seconds without ever seeing the weights. The demo runs Llama 4 Maverick at full size on a single H100, at about 110 prefill tokens/sec in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Meta"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 166
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrydq5/anthropic_opensourced_a_way_to_prove_which_model/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic open-sourced a way to prove which model actually answered your request (and it targets exactly the "is my provider serving a quantized model?" problem)

Reddit · javimbuilds · 2026-11-09

Anthropic recently released FlashProve, a research prototype (Apache 2.0) for zero-knowledge proofs of LLM inference. The provider commits to a set of weights, its GPU generates a proof for each reply, and anyone can verify that proof on a regular CPU in seconds without ever seeing the weights. The demo runs Llama 4 Maverick at full size on a single H100, at about 110 prefill tokens/sec in batches of 24. The protocol's soundness is machine-checked in Lean 4. The catches: each proof is ~18.8 MB, checks only one output token, the context is capped at 1,024 tokens, and the repo is marked "not maintained". As someone building on top of APIs, this is the first time I've seen a real answer to "how do I know I'm getting the model I pay for" instead of just running evals and hoping. Repo: https://github.com/anthropics/FlashProve/ Would you actually pay a bit more for an inference provider that ships verifiable proofs, or does the overhead kill it for anything practical?
