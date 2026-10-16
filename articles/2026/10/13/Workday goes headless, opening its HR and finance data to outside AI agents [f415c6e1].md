---
id: "f415c6e1ed169629"
title: "Workday goes headless, opening its HR and finance data to outside AI agents"
url: "https://thenewstack.io/workday-headless-mcp-agents"
link: "https://thenewstack.io/workday-headless-mcp-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T13:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Workday is opening up its platform and allowing developers to build their own HR and finance agents in Claude Code, Cursor, and other tools, as long as those agents follow the same rules as the people using them. \n\n On Tuesday, at its Workday Rising conference in Las Vegas, the company made its Trusted Agent Platform “headless.” \n\n With this, its Model Context Protocol (MCP) server, SQL access…"
tags: ["AI", "AI Agents", "AI Infrastructure", "Model Context Protocol (MCP)"]
orgs: ["Anthropic", "Google", "Salesforce", "Cursor", "OpenAI", "Meta", "Microsoft", "Nvidia"]
topics: ["agents & coding", "chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1302
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Workday goes headless, opening its HR and finance data to outside AI agents

The New Stack · Frederic Lardinois · 2026-10-13

Workday goes headless, opening its HR and finance data to outside AI agents
Workday is opening up its platform and allowing developers to build their own HR and finance agents in Claude Code, Cursor, and other tools, as long as those agents follow the same rules as the people using them.
On Tuesday, at its Workday Rising conference in Las Vegas, the company made its Trusted Agent Platform “headless.”
With this, its Model Context Protocol (MCP) server, SQL access to live Workday data, and a shared runtime for agents are now generally available, and customers can run their own agents on models from Anthropic, Google, Meta, Mistral, Nvidia, and OpenAI.
As Workday CTO Gabe Monroy noted in a press briefing ahead of the event, “No matter who builds the agent, it runs under Workday permissions, approvals and audit trail — no agent gets a side door.”
Workday notes that many companies currently connect their agents to HR and finance data through copies in a data lake or through service accounts, but, the company argues, those approaches bypass those access controls (though companies like SAP, Microsoft, and others would surely argue that they, too, have access control in place).
MCP tools, SQL, and a shared runtime
For AI developers, the main entry point to the Workday ecosystem is Agent-Ready Tools. That’s the company’s MCP server, which ships as part of Workday Extend AI. Users sign in with their own Workday credentials, and Workday says an agent acting for them can’t reach anything their own account can’t. That’s a key feature here, that ties an agent directly to a user’s account.
Monroy said the server currently offers 275 read tools and 54 tools that write or delete data.
Live Data Query, part of Workday Data Cloud, lets BI tools and agents run SQL queries directly against Workday’s data. Monroy described it as JDBC access to Workday’s object graph, and the company says each query returns only what the requesting user is cleared to see.
Three more components are generally available today. Agent Harness is the shared runtime that Workday’s own agents and those built by customers and partners run on. It passes each agent the user’s identity, org position, and access rights, limits what the agent can do, and picks which model handles each task based on cost and performance. Developer Agent generates Workday agents and apps from a natural-language prompt in Claude Code, Codex, Cursor, or the Workday Developer Site. Custom Agents lets teams deploy agents they built with LangChain or Google’s Agent Development Kit (ADK) onto Agent Harness, though ADK support is limited to design partners for now.
Two more pieces are on the roadmap for early access in early 2027. Agent Context Service will preload only the Workday data a task calls for, which Workday says speeds agents up and limits their exposure to sensitive records. Grounded Reasoning will check a planned action against the customer’s policies, process rules, and Workday records before the agent carries it out.
Workday says customers have built more than 500 agents and more than 6,000 apps with Developer Agent and Agent-Ready Tools in the past four months.
“Headless, the lawless way”
In the briefing, Monroy demoed what he called “headless, the lawless way.” An agent connected to a custom MCP server — a setup he said Workday commonly sees among its customers today — returned job requisitions its user had no business seeing and then moved the wrong employee between teams with no approval. When pointed at a copy of Workday data in Snowflake, the same agent produced the CTO’s salary when asked.
“When it fails, it isn’t just a wrong answer,” Monroy said, “it’s a wrong action that nobody approved.”
When the agent went through Workday’s own MCP server and Data Cloud instead, with the user signed in, the same queries unsurprisingly returned only the requisitions that user was allowed to see (it wouldn’t have been much of a demo of those access controls otherwise, of course).
“A small set of use cases”
Asked whether headless matters as much to Workday as it does to Salesforce, Gerrit Kazmaier, Workday’s president of product and technology, said that Workday is giving customers a choice: “I’d always prefer if they use our user interface, but headless will be equally good.”
Kazmaier noted that building agents directly on Workday’s tools and APIs is “only possible for a small set of use cases where you don’t need to have HR or finance domain logic.” For everything else, he pointed to an AI-to-AI integration in which Claude hands requests to Sana, Workday’s agent orchestrator, which then calls Workday’s own domain agents.
Lakes for analytics, not for agents
It’s worth noting that the Snowflake example is a bit of an awkward one for Workday. When the company announced Data Cloud in September 2025, the pitch included zero-copy sharing of Workday data with Databricks, Salesforce, and Snowflake. Snowflake made its Workday Data Cloud integration generally available on Oct. 7, and Databricks put its Workday connector for Unity Catalog into public beta a day later.
According to Databricks, a Workday admin sets up the connector by registering an Integration System User (ISU), the kind of system account Workday customers use for traditional integrations, with read access to the shared tables. After that, Unity Catalog permissions at the catalog, schema, and table level decide who can query the data.
Monroy said data lakes still make sense for analytics and for joining Workday data with the rest of a company’s data, but that an external lake is “the wrong place to build agents” that need governed access to Workday.
“You can export your data, but you can’t export the rules that govern the data,” he said, adding that rebuilding those rules in the lake means “maintaining a second copy” of Workday’s security model, “and the day it drifts, it’s all wrong.”
Everybody is losing their heads
Headless is the way to go right now, it seems. Salesforce, ServiceNow, and Microsoft, for example, already let outside agents into their systems of record. Salesforce launched Headless 360 at its TDX developer conference in April, so agents in Claude, ChatGPT, Cursor, or a terminal can work with Salesforce data. ServiceNow made its Action Fabric MCP server generally available in May, with Anthropic as a launch partner, and Microsoft offers an MCP server for Dynamics 365 ERP.
All four vendors say outside agents stay within their existing permission models.
Whose identity does the agent use?
When it comes to agent identity, different vendors are currently taking very different approaches.
Salesforce, for example, is preparing to have agents that connect over MCP or its APIs register with their own credentials and permissions instead of acting under a user’s identity, according to Salesforce Ben. MCP clients will eventually need to switch to OAuth credentials tied to those agent identities.
Workday’s documentation says its agents can already get up to two system accounts of their own, called Agent System Users (ASUs), one for acting on a user’s behalf and one for “ambient” work, each with its own OAuth 2.0 client. Workday creates the ambient account automatically when a customer turns on an ambient skill.
Unified.to, which sells a Workday MCP integration, says every Workday MCP path, “official or not,” starts with creating an ISU. Cequence’s setup guide for its Workday MCP integration asks customers to create one “with appropriate security groups.” An agent working through an ISU sees whatever those security groups allow, no matter who is prompting it.
The more telling signal may be Kazmaier’s caveat. If building directly on the MCP server only works for a small set of use cases, the version of headless Workday expects most customers to use is Claude talking to Sana talking to Workday’s own agents, with Workday’s runtime in the middle of every call.
