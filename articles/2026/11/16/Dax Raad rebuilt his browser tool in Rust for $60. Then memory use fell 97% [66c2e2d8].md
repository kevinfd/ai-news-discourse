---
id: "66c2e2d879f10b6b"
title: "Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%."
url: "https://thenewstack.io/opencode-browse-rust-rewrite"
link: "https://thenewstack.io/opencode-browse-rust-rewrite"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T17:59:39Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "OpenCode developer Dax Raad says he rebuilt the project’s browser automation tool in Rust for $60, replacing the parts of Playwright and Patchright it actually used and dramatically reducing its memory footprint. \n\n A 4.3 MB binary \n\n The figures he posted to X on Saturday are striking. The new Rust binary is just 4.3 MB, compared with 53 to 64 MB for the previous Node version. Memory use for…"
tags: ["AI Agents", "Developer tools", "Rust"]
orgs: ["Anthropic", "DeepSeek"]
topics: ["agents & coding"]
content_source: "summary"
word_count: 591
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%.

The New Stack · Amanda Caswell · 2026-11-16

OpenCode developer Dax Raad says he rebuilt the project’s browser automation tool in Rust for $60, replacing the parts of Playwright and Patchright it actually used and dramatically reducing its memory footprint. 

 A 4.3 MB binary 

 The figures he posted to X on Saturday are striking. The new Rust binary is just 4.3 MB, compared with 53 to 64 MB for the previous Node version. Memory use for each OpenCode Browse connector also fell from roughly 190 MB to 5.6 MB after a few calls, a reduction of about 97%. 

 The new Rust binary is just 4.3 MB, compared with 53 to 64 MB for the previous Node version. 

 The relay that wires AI coding agents to the browser shows a similar gap, with Raad’s comparison putting the Rust implementation at 6 MB idle, or 6.6 MB once it has served calls, against 353 MB for the old Node relay after six days of running. 

 Replacing Playwright and Patchright 

 OpenCode Browse connects AI coding agents to a developer’s existing browser through a Chromium extension and an MCP server . The previous Node implementation used Playwright for browser automation and Patchright to reduce detection, but Raad rebuilt the functionality Browse needed in Rust to cut runtime overhead. 

 Raad rebuilt the functionality Browse needed in Rust to cut runtime overhead. 

 The new Rust relay communicates with the Chromium extension over WebSockets and uses the Chrome DevTools Protocol to handle browser operations, agent sessions, recordings, and network captures. It also embeds QuickJS to execute agent-supplied JavaScript without requiring the previous Node runtime. 

 Inside the pull request 

 The merged pull request confirms that Raad replaced the Node-based CLI and relay while keeping the existing Chromium extension and using the Chrome DevTools Protocol for browser operations. 

 The team ran two rounds of testing with about 10 regression agents against a real Chrome browser. Browse scored 85% on Stealth Bench v2, compared with 90.5% for Browser Use Cloud, although the pull request doesn’t include a score for the old Node version. 

 Not everything made it into the rewrite; Raad dropped time zone and locale emulation along with the download tool, which Chrome blocks for extensions. The Rust version also retains a problem from the Node implementation where a busy-looping eval can’t be stopped through the extension. 

 Browse still includes relay authentication, extension pairing and origin restrictions, and agents are limited to tabs they open themselves or that users explicitly share with them. 

 The real $60 cost 

 Raad says the rewrite “only cost $60” and confirmed in a reply on X that he used Claude Opus as his main coding model and DeepSeek as a subagent. 

 The two models helped him replace the Playwright and Patchright functionality Browse needed, although the $60 figure doesn’t include the time he spent checking, testing, and fixing the code. The challenge with Rust rewrites is finding a smaller replacement that matches the original’s functionality without creating more maintenance work. 

 the $60 figure doesn’t include the time he spent checking, testing, and fixing the code 

 The memory savings are impressive, but Raad has also taken on responsibility for code that Playwright and Patchright previously maintained. His team will also have to deal with browser updates, authentication changes and security fixes that previously came through those libraries. That’s where AI-generated technical debt can become a problem, especially when code is cheap to produce but takes considerably more work to maintain. 
 The post Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%. appeared first on The New Stack .
