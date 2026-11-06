---
id: "90cc209fc70ce739"
title: "Claude Code put your email in curl calls. Check your setup"
url: "https://reddit.com/r/ClaudeAI/comments/1xp7e74/claude_code_put_your_email_in_curl_calls_check"
link: "https://reddit.com/r/ClaudeAI/comments/1xp7e74/claude_code_put_your_email_in_curl_calls_check"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T08:06:40Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["MrDogeAlright"]
language: "en"
summary: "Someone who says they work on Claude Code says it sometimes put your account email in the User-Agent of its own curl calls, per a Hacker News comment. Anthropic's new privacy mod blocks one shape of it, but its own README calls it \"a courtesy, not a boundary\". It doesn't check WebFetch, WebSearch, MCP tools or scripts. Quick checks: Run claude --version and update if you're below 2.1.317 Look…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "search & media"]
content_source: "post"
word_count: 95
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xp7e74/claude_code_put_your_email_in_curl_calls_check/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code put your email in curl calls. Check your setup

Reddit · MrDogeAlright · 2026-11-06

Someone who says they work on Claude Code says it sometimes put your account email in the User-Agent of its own curl calls, per a Hacker News comment. Anthropic's new privacy mod blocks one shape of it, but its own README calls it "a courtesy, not a boundary". It doesn't check WebFetch, WebSearch, MCP tools or scripts. Quick checks: Run claude --version and update if you're below 2.1.317 Look for cc-plugin-privacy in /plugins Read any curl User-Agent for your email before you approve it Full thread with sources and the 5-step checklist on X: https://x.com/CobaltHere/status/2118614363695165792
