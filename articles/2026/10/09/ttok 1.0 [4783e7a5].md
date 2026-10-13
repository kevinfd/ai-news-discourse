---
id: "4783e7a5e36c9d75"
title: "ttok 1.0"
url: "https://simonwillison.net/2026/Oct/9/ttok"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-09T00:34:43Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: ttok 1.0 \n I released ttok 0.4 , ran uv tool upgrade ttok , piped a file into the new version... and realized that it was defaulting to the GPT-4 tokenizer when it should very clearly default to GPT-5/GPT-6 instead! \n I figured switching the default was a reasonable excuse to finally ship a 1.0. \n OpenAI haven't actually confirmed that GPT-6 uses the same tokenizer as the GPT-5 family…"
tags: ["projects", "ai", "openai", "generative-ai", "llms", "tokenization"]
orgs: ["OpenAI", "Anthropic"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 187
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# ttok 1.0

Simon Willison · Simon Willison · 2026-10-09

9th October 2026
I released ttok 0.4, ran uv tool upgrade ttok, piped a file into the new version... and realized that it was defaulting to the GPT-4 tokenizer when it should very clearly default to GPT-5/GPT-6 instead!
I figured switching the default was a reasonable excuse to finally ship a 1.0.
OpenAI haven't actually confirmed that GPT-6 uses the same tokenizer as the GPT-5 family yet - there's an angry issue about it - but I found this commit by William Liu which reports on an experiment he ran confirming that the tokenizers are likely the same:
All seven GPT models (5.5, 5.6 Sol/Terra/Luna, 6 Astra/Sol/Luna) report 44,794 tokens and match each other on every one of the 31 fixtures. GPT-6 introduces no input-count change on this corpus.
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
