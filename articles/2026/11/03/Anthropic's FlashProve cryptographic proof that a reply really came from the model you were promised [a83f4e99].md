---
id: "a83f4e9948e93d0a"
title: "Anthropic's FlashProve: cryptographic proof that a reply really came from the model you were promised"
url: "https://reddit.com/r/artificial/comments/1xn4g6l/anthropics_flashprove_cryptographic_proof_that_a"
link: "https://reddit.com/r/artificial/comments/1xn4g6l/anthropics_flashprove_cryptographic_proof_that_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T20:37:55Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["winer666"]
language: "en"
summary: "Anthropic published research on November 2 (with collaborators from EPFL, MIT and others) on provable inference: a system called FlashProve that uses zkSNARKs to prove a response was produced by a specific, committed set of model weights, without revealing those weights. The idea is to let anyone from independent evaluators to end users check they were served the model they were promised, and to…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Meta"]
topics: ["models & research", "policy & regulation"]
content_source: "post"
word_count: 209
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xn4g6l/anthropics_flashprove_cryptographic_proof_that_a/"
score: null
comments: null
community: "r/artificial"
---

# Anthropic's FlashProve: cryptographic proof that a reply really came from the model you were promised

Reddit · winer666 · 2026-11-03

Anthropic published research on November 2 (with collaborators from EPFL, MIT and others) on provable inference: a system called FlashProve that uses zkSNARKs to prove a response was produced by a specific, committed set of model weights, without revealing those weights. The idea is to let anyone from independent evaluators to end users check they were served the model they were promised, and to catch tampering with the token stream in between. Some numbers from the announcement: tested on Llama 4 Maverick (a 400B-parameter mixture-of-experts model, 4-bit weights), proving takes roughly 70 to 95 times the GPU time of running the model on vLLM. Code and Lean formal proofs are open source under Apache 2.0. Anthropic calls it a research prototype, and the limits are real: contexts up to 1,024 tokens only, the proof covers an integer version of the model under greedy decoding, and the model architecture itself is not hidden. What interests me: if proving gets cheap enough, does this change how we think about trusting hosted models at all? Or does the 70-95x overhead mean this stays a niche tool for audits and regulated settings? And would a proof like this matter to you as a user, or is it only meaningful to evaluators and regulators?
