---
id: "b81045175010b499"
title: "A2A (Google's agent-to-agent protocol) joined the Agentic AI Foundation next to MCP, yes I'm two months late on this"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xc93yo/a2a_googles_agenttoagent_protocol_joined_the"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xc93yo/a2a_googles_agenttoagent_protocol_joined_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T04:37:11Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Thirumalaivasan_GJ"]
language: "en"
summary: "Announced Aug 17, 2026, but I only read through the docs and coverage this week and a few details seemed worth a post. What happened: A2A, the open protocol Google created for agents from different vendors to talk to each other, became a hosted project at the Agentic AI Foundation (AAIF), part of the Linux Foundation. Axios reported it Aug 17, and per Forbes the foundation announced it the same…"
tags: ["r/ArtificialInteligence"]
orgs: ["Google", "OpenAI", "Anthropic", "Microsoft", "Amazon", "Salesforce", "IBM"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 310
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xc93yo/a2a_googles_agenttoagent_protocol_joined_the/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# A2A (Google's agent-to-agent protocol) joined the Agentic AI Foundation next to MCP, yes I'm two months late on this

Reddit · Thirumalaivasan_GJ · 2026-10-22

Announced Aug 17, 2026, but I only read through the docs and coverage this week and a few details seemed worth a post. What happened: A2A, the open protocol Google created for agents from different vendors to talk to each other, became a hosted project at the Agentic AI Foundation (AAIF), part of the Linux Foundation. Axios reported it Aug 17, and per Forbes the foundation announced it the same day. Background: Google launched A2A in April 2025 and donated it to the Linux Foundation that June. v1.0 came out in March 2026 and, per the foundation, added multi-protocol bindings, version negotiation, multi-tenancy and signed agent cards. AAIF was announced Dec 9, 2025 with MCP (donated by Anthropic), goose (Block) and AGENTS.md (OpenAI) as founding projects. Axios says it grew from under 40 members to 250+, and Forbes lists agentgateway as another hosted project. How it fits with MCP, from the A2A site itself: MCP is agent-to-tool, A2A is agent-to-agent, and they say the two are complementary. They also list what A2A isn't, not an agent framework, not an MCP replacement, not a chat app. It's Apache 2.0, with SDKs for Python, Go, Java, JS, .NET and Rust plus a CLI. The A2A steering committee on the site lists AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP and ServiceNow. Caveats from Forbes: this changes which foundation hosts A2A, not who controls it. It also doesn't standardize enterprise authorization, so each company still decides what a partner agent can access. Support depth varies (hosting an endpoint isn't the same as implementing signed cards or multi-tenancy), and adoption numbers like the 150+ supporting orgs are reported by the foundation and vendors, not independently measured. Is anyone here actually using A2A in a real project, or is it still mostly MCP for you? Sources: A2A Protocol , Axios , Forbes , SD Times
