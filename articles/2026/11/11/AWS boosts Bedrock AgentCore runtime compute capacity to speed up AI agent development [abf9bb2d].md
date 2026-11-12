---
id: "abf9bb2d1736dedc"
title: "AWS boosts Bedrock AgentCore runtime compute capacity to speed up AI agent development"
url: "https://infoworld.com/article/4247866/aws-boosts-bedrock-agentcore-runtime-compute-capacity-to-speed-up-ai-agent-development.html"
link: "https://infoworld.com/article/4247866/aws-boosts-bedrock-agentcore-runtime-compute-capacity-to-speed-up-ai-agent-development.html"
source: "InfoWorld"
domain: "infoworld.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-11T23:04:00Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Anirban Ghoshal"]
language: "en"
summary: "The new updates bring faster session startup, up to four times more compute, memory reclamation, and data isolation to help developers scale agentic workloads in a cost-effective manner, the company ..."
tags: []
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "business & funding"]
content_source: "fulltext"
word_count: 1107
paywalled: false
image: "http://www.bing.com/th?id=ONUT.WEclzmJzb2XrZjd-4z0hLQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AWS boosts Bedrock AgentCore runtime compute capacity to speed up AI agent development

InfoWorld · Anirban Ghoshal · 2026-11-11

The new updates bring faster session startup, up to four times more compute, memory reclamation, and data isolation to help developers scale agentic workloads in a cost-effective manner, the company said.
AWS on Thursday said that it was upgrading the runtime layer of Amazon Bedrock AgentCore with greater compute capacity, more efficient memory utilization, and faster startup times to help enterprises deploy and scale AI agents more quickly and cost-effectively.
The greater compute capacity includes support for up to four times more compute than the previous version, with each session now supporting up to eight virtual CPUs (vCPUs) and 32GB of memory, the hyperscaler said in a statement.
In addition, the runtime supports container images of up to 10GB, it further said, adding that these upgrades will allow developers to run more demanding agent workloads, including large codebase compilations, browser-driven workflows, and local model inference.
As for memory utilization, the new updates will enable AgentCore runtime to reclaim unused memory within minutes of an agent releasing it and allow idle agents to scale to zero. This will help enterprises reduce the cost of running agents, particularly those that spend considerable time waiting for model responses, tool calls, or human intervention, the hyperscaler said.
For multi-turn agents with natural pauses between interactions, this can reduce memory consumption per session by up to 68%, it added.
Separately, in order to support always-on agents, the hyperscaler has introduced baseline pricing as part of the updates.
Baseline pricing, according to the hyperscaler, sets a minimum memory allocation per session while allowing workloads to burst up to four times that baseline when additional capacity is needed.
That predictability in pricing will allow enterprises to maintain always-on agent sessions without paying for peak capacity upfront while retaining the flexibility to scale when demand increases, it said.
AWS has also extended the runtime’s isolation capabilities beyond compute to the data that agents access and generate during execution by allowing developers to dynamically mount and save agent work to filesystems, including Amazon S3 buckets, using FUSE support.
Previously, enterprises had to build their own mechanisms to manage how files, credentials and tool outputs moved between an agent’s isolated execution environment and external storage systems.
Larger sessions and faster startup could ease agent development
These improvements could make it easier for developers to build and run more complex AI agent workloads, said Ashish Chaturvedi, executive research leader at HFS Research.
“Coding agents that compile large codebases, browser agents that load full web pages, and agents running a small model locally all outgrew the earlier session size, so developers had to either split the work awkwardly or move it outside the isolated environment altogether,” Chaturvedi explained.
“As sessions now stretch to 8 vCPUs and 32GB with 10GB container images, those complex workloads now fit inside the secure boundary,” Chaturvedi added.
The faster startup times, too, are likely to impact developers, particularly in how they provision and manage agent execution environments.
“When a fresh, isolated session takes nearly a minute to start, developers have to maintain warm pools of pre-provisioned capacity to avoid delays, incurring costs even when agents are not actively using those resources,” Chaturvedi said.
“With startup times of under two seconds, regardless of container image size, developers can provision isolated sessions on demand rather than maintaining idle capacity,” Chaturvedi said.
Additionally, the runtime’s ability to reclaim unused memory within minutes while scaling idle agents to zero means developers no longer have to engineer around periods of inactivity, according to the analyst.
“This means that developers can build multi-turn and long-running agents without writing their own logic to shut sessions down, save state, and restart,” Chaturvedi said.
Memory efficiency could lower costs for CIOs
That same efficiency in memory utilization, for CIOs, is likely to result in cost savings, according to Stephanie Walter, practice leader of AI stack at HyperFRAME Research.
“Agents typically should not need the same resources while waiting for approval as they do while executing code. Reclaiming unused memory and scaling idle sessions to zero could reduce the cost of keeping long-running agents available,” Walter said.
“And since enterprises are likely to run hundreds of concurrent agent sessions, particularly agents that spend considerable time waiting for model responses, tool calls or human intervention, reducing resource consumption can be a material change,” Walter added.
Beyond costs, the same improvements in resource utilization could also help CIOs accelerate the rollout of AI agents across the enterprise.
Since improved resource efficiency can help developers build and manage agent workflows more effectively, enterprises could potentially deploy agents faster and scale their use across business functions more quickly, Walter said.
Scale-to-zero, baseline pricing come with trade-offs
However, she warned that CIOs should not assume that runtime’s ability to scale agents to zero would eliminate all associated costs, as storage, model calls, external tools and other services can still incur charges.
“Developers also need to test resumption: are files available, have credentials expired, and does the agent know whether its last action completed? Saving idle resources is useful, but not if waking the agent causes it to repeat a payment or production change,” she added.
Chaturvedi also cautioned that the ability to scale agents to zero could introduce latency when those agents need to resume execution, potentially making it an improper choice for latency-sensitive agents.
Additionally, there could be governance risks as well.
“The lower cost of keeping agents idle could also encourage enterprises to leave large numbers of long-running agents running indefinitely, even when they are no longer needed. These agents may continue to hold permissions and access to enterprise resources, making regular reviews of agent access and deployment necessary,” Chaturvedi said.
Similarly, the committed baseline pricing model could also involve trade-offs for CIOs, particularly when estimating the memory capacity their agents will need.
“If the baseline is set too high, enterprises could end up paying for unused capacity across sessions. If it is set too low, frequent bursts could make costs less predictable, potentially reducing the benefits of committing to a baseline,” Chaturvedi said.
CIOs will therefore need to assess actual workload patterns, understand how additional burst capacity is billed, and monitor usage once agents are deployed, Chaturvedi added.
“The model is likely to work best for workloads with relatively stable resource requirements, while unpredictable or experimental workloads may be better suited to usage-based pricing,” the analyst further said.
Despite these trade-offs, enterprises looking to use the updated AgentCore runtime can access the new capabilities across 19 AWS Regions, the hyperscaler said.
These Regions include N. Virginia, Ohio, Oregon, Canada, São Paulo, Frankfurt, Ireland, London, Milan, Paris, Spain, Stockholm, Malaysia, Mumbai, Seoul, Singapore, Sydney, Thailand, and Tokyo.
