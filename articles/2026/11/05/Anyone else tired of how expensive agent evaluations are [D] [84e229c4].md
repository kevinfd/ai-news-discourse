---
id: "84e229c4b6590b34"
title: "Anyone else tired of how expensive agent evaluations are? [D]"
url: "https://reddit.com/r/MachineLearning/comments/1xo8hlk/anyone_else_tired_of_how_expensive_agent"
link: "https://reddit.com/r/MachineLearning/comments/1xo8hlk/anyone_else_tired_of_how_expensive_agent"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T03:33:01Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Key_Recording9766"]
language: "en"
summary: "So I have been working on some general use agents that work with different domains but these require online simulations to test for some of the domains. And running agents in actual environments takes so much time and compute and then reproducing results is another headache. My goal is to test which VLMs can be better in general for agents irrespective of a singular domain. I found there’s a…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 175
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xo8hlk/anyone_else_tired_of_how_expensive_agent/"
score: null
comments: null
community: "r/MachineLearning"
---

# Anyone else tired of how expensive agent evaluations are? [D]

Reddit · Key_Recording9766 · 2026-11-05

So I have been working on some general use agents that work with different domains but these require online simulations to test for some of the domains. And running agents in actual environments takes so much time and compute and then reproducing results is another headache. My goal is to test which VLMs can be better in general for agents irrespective of a singular domain. I found there’s a benchmark called AgentVQA that tests how well models understand visual information without having to run these expensive full agent evaluations. And they do it all offline without setting up any kind of environments and also claim to have much cleaner data compared to other benchmarks available which have so many ambiguous samples. Do you guys think offline benchmarks like this could actually help reduce the need for online evals? I personally found it quite useful for the work I’m doing and it’s much cheaper and easier with this. I want to know what others think and if this might solve their problems. Here’s the benchmark: https://zlab-princeton.github.io/AgentVQA/
