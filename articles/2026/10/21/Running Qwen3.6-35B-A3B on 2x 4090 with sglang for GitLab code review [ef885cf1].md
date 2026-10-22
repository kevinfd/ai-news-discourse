---
id: "ef885cf11b2b7a25"
title: "Running Qwen3.6-35B-A3B on 2x 4090 with sglang for GitLab code review"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbogcj/running_qwen3635ba3b_on_2x_4090_with_sglang_for"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbogcj/running_qwen3635ba3b_on_2x_4090_with_sglang_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T14:19:33Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Professional-Pear351"]
language: "en"
summary: "I’m sharing a GitLab review agent I’ve been working on. The idea was to keep code reviews on hardware I run. It’s built on LangGraph.js and uses Qwen3.6-35B-A3B (QuantTrio AWQ, 4-bit) on sglang. The box is two 4090s over PCIe, no NVLink, TP=2. Decode is about 180 tok/s single stream at ~50k context and about 160 at ~110k. Prefill is 9-10k tok/s. At 8 concurrent requests I get 985 tok/s total. A…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 198
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbogcj/running_qwen3635ba3b_on_2x_4090_with_sglang_for/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Running Qwen3.6-35B-A3B on 2x 4090 with sglang for GitLab code review

Reddit · Professional-Pear351 · 2026-10-21

I’m sharing a GitLab review agent I’ve been working on. The idea was to keep code reviews on hardware I run. It’s built on LangGraph.js and uses Qwen3.6-35B-A3B (QuantTrio AWQ, 4-bit) on sglang. The box is two 4090s over PCIe, no NVLink, TP=2. Decode is about 180 tok/s single stream at ~50k context and about 160 at ~110k. Prefill is 9-10k tok/s. At 8 concurrent requests I get 985 tok/s total. A review run averages around 26 LLM calls and 2.3M tokens. As of now it has done 1,300+ reviews and about 70% of its comments get resolved by the author. It sometimes catches mistakes in code written with Claude Sonnet/Opus, in the harness’s own repo and in internal projects. I believe it’s good to have different model families in the workflow, you get different perspectives from each. Repetition is the common problem I face with local models (maybe it's the quants). Guardrails catch repeated tool calls and trailing questions, but the model looping on itself still ends about 7% of runs (56 of 847 on my dashboard). Launch flags and the benchmark: https://vrajpal-jhala.github.io/langgraph-harness/sglang-deployment The agent is MIT and also works with Ollama, OpenRouter, Gemini and Groq: https://github.com/vrajpal-jhala/langgraph-harness
