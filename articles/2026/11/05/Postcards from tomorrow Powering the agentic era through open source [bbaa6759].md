---
id: "bbaa6759fe988a0a"
title: "Postcards from tomorrow: Powering the agentic era through open source"
url: "https://thenewstack.io/kubernetes-ai-learning-loop"
link: "https://thenewstack.io/kubernetes-ai-learning-loop"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T16:00:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Lachlan Evenson"]
language: "en"
summary: "When organizations across the industry first adopted generative AI , most consumed it through a hosted API, but open-weight models are changing that. Models like the Qwen family and GLM-5 are published on model registries like Hugging Face, many under Apache 2.0 licensing, and load directly into open-source serving engines like vLLM and SGLang . \n\n “For a growing set of workloads, that gap is…"
tags: ["AI Agents", "AI Infrastructure", "Kubecon Cloudnativecon NA 2026", "Kubernetes", "sponsor-cncf", "sponsored-post-contributed"]
orgs: ["Hugging Face", "Microsoft", "Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "jobs & society"]
content_source: "summary"
word_count: 1390
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Postcards from tomorrow: Powering the agentic era through open source

The New Stack · Lachlan Evenson · 2026-11-05

When organizations across the industry first adopted generative AI , most consumed it through a hosted API, but open-weight models are changing that. Models like the Qwen family and GLM-5 are published on model registries like Hugging Face, many under Apache 2.0 licensing, and load directly into open-source serving engines like vLLM and SGLang . 

 “For a growing set of workloads, that gap is small enough that the model is no longer the main constraint.” 

 Closed models pulled further ahead in 2025, but not by much. The Stanford AI Index 2026 put the top closed model’s lead over the top open model on the Arena leaderboard at 3.3% as of March 2026. For a growing set of workloads, that gap is small enough that the model is no longer the main constraint. 

 KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12. Register now ! 

 Serving a downloaded model is the easy part; the value comes from changing it: fine-tuning on your own data or applying reinforcement learning (RL) against your own tasks, then putting the improved version back into service. That learning loop is where most of the cost and infrastructure complexity sits. 

 Consider an internal coding agent that a platform team builds to fix failing CI builds that runs on an open-weight model pulled from Hugging Face. When a build fails, the agent clones the repository into a sandbox, reads the logs, writes a patch, and runs the tests. Every attempt produces a trajectory, the record of a single run, with a clean reward signal, because the tests either pass or they don’t. 

 Those trajectories feed the learning loop. On a schedule, the team fine-tunes the model on successful fixes or runs an RL job against the reward, then evaluates the new checkpoint and rolls it out behind the existing endpoint. Over time, the model learns how the team’s codebase breaks and how it gets fixed. That one workflow combines three workload types, and each stresses a platform differently. 

 Where a learning loop gets hard 

 Three workloads, three platforms?   Inference needs long-running replicas that scale with traffic and start quickly. Fine-tuning and RL jobs are close to the opposite: gang-scheduled across GPUs and run to completion. Agents need short-lived execution environments that spin up fast. Teams that stand up separate infrastructure for each end up with idle GPUs in one place and queued jobs in another, and every handoff adds cost. 

 Untrusted code at high density Agents execute code the model wrote seconds earlier, and a shared kernel is a thin boundary. The CI agent from our example also spends most of its life waiting on a model response or a test run. Giving each agent a dedicated, always-on pod makes isolation expensive, so teams trade security for density. 

 Scattered capacity and slow starts Teams add GPUs incrementally, across regions, and sometimes on hardware they already own on-premises. A training job may fit on capacity that exists but sits outside the cluster, and when inference scales out, each new replica has to load tens of gigabytes of weights before it serves a single request. 

 One control plane for the whole loop 

 Rather than building a separate platform for each stage, treat the learning loop as a standard cloud native systems problem. Kubernetes already reconciles declared state and schedules work. The job is now to extend those primitives to models, agents, and accelerators, giving the pattern three layers on a shared control plane. 

 Model layer: serving and tuning as declarative workloads 

 The model layer covers serving, fine-tuning, and evaluation. Several open-source projects work here, including KServe , llm-d and the Kubernetes AI Toolchain Operator (KAITO) . KAITO represents a model and its GPU requirements as a custom resource and reconciles that state. A model update becomes a change to desired state, not a script someone has to run. 

 On the training side, Kueue handles queueing and gang scheduling while KubeRay orchestrates distributed jobs. If you’d rather not assemble those pieces yourself, TauGrid , which Microsoft open-sourced in August 2026, packages them with GPU health monitoring and observability into a single Helm install. 

 Model streaming helps with cold starts. The Run:ai Model Streamer , supported in vLLM, reads tensors from object storage straight into GPU memory rather than staging them on local disk first, so new replicas start serving sooner. 

 Agent execution layer: isolation without paying for idle time 

 The agent execution layer runs the code agents produce, and the projects here sit at different levels. Kata Containers and gVisor isolate a workload from the host kernel. agent-sandbox , from Kubernetes SIGs, manages sandboxed agents as Kubernetes resources, and Agent Substrate builds on it to pack many agents onto fewer workers. Hyperlight , a CNCF Sandbox project donated by Microsoft in 2024, works at a finer grain, inside the application itself. 

 Kata runs each pod in a lightweight VM with its own guest kernel, and the pod API stays the same. A workload opts in through its runtime class and nothing else about its deployment changes, which is why agent-sandbox can use Kata as a backend for sandboxed agents. Kata supports several virtual machine monitors, including Cloud Hypervisor, which Agent Substrate uses for its microVM class. 

 Agent Substrate addresses density by mapping a large set of stateful agents onto a smaller pool of pre-warmed workers, assigning work in real time, and suspending idle agents to object storage so they can be restored on demand. It isolates with gVisor by default, with an optional microVM class built on Kata and Cloud Hypervisor. Agents stay isolated, and you stop paying for them while they wait. 

 Hyperlight embeds a micro-VM manager in an application and runs guest code with no kernel or operating system inside the VM. VMs start in one to two milliseconds, and it can snapshot and restore VM memory. 

 Compute layer: bringing capacity to the cluster 

 The compute layer deals with fragmented GPU capacity. Karpenter and the Cluster Autoscaler add nodes as demand grows, and KubeFleet places work across clusters. Dynamic Resource Allocation (DRA) , stable since Kubernetes 1.34, lets workloads request accelerators by their attributes rather than as an opaque device count. 

 Fragmented capacity can also be addressed from the other direction: bringing existing compute into a cluster’s scheduling domain. This allows workloads to use capacity across regions, on-premises environments, or edge locations through standard Kubernetes scheduling and policy. Open-source projects such as Flex nodes for AKS are exploring this model by connecting user-managed VMs and bare-metal hosts to an existing cluster as worker nodes. 

 The loop, end to end 

 Back to our CI agent example: when a build fails, Agent Substrate restores the agent from a snapshot onto a warm, sandboxed worker. The agent works the problem and is suspended again when it finishes, so it holds no compute between failures. 

 Its model calls go to an endpoint served from the model layer. Successful trajectories accumulate in storage, and on a schedule a Kueue-managed fine-tuning job lands on whatever GPU capacity is free, including nodes outside the cluster’s home region. The new checkpoint is evaluated and rolled out by updating the model’s desired state. 

 “With no second (or third) platform to stand up and no handoffs between them, the loop stays cheap enough to run repeatedly.” 

 Every stage runs on one control plane, under the same identity and policy, and shows up in the same observability tools. With no second (or third) platform to stand up and no handoffs between them, the loop stays cheap enough to run repeatedly. 

 Where to start 

 Open-weight models made it possible to own the model. The open-source ecosystem around them is what makes it practical to own the whole loop, from serving through retraining, without depending on a single provider for either.  

 That said, much of this stack is still young. Agent Substrate , gVisor , KAITO , and Hyperlight are CNCF Sandbox projects, but Agent Substrate and Hyperlight remain pre-1.0. Their direction depends heavily on the people running them in production. 

 If you’re building a learning loop of your own, start with the layer where friction is highest today and run that project against your own workload – all these communities’ welcome issues, use cases, and contributions. 

 The post Postcards from tomorrow: Powering the agentic era through open source appeared first on The New Stack .
