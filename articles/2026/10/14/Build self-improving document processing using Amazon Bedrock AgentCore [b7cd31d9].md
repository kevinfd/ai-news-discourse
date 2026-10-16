---
id: "b7cd31d958bda34d"
title: "Build self-improving document processing using Amazon Bedrock AgentCore"
url: "https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore"
link: "https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-14T16:24:07Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Erik Cordsen"]
language: "en"
summary: "IDC research shows that document-related challenges cost organizations $19,732 for each information worker annually and reduce productivity by 21.3 percent. Organizations receiving invoices from hundreds of suppliers often face layouts that vary by issuer and change without notice. Template-based systems require constant maintenance at this scale. Staff can spend up to 30 percent of their time…"
tags: ["Amazon Bedrock AgentCore", "Expert (400)", "Technical How-to"]
orgs: ["Amazon", "Anthropic"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 2365
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Build self-improving document processing using Amazon Bedrock AgentCore

AWS Machine Learning Blog · Erik Cordsen · 2026-10-14

Artificial Intelligence
Build self-improving document processing using Amazon Bedrock AgentCore
IDC research shows that document-related challenges cost organizations $19,732 for each information worker annually and reduce productivity by 21.3 percent. Organizations receiving invoices from hundreds of suppliers often face layouts that vary by issuer and change without notice. Template-based systems require constant maintenance at this scale. Staff can spend up to 30 percent of their time on document-related tasks, and manual data entry error rates range from 1–4 percent. Conventional intelligent document processing (IDP) solutions address some of this burden, but they require extensive upfront configuration for each document format and break when layouts vary across vendors.
In this post, you learn how to build an agentic IDP system using Amazon Bedrock AgentCore that classifies, extracts, validates, and learns from business documents with minimal human intervention. Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. Your agents automatically handle new document formats, such as supplier invoices, purchase orders, insurance claims, and loan applications. By the end of this post, you can:
- Deploy a multi-agent IDP system, often in under 20 minutes.
- Process new document types without manual template configuration.
- Let agents train themselves on each new document format and reuse what they learn, so later documents of that type go straight to extraction without retraining.
Challenges with rule-based document processing
Many IDP pipelines require you to define templates, extraction rules, and validation logic for every document format upfront. When a new vendor sends a purchase order with a different layout, the pipeline breaks. This creates three core challenges:
- Template rigidity: Each new document format requires manual configuration, and even minor layout changes can cause extraction failures.
- No learning: The same extraction errors repeat across similar documents because the system doesn’t retain knowledge from previous corrections.
- Scaling burden: Each new vendor or document variant multiplies the maintenance effort, and organizations processing documents from hundreds of sources face ongoing operational costs.
An agentic approach addresses these challenges. Instead of static templates, AI agents analyze each document, generate extraction instructions, validate results, and learn from corrections automatically. Over time, your system builds a knowledge base of document formats, so you process similar documents with minimal additional configuration.
Solution overview
In this solution, eight specialized agents collaborate across two graph-based workflows running on Amazon Bedrock AgentCore.
The following diagram shows the multi-agent workflow graph built using Strands Agents, an open source SDK for building AI agents.
- Identification workflow: The Analyzer agent extracts text using Amazon Textract and identifies the document type and sender. The Matcher agent searches for similar documents using vector similarity in Amazon S3 Vectors, a capability of Amazon Simple Storage Service (Amazon S3).
- Training workflow (new document types): When no match is found, the Instructions agent generates extraction prompts, the Extractor agent extracts structured data, and the Validator agent checks results against schemas and business rules in Amazon Aurora DSQL. If validation fails, the Instructions Fixer agent refines the prompts and retries. On success, the Save Instructions agent persists the instructions for reuse.
- Automation workflow (known document types): When a match is found, the Extractor agent uses existing instructions. If validation fails, the Troubleshooter agent fixes the extracted data directly without modifying instructions.
How it works
The following diagram shows the infrastructure architecture for the solution.
- Business documents arrive in Amazon Simple Email Service (Amazon SES) or direct upload to Amazon S3.
- Amazon EventBridge triggers an AWS Lambda function that creates a tracking job in Amazon DynamoDB and invokes AgentCore runtime, a capability of Amazon Bedrock AgentCore.
- AgentCore runtime orchestrates document processing through Strands Agents.
- Your agents securely access AWS resources through machine-to-machine credentials managed by AgentCore Identity, a capability of Amazon Bedrock AgentCore, and Amazon Cognito.
- Your Lambda functions become agent-compatible tools through the Model Context Protocol (MCP) interface of AgentCore Gateway, a capability of Amazon Bedrock AgentCore.
- Agents extract text using Amazon Textract, classify documents using vector embeddings in S3 Vectors, and validate data against business rules in Aurora DSQL.
- Agents access enterprise data through MCP servers to validate extracted content against business rules.
- You monitor status and troubleshoot issues through a chat-enabled dashboard hosted on Amazon Elastic Container Service (Amazon ECS).
- You gain visibility into agent performance through AgentCore Observability, a capability of Amazon Bedrock AgentCore, and Amazon CloudWatch telemetry.
Deploy the solution
Follow these steps to deploy the solution infrastructure and web UI to your AWS account.
Prerequisites
To deploy this solution, you must have:
- An AWS account.
- Access to Amazon Bedrock with Amazon Nova and Anthropic (Claude) models enabled. For model availability by AWS Region, refer to Supported models by AWS Region in Amazon Bedrock.
- Access to Amazon Bedrock AgentCore (Runtime, Gateway, Identity), S3 Vectors, and Amazon Aurora DSQL in a supported Region.
- AWS Cloud Development Kit (AWS CDK) v2 installed.
- Docker installed and running (required for building and deploying container images).
- Python 3.11+ and Node.js 18+.
- AWS Identity and Access Management (IAM) permissions to create S3 buckets, Lambda functions, DynamoDB tables, Cognito user pools, Amazon Elastic Container Registry (Amazon ECR) repositories, and Amazon ECS services.
- Clone the repository and set up the environment:
- Deploy the stacks:
This deploys six AWS CloudFormation stacks: Core (S3, Cognito, DynamoDB), Gateway (Lambda tools, AgentCore Gateway), Aurora (Amazon Aurora DSQL), Agent (AgentCore runtime, containers), UI Orchestrator (API endpoints), and Modern UI (React app on Amazon CloudFront). Deployment takes approximately 15–20 minutes.
- Verify deployment by checking that each stack shows CREATE_COMPLETE in the CloudFormation console.
Process files and review results
After deployment, you receive an email with the CloudFront URL, username, and temporary password.
Process a document
- Sign in to the web UI and choose Process Document.
- Upload a sample purchase order from infrastructure/sample_data/purchase_orders/training/.
- The document enters the agent workflow: 
         
  - The Analyzer agent extracts text and identifies the sender and document type.
  - The Matcher agent searches for similar documents in the vector store.
  - For a new document type, the training workflow generates extraction instructions, extracts data, validates it, and saves the instructions for future use.
  - For a known document type, the automation workflow extracts data using existing instructions and validates it.
- Review results in the Review Jobs and Instructions tab to verify extracted data, validation results, and generated instructions.
Example: A new document type (training workflow)
Suppose you upload the first purchase order from a new retailer, Two Wheel Store. The Matcher agent searches the vector store, finds no similar document, and routes the job through the training workflow.
The Analyzer agent uses Amazon Textract to extract the raw document text:
The Instructions agent generates extraction prompts from the schema, and the Extractor agent produces structured JSON:
The Validator agent checks the result against the schema and fails:
The vendor’s SKU format (SB-004) doesn’t match Acme Bikes’ internal format (AB-SB-004). The Instructions Fixer agent diagnoses the mismatch and adds an explicit SKU transformation rule to the extraction prompt: prefix vendor SKUs with AB-. On the second pass, the seven line items validate successfully, and the Save Instructions agent persists the refined prompt to the vector store. End-to-end time for this first run: 3 minutes 49 seconds.
Example: A known document type (automation workflow)
When a second purchase order from Two Wheel Store arrives, the Matcher agent finds the stored instructions from the first run with a confidence score of 3.946 (threshold: 3.7) and routes the job through the automation workflow:
- The Extractor agent applies the stored instructions directly, so the orchestrator skips prompt generation. The SKU transformation rule learned during training applies automatically (EL-002 → AB-EL-002, HB-071 → AB-HB-071, PD-002 → AB-PD-002).
- The three line items validate on the first pass with an order total of $5,979.19.
- End-to-end processing completes in 1 minute 30 seconds, down from 3 minutes 49 seconds on the first run.
Use the interactive chat
The dashboard includes a chat interface for troubleshooting:
- Ask what tools do you have to see available agent capabilities.
- Ask list instructions to view stored extraction instructions.
- Ask what is the status of job XXXX to check processing progress.
- Ask what went wrong with job XXXX, how can we update the instructions? to diagnose failures.
Understand how accuracy improves over time
The system improves over time through two feedback loops:
- Training loop: When the Instructions Fixer agent refines extraction prompts after validation failures, the improved instructions are saved and reused for similar documents.
- Processing loop: When the Troubleshooter agent fixes extraction errors, it provides detailed analysis that helps identify patterns in document format variations.
When changing models, use AgentCore Evaluations, a capability of Amazon Bedrock AgentCore, to confirm that extraction quality remains acceptable. The solution already uses AgentCore Observability, so it has the required instrumentation.
Estimated cost
You pay only for what you use, because the solution runs on serverless and on-demand resources with no idle costs. For a workload of 10 training documents and 1,000 processed documents each month in US East (N. Virginia), the estimated cost is approximately $58 per month. Foundation model (FM) inference through Amazon Bedrock represents approximately 85 percent of the total cost, at roughly $0.055 per document. Actual cost depends largely on the models assigned to each agent. Model choices are centralized in agents/orchestratorgraph/utils/config.py, so you can use lower-cost models for simpler tasks and stronger models where needed. For detailed pricing, refer to the Amazon Bedrock pricing page.
Customize the solution for your use case
You get a purchase order processing use case with a synthetic bike company dataset, a pre-built JSON schema, and a validation Lambda function that checks extracted data against product and vendor records in a mock ERP database. To process your own documents, you must replace the included schemas and validation logic with your own.
Define your document schema
Create a JSON schema that defines the fields you want to extract for each document type. The sample purchase order schema in agents/orchestratorgraph/doc_schema/purchase_order_schema.json provides a reference. Your schema should specify field names, data types, and whether each field is explicitly stated in the document or inferred from context.
Build your validation process
The included validator checks purchase order data against synthetic vendor and product tables in Aurora DSQL. Your production implementation requires a validation process tailored to your business rules. For example:
- An invoice validator might check vendor IDs against your accounts payable system and verify line item totals match the invoice total.
- A contract validator might verify that the document contains required clauses and that dates and party names match your records.
- A claims validator might check policy numbers, coverage limits, and claimant information against your policy management system.
To add a new validator, create a Lambda function that accepts extracted JSON and returns a pass/fail result with detailed error messages, then register it as a tool in AgentCore Gateway. Refer to gateway/tools/po_validator_tool/ for the implementation pattern.
Update agent prompts
The agent prompts in agents/orchestratorgraph/prompts/ reference purchase order terminology. Update these prompts to reflect your document types and extraction requirements. The Orchestrator agent, Validator agent, and Instructions agent each contain document-type-specific language that you should adapt.
Best practices
Keep these recommendations in mind as you train and operate your agentic IDP system.
- Start with representative samples: Upload 5–10 documents per type during training, including edge cases with format variations, to build reliable extraction instructions.
- Use business rule validation: Connect validators to your reference data (vendor lists, product catalogs) in Aurora DSQL to catch extraction errors early.
- Monitor agent performance: Use AgentCore Observability and CloudWatch to track execution paths, identify bottlenecks, and measure extraction accuracy over time.
- Add document types incrementally: Create a JSON schema for each new document type and a corresponding validation Lambda function. The agents handle the rest.
- Add guardrails for production: Apply Amazon Bedrock Guardrails to enforce content filtering and grounding checks on agent outputs. This is especially important when you process sensitive document types such as insurance claims or loan applications.
- Review the OWASP Top 10 for LLMs: Consult the OWASP Top 10 for LLMs and Generative AI Apps for security considerations when building applications that use large language models (LLMs).
Clean up
Important: Before running cleanup, export the data you want to retain. The destroy.py script permanently deletes processed documents (S3), job history (DynamoDB), validation data (Aurora DSQL), and learned extraction instructions (vector store).
To avoid ongoing charges, remove the deployed resources:
Verify that the six CloudFormation stacks are deleted on the console: AgenticIDP-Core-Dev, AgenticIDP-Gateway-Dev, AgenticIDP-Aurora-Dev, AgenticIDP-Agent-Dev, AgenticIDP-UIOrchestr-Dev, and AgenticIDP-ModernUI-Dev.
Conclusion
In this post, you learned how to build a self-improving document processing system using Amazon Bedrock AgentCore, where specialized AI agents collaborate to classify, extract, validate, and learn from business documents. This agentic approach adapts to new document formats automatically and improves accuracy over time through feedback loops, replacing manual template configuration with autonomous learning.
As next steps:
- Deploy the sample solution and test with the included purchase order samples.
- Add your own document types by creating JSON schemas and validation rules.
- Explore how to integrate extracted data with downstream systems such as ERP, CRM, or content management tools.
To learn more about the services and patterns used in this post, refer to the following resources:
- For a deep dive into the agent framework used in this solution, refer to Strands Agents SDK: A technical deep dive into agent architectures and observability.
- To understand how AgentCore Gateway transforms APIs into agent-compatible tools, refer to Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development.
- For background on the Model Context Protocol and how it integrates with AWS services, refer to Unlocking the power of Model Context Protocol (MCP) on AWS.
- To learn how agents can retain context across sessions, refer to Amazon Bedrock AgentCore Memory: Building context-aware agents.
- For details on Amazon Bedrock AgentCore capabilities, refer to the Amazon Bedrock AgentCore documentation.
For expert guidance on building document processing solutions, AWS Professional Services and AWS Partners can help.
