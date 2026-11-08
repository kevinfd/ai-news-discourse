---
id: "11b0263a625a9287"
title: "I priced 194 of my Claude Code sessions at Opus 5.5 API rates. 66% of the cost is cache reads, not output"
url: "https://reddit.com/r/ClaudeAI/comments/1xqw6pa/i_priced_194_of_my_claude_code_sessions_at_opus"
link: "https://reddit.com/r/ClaudeAI/comments/1xqw6pa/i_priced_194_of_my_claude_code_sessions_at_opus"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T11:19:16Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Appropriate-Toe-2993"]
language: "en"
summary: "I wanted to know what a \"normal\" Claude Code session actually costs, so I took 14 days of my team's local Claude Code logs (194 Opus 5.5 sessions, ~46k model calls), deduplicated by response ID (the JSONL logs the same response on several lines, so naive sums double-count), and priced everything at list rates. - Cache reads: 66% of cost. Cache writes: 21%. Output: 13%. - Average cached context…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 177
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqw6pa/i_priced_194_of_my_claude_code_sessions_at_opus/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I priced 194 of my Claude Code sessions at Opus 5.5 API rates. 66% of the cost is cache reads, not output

Reddit · Appropriate-Toe-2993 · 2026-11-08

I wanted to know what a "normal" Claude Code session actually costs, so I took 14 days of my team's local Claude Code logs (194 Opus 5.5 sessions, ~46k model calls), deduplicated by response ID (the JSONL logs the same response on several lines, so naive sums double-count), and priced everything at list rates. - Cache reads: 66% of cost. Cache writes: 21%. Output: 13%. - Average cached context per call: ~395k tokens. - Median session: $8. 75th percentile: $38. 90th: $110. Max: $875. - Top 10% of sessions = 59% of total cost. - Same tokens at Opus 5 rates would cost ~2x, almost entirely because cache reads went from $0.50 to $0.20/MTok. On a subscription none of this is cash, but it tells you which sessions eat your limits. Biggest lever for us: start fresh sessions per task, since every call re-reads the whole context. Full breakdown + method: https://spendbyteam.com/blog/claude-opus-5-5-cost (disclosure: we build SpendByTeam, a cost-by-team tool for Claude Code) Curious if others see the same cache-read share, or if your sessions are more output-heavy?
