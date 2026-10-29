---
id: "8b995ccf23587b42"
title: "Open Source Project to help Secure LLM powered Applications"
url: "https://reddit.com/r/artificial/comments/1xhzatd/open_source_project_to_help_secure_llm_powered"
link: "https://reddit.com/r/artificial/comments/1xhzatd/open_source_project_to_help_secure_llm_powered"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T20:18:25Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Fearless-Might-5439"]
language: "en"
summary: "We built extensible-mcp to help folks build LLM powered applications securely. From a technical perspective it is an MCP proxy capable of loading new MCP Servers dynamically without polluting the LLM’s context while providing Zero Trust policy controls to manage all tool calls. Policies and sensitive credentials are maintained and applied outside the LLMs purview. Policies can be written in any…"
tags: ["r/artificial"]
orgs: []
topics: ["agents & coding", "products & launches", "policy & regulation"]
content_source: "post"
word_count: 170
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xhzatd/open_source_project_to_help_secure_llm_powered/"
score: null
comments: null
community: "r/artificial"
---

# Open Source Project to help Secure LLM powered Applications

Reddit · Fearless-Might-5439 · 2026-10-28

We built extensible-mcp to help folks build LLM powered applications securely. From a technical perspective it is an MCP proxy capable of loading new MCP Servers dynamically without polluting the LLM’s context while providing Zero Trust policy controls to manage all tool calls. Policies and sensitive credentials are maintained and applied outside the LLMs purview. Policies can be written in any of Rego, CEL, and, with the latest release, Cedar. Tool definitions from the various MCP Servers are maintained in a queryable vector store, so the LLM only needs to be aware of those it uses. A particular distinction of extensible-mcp is distinguishing between rights and intents. If an LLM is acting on your behalf, its actions should follow your intent, and not just do any random thing you could do, just because some hallucination told it to! I hope other folks find this useful. We have been using it for our other projects such as Open Executive and wanted to share it. You can check out extensible-mcp here: https://github.com/SenteLabsAI/extensible-mcp
