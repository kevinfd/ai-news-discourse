---
id: "e07e9370893dbecf"
title: "Nvidia turns OpenShell into a full hardware stack for safe AI agents"
url: "https://thenextweb.com/news/nvidia-openshell-ai-agents-safety-anthropic-openai"
link: "https://thenextweb.com/news/nvidia-openshell-ai-agents-safety-anthropic-openai"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-21T04:21:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Ana Maria Constantin"]
language: "en"
summary: "Safety and control must be built into the computing architecture,” says Jensen Huang, as Nvidia launches OpenShell for AI agents."
tags: []
orgs: ["Nvidia", "Anthropic", "Microsoft", "Google", "OpenAI", "Meta", "Amazon", "Perplexity"]
topics: ["chips & infrastructure", "agents & coding", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 460
paywalled: false
image: "http://www.bing.com/th?id=ONUT.OSlE59aD2kpvNCDoP23HFw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia turns OpenShell into a full hardware stack for safe AI agents

The Next Web · Ana Maria Constantin · 2026-10-21

Nvidia has released a design for running AI agents inside fixed limits, from enterprise infrastructure to edge machines. Anthropic, OpenAI, Meta, Microsoft, Google Cloud and AWS are among the companies working with it, Nvidia said.
Nvidia announced the OpenShell Reference Architecture at its GTC Berlin conference on Wednesday. It is available now. Last week, Nvidia set out plans for $2B in European deals.
How it works
The design builds on OpenShell, Nvidia’s open source runtime software, which sets a boundary around what an agent can do. Huang said in his keynote that it is released under the Apache 2.0 licence. OpenShell is also part of the agent safety platform Nvidia launched in September. Models run on Nvidia’s Vera Rubin systems. The software that drives the agents and their tools runs on Vera CPUs.
BlueField-4 data processing units run Nvidia Sentry, software that watches agent behaviour from outside the main system. If an agent tries to move outside its software boundary, Sentry quarantines and stops it in milliseconds, Nvidia said. It said Sentry also raises agent capacity by up to 20%.
The design also covers edge machines, including RTX Spark, DGX Spark and DGX Station systems. Nvidia showed RTX Spark laptops built to run agents locally last week.
“AI capability and safety must advance together. As enterprises prepare to deploy billions of AI agents, safety and control must be built into the computing architecture,” said Jensen Huang, Nvidia’s founder and chief executive.
Huang said last week he would cut off customers who build unsafe AI.
Who is working with it
Agents from Anthropic, Cohere, Google, Meta, OpenAI, Perplexity, Reflection and SpaceX Super Intelligence can run on OpenShell infrastructure, Nvidia said. Security companies including 1Password, Check Point, CrowdStrike, Cisco, Fortinet, Okta, Palo Alto Networks and Zscaler are adding support for it.
On stage, Huang pointed to Nvidia’s partnership with Anthropic. Since September, Anthropic has paired Claude Managed Agents, its service for running Claude agents, with OpenShell, so companies can limit what Claude agents do and log every action, Anthropic said at the time.
BBVA and Santander are exploring it to strengthen agent safety and governance. SAP is building it into its Joule Studio runtime. ServiceNow made Arc, a long-running personal agent, generally available on Wednesday, with its actions enforced by OpenShell.
The design runs on Linux and Kubernetes from Canonical, SUSE and Red Hat, and on Windows through Microsoft Execution Containers. It also runs on AWS, Google Cloud and Microsoft Azure. Dell, Cisco, HPE, Lenovo and Supermicro are building infrastructure with it.
“With the OpenShell Reference Architecture, agents can think on Rubin, act on Vera and be governed on BlueField,” Huang said.
Nvidia did not give prices.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
