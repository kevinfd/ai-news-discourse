---
id: "270d613c0dc421cb"
title: "I built a tiny pixel office where Claude workers turn GitHub issues into tested pull requests (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1x9oqqv/i_built_a_tiny_pixel_office_where_claude_workers"
link: "https://reddit.com/r/ClaudeAI/comments/1x9oqqv/i_built_a_tiny_pixel_office_where_claude_workers"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T05:46:29Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["QueasyCat3096"]
language: "en"
summary: "ApolloOffice is a small local service with a web dashboard. You add a GitHub repo, and a fixed pipeline of workers picks up its bug reports: Scout finds new issues, Repro writes a test that fails, Fixer writes the fix, CI runs your test command, Reviewer reads the diff and Submit opens the pull request. Watcher follows your open PRs and rebases them on merge conflicts. Every worker sits at its…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "models & research"]
content_source: "post"
word_count: 343
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9oqqv/i_built_a_tiny_pixel_office_where_claude_workers/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a tiny pixel office where Claude workers turn GitHub issues into tested pull requests (free, open source)

Reddit · QueasyCat3096 · 2026-10-19

ApolloOffice is a small local service with a web dashboard. You add a GitHub repo, and a fixed pipeline of workers picks up its bug reports: Scout finds new issues, Repro writes a test that fails, Fixer writes the fix, CI runs your test command, Reviewer reads the diff and Submit opens the pull request. Watcher follows your open PRs and rebases them on merge conflicts. Every worker sits at its own pixel desk, so you can watch who is doing what. The part I care about most: ApolloOffice checks the proof itself. The new test has to fail without the fix and pass with it, and your test command has to stay green. By default every PR waits for your approval, with the diff, the proof and an editable PR text. How Claude helped I built it with Claude Code over about five days. I made the product decisions, Claude Code wrote most of the code. The first version was a Node daemon. We rewrote it in Rust as a single binary, then I scrapped a bloated version with too many features and restarted with the fixed pipeline you see in the video. Claude Code ran real end-to-end tests against a private test repo with planted bugs: issue to PR, a hidden bug found by the Hunter worker turned into a second PR, and Watcher rebased that PR after the first one was merged. It fixed what broke along the way. During development I had 10 Opus agents do a read-only bug hunt on the code. They found around 70 bugs, all fixed. The workers themselves run on Claude Code with your own login by default (Haiku for the small jobs, Sonnet for fixing). You can also pick Codex, an API key or a local model through Ollama per worker. Free and open source (AGPL-3.0), one binary for Windows, macOS and Linux. Nothing goes through a server of mine and there is no telemetry. GitHub: https://github.com/Silvertree2010/ApolloOffice Happy to answer questions about the pipeline or how I worked with Claude Code on it.
