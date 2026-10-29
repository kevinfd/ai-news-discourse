---
id: "fbf39aab1b456b3a"
title: "A harness that records where an LLM agent’s tool arguments came from, before the tool runs [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xhnoo2/a_harness_that_records_where_an_llm_agents_tool"
link: "https://reddit.com/r/MachineLearning/comments/1xhnoo2/a_harness_that_records_where_an_llm_agents_tool"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T13:11:49Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Jay299792458"]
language: "en"
summary: "I've been thinking about AI agent safety, and I built a test harness to check my own results. I think it may be useful to people who study models too. It records where each tool argument came from before the tool executes, measures whether the same input gives the same decision, and tests whether a model takes arguments from someone else's text instead of its user's. If you modify the harness,…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "post"
word_count: 80
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xhnoo2/a_harness_that_records_where_an_llm_agents_tool/"
score: null
comments: null
community: "r/MachineLearning"
---

# A harness that records where an LLM agent’s tool arguments came from, before the tool runs [P]

Reddit · Jay299792458 · 2026-10-28

I've been thinking about AI agent safety, and I built a test harness to check my own results. I think it may be useful to people who study models too. It records where each tool argument came from before the tool executes, measures whether the same input gives the same decision, and tests whether a model takes arguments from someone else's text instead of its user's. If you modify the harness, it can probably be used for much more. https://github.com/Jang-woo-AnnaSoft/execution-state-preflight/blob/main/hooks-example/README.md
