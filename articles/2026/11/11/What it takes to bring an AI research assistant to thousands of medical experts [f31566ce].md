---
id: "f31566cea4eb1d90"
title: "What it takes to bring an AI research assistant to thousands of medical experts"
url: "https://commandline.microsoft.com/from-custom-infrastructure-to-hosted-agents"
link: "https://commandline.microsoft.com/from-custom-infrastructure-to-hosted-agents"
source: "Microsoft Source"
domain: "commandline.microsoft.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T21:40:16Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["sbaynes"]
language: "en"
summary: "Tags: \n\n AI Customers Health \n\n The post What it takes to bring an AI research assistant to thousands of medical experts appeared first on Source ."
tags: ["Company News", "AI", "Customers", "Health"]
orgs: ["Microsoft"]
topics: ["agents & coding", "models & research", "health & science", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1415
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# What it takes to bring an AI research assistant to thousands of medical experts

Microsoft Source · sbaynes · 2026-11-11

Clinical research rarely ends with the questions defined in a trial protocol. Medical experts also explore the data from new angles: testing a hypothesis, comparing patient populations, visualizing a trend, or identifying a promising direction for further research.
As part of a forward-deployed engineering engagement, a joint Microsoft and Novo Nordisk development team built an agent that helps medical experts perform this kind of secondary analysis of clinical trial data. We described the original project in a Microsoft customer story. More recently, we reimplemented the solution as a hosted agent in Microsoft Foundry.
The move gave us a simpler operating model, stronger session isolation, and a direct path into Foundry’s tracing, evaluation, experimentation, optimization, and governance capabilities. It also taught us practical lessons about infrastructure planning, observability, and preserving the learning loop that already made the agent better over time.
Here’s what changed, what we measured, and what we would recommend to teams making a similar move.
An agent for questions that don’t have a fixed workflow
Secondary analysis of clinical data is a great task for an agent because the execution path depends heavily on the question. The agent interprets the request, inspects the available data, writes and executes analysis code, examines the result, and often revises its approach before returning a summary and visualization.
This isn’t just attaching a chat interface to a single API. The agent needs a reasoning loop, access to domain-specific skills, and tools for working with data. In our implementation, code execution is the central tool. The agent can generate analysis code and visualizations inside a controlled environment while the surrounding application manages the conversation and presents the result to the user.
Our first production architecture ran the agent in Azure Container Apps. We used PostgreSQL for conversation storage and Azure Container Apps dynamic sessions for sandboxed code execution. That architecture gave us explicit control over every component, and it proved the value of the use case.
It also meant that our team owned much of the platform around the agent: container scaling, session lifecycle, conversation persistence, execution isolation, networking, telemetry, and the integration among them. Foundry hosted agents offered a simpler division of responsibility.
Moving the runtime boundary into Foundry
A hosted agent is our code, packaged as a container, running on infrastructure managed by Foundry Agent Service. We retain control of the orchestration logic, models, tools, and runtime behavior. Foundry manages the endpoint, agent identity, session compute, state persistence, scaling, and lifecycle around it.
At runtime, each session gets its own VM-isolated sandbox. Foundry provisions compute on demand, keeps it active while the session is in use, and de-provisions it after the configured idle period. Session files can persist and be restored when the session resumes. Scaling follows active sessions rather than a replica count that we have to predict and configure.
For Novo’s workload, that model aligned well with the unit of work we were building for: one expert conducting one analysis session. It also changed the architecture in four important ways:
- Scaling became session-native. We no longer needed to connect application-level session creation to a separately scaled pool of execution environments. The platform owns that lifecycle.
- Isolation became the default unit of execution. Each session runs in a VM-isolated sandbox rather than sharing a process or general-purpose application container with other sessions. That matters when the workload includes model-generated code operating on sensitive clinical data.
- Network isolation became part of the service architecture. Foundry Agent Service supports private networking, including virtual network integration and private access to dependent Azure resources. This lets us design controls for both ingress and egress around the agent environment. Those controls are especially important for data that must remain inside an approved network boundary.
- The agent joined a broader development lifecycle. Traces, evaluations, experiments, monitoring, and optimization can now be connected through the same platform. Microsoft Agent 365 integration also provides a path to enterprise inventory, identity, access control, and lifecycle governance.
Using Foundry hosted agents didn’tt remove our responsibility for security or quality. We still had to define access controls, minimize and protect telemetry, test the agent for our use case, and review every system it can call. What changed is that several controls we previously assembled ourselves are now platform capabilities we can configure and operate consistently.
Lessons learned
Here are the top lessons we learned during this project—and some practical advice for your own hosted agents projects in Foundry:
Lesson 1: Treat infrastructure choices as product decisions
Private networking should be an early architecture decision, not a production hardening task left until the end.
Hosted agents consume network capacity according to sessions. The Foundry account, its projects, hosted agents, concurrent sessions, and agent revisions all contribute to IP usage. Because the assigned subnet is an immutable reference at the account level, an undersized range can turn a capacity adjustment into a broader infrastructure migration.
Our advice is to estimate peak concurrent sessions across the account, include headroom for deployments and growth, and involve the network team before creating the Foundry resource. The current networking guidance recommends a /24 subnet for production hosted agent deployments and documents /27 as the supported minimum for smaller deployments.
We used Azure Verified Modules as the foundation for repeatable environments. That gave us a strong starting point, but infrastructure as code doesn’t remove the need to inspect generated dependencies. Throughput for resources like Azure Cosmos DB should reflect expected concurrency and data access patterns. Where a setting requires an operational adjustment, capture it in the deployment process or operator runbook rather than leaving it as unwritten production knowledge.
Subnet sizing, database throughput, private endpoints, DNS, and concurrency aren’t separate infrastructure details. Together, they shape the scale ceiling and reliability of the product.
Lesson 2: Make traces easy to navigate
Foundry tracing uses OpenTelemetry and stores telemetry in Azure Monitor Application Insights. It can capture user inputs, agent outputs, model calls, tool activity, token usage, and latency. That gives us the raw material to understand both reliability and agent behavior.
During the migration, we sent agent traces to both Application Insights and Langfuse. Keeping the existing telemetry path available gave the team continuity while we connected the agent to Foundry’s observability capabilities.
An engineer needs to move quickly from a reported problem to the relevant interaction: what the user asked, what the agent returned, how many operations the run produced, how long it took, and how many tokens it consumed. Stable user, session, conversation, agent-version, and trace identifiers make those views searchable and connect activity across the frontend, backend, agent, and tools.
Be equally deliberate about what not to record. Foundry’s tracing guidance notes that traces can include prompts, outputs, tool arguments, and tool results. For clinical workloads, telemetry needs the same access control, minimization, redaction, and retention discipline as other sensitive production data.
Lesson 3: Preserve the learning loop during migration
We kept the backend contracts stable, which made the migration significantly easier. Our evaluation framework could call the Foundry-hosted implementation through the same interface it used before, so moving the runtime didn’t require us to rebuild the quality system around it.
We could continue to run the same evaluation set against the agent and apply the same graders to its output. Those graders included comparisons with golden answers supplied by subject matter experts. The resulting scores gave us a baseline for the migration, guarded against regressions, and pointed to areas where changes to instructions, tools, or orchestration improved the system.
This is where the broader Foundry lifecycle becomes especially useful. Traces explain what happened in a run. Evaluations measure the result. Experiments compare alternatives. Optimization turns that evidence into candidate improvements. Bringing those capabilities closer together creates a shorter path from a production observation to a tested change.
CONTINUOUS LEARNING LOOP
The takeaway
Our original architecture gave Novo a working agent for a valuable and demanding research scenario. Moving it to hosted agents let us keep control of the agent logic while transferring more of the undifferentiated runtime work to Foundry. The result is not only a different place to run a container. It’s a cleaner platform boundary: isolated compute per session, managed scaling and identity, private networking, durable state, and an integrated path from tracing to evaluation and optimization.
For teams deciding how to take an agent from prototype to production, that boundary is worth evaluating early. Build the part that makes your agent distinct. Let the platform carry more of what every production agent needs.
