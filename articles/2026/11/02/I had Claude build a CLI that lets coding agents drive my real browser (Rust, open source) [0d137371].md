---
id: "0d1373719db40f23"
title: "I had Claude build a CLI that lets coding agents drive my real browser (Rust, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xlrsc7/i_had_claude_build_a_cli_that_lets_coding_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xlrsc7/i_had_claude_build_a_cli_that_lets_coding_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T08:27:37Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["saatvik333"]
language: "en"
summary: "I use Helium (a Chromium fork) as my only browser, and I wanted my coding agents to work in it: my logins, my profiles, but without grabbing my tabs or tripping bot checks. The tools I tried mostly launch their own Chromium, so I had Claude build one. It's called hba. What it does hba open github.com , hba snap -i (the page's accessibility tree, with refs like e12 ), hba click e12 , hba fill ,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "jobs & society"]
content_source: "post"
word_count: 410
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlrsc7/i_had_claude_build_a_cli_that_lets_coding_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I had Claude build a CLI that lets coding agents drive my real browser (Rust, open source)

Reddit · saatvik333 · 2026-11-02

I use Helium (a Chromium fork) as my only browser, and I wanted my coding agents to work in it: my logins, my profiles, but without grabbing my tabs or tripping bot checks. The tools I tried mostly launch their own Chromium, so I had Claude build one. It's called hba. What it does hba open github.com , hba snap -i (the page's accessibility tree, with refs like e12 ), hba click e12 , hba fill , screenshots and so on. A small daemon keeps one DevTools connection open, so reads take 3 to 20 ms and a click that loads a new page takes about half a second. Agents only touch tabs they opened. They can use one of mine only after I hand it over with hba tab use . Console, network log, request mocking, HAR, performance traces and coverage, plus unpacked extension work: load, reload, service worker logs, errors, and driving the popup like a page. It stays away from what anti-bot scripts usually look at. It never turns on Runtime on websites, its own page code runs in an isolated world, and clicks and typing are real input events paced like a person. How Claude helped Claude (Opus) wrote all of the code, running inside my coding agent harness (omp). I set the requirements and made the calls: one Rust binary, a CLI plus a skill file instead of an MCP server, agents in their own tabs. Claude ported my old Python version, vendored Playwright's injected script for snapshots and selectors, and split the work across parallel subagents (DevTools, extensions, screenshots, input). Separate reviewer agents then audited the code twice, and the fixes went back out to new slices. The thing I learned: the bugs that mattered only showed up against my real browser. My Helium window usually sits on another niri workspace, and in that state Chromium holds a lone mouse move for about a second and draws nothing for screenshots. Claude found and worked around both by running hba against the live browser in its own tabs. The unit tests and the headless test browser never hit either one. Try it Free, Apache-2.0, Linux and Helium only for now. Paste this into your agent: Fetch and follow the instructions at https://raw.githubusercontent.com/saatvik333/helium-browser-agent/main/AGENT-SETUP.md to set up hba for me. Repo: https://github.com/saatvik333/helium-browser-agent I'd like feedback, especially from anyone who has used browser-use or agent-browser for the same job. (This post was filled in and submitted by hba.)
