---
id: "6c51129e93f61d6b"
title: "Introducing Kimi K3.1 Pro"
url: "https://simonwillison.net/2026/Oct/23/kimi-k31-pro"
link: "https://simonwillison.net/2026/Oct/23/kimi-k31-pro"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-23T19:40:54Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Simon Willison"]
language: "en"
summary: "Introducing Kimi K3.1 Pro \nKimi K3.1 Pro landed on the Kimi API today - it's not yet open weights, but Moonshot promise \"Full model weights will be released by Nov 4, 2026\". \n They're also offering a \"Highspeed\" version that's 2-3x faster, at twice the price (except for input token cache hits, which are priced the same). \n The US dollar pricing is $2.00/million tokens for input and $10/million…"
tags: ["ai", "generative-ai", "llms", "llm", "llm-pricing", "pelican-riding-a-bicycle", "llm-release", "ai-in-china", "moonshot", "kimi"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["models & research", "business & funding"]
content_source: "fulltext"
word_count: 337
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Introducing Kimi K3.1 Pro

Simon Willison · Simon Willison · 2026-10-23

23rd October 2026 - Link Blog
Introducing Kimi K3.1 Pro (via) Kimi K3.1 Pro landed on the Kimi API today - it's not yet open weights, but Moonshot promise "Full model weights will be released by Nov 4, 2026".
They're also offering a "Highspeed" version that's 2-3x faster, at twice the price (except for input token cache hits, which are priced the same).
The US dollar pricing is $2.00/million tokens for input and $10/million for output - the same as GPT-6.1 Sol and half the price of Claude Opus 5.5.
Moonshot's own benchmarks show Kimi as approximately level with Opus 5.5 and GPT-6 Astra - beating them on a few benchmarks, coming close on others.
Artificial Analysis scored Kimi at 55 - ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (all at 53) and behind only Claude Opus 5.5 (58).
This is the first time a (soon-to-be) open weight model has scored this highly against the frontier.
I tried it out via the Moonshot API using the llm openai endpoint command I added to LLM 0.32 back in August:
llm openai endpoint \
  https://api.moonshot.ai/v1 \
  --key kimi \
  -m kimi-k3.1-pro \
  "Generate an SVG of a pelican riding a bicycle" \
  --responses \
  -o reasoning_effort low \
  > kimi-k3.1-pro-pelican-low.stdout.txt \
  2> kimi-k3.1-pro-pelican-low.stderr.txt
llm openai endpoint can run prompts against any OpenAI-compatible endpoint but doesn't log the results, hence the extra options to save stdout and stderr (the reasoning trace).
Here are the pelicans I got for Kimi K3.1 Pro on the three reasoning levels it supports - low, medium, and max. This is max:
For comparison, I ran fresh pelicans against Kimi K3 on those three reasoning levels.
Recent articles
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
