---
id: "1ec6451e720b3904"
title: "AI agent fixes a real bug, tests it in Docker and opens the PR | Row-Bot + GPT 6.1 Sol"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xcg2u8/ai_agent_fixes_a_real_bug_tests_it_in_docker_and"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xcg2u8/ai_agent_fixes_a_real_bug_tests_it_in_docker_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T11:33:23Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Acceptable-Object390"]
language: "en"
summary: "Gave Row-Bot 5.0 a GitHub issue and a repo: \"the CSV export breaks when a customer's name has a comma.\" GPT 6.1 Sol (through my ChatGPT plan) reproduced it with a failing test, fixed it, ran the tests in a Docker sandbox with the network off, and pushed a branch. The part I care about is the review loop: - every command runs in the sandbox, not on my machine - I approve the first change, then…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI"]
topics: []
content_source: "post"
word_count: 151
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xcg2u8/ai_agent_fixes_a_real_bug_tests_it_in_docker_and/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# AI agent fixes a real bug, tests it in Docker and opens the PR | Row-Bot + GPT 6.1 Sol

Reddit · Acceptable-Object390 · 2026-10-22

Gave Row-Bot 5.0 a GitHub issue and a repo: "the CSV export breaks when a customer's name has a comma." GPT 6.1 Sol (through my ChatGPT plan) reproduced it with a failing test, fixed it, ran the tests in a Docker sandbox with the network off, and pushed a branch. The part I care about is the review loop: - every command runs in the sandbox, not on my machine - I approve the first change, then switch the chat to Auto - it stops before committing so I can read the diff - "looks good, commit it" and it's pushed in ~45s The bug is the classic one: rows were joined with plain commas, so "Smith, Jane" became two columns. The fix quotes fields per RFC 4180 and teaches parseCsv to read quoted fields, escaped quotes and line breaks. Draft PR opened from the Git tab via the gh CLI.
