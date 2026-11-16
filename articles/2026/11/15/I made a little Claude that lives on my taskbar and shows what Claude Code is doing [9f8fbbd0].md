---
id: "9f8fbbd02ad8ea23"
title: "I made a little Claude that lives on my taskbar and shows what Claude Code is doing"
url: "https://reddit.com/r/ClaudeAI/comments/1xx9ig2/i_made_a_little_claude_that_lives_on_my_taskbar"
link: "https://reddit.com/r/ClaudeAI/comments/1xx9ig2/i_made_a_little_claude_that_lives_on_my_taskbar"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T23:04:37Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["According_Blood_1255"]
language: "en"
summary: "I kept alt-tabbing to check whether Claude Code was done or waiting on me, so I built Clawdkin: a tiny desktop pet that sits on your taskbar and mirrors Claude Code's state. - It works when Claude works and waves when Claude needs your permission. Hover over it and a thought cloud shows what it's doing (\"editing login.ts\", the task, how long, how many edits). - It uses no tokens. It only listens…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 209
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx9ig2/i_made_a_little_claude_that_lives_on_my_taskbar/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a little Claude that lives on my taskbar and shows what Claude Code is doing

Reddit · According_Blood_1255 · 2026-11-15

I kept alt-tabbing to check whether Claude Code was done or waiting on me, so I built Clawdkin: a tiny desktop pet that sits on your taskbar and mirrors Claude Code's state. - It works when Claude works and waves when Claude needs your permission. Hover over it and a thought cloud shows what it's doing ("editing login.ts", the task, how long, how many edits). - It uses no tokens. It only listens to Claude Code's hook events, so nothing gets sent anywhere. - Between tasks it gets bored: it hides behind your taskbar apps, peeks out, naps, and on Windows sometimes "accidentally" opens the Start menu and closes it again. It only does that when you're away. - It has nine forms that evolve over time, five of them unlocked by using Claude, plus petting, a catch game, hats and a diary. It's open source (MIT) and built with Claude Code. Setup is git clone, npm install, npm run setup, npm start. npm run uninstall-hooks removes it cleanly, and npm run doctor checks everything if it misbehaves. https://github.com/0HBrar0/clawdkin I've mostly tested it on Windows 11. CI runs on macOS and Linux too, but I'd love to hear how it behaves there, and what tricks it should learn next.
