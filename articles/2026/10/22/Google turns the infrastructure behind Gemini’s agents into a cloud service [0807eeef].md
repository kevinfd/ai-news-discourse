---
id: "0807eeef42b0817b"
title: "Google turns the infrastructure behind Gemini’s agents into a cloud service"
url: "https://thenewstack.io/google-agent-compute-engine"
link: "https://thenewstack.io/google-agent-compute-engine"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T13:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Google will soon make the infrastructure that powers its Gemini agents available to Google Cloud users in preview. \n\n Announced on Thursday at the Linux Foundation’s AGNTCon+MCPCon in San Jose, Agent Compute Engine will become available in preview to Google Cloud users later this year. It will provide every AI agent with a hardware-isolated microVM that combines the speed of containers with the…"
tags: ["AI", "AI Agents", "AI Infrastructure"]
orgs: ["Google", "Amazon"]
topics: ["agents & coding", "chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 1183
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google turns the infrastructure behind Gemini’s agents into a cloud service

The New Stack · Frederic Lardinois · 2026-10-22

Google turns the infrastructure behind Gemini’s agents into a cloud service
Google will soon make the infrastructure that powers its Gemini agents available to Google Cloud users in preview.
Announced on Thursday at the Linux Foundation’s AGNTCon+MCPCon in San Jose, Agent Compute Engine will become available in preview to Google Cloud users later this year. It will provide every AI agent with a hardware-isolated microVM that combines the speed of containers with the security of a sandbox.
Who else offers agent sandboxes?
The idea of agent sandboxes is anything but new, of course. Startups like E2B and Daytona offer them to developers (and support them on any cloud), as does AWS with Bedrock AgentCore.
E2B runs each sandbox in a Firecracker microVM, the open source virtualization technology AWS originally built for Lambda. It can pause a sandbox with its memory and filesystem intact and resume it in about a second. Daytona started out with containers but added microVM sandboxes in July. Those can pause a full machine or fork a running one into identical copies.
AgentCore also gives every agent session its own microVM. AWS doesn’t charge for CPU while an agent waits on a model or tool call, though memory keeps billing until the runtime reclaims it. Those sessions top out at eight hours. In August, AWS added EC2-based runtime instances that can keep shared sessions alive for up to 14 days.
It’s worth noting that Google itself isn’t new to this either. GKE already offers a managed version of Agent Sandbox, the open source Kubernetes project Google launched last November. The company also sells code-execution and computer-use sandboxes through its Gemini Enterprise Agent Platform.
Agent Compute Engine, on the other hand, started out as internal infrastructure for Gemini, Antigravity, and Google’s own model training pipelines.
Google’s take
Few companies — if any — run as many agentic workloads as Google, be that for its own internal use or its customers. According to the company, agentic workloads have quickly become one of the fastest-growing consumers of compute and storage across its fleet.
At this scale, the infrastructure services that power all of these autonomous agents don’t just need to be efficient and able to scale, but maybe more than anything, they need to be secure. Google, like some of its competitors, quickly realized that it needed to build a new purpose-built compute service to power all of these agents, similar to how it needed to build Borg, which later inspired Kubernetes, to manage compute in its early data centers.
As Rohit Jnagal and Ramanathan Venkatapathy, both distinguished engineers at Google, note in a technical deep dive, traditional VMs provide developers with a lot of control and flexibility, but at the cost of speed when it comes to booting, suspending, and resuming a machine. Given how fast agents start and shut down, that’s not an option.
Containers solve some of this, they note, “but there are multiple examples like coding agents and developer assistants that need complete isolation as well as kernel- and root-level control of the agentic environment.”
With Agent Compute Engine, Jnagal and Venkatapathy write, the team went back to first principles to build “a unified, agent compute platform for Google” (and now its customers).
A persistent computer for every agent
At its core, it basically gives every agent a persistent, sandboxed computer to work with. That allows the agents to work with shell scripts, use a headless browser, and write code (with root permissions to that machine) in agent loops that could run for weeks.
But the team also built it for large-scale use cases like the eval loops that frontier labs use to test their models, AI benchmarking, and reinforcement learning.
In addition, the team also designed Agent Compute Engine to run sandboxed backends for Google’s own services.
Jnagal and Venkatapathy also note that agents spend most of their time waiting on the model or the user. So once an agent finishes a tool call, the host checkpoints its microVM, which then uses no active resources until the next call comes in.
Nothing to steal inside the sandbox
The key feature here, besides speed, is to be able to trust that the agents can’t break out of their sandboxes. We’ve seen what happens when they do, after all.
Each agent session runs inside a single-tenant, memory-safe microVM. Those environments hold no secrets in memory or on the disk, and their only identity is a short-lived, session-scoped one delivered through a single per-VM local listener. All traffic is end-to-end encrypted in transit, and snapshots and disks are encrypted at rest.
The microVMs don’t get a standard network interface, either. All traffic runs through a proxy outside the sandbox, and when an agent needs to reach a service like Google Drive, Google’s Agent Gateway checks the user’s delegation and the sandbox’s identity before adding the actual credential, outside the sandbox.
The underlying host is basically a stateless appliance with a read-only filesystem, with the hardware and firmware cryptographically verified at each boot.
All of this is backed by Google’s own Titan and Titanium IPU security platform. The microVMs themselves run on Cloud Hypervisor, an open source virtual machine monitor, and each gets its own guest kernel and root access.
Jnagal and Venkatapathy use the example of an enterprise agent that manages a user’s inbox and reads an email with hidden instructions to find any API keys on the machine and send them to an outside address. Most of the time, they note, the model will ignore that, but not always.
“We started from one rule: Assume an attacker controls everything inside the sandbox, and make sure they find nothing there to use,” the team writes.
Agent Substrate brings the same idea to Kubernetes
But not every team will want to have its agents run in a managed Google service. For them, Google also offers Agent Substrate, an open source runtime for the Google Kubernetes Engine (GKE) that it first announced in May.
Substrate builds on Agent Sandbox, Google’s Kubernetes project, and adds a lightweight control plane that Google says can handle millions of short-lived tool calls that would swamp Kubernetes.
Similar to Agent Compute Engine, Substrate snapshots an idle agent’s memory and returns the machine to the pool until the agent gets more work.
Google says that means up to 10 times the density of traditional compute. In a 200,000-agent benchmark, Substrate handled 500 activations per second, with agents suspending and resuming in under half a second, the company says.
Teams can isolate each sandbox with a microVM or gVisor, and every agent gets its own cryptographic identity. As with Agent Compute Engine, egress proxies attach credentials outside the sandbox. Substrate runs on any Kubernetes cluster, and Google says it works with any harness, including Claude Code, OpenClaw, and Nous Research’s Hermes.
“We built Hermes Enterprise to enable customers to deploy into their existing infrastructure, while handling per-agent isolation and extensible access control,” Hervé Bizira, Nous Research’s chief business officer, notes in the announcement. “Agent Substrate addresses both at the platform layer in a way that also preserves valuable compute resources.”
