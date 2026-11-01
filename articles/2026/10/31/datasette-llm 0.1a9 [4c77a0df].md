---
id: "4c77a0dfd6338deb"
title: "datasette-llm 0.1a9"
url: "https://simonwillison.net/2026/Oct/31/datasette-llm"
link: "https://simonwillison.net/2026/Oct/31/datasette-llm"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-31T22:10:01Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: datasette-llm 0.1a9 \n I have some big upgrades to Datasette Agent in the pipeline, but in the meantime here's a tiny user experience improvement to the underlying datasette-llm plugin. \n It now picks up the default model used by LLM , which means you can start using Datasette Agent without needing to explicitly configure a default model: \n uvx --with datasette-agent datasette content.db…"
tags: ["datasette", "llm", "datasette-agent"]
orgs: []
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 136
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# datasette-llm 0.1a9

Simon Willison · Simon Willison · 2026-10-31

31st October 2026
I have some big upgrades to Datasette Agent in the pipeline, but in the meantime here's a tiny user experience improvement to the underlying datasette-llm plugin. 
It now picks up the default model used by LLM, which means you can start using Datasette Agent without needing to explicitly configure a default model:
uvx --with datasette-agent datasette content.db --internal internal.db
Previously you would also need to specify a model with -s plugins.datasette-agent.default_model gpt-6-astra.
Recent articles
- The October inflection point for vibe game development - 28th October 2026
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
