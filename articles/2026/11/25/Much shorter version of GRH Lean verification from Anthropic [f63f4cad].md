---
id: "f63f4cad14680799"
title: "Much shorter version of GRH Lean verification from Anthropic"
url: "https://github.com/lsernau/grh-lean"
link: "https://github.com/lsernau/grh-lean"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-25T21:48:10Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["nb-t"]
language: "en"
summary: "Research artifact. Not maintained and not accepting contributions.\nA Lean 4 proof of the Riemann Hypothesis and of the Generalized Riemann\nHypothesis for Dirichlet L-functions, built on Mathlib and using only the\naxioms propext, Classical.choice and Quot.sound.\nThe proof is based on Levent Alpöge's, with Claude (https://alpo.ge/remark.pdf). This repository is a shorter version, produced in…"
tags: []
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 178
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50648050"
score: 483
comments: 271
community: "Hacker News"
---

# Much shorter version of GRH Lean verification from Anthropic

GitHub · nb-t · 2026-11-25

Research artifact. Not maintained and not accepting contributions.
A Lean 4 proof of the Riemann Hypothesis and of the Generalized Riemann
Hypothesis for Dirichlet L-functions, built on Mathlib and using only the
axioms propext, Classical.choice and Quot.sound.
The proof is based on Levent Alpöge's, with Claude (https://alpo.ge/remark.pdf). This repository is a shorter version, produced in collaboration with my colleagues at Anthropic, and Claude.
- grh/: readable edition, about 300,000 lines. Start at grh/GUIDE.md.
- grh-compact/: the same five theorems, about 76,000 lines.
Each folder is its own Lake project with its own README.
Needs Lean v4.35.0 and Mathlib at commit 56a00585. In either folder:
lake exe cache get
lake build
lake env lean scripts/PrintAxioms.lean
A build takes one to two hours on 12 cores with 24 GB of memory (about 85 minutes more if the Mathlib cache is missing).
The proof has passed machine checks only, listed in each folder's README. No mathematician has read it through, and no paper comes with it.
Apache 2.0, Copyright 2026 Anthropic, PBC. See LICENSE, and NOTICE and
ATTRIBUTION.md in each folder.
