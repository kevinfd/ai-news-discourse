---
id: "bd7b5fc297108a05"
title: "[Paper] SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding - By Qwen"
url: "https://reddit.com/r/LocalLLaMA/comments/1xoo0pp/paper_specopd_branchparallel_onpolicy"
link: "https://reddit.com/r/LocalLLaMA/comments/1xoo0pp/paper_specopd_branchparallel_onpolicy"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:03:58Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["pmttyji"]
language: "en"
summary: "Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on acceptance length. On-policy distillation (OPD) can push well-trained drafters beyond acceptance-length plateaus, yet…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "policy & regulation", "agents & coding"]
content_source: "post"
word_count: 237
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoo0pp/paper_specopd_branchparallel_onpolicy/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding - By Qwen

Reddit · pmttyji · 2026-11-05

Speculative decoding (SD) accelerates large language model inference by reducing the sequential cost of token-by-token generation. Advanced SD methods reduce proposal cost with parallel drafters that predict entire blocks in one forward pass, but overall speedup still depends on acceptance length. On-policy distillation (OPD) can push well-trained drafters beyond acceptance-length plateaus, yet conventional pipelines collect supervision through sequential draft-and-verify rollouts. Our key insight is that onpolicy supervision need not inherit these dependencies: a draft block can be supervised using only its reference prefix and draft-sampled history. We propose SpecOPD, a branch-parallel OPD framework that parallelizes draft sampling and target supervision across independent branches drawn from the evolving drafter policy at reference anchors. We pack these branches into proposal trees to share target-prefix computation, using tree masks for full attention, branch-consistent indexer groups for sparse attention, and indexed state replay for linear attention to preserve each branch’s history. We train the drafter with an E2E-TV surrogate that directly targets acceptance length. Our study spans 8B full-attention (GQA), 27B full–linear (GQA–GDN), and 125B sparse–linear (QSA–GDN) targets, three parallel draft architectures (DFlash, DSpark, and DFlash V2), and four task domains (dialogue, coding, mathematics, and agentic). SpecOPD achieves up to 41.45% higher mean acceptance length, 16.09× supervised-token throughput over sequential-rollout OPD under native configurations, and up to 3.56× generation speedup over autoregressive decoding . Paper : https://qwenapp.github.io/SpecOPD/specopd-paper.pdf Project/Blog : https://qwenapp.github.io/SpecOPD/en.html GitHub : https://github.com/QwenApp/SpecOPD Tweet 1 : https://x.com/xuyang_liu16/status/2117614595728986227 Tweet 2 : https://x.com/junzhang_zj/status/2117812597856895164
