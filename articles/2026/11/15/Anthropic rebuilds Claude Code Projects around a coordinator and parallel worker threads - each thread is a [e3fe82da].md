---
id: "e3fe82daad0fb4f8"
title: "Anthropic rebuilds Claude Code Projects around a coordinator and parallel worker threads - each thread is a full cloud session on its own branch"
url: "https://reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a"
link: "https://reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T01:38:07Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["winer666"]
language: "en"
summary: "Anthropic posted an update on Nov 14 rebuilding Claude Projects from a folder of files into a coordinated set of working sessions. You describe the work in one conversation; a coordinator scopes it, delegates it to parallel threads, reviews the outputs and assembles the result. Each thread is a Claude Code cloud session with its own copy of the repo and its own Git branch, and it can split its…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 219
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xwj3v0/anthropic_rebuilds_claude_code_projects_around_a/"
score: null
comments: null
community: "r/artificial"
---

# Anthropic rebuilds Claude Code Projects around a coordinator and parallel worker threads - each thread is a full cloud session on its own branch

Reddit · winer666 · 2026-11-15

Anthropic posted an update on Nov 14 rebuilding Claude Projects from a folder of files into a coordinated set of working sessions. You describe the work in one conversation; a coordinator scopes it, delegates it to parallel threads, reviews the outputs and assembles the result. Each thread is a Claude Code cloud session with its own copy of the repo and its own Git branch, and it can split its task further into subagents, loops or workflows. The work keeps going after you close your laptop, and you can steer it from your phone. It is a public beta rolling out gradually to select Pro/Max/Ultra subscribers who use Claude Code cloud sessions; Team and Enterprise plans do not have it yet, and there is a waitlist for everyone else. Anthropic is upfront about the limits: threads run only in the cloud for now (local code and VPN support is coming 'very soon'), several parallel sessions burn through usage limits faster, and if two threads touch the same code it surfaces as an ordinary merge conflict in a PR. Sources: Anthropic's product post (claude.com/blog/projects-redesigned) and the Projects docs (code.claude.com/docs/en/claude-projects). What I am curious about: does parallelizing agents actually speed up real work, or does it just move the bottleneck to review and merge conflicts? Has anyone here tried the beta?
