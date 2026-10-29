---
id: "b5706039ca56947b"
title: "The 5 essential layers of AI agent sandboxing on Kubernetes"
url: "https://thenewstack.io/ai-agent-sandboxing-kubernetes"
link: "https://thenewstack.io/ai-agent-sandboxing-kubernetes"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T12:00:00Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Mickey Boxell"]
language: "en"
summary: "An AI agent given autonomy to run code will inevitably run code no human has reviewed. It may install model-selected packages, run scripts generated moments earlier, and iterate until a developer’s test passes; that risk is limited to a laptop. For a company, it can extend beyond the agent’s workload to any workload deployed on shared Kubernetes infrastructure . Cluster configurations can limit…"
tags: ["AI Agents", "Kubernetes", "Security", "sponsor-cncf", "sponsored-post-contributed"]
orgs: ["Oracle"]
topics: ["agents & coding", "models & research", "safety & ethics", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1185
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The 5 essential layers of AI agent sandboxing on Kubernetes

The New Stack · Mickey Boxell · 2026-10-29

The 5 essential layers of AI agent sandboxing on Kubernetes
An AI agent given autonomy to run code will inevitably run code no human has reviewed. It may install model-selected packages, run scripts generated moments earlier, and iterate until a developer’s test passes; that risk is limited to a laptop. For a company, it can extend beyond the agent’s workload to any workload deployed on shared Kubernetes infrastructure. Cluster configurations can limit a container’s system calls, but an allowed call that reaches a kernel vulnerability can still expose the underlying node.
As agents proliferate, this gap has shifted workload isolation from a niche hardening requirement to a baseline need for platforms that run agents. This is a challenge our users at Oracle Cloud Infrastructure (OCI) have asked us to help solve.
KubeCon + CloudNativeCon takes place in Salt Lake City, Utah, from November 9 to 12. Register now.
As expected in the cloud-native space, the community has developed solutions. These solutions exist across five layers: from the pod request, down to the node, and back up to the agent’s session. Platform teams can assemble the stack rather than reinvent it, while native provider support simplifies configuration and maintenance. Managed Kubernetes services offer sandboxed pods this way, but runtimes isolate agentic workloads differently.
The following sections cover the options and tradeoffs before showing how the components fit together.
1. The isolation layer: choosing your risk boundary
First choose between minimal isolation, a restricted kernel interface, and full VM isolation. Each option comes with trade-offs between security and performance.
runc offers the greatest performance through a shared host kernel. Seccomp-based filtering restricts the system calls a process can make.
gVisor suits use cases where a restricted kernel interface is sufficient. Its user-space application kernel handles system calls instead of booting a guest Linux kernel, so the workload reaches the host through a small interface. gVisor implements a subset of Linux, so it starts quickly and packs densely. Applications must work with the interfaces Sentry implements, which can constrain agent behavior.
“A separate guest kernel with hardware virtualization avoids surprises where system-call emulation falls short and unexpectedly handcuffs agents.”
Kata Containers suit use cases requiring full VM isolation. Each pod runs in a lightweight VM with its own guest kernel, at the cost of a VM boot and guest-kernel memory. Nearly anything that runs in a container runs in Kata. Agents exercise package managers, compilers, nested builds, and headless browsers. For that code, a separate guest kernel with hardware virtualization avoids surprises where system-call emulation falls short and unexpectedly handcuffs agents.
2. The node: assembling it and accounting for it
Worker nodes must be configured for the selected sandboxed runtime.
runc containers use Linux namespaces to separate process, filesystem, and network views, and cgroups to control resource use. They share the host kernel. Nodes need runc configured through a runtime such as containerd, but no guest kernel or hypervisor.
gVisor handles workload system calls in Sentry, while a separate Gofer process mediates access to host-backed files. Each eligible node needs the gVisor runtime installed and integrated with containerd.
Kata Containers place each pod in a lightweight VM. Workload system calls go to the guest Linux kernel, separated from the host by hardware-backed virtualization. This adds overhead and requires bare-metal nodes or VMs that support nested virtualization. In aKernel-based Virtual Machine (KVM) setup, nodes need the Kata runtime shim, a supported virtual machine monitor (VMM), KVM and hardware virtualization, plus a guest kernel and image containing the kata-agent. You must maintain that guest image. A kernel CVE means patching two kernels. For use cases requiring flexibility and strict isolation, that burden may be necessary.
3. The access layer: limiting the agent’s reach
A sandbox protects the host from the agent, not from anything it’s handed. Code inside can still delete a writable repository, read a mounted secret, or send data wherever the network allows. Sandbox policy matters as much as the sandbox itself:
- Network: Default-deny egress with a NetworkPolicy, then allow only the destinations a task needs, such as a package mirror or model endpoint.
- Credentials: Issue short-lived credentials scoped to the task, not long-lived tokens mounted into the pod. A leaked credential expires with the task.
- Storage: Mount repositories and data read-only unless the task needs to write, and give writable workspaces their own volume.
- Remote tools: Give API endpoints and MCP servers their own authorization. They run outside the sandbox, so its boundary does not cover them.
4. The request: RuntimeClass
Kubernetes lets users retain the standard Pod API while selected pods, including agents, opt into a more isolated runtime. RuntimeClass lets pods select the security and performance balance they need without taxing non-agentic workloads.
Additional isolation affects resource consumption and pod readiness. gVisor’s Sentry processes and Kata’s guest kernel, kata-agent, and VMM add memory and CPU overhead. Add measured overhead to the RuntimeClass so the Kubernetes scheduler and resource quotas account for it. Measure your workloads rather than copying an example.
Cluster administrators create a RuntimeClass matching the node’s configured runtime. It tells Kubernetes the runtime is available, how pods select it, and what overhead it needs:
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: kata
handler: kata              # runtime name in the node's containerd config
overhead:
  podFixed:
    memory: "160Mi"        # example value; measure your own
    cpu: "250m"
scheduling:
  nodeSelector:
    sandbox.example.com/kata: "true"
A pod opts in through the runtimeClassName field of its spec: 
apiVersion: v1
kind: Pod
metadata:
  name: agent-task
spec:
  runtimeClassName: kata   # or gvisor; omit for the default runc
  containers:
  - name: workspace
    image: python:3.12
Everything else stays the same. Workloads that do not need sandboxing omit the field and use the default runtime. A cluster can expose each runtime as a separate RuntimeClass.
5. The session layer: Agent Sandbox
Agent work comes in bursts. An agent runs code, then waits minutes or hours for the next interaction with a model or human. Keeping a VM running keeps it ready to resume work but consumes capacity. Tearing it down saves capacity but requires rebuilding it later. Warm pools offer a middle ground, but reserve capacity.
“Agent work comes in bursts. An agent runs code, then waits minutes or hours for the next interaction with a model or human.”
The Agent Sandbox project, owned by Kubernetes SIG Apps, standardizes this choice. Its Sandbox API creates stateful single-pod environments with stable identities and persistent storage, plus extensions for templates, claims, and warm pools. It remains runtime-agnostic and leaves isolation to the selected RuntimeClass.
Our approach: building on community projects
Community projects have helped us achieve our goal of letting users run untrusted agent code on shared infrastructure using Kubernetes tools they already know. They keep workloads portable: the same pod spec runs on any conformant cluster. Security fixes and design reviews come from a network larger than any one vendor. And frameworks that integrate with Agent Sandbox do not need a new API. Thanks to the community, users can adopt these new tools without reinventing the wheel.
We are thankful to be a part of this dynamic space and excited to see it evolve.
