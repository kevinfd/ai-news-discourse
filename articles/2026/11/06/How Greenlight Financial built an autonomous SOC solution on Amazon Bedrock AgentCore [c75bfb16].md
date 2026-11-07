---
id: "c75bfb16cb415abe"
title: "How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock AgentCore"
url: "https://aws.amazon.com/blogs/machine-learning/how-greenlight-financial-built-an-autonomous-soc-solution-on-amazon-bedrock-agentcore"
link: "https://aws.amazon.com/blogs/machine-learning/how-greenlight-financial-built-an-autonomous-soc-solution-on-amazon-bedrock-agentcore"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-06T16:55:05Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Adam Maksimuk"]
language: "en"
summary: "Greenlight Financial resolves more than 90 percent of up to 4,000 security and risk cases each month without human intervention. Greenlight’s Luna uses Amazon Bedrock AgentCore , infrastructure for building, connecting, and optimizing agents at scale. Specifically, Greenlight uses AgentCore runtime, a capability of Amazon Bedrock AgentCore, to host Luna’s agent code. It uses AgentCore memory, a…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Customer Solutions"]
orgs: ["Amazon", "Anthropic"]
topics: ["agents & coding", "safety & ethics", "models & research", "robotics & autonomy"]
content_source: "fulltext"
word_count: 2031
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock AgentCore

AWS Machine Learning Blog · Adam Maksimuk · 2026-11-06

Artificial Intelligence
How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock AgentCore
Greenlight Financial resolves more than 90 percent of up to 4,000 security and risk cases each month without human intervention. Greenlight’s Luna uses Amazon Bedrock AgentCore, infrastructure for building, connecting, and optimizing agents at scale. Specifically, Greenlight uses AgentCore runtime, a capability of Amazon Bedrock AgentCore, to host Luna’s agent code. It uses AgentCore memory, a capability of Amazon Bedrock AgentCore, to support its tiered multi-agent system. This avoids the need to build and operate these capabilities in-house. Luna triages dark web breach-card alerts, identity anomalies, and financial-risk events in seconds.
This post explains how Greenlight Financial built an autonomous security operations center (SOC) solution on Amazon Bedrock AgentCore. We cover its multi-tiered supervisor architecture, more than 30 specialized agents, episodic memory for continuous learning, and expansion from SOC use cases into financial risk triage. We share production metrics, infrastructure decisions, and patterns for building autonomous security operations in regulated industries.
What Greenlight needed to solve
Greenlight Financial provides financial products for families: debit cards, savings tools, and connected devices such as the Family Hub and Pet Tracker. The company processes sensitive financial data at scale under the same regulatory requirements as major banks.
Greenlight’s SOC receives 3,000–4,000 security and risk alerts per month from four primary vectors:
- Dark web breach cards – Card Network and internal threat intel flag Greenlight customer cards found on the dark web.
- Identity and access anomalies – Unusual login patterns, privilege escalations, and policy violations across Identity Provider (IdP) and internal systems.
- Infrastructure alerts – Signals from Signals from EDR (Endpoint Detection and Response), SIEM (Security Information and Event Management), Asset Inventory, and other observability tools.
- Financial risk events – Suspicious transaction patterns, compliance triggers, and fraud indicators from card processing systems.
Each alert demands cross-referencing multiple data sources before an analyst can render a verdict. A single dark web breach card notification requires checking whether the card is active, deduplicating against prior notifications, reviewing customer session data, and checking open support tickets. This workflow takes a human analyst 15-30 minutes per case. At 4,000 cases per month, that math breaks.
Greenlight needed a system that could:
- Triage and resolve routine cases autonomously at machine speed.
- Escalate complex cases with full context to human analysts.
- Learn from resolution patterns to improve accuracy over time.
- Operate within financial services compliance guardrails.
Architecture: Tiered multi-agent system on Amazon Bedrock AgentCore
Greenlight built Luna as a hierarchical multi-agent system on Amazon Bedrock AgentCore. The architecture follows a tiered supervisor pattern that mirrors how human SOC teams operate. L1 handles volume, and L2 handles complexity.
Tier 1 supervisor: High-volume triage
Tier 1 supervisor uses an advanced language model available through Amazon Bedrock running on Amazon Bedrock AgentCore runtime within an Amazon Virtual Private Cloud (Amazon VPC). The runtime uses private subnets and direct code deployment through a ZIP file and Amazon Simple Storage Service (Amazon S3). It handles initial triage of incoming cases by orchestrating more than 30 specialized agents:
The Tier 1 supervisor receives cases through two paths: Amazon API Gateway, which exposes the Luna Queue API and a Model Context Protocol (MCP) endpoint, and Tines SOAR for automated alert ingestion. It determines which specialized agents to invoke based on alert type, synthesizes their findings, and renders a verdict. The median triage time for routine cases is single-digit seconds.
Tier 2 supervisor: Deep-dive investigation
Cases that exceed Tier 1’s confidence threshold escalate to a Tier 2 supervisor using an advanced foundation model on Amazon Bedrock with extended reasoning capabilities. This agent handles the 10 percent of cases that require multi-step reasoning:
- Re-investigates escalated cases with deeper cross-source correlation.
- Invokes specialized agents through boto3 with expanded context windows.
- Chains reasoning across 3–5 data sources to establish causality.
- Produces detailed investigation reports with evidence chains for human review.
The Tier 2 supervisor runs on a scheduled basis, using Amazon EventBridge rate triggers and Amazon Simple Notification Service (Amazon SNS) queue completions to batch-process escalated cases, and on demand for urgent Tier 1-escalated cases.
Entry points for different personas
Different teams engage Luna in different ways, so the application exposes three entry points. These range from fully automated alert ingestion to interactive, on-demand investigation. Each entry point maps to a persona and how their work arrives:
- Tines SOAR – Primary volume driver. Automated alert ingestion feeds cases directly into Tier 1.
- Security, Risk, and ProdOps engineers – Direct API access for ad-hoc investigation requests.
- Claude Desktop extension – Chat-based interface for on-call engineers. An engineer opens the extension, describes what they want investigated, and Luna executes a deep-dive with full tool access.
Memory and learning: How Luna gets smarter over time
The memory layer is built on AgentCore memory. This layer is what separates Luna from a stateless triage tool. It supports pattern recognition, deduplication, and continuous accuracy improvement.
Episodic memory (30-day rolling window)
Stores recent events and resolution outcomes. When a new alert arrives, Luna checks: “Have I seen this pattern in the last 30 days? What was the verdict? Is this a known behavior that I should allowlist?”
Concrete example: A Greenlight infrastructure role generates a specific access pattern every Tuesday at 3 AM for scheduled maintenance. Without memory, Luna would flag this every week. With episodic memory, Luna learned after the first resolution that this pattern is expected and auto-allowlists it.
Long-term memory
Persists semantic preferences and resolution templates beyond the 30-day window:
- “This access pattern is expected because that’s the role’s purpose.”
- Greenlight’s historical case data shows “Cards from this specific dark web source have a 73 percent false-positive rate – prioritize deduplication.”
- Resolution templates for recurring case types that encode institutional knowledge.
Case-learnings pipeline
A dedicated pipeline feeds resolution outcomes back into the system:
- Ingestion – An AWS Lambda function captures every case resolution from Tines events.
- Learnings + Dedup – DynamoDB stores resolution patterns and deduplicates similar cases. When Luna resolves a case the same way three times, it records that as a confirmed pattern.
- Digest – A Lambda function processes new learnings into actionable context that supervisors consume at inference time.
- Feedback loop – Resolution learnings feed back into Tier 1, improving first-pass accuracy incrementally.
This pipeline drove Luna’s autonomous resolution rate from 83 percent (Tier 1 only) to more than 90 percent (Tier 1, Tier 2, and learnings).
Expanding from SOC into financial risk triage
Greenlight expanded Luna into financial risk assessment within two months of the SOC deployment. The architectural changes were minimal: new specialized agents and a risk-domain supervisor layered onto the existing infrastructure.
Dark web breach card workflow
When a Greenlight customer card appears on the dark web, Luna executes this workflow autonomously:
- Ingest – Threat intel providers (Mastercard, internal feeds) report compromised card numbers.
- Verify – Luna queries Galileo: Does this card belong to Greenlight? Is it currently active? What’s the recent transaction history?
- Deduplicate – DynamoDB check: Is this a repeat notification? Has this card already been remediated? Multiple providers often report the same breach.
- Cross-reference – Query Mixpanel for customer session anomalies, Zendesk for related tickets, and internal fraud scoring.
- Assess and act – Determine risk levels. Low risk: log and monitor. Medium risk: flag for review. High risk: escalate to human analysts with full evidence chain.
Greenlight receives hundreds of breach card notifications daily. Luna processes each in seconds. A human analyst doing the same work, logging into Galileo, checking DynamoDB, opening Mixpanel, searching Zendesk, takes 15-30 minutes per card.
Results
The following table tracks Greenlight’s security operations on the metrics that matter most to the SOC. It compares three stages: manual triage before Luna, Tier 1 automation, and the full Tier 1 and Tier 2 system.
Estimated analyst time avoided:
Based on Greenlight’s case volume and manual handling-time measurements, processing 4,000 cases at 15–30 minutes each would require approximately 1,000–2,000 analyst hours per month. Greenlight reports that Luna autonomously resolves more than 90 percent of these cases, avoiding an estimated 900–1,800 hours of routine manual work each month. Analysts can focus instead on cases that require human judgment.
The risk reduction comes from two factors: speed (seconds compared to minutes reduces the exposure window) and consistency (Luna applies the same triage logic at 3 AM on Saturday that it does at 10 AM on Tuesday, with no fatigue and no shortcuts).
Five lessons from building Luna
Building Luna and expanding it from security operations into financial risk surfaced five lessons for teams building multi-agent systems in regulated environments:
1. Start with a bounded domain, then expand horizontally
Greenlight started with security triage because the success criteria were clear: resolve the case correctly or escalate. After the pattern proved reliable at 83 percent resolution, expanding financial risk required adding new specialized agents and a risk-domain supervisor, not rebuilding the architecture.
2. Mirror your human team structure
The Tier 1/Tier 2 pattern maps directly to how SOC teams already operate. L1 analysts handle volume with playbooks. L2 analysts handle the complex cases with investigation skills. This made trust-building with the security team faster. They understood the model intuitively because it matched their own escalation logic.
3. Memory compounds in value
The episodic and long-term memory layer is what moved Luna from 83 percent to more than 90 percent. Each resolved case teaches Luna something: a new allowlisted pattern, a confirmed false positive source, a resolution template. After 6 months of operation, Luna has accumulated institutional knowledge that would take a new human analyst months to build.
4. Triage first, action later
In a regulated environment, Greenlight designed Luna to triage and recommend, not to take autonomous remediation actions without explicit policy approval. The risk expansion follows the same principle. Luna provides evidence supporting its recommendation. In this human-in-the-loop model, a human analyst or an approved automated policy authorizes and executes remediation. This separation satisfied Greenlight’s compliance requirements and built trust with the risk team.
5. Share specialized agents across domains
When Greenlight expanded into financial risk, they reused existing specialized agents (Datadog, Zendesk, Mixpanel) and added domain-specific ones (Galileo, fraud scoring). The same agent that checks Zendesk tickets for security cases also checks them for risk cases. This reduces maintenance overhead and helps keep consistency across domains.
Infrastructure stack
Luna runs entirely on managed AWS services. Amazon Bedrock AgentCore is the orchestration runtime, and the rest of the stack handles scheduling, messaging, state, secrets, and integration. The following table lists each service and its role in the infrastructure:
What Greenlight is building next
Building on the security and risk foundation, Greenlight is extending Luna’s multi-agent pattern into new operational domains and tooling:
- Full risk domain coverage – Autonomous triage for financial and business risk cases (in progress, launched about one month ago).
- Product operations – Exploring AWS DevOps Agent for incident investigation, root-cause analysis, and mitigation guidance. Greenlight is also evaluating how Luna’s existing agents could support operational investigations where their capabilities overlap.
- Custom operational workflows – Exploring AWS DevOps Agent custom agents, skills, and Model Context Protocol integrations for repeatable operational workflows and access to Greenlight’s internal tools.
- AWS DevOps Agent and skills – Combining the UI and skills framework of AWS DevOps Agent for script execution workflows (90-second execution time limit).
- Well-Architected reviews – Exploring Model Context Protocol servers for automated infrastructure assessments against AWS best practices.
Conclusion
According to Greenlight’s production measurements, Luna autonomously resolves more than 90 percent of the company’s security and risk cases and processes up to 4,000 cases each month. Cases requiring additional judgment are escalated to human analysts. This human-in-the-loop approach allows Greenlight to automate routine triage while retaining control over remediation decisions.
Teams in other regulated industries can apply the same approach by starting with a bounded use case, defining clear escalation criteria, and adding specialized agents and memory as the system matures. After the initial pattern proves reliable, teams can extend it to related operational domains.
To learn more, visit the Amazon Bedrock AgentCore product page and Amazon Bedrock AgentCore documentation.
