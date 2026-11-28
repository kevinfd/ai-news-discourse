---
id: "ade01cb2e1b68c1c"
title: "AWS Nitro Sandboxes give AI agents a place to run"
url: "https://thenewstack.io/aws-nitro-sandboxes-agents"
link: "https://thenewstack.io/aws-nitro-sandboxes-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-27T19:16:41Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "A coding agent has written a script and wants to run it. The script may do exactly what the developer asked. The next decision, though, belongs to humans. \n\n The team building the system has to answer a slew of questions: Where should that code run? What should it be able to reach once it starts? \n\n The script doesn’t get a vote. \n\n At the recent KubeCon + CloudNativeCon conference in Salt Lake…"
tags: ["AI Agents", "Containers", "Security", "Podcast", "sponsor-amazon-web-services-aws", "Sponsored", "sponsored-podcast", "Video"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "summary"
word_count: 649
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AWS Nitro Sandboxes give AI agents a place to run

The New Stack · Chris J. Preimesberger · 2026-11-27

A coding agent has written a script and wants to run it. The script may do exactly what the developer asked. The next decision, though, belongs to humans. 

 The team building the system has to answer a slew of questions: Where should that code run? What should it be able to reach once it starts? 

 The script doesn’t get a vote. 

 At the recent KubeCon + CloudNativeCon conference in Salt Lake City, The New Stack’s Frederic Lardinois asked AWS Senior Product Manager Mike Stefaniak what’s keeping more teams from running agents in production. 

 Stefaniak said he’s seen a handful of large customers commit in a big way. Many others are still figuring out security and identity. AWS Nitro Sandboxes , announced at the conference, address one part of that problem by giving developers an isolated place to run container workloads. 

 Keep the image, change where it runs 

 Stefaniak describes Nitro Sandboxes as a way to bring the isolation of the Nitro hypervisor to multiple workloads within one EC2 instance. Each sandbox draws CPU and memory from the parent instance. 

 “You don’t have to change your container image.” 

 On EKS Auto Mode or ECS Managed Instances , Stefaniak says, a runtime configuration tells AWS to place the workload in a sandbox. 

 “You don’t have to change your container image.” 

 That’s important to a developer with an existing build pipeline who wants to change how a workload runs without rebuilding the application around a new packaging model. Teams operating standard EC2 instances can also use the sandboxes, Stefaniak says, with more setup to wire up the runtime. 

 The use case extends beyond agents. A SaaS provider might otherwise put customers on separate nodes or clusters to isolate their workloads. Stefaniak sees an opportunity to run multiple tenants on the same node while keeping their workloads isolated. That could mean fewer clusters to look after, a benefit that anyone who has spent an afternoon coordinating upgrades can appreciate. 

 Decide what can leave the sandbox 

 Stefaniak distinguishes between isolated and confidential modes. In confidential mode, he says, the parent instance can’t inspect what’s inside the sandbox. Attestation also opens up a distribution option for a software vendor or model provider. It can ship encrypted code or model artifacts to a customer and use policy to control where they can be decrypted and run. 

 “Isolation is one piece of the puzzle when it comes to running agents.” 

 A workload with no need for network access can run in a confidential sandbox configured without a network interface. An agent that needs to call a model or query a service raises a different set of questions. 

 “Isolation is one piece of the puzzle when it comes to running agents,” Stefaniak said. 

 Stefaniak identifies workload identity and egress controls as two other pieces. Teams need to decide what identity an agent uses and which destinations it can reach. He describes customers who want model calls to go through an approved gateway, where they can apply governance policies and track spending. AWS is exploring how to enforce that path, including a possible role for Envoy . 

 “I think the tipping point is close.” 

 The interview also gets into what AWS contributed to Linux and containerd and why the company wants Nitro Sandboxes to work with emerging open source orchestration projects. 

 Stefaniak says the integration with Agent Sandbox is already working and describes the Agent Substrate work as an early proof of concept. “I think the tipping point is close,” Stefaniak said. 

 Watch the full interview on The New Stack’s YouTube channel for Stefaniak’s take on what would make teams comfortable moving agents into production, how SaaS developers might use the same isolation, and why some of the hardest work starts when an agent needs to reach outside its sandbox. 
 The post AWS Nitro Sandboxes give AI agents a place to run appeared first on The New Stack .
