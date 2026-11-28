---
id: "78f3a567f630c37b"
title: "Vercel’s CEO thinks the next big AI speedup won’t come from smarter models"
url: "https://thenewstack.io/vercel-workflow-sdk-harness"
link: "https://thenewstack.io/vercel-workflow-sdk-harness"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-27T16:50:06Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Some of the biggest gains in AI performance over the past year have come from improvements to the harness, not the model itself. But Vercel CEO Guillermo Rauch believes that as models become more capable, some implementation details developers have spent months refining will become less visible, and the infrastructure that executes agents will become more important. \n\n “As AI gets smarter,…"
tags: ["AI Agents", "AI Infrastructure", "Developer tools"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research"]
content_source: "summary"
word_count: 663
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Vercel’s CEO thinks the next big AI speedup won’t come from smarter models

The New Stack · Amanda Caswell · 2026-11-27

Some of the biggest gains in AI performance over the past year have come from improvements to the harness, not the model itself. But Vercel CEO Guillermo Rauch believes that as models become more capable, some implementation details developers have spent months refining will become less visible, and the infrastructure that executes agents will become more important. 

 “As AI gets smarter, implementation details blur away: permissions, code diffs, commands, tool calls. … The harness itself blurs away.” 

 “As AI gets smarter, implementation details blur away: permissions, code diffs, commands, tool calls,” Rauch wrote in a post on X . “The harness itself blurs away.” 

 Rauch doesn’t expect the harness to disappear entirely. He sees its role shifting toward executing agents and preserving their state. 

 Vercel offered a glimpse of what that architecture could look like on Wednesday with the release of Workflow SDK 5.8 , which introduces a rebuilt execution engine that substantially reduces the infrastructure overhead associated with running durable agents. 

 Latency between the model calls 

 Inference speed accounts for only part of an agent’s total execution time. Much of the latency can accumulate in the infrastructure that handles work between model calls. 

 Vercel’s new execution engine addresses that overhead through speculative execution of retryable workflow steps. 

 In its benchmarks , Vercel reported that p75 step-to-step overhead fell from 85 milliseconds to 7 milliseconds between Workflow SDK versions 5.2 and 5.8. 

 A five-turn agent loop involving durable token streaming and tool calls incurred just 900 milliseconds of infrastructure overhead… 

 A five-turn agent loop involving durable token streaming and tool calls incurred just 900 milliseconds of infrastructure overhead, compared with three seconds in the previous version. 

 The performance gains are particularly noticeable when agents run multiple tasks in parallel. In Vercel’s benchmark of 256 parallel steps, execution overhead dropped from 13.5 seconds to 2.5 seconds. The time functions spent outside the application’s step code also decreased by a factor of nearly 14. 

 None of those improvements requires switching models, modifying prompts, or giving an agent additional reasoning capabilities. 

 As inference becomes faster, the overhead of persisting state, scheduling execution and resuming workflows can account for a larger share of an agent’s end-to-end latency. 

 Speculative execution and its limits 

 Vercel’s implementation of speculative execution requires idempotent steps. For operations that cannot safely be repeated, developers can disable speculation and retries by setting maxRetries = 0 . 

 Even as models get better at orchestrating their own work, they still depend on the underlying infrastructure for durable execution and recovery from failures. 

 Even as models get better at orchestrating their own work, they still depend on the underlying infrastructure for durable execution and recovery from failures. 

 A 6 MB coding harness 

 Rauch’s vision for the agent harness is reflected in the design of fx. Despite supporting subagents, MCP, skills, sessions, durable execution, ACP, a terminal user interface, and network transport, Rauch said the harness still fits within 6 MB. 

 Vercel has applied a similar architectural approach to eve, an open source framework that treats agents as directories and uses durable workflows to preserve state across interruptions. 

 Other infrastructure providers are separating agent orchestration from the resources required to sustain execution. OpenAI separated the agent harness from the compute environment in its Agents SDK , while Render introduced AI sandboxes capable of running indefinitely , with durable workflows and persistent file storage. 

 Where harness engineering goes next 

 Much of harness engineering today involves working around model limitations. As models become better at managing their own work, developers may need less application-specific orchestration. 

 Execution guarantees are harder to abstract away. Even highly capable models depend on infrastructure that can manage concurrent processes, preserve state, and recover from failures. 

 Vercel’s latest benchmarks lend weight to Rauch’s bet that the competitive advantage will shift from making agents smarter to building infrastructure that makes them faster and more reliable. 
 The post Vercel’s CEO thinks the next big AI speedup won’t come from smarter models appeared first on The New Stack .
