---
id: "586df0c94182c788"
title: "Show HN: Agentic Identity Broker, OAuth Delegation for AI Agents"
url: "https://github.com/zalando-incubator/agentic-identity-broker"
link: "https://github.com/zalando-incubator/agentic-identity-broker"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T15:07:47Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["jbspeakr"]
language: "en"
summary: "Hi HN, I’m Jan. I am co-author of the Agentic Identity Broker (AIB), an MIT-licensed OAuth2 broker in the Zalando Incubator, that lets a user give an AI agent scoped, revocable access to MCP services. The broker solves three major challenges that are especially relevant in corporate environments: (A) Enable users to delegate workloads to agents without providing the agents all the user’s tokens.…"
tags: []
orgs: ["Google"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 643
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50393235"
score: 22
comments: 3
community: "Hacker News"
---

# Show HN: Agentic Identity Broker, OAuth Delegation for AI Agents

GitHub · jbspeakr · 2026-11-06

Agentic Identity Broker manages delegation chains for on-behalf-of flows in Agentic AI, bridges distinct OAuth2 infrastructures, and provides a secure token vault. Deployed within the call path via gateways like Agentgateway, it offloads auth burdens from both agent and MCP server creators.
For users, it provides a simple way to manage consent, granting agents granular permissions across services such as Google, GitHub, Databricks, and Linear without compromising control.
- Secure Identity Management
Agent registration, principal authentication, and session management
- OAuth2 Delegation & Consent
Manage OAuth2 scopes and user consent for third-party service integrations
- Security-First Design
Sensitive value redaction, command injection prevention, cryptographic validation, and fail-closed architecture
- Rich Consent Experience
Modern UX for managing OAuth2 delegations with design system compliance
- Comprehensive Audit Logging
Structured JSON logging for compliance and security monitoring
Frameworks like FastMCP can implement the whole OAuth2.1 ceremonies as mandated by the MCP spec but this means that you have to configure it for every MCP Server you deploy and maintain it. You also have to configure secure storage and basically run a multitude of OAuth2 authorization servers. With the identity broker and a gateway you can dumb down MCP server development to only provide tools on the target technology you want. OAuth2 ceremonies, token vaulting and token translation are done transparently. Because token exchange is done centrally via a gateway, this allows agents to interact with hundreds of MCP servers via one channel.
If you want to offer an MCP server to your customers as part of your SaaS, the identity broker can provide an additional consent surface that records which agents were actually used. With centralized tool authorization, you can keep an audit trail of approvals on your side regardless of which agent the customer runs.
The agentic identity broker can simplify agents by requiring only a single user token that can be used with an arbitrary number of MCP servers. When paired with a portal for user interactions, token procurement can be front-loaded in the portal, and the agent's responsibility is to forward this token to upstream MCP servers via a gateway.
The impersonation feature allows to start delegation chains via privileged clients, like a Google Chat or Slack bridge. The broker can be instructed to trust for two independent machine identities to assume the session for a particular user. This allows to use the permissions of a user on the company chat in another third-party system.
The tool approval support in the broker allows to enforce tool calls independent of the agent interface in use. This allows a last resort check before emails get sent or documents shared with a central audit trail.
Check out the following docs:
- Quickstart — Get started with Agentic Identity Broker in minutes.
- agenticidentitybroker.dev – Underlying concepts, guides and API specs.
The architecture overview describes the system design, component boundaries, and domain glossary.
Agentic Identity Broker has a built-in consent management UI:
For contribution rules, test commands, and coverage reports, see CONTRIBUTING.md.
Agentic Identity Broker is currently in active development. We use this project in production internally for several MCP servers and have seen good potential. We are coding in the open to gauge our approach. If you find it useful, let us know. If you'd like a feature that's missing, open an issue in our GitHub repo.
While this project was created by professionals with decades of experience in the identity space (including building multiple OIDC and OAuth2 providers), it was developed with a strong focus on agentic engineering and spec-driven development. We review every PR and prioritize sound engineering practices over convenience.
Major roadmap topics include: (a) formalizing token exchange for agent-to-agent calls, (b) intent based authorization and (c) user facing acticity logs.
Thanks to all contributors who are helping to make the Agentic Identity Broker better.
Agentic Identity Broker is a Zalando Engineering project.
