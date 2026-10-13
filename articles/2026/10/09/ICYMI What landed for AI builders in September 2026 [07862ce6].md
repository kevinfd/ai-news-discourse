---
id: "07862ce6a3faf1ca"
title: "ICYMI: What landed for AI builders in September 2026"
url: "https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-09T15:38:39Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Prachi Mishra"]
language: "en"
summary: "A recap of the latest Amazon Bedrock, Amazon Bedrock AgentCore, and Strands updates from September 2026 \n At AWS, we believe the fastest path to enterprise AI is giving builders real choice at every layer: model, runtime, and tooling. That belief shapes how we invest across Amazon Bedrock, AgentCore, and Strands. Amazon Bedrock continues expanding access to leading frontier models so you can…"
tags: ["Amazon Bedrock", "Amazon Bedrock AgentCore", "Foundational (100)", "Thought Leadership"]
orgs: ["Amazon", "OpenAI", "Anthropic", "xAI", "Hugging Face"]
topics: ["models & research", "agents & coding", "business & funding", "safety & ethics"]
content_source: "fulltext"
word_count: 1084
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# ICYMI: What landed for AI builders in September 2026

AWS Machine Learning Blog · Prachi Mishra · 2026-10-09

Artificial Intelligence
ICYMI: What landed for AI builders in September 2026
A recap of the latest Amazon Bedrock, Amazon Bedrock AgentCore, and Strands updates from September 2026
At AWS, we believe the fastest path to enterprise AI is giving builders real choice at every layer: model, runtime, and tooling. That belief shapes how we invest across Amazon Bedrock, AgentCore, and Strands. Amazon Bedrock continues expanding access to leading frontier models so you can build and scale AI applications securely. Amazon Bedrock AgentCore provides the managed infrastructure to build, connect, and deploy enterprise agents using any framework or model. Strands gives you an open source toolkit to build agents and run anywhere.
As AI models become more capable and model choice expands, the industry conversations are shifting. Model performance is no longer the only question. Customers now weigh cost against benefit for their specific use case, and those decisions matter when delegating work to agents in production. AI agents are already moving into workflows that require them to reason over enterprise knowledge, operate across long-horizon tasks, and act in systems where security, accuracy, and governance matter. The focus is now shifting beyond the model itself to the broader system around it, including the context agents can access, the actions they can take, and how enterprise data is governed and protected.
In September, updates across Amazon Bedrock, AgentCore, and Strands strengthened those foundations. New capabilities expanded model choice, made agent operations more efficient and measurable, and created more direct ways to connect AI applications with current business information.
Run faster agents and evaluate what matters
Build agents optimized for OpenAI models. Amazon Bedrock Managed Agents, powered by OpenAI, is now available in public preview, helping you build production-ready AI agents without sacrificing enterprise security. You can now use OpenAI models while keeping data within AWS, reuse existing AWS Identity and Access Management (IAM) permissions, and maintain full auditability through AWS CloudTrail. Durable sessions and built-in human approval workflows help reduce development overhead and mitigate risk.
Agents now start faster with less infrastructure overhead. The latest AgentCore runtime, a capability of Amazon Bedrock AgentCore, has more efficient memory management and lower cold start latency for serverless agents, so you pay for actual usage rather than the peak memory. You can run agents faster at lower cost with pay-as-you-go pricing and no need to pre-provision capacity. Sessions scale to zero when idle and run in hardware-isolated environments.
Lower your token cost with frontier performance. Strands harness is a new open source agent harness that matches popular harnesses on accuracy while using 28 percent fewer tokens. You can spin up a production-ready agent in a single line of Python or TypeScript, with built-in context management, prompt caching, and memory, then deploy it anywhere.
Let your models make big decisions safely, locally. Strands Decider 2B is a small, open source, 2B-parameter decision model that picks between predefined options (instead of generating text), delivering answers in ~115ms locally. It’s optimized for agentic AI tasks like tool selection, routing, and guardrails, with all code, data, and weights available on GitHub and Hugging Face.
Find the right model for each workload
Choose from a broader set of OpenAI models for your everyday work. OpenAI’s Astra, Sol, and Luna models are now generally available on Amazon Bedrock, with options for demanding projects, recurring complex work, and high-volume tasks.
GPT-6 Astra is the flagship model for your most ambitious work, bringing deeper reasoning to complex decisions, document analysis, and software development with up to 1 million input tokens. It brings stronger reasoning and more precise judgment to complex business decisions, operates across software and files, and delivers professional-quality output aligned with organizational voice, templates, and standards. GPT-6 Astra Ultrafast adds a premium speed tier for GPT-6 Astra, built for workloads where speed matters most. It delivers up to 6x faster inference in the API, with up to 300 tokens per second.
Sol brings near-Astra intelligence to coding, computer use, and professional workloads that run frequently. Both GPT-6.1 Sol and GPT-6 Sol are available on Amazon Bedrock. GPT 6.1 Luna is designed for high-volume tasks such as extraction, summarization, classification, and routing. Together, they help you balance intelligence, latency, and cost across workloads.
Take on long-running coding and research with Claude. Model choices for Claude now include the latest versions to advance your coding and scientific work. Claude Fable 5.1 expands options for coding, scientific research, and enterprise workflows. Claude Opus 5.5 is built for agentic coding, knowledge work, and long-running tasks. It uses adaptive thinking to gauge how much reasoning a task needs and an effort parameter to set an upper bound on reasoning depth. Claude Sonnet 5.5 is a smarter, more efficient Sonnet suited to focused coding and knowledge work, delivering 30 percent lower cost per task at 30 percent faster speed than Claude Sonnet 5.
Reason through complexity with a broader model portfolio. Moonshot AI’s Kimi K3 is now available on Amazon Bedrock. According to Moonshot AI, Kimi K3 is its most capable model and the first open model to reach 2.8 trillion parameters. With a 1-million-token context window, native vision, and built-in prompt caching, it helps you build smarter apps 2.5x faster at lower cost than previous versions.
xAI’s frontier models Grok 4.6 and Grok 4.7 offer a 500K token context window and support configurable reasoning effort and self-verification for more reliable long-running tasks.
Together, these additions give you more flexibility when matching models to your requirements such as context length, latency, throughput, and cost.
Get more control over your enterprise AI agents
Keep agent knowledge current. With new automatic sync scheduling in Amazon Bedrock Managed Knowledge Base, you can now configure daily, weekly, and monthly refresh options for all native data-source connectors. As a result, your enterprise AI agents retrieve the latest information. The user-managed setup for SharePoint, OneDrive, and Confluence reduces reliance on admin-managed service accounts when you already have the access you need.
Connect more enterprise sources without maintaining custom ingestion pipelines. Amazon Bedrock Managed Knowledge Base now supports ServiceNow, Confluence Data Center, Salesforce, and Zendesk as native connectors to handle data crawling, metadata extraction, and incremental sync automatically. These connectors reduce the amount of custom ingestion code you need to build and maintain support content, internal documentation, and operational knowledge.
Get started
Explore Amazon Bedrock, deploy agents with the AgentCore CLI, or build your first agent with the Strands Harness SDK.
Interested in learning how Amazon Bedrock can support your team? Connect with us to start the conversation.
