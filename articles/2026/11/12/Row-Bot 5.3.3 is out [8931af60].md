---
id: "8931af609887ed5c"
title: "Row-Bot 5.3.3 is out"
url: "https://reddit.com/r/artificial/comments/1xuhliz/rowbot_533_is_out"
link: "https://reddit.com/r/artificial/comments/1xuhliz/rowbot_533_is_out"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T16:40:15Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Acceptable-Object390"]
language: "en"
summary: "You can now run it in your browser with nothing to install. On row-bot website, Continue with Railway creates your own Row-Bot in your own Railway account and opens it already signed in. Railway bills you directly, usually $5-10 a month. The relay in between can only create a Row-Bot and keeps no logs, tokens or addresses. Models: - Providers and models are now one Settings page. Starred models…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Alibaba", "Nvidia", "Mistral", "DeepSeek", "Hugging Face"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 273
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xuhliz/rowbot_533_is_out/"
score: null
comments: null
community: "r/artificial"
---

# Row-Bot 5.3.3 is out

Reddit · Acceptable-Object390 · 2026-11-12

You can now run it in your browser with nothing to install. On row-bot website, Continue with Railway creates your own Row-Bot in your own Railway account and opens it already signed in. Railway bills you directly, usually $5-10 a month. The relay in between can only create a Row-Bot and keeps no logs, tokens or addresses. Models: - Providers and models are now one Settings page. Starred models show in every picker that can use them. - 12 more API providers: DeepSeek, Mistral, Groq, Kimi, Z AI (GLM), Qwen, Together, Fireworks, Cerebras, Hugging Face, NVIDIA NIM, Vercel AI Gateway - LM Studio, vLLM and llama.cpp on your own machine - Backup model: if the main model times out, hits a rate limit or runs out of credit, the backup finishes the turn and the chat says which model answered. It never kicks in for incognito chats going to the cloud. On a Claude plan, every model call in a turn used to start a new Claude Code and re-send the whole conversation. A long agent turn could use up a 5-hour limit in under an hour. Now one Claude Code stays for the whole turn and the conversation is read from the prompt cache. Opus, Sonnet and Haiku 5.5 also get their full 1M context. Image and video generation now also works through OpenRouter, Together, Vercel, Requesty, Qwen, Atlas Cloud, MiniMax and Z.AI. Security fix: if tools_config.json was cut short or locked, tools you'd switched off came back on and the shell's blocked-commands list emptied. Now they stay off. GHSA-68j6-243q-h2hp (low). Windows, macOS, Linux. From 5.3.2 it arrives as a background update.
