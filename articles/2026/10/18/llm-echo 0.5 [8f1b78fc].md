---
id: "8f1b78fcf0c44ef0"
title: "llm-echo 0.5"
url: "https://simonwillison.net/2026/Oct/18/llm-echo"
link: "https://simonwillison.net/2026/Oct/18/llm-echo"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-18T23:16:16Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm-echo 0.5 \n I'm working towards a new LLM release, and testing PRs caused me to revisit the llm-echo debug plugin. This plugin provides a \"model\" which doesn't involve an LLM at all - it just repeats back the prompts that have been fed to it. The new release now updates the simulated token usage counts to take tool calls, system prompts, and reasoning tokens into account. \n Example…"
tags: ["llm"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 170
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm-echo 0.5

Simon Willison · Simon Willison · 2026-10-18

18th October 2026
I'm working towards a new LLM release, and testing PRs caused me to revisit the llm-echo debug plugin. This plugin provides a "model" which doesn't involve an LLM at all - it just repeats back the prompts that have been fed to it. The new release now updates the simulated token usage counts to take tool calls, system prompts, and reasoning tokens into account.
Example usage:
uvx --with llm-echo llm -m echo 'hi there' -o thinking 1 --usage
Outputs:
First I consider the prompt, then I decide what to say.
{
  "prompt": "hi there",
  "system": "",
  "attachments": [],
  "stream": true,
  "previous": []
}
Token usage: 2 input, 24 output
Recent articles
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
- We're going to need default hard budget caps on pretty much everything - 3rd October 2026
