---
id: "8edd1a020853220d"
title: "NVIDIA's Run:AI is now apparently under Apache-2.0 license."
url: "https://github.com/dsx-ai-factory/run-ai"
link: "https://github.com/dsx-ai-factory/run-ai"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T06:07:37Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Ps3Dave"]
language: "en"
summary: "Docs | Roadmap | Installation | API Reference | Contributing | License\nNVIDIA Run:ai is an open-source AI workload and GPU orchestration platform for managing shared AI infrastructure on Kubernetes.\nNVIDIA Run:ai provides a consistent way to run development, training, and inference workloads across Kubernetes environments, whether deployed on-premises, in the cloud, or across hybrid…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "products & launches", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1024
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5jnbf/nvidias_runai_is_now_apparently_under_apache20/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# NVIDIA's Run:AI is now apparently under Apache-2.0 license.

GitHub · Ps3Dave · 2026-10-14

Docs | Roadmap | Installation | API Reference | Contributing | License
NVIDIA Run:ai is an open-source AI workload and GPU orchestration platform for managing shared AI infrastructure on Kubernetes.
NVIDIA Run:ai provides a consistent way to run development, training, and inference workloads across Kubernetes environments, whether deployed on-premises, in the cloud, or across hybrid infrastructure. It combines GPU scheduling, resource management, workload orchestration, governance, and observability to help organizations share GPU resources efficiently across teams and clusters.
This monorepo contains the NVIDIA Run:ai control plane and cluster services, installer, CLI, MCP server, documentation, shared client packages, and the local development environment.
NVIDIA Run:ai is made up of two components, both installed on a Kubernetes cluster:
- NVIDIA Run:ai control plane - Provides centralized resource management, handles workload submission, and delivers cluster monitoring and analytics. The control plane is the management layer; it connects to one or more NVIDIA Run:ai clusters and gives administrators and users a single place to operate across them.
- NVIDIA Run:ai cluster - Set of cluster services that provide enhanced scheduling and workload management on each Kubernetes cluster where workloads run. The cluster component extends Kubernetes native scheduling with Run:ai’s GPU-aware capabilities.
At a high level:
- Users and external systems interact with NVIDIA Run:ai through the web UI, CLI, or REST API.
- The NVIDIA Run:ai control plane manages workloads, organizational resources, policies, and configuration across connected Kubernetes clusters.
- NVIDIA Run:ai cluster services synchronize configuration and workload requests from the control plane to the appropriate cluster.
- NVIDIA Run:ai applies scheduling and resource policies to determine where and how workloads run on available GPU and compute resources.
- Workload and cluster status is synchronized back to the NVIDIA Run:ai control plane, providing centralized visibility across connected clusters.
NVIDIA Run:ai is a scheduling and orchestration layer on top of Kubernetes: it does not replace Kubernetes, a container runtime, or a CI/CD system.
If you need GPU sharing, quota enforcement, and multi-tenant governance across teams sharing one Kubernetes GPU estate, that is the gap NVIDIA Run:ai fills. If you only need to run a single team's jobs on dedicated GPUs, native Kubernetes scheduling may be sufficient.
For a detailed breakdown of individual services and components, see the Service Reference.
The local-dev.sh script builds the NVIDIA Run:ai control plane and cluster services from source and deploys them to a self-contained Kind cluster with a local image registry.
./local-dev.sh                                  # full build + cluster + deploy
./local-dev.sh --skip-build --skip-cluster      # re-deploy only
./local-dev.sh --teardown                       # tear the environment down
See Local Development Guide for prerequisites (Docker/Podman, make, git, curl, python3, openssl, and minimum CPU/RAM/disk; kind, kubectl, and helm are installed automatically) and all available flags. Go, Node, and Java are not needed on the host: all builds run inside containers.
Each service directory has a Makefile with standard targets (make build, make test, make lint, make validate) and a README describing how to build, test, and work with that service. See the Service Reference for a breakdown of individual services and components.
NVIDIA Run:ai can be deployed on Kubernetes or OpenShift in connected or air-gapped environments. To understand the full installation lifecycle, see the Installation and Configuration Overview.
Before you start:
- Support Matrix - Kubernetes/OpenShift versions, operating systems, GPU and network operators, and third-party services NVIDIA Run:ai supports.
- System Requirements - Infrastructure, networking, and access you need to prepare before installing.
Choose an installation method based on how you want to manage the deployment:
- Guided installation (recommended) - Uses the runai-installer CLI with a configuration YAML file. The installer performs preflight checks, installs required dependencies, and deploys the NVIDIA Run:ai control plane and cluster.
- Manual installation - Deploys the NVIDIA Run:ai Helm charts directly. Use this path if you manage deployments through your own tooling, such as Argo CD, or require granular control over Helm values.
To build and run NVIDIA Run:ai locally for development, see Usage.
Released NVIDIA Run:ai container images and Helm charts are published to the NVIDIA NGC container registry under nvcr.io/nvidia/runai: this is the registry the installer and Helm charts pull from by default. Source releases and their notes are on the GitHub Releases page; see Release Process for how releases are cut and versioned.
Contributions are welcome. Please read Contributing for the development workflow, branch and PR policy, and CI expectations, and Code of Conduct for community guidelines.
NVIDIA Run:ai does not publish a long-range feature roadmap in this repository. What is planned and in progress is tracked in the open:
- Open issues - Planned work, accepted feature requests, and known gaps. Issues are triaged and labelled by maintainers.
- Releases - What actually shipped in each version, with notes generated from the merged pull requests on that release branch.
- Support - Which versions are currently supported and when each moves to end of life.
Release cadence, branch naming, and who cuts a release are documented in Release Process.
Known limitations: the root Makefile targets are placeholders; real build, test, and lint targets live in each service directory (see Building Individual Services). The full CI gate runs remotely and is reported back on pull requests as the Validate Successful Run check.
- GitHub Issues - Bug reports, feature requests, documentation issues, and usage questions. This is the project's primary discussion forum; start here.
- Support - Supported versions and where to get help, including commercial support.
- Reporting a vulnerability: see Security; do not open public issues for security reports.
- Supported versions and getting help: see Support.
Licensed under the Apache License, Version 2.0; see LICENSE. Third-party attributions are listed in NOTICE and in the per-component NOTICE files.
Trademark notice: Apache 2.0 applies to the software code in this repository. It does not grant permission to use NVIDIA or Run:ai trademarks, logos, product names, fonts, artwork, or other brand assets. Please see Trademarks for details.
Some subdirectories contain vendored third-party code or bundled assets under their own license. Each is listed below with its license and the path to that license file:
The following subdirectories ship an aggregated third-party dependency license report (not a license for their own code):
