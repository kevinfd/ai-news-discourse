---
id: "e4de297d232f859e"
title: "I built a Claude Code plugin that turns your agent's tool calls into MilkDrop visuals, with a gauge for when it is stuck"
url: "https://reddit.com/r/ClaudeAI/comments/1xgtgey/i_built_a_claude_code_plugin_that_turns_your"
link: "https://reddit.com/r/ClaudeAI/comments/1xgtgey/i_built_a_claude_code_plugin_that_turns_your"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T14:05:14Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["naklitechie"]
language: "en"
summary: "Processing video xaqvo6h8p0yh1... Turbella shows what Claude Code is doing while you wait: every tool call, failure, retry, permission wait and thinking period, as a MilkDrop visualiser and a timeline. A turbulence gauge goes from 0 to 1 as the agent gets stuck, for example when the same command fails again and again or the same file is edited back and forth. Install: claude plugin marketplace…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 180
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgtgey/i_built_a_claude_code_plugin_that_turns_your/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Claude Code plugin that turns your agent's tool calls into MilkDrop visuals, with a gauge for when it is stuck

Reddit · naklitechie · 2026-10-27

Processing video xaqvo6h8p0yh1... Turbella shows what Claude Code is doing while you wait: every tool call, failure, retry, permission wait and thinking period, as a MilkDrop visualiser and a timeline. A turbulence gauge goes from 0 to 1 as the agent gets stuck, for example when the same command fails again and again or the same file is edited back and forth. Install: claude plugin marketplace add NakliTechie/turbella claude plugin install turbella@turbella Everything stays on your machine. Events carry only tool names, timings and SHA-256 hashes, never prompts, code or output. There is no account and no telemetry. It needs Node 22 and has no npm dependencies. It also works with Codex, Cursor, Copilot CLI, Hermes, opencode, pi, omp and dsh. On macOS you get floating windows, one per agent session, and a one-line strip on top of the terminal. How Claude helped: Claude Code wrote most of the code with me, including the hook, the daemon, the Swift helper for the floating windows and the adapters for the other agents. Repo: https://github.com/NakliTechie/turbella Sample clips of the different looks: https://turbella.naklitechie.com
