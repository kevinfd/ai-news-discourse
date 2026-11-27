---
id: "e75a6a337c39b9cf"
title: "A developer ran 50 agents at once. Then his Mac became the bottleneck."
url: "https://thenewstack.io/ai-agents-remote-sandboxes"
link: "https://thenewstack.io/ai-agents-remote-sandboxes"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-26T16:12:29Z"
published_date: "2026-11-26"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "As developers move from working with individual AI coding agents to orchestrating dozens of concurrent sessions, the hardware they use to develop software is becoming a potential bottleneck. \n\n In a post on X Monday, a developer named Pranit described how running more than 50 concurrent agent sessions exposed the biggest bottleneck in his development workflow: his Mac. \n\n Vercel CTO Malte Ubl…"
tags: ["AI Agents", "AI Infrastructure", "Developer tools"]
orgs: []
topics: ["agents & coding", "chips & infrastructure"]
content_source: "summary"
word_count: 667
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A developer ran 50 agents at once. Then his Mac became the bottleneck.

The New Stack · Amanda Caswell · 2026-11-26

As developers move from working with individual AI coding agents to orchestrating dozens of concurrent sessions, the hardware they use to develop software is becoming a potential bottleneck. 

 In a post on X Monday, a developer named Pranit described how running more than 50 concurrent agent sessions exposed the biggest bottleneck in his development workflow: his Mac. 

 Vercel CTO Malte Ubl responded that he had encountered the same limitations in his own development workflow. 

 “No single computer is fast enough to keep up with dozens of agents working on parallel.” 

 “No single computer is fast enough to keep up with dozens of agents working on parallel,” Ubl writes . 

 Rather than moving the agents themselves to the cloud, Ubl keeps them running locally and offloads builds and tests to remote sandboxes. Developers can retain their existing tools and workflows without being constrained by the compute capacity of a single machine. 

 “Dozens of agents can all decide to run a build at the same time,” Ubl tells The New Stack . “They’re competing for the same machine, and everything slows down.” 

 When agents outrun one machine 

 Even when model inference runs in the cloud, compilation, dependency management, and test execution initiated by coding agents can place significant demands on local CPU and memory. 

 Separating agent orchestration from code execution lets developers scale those workloads independently of their local hardware. 

 Separating orchestration from execution 

 Developers can install the Vercel Plugin by running npx plugins add vercel/vercel-plugin and then instruct their coding agents to offload builds and tests to remote sandboxes. 

 One technical challenge of remote execution is maintaining consistency between the local workspace and the sandbox, particularly when agents modify code that hasn’t been committed. 

 Ubl tells The New Stack that execution begins from a snapshot with dependencies already installed. The current source code, including uncommitted edits and new files that aren’t excluded by Git ignore rules, is then copied to the sandbox. Dependencies persist in the remote environment and are updated when they change. 

 “You shouldn’t have to commit and push just to test what an agent is working on.” 

 “You shouldn’t have to commit and push just to test what an agent is working on,” Ubl says. 

 Unlike conventional CI workflows triggered by repository events, this approach brings remote execution into the development feedback loop itself. 

 Agents can validate changes before committing, and computationally expensive tasks no longer need to compete for the same local resources. 

 When remote execution pays off 

 There is no specific number of concurrent agents at which remote execution becomes more efficient than running builds and tests locally. 

 The crossover depends on the project’s computational requirements, the frequency of builds and tests, network latency, and the cost of provisioning remote infrastructure. 

 “You have to weigh the upload, setup time and cloud compute cost against the time saved.” 

 “You have to weigh the upload, setup time and cloud compute cost against the time saved,” Ubl tells The New Stack . “Warm snapshots help.” 

 In Seoul, regional image caching brought sandbox startup times down from roughly 3.5 seconds to 1.05 seconds, according to benchmarks published by Vercel . 

 But spinning up a sandbox is only part of the equation. Developers still have to transfer source files and pay for remote compute. Vercel did not provide benchmarks comparing the total time or cost of running builds and tests locally versus remotely. 

 Local execution may still make more sense when running a handful of agents on a small codebase. The economics could change when dozens of agents compete for CPU and memory to run builds and tests concurrently. 

 Local development goes distributed 

 Remote build systems and cloud-based development environments predate AI coding agents. What’s changing is the number of concurrent workloads an individual engineer can generate. 

 “As developers run more agents in parallel, I expect this split to become common,” Ubl tells The New Stack. 

 The post A developer ran 50 agents at once. Then his Mac became the bottleneck. appeared first on The New Stack .
