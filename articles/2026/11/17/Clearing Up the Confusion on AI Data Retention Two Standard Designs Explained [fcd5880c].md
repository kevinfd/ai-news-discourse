---
id: "fcd5880c8a2d20f8"
title: "Clearing Up the Confusion on AI Data Retention: Two Standard Designs Explained"
url: "https://marktechpost.com/2026/11/17/zero-data-retention-ai-apis-explained"
link: "https://marktechpost.com/2026/11/17/zero-data-retention-ai-apis-explained"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T20:49:45Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Data retention has become one of the most misunderstood terms in AI infrastructure. After a wave of AI security headlines, many dev teams now ask a simple question. Does my AI provider keep my data? The honest answer depends on how you send it. Send a prompt to an inference API, and it is processed and returned without being kept. That design is called zero data retention (ZDR). Upload a dataset…"
tags: ["Agentic AI", "AI Governance", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Comparison", "Editors Pick", "Enterprise AI", "For Devs", "Guardrail", "Harness"]
orgs: ["Amazon", "OpenAI", "Google", "Anthropic"]
topics: ["jobs & society", "models & research", "chips & infrastructure", "policy & regulation"]
content_source: "summary"
word_count: 1922
paywalled: false
image: "https://www.marktechpost.com/wp-content/uploads/2026/11/WP-BLOG-BANNER-10019-scaled.png"
discussion_url: null
score: null
comments: null
community: null
---

# Clearing Up the Confusion on AI Data Retention: Two Standard Designs Explained

MarkTechPost · Asif Razzaq · 2026-11-17

Data retention has become one of the most misunderstood terms in AI infrastructure. After a wave of AI security headlines, many dev teams now ask a simple question. Does my AI provider keep my data? The honest answer depends on how you send it. Send a prompt to an inference API, and it is processed and returned without being kept. That design is called zero data retention (ZDR). Upload a dataset for a batch job, and it stays stored until you delete it. Both are standard designs, and in both the customer is in control. What changes is who manages the data lifecycle, and where. 

 Fireworks AI cofounder and CEO Lin Qiao set out a clear way to think about this. In a November 13, 2026 post on X , she described two standard API designs. Each one decides where control of the data lifecycle sits. The same split has shaped data processing systems for decades. In this article, we will go through that framework with examples from public API documentation. 

 TL;DR 

 The framework: Two standard API designs : upload, use, delete, or send, compute, return. 

 What it is: ZDR is a per-endpoint commitment not to persist covered prompts and outputs after an eligible request. 

 Where it applies: Eligibility depends on the endpoint, request flags and account settings, not the vendor name. 

 Stored features: Batch, file and dataset features keep data until it is deleted or expires. 

 Bottom line: Prefer ephemeral endpoints. If you upload, deletion is your job, so never assume an expiry. 

 What is an AI data retention policy? 

 An AI data retention policy defines what a platform stores from your requests, and for how long. OpenAI’s data controls describe two layers. Application state is data a feature must keep, such as uploaded files. Abuse-monitoring logs are copies held for safety review. A platform can be at zero on one layer and not the other. 

 What are the two common API designs? 

 AI inference and training APIs follow two lifecycle designs. The difference is who manages the data, and where. 

 Pattern 1: Customer-managed retention (upload, use, delete) 

 You create a file or dataset, run jobs against it, then delete it. The platform keeps the data stored and available until you ask for deletion. It cannot know when you are finished unless you define it. So deletion is your job, done through the platform’s APIs. 

 Batch APIs with uploaded datasets are the standard example: 

 OpenAI Batch : upload a JSONL input file, then create the batch. 

 Amazon Bedrock batch inference : input JSONL files sit in an S3 location you choose. 

 Gemini Batch API : jobs run from an input file you provide. 

 Fireworks AI Batch : create a dataset, then submit jobs against it. 

 Once you delete the data, it is gone. According to Fireworks CEO, it keeps nothing after a deletion request . 

 OpenAI non-batch files persist until you delete them. Fireworks AI managed training datasets have no time limit, and the customer deletes them. Amazon Bedrock and Google batch jobs read and write your own cloud storage. 

 OpenAI batch files last 30 days by default, and Anthropic batch data 29 days. Treat expiry as the exception, and confirm it per feature. 

 Pattern 2: Ephemeral processing (send, compute, return) 

 You send data, the platform computes, and the result comes back. No application state stays behind. Your application owns the conversation history, so no platform cleanup step is needed. This is the pattern ZDR applies to. A synchronous response alone does not establish ZDR. 

 Documented examples: 

 OpenAI Chat Completions : store defaults to false. 

 Amazon Bedrock Converse : content is only used to generate the response. 

 Google Gemini text generation : stateless when store is false. 

 Fireworks AI Chat Completions : direct or through Nexus . The schema has no store field. 

 Fireworks AI Training SDK , including Serverless Training : forward_backward sends tokenized batches per call. No dataset is uploaded , and training data is not stored at rest . 

 Think of saving a spreadsheet to a cloud drive versus passing its numbers to a calculator. The drive keeps the file for later. The calculator computes the answer, returns it and keeps nothing. 

 In both designs, customers fully control how their data is handled. What differs is where the lifecycle is managed. In pattern 1, it is explicit dataset creation and deletion. In pattern 2, it lives entirely in your application. 

 Does zero data retention cover every endpoint? 

 The answer is No. ZDR is scoped per endpoint, and defaults differ by platform. 

 OpenAI keeps abuse-monitoring logs for up to 30 days by default. The Amazon Bedrock none mode writes no request or response data to durable storage. 

 Fireworks AI documents ZDR by default for open models. Its ephemeral inference APIs, Training SDK and Nexus carry ZDR guarantees. Prompts and generations are not persisted at rest. For the Batch API , Fireworks document states that no data is retained after deletion . 

 A single parameter can also flip the pattern. On Google’s Interactions API , store defaults to true. At OpenAI , setting store to false is not ZDR, which needs approval. 

 Platform Synchronous inference: default Zero retention option Stored features (pattern 1) OpenAI API Abuse-monitoring logs are kept for up to 30 days, or longer where law requires. No application state on /v1/chat/completions, with exceptions. Chat Completions store defaults to false. Modified Abuse Monitoring or ZDR, each by prior approval. Under ZDR, store is always treated as false. Batch input files expire after 30 days by default. Batch output and error files expire 30 days after creation. Other files persist until deleted. /v1/files and /v1/batches are not ZDR eligible. Responses API: at least 30 days when store is true. Amazon Bedrock The Converse reference says content is only used to generate the response. The effective retention mode is the first non-inherit value across project, account and model default. New accounts and projects start in inherit. Models that require aws_review are retained for up to 30 days. Set the mode to none. No request or response data is written to durable storage. Batch inference reads and writes S3 locations you specify. Under none, requests to models that require retention are blocked. Model invocation logging to your own S3 or CloudWatch is off by default and customer-enabled. Google Gemini Enterprise Agent Platform In-memory and durable caching are on by default for supported Gemini models. Each clears within 24 hours of being written. Abuse-monitoring prompt logging applies to customers on the online Cloud terms. Master Agreement customers are exempt by default, except on designated frontier models. Durable caching can be turned off while in-memory caching stays on. Leave request-response logging and Live API session resumption off. Set Interactions API store to false. Batch inference uses Cloud Storage or BigQuery for input and output. Interactions API store defaults to true. On the separate Gemini API , stored interactions are kept for 55 days on the paid tier and 1 day on the free tier. Anthropic Claude API Standard policy : API inputs and outputs are deleted within 30 days. Content flagged for Usage Policy violations can be kept for up to 2 years. Covered Models : 30 days required. ZDR by arrangement with sales, per organization. Not offered for Covered Models unless Anthropic expressly authorizes it. Message Batches: retained 29 days. Files API: kept until deleted or expired. Neither is ZDR eligible. Fireworks AI ZDR by default for open models. Prompts and generations are not logged or stored without opt-in. They stay in volatile memory for the request. Prompt caches are held in memory only. Request metadata, such as token counts, is logged to run the service. Nexus uses ZDR on every account and plan. Turns it routes to your own Anthropic, OpenAI or Bedrock account follow that provider’s policy. Already the default on Chat Completions , the Training SDK and Nexus. Enterprise admins can also enforce an account-wide ZDR policy . Batch API : runs on uploaded datasets. Customers delete datasets through the console or the API . No data is retained after deletion . Managed training : uploaded datasets stay until the customer deletes them. 

 Documentation checked November 15, 2026. Policies change, so confirm against the linked pages. OpenAI and AWS note that content flagged as CSAM can be retained even under zero retention. 

 Why is ephemeral processing the safer default? 

 Every retained copy must be protected, tracked and eventually deleted. Data that never reaches disk cannot be taken from disk later. 

 Regulation points the same way, with one important thing to note. Under GDPR Article 5 , ephemeral processing supports storage limitation. Data minimisation still depends on what your application sends. 

 “Ephemeral processing is preferable whenever the workflow allows it.” Lin Qiao, cofounder and CEO, Fireworks AI ( post on X ) 

 The reasoning is about human error. Ephemeral processing leaves no forgotten datasets and no missed delete calls. It also means fewer retained copies to protect and eventually delete. 

 Stored features still have a place: dataset-based fine-tuning needs data at rest. 

 What should developers check now? 

 Map every endpoint you call to pattern 1 or pattern 2. 

 Default to ephemeral endpoints when you only need the result. 

 For each upload, plan the delete call. Record any documented expiry. OpenAI supports expires_after. 

 Audit flags that persist data, such as store. 

 Keep secrets out of prompts and datasets. Rotate any that slip in. 

 Define ZDR per processing path in contracts. Then verify the setting in your account. 

 Key Takeaways 

 ZDR is an endpoint property, not a vendor label. 

 Stored features keep data until it is deleted or expires. 

 Prefer ephemeral when you only need the result. 

 If you upload, deletion is your job. Never assume an expiry. 

 Further reading: Lin Qiao Post , OpenAI data controls , Amazon Bedrock data retention , Google zero data retention , Anthropic API data retention and Fireworks AI zero data retention . 

 Sources: 

 OpenAI 

 Data controls in the OpenAI platform: https://developers.openai.com/api/docs/guides/your-data 

 Chat Completions reference (create, store default): https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create 

 Batch API guide: https://developers.openai.com/api/docs/guides/batch 

 Batch API guide, upload your batch input file: https://developers.openai.com/api/docs/guides/batch#2-upload-your-batch-input-file 

 Files API reference (create, expires_after): https://developers.openai.com/api/reference/typescript/resources/files/methods/create 

 Amazon Bedrock 

 Data retention: https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html 

 Converse API reference: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html 

 AWS Security Blog, Enforce zero data retention on Amazon Bedrock (July 7, 2026, updated August 13, 2026): https://aws.amazon.com/blogs/security/enforce-zero-data-retention-on-amazon-bedrock-with-bedrock-projects-and-service-control-policies/ 

 Create a batch inference job: https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-create.html 

 Format and upload batch inference data: https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html 

 Model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html 

 Google 

 Gemini Enterprise Agent Platform and zero data retention (updated November 12, 2026): https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention 

 Abuse monitoring: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring 

 Batch inference from Cloud Storage: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-prediction-from-cloud-storage 

 Gemini API, Text generation: https://aistudio.google.com/docs/text-generation?codelanguage=rest 

 Gemini API, Batch API input file: https://aistudio.google.com/docs/batch-api#input-file 

 Gemini API, Interactions API overview (data storage and retention): https://ai.google.dev/gemini-api/docs/interactions-overview 

 Anthropic 

 API and data retention: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention 

 How long do you store my organization’s data: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data 

 Data retention practices for Covered Models: https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models 

 Fireworks AI 

 Zero Data Retention (data handling): https://docs.fireworks.ai/guides/security_compliance/data_handling 

 Zero Data Retention policy (Enterprise account setting): https://docs.fireworks.ai/accounts/zero-data-retention 

 Secure Training: https://docs.fireworks.ai/guides/security_compliance/secure_training 

 Chat Completions reference: https://docs.fireworks.ai/api-reference/post-chatcompletions 

 Training SDK reference, forward_backward: https://docs.fireworks.ai/fine-tuning/training-api/reference/service-client#forward_backward-datums-loss_type-loss_fn_config=none 

 Batch API: https://docs.fireworks.ai/guides/batch-inference#getting-started 

 Delete Dataset reference: https://docs.fireworks.ai/api-reference/delete-dataset 

 Serverless Training: https://docs.fireworks.ai/fine-tuning/training-api/serverless 

 Prompt caching: https://docs.fireworks.ai/guides/prompt-caching 

 Nexus, Data Security and Privacy: https://docs.fireworks.ai/nexus/data-security 

 Nexus, APIs and SDKs: https://docs.fireworks.ai/nexus/apis-and-sdks 

 Security bulletin, Update on October 2026 security incident (Training SDK: training data not stored at rest): https://fireworks.ai/security/bulletins/october-2026-security-incident-update 

 Fireworks statement on data retention, “Data retention: the control and standard” (November 13, 2026): https://x.com/lqiao/article/2121434466082242896 

 Other 

 Regulation (EU) 2016/679 (GDPR): https://eur-lex.europa.eu/eli/reg/2016/679/oj 

 Thanks to the Fireworks team for the thought leadership / resources for this article. This article is sponsored. 
 The post Clearing Up the Confusion on AI Data Retention: Two Standard Designs Explained appeared first on MarkTechPost .
