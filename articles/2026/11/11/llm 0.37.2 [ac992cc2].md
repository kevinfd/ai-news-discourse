---
id: "ac992cc25d49f443"
title: "llm 0.37.2"
url: "https://simonwillison.net/2026/Nov/11/llm"
link: "https://simonwillison.net/2026/Nov/11/llm"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-11T17:19:52Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm 0.37.2 \n Fixes a security issue reported by Daniel de Araujo in GHSA-v9h7-jj4g-f862 and GHSA-r639-rr7r-x72w . \n LLM has a mechanism called extra-openai-models.yaml - now managed by the new-in-0.37 llm openai endpoint add command - for using LLM with OpenAI-compatible API endpoints from other providers. \n Daniel reported two ways this could accidentally send your configured OpenAI…"
tags: ["projects", "security", "llm", "releases"]
orgs: ["OpenAI", "Anthropic", "Alibaba"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 140
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm 0.37.2

Simon Willison · Simon Willison · 2026-11-11

11th November 2026
Fixes a security issue reported by Daniel de Araujo in GHSA-v9h7-jj4g-f862 and GHSA-r639-rr7r-x72w.
LLM has a mechanism called extra-openai-models.yaml - now managed by the new-in-0.37 llm openai endpoint add command - for using LLM with OpenAI-compatible API endpoints from other providers.
Daniel reported two ways this could accidentally send your configured OpenAI API key to one of those providers: if the key named by api_key_name had never been stored, or if a responses: true model was run with -o chat_completions 1.
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
