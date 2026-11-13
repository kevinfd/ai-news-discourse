---
id: "52ff0a203f06b51d"
title: "A 10-minute 'manual dreaming' pass for your CLAUDE.md and memory files"
url: "https://reddit.com/r/ClaudeAI/comments/1xuwooe/a_10minute_manual_dreaming_pass_for_your_claudemd"
link: "https://reddit.com/r/ClaudeAI/comments/1xuwooe/a_10minute_manual_dreaming_pass_for_your_claudemd"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T03:00:20Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["ibitneo"]
language: "en"
summary: "Anthropic's agent memory writeup describes \"dreaming\": between sessions, Claude rereads transcripts of what it actually did, checks them against the notes it saved, and rewrites the ones that turned out wrong. Your CLAUDE.md and memory files only get that kind of pass if you do it yourself. WikiTrace found that 52% of failures on tasks the agent had solved without memory traced back to a lesson…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 200
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuwooe/a_10minute_manual_dreaming_pass_for_your_claudemd/"
score: null
comments: null
community: "r/ClaudeAI"
---

# A 10-minute 'manual dreaming' pass for your CLAUDE.md and memory files

Reddit · ibitneo · 2026-11-13

Anthropic's agent memory writeup describes "dreaming": between sessions, Claude rereads transcripts of what it actually did, checks them against the notes it saved, and rewrites the ones that turned out wrong. Your CLAUDE.md and memory files only get that kind of pass if you do it yourself. WikiTrace found that 52% of failures on tasks the agent had solved without memory traced back to a lesson it followed. A pass I'd do: One-off corrections that became rules. Anything saying "always" or "never" that started as a single fix. Scope it to that file or bug, or delete it. Superseded decisions. Old choices you've since reversed (previous test runner, previous API client). Delete them or mark "replaced by X" so two conflicting rules don't sit side by side. Version-bound lessons. Add the range: "Next 14 only", "before the auth refactor". Provenance. Append the commit hash or PR behind each lesson. In WikiTrace, lessons linked to their source runs had 4.5% regression on previously solved tasks, vs 6.5% for the same lessons unlinked. A rule you can't trace to anything is a good deletion candidate. How often do people here actually prune these files? On a schedule, or only after something breaks?
