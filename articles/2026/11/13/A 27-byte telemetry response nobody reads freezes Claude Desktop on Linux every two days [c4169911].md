---
id: "c41699116c50ad7d"
title: "A 27-byte telemetry response nobody reads freezes Claude Desktop on Linux every two days"
url: "https://reddit.com/r/ClaudeAI/comments/1xv8fns/a_27byte_telemetry_response_nobody_reads_freezes"
link: "https://reddit.com/r/ClaudeAI/comments/1xv8fns/a_27byte_telemetry_response_nobody_reads_freezes"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T13:52:32Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["adminvasheypomoiki"]
language: "en"
summary: "A couple of months ago I migrated from ChatGPT to Claude Desktop, which is yet another Electron app. And every couple of days it dies, in one of two ways: either every element disappears and only the skeleton placeholders stay, or it just freezes: you click, and nothing happens. But when it hangs, it picks the best time for it :) It took two months and a 1.5 TiB core dump to find out why. The…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["products & launches"]
content_source: "post"
word_count: 113
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xv8fns/a_27byte_telemetry_response_nobody_reads_freezes/"
score: null
comments: null
community: "r/ClaudeAI"
---

# A 27-byte telemetry response nobody reads freezes Claude Desktop on Linux every two days

Reddit · adminvasheypomoiki · 2026-11-13

A couple of months ago I migrated from ChatGPT to Claude Desktop, which is yet another Electron app. And every couple of days it dies, in one of two ways: either every element disappears and only the skeleton placeholders stay, or it just freezes: you click, and nothing happens. But when it hangs, it picks the best time for it :) It took two months and a 1.5 TiB core dump to find out why. The app never reads a 27-byte telemetry reply. Chromium says it works as intended, and Anthropic's bot closed my issue as "not about Claude Code". So I used this opportunity to write a post about Chromium internals: https://blog.dfb.sh/blog/claude-desktop-freeze/
