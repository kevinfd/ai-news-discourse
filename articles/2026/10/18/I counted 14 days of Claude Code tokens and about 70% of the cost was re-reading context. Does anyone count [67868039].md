---
id: "678680398d774d59"
title: "I counted 14 days of Claude Code tokens and about 70% of the cost was re-reading context. Does anyone count turns instead of tokens?"
url: "https://reddit.com/r/ClaudeAI/comments/1x93701/i_counted_14_days_of_claude_code_tokens_and_about"
link: "https://reddit.com/r/ClaudeAI/comments/1x93701/i_counted_14_days_of_claude_code_tokens_and_about"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T13:26:12Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Ok-Motor-9812"]
language: "en"
summary: "14 days, 25,247 turns across my sessions. 5.4 billion tokens were cache reads, output was 11.8M. At API prices that's about 70% cache reads, 21% cache writes, under 8% output. So the bill is basically context size times number of turns. Which made me look at my own guards differently. Every time a check blocks the model, that's another full context turn, and it can cost more than the file read…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "business & funding", "policy & regulation"]
content_source: "post"
word_count: 106
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x93701/i_counted_14_days_of_claude_code_tokens_and_about/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I counted 14 days of Claude Code tokens and about 70% of the cost was re-reading context. Does anyone count turns instead of tokens?

Reddit · Ok-Motor-9812 · 2026-10-18

14 days, 25,247 turns across my sessions. 5.4 billion tokens were cache reads, output was 11.8M. At API prices that's about 70% cache reads, 21% cache writes, under 8% output. So the bill is basically context size times number of turns. Which made me look at my own guards differently. Every time a check blocks the model, that's another full context turn, and it can cost more than the file read it was trying to save. My checks blocked 607 times last week. The softer ones now warn once and let it through. I keep blocks only where a miss costs more than the extra turn.
