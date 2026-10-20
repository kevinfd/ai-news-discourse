---
id: "e032f90cca656492"
title: "Microsoft and Sumsub treat AI agents as insider threats, forcing zero-trust controls"
url: "https://vectorwire.ai/article/microsoft-and-sumsub-treat-ai-agents-as-insider-threats-forcing-zero-trust-contr-9b50d1"
link: "https://vectorwire.ai/article/microsoft-and-sumsub-treat-ai-agents-as-insider-threats-forcing-zero-trust-contr-9b50d1"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-10-20T09:42:31Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["VectorWireAI"]
language: "en"
summary: "ANALYSIS Two unrelated security announcements on the same day point to a shared conclusion now hardening into industry consensus: the AI agents enterprises are deploying should be governed not as trusted software but as untrusted insiders capable of mistakes, manipulation, and collusion.\nWhy it matters\nMicrosoft and Sumsub, operating at very different scales and market positions, each shipped…"
tags: ["r/artificial"]
orgs: ["Microsoft", "Amazon"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 805
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xanr5c/microsoft_and_sumsub_treat_ai_agents_as_insider/"
score: null
comments: null
community: "r/artificial"
---

# Microsoft and Sumsub treat AI agents as insider threats, forcing zero-trust controls

Vector Wire · VectorWireAI · 2026-10-20

ANALYSIS Two unrelated security announcements on the same day point to a shared conclusion now hardening into industry consensus: the AI agents enterprises are deploying should be governed not as trusted software but as untrusted insiders capable of mistakes, manipulation, and collusion.
Why it matters
Microsoft and Sumsub, operating at very different scales and market positions, each shipped agent-governance products on October 19 that rest on the same premise: an AI agent with access to corporate data, tools, and financial systems is functionally equivalent to a new employee who has not yet earned trust1,3. The convergence matters because it is moving "agent-as-insider-threat" from a conceptual warning to a product category with concrete controls, pricing tiers, and compliance hooks.
The big picture
Microsoft's additions center on Project Perception, the agentic security system introduced in June that originally fielded red, blue, and green agent teams to simulate and remediate external attacks. The new layer, Guardian Agents, flips the threat model inward: Guardian Agents monitor every action of every deployed agent before it happens, around the clock8. Alongside Guardian Agents, Microsoft introduced Dynamic Permissions, under which an agent "starts with no access of its own and gets only what it needs for one task, for as long as the task lasts," according to the company6. A companion feature, Dynamic Agent Risk, rates each agent continuously using signals from identity, data, devices, cloud, network, and the agent's own behavior.
Hayete Gallot, executive vice president of Microsoft Security, wrote that companies should treat AI agents as insiders because agents "can reach data, tools, and systems, are often given too much access, and can behave in unexpected ways". She added that frontier models "cannot be trusted" and that agents can become unpredictable even without being compromised, "including by collaborating or colluding with other agents to achieve objectives".
Sumsub's announcement operates at the data-access layer rather than the platform layer. Its new KYA Module for Model Context Protocol screens every agent request and strips personally identifiable and other sensitive information before it reaches the agent4. The module applies a configurable rule engine based on data sensitivity, action type, requesting department, and other parameters. When an agent attempts a flagged or high-value action, the system can trigger a real-time liveness check to confirm an authorized human is behind the request5. The module initially supports Amazon Bedrock AgentCore Gateway, with additional MCP gateways planned.
Between the lines
Satya Nadella's private blog post earlier this month urged enterprises to "stop trusting AI model providers, even if they offer assurances of safety and security with their agentic products," and called for separate systems, not controlled by the AI labs, to watch and control the agents those labs produce. ANALYSIS That framing is striking coming from a company that both sells frontier models through Azure and now sells the tools to distrust them. Microsoft is, in effect, building a business on both sides of the trust gap: supplying the agents and supplying the surveillance layer that treats those agents as potential adversaries.
Nadim Abdo, corporate vice president for identity and network access at Microsoft, stressed that agents "can make mistakes, be manipulated or be compromised" and that "an agent that behaves as intended at the start of a task can act differently as its context changes"7. ◆ The language mirrors how enterprises have historically described privileged human users, not software components, reinforcing the organizational shift from treating agents as tools to treating them as personnel.
Sumsub's approach builds on two earlier milestones: AI Agent Verification in January, which bound AI-driven automation to a verified human identity, and an MCP integration in June that let agents configure and operate the platform directly. ◆ The progression from verifying agents to letting them operate autonomously to now restricting what they can access traces the same arc Microsoft describes: enterprises granted broad permissions first and are now retrofitting controls.
Research cited by Sumsub found that 65% of organizations had experienced at least one security incident involving an AI agent operating on their networks during the previous year, with exposure of sensitive data identified as the leading cause.
What's next
Microsoft's Dynamic Conditional Access extends Entra identity controls to agents, with graduated responses as risk rises. Sumsub plans support for additional MCP gateways beyond Amazon Bedrock AgentCore Gateway. ANALYSIS Both roadmaps assume agent deployments will accelerate, not slow, and that the governance layer will need to scale alongside them. The practical question for enterprise buyers is whether agent security becomes a platform-level feature bundled into suites like 365 E7, a standalone compliance product like Sumsub's KYA, or both. Gallot's position that security systems should be able to "discover agents, assign identities, containers and policies, and then adjust permissions dynamically as risk changes" describes a control plane that did not exist a year ago and that multiple vendors are now racing to define.
