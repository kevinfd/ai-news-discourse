---
id: "e3bfe384642224fc"
title: "When “isolated” doesn’t mean isolated: How to sandbox AI agents"
url: "https://thenewstack.io/how-to-sandbox-agents"
link: "https://thenewstack.io/how-to-sandbox-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T13:00:00Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Michael Levan"]
language: "en"
summary: "Separation of workloads before AI wasn’t easy, but it was far more straightforward. Servers sat in data centers, VLANs segregated packets, firewall rules managed ingress/egress, and physical cables separated packets to and from their destinations. \n\n Now, flip on an agent, and it has access to almost everything by default. \n\n Enterprises cannot operate with that default, and in this article,…"
tags: ["AI Agents", "Containers", "Security", "sponsor-cncf", "sponsored-post-contributed"]
orgs: ["Anthropic", "OpenAI", "Hugging Face"]
topics: ["agents & coding", "chips & infrastructure", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 1246
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# When “isolated” doesn’t mean isolated: How to sandbox AI agents

The New Stack · Michael Levan · 2026-10-27

When “isolated” doesn’t mean isolated: How to sandbox AI agents
Separation of workloads before AI wasn’t easy, but it was far more straightforward. Servers sat in data centers, VLANs segregated packets, firewall rules managed ingress/egress, and physical cables separated packets to and from their destinations.
Now, flip on an agent, and it has access to almost everything by default.
Enterprises cannot operate with that default, and in this article, you’ll learn how to implement true sandboxing at every layer that matters.
Why aren’t containers enough to sandbox AI agents?
When you run a container (think Docker), it’s a lightweight package that runs as an isolated process. But that isolation has limits. Containers share the host kernel, and those on Docker’s default bridge can communicate with one another. A container cannot directly access host files by default, but a writable bind mount can let it modify or delete the host files exposed through that mount.
If you rely on a container alone for agent isolation, you may leave important boundaries unprotected. Thinking of containers as locked down by default is a major security risk. When running workloads in Kubernetes, you have tools like NetworkPolicy, service mesh for secure service communication, and SecurityContext to ensure containers run in a governed way.
KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12. Register now!
That’s why having default security out of the box, easily turned on, and policy enforcement built into your AI sandboxing solution is key to enabling all teams. Without it, every organization risks thinking security exists, only to face a harsh reality.
So, regardless of what agentic workloads we’re running, the question we must answer is: “What makes up a true sandbox?”
What’s a true agent sandbox?
OpenAI reported that agents in restricted research sandboxes found a route to the internet through its internal Artifactory service; an agent later found and shared publicly exposed Hugging Face credentials. Anthropic described a different failure: in three cybersecurity evaluations, Claude reached real systems because a third-party test environment had internet access despite instructions that it did not. These cases show that sandboxing depends on the network and service boundaries around an agent, not just the runtime that contains it.
“These cases show that sandboxing depends on the network and service boundaries around an agent, not just the runtime that contains it.”
Agent sandboxing by default can sound “buzzword-ish”, but there is merit in implementing it at all of the boundaries that count for you and your organization. That means sandboxing will look different depending on where, and ultimately how, you put it into production. For example, sandboxing an agent with access to government- or healthcare-related data could mean locking down ingress/egress to public, consumer-based LLMs and allowing the agent to interact only with dedicated models for specific tasks on the data it must use. On the flipside, a software engineer or architect coding up a new integration may have more flexibility in the LLMs, MCP Server tools, and agent skills that agents they’re using can interact with and ultimately where those Agents can run (e.g. on your laptop/desktop vs an isolated server running an Agent runtime).
That’s where the fun, ironic consulting answer of “it depends” comes in, because it really does. As with everything security-related, there is a spectrum of what you can implement ranging from “cover the key use cases” to “this is Area 51”, and that plethora of range needs to be thought about and ultimately implemented in the best and most efficient way for your organization.
So, here’s the answer to the underlying question from this section’s header: true agent sandboxing means clarifying, understanding, and implementing what your agents should and shouldn’t be able to interact with. This includes other agents, LLMs, web searches, MCP servers, tools, and APIs.
“True agent sandboxing means clarifying, understanding, and implementing what your agents should and shouldn’t be able to interact with.”
In the next section, you’ll learn the key differentiating factors that make up a true sandbox. With that knowledge, you’ll be able to draw a proper conclusion about what level of agent sandboxing an organization should implement.
The differentiating factors for your agent sandbox
There are four key areas that you must keep in mind when implementing agentic workloads:
- Software vs. hardware-level isolation (think user space vs. at the chip level)
- Where the agents run (is it running on an isolated runtime or your workstation)
- What the agents have access to (ingress/egress/web search/models/tools/APIs)
- Secure code execution for AI agents (what commands/code/scripts can an agent run)
When thinking about software-level isolation, think container-level isolation. Now, after the first section of this blog post, ” Why aren’t containers enough to sandbox AI agents?, you may be thinking to yourself, “No way I’m going to run Agents in containers; it’s not isolated at all.” That’s true, but only by default/out of the box. You can secure and govern software-level isolation; it’s just a matter of what policies you put in place to ensure it. It runs inside a Linux kernel using Linux Namespaces/the user space for boundaries. Hardware isolation, on the other hand, is running a guest VM (think microVM/Firecracker) at the chip/CPU level. That means it runs a dedicated, standalone guest VM, and all processes run inside that guest VM.
The next two pieces of the puzzle are where agents run, and that brings us back to the previous section. An agent can run on your laptop/desktop, in a container, or within an isolated guest VM at the hardware level. Regardless of which option you choose, you still need proper guardrails, policy enforcement, and access to LLMs and tools, but the segregation may occur elsewhere. In any case, outbound and inbound connectivity (to/from the agent) occurs at your “line of communication”, which is an AI gateway. That’s typically where you set up policies, guardrails, tool isolation, agent access, and LLM connectivity.
The final step is “how” the agents run. For many use cases, agents run on a laptop/desktop. Still, in an organization, most agentic runtimes run on a server/platform like Kubernetes (which also covers “where” the Agents run). For example, an agent you may interact with on an eCommerce website isn’t running on someone’s laptop; it runs on a hosted runtime.
When working with a hardened solution, the ability to ensure agents run within your harness of choice and that it implements a true agent sandbox environment under the hood should be out of the box, and this is an important decision factor.
kind: Harness
metadata:
  name: YOUR_HARNESS_NAME
  namespace: YOUR_NAMESPACE
spec:
  kagent: {}
  workload:
    image: YOUR_AGENTIC_WORKLOAD_IMAGE
  substrate:
    workerPoolRef:
      name: kagent-default
    snapshotPolicy:
      location: ACTOR_SNAPSHOT_STORAGE_LOCATION
  allowedAgentTemplates:
    selector:
      matchLabels:
        kagent.dev/harness: kagent
kind: AgentTemplate
metadata:
  name: assistant
  namespace: kagent
  labels:
    kagent.dev/harness: kagent
spec:
  modelConfig:
    name: default-model-config
  description: A substrate-backed assistant used to verify this main build.
  systemPrompt: You are a helpful assistant running on agentic workloads.
Choosing the right agentic runtime, and therefore framework, lets you specify which AI gateway your agent traffic goes through from the sandbox, which harness you use, your underlying software- or hardware-level isolation, governance around agentic workloads, and where agents store memory/context.
Closing thoughts
Sandboxing agents will always come down to a keen understanding of what those AI agents need to do, and that’s the hardest part. Locking down an agent and implementing governance, security, and policy enforcement should be easy with the right tooling and platforms. The “what” is crucial. What exactly are you locking down and why?
