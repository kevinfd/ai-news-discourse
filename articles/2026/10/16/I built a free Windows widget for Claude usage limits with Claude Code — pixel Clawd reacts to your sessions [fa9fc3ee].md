---
id: "fa9fc3ee932c0a4d"
title: "I built a free Windows widget for Claude usage limits with Claude Code — pixel Clawd reacts to your sessions"
url: "https://reddit.com/r/ClaudeAI/comments/1x7o895/i_built_a_free_windows_widget_for_claude_usage"
link: "https://reddit.com/r/ClaudeAI/comments/1x7o895/i_built_a_free_windows_widget_for_claude_usage"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T18:36:32Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["venhed"]
language: "en"
summary: "I built a small Windows widget (floating window + tray icon) that shows my Claude plan limits: the same numbers as /usage in Claude Code — current session, weekly and Fable limits — refreshed every minute. It also lists running Claude Code sessions (working / waiting for input / idle), shows Anthropic service status and tells you when a Claude Code update is out. How it works: it runs `claude -p…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 374
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7o895/i_built_a_free_windows_widget_for_claude_usage/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free Windows widget for Claude usage limits with Claude Code — pixel Clawd reacts to your sessions

Reddit · venhed · 2026-10-16

I built a small Windows widget (floating window + tray icon) that shows my Claude plan limits: the same numbers as /usage in Claude Code — current session, weekly and Fable limits — refreshed every minute. It also lists running Claude Code sessions (working / waiting for input / idle), shows Anthropic service status and tells you when a Claude Code update is out. How it works: it runs `claude -p "/usage"` headless, which returns the server-side percentages for your existing login without calling the model, so it spends no tokens. Sessions come from the registry Claude Code keeps in ~/.claude/sessions. Plain PowerShell 5.1 + WPF, nothing to install besides Claude Code. Clawd lives in the window and reacts to the data: sleeps in a burrow when nothing runs, runs while a session works, waves with a "?" when one is waiting for you, sweats near the limit and lies belly-up at 100%. The hearts in the header are the session limit left. How Claude Code helped build it: - I built the whole thing with Claude Code, in PowerShell (which I wouldn't have written by hand at this size — ~3k lines of WPF in PowerShell 5.1). - Clawd's pose glyphs and animations: Claude Code reproduced them from its own welcome-screen art, cell by cell, so they match the terminal version. - It split the original single script into ~18 dot-sourced modules and wrote a CLAUDE.md with the load-order rules and PowerShell 5.1 gotchas (UTF-8 BOM, no `??`), which kept later sessions from breaking things. - For the public release it added an English UI with on-the-fly language switching, translated all code comments, and wrote a recorder script that renders the README GIFs straight from WPF with scripted fake data. Recording those GIFs is how it caught a layout bug where English text overlapped a header. - One gotcha it found: running `claude -p "/usage"` from Git Bash turns `/usage` into a file path and sends it to the model as a prompt — so the widget only calls it from PowerShell. Free and open source (MIT). To try it: clone or download the ZIP from GitHub and double-click start-widget.vbs. Needs Windows 10/11 and Claude Code logged in. https://github.com/Enhed/clawd-usage-winwidget Not affiliated with Anthropic.
