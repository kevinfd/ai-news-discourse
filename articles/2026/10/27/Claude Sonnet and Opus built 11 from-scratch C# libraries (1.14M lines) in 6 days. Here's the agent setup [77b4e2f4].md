---
id: "77b4e2f4b2164cb4"
title: "Claude Sonnet and Opus built 11 from-scratch C# libraries (1.14M lines) in 6 days. Here's the agent setup."
url: "https://reddit.com/r/ClaudeAI/comments/1xgv8br/claude_sonnet_and_opus_built_11_fromscratch_c"
link: "https://reddit.com/r/ClaudeAI/comments/1xgv8br/claude_sonnet_and_opus_built_11_fromscratch_c"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T15:14:29Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["ai-tacocat-ia"]
language: "en"
summary: "Since last Wednesday, a team of Claude agents built 11 foundational C# libraries from scratch: a PDF stack, image codecs, a font shaper, an HLSL shader compiler, audio, an HTML parser, an HTML/CSS rendering engine, a JavaScript interpreter, compression, OCR and a game engine. About 1.14M lines and 2,100+ commits. Seven are on NuGet. A few results, each judged by an outside test suite or a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 328
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgv8br/claude_sonnet_and_opus_built_11_fromscratch_c/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Sonnet and Opus built 11 from-scratch C# libraries (1.14M lines) in 6 days. Here's the agent setup.

Reddit · ai-tacocat-ia · 2026-10-27

Since last Wednesday, a team of Claude agents built 11 foundational C# libraries from scratch: a PDF stack, image codecs, a font shaper, an HLSL shader compiler, audio, an HTML parser, an HTML/CSS rendering engine, a JavaScript interpreter, compression, OCR and a game engine. About 1.14M lines and 2,100+ commits. Seven are on NuGet. A few results, each judged by an outside test suite or a reference implementation: - JS interpreter: 99.55% of test262 (43,471 tests) - HTML renderer: a 10k-row table to PDF in 1.8 s / 305 MB, vs headless Chrome's 6.5 s / 2.1 GB - Shader compiler: matches Microsoft's DXC on 330/330 GPU tests, compiles 2.4× faster - HTML parser: 100% of html5lib-tests The setup: Models. Sonnet writes the code. Opus plans, orchestrates, reviews and releases. Roles. - A project planner runs a design interview for each library. - A project manager answers that interview on my behalf and records who decided each thing. - A build orchestrator splits the work into units, gives each unit its own git worktree and engineer, verifies the result, and merges it. Context. At 400k tokens, an agent writes a handoff note and a fresh successor picks up the same worktree. Nobody tries to fit a project into one context. Heavy work runs elsewhere. Full test suites, benchmarks, fuzzing and model training run on a second machine. The agents share it through a lock. Fixed rules for every library. From scratch. Nothing but the .NET base library. Competitors studied only through docs and black-box output. Judged by outside test suites, and benchmarked against the incumbent. The biggest lesson was to give the agents less process, not more. Agents invent rules and then obey them. The more you tell a flexible agent to do, the more it does wrong. Trimming the prompts did more than adding to them. My messages per library went from 112 on the first one to 11 by the fourth. Full write-up: https://recursiveai.org/research/alera-library-factory/ Repos: https://github.com/orgs/recursive-ai-oss/repositories
