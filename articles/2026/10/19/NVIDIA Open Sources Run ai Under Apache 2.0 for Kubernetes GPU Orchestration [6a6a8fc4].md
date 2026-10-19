---
id: "6a6a8fc4981604fb"
title: "NVIDIA Open Sources Run:ai Under Apache 2.0 for Kubernetes GPU Orchestration"
url: "https://marktechpost.com/2026/10/18/nvidia-runai-open-source-gpu-orchestration-kubernetes"
link: "https://marktechpost.com/2026/10/18/nvidia-runai-open-source-gpu-orchestration-kubernetes"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T03:19:18Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA has released the full NVIDIA Run:ai platform as open source software. The source code ships under the Apache 2.0 license on GitHub. NVIDIA Run:ai open source puts production GPU scheduling, quotas and workload management in developers’ hands. The release, makes Run:ai part of the NVIDIA DSX AI Factory platform. Platform teams can now inspect, fork and self-host the stack without a paid…"
tags: ["Agentic AI", "AI Infrastructure", "Applications", "Artificial Intelligence", "Editors Pick", "Embedding Model", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Nvidia", "Microsoft", "Tesla", "Intel", "AMD"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 951
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Open Sources Run:ai Under Apache 2.0 for Kubernetes GPU Orchestration

MarkTechPost · Asif Razzaq · 2026-10-19

NVIDIA has released the full NVIDIA Run:ai platform as open source software. The source code ships under the Apache 2.0 license on GitHub. NVIDIA Run:ai open source puts production GPU scheduling, quotas and workload management in developers’ hands. The release, makes Run:ai part of the NVIDIA DSX AI Factory platform. Platform teams can now inspect, fork and self-host the stack without a paid subscription. 

 TL;DR 

 Size: Monorepo with control plane, cluster services, installer, CLI and MCP server. Local dev builds about 50 Go services. 

 Runs on: Kubernetes or OpenShift clusters with NVIDIA GPUs. Local dev runs on macOS or Linux with 8 simulated Tesla-A10 GPUs, no GPU needed. 

 Performance: NVIDIA published no platform-level benchmark for this release. 

 Best: The related Model Streamer loaded models 3x to 6x faster on 8 NVIDIA H100 VMs on Azure. 

 Worst: The community edition has no NVIDIA enterprise support. Local builds need 16 GB RAM and 100 GB disk on Linux. 

 What is NVIDIA Run:ai? 

 NVIDIA Run:ai is an AI workload and GPU orchestration platform for Kubernetes from NVIDIA. It schedules development, training and inference workloads across shared GPU clusters. It runs on top of Kubernetes and does not replace it. 

 The control plane handles workload submission, resource management and monitoring. Cluster services run on each Kubernetes cluster and add GPU-aware scheduling. Users reach it through a web UI, CLI, REST API and an MCP server for AI assistants. 

 What are the 4 modular components? 

 NVIDIA split the release into 4 components that teams can adopt independently: 

 KAI Scheduler is the Kubernetes-native scheduling engine. It is Apache 2.0 and a CNCF Sandbox project . It covers gang scheduling, time-based fair-share, topology awareness, bin-packing and DRA support. 

 GPU Fractioning Operator brings CUDA 13.4-native GPU fractions to Kubernetes. The CUDA driver enforces a hard memory limit per workload. NVIDIA retired its older proprietary fractioning in favor of this approach. The operator is scheduler-agnostic and exports per-pod metrics. 

 KAI Resource Management adds projects, departments, quotas and node pools. NVIDIA’s example guarantees 50% of a cluster to a research team. 

 Workload Map is a Go library that describes workload types such as PyTorchJob, RayCluster and KServe services. It works offline and does not schedule, queue or autoscale. 

 How do developers run NVIDIA Run:ai locally? 

 The local development guide stands on 1 script, local-dev.sh . It builds about 50 Go services from source inside containers. It then creates a 5-node Kind cluster pinned to Kubernetes v1.32.5. A fake GPU operator simulates 8 Tesla-A10 GPUs, so no GPU hardware is required. 

 Supported hosts: macOS or Linux, on amd64 or arm64. Windows is not supported. 

 Linux hosts need 4 CPUs, 16 GB RAM and 100 GB free disk. 

 macOS Podman VMs need at least 12 GB RAM. 

 1 full build leaves about 44 GB of caches. 

 The --gpu-operator flag switches to real NVIDIA GPUs. That mode needs Linux, Docker and the NVIDIA Container Toolkit. AMD and Intel accelerators are not supported. 

 How can teams deploy it in production? 

 Dev teams can deploy from source or from the NGC Community Product Helm chart. That edition needs no paid subscription but excludes NVIDIA enterprise support. 

 Teams can also adopt it through 8 DSX ecosystem partners. These are Crusoe , Mirantis , Nebius , OpenNebula Systems , Rafay , Saturn Cloud , Spectro Cloud and vCluster . Supported commercial editions continue through NVIDIA AI Enterprise, NVIDIA Mission Control and select cloud marketplaces. 

 What related open source projects ship alongside? 

 Two adjacent projects round out the stack. Model Streamer streams model weights directly into GPU memory. vLLM and SGLang enable it with --load-format runai_streamer . 

 Microsoft’s published benchmark used 8 NVIDIA H100 VMs. It showed 3x to 6x faster loading than the default loader. Throughput held at 80 Gbps versus about 40 Gbps on the default path. 

 Grove orchestrates multicomponent inference workloads. It starts components such as prefill and decode as all-or-nothing units. 

&&&

 How does NVIDIA Run:ai compare with other open source Kubernetes schedulers? 

 Feature NVIDIA Run:ai (open source) Volcano Kueue Apache YuniKorn License Apache 2.0 Apache 2.0 Apache 2.0 Apache 2.0 Governance NVIDIA DSX AI Factory org (KAI Scheduler: CNCF Sandbox) CNCF Incubating kubernetes-sigs (wg-batch) Apache Software Foundation Scope Full platform: control plane, UI, CLI, REST API, MCP server Batch scheduling system Job queueing controller Scheduler, alternative to default Replaces kube-scheduler No, extends it with KAI Scheduler Not disclosed No Yes, as an alternative Gang scheduling Yes Yes Timeout-based all-or-nothing Yes Quota hierarchy Projects, departments, node pools Multi-level queues Cohorts, fair sharing Hierarchical queues GPU sharing CUDA 13.4-native fractions with hard memory limits vGPU, dynamic MIG DRA-based GPU quota; fractioning not in overview Not disclosed Topology-aware Yes Yes Yes Not disclosed Multi-cluster Yes, via control plane Yes Yes, MultiKueue Not disclosed Web UI Yes Separate dashboard project Not disclosed Not disclosed 

 The key difference is scope. Volcano, Kueue and YuniKorn focus on scheduling or queueing. Run:ai ships a full management platform on top of its scheduler. 

 Key Takeaways 

 NVIDIA Run:ai is now fully open source under Apache 2.0. 

 4 components ship standalone: KAI Scheduler, GPU Fractioning, Resource Management, Workload Map. 

 GPU fractioning now uses CUDA 13.4-native memory isolation. 

 Local dev runs on a 5-node Kind cluster with 8 simulated GPUs. 

 The free edition excludes NVIDIA enterprise support. 

 Check out the GitHub repo , the local dev guide and NVIDIA’s technical blog . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post NVIDIA Open Sources Run:ai Under Apache 2.0 for Kubernetes GPU Orchestration appeared first on MarkTechPost .
