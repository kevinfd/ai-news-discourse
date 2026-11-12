---
id: "0afd1907df33baa7"
title: "Accelerating generative AI delivery with reusable assets"
url: "https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-delivery-with-reusable-assets"
link: "https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-delivery-with-reusable-assets"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T19:19:21Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Sabine Khan"]
language: "en"
summary: "If you’re building generative AI solutions, reusable assets can help you stop rebuilding components that already exist: Retrieval Augmented Generation (RAG) pipelines, document processors, agent scaffolding, and so on. This has a compounding cost: time not spent solving the customer’s actual problem. \n This post shows you how to access a curated catalog of 23 production-ready assets from the AWS…"
tags: ["Amazon Bedrock", "Generative AI", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 2341
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Accelerating generative AI delivery with reusable assets

AWS Machine Learning Blog · Sabine Khan · 2026-11-11

Artificial Intelligence
Accelerating generative AI delivery with reusable assets
If you’re building generative AI solutions, reusable assets can help you stop rebuilding components that already exist: Retrieval Augmented Generation (RAG) pipelines, document processors, agent scaffolding, and so on. This has a compounding cost: time not spent solving the customer’s actual problem.
This post shows you how to access a curated catalog of 23 production-ready assets from the AWS Generative AI Innovation Center, now part of AWS Frontier AI Engineering & Services. These assets can reduce your development time from months to weeks, with evidence from companies like DoorDash, Lyft, and Ricoh.
Since 2023, the AWS Generative AI Innovation Center has published open source reusable assets. These production-grade building blocks give you a validated foundation to start from instead of a blank file. These assets have powered customer solutions delivering measurable results: 50x increases in testing capacity, 90 percent reductions in engineering hours, and deployment timelines compressed from months to weeks. In this post, you will learn why teams keep rebuilding generative AI components, what makes an asset truly reusable, how companies like DoorDash and Ricoh achieved measurable results by using these assets, and how to access and deploy 23 open source assets from the catalog. For a complete list of all available assets, see the asset catalog at the end of this post.
The problem: Why teams keep rebuilding
Three root causes drive redundant development across generative AI teams:
- No single source of truth – Assets scatter across repositories, wikis, and drives. Builders can’t find what exists, so they rebuild from scratch.
- No quality signal – Without verification of production readiness, security reviews, or maintenance status, builders have no way to trust existing solutions and default to writing their own code.
- No reuse culture – Sharing remains informal and ungoverned. What one team builds stays with that team, and problems get solved repeatedly.
The cost of rebuilding compounds. Each redundant build consumes engineering hours, delays customer delivery, and creates maintenance burden. Even AI-generated code requires production hardening, security reviews, testing at scale, and ongoing maintenance. These assets arrive already validated, security-reviewed, and production-grade, avoiding that verification burden. When teams finally reach production, they’ve spent weeks on undifferentiated heavy lifting, work that should have been reusable from day one. The AWS Frontier AI Engineering & Services resolves this challenge through reusable assets.
What a reusable asset actually is
A reusable asset isn’t a code snippet or a sample. It’s a production-grade, composable building block that implements a discrete generative AI capability. Reusable assets are validated for quality and security before publication. They include clear deployment guides for discoverability and are instrumented to track adoption across customer engagements. These assets are maintained across their lifecycle.
Examples from the catalog include RAG pipeline components, document ingestion modules, agent scaffolding templates, evaluation frameworks, and prompt management patterns. The assets are tested in production environments, reviewed for security compliance, and refined based on real customer feedback.
This is the difference between a one-off artifact and a building block you can trust.
Real results: Customer success stories
The value of reusable assets isn’t theoretical. Here’s what happens when teams build on proven foundations instead of starting from scratch.
Contact Center GenAI Agent: DoorDash and Lyft
According to the AWS case study, DoorDash built a fully voice-operated self-service generative AI contact center solution using the Contact Center GenAI Agent asset. As reported, the solution handles over 100,000 calls per day with 2.5-second response latency, achieving a 50x increase in testing capacity. Using Amazon Bedrock reduced development time by 50 percent. The team reached live testing readiness in 2 months.
Lyft used the same Contact Center GenAI Agent asset to bring agentic AI to life for riders and drivers, demonstrating the asset’s versatility across different customer engagement models.
The Contact Center GenAI Agent provides automated question answering capabilities for both text and voice channels. It employs a RAG architecture to facilitate multi-turn conversations while maintaining context. The solution integrates with Amazon Connect and uses Amazon Bedrock Knowledge Bases, a fully managed RAG capability, for hybrid search and metadata filtering.
Learn more:
GenAI Intelligent Document Processing: Ricoh
Ricoh serves major health insurance payers, managed care organizations, and healthcare providers. These customers process hundreds of thousands of critical documents each month, including insurance claims, grievances, appeals, and clinical records. As Ricoh scaled to serve more healthcare customers, they needed a standardized, multi-tenant document processing approach. That approach had to onboard new implementations without requiring unique development and tuning for each one.
Using the Accelerated Intelligent Document Processing on AWS asset as a foundation, Ricoh built a standardized, multi-tenant solution for automated document classification and extraction. This transformed their document processing from a custom-engineering bottleneck into a scalable, repeatable service.
Results: As documented in the published case study, Ricoh achieved a 7-fold throughput increase, from 10,000–70,000 documents monthly. Engineering hours per deployment dropped by over 90 percent (80 hours to under 5). Onboarding time fell from 4–6 weeks to 2–3 days. The system now processes 1,000 documents in minutes during traffic spikes, delivering over 1,900 potential annual person-hours in savings.
The GenAI IDP Accelerator, introduced in this 2025 blog post, is a scalable, serverless solution for automated document processing and information extraction using AWS services. This system combines optical character recognition (OCR) with generative AI to convert unstructured documents into structured data at scale. The AWS Frontier AI Engineering & Services continuously maintains the assets as well.
Learn more:
- Blog post: AWS GenAI Intelligent Document Processing (IDP) Accelerator
- Blog post: How Ricoh built a scalable intelligent document processing solution on AWS.
- Source Code: accelerated-intelligent-document-processing-on-aws
New assets: Building the future of agentic AI
Reusable assets become more valuable as teams shift focus from infrastructure to business logic. Two recently launched assets demonstrate how reusable building blocks can accelerate the development of next-generation agentic applications.
Fullstack AgentCore Solution Template (FAST)
The Fullstack AgentCore Solution Template (FAST) is a starter project repository. With FAST, you can quickly deploy a secured React frontend connected to Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale with any framework or model. In this implementation, FAST uses a React-based frontend with the managed infrastructure of AgentCore to accelerate building full-stack agentic applications from weeks to days.
FAST deploys in under 30 minutes using infrastructure as code (IaC), with built-in integrations for AgentCore memory, a capability of Amazon Bedrock AgentCore, along with Gateway, Code Interpreter, and Observability. Authentication uses Amazon Cognito, configured with enterprise security best practices, and the template is designed for AI-assisted development with extensive documentation and steering docs.
With FAST, you can access a complete reference architecture that shows you how the pieces integrate, with a working full stack application that you can learn from and build upon. With the modular design, you can swap out major components (identity providers, frontend frameworks, hosting solutions, or agent frameworks) as your requirements evolve.
Learn more:
- FullStack AgentCore Solution Template
- Accelerate agentic application development with a full-stack starter template for Amazon Bedrock AgentCore
Agentic Chatbot Accelerator
The Agentic Chatbot Accelerator is a web application deployment solution that uses the AWS Cloud Development Kit (AWS CDK) for infrastructure as code so you can create agentic chatbots. Built on Strands Agents and Amazon Bedrock AgentCore, this solution streamlines the development of agentic chatbot applications.
The accelerator provides rapid deployment using AWS CDK, with scalable agent runtime management through Strands Agents and Amazon Bedrock AgentCore. It is configurable and extensible for diverse chatbot use cases, with pre-configured patterns for authentication, hosting, and scaling, validated across customer deployments.
Learn more:
Walkthrough: Using an asset from the library
Let’s walk through a concrete example of selecting and using the Contact Center GenAI Agent asset from the open source catalog.
Prerequisites
To follow this walkthrough, you need:
- An AWS account with permissions to create AWS CloudFormation stacks, Amazon Connect instances, Amazon Bedrock resources, and Amazon Quick Sight dashboards.
- AWS Command Line Interface (AWS CLI) installed and configured with appropriate credentials.
- An Amazon Connect instance (or permissions to create one).
- Access to Anthropic Claude Sonnet and Anthropic Claude Haiku on Amazon Bedrock.
- A Jupyter notebook environment for validation testing.
The scenario
You’re building a customer support solution that needs to handle both voice and text interactions, answer questions using your company’s knowledge base, and escalate complex issues to human agents.
Finding the asset
Navigate to Contact Center GenAI Agent on GitHub. The README provides a clear overview of capabilities, architecture, and deployment steps. The following figure shows the solution architecture for the Contact Center GenAI Agent.
Evaluating the asset
The asset includes security-reviewed code with AWS CDK infrastructure as code, integration with Amazon Connect for voice and chat, and Amazon Bedrock Knowledge Bases, a fully managed RAG capability, for question answering. An automated testing framework and conversation analytics dashboard are built in.
Responsible-AI controls are integral to the architecture. Amazon Bedrock Guardrails enforces production-grade safety controls, including hallucination detection, content filtering, and topic-level boundaries, making sure agents operate within defined safety parameters from day one.
The repository shows active maintenance, comprehensive documentation, and links to customer success stories (DoorDash, Lyft) that validate production readiness.
Deploying the solution
Deployment follows four steps:
- Clone the repository and install dependencies.
- Deploy two AWS CloudFormation templates: one for the Knowledge Base stack and one for the RAG solution stack.
- Integrate with Amazon Connect using the pre-built contact flows included in the repository.
- Validate the deployment using the included Jupyter notebooks.
The full process takes under an hour. The solution also includes an Amazon Quick Sight dashboard for real-time conversation analytics.
For detailed deployment instructions and prerequisites, see the deployment guide.
Clean up
To avoid ongoing charges, delete the resources created during this walkthrough. The deployment uses two AWS CloudFormation stacks, so deletion follows the reverse order:
- Delete the RAG solution stack from the AWS CloudFormation console.
- Delete the Knowledge Base stack from the AWS CloudFormation console.
- Remove the Amazon Connect contact flows created during integration.
- Delete the Amazon Quick Sight dashboard and any associated SPICE datasets.
- For detailed cleanup instructions, see the deployment guide.
The outcome
Instead of spending weeks building a contact center solution from scratch, you can deploy a security-reviewed, tested foundation in days. Your team focuses on customizing the knowledge base, refining prompts for your domain, and integrating with your existing systems. This is the high-value work that differentiates your solution.
Potential time saved: 4–6 weeks of development time
What you focus on instead: Domain-specific customization, prompt engineering, business logic integration
Access to the AWS Generative AI Innovation Center open source assets
You can access 23 reusable assets as open source on GitHub and AWS Labs. Each asset includes deployment guides, sample code, and documentation to help you get started quickly.
Document processing and extraction
- GenAI Intelligent Document Processing (GenAIDP) – Scalable, serverless solution for automated document processing.
- Multi-lingual Document Processor (MDP) – Transforms complex multi-modal documents into structured text.
- Intelligent Document Processing with Generative AI – Extract information from custom documents.
- Extracting Information From Complex Documents – Hands-on workshop for document extraction.
- Semi-Structured Documents Automatic Pre-Labeling Tool – Automates pre-labeling for Amazon Comprehend.
Contact center and voice
- Contact Center GenAI Agent – Automated question answering for voice and text channels.
- Live Call Analytics with Agent Assist (LCA) – Real-time generative AI for customer and agent voice calls.
- Contact Center: Post Call Analytics (PCA) – Generative AI analysis of post-call recordings.
- Live Meeting Assistant (LMA) – Captures audio from browser-based meetings with transcription and insights.
- Recorded Voice Insight Extraction Webapp (ReVIEW) – Upload recordings and use generative AI to answer questions.
Agentic AI and chatbots
- Fullstack AgentCore Solution Template (FAST) – Deploy secured React frontend with AgentCore backend.
- Agentic Chatbot Accelerator – Web application deployment for agentic chatbots.
- Fashion Assistant Agent – Fashion assistant built with Amazon Titan on Amazon Bedrock AgentCore.
- Natural Language Database Agent – Query databases using natural language with LangGraph.
RAG and knowledge bases
- Deploy Amazon Bedrock Knowledge Bases using Terraform – Infrastructure as code for Knowledge Bases.
- Leveraging the User to Improve Agents in RAG Use Cases – Custom LangChain tool for conversational RAG.
- Reranker Fine-Tuning and Deployment – Fine-tune BAAI BGE Reranker for improved retrieval.
- Durable Semantic Caching in Amazon MemoryDB – Persistent semantic caching for GenAI applications.
Development and migration
- C to Java Code Conversion – Agentic workflow for legacy code migration.
- OpenAI Migration Framework – Systematic framework for large language model (LLM) migration.
- Fine-tuning ModernBERT for Intent Classification – Create smart LLM routing systems.
Infrastructure and operations
- Bedrock Logging Automation – Automate logging setup for Amazon Bedrock.
- Data Analyst BI – AI-powered business intelligence tool for non-experts.
To get started:
- Select one of the assets listed earlier.
- Review the README and deployment guides for assets relevant to your use case.
- Clone the repository and follow the deployment instructions.
- Customize the asset for your specific requirements.
- Reach out to the AWS Frontier AI Engineering & Services team for advisory support.
Conclusion
The cost of rebuilding is real, and it compounds. When teams rebuild RAG pipelines, recreate document processing logic, or start from scratch, those hours add up in engineering time that could have been spent solving actual customer problems.
A curated, validated asset catalog changes the economics of generative AI delivery. Not by doing the work for you, but by making sure you’re not doing work that’s already been done. The 23 open source assets published since 2023 represent thousands of engineering hours, dozens of customer engagements, and countless lessons learned. They’re packaged into building blocks you can deploy today.
The assets are open source. The deployment guides are comprehensive. The customer’s success stories are real. Start with one asset that matches your current challenge. For expert assistance, reach out to the AWS Generative AI Innovation Center.
