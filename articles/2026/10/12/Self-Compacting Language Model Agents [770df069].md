---
id: "770df069ccb53165"
title: "Self-Compacting Language Model Agents"
url: "https://machinelearning.apple.com/research/self-compacting-language-agents"
link: "https://machinelearning.apple.com/research/self-compacting-language-agents"
source: "Apple Machine Learning Research"
domain: "machinelearning.apple.com"
source_type: "research"
collector: "rss"
date: "2026-10-12T00:00:00Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: []
language: "en"
summary: "Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. We propose…"
tags: []
orgs: []
topics: ["models & research", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 430
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Self-Compacting Language Model Agents

Apple Machine Learning Research · 2026-10-12

Self-Compacting Language Model Agents
AuthorsTianjian Li†, Jingyu Zhang†, William Jurayj†, Xi Wang†, Chuanyang Jin†, Mehrdad Farajtabar, Eric Nalisnick†, Daniel Khashabi†
content type paperpublished October 2026
Long agent traces composed of chains of thought and tool calls accumulate stale content that anchor subsequent generations, and eventually outgrow the context window. Existing scaffolds mitigate it with fixed-interval compaction triggered at a token threshold. Such triggers pay no heed to trajectory structure, risking discard of partial results mid-derivation or mid-search. We propose SELFCOMPACT, a scaffold that allows the model itself to decide when and how to compact. Specifically, it pairs two inference-time elements: (i) a compaction tool the model invokes to summarize the accumulated context, and (ii) a lightweight rubric specifying when to fire (a sub-task has resolved, or the trajectory is converging) and when to suppress (mid-derivation, or when stuck). Both are needed. The tool alone is unevenly used across open-weight models, often invoked at unhelpful moments or not at all; the rubric alone cannot act. Together, they elicit effective adaptive compaction without any fine-tuning or external supervision. We present empirical results on six benchmarks (competitive math and agentic search) and seven models. Our results show that SELFCOMPACT matches or exceeds fixed-interval summarization at a fraction of the token cost, improving over a no-summarization baseline by up to 18.1 points on math and 5–9 points on agentic search at 30–70% lower per-question cost. Our results expose a meta-cognitive gap: although unprompted models cannot reliably tell when their own context is rotting, a lightweight rubric closes this gap, reframing when to compact as a capability that scaffolds can supply without training.
- † Johns Hopkins University
RISED: Rubrics for Agentic Multi-Environment Selection and Self-Distillation
October 6, 2026research area Data Science and Annotation, research area Speech and Natural Language Processing
Training a single LLM agent jointly across diverse interactive environments has attracted increasing attention as a route to generalist agents. Existing curriculum and data-selection strategies often allocate training at the environment level or prioritize local reward-based signals, without explicitly considering relationships between current rollouts across environments for prompt-group selection. Meanwhile, as environments are learned at…
From Preferences to Principles: Rubric-Based Alignment for Grounded Knowledge Answers
August 27, 2026research area Methods and Algorithms, research area Speech and Natural Language Processing
Designing effective reward signals for open-domain question answering is challenging because high-quality responses must simultaneously satisfy multiple aspects of answer quality that are difficult to capture with a holistic scalar objective. We introduce a rubric-based reward framework that generates query-specific rubrics grounded in retrieved evidence and decomposed into multiple quality dimensions, providing fine-grained supervision during…
