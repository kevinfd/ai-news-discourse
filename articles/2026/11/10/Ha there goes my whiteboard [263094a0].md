---
id: "263094a07d736b7b"
title: "Ha there goes my whiteboard"
url: "https://reddit.com/r/ClaudeAI/comments/1xt0cgb/ha_there_goes_my_whiteboard"
link: "https://reddit.com/r/ClaudeAI/comments/1xt0cgb/ha_there_goes_my_whiteboard"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T22:12:41Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["SSJE0"]
language: "en"
summary: "Three days ago I pushed my whiteboard to GitHub and my website, and today Claude launches Whiteboards!! Had to laugh. Mine is a different kind of thing though, so here's what I built and how Claude helped. Used Opus 5.5 xhigh!! Tested on Surface Book 7 Pro and Pi 5 check my GitHub for an in-depth review!! **What I built** ZP Whiteboard is a desktop app: an infinite whiteboard and a Markdown…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 424
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xt0cgb/ha_there_goes_my_whiteboard/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Ha there goes my whiteboard

Reddit · SSJE0 · 2026-11-10

Three days ago I pushed my whiteboard to GitHub and my website, and today Claude launches Whiteboards!! Had to laugh. Mine is a different kind of thing though, so here's what I built and how Claude helped. Used Opus 5.5 xhigh!! Tested on Surface Book 7 Pro and Pi 5 check my GitHub for an in-depth review!! **What I built** ZP Whiteboard is a desktop app: an infinite whiteboard and a Markdown editor side by side. Draw with a pen (pressure, palm rejection, handwriting to text on Windows), write a doc next to the board, and review it Word-style with comments, replies, @mentions and suggested changes you accept or reject. **What it does** - Runs fully offline. No account, no telemetry, it never talks to the network. - Exports to Word (real comments and tracked changes), PDF, Markdown, or "Export for AI": a review file + board image + a ready prompt on your clipboard for Claude Code. - Fast: drawing on a 5,000-element board went from under 1 fps to 60 fps, and pen latency from 455 ms to 9 ms, measured on my Surface Pro 7. **How Claude helped** I built it with Claude Code (Opus) as my pair. Every commit is co-authored with Claude. Two main agents and 15 subagents over the whole build. How we worked: - For big features, agents did the research first: file format, post-quantum encryption, canvas performance. - After each build, three independent subagents audited the code with different lenses (security, correctness, performance). They got the code but not the main session's conclusions, so they couldn't just agree with it. They caught real bugs: a Windows hash leak through //server image links, broken undo on suggestions, and an emoji picker that never fired. - Every speed claim had to be measured old vs new on the real device, not guessed. - Even the little handwriting helper is Rust, written with Claude around Windows Ink. **Free to try** - Free download for Windows (x64 and ARM) and Linux (.deb and AppImage): https://zeropodnews.com/software/whiteboard - Open source, Apache 2.0, build it yourself: https://github.com/Zeropodaerodynamist/whiteboard-app (npm install, then npm start) - The installers add an optional encrypted file format (.swbdx, post-quantum) that isn't in the repo. Everything else is. - Windows shows a SmartScreen warning the first time because the builds aren't code-signed yet. Click More info, then Run anyway, or build from source. It's the first public release, so there are rough edges: no Mac build yet, no live collaboration. Tell me what breaks!! Build, publish, build again, never stop!!
