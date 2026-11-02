---
id: "06e6d583ce46c78e"
title: "Claude Code helped me build brepjs, a free open source typesafe CAD as code library, that I use every day."
url: "https://reddit.com/r/ClaudeAI/comments/1xl5x0d/claude_code_helped_me_build_brepjs_a_free_open"
link: "https://reddit.com/r/ClaudeAI/comments/1xl5x0d/claude_code_helped_me_build_brepjs_a_free_open"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T15:29:43Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["veroz"]
language: "en"
summary: "I'm a fullstack dev with over 20 years of experience who has been an early adopter of AI at every evolution of it's journey over the years and just wanted to echo what folks have already said on this sub. Claude is an absolute beast when it comes to execution. I'm currently working on 4 projects concurrently with Claude: brepjs: CAD as code library built for manufacturable geometry…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 279
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xl5x0d/claude_code_helped_me_build_brepjs_a_free_open/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code helped me build brepjs, a free open source typesafe CAD as code library, that I use every day.

Reddit · veroz · 2026-11-01

I'm a fullstack dev with over 20 years of experience who has been an early adopter of AI at every evolution of it's journey over the years and just wanted to echo what folks have already said on this sub. Claude is an absolute beast when it comes to execution. I'm currently working on 4 projects concurrently with Claude: brepjs: CAD as code library built for manufacturable geometry https://brepjs.dev/ https://github.com/andymai/brepjs (Apache 2.0) gridfinitylayouttool: a tool to plan and design Gridfinity storage bins (build with brepjs) https://gridfinitylayouttool.com/designer https://github.com/andymai/gridfinity-layout-tool (AGPL 3.0) occt-wasm: a port of OpenCascade to WASM https://github.com/andymai/occt-wasm brepkit: a B-Rrep CAD kernel written in rust https://github.com/andymai/brepkit Tips I would share to folks wanting to build high-quality open source code bases Plan a strong foundation up front. Beyond just the tech stack: be opinionated about the architecture. Enforce domain boundaries, the way files are organized and named, set budgets for code coverage, build out a design system, set performance benchmarks, define git branch protections for how things get merged, set up a release system. Don't overthink your prompts, let Claude cook. My #1 prompting technique for most tasks is: Help me do X. Ask me multiple choice question prompts using the AskUserQuestion tool (highlighting your recommendations) until you have a clear understanding of how to complete the task at the highest quality possible. (I use https://espanso.org/ so I just have to type :ama for the latter sentence) Use another agent for code review. The same agent doesn't do as good of a job verifying its work. It needs another agent gathering fresh content to catch things it missed. Tune this second agent to be adversarial and challenge what was built.
