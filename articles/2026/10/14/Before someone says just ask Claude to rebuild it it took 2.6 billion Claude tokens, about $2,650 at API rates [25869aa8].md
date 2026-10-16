---
id: "25869aa8b5a68140"
title: "Before someone says \"just ask Claude to rebuild it\": it took 2.6 billion Claude tokens, about $2,650 at API rates"
url: "https://reddit.com/r/ClaudeAI/comments/1x660qx/before_someone_says_just_ask_claude_to_rebuild_it"
link: "https://reddit.com/r/ClaudeAI/comments/1x660qx/before_someone_says_just_ask_claude_to_rebuild_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T23:11:28Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["sociosim"]
language: "en"
summary: "Last time I posted this, the top comments were all \"Claude, make me one of these.\" Reasonable. Here's what it took the first time: 81 days, 2.6 billion Claude tokens, 574 million Codex tokens and 163 subagents. I was on the Claude and OpenAI subscriptions, so I paid the plans, not a token bill; at API rates those tokens would be roughly $2,650. The number that actually hurt was the weekly limit,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "Cursor"]
topics: ["business & funding", "policy & regulation", "agents & coding"]
content_source: "post"
word_count: 296
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x660qx/before_someone_says_just_ask_claude_to_rebuild_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Before someone says "just ask Claude to rebuild it": it took 2.6 billion Claude tokens, about $2,650 at API rates

Reddit · sociosim · 2026-10-14

Last time I posted this, the top comments were all "Claude, make me one of these." Reasonable. Here's what it took the first time: 81 days, 2.6 billion Claude tokens, 574 million Codex tokens and 163 subagents. I was on the Claude and OpenAI subscriptions, so I paid the plans, not a token bill; at API rates those tokens would be roughly $2,650. The number that actually hurt was the weekly limit, which I hit more than once before it was tested. That bill is also the answer to how Claude helped. Claude Code sessions wrote the code and I read diffs; 181 of the 205 commits carry a Claude co-author line. Two sessions each had their own git worktree, a third acted as conductor and merged their PRs in a queue of one, and Codex reviewed about half of the PRs by running the test suite locally. What it built is SessionDeck, a VS Code and Cursor sidebar listing every Claude Code session on your machine by project. A red bell marks the one waiting on a permission prompt or a question, and clicking its row takes you to its tab or terminal, even when another window owns it. Codex and cursor-agent sessions are listed too, as working, idle or finished. The limits, since you'll ask: the bell is Claude Code only and needs a one-time Install Hooks command. Status is read off transcripts and the process table rather than reported by Claude, so it can be a beat late. I develop on Linux and WSL. Mac mostly works; native Windows has no approval alerts. It's free to try. All of the source is public on GitHub (source-available license, not open source), so you can read it before you decide to rebuild it. https://sessiondeck.dev/ https://github.com/len5ky/sessiondeck
