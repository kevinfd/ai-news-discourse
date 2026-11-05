---
id: "b860dcb6054f0104"
title: "How Indegene is modernizing and scaling enterprise data quality in life sciences"
url: "https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences"
link: "https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-04T16:25:57Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Bhagyashree Chandak"]
language: "en"
summary: "This post is co-written with Shravan K S from Indegene Limited. \n Enterprise AI is creating new opportunities for life sciences organizations to improve decision-making across commercial, medical, market access, and other business functions. But the quality of every AI model, dashboard, and business insight depends on one thing: trusted data. As enterprise data grows across multiple platforms,…"
tags: ["Advanced (300)", "Customer Solutions"]
orgs: ["Amazon"]
topics: ["agents & coding", "health & science", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 2675
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How Indegene is modernizing and scaling enterprise data quality in life sciences

AWS Machine Learning Blog · Bhagyashree Chandak · 2026-11-04

Artificial Intelligence
How Indegene is modernizing and scaling enterprise data quality in life sciences
This post is co-written with Shravan K S from Indegene Limited.
Enterprise AI is creating new opportunities for life sciences organizations to improve decision-making across commercial, medical, market access, and other business functions. But the quality of every AI model, dashboard, and business insight depends on one thing: trusted data. As enterprise data grows across multiple platforms, pipelines, and business domains, maintaining consistent data quality has become increasingly difficult. Manual data quality rule creation, fragmented governance, and evolving business definitions make it challenging to scale data quality across the enterprise.
This post explores how Indegene built a production-grade, large language model (LLM) powered Data Quality Agent within its NEXT Unified Data Platform (NEXT UDP) on AWS. The agent generates context-aware data quality rules, validates them, and produces ready-to-run SQL and Python code under centralized, human-in-the-loop governance. Together, these capabilities help organizations improve data quality at enterprise scale while reducing the effort required to build and maintain data quality programs.
About Indegene
Indegene Limited (BSE: 544172, NSE: INDGN) is the strategic operating partner to the life sciences industry, orchestrating commercial, medical, R&D, and safety operations across the product lifecycle. Trusted by the world’s top 20 biopharma companies, Indegene helps run complex, highly regulated workflows at global scale. Indegene combines deep life sciences expertise with AI-embedded platforms and governed operating models to improve speed, consistency, and compliance across mission-critical operations. By integrating technology into how work is executed and scaled, Indegene helps life sciences organizations deliver measurable outcomes in regulated environments.
Why conventional data quality programs break down
Most organizations have established data quality processes but keeping them effective is becoming increasingly difficult as enterprise data ecosystems evolve.
One of the biggest challenges is the divide between technical and business rule ownership. Data engineers typically define technical rules that confirm whether data is structurally correct. For example, verifying that an HCP ID (Healthcare Professional ID) isn’t null, follows the required format, is unique, and maps to a valid reference record. Business teams define rules that determine whether the data makes sense in its operational context. For example, confirming that product market share totals 100 percent within a territory or that an HCP’s prescription activity aligns with their specialty and eligibility criteria. Because technical rules are often maintained in code while business rules reside in glossaries, SOPs, and subject-matter expertise, keeping them aligned and consistently governed across datasets and platforms becomes difficult.
Traditional validation techniques also have inherent limitations. Checks for null values, data types, uniqueness, or referential integrity remain essential, but they can’t capture business-specific context. Validating product hierarchies, customer segmentation, territory alignment, or commercial business rules requires domain knowledge that static validation logic can’t easily represent.
Creating and maintaining data quality rules is equally demanding. Every new dataset requires data profiling, rule definition, SQL development, validation, and ongoing maintenance. These rules are often spread across SQL scripts, pipeline code, spreadsheets, data catalogs, and tool-specific configurations. As schemas, business definitions, or validation thresholds change, the effort required to update and govern these rules grows significantly.
Additionally, the operational impact is significant. Onboarding new datasets becomes slower because many activities are repeated manually. Maintaining quality rules across hundreds of datasets consumes valuable engineering effort. Business users lose confidence when validation rules are difficult to understand, trace, or relate to business context.
As a result, data quality often becomes a periodic governance activity rather than a continuous, scalable capability.
Rethinking data quality with generative AI
Traditional data quality tools often operate as standalone capabilities, disconnected from the broader enterprise data ecosystem. As organizations scale AI and analytics, data quality needs to be embedded within the data platform itself, where governance, metadata, lineage, and analytics work together.
Indegene addresses this through the NEXT Unified Data Platform (NEXT UDP), a modern, AI-driven data platform built specifically for life sciences. NEXT UDP brings together fragmented commercial, medical, clinical, and enterprise data into a single, governed environment so organizations can manage the complete data lifecycle from ingestion to analytics. NEXT UDP provides several standalone AI agents, such as the Data Ingestion agent, Data Quality agent, Orchestration agent, Data Catalog agent, and SQL Bot Generator agent. You can use them standalone within your data pipelines or customize them further for agent-to-agent communication.
By integrating data ingestion, transformation, data quality, governance, metadata management, and analytics within a unified platform, NEXT UDP helps organizations:
- Consolidate fragmented enterprise data into a trusted source of truth.
- Standardize data quality and governance across business domains.
- Improve metadata visibility, lineage, and traceability.
- Reduce manual effort across data engineering workflows.
- Deliver trusted, AI-ready data for enterprise analytics and decision-making.
Indegene’s life sciences clients needed an agent that could run reliably in production and meet strict governance requirements, while giving the team flexibility in how they build it. Within NEXT UDP, Generative AI powers an intelligent Data Quality Agent that augments existing data quality processes. The agent boosts data engineer and data steward productivity by accelerating rule creation, simplifying validation, and helping maintain consistent governance at enterprise scale.
Indegene built the Data Quality Agent on a set of AWS services, with Amazon Bedrock, Strands Agents and Amazon Bedrock AgentCore at its core. Amazon Bedrock, provides a choice of foundation models (FMs), built on a foundation of security, privacy, and responsible AI controls. For life sciences organizations, this matters because their data often includes sensitive healthcare professional and patient information. Strands Agents streamlines building and updating the agent, and its evaluation tools help Indegene test rule accuracy, which is critical in regulated life sciences environments. The agent runs on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale, with any framework or model. The solution also inherits existing AWS security and audit controls, so Indegene can focus on data quality logic instead of agent infrastructure.
What makes the Data Quality Agent unique? Two knowledge bases that power context-aware data quality
Any data quality tool can check for null values, duplicates, or invalid data types. Services such as AWS Glue Data Quality, a capability of AWS Glue, already recommend rules like these from data statistics, and they remain a strong foundation. The harder problem is determining whether the data makes sense for its business purpose. To address this, the Data Quality Agent uses two complementary knowledge bases that combine curated domain knowledge with experience gained from governed usage.
The first is an Internal Enterprise knowledge base: It combines internal business glossaries, data dictionaries, SOPs, regulatory guidance, approved data quality rules, validated scripts, profiling results, historical anomalies, and subject matter expert (SME) feedback. Content is ingested, vectorized, and retrieved through Retrieval Augmented Generation (RAG) to generate data quality rules grounded in enterprise standards and proven outcomes.
The second is an External Reference knowledge base: It’s built and periodically updated using approved standardized data quality frameworks, web search, and controlled web-scraping. When a dataset is selected, the agent analyzes table and column metadata and retrieves relevant data quality standards, reference values, and validation best practices from trusted sources. For example, for an NPI (National Provider Identifier) column, it can identify applicable quality standards, recommend format (the required 10-digit numeric format) and perform reference-validation checks.
How it works
The Data Quality Agent takes users from data profiling to rule creation and governance in a single workflow:
- Select source: Connect to a supported source such as Amazon Redshift or Snowflake.
- Select database and schema: Browse the available tables, with the rule count and active rule status for each.
- Profile data: The solution computes quality metrics and column patterns for the table, which users review.
- Detect anomalies: The solution flags anomalies against historical baselines, and users review the total, critical, and warning issues and the affected records.
- Manage rules: Review a table’s existing rules or start creating new ones.
- Choose rule mode: Pick Column Level, Table Level, or Custom Query.
- Generate rule suggestions: The agent uses metadata, profiling results, anomalies, existing rules, and knowledge base context to recommend technical and business rules, each with a severity.
- Review, refine and apply: Users edit or approve each recommendation.
- Generate and validate code: The agent produces SQL and Python for approved rules, and a validation step checks them.
- Store in the central rule repository: Approved rules become available for execution, monitoring, and audit.
Solution architecture of the generative AI-powered Data Quality Agent on AWS
The following diagram shows the end-to-end architecture of the Data Quality Agent on the NEXT UDP platform, from the data steward request to rule execution.
Data stewards and data quality analysts call the solution from the Indegene application. The following table provides a walkthrough of the solution pipeline and lists the AWS services used for each layer. It also captures other options the solution supports, so you can adapt it to your data volumes, existing tools, and operational preferences.
How the Data Quality Agent builds context
Before recommending any validation rule, the Data Quality Agent assembles context from six distinct sources, each answering a different question about the data:
Together, these sources let the agent reason like an experienced data steward. Grounding every recommendation in what the data is, what the standards require, how the enterprise defines quality, and what has already been implemented.
What the solution does
The Data Quality Agent generates several categories of checks and keeps data stewards in control of the results.
Anomaly checks generation
The solution generates anomaly checks that catch values which are technically valid but don’t match how a pharmaceutical market behaves. These include negative switch percentages, market shares that don’t add up to 100 percent within a market, inconsistent drug rankings (for example, a drug ranked first with a lower share than the drug ranked second), rating values outside the defined scale, and panel sizes that are too small or don’t match the number of respondents.
Context-aware rule generation with RAG
The Data Quality Agent generates rule recommendations in three modes:
The Create New Quality Rule interface provides dedicated Column Level, Table Level, and Custom Query modes.
The platform supports both technical validation and business-specific quality checks.
For technical rules, the agent generates checks that confirm the data is structurally sound. These include null checks for mandatory fields, data type validation, range validation for numeric and date values, pattern validation for formatted fields such as identifiers and codes, duplicate detection, and referential integrity checks between related tables.
For business rules, the agent generates life sciences checks that confirm the data is consistent with how the business operates. These include account affiliation consistency (for example, a healthcare provider linked to the correct organization), segmentation logic, eligibility criteria, and market share and product share validation (for example, shares within a territory not exceeding 100%).
Real use-case example
Consider an HCP Product Performance table with the columns HCP_ID, Specialty, Territory_ID, Product_ID, Prescription_Volume, Market_Share_Pct, Switch_Pct, Rating_Scale, and Reporting_Month. Using the table profile and the two Knowledge Bases, this is how the Data Quality Agent generates and performs the following checks:
- Anomaly checks performed. 
         
  - Negative switch percentage.
  - Market share total mismatch.
  - Sudden increase or decrease in prescription volume.
  - Inconsistent product rankings.
  - Invalid rating-scale values.
- Technical rules generated. 
         
  - HCP_ID must not be null or duplicated.
  - Prescription_Volume must be numeric and non-negative.
  - Market_Share_Pct and Switch_Pct must be between 0 and 100.
  - Reporting_Month must follow the required date format.
  - Territory_ID and Product_ID must match their reference tables.
- Business rules generated. 
         
  - Market share across all products must total 100 percent for each territory and reporting month.
  - The HCP’s product eligibility must align with their specialty.
  - Only eligible HCPs can be included in the target segment.
AI-assisted severity recommendation
The solution recommends severity based on dataset context, rule type, and business impact. Severity categories help distinguish between:
- Critical issues, such as invalid commercial metrics, incorrect identifiers, or business rule violations.
- Basic validations, including schema conformance, null checks, and length validation.
- Complex validations involving advanced SQL logic, multi-column rules, or domain-specific business checks.
- Information: Validation conducted for awareness and transparency purposes only. No action is required unless concerns are identified.
SQL/Python code generation and ETL integration
After a rule is approved, the LLM generates the equivalent SQL, Python, and PySpark code. Before it’s stored, the code is validated automatically with syntax checks, a check against the target schema, and a test run on sample data where the language supports it. This means existing extract, transform, and load (ETL) and orchestration tools can run them as part of the current data pipelines.
AI-assisted validation
Using an LLM as a Validation Agent to review data quality (DQ) rules/scripts generated by another LLM for reducing hallucinations and improving governance. Further, Amazon Bedrock provides security, privacy, and responsible AI controls. Prompts and outputs aren’t used to train the models or shared with model providers. Amazon Bedrock is HIPAA eligible and in scope for compliance programs such as SOC, ISO and GDPR, which helps Indegene meet the requirements of its life sciences clients. Amazon Bedrock Guardrails adds configurable safeguards on model inputs and outputs. It detects and masks personally identifiable information (PII), blocks harmful content and prompt injection attacks, and uses contextual grounding checks to flag responses that aren’t supported by the retrieved knowledge.
Human oversight remains central
The Data Quality Agent is designed to augment existing data quality processes. Each generated rule receives a confidence score. Only high-confidence, low-risk rules are approved automatically, while critical and business rules always go to an SME for review. Every decision is recorded in the rule repository, so rule management stays governed, traceable, and aligned with enterprise standards.
Delivering operational impact and business value
In production, across Indegene’s deployments of NEXT UDP for life sciences clients, the Data Quality Agent has reduced the effort to define and implement data quality rules from about 30 hours to about 4 hours per dataset. That’s roughly 85 percent less effort, or about 7x higher productivity. Onboarding a new table now takes 2–4 hours instead of 2–5 working days. Data engineers and data stewards now spend their time reviewing and approving rules rather than writing them from scratch.
Key outcomes include:
- Less manual effort through AI-generated rules, SQL, and Python.
- Faster onboarding of new tables, schemas, and business domains.
- More consistent rules, grounded in approved standards, enterprise knowledge, and existing rules.
- Better collaboration between business and technical teams through the review, refine, and approve workflow.
- Earlier detection of data quality issues through automated profiling and anomaly detection.
Table 1: Performance and Scale
*Estimated from Indegene’s production deployments
Table 2: Rule quality and validation
*Estimated from Indegene’s production deployments
Table 3: Operational efficiency
*Estimated from Indegene’s production deployments
Table 4: Manual compared to agent-assisted data quality
*Estimated from Indegene’s production deployments
Looking ahead
As enterprise data ecosystems continue to grow, maintaining consistent and scalable data quality becomes increasingly difficult using manual rule creation and fragmented governance processes. Generative AI provides an opportunity to augment these workflows by accelerating rule generation, incorporating business context, and supporting governed decision-making.
The generative AI-powered Data Quality Agent within the NEXT Unified Data Platform demonstrates how large language models, RAG, and centralized rule governance can work together to simplify data quality management while keeping humans in control of review and approval. Future enhancements will continue to build on this foundation, including:
- AI-assisted remediation recommendations to help users resolve failed data quality checks.
- Root cause analysis to identify recurring anomaly patterns and support faster investigation of repeated data quality issues.
As these capabilities evolve, the focus remains the same: helping organizations improve data quality through AI-assisted automation while maintaining governance, transparency, and business oversight.
To learn more, refer to the following resources:
- Indegene in the life sciences space
- Generative AI in Healthcare & Life Sciences
- AWS Skill Builder course: Building Generative AI Applications Using Amazon Bedrock
- GitHub repo: Sample Healthcare and Life Sciences Agents on AWS
