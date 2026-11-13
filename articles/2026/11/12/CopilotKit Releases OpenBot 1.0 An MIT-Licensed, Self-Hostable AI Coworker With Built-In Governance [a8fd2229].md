---
id: "a8fd2229a85b22e2"
title: "CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Coworker With Built-In Governance"
url: "https://marktechpost.com/2026/11/12/copilotkit-openbot-1-0-open-source-ai-coworker"
link: "https://marktechpost.com/2026/11/12/copilotkit-openbot-1-0-open-source-ai-coworker"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T21:45:36Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Most AI coworker products are vendor locked. They pick the model, host the data, and write the rules. CopilotKit is taking the opposite route. OpenBot 1.0 , was released November 9th, an MIT-licensed , self-hostable agent workspace. What sets it apart is, a company brings their own models, agents and infrastructure. Governance is fully baked in, and every Bot action is checked against a policy…"
tags: ["Agentic AI", "AI Agents", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Generative AI", "Harness", "Language Model", "New Releases"]
orgs: ["OpenAI", "Google", "Microsoft", "Anthropic", "Amazon", "xAI", "Mistral", "DeepSeek"]
topics: ["agents & coding", "policy & regulation", "models & research", "products & launches"]
content_source: "summary"
word_count: 833
paywalled: false
image: "https://www.marktechpost.com/wp-content/uploads/2026/11/image.png"
discussion_url: null
score: null
comments: null
community: null
---

# CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Coworker With Built-In Governance

MarkTechPost · Asif Razzaq · 2026-11-12

Most AI coworker products are vendor locked. They pick the model, host the data, and write the rules. CopilotKit is taking the opposite route. OpenBot 1.0 , was released November 9th, an MIT-licensed , self-hostable agent workspace. What sets it apart is, a company brings their own models, agents and infrastructure. Governance is fully baked in, and every Bot action is checked against a policy before it runs. 

 What is OpenBot? 

 OpenBot is a modular agent workspace from CopilotKit , the team behind the AG-UI protocol. You give a Bot a task and watch it work. You review findings, interact with results and approve next steps in the same conversation. 

 Each Bot gets a computer of its own . That is a container with its own Chromium browser, logins and files. It reaches only the tools you grant. Answers can come back as charts, checklists, tables and cards. In the new v1.0, Bots now reply in Markdown by default and draw components when they help. 

 How does the governance gateway work? 

 Every browser click, file write, MCP tool call and component goes through one gateway. It evaluates a CEL policy, writes the audit row first , then acts. Deny rules run before allow rules, and a broken rule refuses rather than opens. 

 On top of that, the business tier adds: 

 Single sign-on and SCIM sync for users and groups. The README documents Google, Microsoft (Entra) and Okta, plus SAML and OIDC. 

 On-behalf-of tokens, usually scoped to a subset of the person’s permissions. 

 Tool grants per Bot, per role or per person, with access requests to an admin. 

 Policies that block actions or route sensitive work to a human for approval. 

 Spend visibility per Bot, role, team or person, plus daily, weekly or monthly token limits. 

 A full audit trail with SIEM export, multi-tenancy and an admin plane. 

 EU AI Act content labeling, retention controls and deletion on request. CopilotKit itself holds SOC 2 Type II. 

 Which agents and models can you bring? 

 Any agent that speaks AG-UI plugs in. The site lists 8 frameworks: Claude Agent SDK, OpenAI Agents SDK, LangChain, Google ADK, Mastra, AWS Strands, Microsoft Agent Framework, CrewAI. The repo also ships Agno, AG2, LlamaIndex and Pydantic AI examples. 

 For models, teams can use OpenAI, Claude, Gemini or Grok through existing subscriptions or API keys. Open models such as Kimi, DeepSeek, Qwen, Nemotron and Mistral are also supported. Sandboxes, MCP hubs and browsers are swappable lanes. 

 What is new in OpenBot 1.0? 

 Desktop app for Mac (Apple Silicon and Intel) and Windows, with signed updates and backup before upgrade. 

 Teach a Bot: record a task once, and Learning turns the recording into a reusable skill you review. 

 Multiple accounts per app through Composio and Arcade , with approval rules saved per account. Composio alone brokers a few hundred apps. 

 Orchestration: one Bot can hand work to specialist Bots, within admin-granted pairs and depth limits. 

 Early access for iOS, Android, Slack (through OpenTag) and Microsoft Teams. 

 How do you deploy it? 

 Personal use runs locally, with workspace data and API keys stored on your machine. For companies, 1 Helm chart deploys into AWS (EKS), Azure (AKS), Google Cloud (GKE) or any Kubernetes cluster. 

 Pricing is free for personal projects. OpenBot for Business costs up to $29 per active user per month. A 5% charge applies only to model spend above $5,000 per month. The Annual plan adds air-gapped deployment and 24/7 support. Forward-deployed engineers help teams roll it out. 

 Example use cases 

 Ticket triage: route new support tickets, then post to Slack after a person approves. 

 Expense review: check each claim line against policy and flag overages. 

 Ops workflows: find problems and draft fixes for a human to approve. 

 How does OpenBot compare? 

 Feature OpenBot 1.0 OpenAI dots  OpenClaw  Code license MIT Closed MIT  Where it runs Laptop, your VPC, any Kubernetes OpenAI cloud computer per dot Your machine, VPS or server Models OpenAI, Claude, Gemini, Grok, Kimi, DeepSeek, Qwen, Nemotron, Mistral GPT-6 Astra Model-agnostic Bring your own agent Any AG-UI agent, 8+ frameworks Not disclosed Built around its own agent Policy before each action Yes, CEL gateway, fail closed User-set approval rules Not disclosed SSO / SCIM Yes (business tier) Enterprise admin controls, beta Not disclosed Apps / tools Composio, Arcade, MCP 4,000+ apps Plugins and skills Price Free personal; up to $29/user/month First dot included in ChatGPT Pro and Business Premium Free; you pay for models and hosting 

 Key Takeaways 

 OpenBot 1.0 is MIT-licensed and self-hostable, from laptop to Kubernetes. 

 Any AG-UI agent and 9 model families plug in. 

 Every Bot action passes a policy check before it runs. 

 Business tier: up to $29 per active user per month. 

 Check out the GitHub repo , v1.0.0 release notes and open.bot . 

 Thanks to the Copilotkit team for the thought leadership / resources for this article. This article is sponsored by Copilokit. 
 The post CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Coworker With Built-In Governance appeared first on MarkTechPost .
