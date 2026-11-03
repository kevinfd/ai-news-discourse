---
id: "db8b36c17feae8fa"
title: "llm 0.37"
url: "https://simonwillison.net/2026/Nov/2/llm"
link: "https://simonwillison.net/2026/Nov/2/llm"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-02T23:49:30Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm 0.37 \n There's a lot of stuff in this new release of my LLM CLI tool and Python library, representing around two months of accumulated features and fixes. \n I added gpt-6.1-sol and gpt-6.1-terra , plus a new llm openai endpoint add command to make it easier to configure additional models that use OpenAI-compatible endpoints. \n I switched the default model (if you have not set your…"
tags: ["open-source", "projects", "ai", "annotated-release-notes", "generative-ai", "llms", "embeddings", "llm"]
orgs: ["OpenAI", "Google"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 304
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm 0.37

Simon Willison · Simon Willison · 2026-11-02

2nd November 2026
There's a lot of stuff in this new release of my LLM CLI tool and Python library, representing around two months of accumulated features and fixes.
I added gpt-6.1-sol and gpt-6.1-terra, plus a new llm openai endpoint add command to make it easier to configure additional models that use OpenAI-compatible endpoints.
I switched the default model (if you have not set your own default) to gpt-6-luna - half the price of the previous default, gpt-5.6-luna.
LLM's support for embeddings now accepts that different binary content may have different content-type - necessary for models like Gemini Embedding 2, which can embed text, audio, images, and video.
A lot of open source maintainers complain about a flood of AI-assisted PRs. LLM is my project that has been most affected by this and, to be honest, I'm not finding it to be a problem. That's mainly because I have Opus 5.5 or GPT-6 Astra help me with triage to spot the most useful fixes!
This release includes fixes from 12 authors - almost all AI-assisted - and the burden of reviewing them wasn't nearly as great as I expected. I really see them as bug reports with attached examples - sometimes I land them, sometimes I implement my own fix.
So thanks to 0d00ciallo0721, ac1982, Allen Flux, Bian Yuhan, Bishop Kammeraad, Chen Yufeiyang, Christopher Krah, Ethan Stoner, Jiachen Xie, Olamide Faniyan, Sharat Chandra Sai Boddu, nosmile99 for helping out with (or spending tokens on) this release!
Recent articles
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
- The October inflection point for vibe game development - 28th October 2026
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
