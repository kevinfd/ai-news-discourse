---
id: "c60558e98558e0e7"
title: "External sandboxes for coding agents"
url: "https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents"
link: "https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-17T22:52:29Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Simon Willison"]
language: "en"
summary: "External sandboxes for coding agents \nI've been exploring new ways to sandbox code that is executed by agents, with a focus on making it safer to try out local models without worrying that a mistake or prompt injection attack might cause them to take damaging actions on a machine. \n I worked on this project with Prime Radiant , the AI research lab behind Superpowers and other projects . \n My…"
tags: ["sandboxing", "security", "ai", "webassembly", "generative-ai", "llms", "coding-agents", "claude-code", "codex", "pi"]
orgs: ["Anthropic", "Microsoft", "Apple", "Alibaba"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 353
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# External sandboxes for coding agents

Simon Willison · Simon Willison · 2026-11-17

17th November 2026 - Link Blog
External sandboxes for coding agents. I've been exploring new ways to sandbox code that is executed by agents, with a focus on making it safer to try out local models without worrying that a mistake or prompt injection attack might cause them to take damaging actions on a machine.
I worked on this project with Prime Radiant, the AI research lab behind Superpowers and other projects.
My post on the Prime Radiant blog introduces the external sandbox pattern, where code executed by the agent runs inside a dedicated sandbox while the agent itself lives outside of that sandbox.
To demonstrate this pattern we've released three sandbox server implementations:
- external-sandbox-v86 runs a Node.js server which then uses v86 to run Alpine Linux inside WebAssembly.
- external-sandbox-container is a Python web server which runs the sandbox in Alpine Linux inside an Apple Containers instance.
- external-sandbox-quicksand is another Python web server, this time using Microsoft's Quicksand sandboxing library, which bundles QEMU and Alpine Linux in a Python package!
Each of these implementations offers the same localhost API. You can then configure Pi, Claude Code, or Codex to send API calls to that sandbox any time they want to execute code.
The sandboxes also include an optional HTTP/HTTPS allow-list proxy, so you can control exactly which hosts your agent's code is allowed to communicate with - plus a credential replacement mechanism to make authenticated API calls without sharing a secret with the agent. Here's the UI you can use to reconfigure that proxy while the sandbox is still running:
I continue to be fascinated by the challenge of safely running untrusted code. This external sandbox pattern provides a neat way to experiment with different approaches.
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
