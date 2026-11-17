---
id: "764198fc49a3e15f"
title: "llm 0.37.3"
url: "https://simonwillison.net/2026/Nov/16/llm"
link: "https://simonwillison.net/2026/Nov/16/llm"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-16T23:57:26Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: llm 0.37.3 \n A bug fix release for LLM , mainly to cover a problem with the most recent Homebrew package of the software. \n Homebrew now ships the latest SQLite, 3.54.1 , which includes a fix that broke LLM's logging code . \n Short version: in SQLite 3.54.0 the following SQL: \n select json_object('a', (select json_array(1)))\n \n Returns this: \n {\"a\":[1]}\n \n But in 3.54.1 the same query…"
tags: ["llm", "webassembly", "sqlite", "generative-ai", "ai", "llms", "d-richard-hipp"]
orgs: ["Anthropic", "Alibaba"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 159
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# llm 0.37.3

Simon Willison · Simon Willison · 2026-11-16

16th November 2026
A bug fix release for LLM, mainly to cover a problem with the most recent Homebrew package of the software.
Homebrew now ships the latest SQLite, 3.54.1, which includes a fix that broke LLM's logging code.
Short version: in SQLite 3.54.0 the following SQL:
select json_object('a', (select json_array(1)))
Returns this:
{"a":[1]}
But in 3.54.1 the same query returns this:
{"a":"[1]"}
According to D. Richard Hipp:
That was a bug fix. Per the documentation, (SELECT json_array(...)) returns SQL text, not JSON. Hence the 3.54.1 behavior is correct and 3.54.0 was a bug.
The workaround looks like this:
select json_object('a', json((select json_array(1))))
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
