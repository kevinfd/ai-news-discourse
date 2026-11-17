---
id: "e67a42e4259862bd"
title: "NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure"
url: "https://marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu"
link: "https://marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T10:37:11Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA has released 2 open-source projects for running managed Kubernetes on GPU infrastructure: NVIDIA Kubernetes Engine (NVKE) and NVIDIA Kubernetes Recipes (NVKR) . Both were recently announced as components of the NVIDIA DSX AI Factory Platform . NVKE is the control plane for a managed Kubernetes service. NVKR builds the OS images, container images and packages those clusters depend on. Both…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "New Releases", "Open Source", "Staff", "Tech News"]
orgs: ["Nvidia", "Microsoft", "Amazon", "Hugging Face"]
topics: ["chips & infrastructure", "products & launches", "models & research", "jobs & society"]
content_source: "summary"
word_count: 943
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure

MarkTechPost · Asif Razzaq · 2026-11-17

NVIDIA has released 2 open-source projects for running managed Kubernetes on GPU infrastructure: NVIDIA Kubernetes Engine (NVKE) and NVIDIA Kubernetes Recipes (NVKR) . Both were recently announced as components of the NVIDIA DSX AI Factory Platform . NVKE is the control plane for a managed Kubernetes service. NVKR builds the OS images, container images and packages those clusters depend on. Both ship under Apache 2.0 and are in public preview. 

 TL;DR 

 Size / footprint: 3 CPU servers for the management cluster, 3 CPU servers per workload control plane, plus a pool of GPU worker nodes. A local evaluation needs 6 CPUs, 12 GiB RAM, 100 GiB disk and no GPU. 

 Runs on: your own NVIDIA GPU bare-metal servers, provisioned through NVIDIA Infra Controller (NICo). Node images build for amd64 and arm64. 

 Performance: no throughput or provisioning-time benchmarks are published. Quality signal is certification, not speed. 

 Best: Certified Kubernetes AI Platform and Certified Kubernetes Installer, conformance tested on Kubernetes 1.36. 

 Worst: after install, the NVKE API serves plain HTTP on port 30080 with authentication off, and there is no management-plane upgrade or backup procedure. 

 Bottom line: best thing: open, attested, upstream Kubernetes for GPU clouds. Worst thing: preview-grade security and lifecycle gaps; not for production yet. 

 What is NVIDIA Kubernetes Engine (NVKE)? 

 NVKE is open-source software that an AI factory installs to run a managed Kubernetes service on its own NVIDIA GPU infrastructure . The repo calls it ‘a self-hosting factory for Kubernetes clusters,’ not a distribution. It exposes a REST API and controllers on a management cluster. Customers get standard clusters and use kubectl . The operator manages them through the NVKE API or the nvkectl CLI. 

 NVKE uses upstream Kubernetes, kubeadm and Cluster API . It is written in Go and has no runtime dependency on NVKR. 

 What does NVIDIA Kubernetes Recipes (NVKR) do? 

 NVKR is a build system with declarative Definitions . It produces executables, container images, Helm charts and node images for amd64 and arm64. ‘Recipes’ define validated combinations of software versions and GPU generations. Hosted workflows attach signatures, SBOMs and provenance to digest-pinned OCI references. NVKR can also build artifacts for other Kubernetes management systems. 

 How does the NVKE architecture work? 

 The NVIDIA technical blog walkthrough describes 5 stages: 

 Bootstrap: nvkectl bootstrap site starts a temporary single-node kind cluster on a bootstrap host. 

 Management cluster: NVKE requests 3 servers from NICo, which boots them from the node image. The temporary cluster is then deleted. 

 Machine provisioning: NICo handles bare-metal lifecycle. CAPNICo , a Cluster API provider, connects NICo to NVKE. 

 Release sets: operators publish a machine image, a cluster release and a node pool release. Customers pick a release by name. 

 Workload clusters: each customer cluster has its own control plane, etcd and node pools. NVKE installs OVN-Kubernetes and NodeLocal DNSCache. 

 A node must present an attested SPIFFE identity before it gets join credentials. The README says SPIRE uses TPM for this. Per-cluster etcd encryption is available. An OpenTelemetry-based Helm chart exports logs, metrics and traces over OTLP. 

 Inside workload clusters, 3 companion projects plug in: AI Cluster Runtime (AICR) for the GPU runtime, NodeWright for node packages and NVSentinel for break-fix automation. 

&&

 How does NVKE compare with Gardener and Kamaji? 

 NVKE + NVKR ( NVIDIA ) Gardener ( SAP ) Kamaji ( Clastix ) What it is Managed Kubernetes management plane plus artifact builder Kubernetes clusters as a service Hosted control plane manager Control plane model Dedicated per cluster: own control plane, etcd, node pools Runs as pods in seed clusters Runs as pods; shared Datastore possible Target infrastructure NVIDIA GPU bare metal via NICo AWS, Azure, GCP, OpenStack, Alicloud (conformance table); extensible Works alongside Cluster API providers License Apache 2.0 Apache 2.0 Apache 2.0 Conformance Certified Kubernetes AI Platform and Installer; tested on 1.36 Certified up to v1.35 Described as CNCF-compliant Node identity SPIFFE/SPIRE attestation with TPM Not disclosed Not disclosed Signed build pipeline Yes (NVKR: signatures, SBOMs, provenance) Not disclosed Not disclosed Maturity Public preview, not for production Self-described production-ready Not disclosed 

 Who is adopting NVKE and NVKR? 

 NVIDIA Cloud Partners Firmus and SK Telecom are integrating both projects into AI factories. Mirantis, Rafay, Spectro Cloud, OpenNebula Systems and vCluster are adding components to managed Kubernetes offerings. Netris is enabling NVKE for its network automation. 

 How do you try NVKE? 

 A local quickstart runs on 1 Linux host or VM, amd64 or arm64. It needs at least 6 CPUs, 12 GiB free memory, 100 GiB free disk, Docker and virtual TPM support. No GPU or NVIDIA account is required. A real install needs a NICo deployment with enrolled capacity, a build host with KVM, an HTTP server and a registry. 

 NVKR has no qualified Release yet . 

 Key Takeaways 

 NVKE manages clusters; NVKR builds and signs what they run. 

 Both are Apache 2.0, in public preview, not for production. 

 Conformance tested on Kubernetes 1.36, with TPM-attested node identity. 

 Default API is HTTP on port 30080 with auth off. 

 Local evaluation needs 6 CPUs, 12 GiB RAM and no GPU. 

 Check out the NVKE repo , NVKR repo , docs and technical blog . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post NVIDIA Open-Sources NVKE and NVKR for Managed Kubernetes on GPU Infrastructure appeared first on MarkTechPost .
