---
id: "1e2bfe91141bbb65"
title: "My AI workers got ~316 PRs merged in 7 days. The model was never the bottleneck"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xch8qu/my_ai_workers_got_316_prs_merged_in_7_days_the"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xch8qu/my_ai_workers_got_316_prs_merged_in_7_days_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T12:30:05Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["QueasyCat3096"]
language: "en"
summary: "Ran a small pipeline of coding agents on 13 Rust repos for a week. It takes an issue, writes a failing test, fixes it, runs CI and opens a PR. Around 316 got merged in the first seven days. What I learned: Check the result in code, not with the model. A PR only goes out if the new test is red without the fix and green with it. Small models handle more steps than one might think. Only the real…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 115
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xch8qu/my_ai_workers_got_316_prs_merged_in_7_days_the/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# My AI workers got ~316 PRs merged in 7 days. The model was never the bottleneck

Reddit · QueasyCat3096 · 2026-10-22

Ran a small pipeline of coding agents on 13 Rust repos for a week. It takes an issue, writes a failing test, fixes it, runs CI and opens a PR. Around 316 got merged in the first seven days. What I learned: Check the result in code, not with the model. A PR only goes out if the new test is red without the fix and green with it. Small models handle more steps than one might think. Only the real fix needs a strong one. Most "bad fixes" came from a broken build image, not from the model. Works with Claude Code, Codex, API keys or Ollama. Open source, single Rust binary. GitHub: https://github.com/Silvertree2010/ApolloOffice
