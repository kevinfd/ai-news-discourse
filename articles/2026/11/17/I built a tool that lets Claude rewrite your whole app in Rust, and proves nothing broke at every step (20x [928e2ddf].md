---
id: "928e2ddff93dbfed"
title: "I built a tool that lets Claude rewrite your whole app in Rust, and proves nothing broke at every step (20x faster in one case)"
url: "https://reddit.com/r/ClaudeAI/comments/1xyj19z/i_built_a_tool_that_lets_claude_rewrite_your"
link: "https://reddit.com/r/ClaudeAI/comments/1xyj19z/i_built_a_tool_that_lets_claude_rewrite_your"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T12:20:26Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["erkamyaman"]
language: "en"
summary: "Asking an agent to \"rewrite this in Rust\" usually ends with a big diff and no idea if it still behaves the same. So I built rust-anything: Claude writes the Rust, and the tool keeps it honest. Repo: https://github.com/erkamyaman/rust-anything What it does Takes a TypeScript/JavaScript, Python, C, Go, Ruby or Java app to a pure Rust app, one piece at a time: CLIs, HTTP servers and libraries.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding", "models & research"]
content_source: "post"
word_count: 517
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xyj19z/i_built_a_tool_that_lets_claude_rewrite_your/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a tool that lets Claude rewrite your whole app in Rust, and proves nothing broke at every step (20x faster in one case)

Reddit · erkamyaman · 2026-11-17

Asking an agent to "rewrite this in Rust" usually ends with a big diff and no idea if it still behaves the same. So I built rust-anything: Claude writes the Rust, and the tool keeps it honest. Repo: https://github.com/erkamyaman/rust-anything What it does Takes a TypeScript/JavaScript, Python, C, Go, Ruby or Java app to a pure Rust app, one piece at a time: CLIs, HTTP servers and libraries. Records what the original actually does first, including nasty edge cases (emoji, negative modulo, integer overflow, float extremes, map order). Each case runs twice, and anything that changes between runs (timestamps, ids) is ignored. Puts a Rust front door in front of the app on day one. Anything not ported yet falls back to the original, so the app never stops working. Every ported piece must pass a gate (fmt, clippy, tests, every error path covered, no stray unwrap ), then the whole app is replayed : 100% or it doesn't ship. Each piece has a kill switch back to the original. At the end it lifts the app to pure Rust: fallback gone, bindings gone, replayed one last time on a copy before anything is written. Only want speed? It profiles a real workload and moves just the hot loop: a search over 50,000 keys went from 10 ms to 0.5 ms per query in Node, slugify got 17x faster in Python. Same results, checked before every benchmark. How it works with Claude rust-anything setup installs an agent skill and an MCP server for Claude Code (also Codex and others). For a whole app, the skill first grills you : rounds of numbered questions, each with a recommended answer, until every decision is settled (byte-for-byte or normalized output, which crates, when to stop for your OK). The grilling style is adapted from Matt Pocock's skills. Background subagents research each dependency against primary sources and write down the traps they find. A MAP.md lets the port span many sessions: each session claims one unit, and every checkpoint leaves a HANDOFF.md for the next one. Independent units can be ported in parallel by subagents. At cutover, Claude writes a script for the steps only you can do (deploys, DNS, secrets). How Claude helped build it Built with Claude Code (Opus). I set the direction and made the calls; Claude did most of the work: Wrote the Rust: the bridges for all six languages (napi-rs, PyO3, C ABI, cgo, magnus, JNI), record/replay, the axum proxy front door, and the lift. Researched how real rewrites went (fish shell, Turborepo, librsvg, papers on LLM code translation) and turned it into the design. Grilled me on that design, then built it in six milestones, each verified on small apps in all six languages before moving on. Set up the GitHub release and npm publishing with trusted publishing (no tokens). Try it (free, MIT) npm i -g rust-anything or cargo install --git https://github.com/erkamyaman/rust-anything Then rust-anything setup and ask Claude to port something. Repo: https://github.com/erkamyaman/rust-anything Happy to answer questions, and I'd love to hear what broke for you in big rewrites that recorded cases wouldn't have caught.
