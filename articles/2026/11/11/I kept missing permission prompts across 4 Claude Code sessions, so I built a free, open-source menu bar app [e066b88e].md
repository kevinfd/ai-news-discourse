---
id: "e066b88e1a081d91"
title: "I kept missing permission prompts across 4 Claude Code sessions, so I built a free, open-source menu bar app that tells me who's waiting on me"
url: "https://reddit.com/r/ClaudeAI/comments/1xtm9vp/i_kept_missing_permission_prompts_across_4_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xtm9vp/i_kept_missing_permission_prompts_across_4_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T16:29:59Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Front-Sky-8272"]
language: "en"
summary: "I usually have a few coding agents going at once, like Claude Code in two repos and Codex in a third. I kept losing time the same way: a session would sit on a permission prompt for 20 minutes while I was busy in another window. So I built Hoply, a macOS menu bar app that keeps an eye on them for me. What it does - Live sessions for Claude Code, Codex CLI, Copilot CLI, Copilot in JetBrains and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft", "Alibaba", "Apple", "Intel"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "post"
word_count: 541
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtm9vp/i_kept_missing_permission_prompts_across_4_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I kept missing permission prompts across 4 Claude Code sessions, so I built a free, open-source menu bar app that tells me who's waiting on me

Reddit · Front-Sky-8272 · 2026-11-11

I usually have a few coding agents going at once, like Claude Code in two repos and Codex in a third. I kept losing time the same way: a session would sit on a permission prompt for 20 minutes while I was busy in another window. So I built Hoply, a macOS menu bar app that keeps an eye on them for me. What it does - Live sessions for Claude Code, Codex CLI, Copilot CLI, Copilot in JetBrains and Qwen Code. They're grouped by repo and named by the task, not by a session ID. - "Waiting on you" : any session that needs you moves to the top. That covers permission prompts, questions, finished turns, runs stopped at a usage limit and failed runs (with the actual error, not a spinner). Each one also gets a notification. - Approve from the menu bar (optional, off by default): Allow and Deny for Claude Code permission prompts, in the panel or on the notification. Your terminal prompt still works, and whichever you answer first wins. - Usage ledger : API-equivalent cost per project, model, day and agent, kept in a local SQLite file. It reads Claude Code's transcripts, so you get history from before you installed it. It also keeps that history after Claude Code deletes old transcripts (about 30 days). - Claude plan limits : the 5-hour and weekly windows, your pace against the clock, a projection at reset, and alerts at 80% and 95%. - Local model servers (vLLM, llama.cpp, SGLang, TGI, Ollama, LM Studio): tok/s, KV cache, queued requests, and what those tokens would have cost on the API. - Dev servers your agents started, tied back to the session that started them, with a Stop button. - Clean up : merged worktrees, big build caches and processes agents left running. Nothing is removed without a review sheet, and files go to the Trash. - ⌥Space command palette from any app. You can also resume a finished session in Terminal. Privacy (it touches your agent config, so this matters) - No account and no telemetry. The listener binds to 127.0.0.1 and refuses anything else. - Transcripts and Copilot's database are only ever read, never changed. - It makes three kinds of outgoing request: to model servers you add, a daily update check, and Anthropic's usage endpoint with your own Claude Code login. That last one only happens if you turn on the limits card, and macOS asks you first. - Connect writes hooks into ~/.claude/settings.json (and Codex's and Copilot's equivalents). It backs the file up first and only touches its own entries. - It's MIT licensed, so you can check every one of these claims in the code. Setup: install it, open Settings → Agents → Connect, then restart any sessions that were already running. - Download: https://hoply.dev - Homebrew: brew install --cask milos5611/hoply/hoply - Source: https://github.com/Milos5611/hoply It needs macOS 26 Tahoe, runs on Apple silicon and Intel, and is signed and notarized. It's free during early access. It's not on the Mac App Store because the sandbox would block it from reading transcripts and writing hooks. This is 0.1.0, so I'd love to hear what breaks, and which agent you'd want supported next. Disclosure: I'm the developer.
