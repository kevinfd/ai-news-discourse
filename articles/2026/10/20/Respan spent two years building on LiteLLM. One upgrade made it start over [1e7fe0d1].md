---
id: "1e7fe0d1d76c538f"
title: "Respan spent two years building on LiteLLM. One upgrade made it start over."
url: "https://thenewstack.io/respan-rust-ai-gateway"
link: "https://thenewstack.io/respan-rust-ai-gateway"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T22:13:08Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Respan released an open-source AI gateway written in Rust on Tuesday, after spending two years building more than 100,000 lines of wrapper code around LiteLLM. \n\n The new gateway replaces that system with a small core and plugins that handle model providers, routing, MCP tools, realtime voice, and security controls. \n\n A LiteLLM upgrade breaks \n\n The breaking point came in January 2026, when a…"
tags: ["AI Infrastructure", "Open Source", "Rust"]
orgs: ["OpenAI", "Google", "Mistral"]
topics: ["models & research", "agents & coding", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 721
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Respan spent two years building on LiteLLM. One upgrade made it start over.

The New Stack · Amanda Caswell · 2026-10-20

Respan spent two years building on LiteLLM. One upgrade made it start over.
Respan released an open-source AI gateway written in Rust on Tuesday, after spending two years building more than 100,000 lines of wrapper code around LiteLLM.
The new gateway replaces that system with a small core and plugins that handle model providers, routing, MCP tools, realtime voice, and security controls.
A LiteLLM upgrade breaks
The breaking point came in January 2026, when a routine LiteLLM upgrade caused intermittent connection failures. Respan rolled back the update but never figured out the problem.
“We still haven’t figured out the cause,” the company said in its Hacker News launch post.
Since then, its engineers have stopped upgrading LiteLLM directly, instead pulling in upstream fixes one at a time.
A small plugin core
To avoid another maintenance headache, the company borrowed an idea from Nginx, keeping the gateway’s core small and moving features like routing, model providers, and security into plugins. Developers can build their own using the same interfaces, without having to change the underlying code.
Developers can build their own using the same interfaces, without having to change the underlying code.
Some of those integrations are surprisingly small. Respan says its Mistral provider takes just 22 lines of code, while quirks like Groq reporting token usage in a different field can be handled separately. This makes it easier when updating one provider while avoiding the need to change how the rest of the gateway works.
When a request comes in over HTTP or WebSocket, the gateway runs it through the plugins in order. They can decide which model handles it, change the response, make additional calls, or stop the request before it reaches a provider.
When both sides use the same format, the gateway can leave the original request and its provider-specific fields intact.
The gateway can also translate between protocols. An application built for OpenAI’s Realtime API, for example, can connect to Gemini Live without changes to the client, according to Respan, although some features may not carry over. When both sides use the same format, the gateway can leave the original request and its provider-specific fields intact.
Plugins you must compile
Custom plugins are compiled into the gateway, so adding one means maintaining the code and rebuilding the binary. There’s also a security concern. Plugins run inside the gateway process, where they can access model requests and other sensitive data.
Rust helps prevent memory-safety bugs, but it can’t protect against malicious dependencies, or flawed application logic, which is probably why the concern came up following the launch in a Hacker News discussion. One commenter questioned whether compiled crates should even be called plugins, arguing that they force developers to maintain a build pipeline and introduce supply-chain risks. Respan’s founder acknowledged the concern, pointing out that developers can at least inspect the source code they’re compiling.
Plugin order is important, too, which is why Respan processes plugins in the order they’re registered, and one can answer or reject a request before the others run. Put a cache ahead of a security check, for example, and a cached response could bypass that check entirely. Developers need to account for that when configuring the gateway.
LiteLLM’s slower Rust road
Respan isn’t alone in deciding that Rust belongs under an AI gateway. LiteLLM is porting its own gateway to Rust, but where Respan rebuilt from the core out, LiteLLM is moving one route at a time, with the Rust core switched off by default and any request it can’t yet handle falling back to the existing Python path, so turning it on can’t break something Python already served.
The company laid out the plan in June and has said its goal is a pure Rust server that runs every hot path, auth, and rate limiting included, which the current beta doesn’t reach yet.
Respan isn’t alone in deciding that Rust belongs under an AI gateway.
LiteLLM has also published benchmarks claiming its Rust gateway has about seven times less overhead and uses nine times less memory than Bifrost. But those numbers come from LiteLLM’s own tests, using a benchmark harness the company developed.
Respan’s gateway is still pre-alpha, although developers can download a prebuilt binary from GitHub and run it without the company’s paid platform. Custom plugins still require compiling their own build.
