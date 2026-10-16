---
id: "3d3aec967750f992"
title: "Why do LLM pelicans look like this?"
url: "https://arcfu.com/post/the-emperor-pelican-has-no-clothes"
link: "https://arcfu.com/post/the-emperor-pelican-has-no-clothes"
source: "Aman Rusia"
domain: "arcfu.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-14T16:33:34Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["pcwelder"]
language: "en"
summary: "⚠️ Frontier AI models still fall significantly short of human designers on design creativity. ⚠️\nIntroducing Design Creativity Bench, a new benchmark evaluating AI models’ creativity on UI design tasks.\nDespite rapid advances in their ability to generate functional websites and product UIs, leading AI models still struggle to make creative design decisions.\nWe evaluated 16 frontier models across…"
tags: []
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 195
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50090443"
score: 162
comments: 138
community: "Hacker News"
---

# Why do LLM pelicans look like this?

Aman Rusia · pcwelder · 2026-10-14

⚠️ Frontier AI models still fall significantly short of human designers on design creativity. ⚠️
Introducing Design Creativity Bench, a new benchmark evaluating AI models’ creativity on UI design tasks.
Despite rapid advances in their ability to generate functional websites and product UIs, leading AI models still struggle to make creative design decisions.
We evaluated 16 frontier models across 80 open-ended UI tasks, each adapted to two distinct product domains alongside human designer references.
Existing UI benchmarks often measure a single output quality metric. Instead, we measure three dimensions of design creativity:
- – Originality: How distinct a model's designs are from other models' outputs for the same brief.
- – Creative Range: How much a model adapts its design decisions when the product domain changes.
- – Appropriateness: How well the generated UI satisfies the functional requirements of the brief.
The results reveal a substantial gap in overall creativity: The best model, @OpenAI GPT-6 Astra, scores 65.5 against a human reference of 92.3.
We're publishing the full leaderboard, methodology, and reproducible evaluation framework to make design creativity a measurable dimension of frontier model capability.
📄 Paper: https://arxiv.org/abs/2610.11539
🤗 HuggingFace Datasets: https://huggingface.co/datasets/Kombai/design-creativity-bench
🔗 Github: https://github.com/kombai-io/design-creativity-bench/
