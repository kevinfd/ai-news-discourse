---
id: "f8d514419fc87980"
title: "I built an open-source tool that lets Claude Code make Screen Studio-quality screen recordings"
url: "https://reddit.com/r/ClaudeAI/comments/1xmp6kt/i_built_an_opensource_tool_that_lets_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1xmp6kt/i_built_an_opensource_tool_that_lets_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T10:10:25Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["gptrv"]
language: "en"
summary: "Just released Screenplay 🎬 Ask Claude Code \"make a 30s video of https://yoursite.com \" and you get a polished MP4: smooth cursor, auto zooms, click effects, captions, optional voice-over. How it works Claude explores the site and writes a short JSON scenario (open this page, click here, type that) Screenplay plays it in headless Chromium (Playwright), films it and edits it Works for desktop apps…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 202
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmp6kt/i_built_an_opensource_tool_that_lets_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an open-source tool that lets Claude Code make Screen Studio-quality screen recordings

Reddit · gptrv · 2026-11-03

Just released Screenplay 🎬 Ask Claude Code "make a 30s video of https://yoursite.com " and you get a polished MP4: smooth cursor, auto zooms, click effects, captions, optional voice-over. How it works Claude explores the site and writes a short JSON scenario (open this page, click here, type that) Screenplay plays it in headless Chromium (Playwright), films it and edits it Works for desktop apps too (Mac, Windows, Linux), from the same kind of scenario No AI inside, no API key: Claude does the thinking, Screenplay does the filming and editing. Headless, so it also runs in containers without a screen. How Claude helped I built it with Claude Code, and it's made for it. npx agent-screenplay init adds an MCP server and a /screenplay command to Claude Code (Codex and Cursor work too), plus a guide that teaches the agent how to write a good scenario: what to zoom on, how long to linger, when to add a callout. After filming, Claude looks at a storyboard of the take and fixes the scenario if a shot is off. Try it (free, MIT): npx agent-screenplay init , restart Claude Code, then /screenplay Make a 30-second walkthrough of https://yoursite.com Repo: https://github.com/gmpetrov/agent-screenplay Feedback welcome!
