---
id: "c93d375c0b743342"
title: "Please don’t give the robot my SSH keys: How to keep AI out of trouble"
url: "https://thenewstack.io/teleport-agent-delegated-identity"
link: "https://thenewstack.io/teleport-agent-delegated-identity"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T21:57:58Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "Say a developer asks an AI agent to find out why a Kubernetes pod keeps crashing. The agent needs logs. Depending on what it finds, it may need to look at another service. The developer has credentials that can get it there, but handing those over would give the agent everything those credentials can reach. By the time the pod is healthy again, someone may have a second incident to investigate.…"
tags: ["AI Agents", "Kubernetes", "Security", "Podcast", "sponsor-teleport", "Sponsored", "sponsored-podcast", "Video"]
orgs: []
topics: ["agents & coding", "policy & regulation", "models & research", "robotics & autonomy"]
content_source: "summary"
word_count: 646
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Please don’t give the robot my SSH keys: How to keep AI out of trouble

The New Stack · Chris J. Preimesberger · 2026-11-24

Say a developer asks an AI agent to find out why a Kubernetes pod keeps crashing. The agent needs logs. Depending on what it finds, it may need to look at another service. The developer has credentials that can get it there, but handing those over would give the agent everything those credentials can reach. By the time the pod is healthy again, someone may have a second incident to investigate. 

 In a conversation with The New Stack’s Frederic Lardinois at KubeCon + CloudNativeCon this month in Salt Lake City, Teleport field CTO Boris Kurktchiev uses that debugging scenario to explain delegated identity. The agent starts without access and requests what it needs for the job. The audit trail links the person who requested the work to the actions the agent took. A developer can send the agent to investigate without lending it their keys. 

 “The agent had access on behalf of Boris,” Kurktchiev said. 

 One access policy across the stack 

 Teleport’s core platform is designed to give teams a common way to define access across systems that otherwise have their own controls. For developers, that matters when a single investigation takes them from Kubernetes to a database or when a CI/CD pipeline needs access to infrastructure. Kurktchiev describes applying the same policy model to people, automated workloads and agents, with permissions scoped to resources such as a particular pod or database table. 

 The appeal becomes clearer when one developer launches several agents at once. Each can generate access requests, and a human who has to approve every routine step will eventually run out of patience. As Kurktchiev and Lardinois discuss, the convenience of turning off the prompts starts to look different when the work touches production. The practical question is which decisions a team can encode in policy and which still need a person’s attention. 

 What happens inside the sandbox 

 Teleport announced Beams at KubeCon, and Kurktchiev describes it as an agent runtime that combines sandboxing, identity, access, and observability and auditing. Isolation gives an agent a place to run. Teams still have to consider what credentials are available in that environment and what those credentials can reach. 

 “So just having a sandbox is not enough.” 

 “So just having a sandbox is not enough,” Kurktchiev told TNS. 

 With Beams, Kurktchiev says, an agent starts without access. A team can define which resources it should be able to request, for how long, and what an acceptable execution path looks like. 

 “The default is always zero,” Kurktchiev said. 

 That approach lets developers distinguish between the plan an agent proposes and the permissions it actually gets. If execution diverges from the plan, Kurktchiev describes options to alert someone, stop the run, or fork it to explore an alternate path. That last option matters because a detour can turn up something worth pursuing. The token bill, the two men joke, is a separate discussion. 

 “The default is always zero.” 

 The interview also looks beyond Teleport. Kurktchiev points to SPIFFE as a foundation for machine identity across systems and considers what agents might need from it as they work across organizational boundaries. He also sees work ahead for the Model Context Protocol (MCP) , which gives agents a way to connect to tools and data. Connecting an agent to a service opens up a second set of questions about what it can do there and how a team will account for it afterward. 

 Watch the full interview on The New Stack ’s YouTube channel to hear Kurktchiev and Lardinois discuss what it takes to move an agent from a developer’s sandbox into production, how to keep approvals manageable when agents multiply, and what an audit trail needs to show when an investigation takes an unexpected turn. 
 The post Please don’t give the robot my SSH keys: How to keep AI out of trouble appeared first on The New Stack .
