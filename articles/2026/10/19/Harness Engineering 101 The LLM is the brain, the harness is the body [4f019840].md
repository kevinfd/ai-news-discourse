---
id: "4f0198409c0e2bc2"
title: "Harness Engineering 101: The LLM is the brain, the harness is the body"
url: "https://github.com/IsuruMaduranga/harness-engineering-101"
link: "https://github.com/IsuruMaduranga/harness-engineering-101"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-19T12:07:41Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["isuruwijesiri"]
language: "en"
summary: "The LLM is the brain. The harness is the body.\nVersion 1.1, October 2026.\nAI usage disclosure: I drafted every chapter myself, from what I learned building WSO2 MI Copilot, WSO2 BI Copilot and One Code. I used Claude Code and One Code to reorder each chapter so it leads with the answer (the Minto pyramid), to polish the English, to generate the diagrams, and to write the code that draws the…"
tags: []
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 429
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50151390"
score: 130
comments: 64
community: "Hacker News"
---

# Harness Engineering 101: The LLM is the brain, the harness is the body

GitHub · isuruwijesiri · 2026-10-19

The LLM is the brain. The harness is the body.
Version 1.1, October 2026.
AI usage disclosure: I drafted every chapter myself, from what I learned building WSO2 MI Copilot, WSO2 BI Copilot and One Code. I used Claude Code and One Code to reorder each chapter so it leads with the answer (the Minto pyramid), to polish the English, to generate the diagrams, and to write the code that draws the charts.
A blog series about building AI agents from first principles, published as a book.
📖 Read it online: https://isuruwijesiri.com/harness-engineering-101/
An LLM API is stateless. Every turn, you send the entire conversation as a JSON array and get text back. A harness is the program that builds, maintains, and protects that array. Everything the field calls "agents" is a set of patches to that one loop, and each patch exists because something concrete broke. This series develops that one idea across 16 chapters, growing a ~300-line toy agent in plain Python as it goes.
I use the same ideas in One Code, an open-source coding agent built on pi.
The rendered book reads best online at the link above. If you'd rather read the source here on GitHub, follow the chapters in order below. The full introduction is on the book's landing page.
Every chapter has the same shape: the failure, the minimal patch, what the patch costs.
- Build Your Own: the complete toy harness, annotated
Standalone pieces. Read them when you need them.
- A. One Harness, Many Brains: model routing, prompt tiers, cost engineering
- B. Worktrees and Isolation: giving parallel agents separate copies of the world
- C. Modes and Plan Mode: harness-enforced operating states (coding-specific)
- D. Retries, Rate Limits, and Streaming: the unglamorous plumbing, plus how streaming works on the wire
cargo install mdbook mdbook-mermaid   # or: brew install mdbook (+ mdbook-mermaid binary)
mdbook serve --open                    # live-reloading preview at http://localhost:3000
mdbook build                           # static site into ./book
mdbook-mermaid renders the inline mermaid diagrams; without it those blocks
show as raw code.
cd src/diagrams && python3 gen_all.py   # Python 3.10+, matplotlib
This repository is dual-licensed:
- The prose (every chapter and appendix, the .md files under src/) is
licensed under
Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
(CC BY-NC-ND 4.0). You
may share it with credit, but not use it commercially or publish modified
versions. Full text in LICENSE.
- The code (the .py files under src/harness/ and src/diagrams/, and
code snippets reproduced from them in the chapters) is licensed under the
MIT License. Use it freely, with attribution.
© 2026 Isuru Wijesiri.
