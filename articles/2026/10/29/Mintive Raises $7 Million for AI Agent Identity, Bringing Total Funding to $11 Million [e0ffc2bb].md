---
id: "e0ffc2bbabbfa094"
title: "Mintive Raises $7 Million for AI Agent Identity, Bringing Total Funding to $11 Million"
url: "https://unite.ai/mintive-7-million-ai-agent-identity-11-million-total-funding"
link: "https://unite.ai/mintive-7-million-ai-agent-identity-11-million-total-funding"
source: "Unite.AI"
domain: "unite.ai"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-29T11:41:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Evan Mercer", "AI Startups", "Venture Capital AI Research Agent"]
language: "en"
summary: "Mintive has raised $7 million in new funding led by Cowboy Ventures, bringing its total financing to $11 million as companies seek tighter control over AI agents operating inside their systems. The ..."
tags: []
orgs: ["Google"]
topics: ["agents & coding", "business & funding", "models & research"]
content_source: "fulltext"
word_count: 840
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Isag0QA9PHy_oUZi99MFXQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Mintive Raises $7 Million for AI Agent Identity, Bringing Total Funding to $11 Million

Unite.AI · Evan Mercer, AI Startups, Venture Capital AI Research Agent · 2026-10-29

Funding
Mintive Raises $7 Million for AI Agent Identity, Bringing Total Funding to $11 Million
Add Unite.AI to your preferred sources on Google
Mintive has raised $7 million in new funding led by Cowboy Ventures, bringing its total financing to $11 million as companies seek tighter control over AI agents operating inside their systems. The company says it now handles 2.5 million agent calls a day across more than 50 paying enterprise customers, with over 200 million calls processed in seven months.
The October 29 announcement names customers including Ro, Modern Treasury, Coursera, the University of Michigan, and Apax. The funding backs a platform intended to give each agent its own identity, narrowly scoped permissions, and a traceable record of its actions across enterprise tools and AI models.
Funding for the Infrastructure Around Enterprise Agents
Mintive’s investors include Coatue, Operator Collective, Burst Capital, Maven Ventures, and Hustle Fund. Individual backers include Okta co-founder Frederic Kerrest, WorkOS founder and CEO Michael Grinich, Scott Belsky, Jeff Dean, and Andrej Karpathy. The announcement does not disclose a valuation or designate the new round’s stage.
The underlying problem is permission management. An employee may have access to many systems because their responsibilities span multiple tasks. An agent using that employee’s credentials can inherit a much larger reach than its immediate job requires. As organizations deploy agents through different interfaces, security teams also face fragmented controls and incomplete accounts of who authorized an action.
“Agents are already working inside company systems, and each one needs its own identity and permissions, just as every employee does,” said Jiquan “JQ” Ngiam, Mintive’s co-founder and CEO, in the announcement.
How Mintive Separates Agent Identity From User Credentials
The company’s Agent Identities documentation describes each agent as a separate principal within its gateway. It has its own tool bundle, status, and identity in the audit log. Access can be delegated from the user triggering a task, a team credential, or a service account provisioned for the work.
Underlying service credentials stay in the gateway. The agent authenticates through its own credential and obtains short-lived tokens, while administrators control which individual tools it can reach. Revoking an agent’s token can stop that agent without requiring an organization to disable unrelated users or agents.
This separation also addresses continuity. A business process should not depend indefinitely on the personal credentials of the employee who first configured it. Mintive describes shared administration and transferable ownership for agent bundles, allowing teams to manage access as responsibilities change.
Gateways Govern Both Tools and Model Calls
Mintive combines an MCP Gateway for tool access with an LLM Gateway for model calls. Model Context Protocol provides a common interface between AI applications and external tools; the governance question is which of those connections a particular agent should be allowed to use.
The MCP Gateway product page describes an internal catalog of approved servers, grouped into role-specific bundles. Administrators can disable individual tools, including destructive operations, and apply a common access policy across different AI clients. The gateway can also host internal MCP servers behind enterprise authentication.
Each call is logged with its user, tool, destination server, and guardrail result. The product supports exporting logs to security information and event management systems and streaming them through OpenTelemetry’s OTLP protocol. That gives security teams a way to bring agent activity into their existing monitoring processes.
Mint Guard adds screening for prompt injection, exposed secrets, personal data, and other risks. The company says its platform is SOC 2 Type II audited. These controls help define permitted behavior and make activity inspectable; their effectiveness still depends on the policies and integrations an organization configures.
Customer Workflows Show the Access Problem in Practice
At Modern Treasury, the company says a bank-operations agent searches Sentry, Notion, Linear, source code, and internal tools before a technical account manager intervenes. Mintive reports savings of 30 minutes on simpler cases and up to four hours on complex ones. Those are customer-specific results reported in the announcement.
The University of Michigan uses Mintive as an enterprise MCP gateway, providing a shared route to approved tools while central IT manages access. Mintive also offers Coworker agents in Slack and Teams, combining enterprise tool access with long-term memory and scheduled work.
As Unite.AI’s analysis of enterprise software above the MCP connection layer explains, making a tool reachable is only part of delivering a useful workflow. Mintive is addressing the identity, permissions, and operational record surrounding that connection.
A Founding Team With AI and Software Infrastructure Experience
Mintive, previously known as MintMCP, lists four co-founders in its official media kit: Jiquan Ngiam, Vijay Vasudevan, Bozhi See, and Phillip Bensaid. The release describes Ngiam’s background as Coursera’s founding engineer and a senior staff software engineer at Google Brain, while Vasudevan helped create TensorFlow at Google.
The new funding places the company in a growing operational layer around enterprise AI: deciding which agent can act, whose authority it uses, and what evidence remains afterward. Its reported usage suggests those questions are already production requirements for customers deploying agents across business systems.
