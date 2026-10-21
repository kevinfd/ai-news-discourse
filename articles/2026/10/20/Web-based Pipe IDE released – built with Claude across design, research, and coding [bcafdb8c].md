---
id: "bcafdb8cb6d0ec1d"
title: "Web-based Pipe IDE released – built with Claude across design, research, and coding"
url: "https://reddit.com/r/ClaudeAI/comments/1xb5p1o/webbased_pipe_ide_released_built_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xb5p1o/webbased_pipe_ide_released_built_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T22:07:19Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["PurpleDragon99"]
language: "en"
summary: "I built Pipe IDE, a browser-based development environment for Pipe, a general-purpose visual programming language I’ve been designing for seven years. This is its first public release. What it does: You build programs as visual diagrams — add blocks on a canvas, connect them, and run them. Blocks can contain Python, so visual structure and text code mix in one program. There’s a test bed to feed…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 331
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xb5p1o/webbased_pipe_ide_released_built_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Web-based Pipe IDE released – built with Claude across design, research, and coding

Reddit · PurpleDragon99 · 2026-10-20

I built Pipe IDE, a browser-based development environment for Pipe, a general-purpose visual programming language I’ve been designing for seven years. This is its first public release. What it does: You build programs as visual diagrams — add blocks on a canvas, connect them, and run them. Blocks can contain Python, so visual structure and text code mix in one program. There’s a test bed to feed in inputs and run a workflow, and a log that shows how signals propagate through it. Tech-wise it’s Flutter/Dart compiled to web, with Python running in-browser via Pyodide (CPython on WebAssembly) in web workers. Free to try: Yes — no account, no install. Just open https://www.pipelang.com/pipe/v1/ and start building; everything is stored locally in your browser. Two short demos: Data Swap ( https://www.pipelang.com/assets/tutorials/v1/tutorial1.mp4 ) and Reusable Sum ( https://www.pipelang.com/assets/tutorials/v1/tutorial2.mp4 ). How Claude helped (used at every stage): Language and runtime design: I worked through Pipe’s semantics with Claude — how runlets, memlets, and mergers behave, how signals propagate, and how to reconcile the running implementation with my formal spec. It caught several places where my Python runtime diverged from the spec and helped rewrite them to match. Coding the IDE: Claude helped implement Flutter/Dart features, choose and wire up libraries (for example, the in-editor code component, with word-wrap and enforced font settings), and build the Python/Pyodide execution layer. Debugging: concrete fixes — e.g., tracking down a stray Unicode character (U+2028) that was breaking the Python editor, and sorting out demo-video encoding and streaming. Writing block code to the API: after reading my runtime’s API spec, Claude generated the Python entry-point/runlet code so it matched the actual interface. Research: evaluating options (code-editor components, in-browser video playback, encoding settings) before I committed to one. Status: It’s an early MVP. The core is there — canvas, Python blocks, test bed, signal log, reusable components, typed data — a backend and collaboration are next. Happy to answer questions about the architecture or how I used Claude through it.
