---
id: "def148925dadcfbe"
title: "AI agents turn one request into about 20. Kubernetes is evolving to handle it."
url: "https://thenewstack.io/kagent-kubernetes-ai-agents"
link: "https://thenewstack.io/kagent-kubernetes-ai-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-16T18:37:03Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Bill Doerrfeld"]
language: "en"
summary: "Welcome to another edition of Road to KubeCon , where we’re tracking interesting movements in the cloud-native and Kubernetes ecosystem as we count down the days to KubeCon + CloudNativeCon NA 2026 , to be held in Salt Lake City, Utah, November 9-12. \n\n In this edition, we get formal, requesting audiences with some key cloud-native players. We also cover new SUSE validation for HPE Morpheus…"
tags: ["AI Agents", "Kubecon Cloudnativecon NA 2026", "Platform Engineering", "Road to KubeCon", "sponsor-hpe", "Sponsored", "sponsored-post"]
orgs: ["OpenAI", "Anthropic", "Google", "Microsoft"]
topics: ["agents & coding", "chips & infrastructure", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 1304
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI agents turn one request into about 20. Kubernetes is evolving to handle it.

The New Stack · Bill Doerrfeld · 2026-10-16

AI agents turn one request into about 20. Kubernetes is evolving to handle it.
Welcome to another edition of Road to KubeCon, where we’re tracking interesting movements in the cloud-native and Kubernetes ecosystem as we count down the days to KubeCon + CloudNativeCon NA 2026, to be held in Salt Lake City, Utah, November 9-12.
In this edition, we get formal, requesting audiences with some key cloud-native players. We also cover new SUSE validation for HPE Morpheus Software and what to expect at Platform Engineering Day this year.
Plus, we check out a new(ish) CNCF sandbox project for running agents as Kubernetes resources, a look at assigning Kubernetes compliance ownership, and a story of when to not use Kubernetes in practice.
HPE Morpheus Software adds SUSE validation
If you’re an HVM hypervisor user also using SUSE, you’re in luck: HPE Morpheus Software has now officially gained SUSE certification, meaning the hypervisor can now support SUSE Linux Enterprise Server (SLES) 16.
Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon. HPE Software helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.
Why does SUSE validation matter? According to HPE’s announcement, “Operating system validation plays a critical role in reducing deployment risk and ensuring predictable outcomes in production environments.” The validation signals maturity and gives operators more confidence.
The addition arrives at a time when some enterprises are juggling hybrid cloud estates and looking for a unified way to manage their virtual machine infrastructure.
Platform Engineering Day goes agentic
Since 2024, a platform engineering event has run alongside KubeCon + CloudNativeCon events, and this year is no different. Platform Engineering Day will be a co-located event on Monday, November 9, at KubeCon + CloudNativeCon NA 2026.
As Paula Kennedy, Stacey Potter, and Ramiro Berrelleza share on the CNCF blog, “Since its inception, the goal has remained simple: create a space where platform engineers and practitioners can learn from one another.” Just as important as sharing wins is sharing anti-patterns and explaining why decisions are made, they add.
Based on the published agenda, attendees should expect a blend of end-user stories, keynotes, lightning talks, and panels, with a strong focus on agents as both producers and consumers of internal developer platforms.
Agents and Kubernetes are formally introduced
Luca Berton, AI advisor and architect, recently kicked off an interesting series, Udienza. “Udienza” is Italian for an audience with someone you don’t usually get to meet. Cambridge defines it as “a formal interview with someone important.”
So far, Berton’s series has stuck to that definition, featuring short chats with leaders in cloud-native and AI infrastructure, including Luca Galante, Chris Aniszczyk, Kat Cosgrove, Manik Surtani, and others.
His recent interview features CNCF directors Bob Killen and Daniel Krook. A key takeaway is that Kubernetes is becoming the operating system for AI, serving as the default base layer for a wave of newer projects that solve specific problems on top of it.
They also acknowledged the new traffic stresses of agents, noting that a single human request can trigger about 20 agent requests. And agents expect sub-200-millisecond responses, while a new Kubernetes pod is only guaranteed to spin up in about a second.
To close that gap, they highlighted emerging projects across the stack, like llm-d, for distributed LLM inference, and Agent Substrate, a runtime for large-scale agent deployments.
What no one wants to own: Kubernetes compliance
“Security can write the policy. Security cannot merge the Helm chart.”
That’s the message from Matteo Bisi of Reevo in a CNCF blog post published last Friday. He’s hitting on a common issue that many organizations don’t have a clear answer to: who owns compliance? Specifically, who owns ensuring Kubernetes platforms meet the requirements of EU regulations like NIS2 and DORA?
As the opening pull quote suggests, Bisi argues cloud-native operators have a role to play. He advocates creating “traceability chains” that let risk, legal, and security teams define scope, control requirements, and required evidence, then hand off specific artifacts, sprint items, and recurring operations to platform and application teams.
By aligning on who does what, compliance becomes less of an unresolved bottleneck and more of a plan of attack for these frameworks, with a repeatable handoff for future ones, too.
As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor HPE helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.
Spinning up agents on Kubernetes gets boring
Getting agents running on Kubernetes is starting to feel like just another part of the infrastructure. kagent is an interesting CNCF sandbox project that runs AI agents as Kubernetes custom resources. A new tutorial shows just how routine that has become, using kagent to build an agent that builds other agents.
“You write an Agent with a system prompt, a model, and a list of tools. You apply it, and the controller turns it into a running pod that speaks A2A,” writes Antonio Berben from Solo.io and Felipe Vicens from Telefónica on the CNCF blog in a post published Monday.
The walkthrough runs on a laptop with a local model through Ollama (kagent also supports hosted providers like OpenAI, Anthropic, Azure OpenAI, and Gemini), though the authors found smaller models struggled to produce valid manifests. The builder is fenced in by an allowlist of three tools, requires human approval before anything is applied, and uses RBAC that lets it write only Agent resources. You can drive it through kagent’s UI or its A2A API.
A story of when not to use Kubernetes
On Tuesday at the Nordic APIs Summit 2026 in Stockholm, Sweden, Faith Sodipe, software developer at Bauer Media Outdoor UK, took the stage with a presentation that might offend some diehard Kubestronauts.
In the talk, You Don’t Need Kubernetes: How We Scaled Our API Layer Without the Infrastructure Theatrics, Sodipe defined infrastructure theater as “building for the appearance of scale rather than the reality of it.” Too often, platform teams build for a scale that’s disproportionate to production reality.
Bauer Media Outdoor UK’s ingestion system processes close to a million events per day, with bursty traffic and variable payload sizes. At that scale, better system design (fixing connection pool exhaustion, a cache stampede, and slow queries) mattered more than heavyweight container orchestration. The team containerized with Docker but skipped Kubernetes altogether.
As Sodipe recaps on LinkedIn, “My message was simple: solve the actual problem, not the problem you assume you have.”
Vendor’s take: AI coding evolves platform engineering
Now that AI coding agents are ubiquitous, is platform engineering less relevant? Cory O’Daniel, one of the early drivers behind OpenTofu, the open-source Terraform alternative, and CEO and co-founder at Massdriver, an internal developer platform (IDP), tells The New Stack that coding agents make platform engineering more important, not less. Yet, the infrastructure surrounding IDPs must evolve.
“The architectural shift I see is from infrastructure as code to infrastructure as data,” says O’Daniel. This doesn’t replace Terraform, OpenTofu, or Git, he says, but involves representing infrastructure as a queryable graph of resources, dependencies, ownership, environments, and policy.
Serving things this way could help agents consume infrastructure information more efficiently. Plus, he says, additional controls are needed more than ever now that anybody can create and ship. “The guardrails are becoming the only control ops has left.”
Follow the Road to KubeCon
Road to KubeCon is an eight-part series presented by HPE. Before you go, explore how HPE Software helps IT teams do more with less complexity.
Road to KubeCon will be here every Friday on The New Stack, until KubeCon. Catch up on the latest releases on the Road to KubeCon archive page.
Bill Doerrfeld, the writer for this series, welcomes community contributions. You can send your PRs, blurbs, hot takes, or cloud-native forecasts through his contact page.
