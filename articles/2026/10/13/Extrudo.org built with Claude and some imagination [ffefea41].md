---
id: "ffefea41838789c3"
title: "Extrudo.org built with Claude and some imagination"
url: "https://reddit.com/r/ClaudeAI/comments/1x58kqn/extrudoorg_built_with_claude_and_some_imagination"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T20:59:05Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["slartibartfastda"]
language: "en"
summary: "Extrudo is a parametric CAD tool for 3D printing that runs in the browser. You sketch with constraints, extrude, fillet, give your dimensions names, and drag a slider to watch the whole part rebuild. The video is a 15-minute session cut down to 80 seconds: a mounting plate whose hole positions, size, thickness and corner radius are all parameters. Try it: https://app.extrudo.org (free, no…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 482
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x58kqn/extrudoorg_built_with_claude_and_some_imagination/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Extrudo.org built with Claude and some imagination

Reddit · slartibartfastda · 2026-10-13

Extrudo is a parametric CAD tool for 3D printing that runs in the browser. You sketch with constraints, extrude, fillet, give your dimensions names, and drag a slider to watch the whole part rebuild. The video is a 15-minute session cut down to 80 seconds: a mounting plate whose hole positions, size, thickness and corner radius are all parameters. Try it: https://app.extrudo.org (free, no account, works offline once loaded, your files stay on your machine). Desktop builds for Mac, Linux and Windows are in the GitHub releases. Code: https://github.com/zoltanf/extrudo (GPL-3.0) How it was built It was built in the span of around one month. Initially just investigations and planning: what libraries are available, whether a similar open-source product already exists, etc. The first git commit was on September 25. Main has 322 commits since then, most of the work was done by Opus 5.5, initial planning by Fable. For some easier work I used cheaper models through opencode. I decided what to build and in what order, and reviewed the work. Claude wrote the code, the tests and the docs. Under the hood: OpenCascade compiled to WebAssembly and running in a Web Worker, behind a C++ layer Claude wrote (about 9k lines). Sketches use the planegcs constraint solver, the viewport is three.js and the UI is React. CI runs 528 test files, Vitest plus Playwright end-to-end, on every push. The setup - One Claude Code session is the coordinator (usually Opus). It picks the next task from the roadmap, writes the design decision down as an ADR (82 so far), and writes a brief for a worker: which files, function signatures, test cases, acceptance checks. - Workers run headless on a second PC (as my main laptop is quite slow): Claude Code (Opus for the geometry kernel, Sonnet for well-specified UI work) and opencode with cheaper models for small slices. Each job gets its own git worktree and branch. The coordinator reviews every diff and merges once CI is green. Things I learned Having a well-designed plan and roadmap is worth spending time on at the begining. It was mostly done with my inputs and Fable for investigations. Don't fan out too wide. Running 8 to 16 Opus, Fable and Sonnet agents at once on a long investigation used too much of the plan. I now cap it at two or three parallel jobs. Keep CLAUDE.md short. Mine is a map: where the docs are, the hard rules, the commands. The detail lives in an "ADR digest", one paragraph per decision listing the rules a change has to keep, and agents read only the paragraphs for the area they touch. It's rough in places (the roadmap in the repo lists what's missing), and I'd like to hear what breaks if you give it a shoot. Feedback from people who actually 3d print things is extra welcome. Music: "Scaling Up" by Ruskerdax (CC0)
