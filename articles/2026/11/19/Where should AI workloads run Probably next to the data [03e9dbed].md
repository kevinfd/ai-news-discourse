---
id: "03e9dbed5d4c5185"
title: "Where should AI workloads run? Probably next to the data."
url: "https://thenewstack.io/ai-workloads-data-gravity"
link: "https://thenewstack.io/ai-workloads-data-gravity"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T16:30:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Shubham Thakur"]
language: "en"
summary: "AWS raised prices on EC2 Capacity Blocks , its reserved GPU capacity, by about 15% in January and about 20% in July . Picture a platform team watching a training job’s bill climb after copying a few hundred terabytes of sensor data across regions just to reach the GPUs, then realizing the data never had to move. \n\n For AI workloads, the real question is whether the workload goes to the data or…"
tags: ["AI Infrastructure", "AI Strategy", "Data", "sponsor-acceldata", "sponsored-post-contributed"]
orgs: ["Amazon"]
topics: ["chips & infrastructure", "jobs & society", "models & research", "policy & regulation"]
content_source: "summary"
word_count: 1500
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Where should AI workloads run? Probably next to the data.

The New Stack · Shubham Thakur · 2026-11-19

AWS raised prices on EC2 Capacity Blocks , its reserved GPU capacity, by about 15% in January and about 20% in July . Picture a platform team watching a training job’s bill climb after copying a few hundred terabytes of sensor data across regions just to reach the GPUs, then realizing the data never had to move. 

 For AI workloads, the real question is whether the workload goes to the data or the data goes to the workload. Data gravity usually answers it. 

 Data gravity hits AI workloads harder than it ever hit analytics 

 Data gravity is the tendency of compute, applications, and services to be pulled toward large concentrations of data, because moving the data costs more than moving the logic that processes it. The larger a dataset grows, the more expensive every copy becomes, and the more everything that needs that data ends up living next to it. 

 Scheduled BI often tolerates periodic queries against sampled or aggregated data. Large training runs can require repeated reads of a much larger dataset, while agents retrieve fresh context throughout a workflow. When those reads cross regions or environments, transfer costs and latency add up. Each agent output also becomes new data that feeds the next round of retrieval, which compounds the pull over time. 

 A January 2026 analysis in BigDATAwire argued that AI workloads removed the cushion that let enterprises leave data gravity unmanaged for a decade. The year’s pricing moves make the same point from the cost side. Combined, the two increases add up to roughly 38% on the H200 instances that took both. 

 Moving data to the compute stops working at AI scale 

 Centralizing compute can require copying data into its environment before a job starts, and that transfer may carry charges. 

 For illustration, assume a transfer rate of $0.02 per GB and a 300 TB dataset (300,000 GB). The transfer alone would cost $6,000 per copy. That’s a hypothetical, not an AWS quote. Real charges depend on source, destination, route, service, and terms, so cross-region and cloud-to-premises movement needs explicit costing. Remote reads also add network latency, which matters when a workload has a tight response-time target. 

 “Transfer bills, duplicate pipelines and the engineering hours spent maintaining them belong in the placement calculation alongside compute charges.” 

 Two more costs rarely show up next to the GPU rate: 

 Interoperability overhead: cross-environment pipelines need their own translation layers when engines, query languages, connectors, and software development kits (SDKs) differ. 

 Lock-in: transfer charges and the engineering work of moving data and pipelines can make leaving an environment expensive. 

 Transfer bills, duplicate pipelines and the engineering hours spent maintaining them belong in the placement calculation alongside compute charges. 

 Moving compute to the data instead 

 A scheduling and placement layer can send a job to an environment that already holds its data, avoiding repeated full-dataset transfers. The job still needs compatible accelerators, enough memory, a supported runtime, and adequate storage throughput. Model weights, container images and checkpoints may also need to move. 

 Making that decision well means evaluating four inputs together, every time a job is scheduled: 

 Input What to evaluate Cost The total cost of this job in each candidate environment, including compute, transfer, storage, and queueing, at current prices. Data gravity How much data the job needs, where it sits, and what it would cost to move. Residency Which jurisdictions the data and the job are allowed to touch. Policy Which access rules, classifications and quality gates apply wherever the job lands. 

 A placement layer first excludes environments that violate residency or access rules, then compares feasible options by capacity, performance, and total cost. It dispatches the job with its runtime policies and revisits placement when those conditions change. 

 Where a specific workload belongs depends on the workload 

 There’s no universal rule. It’s a workload-by-workload decision. 

 Bursty training: public cloud can suit elastic demand, provided suitable GPU capacity is available, and transfer costs don’t erase the benefit. 

 Residency-restricted work: applicable law or contract determines the permitted jurisdiction and environment. An approved in-region cloud can qualify where an out-of-region on-premises cluster cannot. Large data volume adds an economic constraint, not a legal one. 

 Transaction-near inference: place execution close enough to the transaction to meet its latency target, whether in cloud, on-premises or at the edge. 

 Back to the platform team. Their training job reads a large dataset from an on-premises store, and policy excludes processing outside an approved region. A local cluster has the required GPU memory and runtime. An approved cloud region offers suitable GPUs but requires copying the dataset. So they compare completion time and total cost, including transfer, storage, and queueing. If local execution meets the deadline at lower total cost, the job runs there with the same access controls. If not, they assess the approved cloud option. 

 If neither environment meets policy and capacity requirements, the job is queued or rejected rather than sent to an unapproved region with restricted data. They record the choice and its assumptions so a price change, a growing dataset, or a missed deadline triggers a new review. 

 Formal policy on all this is uneven. In BARC’s State of Data and AI Governance study, which Acceldata sponsored, 56% of North American respondents report formal sovereignty policies for AI processing and storage, against 30% in Europe, the Middle East and Africa (EMEA). That runs against expectations, since Europe is known for strict data rules. EMEA respondents also name siloed data as a top governance obstacle more than twice as often as their North American peers, 35% versus 17%. 

 Hybrid architecture matters more than picking a cloud 

 Hybrid can be a lasting architecture, not merely a stop on the way to the cloud. Data-heavy, latency-sensitive, or sovereignty-bound work can stay on-premises, while the cloud handles demand where elasticity is worth the cost. 

 It needs common operational controls across both environments: identity, runtime compatibility, observability, and policy enforcement. An all-cloud estate incurs transfer and lock-in costs when data must leave a region or provider. An all-on-premises estate leaves bursty work waiting for fixed capacity. 

 “Hybrid can be a lasting architecture, not merely a stop on the way to the cloud.” 

 Job portability helps only where the target environment supports the required engines, dependencies, and hardware. Open table formats such as Apache Iceberg, Delta Lake, and Apache Hudi help here, because several engines can read the same tables in place. Moving the job doesn’t have to mean converting or copying the data first. 

 This is the problem Acceldata built its xLake platform around: keep data where it lives, in open formats, and bring governed compute to it across cloud and on-premises environments.  

 Sovereign AI requires more than GPU power 

 The sovereign AI conversation usually starts with GPUs, but GPU compute alone is an incomplete architecture. Owning or reserving GPU capacity says nothing about whether the data feeding those GPUs, or the retrieval and orchestration layers around them, stays inside infrastructure the organization controls. Sovereignty is a property of the whole data and AI stack. Compute is one layer of it. 

 For a strict customer-controlled boundary, Acceldata’s May 2026 analysis of sovereign GPU infrastructure identifies four controls:  

 Route tool calls through internally hosted endpoints so operational data, prompts, and workflow context never leave the organization’s network. 

 Retrieval infrastructure (embedding indexes and vector search) running on infrastructure the organization controls rather than a provider-managed vector service . 

 Orchestration of prompts, memory, and intermediate agent state inside the organization’s own environment. 

 Access policies for permissions and retrieval scope enforced within that same governed boundary. 

 “A workload can run on the most expensive reserved GPUs available and still fail a sovereignty review if its prompts, embeddings, or agent state cross a boundary they were never cleared to cross.” 

 Placement decisions inherit all four. A workload can run on the most expensive reserved GPUs available and still fail a sovereignty review if its prompts, embeddings, or agent state cross a boundary they were never cleared to cross. 

 The workload goes where the data already lives 

 Changes in compute prices are a reason to revisit placement, not proof that one environment is always cheaper. Transfer charges, storage, engineering effort, and completion time belong in the same comparison. That makes the cost of reaching the data a first-order input to any placement call, not a footnote to the GPU rate. 

 Keep the assumptions with each decision: dataset location, permitted destinations, compatible capacity, expected completion time, and total cost. When one changes, review the affected workload. Where running beside the data wins, move the job instead of the dataset. 

 Teams that revisit placement now, while their datasets are still manageable, will spend less fighting data gravity later than teams that keep copying data to wherever the GPUs happen to be. 

 That’s the lesson the platform team learned the hard way at the start of this piece. The data never had to move. The job did. 
 The post Where should AI workloads run? Probably next to the data. appeared first on The New Stack .
