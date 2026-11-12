---
id: "2f5ac4847b023025"
title: "How DXC Technology built a multi-model AI substrate on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/how-dxc-technology-built-a-multi-model-ai-substrate-on-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/how-dxc-technology-built-a-multi-model-ai-substrate-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T20:45:45Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Asif Fouzi"]
language: "en"
summary: "This post is co-written with Nick Tamburro of DXC Technology. \n When an AI agent can act on a production server at a bank or a hospital, access to a capable foundation model is only the starting point. Recent public incidents, in which autonomous agents took destructive actions their operators never intended, show that the real risk is rarely the model alone. It’s an agent holding more authority…"
tags: ["Amazon Bedrock", "Customer Solutions", "Intermediate (200)"]
orgs: ["Amazon", "Anthropic", "Meta"]
topics: ["models & research", "agents & coding", "policy & regulation", "safety & ethics"]
content_source: "fulltext"
word_count: 2134
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How DXC Technology built a multi-model AI substrate on Amazon Bedrock

AWS Machine Learning Blog · Asif Fouzi · 2026-11-11

Artificial Intelligence
How DXC Technology built a multi-model AI substrate on Amazon Bedrock
This post is co-written with Nick Tamburro of DXC Technology.
When an AI agent can act on a production server at a bank or a hospital, access to a capable foundation model is only the starting point. Recent public incidents, in which autonomous agents took destructive actions their operators never intended, show that the real risk is rarely the model alone. It’s an agent holding more authority than its task requires, with nothing in the architecture to stop it. Avoiding that starts with a substrate that governs model access at the infrastructure level.
Amazon Bedrock provides that substrate. Through a single managed interface, it gives DXC OASIS access to multiple foundation models: Anthropic Claude, Amazon Nova, Meta Llama, and open-weight families. Amazon Bedrock Guardrails enforce content filtering, personally identifiable information (PII) redaction, and denied-topic policies uniformly across every model. AWS PrivateLink keeps inference traffic within the customer’s virtual private cloud (VPC), and serverless scaling avoids self-managed GPU infrastructure as a failure point. Because these are system-level controls rather than bolt-ons, they gave DXC Technology a governed foundation for what no model layer can deliver on its own: a trusted harness that orchestrates, governs, and audits AI agents across enterprise IT operations at scale.
Model availability varies by AWS Region. See Supported models by AWS Region in Amazon Bedrock.
DXC Technology runs managed IT services for some of the world’s most regulated organizations: banks, hospitals, and government agencies. With more than 115,000 employees across 70 countries, DXC operates mission-critical systems where resilience and governance are non-negotiable. When DXC set out to build DXC OASIS, the harness for mission-critical IT operations, the team separated the problem into two layers. The first is a governed model substrate built on Amazon Bedrock. The second is the trusted harness built on top: DXC’s own orchestration, governance, and assurance layer.
In this post, we explore how DXC built the resilient, flexible model substrate beneath DXC OASIS on Amazon Bedrock. We also show where DXC drew the line between what the substrate provides and what the harness must provide. Since general availability in March 2026, DXC OASIS has reduced resolution time by 95% on average across 56 measured use cases.
Across every model, customer data stays within the AWS data boundary: prompts and completions are not shared with third-party model providers and are not used to train the underlying foundation models.
        “Our customers operate complex, business-critical environments and need both choice and resilience in how they adopt AI. Amazon Bedrock provides access to a broad ecosystem of models with the governance, security, and operational controls required at enterprise scale. That flexibility allows us to use the right model for the right task, adapt as technology evolves, and stay focused on delivering measurable business outcomes for our customers.”
— Dan Gray, President, GIS, DXC Technology
Solution overview
DXC OASIS separates the question of which model from the question of how work gets done. Amazon Bedrock is the substrate: a governed gateway to foundation models (FMs), reachable through one consistent API, with security and networking controls that keep traffic inside the AWS perimeter. The harness is everything DXC builds on top: orchestration across tools and systems, operational context drawn from 60 years of runbooks and escalation logic, policy enforcement, human-oversight gates, and full auditability of every agent action.
The design goals were:
- Resilience: No single point of failure at the model layer.
- Flexibility: Route each task to the most appropriate model on cost, latency, and capability.
- Regulatory sovereignty: Meet the data-handling expectations of regulated tenants.
- Safety by design: Bound what every agent can do, so that no action with operational impact runs without policy checks and, where required, human approval.
The main risk DXC designed against was coupling the system to any single provider, framework, or deployment target. The following diagram shows the key AWS services in the DXC DXC OASIS architecture.
Engineers and operators reach the system through Amazon Route 53 and an Application Load Balancer inside the customer’s Amazon Virtual Private Cloud (Amazon VPC). The DXC OASIS agent runtime runs on Amazon Elastic Kubernetes Service (Amazon EKS) in a private subnet. There, a supervisor agent delegates to capability agents that draw on a knowledge base, AWS Secrets Manager, Amazon EventBridge, and Amazon Simple Storage Service (Amazon S3). Every model call leaves the subnet through a VPC interface endpoint and AWS PrivateLink to reach Amazon Bedrock, so inference traffic doesn’t traverse the public internet. AWS Identity and Access Management (AWS IAM), AWS Key Management Service (AWS KMS), TLS 1.2, Amazon CloudWatch, VPC Flow Logs, AWS CloudTrail, and OpenTelemetry provide security and observability across every layer.
Building the DXC OASIS substrate
DXC began building DXC OASIS as a prototype in early 2025. A cross-functional team reached general availability in March 2026, scaling toward 130 customer environments on Amazon EKS with per-tenant namespaces and GitOps rollout. Building the substrate involved the following tasks:
- Establish governed, multi-model access through Amazon Bedrock.
- Engineer resilience into every layer of the architecture.
- Route each workload to the most appropriate model.
- Draw the line between the substrate and the harness.
Establish governed, multi-model access through Amazon Bedrock
Every model DXC OASIS uses (Anthropic Claude, Amazon Nova, Meta Llama, and open-weight families) is reached through Amazon Bedrock model inference. A provider outage or deprecation therefore becomes a routing decision, not a system rebuild. Uniform access isn’t the same as uniform behavior, however: models differ in capability, response style, and failure modes. Substituting one model for another is an assurance activity as much as a routing change. Before a model enters production routing, the harness (not the API) evaluates it against DXC OASIS task suites. For more information, see Getting started with Amazon Bedrock.
Engineer resilience into every layer
Resilience in DXC OASIS isn’t one control but the compounding of several. The following table summarizes the resilience controls and what each does for DXC OASIS.
Beyond resilience, DXC OASIS also addresses data residency and sovereignty. Regional inference controls and AWS PrivateLink keep inference within approved AWS Regions and off the public internet, meeting the data-handling expectations of regulated tenants.
Route each workload to the most appropriate model
The strategic reason DXC built on Amazon Bedrock is optionality. Because every model sits behind the same API, the team routes each task to the most appropriate model on cost, latency, and capability, and adopts new frontier models as they arrive without re-plumbing the system.
Model choice as a workload decision
Each task’s capability, latency, and cost requirements determine which model it uses, not system constraints.
Intelligent prompt routing – A single serverless endpoint predicts response quality and routes requests between models in the same family. It sends simpler prompts to lower-cost models and complex reasoning to more capable ones. Prompt caching further cuts latency and cost. For more information, see Intelligent prompt routing in the Amazon Bedrock documentation.
Custom model import – With Custom Model Import, the same governance and tooling extend to models that DXC or its clients bring themselves.
Open and closed models together
Amazon Bedrock supports open-weight models alongside proprietary ones, so DXC pairs frontier reasoning with open-weight models a client can adapt and deploy under one set of guardrails.
Draw the line between the substrate and the harness
Every enterprise agent needs six capabilities. Some are substrate capabilities Amazon Bedrock provides directly. Others are things only the harness can provide because they depend on DXC’s operational context and accountability model. This boundary is also where agent safety is won or lost. Guardrails on model inputs and outputs are necessary, but only the harness can limit what an agent is allowed to do. The following table draws that line.
How a workload flows through DXC OASIS
To make the architecture concrete, the following use cases come from the DXC OASIS demo environment. The environment is built around AnyCompany Airlines, a fictional mid-sized airline running a hybrid on-premises and AWS estate.
- Incident resolution: Diagnose and fix an at-risk production server, from alert to resolution in under 10 minutes.
- Problem management: The ITSM agent ranks the top five incident categories and suggests how to reduce each, work that takes 2–3 hours by hand.
- Cloud cost analysis: For the AWS cloud engineer, the Metrics agent breaks down a 90-day cost trend by service and region, then investigates spending peaks on request.
The incident-resolution workflow shows how the substrate and the harness work together:
- Alert in business terms – A runbook fails to clear disk space on the FlightOps server. The CIO sees the alert as a business risk: Flight Operations scheduling might be affected within 4 hours. At the same moment, the Linux engineer sees the same alert with the technical detail needed to act.
- Plan and delegate – The engineer opens AI Assist from the dashboard widget, and the metric carries into the chat as context. A supervisor agent breaks the request into a plan and delegates to capability agents (DXC OASIS Metrics, Linux System, and ITSM), with every model call made through Amazon Bedrock.
- Grounded diagnosis – The DXC OASIS Metrics agent confirms the server is 99% full and cites the knowledge base articles behind its answer. The Linux System agent traces the problem to a single 5 GB temporary file.
- Human approval – The agent presents its full execution plan, and nothing runs until the engineer confirms it. In this workflow, the agent operates at the act-with-approval tier: it can diagnose freely, but it can’t change the production server without an explicit, recorded approval.
- Governed execution – The fix runs, and DXC OASIS records what ran, on which server, who approved it, and when. The audit trail comes from the harness, not from the agent’s own account of what it did.
- Learn and observe – The engineer can turn the conversation into a draft knowledge article. The Query Metrics view shows the agent timeline, delegation flow, and token usage behind the answer.
Results
Since reaching general availability in March 2026, DXC OASIS agents now serve 12 operational personas, spanning Linux, Windows, SAP, virtualization, backup and patching, AWS, Azure, and network operations. Across 56 measured use cases, DXC OASIS has reduced resolution time by 95 percent on average. The following table shows representative measurements.
Diagnostic accuracy is 92% or better, validated against senior engineer judgment.
Lessons learned and what comes next
Four architectural decisions proved most valuable:
Separate model choice from orchestration
By keeping model selection, orchestration framework, and deployment target as independent decisions, DXC avoids re-platforming when a layer evolves.
Compound resilience controls
No single control makes the system resilient. The combination of serverless infrastructure, guardrails at the model layer, private networking, and human-oversight gates creates defense in depth.
Draw the substrate-harness line explicitly
Clarity about what the cloud provides versus what you must build avoids both under-engineering (trusting the model to govern itself) and over-engineering (rebuilding capabilities the substrate already offers).
Bound autonomy before you scale it. Every DXC OASIS persona starts read-only, and broader authority is granted deliberately, one tier at a time. Treating autonomy as something granted per task, rather than a default, is what lets DXC put agents in front of production systems with confidence.
Bound autonomy before you scale it
Every DXC OASIS persona starts read-only and broader authority is granted deliberately, one tier at a time. Treating autonomy as something granted per task, rather than a default, is what lets DXC put agents in front of production systems with confidence.
Looking ahead, DXC is evaluating Amazon Bedrock AgentCore alongside the current orchestration layer, and expanding the system to support additional regulated workloads as new frontier models become available through Amazon Bedrock.
Conclusion
In this post, we showed how DXC Technology built DXC OASIS, the harness for mission-critical IT operations, on a governed, multi-model substrate in Amazon Bedrock. Keeping model reasoning separate from operational orchestration builds resilience, flexibility, and regulatory compliance into the architecture from the start. The payoff is measurable: resolution time is down 95 percent on average across 56 measured use cases. For teams building their own agentic systems, the lesson is to treat the substrate (what Amazon Bedrock provides) and the harness (what you build on top) as separate layers. Decide early which capabilities belong in each. As scrutiny of autonomous AI grows, that clear line, together with bounded, auditable agent authority, is what lets a system earn trust at scale.
To get started with multi-model architectures on Amazon Bedrock, see the Amazon Bedrock User Guide. To learn more about how DXC OASIS applies this architecture to enterprise IT operations, contact DXC Technology.
Related resources
- Amazon Bedrock User Guide
- Amazon Bedrock Guardrails documentation
- AWS PrivateLink documentation
- DXC OASIS
