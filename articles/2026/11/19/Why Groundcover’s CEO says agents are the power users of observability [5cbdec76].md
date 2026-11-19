---
id: "5cbdec76c3653574"
title: "Why Groundcover’s CEO says agents are the power users of observability"
url: "https://thenewstack.io/groundcover-coding-agents-observability"
link: "https://thenewstack.io/groundcover-coding-agents-observability"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T03:15:24Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "An AI coding agent can write a patch in minutes. Ask it whether that patch slows down the API endpoint your customers hit most, and suddenly it needs something that lives outside the repository. It needs to see how the software runs. \n\n That’s the premise behind Groundcover , an observability platform that wants to put production telemetry in the hands of developers and their coding agents. Yes,…"
tags: ["AI Agents", "Kubecon Cloudnativecon NA 2026", "Kubernetes", "Observability", "Podcast", "sponsor-groundcover", "Sponsored", "sponsored-podcast", "Video"]
orgs: []
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "summary"
word_count: 636
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Why Groundcover’s CEO says agents are the power users of observability

The New Stack · Chris J. Preimesberger · 2026-11-19

An AI coding agent can write a patch in minutes. Ask it whether that patch slows down the API endpoint your customers hit most, and suddenly it needs something that lives outside the repository. It needs to see how the software runs. 

 That’s the premise behind Groundcover , an observability platform that wants to put production telemetry in the hands of developers and their coding agents. Yes, you read that correctly. 

 In a conversation with The New Stack ’s Frederic Lardinois at KubeCon + CloudNativeCon this month in Salt Lake City, Groundcover CEO and co-founder Shahar Azulay explained why he thinks the same data engineers use to troubleshoot an incident can help an agent write and test a better change in the first place. 

 Your new observability user is an agent 

 “Now agents are the power users of observability,” Azulay told TNS.  

 Groundcover exposes telemetry through the Model Context Protocol (MCP) , giving coding agents a way to query it while they work. An agent investigating a slow API, for example, could use traces to see which service accounts for most of the latency. A developer writing a test could use observed application behavior to pick a scenario customers actually encounter. 

 Groundcover uses that approach internally. Its coding agents pull context from the company’s own telemetry, and agents involved in code review can look at measurements from staging deployments. It’s a way to give a reviewer something concrete to check when a patch looks perfectly reasonable in a diff. 

 Agents also give engineers something new to monitor. Azulay contrasts a familiar application trace that follows a request across several microservices with an agent run that can span hours and thousands of tool calls. A trace that long can make a Kubernetes incident look like light reading.  

 Developers may need to inspect prompts and tool calls or use evaluations to judge whether a run behaved as intended. A completed run tells you the agent stopped. The trace can help you figure out what it did along the way. 

 Less instrumentation work, more room for detail 

 Groundcover uses an eBPF sensor to collect application and infrastructure telemetry without requiring developers to add an SDK to every service. It also supports OpenTelemetry, so teams can keep sending the signals they already collect and add custom instrumentation where they need more detail. That gives developers a baseline for a new service and a way to get more specific when a particular path or business operation warrants it. 

 Where the data runs is part of the pitch. Groundcover’s bring-your-own-cloud model keeps telemetry and Groundcover’s agent operations in the customer’s cloud environment, Azulay said. Customers pay for the underlying infrastructure, and Groundcover manages the deployment.  

 For teams weighing how much telemetry to retain, the model puts the infrastructure bill in their own account. It also matters when prompts or tool calls may contain sensitive customer data and teams want to keep that information under their control. 

 We also ask what happens when the platform starts acting on what it sees. Azulay points to Groundcover’s move into Kubernetes optimization, where the immediate work centers on cost and resilience. He sees a path from there to agents that can help address an incident on both sides of the deployment, proposing a code change and adjusting infrastructure configuration. The conversation also gets into the practical work of switching observability platforms, including what happens to the dashboards and monitors engineers have spent years building. 

 Watch the full KubeCon interview on The New Stack ’s YouTube channel to hear how Groundcover uses its own telemetry in code reviews and why Azulay thinks the next generation of coding agents will be a regular part of the observability stack. 
 The post Why Groundcover’s CEO says agents are the power users of observability appeared first on The New Stack .
