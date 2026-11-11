---
id: "e765b637341f19e6"
title: "Someone used $167 on my Anthropic API keys (limit was $30), and the key was never in my code. How could it leak?"
url: "https://reddit.com/r/ClaudeAI/comments/1xsudl0/someone_used_167_on_my_anthropic_api_keys_limit"
link: "https://reddit.com/r/ClaudeAI/comments/1xsudl0/someone_used_167_on_my_anthropic_api_keys_limit"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T18:20:15Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["alisaleem252"]
language: "en"
summary: "I run a small SaaS, a WordPress plugin with an AI backend. This week I found that someone else had used my Anthropic API key. They ran $167 of usage, mostly Opus 5.5 and Fable requests , even though I had a $30 spend limit set. What I know one of the affected keys was an older key that was never committed to my code . Other keys were hardcoded in a private GitHub repo. I only use Claude chat and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 295
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsudl0/someone_used_167_on_my_anthropic_api_keys_limit/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Someone used $167 on my Anthropic API keys (limit was $30), and the key was never in my code. How could it leak?

Reddit · alisaleem252 · 2026-11-10

I run a small SaaS, a WordPress plugin with an AI backend. This week I found that someone else had used my Anthropic API key. They ran $167 of usage, mostly Opus 5.5 and Fable requests , even though I had a $30 spend limit set. What I know one of the affected keys was an older key that was never committed to my code . Other keys were hardcoded in a private GitHub repo. I only use Claude chat and Claude Desktop, with no other AI tools. The usage was on the most expensive models, which looks like someone choosing the priciest option rather than normal traffic from my app. The cause is still unknown. Processing img g8t8py564u0i1... Both of the keys were used in specific proportion, the one key in code could make sense, but the other one which never was in code was also used which doesnt' make sense. What I’ve done Rotated every key in the project. Moved all secrets out of git into an untracked config file. I’m checking the usage logs for the first unauthorized call, and my GitHub security log. Questions Where could a key that was never in my repo have leaked from? I’m checking old .env and notes files, pasted text in chats, shell history, browser extensions, old laptops, backups and clipboard tools. What am I missing? Why did a $30 limit allow $167? Has anyone seen limits overshoot because of delayed usage reporting, per-workspace versus org limits, or limits that only apply to part of the usage? there is no way to opening a support ticket with Anthropic just a fin agent. Is there a way to see which IP or client made each request, so I can tell it apart from my own traffic?
