---
id: "728c42f6370fd8ef"
title: "Microsoft’s new Copilot harness makes agents easy — until you want to switch"
url: "https://thenewstack.io/microsoft-copilot-harness-foundry"
link: "https://thenewstack.io/microsoft-copilot-harness-foundry"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T20:54:15Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Microsoft is opening up the GitHub Copilot agent harness to outside developers through Microsoft Foundry, bringing the same orchestration infrastructure used across its Copilot products into a managed service for building and deploying autonomous agents. \n\n Announced Wednesday , the Microsoft Copilot harness is now available in public preview through Foundry Agent Service. It comes with built-in…"
tags: ["AI Agents", "AI Infrastructure", "Developer tools"]
orgs: ["Microsoft"]
topics: ["agents & coding", "models & research", "robotics & autonomy"]
content_source: "fulltext"
word_count: 566
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft’s new Copilot harness makes agents easy — until you want to switch

The New Stack · Amanda Caswell · 2026-10-29

Microsoft’s new Copilot harness makes agents easy — until you want to switch
Microsoft is opening up the GitHub Copilot agent harness to outside developers through Microsoft Foundry, bringing the same orchestration infrastructure used across its Copilot products into a managed service for building and deploying autonomous agents.
Announced Wednesday, the Microsoft Copilot harness is now available in public preview through Foundry Agent Service. It comes with built-in sandboxing, reusable skills, MCP integrations, and support for subagents. Microsoft takes care of running the agent and managing its execution environment, leaving developers to choose a supported model and configure the instructions and tools for their applications.
The same harness now supports Copilot Code, Copilot Studio, GitHub Copilot, the CLI, and VS Code.
The company is also using GitHub’s agent infrastructure across more of its Copilot products. It’s a continuation of the Foundry strategy outlined at Build 2026, which focuses on making AI agents easier for companies to run, manage, and control. The same harness now supports Copilot Code, Copilot Studio, GitHub Copilot, the CLI, and VS Code.
Inside the managed Copilot harness
Microsoft’s harness manages model and tool calls, tracks context, and keeps agents within configured policies. Skills can package instructions, scripts, and supporting resources, while MCP integrations require authentication and approval. Agents can also work with files, run code, and delegate tasks to subagents, with the main agent coordinating the results.
Microsoft’s harness manages model and tool calls, tracks context, and keeps agents within configured policies.
How developers deploy agents
The company’s technical walkthrough shows how this works with a research agent. A Markdown-based skill lays out the steps for collecting evidence, analyzing data, and writing a report, while an azure.yaml file defines the model deployment, tools, instructions, and harness.
Developers select microsoft_copilot_preview as the harness type, deploy the agent using azd deploy --all and invoke it through the Azure Developer CLI. They can keep agent configurations and supporting files in source control, making it easier to track changes alongside their application code.
Runtime limits and lock-in
The Copilot harness must be selected when creating a prompt agent, and that choice can’t be changed later, even in a new version. Microsoft also controls how much CPU and memory the agent gets and how long it can sit idle. Developers can decide what their agents do, but have less control over the environment they run in.
Developers can decide what their agents do, but have less control over the environment they run in.
Microsoft is positioning its broader harness strategy as multi-model, although there are limits. Developers can choose from compatible models deployed through Foundry, but bringing their own models isn’t supported with the managed Copilot harness.
Teams that want more control can use Foundry’s hosted agents instead. Teams can build and run agents using their own frameworks and customize how they operate, while Microsoft handles the hosting. The company also announced general availability of long-running resilience for hosted agents on Wednesday, helping them recover from interruptions during tasks that take hours or even days to complete.
Foundry agent pricing explained
The Copilot harness in Foundry Agent Service for free until December 1, 2026, although model inference and some tools and connected services still come with separate charges.
After that, Microsoft will charge $0.0994 per vCPU-hour for compute and $0.0118 per GiB-hour for memory. Those rates may vary depending on the region and customer agreement.
Learning Path
