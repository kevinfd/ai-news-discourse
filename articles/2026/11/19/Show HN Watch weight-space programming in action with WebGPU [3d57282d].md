---
id: "3d57282d181c15b5"
title: "Show HN: Watch weight-space programming in action with WebGPU"
url: "https://tabbyml.github.io/weight-space-playground"
link: "https://tabbyml.github.io/weight-space-playground"
source: "Weight-Space Playground"
domain: "tabbyml.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-19T15:32:47Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["wsxiaoys"]
language: "en"
summary: "I wanted to build a full weight-space programming loop entirely in the browser with WebGPU: let an LLM inspect Qwen3.5-0.8B, edit its weights, evaluate, and repeat. the full loop needed too much VRAM. so I turned it into an interactive walkthrough of a concrete example: editing 0.016% of a model's weights to reduce reasoning loops, no gradient descent. Based on exp8 of “Sparks of Weight-Space…"
tags: []
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 174
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50561436"
score: 38
comments: 6
community: "Hacker News"
---

# Show HN: Watch weight-space programming in action with WebGPU

Weight-Space Playground · wsxiaoys · 2026-11-19

Press play. Thinking text appears in grey, the final answer in dark ink.
The problem: repeated reasoning
In the original experiment, Qwen3.5-0.8B often repeated its reasoning until it hit the token limit before reaching an answer. These figures come from the original experiment’s published evaluation.
The intervention: a small weight edit
It subtracts one direction from 64 neurons' output weights (ffn_down) in
      layers 15 and 19  -  131,072 of ~800M weights.
Stripes drawn ~25× wider than true scale - at real size they would be invisible.
The result: fewer capped runs
The original experiment reported fewer capped runs and higher MATH-500 accuracy. Some runs still reached the token limit.
A familiar experimental loop
Start with a few examples of unwanted behavior, propose an edit, and test whether it helps. Then check other examples for regressions. People working with prompts or fine-tuning will recognize the pattern. An AI agent makes this loop practical at the weight level: it can inspect tensors, write editing code, run evaluations, and use the results to choose the next experiment.
