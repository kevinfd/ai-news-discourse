---
id: "cc4b1fa6fa451160"
title: "I built a Claude Code plugin that keeps your prompt cache warm, so you stop paying to rebuild it"
url: "https://reddit.com/r/ClaudeAI/comments/1x5ttwo/i_built_a_claude_code_plugin_that_keeps_your"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T15:12:33Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["sohamspat"]
language: "en"
summary: "Every time your Claude Code cache expires (5 minutes or an hour idle, depending on your setup and main session v/s subagent), the next message pays the full cache write cost on the conversation. On Opus, that's $5 per million tokens (5min TTL) or $8 per million tokens (1 hr TTL) against a cost of $0.20 to read the cache , and nothing on screen tells you it's about to happen. So I built Cache…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["business & funding", "products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 440
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5ttwo/i_built_a_claude_code_plugin_that_keeps_your/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Claude Code plugin that keeps your prompt cache warm, so you stop paying to rebuild it

Reddit · sohamspat · 2026-10-14

Every time your Claude Code cache expires (5 minutes or an hour idle, depending on your setup and main session v/s subagent), the next message pays the full cache write cost on the conversation. On Opus, that's $5 per million tokens (5min TTL) or $8 per million tokens (1 hr TTL) against a cost of $0.20 to read the cache , and nothing on screen tells you it's about to happen. So I built Cache Maxxer , a Claude Code plugin that puts a band right above the input box: A countdown on the cache, timed to your real cache length (1 hour or 5 minutes, read from your session, so it's right on a subscription and on an API key) Your real hit rate , for the last request and the whole session A notice every time the cache gets rebuilt , with how much was re-written, what it cost and why (idle, model switch, compact, tools changed) Keep warm : one tiny ping just before expiry, so you pay the read cost only and get a fresh timer. It stops on its own after you've been idle for 3 hours (configurable) It's built specifically for Claude Code and runs in the terminal and in the Claude desktop app, on Mac, Windows and Linux. How it works under the hood: Claude Code already records the cache read and write of every request in your session, so the plugin reads those to get your real hit rate and to spot a rebuild (a request that writes over 20K tokens and reads less than half of what the one before it had cached). The countdown starts from your last request and uses your actual cache length. The whole thing uses about a tenth of a percent of one core while it watches. How Claude Code helped build it: I designed it and built it with Claude Code. It wrote most of the code and tests from my specs, and I used it to compare the desktop band against screenshots of the real app, again and again, until they matched pixel for pixel. That's also how two bugs in the Claude desktop app turned up, which other developers had already reported, so I added my measurements to their issues. I reviewed every change before it went in. Free to try: It's free and open source (MIT). Install it with these two commands in Claude Code: claude plugin marketplace add vayaan-labs/plugins claude plugin install cache-maxxer@vayaan-labs Or just point your agent at github.com/vayaan-labs/cache-maxxer and tell it to install the plugin. Hope this saves y'all a lot of costs and extends your sub usage !
