---
id: "f9a3c449e5989b1d"
title: "datasette-llm 0.1a11"
url: "https://simonwillison.net/2026/Nov/14/datasette-llm"
link: "https://simonwillison.net/2026/Nov/14/datasette-llm"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-14T23:59:28Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: datasette-llm 0.1a11 \n datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins. \n This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard web protocol. \n This means that if you're running local models with LM Studio or…"
tags: ["uv", "datasette-agent", "llm", "datasette", "llms", "ai", "generative-ai"]
orgs: ["OpenAI", "Anthropic", "Alibaba"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 166
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# datasette-llm 0.1a11

Simon Willison · Simon Willison · 2026-11-14

14th November 2026
datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins.
This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseudo-standard web protocol.
This means that if you're running local models with LM Studio or Ollama or llama.cpp (which just hit v1.0.0) you can run Datasette via uvx like this:
wget https://datasette.io/content.db
uvx --with datasette-agent datasette \
  --root --secret 1 \
  -s plugins.datasette-llm.default_model '{
    "model": "lmstudio-qwen",
    "model_name": "qwen/qwen3.8-27b",
    "api_base": "http://localhost:1234/v1"
  }' content.db
And you'll get a local server running a Datasette Agent instance powered by your local model!
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
