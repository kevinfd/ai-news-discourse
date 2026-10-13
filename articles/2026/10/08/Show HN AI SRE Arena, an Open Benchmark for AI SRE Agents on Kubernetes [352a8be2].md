---
id: "352a8be27229a4e5"
title: "Show HN: AI SRE Arena, an Open Benchmark for AI SRE Agents on Kubernetes"
url: "https://github.com/edgedelta/project-arena"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T17:13:08Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["emrahsamdan"]
language: "en"
summary: "A vendor-neutral starter for deploying a disposable Kubernetes fixture, injecting faults, saving investigation records from any product, and scoring completed investigations with a configurable judge. Python 3.10+ is the only Python dependency. Kubernetes operations additionally need kubectl; local cluster creation needs Docker and kind.\nChoose local kind or AWS EKS for your cluster, then select…"
tags: []
orgs: ["Amazon", "Anthropic", "Apple", "OpenAI", "Intel", "AMD"]
topics: ["jobs & society", "models & research"]
content_source: "fulltext"
word_count: 1696
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50008642"
score: 24
comments: 10
community: "Hacker News"
---

# Show HN: AI SRE Arena, an Open Benchmark for AI SRE Agents on Kubernetes

GitHub · emrahsamdan · 2026-10-08

A vendor-neutral starter for deploying a disposable Kubernetes fixture, injecting faults, saving investigation records from any product, and scoring completed investigations with a configurable judge. Python 3.10+ is the only Python dependency. Kubernetes operations additionally need kubectl; local cluster creation needs Docker and kind.
Choose local kind or AWS EKS for your cluster, then select the 21-scenario full suite or six-scenario smoke fixture. Cluster type and scenario suite are separate choices.
flowchart LR
    A[Deploy cluster and application] --> B[Connect your product]
    B --> C[Inject and verify a fault]
    C --> D[Let your product investigate]
    D --> E[Save investigation records]
    E --> F[Score with your chosen judge]
    F --> G[Compare results]
    Run commands from the Project Arena directory. Cluster setup, product integration, scenario execution, and scoring are separate steps; follow the sections below in order.
We compared Edge Delta’s native AI investigations, Grafana’s native AI investigations, and Claude using each platform’s observability CLI across 21 Kubernetes incident scenarios. edx provides access to Edge Delta; gcx provides access to Grafana. All final investigations were evaluated against the same incident facts and scoring rubric using GPT-6-Astra.
Edge Delta detected and investigated 18 scenarios; Grafana detected and investigated 12. Claude was started externally for all 21 scenarios on each platform: 16 alerts and 5 customer reports with edx, and 12 alerts and 9 customer reports with gcx. Detection was not independently measured for Claude, so those cells are shown as —.
Investigation scores use every completed investigation for that column. Implementation readiness excludes cases with no mitigation proposal.
This table uses the 12 incident types investigated by both native products, with the corresponding Claude investigations. It controls which scenarios are included, not differences in launch prompts, timing or available evidence.
View results for every scenario · Download CSV
Mitigation and readiness measure proposals, not executed repairs or verified recovery.
See the scoring rubric for grading rules and full results and methodology for verdict breakdowns and evaluation details.
Run all commands from the Project Arena directory. Both environments use the same benchmark commands after cluster and image setup. The runner uses the context you provide; it does not automatically install networking or configure registry access.
Cluster setup and deployment method are separate choices:
The GitOps path uses component Applications, flagd-values, and batch-active. Application and fault configuration can live in separate repositories or separate paths in one repository. Use your own repositories and configure their URLs. Record which repositories the investigating product can access.
The deployment, fault, and reset commands below use the direct path. For an Argo-managed application, use the GitOps guide's commands; direct mutations are blocked to avoid conflicting with Argo's self-healing. Investigation import, scoring, and reporting work the same way for both paths.
Install Python 3.10+, kubectl, Docker, kind and Helm. Follow the kind setup to create a cluster with Cilium and load the full-suite images. Then select its context:
export ARENA_CONTEXT=kind-incident-bench
The full suite uses prebuilt application images for Linux AMD64 and requires AMD64 workers. Apple Silicon Macs can run the smoke suite on native ARM64 kind workers, or operate an AMD64 EKS cluster. Building ARM64 fault images alone does not make the full application ARM64-compatible.
For the full suite, keep registry: "fixture.local" and tag: "v1" in arena.json. The linked setup enables NetworkPolicy enforcement for netpol-isolation. For smoke alone, python3 -m bench cluster create is sufficient; smoke uses a pinned public image and does not need the full-suite image build.
Install Terraform and the AWS CLI in addition to Python, kubectl and Docker. Configure your AWS credentials, then follow the AWS cluster setup to create the cluster and kubeconfig context. Authenticate Docker to your registry and build images for your worker architecture:
export ARENA_CONTEXT=YOUR_CONTEXT
kubectl --context "$ARENA_CONTEXT" get nodes -L kubernetes.io/arch
# Choose the platform matching the workers shown above.
export ARENA_PLATFORM=linux/amd64  # Required by the full suite’s prebuilt application.
python3 -m bench.scenarios build-images --registry YOUR_REGISTRY/bench \
  --tag YOUR_TAG --platform "$ARENA_PLATFORM" --push
Choose the worker architecture, regardless of which computer runs the build:
An Apple Silicon Mac can build for Intel/AMD EKS workers using linux/amd64; Docker Desktop supports cross-platform builds through emulation. This command builds one target architecture at a time. On mixed-architecture clusters, the application is scheduled on AMD64 workers.
Set registry and tag in arena.json to those same values. Nodes must have pull access to the registry; configure registry permissions or Kubernetes pull credentials yourself. AWS resources incur charges. Terraform currently creates subnets in three availability zones within one region; zone count and worker count are separate settings.
After either setup, install your product's collector and alert configuration using its instructions. Continue with the run configuration below.
python3 -m bench init
Edit the generated arena.json:
The default full suite currently includes 21 scenarios. The smaller smoke suite includes six and uses a public Python image, so it does not need the fault-image build. They use different applications; select a suite before deploying. See the scenario table for requirements and differences.
python3 -m bench catalog
python3 -m bench deploy
Before injecting a fault, complete product setup and confirm the product receives the healthy application's telemetry.
For the full suite:
python3 -m bench fault
python3 -m bench verify
python3 -m bench evidence
fault applies the manifests; verify checks whether the expected failure is observed. Successful application alone does not establish a valid test. Let the product finish investigating before resetting the fault.
For smoke, use fault and evidence, then inspect pod status, events and service availability yourself; automated verify currently supports only full. A healthy smoke app serves HTTP on port 8080:
kubectl --context "$ARENA_CONTEXT" -n incident-bench port-forward service/api 8080:8080
# In another terminal:
curl http://localhost:8080/health
For another attempt, reset first and select a fresh case directory with --case, placed before the command:
python3 -m bench --case oom-attempt2 fault
python3 -m bench --case oom-attempt2 verify
python3 -m bench --case oom-attempt2 evidence
Use that same --case for subsequent import and scoring commands. It selects an artifact directory, not a different scenario. Change scenario in the run file when testing another fault.
Install your product's collector and configure alerts using its own instructions. Project Arena does not install a vendor agent, log in to a product, or configure alerts automatically. Kubernetes logs, events, pod state and application behavior provide the fault signals; collect metrics and traces through your chosen tooling.
Set product in arena.json to the name you want in comparison tables. After the investigation, save these files under <output_dir>/<scenario>/ (or your selected case directory):
Import them with:
python3 -m bench archive
The command uses those filenames automatically. Missing final input is an error; missing intermediate/action evidence stays missing. Record detection explicitly with --detection detected or --detection not_detected when supported by an observation window and evidence; the default is not_measured.
Manual export is supported. For API-based integration, provide an exporter using the investigation record format. Hosted-product connectors are not bundled. An undetected case can still have a record with an empty final answer; it must not be represented as a completed investigation.
The judge is an AI model that compares a completed investigation with the scenario's answer key and the scoring rubric. Answer keys are included.
- In arena.json, choose the judge provider and model. For example, edit the existing judge section:
"judge": { "provider": "openai", "model": "YOUR_MODEL" }
- Make the provider's API key available in your shell (OPENAI_API_KEY for this example). Keep the key out of arena.json. Other providers and local models are supported.
- After importing the investigation, run: python3 -m bench packet # Prepare the investigation, answer key and scoring rules python3 -m bench judge # Send them to your chosen model
The result is judgment.json in the case directory: scores, explanations and supporting quotes. Use the same judge model and settings for every product you compare. API calls may incur charges.
You can score the same saved investigation again without rerunning the incident. See rescoring and saved results for details.
python3 -m bench report --summary > summary.csv
python3 -m bench report --details > details.csv
The summary puts metrics in rows and products in columns. Each cell shows successful/applicable (percentage). Illustrative values, not benchmark results:
The actual report includes every scoring dimension. The detail table lists each scenario's verdict and whether it is included in the denominator. Undetected cases count against detection rate; not-applicable cases are excluded from the relevant scoring denominator. Insufficient evidence stays in the denominator for applicable scored cases. Missing measurements and unscored investigations remain visible in the details. A dash means no applicable scored cases.
Product names come from investigation records, matched to judgments by content hash. Records and judgments are discovered in the configured run directory. Include records for undetected cases too. Use matching scenario cohorts, rubric and judge settings when comparing products; see report options and counting rules for combining runs and interpreting each metric.
For GitOps, follow the Git reset and sync workflow so the repository and cluster return to the same baseline.
For the full suite using direct deployment:
python3 -m bench reset --confirm-disposable
This retires the injected resources, restores the three scenario flags, and clears only that fault’s persistent effects. Healthy services, application data, credentials and the cluster remain in place; reset verifies the baseline before another fault. For smoke, use python3 -m bench reset; it restores the app but retains the storage fault's PVC.
python3 -m bench cluster delete --confirm-delete
Remove application resources and any provisioned volumes or load balancers, then follow the AWS teardown instructions. Resetting a fault does not stop AWS charges. Optional Terraform state storage persists separately.
- Use --run path/to/run.json before a command to select another configuration. Explicit flags override saved settings.
- Configured file paths are relative to the run file. Explicit CLI paths and judge executable arguments are relative to the current working directory.
- Use packet --rubric path/to/rubric.md for a custom rubric. Keep the same rubric and judge settings across compared products.
- Product exporters and judge formats describe custom integrations and evidence requirements.
- Scenario implementation guide covers manifests, image builds, verification and reset behavior.
To run the offline tests:
python3 -m unittest discover -s tests -v
Project Arena is licensed under the MIT License. Bundled third-party code retains its own license, including the shop application under Apache-2.0.
