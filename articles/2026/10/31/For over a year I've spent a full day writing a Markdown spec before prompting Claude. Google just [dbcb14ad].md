---
id: "dbcb14ad2dd7fc04"
title: "For over a year I've spent a full day writing a Markdown spec before prompting Claude. Google just open-sourced the \"Elephant-Goldfish Model\" that takes this 10x further"
url: "https://reddit.com/r/ClaudeAI/comments/1xkn61s/for_over_a_year_ive_spent_a_full_day_writing_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xkn61s/for_over_a_year_ive_spent_a_full_day_writing_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T22:27:55Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["derekleeth"]
language: "en"
summary: "Whether you've been coding for 15+ years or started \"vibe coding\" with Claude a month ago, you've probably hit the same wall: you let the agent start coding right away, the first two hours feel like magic, and by day 3 you're stuck in a 150-message thread where fixing one bug breaks two other things. For over a year, my rule on every work and side project before prompting Claude to write code…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 302
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkn61s/for_over_a_year_ive_spent_a_full_day_writing_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# For over a year I've spent a full day writing a Markdown spec before prompting Claude. Google just open-sourced the "Elephant-Goldfish Model" that takes this 10x further

Reddit · derekleeth · 2026-10-31

Whether you've been coding for 15+ years or started "vibe coding" with Claude a month ago, you've probably hit the same wall: you let the agent start coding right away, the first two hours feel like magic, and by day 3 you're stuck in a 150-message thread where fixing one bug breaks two other things. For over a year, my rule on every work and side project before prompting Claude to write code has been simple: spend a full day (or more) working purely on a detailed project plan in a Markdown (.md) file. On my latest project, spending days revising project_plan.md and implementation_plan.md before coding paid off immediately: Killed bad architecture on paper: Draft #1 used an embedded Axum mTLS server for sync. Revising the spec showed iroh (QUIC) dialing by Ed25519 public key + mDNS was way cleaner—saving weeks of wasted code. Locked down sync & crypto: Ed25519/X25519 keys in the OS keychain (no cloud accounts), SQLite outbox triggers + Hybrid Logical Clocks (HLC) for field-by-field conflict merging, and a signed team membership log that rotates the vault key when a member is removed. Google just open-sourced the Elephant-Goldfish Model (EGM) plugin ( https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html ), based on Dave Rensin's essay, which takes this Markdown workflow several steps further by fixing conversational bias: The Elephant (/egm-brainstorm, /egm-draft): Long-context session that interviews you and writes the Markdown spec. Strict rule: It writes ZERO code. The Goldfish (/egm-review): Spawns stateless subagents with ZERO memory of your brainstorming chat. They read only your .md spec and repo cold as adversarial reviewers to expose edge cases and ambiguities before any code is written. Drift Check (/egm-drift-report): Checks the final code diff against the .md spec. How many of you keep a project_plan.md before coding, and has anyone started running zero-context review subagents on their specs?
