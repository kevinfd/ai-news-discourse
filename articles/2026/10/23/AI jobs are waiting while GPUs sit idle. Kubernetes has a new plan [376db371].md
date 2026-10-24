---
id: "376db3718401f53e"
title: "AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan."
url: "https://thenewstack.io/kubernetes-agentic-ai-inference"
link: "https://thenewstack.io/kubernetes-agentic-ai-inference"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T19:08:53Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Nick Lucchesi"]
language: "en"
summary: "Welcome to another edition of Road to KubeCon ! We’re tracking movements in the Kubernetes and cloud-native ecosystem as we count down to KubeCon + CloudNativeCon North America 2026 November 9–12 in Salt Lake City. \n\n Half of our column this week focuses on untangling Kubernetes as we add the demands of agentic AI: automating pod-restart troubleshooting, syncing communication between the…"
tags: ["AI Infrastructure", "Kubecon Cloudnativecon NA 2026", "Kubernetes", "Observability", "Road to KubeCon", "sponsor-hpe", "Sponsored", "sponsored-post"]
orgs: ["IBM", "Amazon", "Google", "Tesla", "Oracle", "China"]
topics: ["chips & infrastructure", "agents & coding", "jobs & society", "models & research"]
content_source: "fulltext"
word_count: 1741
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan.

The New Stack · Nick Lucchesi · 2026-10-23

AI jobs are waiting while GPUs sit idle. Kubernetes has a new plan.
Welcome to another edition of Road to KubeCon! We’re tracking movements in the Kubernetes and cloud-native ecosystem as we count down to KubeCon + CloudNativeCon North America 2026 November 9–12 in Salt Lake City.
Half of our column this week focuses on untangling Kubernetes as we add the demands of agentic AI: automating pod-restart troubleshooting, syncing communication between the scheduler and autoscaler, and maturing how we distribute inference across a cloud-native stack.
The other half goes deeper into what we need to look at closely in Kubernetes environments: What context’s missing, what slips through the gaps in metrics, and whether the AI agents you already use are really worth their salt as SREs.
Let’s get into it.
HPE on automating pod restarts in AI development
As more enterprises turn to Kubernetes for large-scale AI and machine learning jobs, they’re hitting a common obstacle: pod restarts. This is something that HPE has noticed as customers utilize its HPE Private Cloud AI (PCAI) to host long-running AI/ML workloads on inherently ephemeral container-based infrastructure like Kubernetes.
Hewlett Packard Enterprise (HPE) is a presenting sponsor of Road to KubeCon. HPE Software helps IT organizations modernize infrastructure, streamline operations, and accelerate AI initiatives across hybrid, multi-vendor environments.
According to HPE system software engineer Guoping Jia, Kubernetes provides some troubleshooting commands out of the box, but it still requires extensive manual investigation. “This operational workflow does not scale effectively in PCAI’s large-cluster environment,” writes Jia on the HPE blog.
His solution involves smarter automation for troubleshooting, using an open-source Kubernetes troubleshooting tool, k8s-pod-restart-info-collector, to automatically gather details and send diagnostic information straight to a Slack channel. It’s one helpful strategy to improve usability for Kubernetes operators.
Will the scheduler and autoscaler unite?
There’s been a lot of talk recently about how Kubernetes is evolving to meet AI’s new demands. This week, AWS senior software development managers Sajjan Gundapuneedi and Neelendra Bhandari weighed in with this blog post on how AI is reshaping Kubernetes autoscaling.
The core problem they highlight is friction between the scheduler, which places pods on existing nodes, and the autoscaler, which adds new ones, when managing GPU accelerators on Kubernetes. Often the two sides aren’t on the same page, leaving pods pending and pricey GPUs sitting idle. Capacity reservations, device topology, and GPU sharing complicate things further.
“A scarce accelerator is only as useful as the agreement between the loop that schedules it and the loop that provisions it.”
“A scarce accelerator is only as useful as the agreement between the loop that schedules it and the loop that provisions it,” the authors write. “Inference is what makes this pressing rather than academic, since bursty serving and agentic workloads have no patience for a cold node.”
To them, solutions are already taking shape: dynamic resource allocation (DRA)-aware autoscalers, workload-aware scheduling, and a companion mechanism, provisioning requests, to bridge the two sides. Still, they expect the autoscaler to grow into “a more scheduler-aware partner.”
Deeper integration is underway, too. A public proposal in the SIG-Autoscaling group sketches APIs that would let the two loops talk directly, so the scheduler could see capacity that could be provisioned, express placement preferences across it, and request it explicitly.
Distributed AI inference grows up with llm-d v1.0 release
On Tuesday, at PyTorch Conference North America, the CNCF sandbox project llm-d reached v1.0. The project now bridges AI application developers in the PyTorch ecosystem and the production cloud-native stack.
Carlos Costa, co-founder and lead maintainer of llm-d, and a distinguished engineer on IBM’s hybrid cloud platform for AI, says the v1.0 release signals maturity.
“This is the moment open source AI serving crosses from experimental projects into dependable infrastructure you can build on,” Costa tells The New Stack. Whereas earlier versions focused on proving state-of-the-art performance, v1.0 is about sustaining that performance in production, he adds.
llm-d has already seen plenty of use at Tesla, AWS, Oracle, Google, and beyond. Costa adds that a recent IBM Research demonstration found that an agent factory exploring quantum error correction hardware ran at 11.5x lower inference cost on open models with llm-d than on an all-proprietary configuration.
“This demonstration shows where llm-d really shines: agentic workloads,” he says, adding that it absorbs bursty agentic traffic and, in IBM’s test, pushed cache reuse to about 98%.
From building models to operating frontier intelligence at scale
For a taste of the type of discussion to expect at KubeCon NA, let’s briefly visit the East. Chris Aniszczyk, CTO at CNCF, set the stage very well at last month’s KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026 in Shanghai, in the talk Operating Frontier Intelligence at Scale with Xiao Zhang.
As he puts it, it’s not just about models anymore. It’s about putting them all to work. “AI is essentially moving from just purely about building the greatest models [to] how do we actually make this run at scale, stitch it all together and run in different types of environments,” says Aniszczyk.
Cloudflare CEO Matthew Prince recently declared that bot traffic, driven by AI agents, has passed human traffic online for the first time. Aniszczyk says that shift is putting tremendous pressure on systems, pointing to recent GitHub outages. As inference becomes the predominant workload, everything shifts.
“It’s the craziest kind of technology change that I’ve seen probably in my career.”
This shift is causing all sorts of side problems, he notes, from building new infrastructure to building more data centers to ensuring enough power is available. “It’s the craziest kind of technology change that I’ve seen probably in my career,” says Aniszczyk.
Still, he’s an optimist, framing it as a fun problem and challenge for the cloud-native community to tackle together.
Promoting your AI agent to the SRE role
Plenty of AI site reliability engineer (SRE) platforms are emerging. But according to Roy Libman, CPO, Radar (Skyhook.io), your next SRE hire might be right under your fingertips: the AI coding agent you already use. The trick is giving it the right context.
“The coding agent your engineers use, whether that’s Claude Code, Codex or Cursor, can already investigate a Kubernetes cluster,” writes Libman on the CNCF blog. “What it usually lacks is context: what’s failing right now, and what changed before it broke.”
In his benchmark of 50 injected faults on a live cluster, Claude Code, given read-only context through MCP tools, diagnosed slightly more accurately than with shell and kubectl access. The bigger difference was speed: with context, it reached a correct diagnosis within two minutes on 86% of faults, versus 60% with a shell.
It’s an interesting sign that context is king for diagnosing complex errors, and that you might not need to shell (pun intended) out for another AI subscription just to triage issues.
Industry take: what goes undetected in Kubernetes
A previous Road to KubeCon asked what’s still missing with OTel and Prometheus. Well, one gap is state that isn’t a time series, like slowlog entries, client lists, and access control list (ACL) changes, shares Kristiyan Ivanov, former engineering manager at Redis, current contributor to Valkey, and founding CTO of BetterDB. “These get lost between scrapes,” he tells The New Stack.
“Metrics count, but they don’t explain.”
Metrics count, but they don’t explain.” According to Ivanov, much goes undetected in Kubernetes because Valkey and Redis keep evidence in in-memory buffers, which Prometheus reduces to lengths and counters. “Kubernetes makes this even worse in several ways,” he says, noting that pod restarts, failovers, and ephemeral pod IPs worsen tracking.
“Almost everything in the ecosystem is an INFO scraper,” he says. “Missing across the board: durable history across restarts and failovers, attribution to a service or ACL user, an audit trail of ACL and config changes, and aggregation across shards.”
Emerging approaches are helping cloud operators see these gaps. He points to improvements in Valkey’s detection capabilities and OpenTelemetry eBPF Instrumentation to enable granular tracing. But eBPF can’t see evictions, ACL denials, or configuration changes, he says. Those require engine-level collection.
As Kubernetes evolves, so do the demands on the teams running it. Presenting sponsor HPE helps teams address that complexity with software spanning virtualization, cloud management, observability, and automation.
Half can’t measure AI agents effectively
Eighty-seven percent of respondents say monitoring AI is a priority, yet over half admit they can’t effectively measure AI quality, like LLM response quality, or control AI costs, found Splunk State of Observability 2026, which surveyed 2,050 ITOps and engineering professionals and was released Oct. 20.
The report also found 83% are concerned about the unintended consequences of AI agents. This tracks with agentic AI’s tendency to take unexpected actions and create bursty traffic patterns, both of which are driving major infrastructure changes.
“Most companies will soon have far more agents at work than people,” said Jeetu Patel, president and chief product officer at Cisco, in the press release. Monitoring AI is also driving more collaboration between observability and security teams, according to 81% of respondents.
More updates from the cloud-native universe
The excitement around cloud native never sleeps. Here are a few more community, project, and vendor updates from the past week or so.
- Congratulations to Anish Bista, the first Golden Kubestronaut from Nepal!
- Kubernetes v1.38.0 is targeted for release on Wednesday, December 16.
- Per the release schedule, Kubernetes 1.34 hits end of life October 27.
- Fairwinds shares lessons from running n8n in production on Amazon EKS.
- Broadcom’s AAI v26 adds cost tracking and Kubernetes support; see EMA’s impact brief.
- Splunk now lets teams remotely configure OpenTelemetry Collectors on Kubernetes.
- New Relic shipped v4.8.2 of its Kubernetes integration with dependency updates.
One more stop on the Road to KubeCon
Road to KubeCon is an eight-part series presented by HPE. Before you go, explore how HPE Software helps IT teams do more with less complexity.
This series is almost over — only one edition remains.
We’ll be here next week to round things off with a special sign-off for Road to KubeCon. In the meantime, you can catch up on previous editions in the Road to KubeCon archive.
Bill Doerrfeld, the writer of this series, is open to community pitches. Feel free to share interesting takes, new releases, or tips on the best dive bar in Salt Lake City.
He accepts direct messages on LinkedIn, or you can reach him through his personal contact page.
