---
id: "1014d195926575d5"
title: "Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes and vLLM"
url: "https://marktechpost.com/2026/11/07/buoyant-kinference-open-source-inference-control-plane-kubernetes-vllm"
link: "https://marktechpost.com/2026/11/07/buoyant-kinference-open-source-inference-control-plane-kubernetes-vllm"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-07T08:16:33Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Buoyant, the company behind Linkerd, has released Kinference , an open source project for building inference platforms on Kubernetes. Kinference is an inference control plane for Kubernetes and vLLM. It sits in front of a fleet of vLLM workers and decides where each request goes. It applies routing policies, token rate limits, KV-cache-aware load balancing and per-tenant metrics in one layer.…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source"]
orgs: ["Nvidia", "Google", "Amazon", "IBM", "CoreWeave"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 1034
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes and vLLM

MarkTechPost · Michal Sutter · 2026-11-07

Buoyant, the company behind Linkerd, has released Kinference , an open source project for building inference platforms on Kubernetes. Kinference is an inference control plane for Kubernetes and vLLM. It sits in front of a fleet of vLLM workers and decides where each request goes. It applies routing policies, token rate limits, KV-cache-aware load balancing and per-tenant metrics in one layer. For dev teams serving many open-weight models to many internal clients, it targets the layer above the model server. The project is Apache 2.0 licensed on GitHub . The current release is v0.1.0-alpha.7 . 

 TL;DR 

 Size: v0.1.0-alpha.7, written in Rust, Apache 2.0, configured through 5 Kubernetes CRDs. 

 Runs on: any GPU-enabled Kubernetes cluster running vLLM. Buoyant’s benchmark used 3 L40S GPUs per pool. 

 Performance: large gains on prefix-heavy traffic versus plain Kubernetes Service routing (self-reported). 

 Best: median TTFT fell from 6.88 s to 0.31 s (95%) on a shared-prefix workload. 

 Worst: no median TTFT gain on prompts without shared prefixes (6.92 s vs 6.83 s). 

 What is Kinference? 

 Kinference is a policy-driven control plane that turns Kubernetes plus vLLM into a multi-tenant inference platform. Buoyant’s FAQ puts it simply: vLLM is the data plane and Kinference is the control plane. 

 How does Kinference work? 

 The system has 2 parts: a traffic gateway and an inference handler. The GitHub README states that the handler exposes a gRPC interface. It takes a request and returns the chosen endpoint plus a possibly mutated body. It pairs with a proxy such as the Buoyant Gateway . 

 Kinference watches vLLM KV-cache events and engine metrics. It currently uses NVIDIA’s dynamo-kv-router crate to process cache events. Configuration lives in 5 CRDs: GatewayBackend, InferencePolicy, InferencePool, InferenceProvider and InferenceWorkerSet . 

 What are inference policies? 

 Inference policies are declarative rules for how each request is routed or rejected. Rules can match on tenant, requested model, GPU pool state and semantic tags. Example policies on the project site cover 5 patterns: 

 Simple to cheaper: route low-complexity prompts to a smaller model, unless cache overlap makes the large model faster. 

 Burst to cloud: skip workers with over 2 queued prompts, then fall back to providers like Bedrock. 

 PII stays local: remove external providers when a PII tag fires, and fail closed with onEmpty: Reject . 

 Batch on idle GPUs: send batch requests only to workers under 70% KV-cache usage. 

 Model aliasing: publish one stable name, such as standard-model , backed by several models. 

 Most rules end with minimize: PredictedTTFT . Kinference predicts time-to-first-token for each candidate endpoint, using cache overlap and queue length. Policies live in git and can be validated offline with the kinfctl CLI. 

&&

 How fast is Kinference in benchmarks? 

 Buoyant published a benchmark against plain Kubernetes load balancing . Each arm used 3 vLLM 0.31.0 pods, each on 1 L40S GPU. The model was Qwen3.8-27B-FP8 . Load came from GuideLLM 0.8.1. The baseline was a ClusterIP Service, where kube-proxy picks a random pod per connection. 

 Unloaded latency results (median TTFT): 

 Workload Kubernetes Service Kinference Change Control (no shared prefix) 6.92 s 6.83 s No significant difference Shared-prefix 6.88 s 0.31 s about -95% Multiturn 1.70 s 0.59 s about -65% 

 Median end-to-end latency fell 45% on shared-prefix and 32% on multiturn. On control traffic, p95 TTFT still dropped from 21.46 s to 12.33 s. Buoyant attributes this to queue-aware balancing. 

 The capacity test measured goodput: requests per minute meeting a TTFT SLO. Peak goodput was 103.0 vs 14.0 req/min on shared-prefix, about 7.4x. On multiturn it was 82.7 vs 23.8, about 3.5x. The Service baseline never met the SLO at any tested concurrency. 

 These numbers are self-reported. The baseline is random routing, not another cache-aware router like llm-d or Dynamo. Buoyant also notes its SLOs (8 s and 4 s) suit offline agents, not chat. 

 How does Kinference compare with llm-d, Dynamo and Production Stack? 

 Feature Kinference llm-d NVIDIA Dynamo vLLM Production Stack Backer Buoyant CNCF sandbox (Red Hat, Google Cloud, IBM, CoreWeave, NVIDIA) NVIDIA vLLM project License Apache 2.0 Apache 2.0 Apache 2.0 Apache 2.0 Maturity v0.1.0-alpha.7 v0.7 (May 2026) 1.x (1.5.1 containers) Reference stack Engines vLLM (SGLang, TensorRT-LLM planned) vLLM, SGLang vLLM, SGLang, TensorRT-LLM vLLM KV-cache-aware routing Yes, predicted TTFT Yes, prefix-cache and predicted latency Yes, KV-aware router Session-based; prefix-aware listed as WIP Declarative routing policy CRD Yes (InferencePolicy) Not documented in README Not documented in README Not documented in README Burst to external providers Yes (InferenceProvider) Not documented in README Not documented in README Not documented in README Disaggregated prefill/decode Not disclosed Yes Yes On roadmap Multi-tenant controls Per-tenant metrics; rate limits planned Flow control for multi-tenant serving Gateway-level rate limiting via GAIE Not documented in README Main result -95% median TTFT vs kube-proxy (3x L40S) 3x throughput, 2x faster TTFT vs round-robin (4x MI300X) 2x faster TTFT with KV-aware routing (Baseten) Not disclosed 

 Kinference’s distinct angle is governance: policies, aliases, provider fallback and tenant accounting. llm-d and Dynamo lead on raw serving performance, disaggregation and engine coverage. 

 Deployment and availability 

 Installation takes 5 steps per the getting started guide . Teams install Gateway API v1.5.1 CRDs, the Buoyant gateway Helm chart, then the Kinference chart. Kinference ships Prometheus metrics and Grafana dashboards . Metrics include TTFT, ITL, end-to-end latency and cached versus uncached prompt tokens, mostly per tenant. 

 Key Takeaways 

 Kinference is an Apache 2.0 control plane for vLLM on Kubernetes, from Linkerd maker Buoyant. 

 Declarative InferencePolicy rules handle model choice, provider bursting, PII routing and batch admission. 

 Self-reported median TTFT fell 95% on shared-prefix traffic versus kube-proxy. 

 Peak goodput rose about 7.4x on shared-prefix and 3.5x on multiturn. 

 It is alpha: rate limiting, classifiers and Anthropic API support are not yet shipped. 

 Check out the GitHub repo , docs , launch post and benchmark report . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes and vLLM appeared first on MarkTechPost .
