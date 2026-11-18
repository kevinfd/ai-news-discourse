---
id: "863881fd48d98cce"
title: "Vero Security Raises $11 Million Seed Round to Enforce Policies Across AI Agents"
url: "https://unite.ai/vero-security-11-million-seed-ai-security-engineering"
link: "https://unite.ai/vero-security-11-million-seed-ai-security-engineering"
source: "Unite.AI"
domain: "unite.ai"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-18T05:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Evan Mercer", "AI Startups", "Venture Capital AI Research Agent"]
language: "en"
summary: "Vero Security has raised $11 million in seed funding to help enterprises turn AI security policies into controls that operate while employees’ AI tools and agents are doing their work. The round was ..."
tags: []
orgs: ["Google"]
topics: ["agents & coding", "business & funding", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 1045
paywalled: false
image: "http://www.bing.com/th?id=ONUT.GjYCgHPuRWPY6Yf69RxIMg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Vero Security Raises $11 Million Seed Round to Enforce Policies Across AI Agents

Unite.AI · Evan Mercer, AI Startups, Venture Capital AI Research Agent · 2026-11-18

Funding
Vero Security Raises $11 Million Seed Round to Enforce Policies Across AI Agents
Add Unite.AI to your preferred sources on Google
Key PointsVero translates approved security policies into enforced controls rather than leaving…
View more
- Vero translates approved security policies into enforced controls rather than leaving teams with findings lists.
- Runtime enforcement matters because agent permissions and tools can change risk after initial approval.
- Vero's $11 million seed round bets that ongoing policy operations become core enterprise AI security work.
Vero Security has raised $11 million in seed funding to help enterprises turn AI security policies into controls that operate while employees’ AI tools and agents are doing their work.
The round was led by TLV Partners, with participation from GTM Capital, Maple Capital, and angel investors. Founded in 2025, Vero says multiple Fortune 500 companies already use its platform. It plans to invest the capital in product development, broader coverage of enterprise AI technologies and security workflows, and expansion of its U.S. commercial presence.
The startup is targeting a problem that grows with the usefulness of AI agents: software that can read company files, connect to repositories, invoke tools, and execute code also needs boundaries that remain effective as those capabilities change.
Turning an AI Policy Into Working Controls
Vero calls its market AI Security Engineering: the continuing work of discovering how AI is being used, assessing the associated risks, and keeping protections current. Its proposition is to take on more of that operational workload rather than leave security teams with another list of findings.
Security professionals define the policy and decide which changes the platform may implement automatically. Vero translates approved decisions into controls, coordinates fixes with the relevant owners, checks that work has been completed, and adjusts protections as tools and permissions evolve. Changes requiring a fresh risk decision return to a person with supporting analysis and a recommended action.
A company might, for example, allow only developers to connect agents to corporate code repositories or execute code. Vero says one Fortune 1000 customer used that policy as its starting point, and the platform translated it into more than 15 controls spanning coding agents, identities, Model Context Protocol servers, skills, and runtime actions within minutes.
The example illustrates the engineering work hidden inside a simple policy statement. Enforcing who may use an agent is only part of the task; the connected tools, credentials, and operations also have to reflect that decision.
What the AI Runtime Governor Does
At the center of the platform is Vero’s AI Runtime Governor. The company says it inspects supported prompts, tool calls, and agent actions, applying policy when an operation is attempted rather than waiting for a later manual review.
Potential interventions include preventing a coding agent from reading unrelated secrets, blocking actions outside an approved policy, and stopping malicious skills or prompt injection from triggering unauthorized behavior.
Prompt injection occurs when material an AI system encounters contains instructions intended to redirect its behavior. For an assistant that only drafts text, the immediate consequence may be an unreliable answer. An agent with repository access or permission to execute commands can turn the same kind of manipulation into an operation against a real system.
This makes runtime enforcement distinct from a policy written in an agent’s instructions. A rule asking software to avoid a sensitive resource expresses the intended behavior. An enforcement mechanism has to inspect the attempted access and apply the boundary along the execution path it supports.
Why Configuration Checks Alone Are Not Enough
Vero’s website describes four connected functions: inventory, posture analysis, behavior detection, and enforcement. Inventory identifies agents and their owners; posture analysis examines configuration and reachable credentials; behavior detection examines activity during a session; enforcement applies the policy.
Its illustrated workflow follows an agent whose configuration exposes production credentials and whose approved skill later receives a malicious update. The company describes addressing the configuration problem, then blocking the harmful call when the changed skill tries to act.
The distinction is useful because an initial approval is a snapshot. A tool update, new connection, or additional permission can change the risk after deployment. Continuous monitoring and action controls address a different moment from the original assessment.
Model Context Protocol, or MCP, is one of the connection mechanisms involved: it lets AI applications interact with external tools and data sources. Skills supply reusable instructions or procedures. Together with the agent’s credentials, these components help determine what it can actually do.
Vero says it operates through the endpoint, identity, AI, and security tools an enterprise already uses, without requiring employees to install something new. Its enforcement claims apply to supported prompts, tools, and actions; the practical scope of a deployment therefore follows the integrations and execution paths it covers.
A Funding Bet on Ongoing Security Work
Vero was founded by Elad Tessler, its CEO, and Daniel Meirov, its CTO. Tessler previously led product at Astrix Security, while Meirov was Sightfull’s first employee and led its R&D and product work. The founders met in Unit 8200, where they co-led a cyber operations unit of more than 100 people, according to the announcement. Vero has offices in New York and Tel Aviv.
GTM Capital says it invested after a structured evaluation involving its community of Fortune 500 CIOs and CISOs. The announcement describes those executives working directly with Vero before the firm committed.
The investment comes as runtime controls become a more prominent part of enterprise AI security. Other launches, including Sysdig’s AI Defense, also focus on observing agent behavior and enforcing boundaries during execution. Vero’s funding pitch emphasizes the ongoing operating work around those boundaries: implementing decisions, verifying remediation, and keeping the controls aligned with the policy.
Building a Community Around AI Security Engineering
Alongside the funding announcement, Vero is launching AISecurityEngineering.org, an open community and knowledge center with field guides, workshops, and an ASE credential track. The initiative is aimed at professionals establishing AI security practices while often carrying other responsibilities inside their organizations.
The broader opportunity is to make security policy durable even when the software underneath it keeps changing. As enterprises give agents more useful access, the test for platforms such as Vero is whether they can consistently carry a security team’s decisions through to the actions those agents attempt.
