---
id: "38f8cbc7334120ae"
title: "llm-openai-decisions 0.1a0"
url: "https://simonwillison.net/2026/Oct/6/llm-openai-decisions"
link: "https://simonwillison.net/2026/Oct/6/llm-openai-decisions"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-06T23:04:13Z"
published_date: "2026-10-06"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm-openai-decisions 0.1a0 \n OpenAI released their new Jev-style Decisions API , as previously announced at last week's DevDay. \n Since I already have an llm-typesafe plugin for talking to Jev, I had GPT-6 Astra read the new OpenAI API documentation and build an llm-openai-decisions plugin inspired by llm-typesafe . \n Unlike Jev, the new gpt-6-luna decision model supports image input in…"
tags: ["openai", "llm", "coding-agents", "jev"]
orgs: ["OpenAI", "Anthropic"]
topics: ["business & funding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 225
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm-openai-decisions 0.1a0

Simon Willison · Simon Willison · 2026-10-06

6th October 2026
OpenAI released their new Jev-style Decisions API, as previously announced at last week's DevDay.
Since I already have an llm-typesafe plugin for talking to Jev, I had GPT-6 Astra read the new OpenAI API documentation and build an llm-openai-decisions plugin inspired by llm-typesafe.
Unlike Jev, the new gpt-6-luna decision model supports image input in addition to text. Both models charge for input it and not for output: OpenAI's is 10 cents per million input tokens, Jev's is 4.2 cents per million.
Otherwise the API shape is very similar to Jev, at least conceptually. Jev supports three question types for yes/no, choices, or scores. OpenAI Decisions supports the same three types.
Install the plugin like this:
llm install llm-openai-decisions
Here's an example query against an image attachment:
llm -m openai-decisions/gpt-6-luna \
  -a https://static.simonwillison.net/static/2025/two-pelicans.jpg \
  -s 'Does this image contain any mammals?'
And example output:
{"type": "predicate", "name": "evaluation", "probability": 0.0}
Consult the README for full details of how to run the other types of questions.
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
