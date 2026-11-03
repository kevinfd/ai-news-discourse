---
id: "195c284d0de53e7f"
title: "Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI"
url: "https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai"
link: "https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-02T17:11:21Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Daxeshkumar Patel"]
language: "en"
summary: "When you build Retrieval Augmented Generation (RAG) applications, answer quality depends on the data that you ingest. Amazon Bedrock Knowledge Bases is the fully managed RAG capability of Amazon Bedrock. With Amazon Bedrock Managed Knowledge Base , you connect your data sources, and Amazon Bedrock manages ingestion, storage, indexing, and retrieval for you. You don’t provision or scale a vector…"
tags: ["Advanced (300)", "Amazon Bedrock Knowledge Bases", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 3788
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI

AWS Machine Learning Blog · Daxeshkumar Patel · 2026-11-02

Artificial Intelligence
Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI
When you build Retrieval Augmented Generation (RAG) applications, answer quality depends on the data that you ingest. Amazon Bedrock Knowledge Bases is the fully managed RAG capability of Amazon Bedrock. With Amazon Bedrock Managed Knowledge Base, you connect your data sources, and Amazon Bedrock manages ingestion, storage, indexing, and retrieval for you. You don’t provision or scale a vector store, and embedding and reranking use service-managed models by default.
For web content, start with the Amazon Bedrock Web Crawler data source connector for managed knowledge bases. You give it the seed URLs or sitemaps that you’re authorized to crawl, and it crawls within the scope and rate limits that you set. Scheduled syncs keep your knowledge base current as pages change, and the connector can wait for content that loads with JavaScript. There’s no crawler for you to build, host, or operate, so this connector is the starting point for most public website content.
Some sources need more control over what reaches the knowledge base. You might want to index only the main content region of each page, remove navigation and other boilerplate, or attach your own metadata attributes to every document. For that class of source material, you can extend the reach of your knowledge base with a preparation step built with Crawl4AI, an open source Python crawler. The step writes Markdown and a metadata sidecar for each page to Amazon Simple Storage Service (Amazon S3), and the knowledge base ingests both through its Amazon S3 data source.
In this post, we show you how to choose the appropriate web ingestion path and implement custom preparation for content that needs additional processing. You then start ingestion into a managed knowledge base and validate retrieval quality. The companion aws-samples repository provides the complete workflow as a sample implementation.
This is batch ingestion of known web properties, not real-time web access at inference time such as Web Grounding with Amazon Nova.
Solution overview
Start with the Amazon Bedrock Web Crawler when it can reach and index the pages you need. It respects robots.txt, and after the first full crawl, each sync captures only added, updated, and deleted content.
Use the Crawl4AI preparation path when public source material needs one or more of the following before ingestion:
- Structured Markdown preparation: Use DefaultMarkdownGenerator with a pruning content filter to reduce navigation and other boilerplate while preserving headings, lists, and tables. Because pruning is heuristic, review representative output from your sites.
- Bounded, targeted extraction: Extract only the page region that an optional CSS selector matches. Constrain breadth-first traversal by seed origin, page/path/host scope, depth and page caps, and URL patterns.
- Custom metadata: Attach source URLs, crawl timestamps, content type, and your own attributes to each document, so that you can filter retrieval results on them.
Because managed and customer-managed knowledge bases both support Amazon S3 data sources, the Crawl4AI path works with either type. This post uses a managed knowledge base and notes where a customer-managed knowledge base differs.
The rest of this post follows the companion sample. Treat its architecture and defaults as a starting point, not as requirements of Amazon Bedrock Knowledge Bases.
By default, the sample runs the AWS Fargate task in a public subnet, where it reaches your configured websites through an internet gateway. Crawl4AI’s role ends once it has prepared the source documents and metadata sidecars. From ingestion onward, Amazon Bedrock Knowledge Bases handles parsing, chunking, embedding, indexing, and retrieval. The following diagram shows the Crawl4AI path from the schedule through to retrieval.
The numbered steps in the diagram map to the following workflow:
- Amazon EventBridge starts the Amazon Elastic Container Service (Amazon ECS) task on AWS Fargate on the configured schedule.
- The task crawls the public websites you configured and prepares Markdown with a metadata sidecar for each page.
- The task uploads the prepared files to the Amazon S3 bucket that backs the knowledge base data source.
- The task starts an Amazon Bedrock Knowledge Bases ingestion job.
- Amazon Bedrock Knowledge Bases reads the new and changed objects, parses them, and applies the chunking strategy you selected.
- It creates embeddings and indexes them in the knowledge base’s vector store, which Amazon Bedrock manages for a managed knowledge base.
- Your generative AI application queries the knowledge base for relevant chunks or for a generated response with citations.
The task reads its non-secret pipeline configuration from AWS Systems Manager Parameter Store at startup.
The workflow processes public pages only and doesn’t implement authenticated sessions. For sites that require sign-in, evaluate the Amazon Bedrock Web Crawler authentication options first, which include basic, form-based, and SAML authentication. Extending the sample with authentication requires session handling, credentials in AWS Secrets Manager, and a security review.
How the workflow works
The AWS Cloud Development Kit (AWS CDK) app packages the implementation in a container image during deployment. When the schedule fires, the container runs scripts/container_entrypoint.py and executes crawl, upload, and ingestion in sequence. The following three steps explain the core logic.
Step 1: Crawl and extract content
The crawl step performs bounded crawling and writes a Markdown file with a metadata sidecar for each successfully prepared page. The following excerpt is simplified. The module src/crawl4ai_bedrock_kb/crawl.py contains the complete seed pacing, URL filtering and scoping, page limits, and redirect checks:
Amazon Bedrock Knowledge Bases supports several document formats for Amazon S3 data sources, including plain text, HTML, Markdown, PDF, and DOCX. The workflow writes Markdown because it preserves headings, lists, and tables without carrying all raw HTML into ingestion.
Step 2: Upload to Amazon S3
The upload step sends each prepared Markdown document and its matching metadata sidecar to the configured S3 bucket, under the workflow’s s3Prefix. For page.md, the sidecar must be named page.md.metadata.json, the complete source filename with .metadata.json appended. The workflow stores each sidecar in the same S3 location as its document. Amazon Bedrock limits each metadata sidecar to 10 KB. If a sidecar would exceed that limit, the run stops with an error before it writes either file.
Each attribute in the sidecar uses the typed format that both managed and customer-managed knowledge bases accept for Amazon S3 data sources. The following abbreviated sidecar, formatted for readability, shows three of the attributes that the workflow writes:
The pipeline uploads only the paths produced by the current crawl, so stale local files are not sent.
Step 3: Let Amazon Bedrock Knowledge Bases chunk, embed, and index
After content is in S3, an ingestion job hands each document to the data source’s ingestion pipeline. By default, a managed knowledge base parses each file with its managed parser, which automatically selects a parsing approach for your content. You select the chunking strategy when you connect the data source. You can’t change it afterward, so evaluate the options before you create a production data source. A managed knowledge base offers the following chunking strategies:
- Default chunking uses fixed-size chunks of 300 tokens with 20 percent overlap.
- Fixed-size chunking splits content by a maximum token count and an overlap percentage that you set.
- No chunking treats each file as a single chunk, for content that you have already split.
Chunk boundaries and retrieval results depend on the content and the selected strategy, so compare the options with representative pages and evaluation questions. To change strategies later, create a new data source. For more information, see Customize ingestion for a data source. A customer-managed knowledge base also offers semantic and hierarchical chunking and additional parsing options. For details, see How content chunking works for knowledge bases.
The workflow then starts an ingestion job so the knowledge base processes the new documents. The following simplified excerpt from src/crawl4ai_bedrock_kb/ingest.py shows the call:
The same StartIngestionJob and GetIngestionJob calls work for both knowledge base types, and you can also monitor progress on the console.
Deploy the solution
In this section, you deploy the workflow into your AWS account with AWS CDK. Only the knowledge base prerequisites differ between the two knowledge base types. When you’re finished, follow the steps in the Clean up section to remove the resources.
Prerequisites
Before you start, make sure that you have:
- An AWS account.
- One of the following knowledge bases: 
         
  - A managed knowledge base, which this post uses, in an AWS Region where managed knowledge bases are available. For instructions, see Create a managed knowledge base and the Amazon S3 connector. On the data source, leave Metadata files prefix empty, because the workflow writes each metadata sidecar alongside its document.
  - An existing customer-managed knowledge base. To add an Amazon S3 data source, see Connect to Amazon S3 for your knowledge base. The workflow writes a metadata sidecar for every document, so confirm that your vector store can store and filter those attributes, as described in Metadata and filtering. For example, an Amazon OpenSearch Serverless vector index must use the faiss engine. An Amazon Aurora vector index needs a custom metadata column or a column for each metadata attribute. With Amazon S3 Vectors, a capability of Amazon S3, you can attach up to 1 KB of custom metadata to each vector, so keep attributes that you add short.
- An Amazon S3 data source in that knowledge base whose status is AVAILABLE. It can be a new data source or one you already use. It must use the S3 bucket that you configure for this workflow. If the data source filters content by prefix or file pattern, the filters must allow the files that the workflow writes under its s3Prefix (default web-content/).
- The knowledge base, the S3 bucket, and the stack you deploy all in one Region.
- Authorization to crawl the public websites you configure.
- A deployment workstation with Git, Python 3.10 or later, Node.js, the AWS Command Line Interface (AWS CLI) version 2, the AWS CDK CLI v2, and a running Docker-compatible container engine. The deployment guide lists the minimum AWS CDK CLI version.
- AWS credentials configured on the deployment workstation with permission to bootstrap the target environment and deploy the CDK stack.
- A bootstrapped CDK environment in the target account and Region. The deployment steps include the bootstrap command.
You need the workstation only to build and deploy. After deployment, the schedule runs the task in AWS.
Deploy the scheduled workflow
Clone the companion repository and install the deployment dependencies:
Keep Docker running. Set AWS_DEFAULT_REGION to your knowledge base’s Region first, because cdk deploy uses the Region from your environment or AWS profile, not the one in the bootstrap command. Bootstrap the target account and Region once, if needed. Then deploy the stack with your knowledge base, data source, S3 bucket, and authorized seed URLs:
Replace every example value, including ACCOUNT_ID, REGION, and the four required context keys, with your own. The example values are syntactically valid, so an unedited command deploys a stack that points at a bucket you don’t own. You can also set these keys in cdk.json.
The maxDepth and maxPages values limit the first crawl to one link level and 25 pages. Raise them after you review the prepared output. To preview which pages a crawl prepares, you can also run the pipeline locally with --dry-run, as described in the README. The stack name is fixed, so another cdk deploy in the same account and Region updates this stack.
The sample builds an ARM64 container image by default. If Docker on your x86_64 workstation can’t build ARM64 images, add -c cpuArchitecture=X86_64 to the cdk deploy command.
If your account turns on VPC Block Public Access, the task can’t reach the internet from the default public subnet. To check the mode, run aws ec2 describe-vpc-block-public-access-options. In ingress-only mode, deploy with -c egressMode=nat, which adds a NAT gateway with hourly charges. Bidirectional mode also needs an exclusion, as the deployment guide describes.
The stack doesn’t create or change your knowledge base or data source.
With the default rate(24 hours) schedule, the first run starts when the deployment creates the Amazon EventBridge rule. To follow that run, use the command in the TailLogsCommand output, which cdk deploy prints when it finishes. A successful run logs job_status: COMPLETE. To start another run outside the schedule, use the command in the RunTaskCommand output after the current run finishes. To list the outputs later, run aws cloudformation describe-stacks --stack-name Crawl4aiBedrockKbCrawler --region REGION --query "Stacks[0].Outputs".
The deployment guide covers the remaining configuration, including crawl boundaries, the schedule, networking, container architecture, monitoring, and on-demand runs.
Validate retrieval quality
After ingestion, test representative questions with Retrieve before you add generation. A managed knowledge base uses hybrid search. When it uses the default managed embedding model, it also reranks results with its managed reranker. You can narrow results with the metadata from the sidecars. The sample’s default configuration adds content_category set to web to every page. The following example returns up to five chunks from those pages that were crawled in the last seven days. It requires the AWS SDK for Python (Boto3) 1.43.32 or later, which you can install with python -m pip install "boto3>=1.43.32". Replace the Region and knowledge base ID with your own values:
The example passes an integer timestamp, which both knowledge base types accept in number filters. A managed knowledge base doesn’t support the startsWith and stringContains filters. For a customer-managed knowledge base, pass the same filter in vectorSearchConfiguration instead of managedSearchConfiguration. The operators it supports depend on its vector store.
Metadata filtering can improve retrieval precision, but it is not an authorization boundary. If different users should see different pages, the Amazon S3 connector for managed knowledge bases supports document-level access control with access control list (ACL) files that you provide. The sample doesn’t create ACL files.
To generate responses from a managed knowledge base, use agentic retrieval. The AgenticRetrieveStream operation returns the retrieved results and a generated response with citations to those results. For a customer-managed knowledge base, use RetrieveAndGenerate. In both cases, each cited result includes the source_url metadata from its sidecar, which your application can present as the user-facing source.
Evaluate retrieval relevance, source-page coverage, and citation quality whenever you change content preparation, chunking, or retrieval settings. For the retrieval settings that you can tune, see Configure and customize queries for managed knowledge bases.
Running it repeatedly
Each scheduled event launches one standalone Fargate task. The stack doesn’t prevent overlapping runs, so choose an interval longer than the expected crawl and ingestion duration. A failed run isn’t announced, because the sample adds no retry policy, dead-letter queue, or alarm. An ingestion job can also report COMPLETE when some documents fail to ingest, and the task then exits with code 0. The task logs the job’s failure reasons. Add the monitoring you need, including an alarm on those failure reasons, before you rely on the schedule.
Each run incurs Fargate charges for the configured task size, which defaults to 2 vCPU and 4 GB. The task keeps running while it polls the ingestion job for up to 30 minutes, so a slow ingestion job extends billable task time. If ingestion takes longer, the task exits with a nonzero code, and the ingestion job keeps running. The stack turns on Container Insights for the cluster, and flow logs for an Amazon Virtual Private Cloud (Amazon VPC) that it creates. Both add Amazon CloudWatch charges. The stack’s AWS KMS key has a monthly charge, and the task’s public IPv4 address is billed while the task runs. With egressMode=nat or privateEndpoints=true, the NAT gateway and interface endpoints are billed hourly, even when no task is running. Knowledge base usage is billed separately. For details, see Amazon VPC pricing and Amazon Bedrock pricing.
Uploads are additive: removing a URL or missing a page during a later crawl doesn’t delete its existing S3 objects. To remove stale content, delete the obsolete document and matching sidecar under the configured prefix, then start ingestion again. If you turn on the document deletion safeguard (deletion protection) for a managed knowledge base data source, check its threshold. A sync that would delete more than that percentage of documents skips its delete phase, so those documents stay indexed. To start ingestion automatically whenever objects in the bucket change, see Build and deploy an automatic sync solution for Amazon Bedrock Knowledge Bases.
Responsible AI considerations
Retrieved passages become the context that a foundation model uses to generate a response. Apply the following controls before you run this workflow in production:
- Amazon Bedrock Guardrails: Attach a guardrail to your agentic retrieval or RetrieveAndGenerate requests to apply content filters, denied topics, word filters, and sensitive information filters. Agentic retrieval supports only the guardrail BLOCK action, not MASK.
- Contextual grounding checks: Turn on the Guardrails contextual grounding check to score each response for grounding against the retrieved passages and for relevance to the query. The guardrail blocks responses that score below the thresholds you set. For agentic retrieval, you can run the check on the generated answer with the ApplyGuardrail API. The check supports question answering and summarization, not conversational chatbot use cases.
- Treat crawled content as untrusted input: Prepared web pages become model context, so text on a public page can attempt prompt injection through retrieval. Don’t rely on guardrails alone to catch it. Restrict seed URLs to sites you trust, and apply the ingestion filtering patterns described in the next section before content reaches the knowledge base.
- Citations and human review: Return citations with every generated response so users can verify claims against the source page. For higher-risk use cases, keep a human reviewer in the loop.
Security and compliance considerations
Review the following considerations before you run this workflow against production content:
- Use trusted public crawl targets: Seed URLs and crawl settings are deployment configuration, and the Fargate task allows outbound access so it can reach public websites. In the sample’s default networking mode, the task runs in a public subnet with a public IP. Configure only authorized public sites. Don’t use this sample to crawl private or internal endpoints. Review network egress and destination controls before adapting the workflow for other trust models.
- Respect crawl directives: The workflow turns on Crawl4AI’s robots.txt check by default, and the CDK path pins it on with no context key to disable it. Verify you have authorization to crawl the target sites, consistent with the AWS Acceptable Use Policy.
- Rate limiting: Configure delays between requests to avoid overwhelming source websites.
- Encryption at rest: The stack creates an AWS Key Management Service (AWS KMS) customer managed key with automatic key rotation and encrypts its CloudWatch log groups with it. Amazon S3 encrypts new objects with server-side encryption with Amazon S3 managed keys (SSE-S3) by default. If your data classification requires a customer managed key for the bucket, configure the bucket to use it. Then grant the uploader and the knowledge base service role the required AWS KMS permissions in both AWS Identity and Access Management (IAM) and the key policy. The stack’s task role doesn’t include AWS KMS permissions. A managed knowledge base encrypts its data with an AWS owned key by default, or with a customer managed key that you specify when you create it. For a customer-managed knowledge base, review encryption for its vector store.
- Least privilege IAM: The CDK stack grants the Fargate task role s3:PutObject on the configured bucket prefix. It also grants bedrock:StartIngestionJob and bedrock:GetIngestionJob on the target knowledge base, plus ssm:GetParameter for its single configuration parameter. Separate roles cover Amazon EventBridge task launch and the standard container image pull and log delivery. The pipeline doesn’t read or list S3 and doesn’t call InvokeModel or Retrieve.
- Container and template checks: The container runs as a non-root user, and the CDK app runs cdk-nag AWS Solutions checks on every synthesis with resource-scoped suppressions.
- Protect deployment configuration: The CDK app stores non-secret pipeline settings in a plaintext Parameter Store String parameter. Only the parameter name is placed in the task definition. Don’t put passwords, cookies, tokens, or other secrets in CDK context or this parameter.
- Ingestion pipeline security: See Securing the RAG ingestion pipeline: Filtering mechanisms for filtering and validation patterns to apply before content reaches the knowledge base.
Clean up
To avoid ongoing charges, delete the resources created during this walkthrough:
- From the repository’s deploy/ directory, run cdk destroy in the same Region, with the same four required -c values that you passed to cdk deploy. The app checks them on every command. This removes the stack’s Amazon EventBridge rule, ECS cluster, task definition, log groups, IAM roles, Parameter Store parameter, and security groups, and the VPC if the stack created it. It also schedules the stack’s AWS KMS key for deletion after a 30-day waiting period. It doesn’t delete an imported VPC, your knowledge base, your S3 bucket, or the objects that the workflow uploaded. CDK also keeps the container image and templates in its bootstrap resources. It also leaves the cluster’s Container Insights log group, whose name starts with /aws/ecs/containerinsights/Crawl4aiBedrockKbCrawler-.
- To remove the ingested web content, delete the prepared objects under s3://<bucket>/<prefix> and sync the data source again. If the document deletion safeguard is on for a managed knowledge base data source, a sync that would delete more than its threshold percentage of documents skips its delete phase.
- Delete the managed knowledge base only if you created it solely for this walkthrough. A managed knowledge base has no separate vector store to delete.
- For a customer-managed knowledge base, delete the Amazon S3 data source only if you created it for this walkthrough. Its data deletion policy determines whether Amazon Bedrock also deletes the data source’s vector embeddings from your vector store.
Conclusion
In this post, you learned how to extend Amazon Bedrock Knowledge Bases to authorized public web content that needs preparation before ingestion. A scheduled Fargate task uses Crawl4AI for bounded crawling, prepares Markdown with page.md.metadata.json sidecars, uploads them to an Amazon S3 data source, and starts ingestion. The knowledge base then handles parsing, chunking, embeddings, indexing, retrieval, and grounded responses with citations.
Start with the Amazon Bedrock Web Crawler in a managed knowledge base for most public websites. Use the Crawl4AI path when you need control over which part of each page is indexed or which metadata travels with it. To get started, deploy the scheduled Fargate workflow from the companion sample-crawl4ai-bedrock-knowledge-base repository, and then validate retrieval quality and citations with representative content before scaling.
Learn more
For more information about the services and patterns in this post, refer to the following resources:
Acknowledgments
This product includes software developed by UncleCode as part of the Crawl4AI project.
