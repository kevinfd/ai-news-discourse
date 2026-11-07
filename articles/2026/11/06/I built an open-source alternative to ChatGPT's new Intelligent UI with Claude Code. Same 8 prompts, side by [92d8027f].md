---
id: "92d8027f0bfa8ea8"
title: "I built an open-source alternative to ChatGPT's new Intelligent UI with Claude Code. Same 8 prompts, side by side 👀!"
url: "https://reddit.com/r/ClaudeAI/comments/1xpkiro/i_built_an_opensource_alternative_to_chatgpts_new"
link: "https://reddit.com/r/ClaudeAI/comments/1xpkiro/i_built_an_opensource_alternative_to_chatgpts_new"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T18:38:41Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["prakashTech"]
language: "en"
summary: "Chat answers are still mostly walls of text, even when what you actually wanted was a tool. So I've been building Ripple: the model writes a small JSON spec and Ripple renders it as a real interface while it's still streaming. Sliders, forms, 3D models, games, a full checkout. It's open source (MIT). I wanted to see how it holds up, so I gave ChatGPT and Ripple + Claude the same 8 prompts and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 324
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpkiro/i_built_an_opensource_alternative_to_chatgpts_new/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an open-source alternative to ChatGPT's new Intelligent UI with Claude Code. Same 8 prompts, side by side 👀!

Reddit · prakashTech · 2026-11-06

Chat answers are still mostly walls of text, even when what you actually wanted was a tool. So I've been building Ripple: the model writes a small JSON spec and Ripple renders it as a real interface while it's still streaming. Sliders, forms, 3D models, games, a full checkout. It's open source (MIT). I wanted to see how it holds up, so I gave ChatGPT and Ripple + Claude the same 8 prompts and recorded both from the first keystroke. Waits play at real speed, I only cut my own pauses between clicks. ChatGPT did better than I expected. Heart rate, bike gears, the habit tracker and tic-tac-toe all came back as working widgets. The gaps showed up elsewhere: the plane was a labeled picture rather than a 3D model, the HIIT "next exercise" button did nothing, and the food order's follow-up sat on "thinking" for 3+ minutes. On the Ripple side that order runs menu → test payment → live tracker, live on Sonnet against a local test store. Everything else is recorded Sonnet runs, plus Opus for the dashboard. Almost all of the engine was written with Claude Code: the renderer, 200+ widgets, the streaming parser and the tests. I spent my time on design calls and reviews. What moved quality the most: - asking Claude to choose the widget before writing any data - making it look at its own output: render, screenshot at phone and desktop size in light and dark, fix, repeat - keeping the spec streamable, so the UI grows while the model types To use it in your own app, hand your claude the docs or the skill(link below) and it will start integrating Ripple UI into your apps. Try it: ripple.pocketpaw.xyz Skill: npx skills add qbtrix/ripple-iui --skill ripple Code: github.com/qbtrix/ripple npm i u/ripple-ui/svelte (also u/ripple-ui/react, u/ripple-ui/embed) Curious what you'd build with it, and happy to go deep on the spec format or my Claude Code workflow.
