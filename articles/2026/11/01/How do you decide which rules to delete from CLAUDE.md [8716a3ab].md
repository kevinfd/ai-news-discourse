---
id: "8716a3abef5852c1"
title: "How do you decide which rules to delete from CLAUDE.md?"
url: "https://reddit.com/r/ClaudeAI/comments/1xkrln3/how_do_you_decide_which_rules_to_delete_from"
link: "https://reddit.com/r/ClaudeAI/comments/1xkrln3/how_do_you_decide_which_rules_to_delete_from"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T02:11:15Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Duckducklaugh"]
language: "en"
summary: "I’ve been using Claude Code daily across a few projects, and my rules keep growing. Every mistake turns into a new line. Eventually the startup docs alone took about 37k tokens, and I got that down to 28k by compressing them. So I tried hard word limits on every doc. That backfired. Across six repos the checker flagged 692 paragraphs, and 37% of those were less than 20% over. Most of my doc…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["business & funding"]
content_source: "post"
word_count: 178
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkrln3/how_do_you_decide_which_rules_to_delete_from/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How do you decide which rules to delete from CLAUDE.md?

Reddit · Duckducklaugh · 2026-11-01

I’ve been using Claude Code daily across a few projects, and my rules keep growing. Every mistake turns into a new line. Eventually the startup docs alone took about 37k tokens, and I got that down to 28k by compressing them. So I tried hard word limits on every doc. That backfired. Across six repos the checker flagged 692 paragraphs, and 37% of those were less than 20% over. Most of my doc warnings were noise, and real problems got buried. Now I’m replacing the limits with a short writing guide: say each thing in one place, only write what’s true now, and for each sentence ask whether deleting it would make the reader do something wrong. What I still can’t judge is which rules are actually doing anything. A rule that’s working looks the same as a rule Claude would have followed anyway. How do you tell the difference? Do you test by removing rules, keep a log of what they prevented, or just go by feel? What’s the last rule you deleted, and did anything break?
