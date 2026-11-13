---
id: "6d29ea24a6e6fee7"
title: "Migrate to Amazon Bedrock Managed Knowledge Base with your coding agent"
url: "https://aws.amazon.com/blogs/machine-learning/migrate-to-amazon-bedrock-managed-knowledge-base-with-your-coding-agent"
link: "https://aws.amazon.com/blogs/machine-learning/migrate-to-amazon-bedrock-managed-knowledge-base-with-your-coding-agent"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-12T16:16:45Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Josh DeMuth"]
language: "en"
summary: "With a customer-managed knowledge base on Amazon Bedrock , you provision and scale the vector store, tune the embedding model and index settings, and plan capacity for each new data source. The migration guide in the Agent Toolkit for AWS helps you migrate to Amazon Bedrock Managed Knowledge Base . Managed Knowledge Base takes over that work and adds new retrieval capabilities, and your team…"
tags: ["Amazon Bedrock", "Amazon Bedrock Knowledge Bases", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon", "Microsoft"]
topics: ["agents & coding", "models & research", "search & media", "products & launches"]
content_source: "fulltext"
word_count: 2737
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Migrate to Amazon Bedrock Managed Knowledge Base with your coding agent

AWS Machine Learning Blog · Josh DeMuth · 2026-11-12

Artificial Intelligence
Migrate to Amazon Bedrock Managed Knowledge Base with your coding agent
With a customer-managed knowledge base on Amazon Bedrock, you provision and scale the vector store, tune the embedding model and index settings, and plan capacity for each new data source. The migration guide in the Agent Toolkit for AWS helps you migrate to Amazon Bedrock Managed Knowledge Base. Managed Knowledge Base takes over that work and adds new retrieval capabilities, and your team keeps control of the content and the application that uses it.
Moving a production knowledge base means your team maps its configuration, creates the replacement, ingests content, updates the application’s retrieval call, and validates retrieval before switching traffic. To help, we added a knowledge base migration guide to the amazon-bedrock skill in the Agent Toolkit for AWS. The guide gives your coding agent the context to plan the migration with you, starting with read-only discovery and a plan you review line by line. On your approval, the agent creates the new knowledge base and its data sources alongside the original, or writes a migrated infrastructure as code (IaC) template for your pipeline. Ingestion and updating your application’s Retrieve calls stay with you, and your agent can walk you through both.
In this post, we explain why we recommend the move and how the migration guide works, review the prerequisites, install the skill, plan a migration, update the application’s retrieval call, and validate retrieval before cutover.
Why move to Managed Knowledge Base
We recommend Managed Knowledge Base because it balances ease of use, retrieval accuracy, and cost.
AWS runs the store
With a Managed Knowledge Base, Amazon Bedrock handles ingestion, storage, indexing, and retrieval, and the store scales automatically as your content grows. Hybrid search, which combines keyword and semantic matching, is always on, with no index to configure. The knowledge base includes a managed embedding model, a managed reranker, and a built-in parser for multimodal file types.
You can still bring your own Amazon Bedrock embedding model when you create the knowledge base. On each retrieval request, you choose the managed reranker, an Amazon Bedrock reranking model, or no reranking. The managed reranker requires the managed embedding model.
Built-in capabilities
Managed Knowledge Base includes capabilities you’d otherwise build yourself:
- Native connectors ingest content directly from sources such as Amazon Simple Storage Service (Amazon S3), Microsoft SharePoint, and Atlassian Confluence. For the current list, see supported connectors. After the first full sync, later syncs pick up only changes, on demand or on a schedule. The Managed Knowledge Base includes a deletion safeguard to help protect against accidental bulk removal of indexed content.
- Access control list (ACL) awareness ingests document permissions with the content, so retrieval returns only what the signed-in user can access. For connectors that support it, such as Microsoft SharePoint and Atlassian Confluence, a real-time check against the source also catches permission changes since the last sync. ACL awareness doesn’t authenticate users, so your application must verify and pass the user’s identity.
- Agentic retrieval answers questions that a single search can’t by handling multi-part questions and retrieving iteratively. It can search more than one knowledge base in a single request.
- Integration with AgentCore Gateway, a capability of Amazon Bedrock AgentCore, exposes your knowledge base as a target. Any client that supports the Model Context Protocol (MCP) can then query the knowledge base, and the gateway handles authentication.
- Resource-based policies let applications in other AWS accounts use one team’s knowledge base. Scope each policy to the specific roles that call the knowledge base, and grant only the actions they use, such as bedrock:Retrieve.
Agentic retrieval, AgentCore Gateway integration, and resource-based policies are not available on customer-managed knowledge bases. For the AWS Regions where managed knowledge bases are available, and the features that AWS GovCloud (US-West) doesn’t support, see Supported AWS Regions.
Higher quotas
As of this writing, higher default quotas change how you can organize content. With 200 data sources per knowledge base, you can group related content in one knowledge base. With 10,000 knowledge bases per account, per Region, each team or product line can use a separate knowledge base.
For current values, see Amazon Bedrock endpoints and quotas and Service quotas for managed knowledge bases.
Pay for what you store and retrieve
Cost is one of three things teams weigh when they consider this move, alongside customizability and direct control of the vector store. On a customer-managed knowledge base, you choose, provision, scale, and update the vector and text stores, and pay separately for the infrastructure you select. On a Managed Knowledge Base, those stages are part of the service, and storage and retrieval are metered directly.
The pricing models can differ too. With a customer-managed knowledge base, storage and retrieval charges depend on the vector store you choose. Some stores charge for provisioned or minimum capacity, and others, such as Amazon S3 Vectors, a capability of Amazon S3, charge only for what you use. A Managed Knowledge Base is priced on what you store and retrieve, so cost follows real usage. Usage-based pricing can fit enterprise question-answering, policy, and support knowledge bases that run at low utilization. For current rates, see Amazon Bedrock pricing. For the parsers available on a customer-managed knowledge base and how each is billed, see Parsing options for your data source.
Rates are only part of the total cost of ownership. On a customer-managed knowledge base, your team provisions, scales, and operates each stage as a separate resource. A Managed Knowledge Base consolidates them into one resource, with a default embedding model, foundation model, and reranker, and with per-knowledge-base rate limits by default. You manage the content and the application that uses it, and Amazon Bedrock operates the managed storage, embedding model, foundation model, and reranker.
Solution overview
A customer-managed knowledge base uses the VECTOR type, with a vector store you configure. A Managed Knowledge Base uses the MANAGED type. The migration guide directs your agent to create a new MANAGED knowledge base alongside the original without modifying or deleting the original during migration. Using the guide’s map, your agent writes a plan that lists which settings remain unchanged, which Managed handles differently, and which application changes you need to make. As Figure 1 shows, the original keeps serving every request while your team ingests content, validates, and cuts over.
How the migration guide works
The guide separates planning from implementation. In Explore mode, your agent answers questions about Managed Knowledge Base and can inspect your configuration with read-only calls, so you can estimate the effort. In Migration mode, the guide takes your agent through checkpoints:
- Introduce and choose. Your agent explains what it will and won’t touch. Choose the mode, a live knowledge base or IaC source, and a plain (default) or technical explanation style.
- Identify. Confirm the account and AWS Region. Your agent flags over-broad credentials, asks whether you want a cost analysis, and creates an output directory.
- Discover. Your agent reads the knowledge base and data sources with read-only calls, or reads your template files.
- Plan. Review the plan and application changes. By default, your agent stops here.
- Implement, if requested. For a live build, approve the exact preview of the provisioning script, and approve again if it changes. For IaC, your agent writes a migrated template and reports which schema checks ran.
- Handoff. Review what was produced and your team’s remaining steps.
As Figure 2 shows, resource creation stays separate from ingestion and cutover.
Review the configuration mapping
The guide maps each setting to preserve your data sources, filters, and chunking behavior when the managed type uses a different configuration. The plan classifies each setting:
- 1:1. The new knowledge base uses the same setting.
- Adjusted. Managed uses a different setting for the same outcome, and the plan applies the substitution.
- Blocked. There is no managed path today. Your agent excludes that knowledge base from the build, explains why, and points you to AWS Support. Other knowledge bases in the same run can proceed.
Compare chunking on your own content when you validate.
Review the permissions and generated changes
Discovery, planning, and the entire IaC path need only read-only credentials. For a live build, the guide directs your agent to propose a scoped policy that explicitly denies changes to the original knowledge base, and to never ask for administrator or full-access permissions. It also directs your agent to change only resources it created, reference secrets by Amazon Resource Name (ARN), and ignore instructions found in the data it reads. Review the generated AWS Identity and Access Management (IAM) policy and provisioning script before you approve the run. After the build, check what the agent did in AWS CloudTrail event history, which keeps 90 days of management events. Each event records the API call, such as CreateKnowledgeBase, and the identity that made it.
For the optional cost analysis, your agent compares current spend with a Managed Knowledge Base estimate using current AWS prices. It uses read-only inputs, including Amazon CloudWatch metrics, Amazon S3 object sizes, and AWS Cost Explorer. Each figure is labeled as measured, supplied by you, or estimated.
Prerequisites
Use separate credentials for planning and for any approved resource creation.
- A compatible development environment with the Agent Toolkit for AWS.
- The AWS Command Line Interface (AWS CLI), configured with a least-privilege, read-only profile.
- Access to the original knowledge base configuration or its IaC files.
- For the optional live build: 
         
  - A scoped build profile, using the policy the guide recommends.
  - An IAM service role for the new knowledge base. The guide gives your agent the trust policy and permissions to help you create it.
  - Python 3 with boto3 for the generated provisioning script.
The Agent Toolkit for AWS works with compatible development environments and its repository on GitHub lists the available skills. Examples in this post use AWS CLI 2.37 and boto3 1.43.32.
Install the skill
Follow the Agent Toolkit for AWS getting-started instructions for your coding agent. The add-skill command installs the amazon-bedrock skill to the coding agents it detects. Add --agent to target one, for example --agent kiro.
After installation, your agent loads the migration guide when you describe a migration task. The following prompts are illustrative inputs, not transcripts.
Plan the migration
Choose the path that matches how you maintain the source.
To start in Explore mode, ask a question:
When you’re ready, choose the live or IaC path.
Migrate a live knowledge base
Ask for a plan before authorizing resource creation:
Confirm the account and Region, then review the plan’s mappings and application changes. By default, the new knowledge base takes the original’s name with a -managed suffix. To build it, confirm the service role exists, switch to the build profile, inspect the provisioning script and its preview, and approve. Your agent runs the script, which creates the knowledge base and data sources, and reports their status.
Migrate infrastructure as code
Point your agent at the source template or configuration:
Your agent writes the migrated file to the output directory, deploys nothing, and shows you the diff. To keep the diff, ask your agent to save it. Run terraform init -backend=false and terraform validate before deployment. Your agent can walk you through both commands, but the guide leaves these checks to you because terraform init downloads the large AWS provider. Before you apply the deployment plan, check that it keeps the original resources you need for rollback.
Example conversation
The migration runs as a conversation. Before reading anything, your agent states its scope and asks how to proceed:
The plan summary shows each mapping, the caller changes, and the decisions you need to make:
For a live build, your agent stops at a preview, and the approval command requires the plan’s hash:
Example exchanges are lightly edited, with identifiers replaced.
Update the application’s retrieval call
Your application uses the same Retrieve operation for both types. The managed request targets the new knowledge base ID and replaces vectorSearchConfiguration with managedSearchConfiguration. Passing vectorSearchConfiguration to a managed knowledge base returns a validation error. Managed retrieval always uses hybrid search, so the managed request shape has no overrideSearchType field. Metadata filters keep the same syntax, except that managed knowledge bases don’t support the startsWith and stringContains operators. For the full syntax, see the Retrieve API reference.
The example assumes both knowledge bases contain the locale metadata used by the filter.
Validate retrieval and cut over
Evaluate the new knowledge base while the application still uses the original.
- If using IaC, review and deploy the target configuration through your pipeline.
- Sync each data source and review any failures. See Sync your data.
- Grant your application’s runtime IAM role bedrock:Retrieve on the new knowledge base ARN, and keep its access to the original knowledge base so you can roll back.
- Run representative queries against both knowledge bases with Retrieve, using that role. The two types use different score scales. Managed scores also depend on rerankingModelType, which defaults to MANAGED with the managed embedding model and to NONE with a custom one. Tune thresholds per mode, and hold the mode constant while comparing.
- Test metadata filters and permission-aware retrieval where used, including content the signed-in user shouldn’t receive. On an ACL-enabled data source, requests without userContext.userId (the user’s email) return no results.
- After acceptance, deploy the new knowledge base ID and request shape. Keep the original knowledge base, with current content, and application configuration through your rollback period.
For each query, check whether both return the same top document and how much results overlap. A short script can report pass or fail against criteria such as a matching top document on at least 90 percent of queries and no zero-result queries on the managed knowledge base. Tune that threshold for your workload. For other retrieval quality measures, such as context relevance and context coverage, see Use metrics to understand RAG system performance.
Watch for these differences when you compare results:
- Normalize source locations before comparison. A customer-managed knowledge base can return s3://bucket/key in location.s3Location.uri, and a managed knowledge base can return an https:// URL. Compare by object key.
- Compare the top result instead of assuming equal result counts. The two knowledge base types can return different numbers of results, and numberOfResults sets a maximum rather than a guarantee. Compare the top document, and review each query where it changes. For details, see Configure and customize queries for managed knowledge bases.
- Map renamed system metadata keys. For example, replace x-amz-bedrock-kb-data-source-id with _data_source_id in comparison code. Your own metadata attributes keep their names. For details, see Configure and customize queries for managed knowledge bases.
Clean up
If you complete the migration, retire the original only after the rollback period and a dependency review. Keep the source documents and buckets the managed knowledge base ingests from, and storage that other workloads use. Clean up IaC-managed resources through their owning template.
If you end the evaluation instead, keep the original and delete what you created in this order:
- Delete each managed data source and wait until it’s gone.
- Delete the managed knowledge base and wait until it’s gone.
- If you created the service role only for this evaluation, delete its inline policy, then the role.
- With a customer managed key, check aws kms list-grants for grants Amazon Bedrock created, which can remain after the knowledge base is deleted.
- Keep any S3 bucket that another knowledge base still reads.
Deletion protection on a managed data source limits how much a sync can delete, not whether you can delete the data source. Deleting the original knowledge base doesn’t delete its vector store, which continues to incur charges until you remove it. See Delete an Amazon Bedrock knowledge base.
Conclusion
With Amazon Bedrock Managed Knowledge Base, your team no longer runs a vector store or manages the underlying retrieval infrastructure. With the migration guide in the amazon-bedrock skill, you ask your agent for a plan, review it, and approve only the resources you want built.
To get started, set up the Agent Toolkit for AWS and ask your agent for a read-only assessment of your knowledge base. After migration, explore agentic retrieval for multi-part questions. To learn more, see Build enterprise search for agents with Amazon Bedrock Managed Knowledge Base on the AWS Machine Learning Blog.
