---
id: "cd0c3adea5a38d8b"
title: "Autonomous treasury agents: How Trovata built an AI-native solution on Amazon Bedrock and AgentCore"
url: "https://aws.amazon.com/blogs/machine-learning/autonomous-treasury-agents-how-trovata-built-an-ai-native-solution-on-amazon-bedrock-and-agentcore"
link: "https://aws.amazon.com/blogs/machine-learning/autonomous-treasury-agents-how-trovata-built-an-ai-native-solution-on-amazon-bedrock-and-agentcore"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-10T18:11:08Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Kushal Mangtani"]
language: "en"
summary: "Corporate treasury teams face a persistent challenge: fragmented banking data scattered across dozens of bank portals, manual reporting trapped in spreadsheets, and legacy Treasury Management Systems (TMS) that can’t scale for modern enterprise needs. For treasury teams these manual processes create delays, errors, and an inability to make real-time cash decisions when they matter most. \n…"
tags: ["Amazon Bedrock", "Amazon Bedrock AgentCore", "Customer Solutions", "Intermediate (200)"]
orgs: ["Amazon"]
topics: ["agents & coding", "robotics & autonomy", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 1283
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Autonomous treasury agents: How Trovata built an AI-native solution on Amazon Bedrock and AgentCore

AWS Machine Learning Blog · Kushal Mangtani · 2026-11-10

Artificial Intelligence
Autonomous treasury agents: How Trovata built an AI-native solution on Amazon Bedrock and AgentCore
Corporate treasury teams face a persistent challenge: fragmented banking data scattered across dozens of bank portals, manual reporting trapped in spreadsheets, and legacy Treasury Management Systems (TMS) that can’t scale for modern enterprise needs. For treasury teams these manual processes create delays, errors, and an inability to make real-time cash decisions when they matter most.
Trovata is an AI-native cash and liquidity management platform with direct connections to over 10,000 banks, serving enterprises globally from a single cloud-based platform. In 2023, Trovata launched the first generative AI built specifically for treasury. Now, with Trovata’s latest AI-native updates, they’ve evolved from delivering insights to deploying autonomous agents that act on behalf of treasury teams.
Trovata’s customers have seen measurable results: $1M+ in annualized cost savings, over 5 hours per day saved per accounting team, a 77 percent reduction in annual TMS costs, and treasury reporting reduced from hours or days to under a minute.
In this post, we explore how Trovata built autonomous treasury agents on Amazon Bedrock and Amazon Bedrock AgentCore, the architecture secured with role-based access control (RBAC) that supports bank-branded AI deployment, and how agentic workflows are transforming corporate treasury from manual operations to real-time decision-making at enterprise scale.
Solution overview
Trovata operates as an AI-native treasury operating system, providing direct connections to over 10,000 banks through a single system for cash reporting, forecasting, analysis, and money movement.
Treasury teams today face a three-pressure problem:
- Fragmented banking data across multiple portals, requiring manual aggregation and reconciliation.
- Manual reporting and reconciliation consuming hours or even days of skilled team members’ time.
- Legacy TMS applications that lack cloud-native architecture and AI capabilities needed for modern operations.
Trovata’s evolution from its first generative AI for treasury in 2023 to its AI-native capabilities with autonomous agents represents a fundamental shift. The solution moves from static insights to persistent agentic workflows that operate continuously on behalf of treasury teams. Critically, Trovata AI is built directly into the treasury operating system. It’s not a generic chatbot layered on top, but embedded intelligence tied to real treasury objects with a governed path to automation through agents.
Trovata chose AWS for this transformation for three reasons. Its serverless, cloud-native infrastructure supports real-time execution, Amazon Bedrock provides large language model (LLM) inference for natural language queries and AI features, and Amazon Bedrock AgentCore handles agent orchestration with RBAC security, rapid deployment, and global scale.
The core AWS services powering Trovata’s AI-native solution include:
- Amazon Bedrock – LLM inference for natural language understanding and generation.
- Amazon Bedrock AgentCore – Agent orchestration, agentic workflows, and RBAC security.
- Serverless AWS infrastructure – Real-time execution at enterprise scale.
Architecture diagram
The Trovata AI architecture centers on autonomous treasury agents operating within a bank-branded, RBAC-secured framework. The solution comprises several key components working together:
- Trovata AI Chat – Natural language querying of multi-bank treasury data, so users can ask questions like “What was our net cash position across all accounts yesterday?” and receive instant, accurate responses.
- AI Insights – Automated anomaly detection, variance explanation, and trend analysis that surfaces critical information proactively.
- AI Agents – Persistent workflows running on schedules, triggers, or rules to monitor activity, explain variance, detect anomalies, and deliver updates automatically, without human intervention.
- Agent Builder-Configurator – A management console for building and configuring treasury agents, giving teams full control over agent behavior and scope.
- Enterprise RBAC – Role-based access control securing agentic workflows, making sure that agents operate within the same permission boundaries as human users.
Technical implementation
Trovata built its AI-native solution on Amazon Bedrock AgentCore, combining autonomous agents, natural language querying, and enterprise access controls. The following sections describe what the team built, the primary use cases, and the AgentCore capabilities behind it.
What Trovata built: AI-native solution
Trovata AI delivers autonomous treasury management agents embedded directly within the Trovata treasury operating system. These AI agents turn repeatable operational work into persistent workflows that run continuously. This is the work that consumes hours of skilled professionals’ time.
Agents operate on schedules, triggers, or rules to monitor activity, explain variance, detect anomalies, and deliver updates automatically. The entire system runs on Amazon Bedrock AgentCore, a secure, isolated environment purpose-built for enterprise AI. When a user asks a question, the AI retrieves data through Trovata’s own verified API layer, analyzes it, and presents the response within that secure infrastructure.
Primary use cases
- Cash forecasting – Automated cash flow forecasting across multi-bank environments with scenario modeling, replacing manual spreadsheet-based projections.
- Natural language querying – Enterprise users query bank data in plain English. For example: “What was our net cash position across all accounts yesterday?”.
- Anomaly detection – Real-time detection of unusual transactions, balance changes, or cash flow patterns that might indicate errors, fraud, or operational issues.
- Automated reconciliation – AI-powered reconciliation summaries across hundreds of accounts, reducing what previously took hours to seconds.
- Agentic workflows – Persistent agents that run autonomously by monitoring, analyzing, and reporting without human intervention on an ongoing basis.
Ten agent patterns from real customer deployments
Treasury teams have already started building AI agents in production. Trovata’s AI Agents Playbook provides a working library of ten agent patterns drawn from real customer deployments, covering the most common and high-value treasury workflows. Most treasury teams have 5–15 workflows that are ready for AI agents today.
AgentCore capabilities Trovata uses
Trovata’s implementation takes advantage of several key Amazon Bedrock AgentCore capabilities:
- Agent orchestration – Multi-step agentic workflows for complex treasury operations that require sequential reasoning and action.
- RBAC security – Role-based access control securing agent actions, making sure agents respect organizational permission boundaries.
- Real-time execution – Serverless infrastructure that delivers sub-minute treasury reporting across hundreds of bank accounts.
- Bank-branded deployment – Agents embedded within bank-branded tools, so banks can offer AI-powered treasury capabilities without needing to build AI themselves.
Security and governance architecture
Results
Key differentiators
Prerequisites
To explore a similar architecture, you will need:
- An AWS account with access to Amazon Bedrock and Amazon Bedrock AgentCore.
- Familiarity with treasury management operations (cash forecasting, reconciliation, multi-bank connectivity)
- Understanding of agentic AI architectures and enterprise RBAC models.
- Knowledge of financial services compliance requirements.
Cleanup
If you deployed any example resources while exploring this architecture, remember to delete them to avoid incurring future costs. Remove any Bedrock agents, AgentCore configurations, and associated infrastructure that were created for testing purposes.
Conclusion
Trovata’s journey from manual treasury operations to autonomous AI-powered treasury management demonstrates the transformative potential of agentic AI in financial services. With over $1M in annualized cost savings, over 5 hours per day saved per accounting team, a 77 percent reduction in annual TMS costs, and reporting reduced from hours or days to under a minute, the impact is measurable.
The bank-branded deployment model is especially effective. Banks and enterprises get production-ready AI without building it themselves. Trovata AI shows how, with Amazon Bedrock AgentCore, independent software vendors (ISVs) can embed governed, autonomous AI agents directly into vertical software as a service (SaaS) applications, delivering AI with the security and compliance-awareness that financial services demands.
Looking ahead, Trovata plans to expand its agent patterns, deepen enterprise resource planning (ERP) integrations, and extend global bank connectivity. The company continues to advance what autonomous treasury management can achieve.
Get started
- Trovata AI – Explore Trovata’s AI-powered treasury solution.
- Trovata AI Agents Playbook – Ten agent patterns from real customer deployments.
- Amazon Bedrock AgentCore – Learn about agent orchestration on AWS.
- Trovata on AWS Marketplace – Deploy Trovata from AWS Marketplace.
