---
id: "c636885b9662b9ce"
title: "Customize answers per tenant in Amazon Bedrock Managed Knowledge Base"
url: "https://aws.amazon.com/blogs/machine-learning/customize-answers-per-tenant-in-amazon-bedrock-managed-knowledge-base"
link: "https://aws.amazon.com/blogs/machine-learning/customize-answers-per-tenant-in-amazon-bedrock-managed-knowledge-base"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T15:46:28Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Josh DeMuth"]
language: "en"
summary: "With retrieval instructions in Amazon Bedrock Managed Knowledge Base , you can customize answers per tenant. The same product and policy documents often serve several audiences, such as customers in different regions or internal teams, and each audience needs its own answer. You set the voice, format, retrieval guidance, and answer policy that agentic retrieval applies to each request. Before…"
tags: ["Advanced (300)", "Amazon Bedrock", "Technical How-to"]
orgs: ["Amazon"]
topics: ["policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 3018
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Customize answers per tenant in Amazon Bedrock Managed Knowledge Base

AWS Machine Learning Blog · Josh DeMuth · 2026-11-16

Artificial Intelligence
Customize answers per tenant in Amazon Bedrock Managed Knowledge Base
With retrieval instructions in Amazon Bedrock Managed Knowledge Base, you can customize answers per tenant. The same product and policy documents often serve several audiences, such as customers in different regions or internal teams, and each audience needs its own answer. You set the voice, format, retrieval guidance, and answer policy that agentic retrieval applies to each request. Before this feature, you couldn’t set the answer style, so agentic retrieval could use a different style from one request to the next. For a fixed voice or structured output, you had to turn off response generation, call a model yourself, and maintain the prompt in every application.
Now you write that guidance once, as a managed, versioned Amazon Bedrock resource, and each request references it. When you change an instruction, you can pin a version so that each application switches to the new version when you’re ready.
Take AnyCompany Smart Home, a fictitious company that sells a home controller and room sensors in three sales regions. Its customer assistant serves all three regions, and its support, field sales, and legal teams use internal assistants that they built on the same documents. AnyCompany defines each region and internal team as a tenant here, and each needs a different answer. A customer in Sales Region Central needs Spanish with day/month/year dates, and a support agent needs a short ticket note. To keep the example compact, every tenant queries one knowledge base. However, agentic retrieval can search up to five knowledge bases in a single request, and the tenant’s instruction applies to all of them.
Retrieval instructions change how the assistant answers, but they aren’t an authorization or data-isolation boundary. Use metadata filters or separate knowledge bases to control what each tenant can retrieve. In this post, we show how to give each tenant its own answers from shared knowledge bases while keeping each tenant’s data separate. By the end, you can roll out a change to one tenant’s instruction and confirm which version answered each request.
Why tenants need their own instructions
Tenants that share documents still differ in language, date and money conventions, voice, and which policy values they can quote. A retrieval instruction has four fields for these differences:
- persona: who the assistant is, including identity, tone, and language.
- answerFormat: how the answer is structured, including how it cites sources.
- retrievalGuidance: how the agent interprets the question and what it prioritizes when it searches.
- answerPolicy: whether and how to answer, including questions outside scope.
The persona, answerFormat, and answerPolicy fields apply only when generateResponse is true, which is the default, and retrievalGuidance applies either way. For details, see Create and manage retrieval instructions. Table 1 shows how the answer to the same return question changes when the request includes the Sales Region Central instruction and names the customer’s region.
Table 1: The same return question with and without the Sales Region Central instruction
These patterns come up across industries. An enterprise software provider can run one assistant for many of its own customers. Each customer uploads its policies, standard operating procedures, and company values, and persona and answerPolicy give each one its own voice and rules. A regulated enterprise can put a fixed disclaimer in answerPolicy and a set citation form in answerFormat, so every answer includes both. A team that sends answers to downstream code can get strict JSON from an answerFormat, without a separate generation step. In each case, the documents are shared, and the voice, format, and policy change from caller to caller.
How retrieval instructions work
An instruction belongs to your AWS account and AWS Region, not to a knowledge base, and goes through these stages:
- Create – CreateRetrievalInstruction returns HTTP 202.
- Review – Amazon Bedrock reviews the instruction’s fields asynchronously, and you poll for the result. If the review fails, lastTransitionStatusReasons says why.
- Activate – A passing review makes the instruction ACTIVE, and DRAFT points to its current content.
- Version – CreateRetrievalInstructionVersion saves an immutable numbered version.
- Apply – A request names the instruction and, optionally, a version, which defaults to DRAFT.
- Report – The first Planning trace event includes appliedInstruction.
Scope and trade-offs
Instructions set voice, format, conventions, and policy wording. They don’t limit which documents the agent can retrieve, and they don’t choose the tenant’s own values, which come from naming the tenant in the request. Use metadata filters or separate knowledge bases to limit what each tenant can retrieve.
Solution overview
Each tenant gets its own instruction and metadata filter. The instruction sets the voice, format, and policy of the answer, and the filter limits which documents the agent retrieves. Your backend chooses both from the authenticated tenant, so one shared knowledge base can serve every tenant. In Figure 1, your backend maps the authenticated tenant to an instruction version and a metadata filter, and adds a short tenant line to the message. Then it calls AgenticRetrieveStream on one shared managed knowledge base.
The same pattern works with a separate knowledge base for each tenant. A request can query a shared global knowledge base and the tenant’s own knowledge base together, each with its own filter.
The example uses 32 short, fictitious AnyCompany Smart Home policy and product documents for the AnySmartProduct-5 home controller and AnySmartProduct-6 room sensors. They’re stored in an Amazon Simple Storage Service (Amazon S3) bucket, and each has region, audience_team, and sensitivity metadata. Each of the six tenants, three regions and three teams, has its own instruction pinned to version 1. Two restricted engineering notes belong to no tenant, so no tenant’s filter should return them.
The code is in the GitHub repo, in Python and TypeScript, and runs in the US East (N. Virginia) Region (us-east-1) by default. To use another AWS Region, set AWS_REGION. For the latest Region support, see Supported AWS Regions.
Prerequisites
You need the following:
- An AWS account with permissions to create retrieval instructions, AWS Identity and Access Management (IAM) roles, and an S3 bucket.
- One or more managed knowledge bases, with a metadata file for each document you want to filter on.
- Python 3.10 or later and a current version of the AWS SDK for Python (Boto3). Older Boto3 versions don’t include the retrieval instruction operations.
- A current version of the AWS Command Line Interface (AWS CLI) for control-plane commands. AgenticRetrieveStream has no CLI command, so call it through an SDK.
- Optional: an AWS Key Management Service (AWS KMS) customer managed key, if you want to encrypt instructions with your own key.
Examples use Python with these two clients. Later snippets leave out the client setup and import lines.
Create a retrieval instruction for each tenant
The Sales Region Central instruction sets the language, date and money formats, and policy wording:
To create and pin each tenant’s instruction:
- Select a tenant key, such as sales-region-central, for the name and the tenant tag.
- Enter the instruction fields for that tenant.
- Send CreateRetrievalInstruction with the content and tags.
- Poll GetRetrievalInstruction until lastTransitionStatus is neither CREATING nor UPDATING.
- If the status isn’t ACTIVE, read lastTransitionStatusReasons, revise, and update.
- Create a version and record it in your release configuration.
This code runs steps 3 and 6. The repo version adds the polling for steps 4 and 5.
An update replaces the whole instruction, including the description, so resend every field you want to keep. To encrypt an instruction with your own key, set customerEncryptionKeyArn when you create it. You can’t add or change the key later. Your key policy also needs the statement in Encryption of retrieval instructions.
Keep tenant data apart with metadata filters
An instruction doesn’t limit which documents the agent retrieves. On a shared knowledge base, a Sales Region North customer’s question can return the Sales Region Central and South addenda, and even notes that no tenant should see. To keep each tenant to its own documents, add a metadata filter built from the authenticated tenant, or give the tenant its own knowledge base. A request can still query the tenant’s knowledge base alongside shared ones. Figure 2 compares the three approaches.
A metadata filter keeps one knowledge base to sync and maintain, but every document needs accurate metadata, and your backend must build the filter correctly on every request. A separate knowledge base per tenant isolates tenant data by design, but each tenant adds a knowledge base and data source to create, sync, and pay for. You can combine them: one request can query a shared knowledge base and the tenant’s own knowledge base, each with its own filter.
With a tenant filter or a separate knowledge base, the agent retrieves only documents the tenant is entitled to, so answers don’t quote other regions’ values. An answer policy that limits the assistant to one region helps, but without a filter an answer can still quote another region’s value.
Build the filter on your server from the authenticated tenant, because Amazon Bedrock applies whatever filter the request sends:
This filter uses the equals, andAll, and orAll operators on document metadata. It isn’t per-user access filtering through userContext.
Answer policies are best effort. A line such as “Never share restricted engineering notes” can keep values out of the answer. If the notes are retrieved, though, an answer can still name the mechanism or record ID. To keep restricted content out of answers, exclude it with a metadata filter.
Answer as the tenant
For each request, your backend sends the tenant’s instruction ID and version, the tenant filter, and a tenant line. A tenant line is a short sentence, such as Customer sales region: Sales Region Central., placed before the question:
Here’s the same return question answered with three tenant instructions on one knowledge base, trimmed:
A tenant line tells the agent who is asking, which helps the answer quote that tenant’s values. It doesn’t set the tenant’s language, answer format, or date and money formats, so pair it with the tenant’s instruction. Without the instruction, a Sales Region Central answer can come back in English, without the Source: line, or in the wrong date format.
Without an instruction, a customer answer can also quote internal discount tiers from a document the tenant can retrieve. An answer policy that forbids them, like the Sales Region Central one, can keep them out, but to make sure, filter out the document that contains them. Team formats such as the ticket note aren’t guaranteed on every answer, so validate the format in any code that depends on it.
Instructions change how an answer is written. The facts still come from the documents the agent retrieves, so compute exact values such as a return deadline in your application.
Cover users who belong to a region and a team
A request can reference only one retrieval instruction. When a user belongs to both a region and a team, that instruction has to cover both. For example, a support agent in Sales Region South needs the support team’s voice and the region’s date and money formats. Table 2 compares two ways to set that up for N regions and M teams.
Table 2: Two ways to cover a region and a team with one instruction
Start with the team’s instruction and a region tenant line, which keeps the count at N + M. Add a combined instruction only for pairs whose formats differ from the team’s default. Neither approach limits what the agent retrieves, so keep the tenant filter on every request. A filter also can’t remove a value from a shared document the tenant is entitled to, such as a global policy that lists every region’s dates. As of this writing, the default quota is 50 retrieval instructions per account per AWS Region, and you can request an increase. Combined instructions add up quickly, with 15 for 3 regions and 3 teams and 65 for 10 regions and 5 teams.
Scope tenant roles with instruction tags
If your application calls agentic retrieval with the same role for every tenant, IAM can’t tell tenants apart, and your code alone chooses each request’s instruction and filter. When each tenant’s requests run under that tenant’s own credentials, tag conditions add a second check on which instruction a request can apply and who can change it. Those credentials can come from a role per tenant or a role assumed with a tenant session tag.
AgenticRetrieveStream has no IAM resource. To apply an instruction, the caller needs bedrock:GetRetrievalInstruction on the instruction’s Amazon Resource Name (ARN), so that’s where the tag condition goes. These attribute-based access control (ABAC) statements from the example’s AWS Cloud Development Kit (AWS CDK) app scope one tenant:
With these statements, a tenant’s applier role can apply only instructions tagged with its tenant, and its tenant admin role can manage only those instructions. The platform admin can manage any tenant’s instructions. Require both tag conditions on TagResource. With only the request-tag condition, a tenant admin can retag another tenant’s instruction into its own scope. To add a tenant, add its key to the tenantRoles context value and deploy the AWS CDK app again with the same trustedPrincipalArn. Apply permission doesn’t limit retrieval, so scope bedrock:Retrieve to each role’s knowledge bases. ListRetrievalInstructions can’t be scoped by tag, so keep instruction names free of sensitive information.
Trace each answer to a tenant and version
As Use retrieval instructions with agentic retrieval describes, the first Planning trace event includes appliedInstruction, with the ID and version of the instruction that was applied. Log it with the tenant ID:
For every event type, see the AgenticRetrieveStream API reference. To capture the applied instruction, check for the first Planning event in the loop that reads the answer:
For an audit record outside your application, use AWS CloudTrail. CloudTrail logs Agents for Amazon Bedrock Runtime operations, including AgenticRetrieveStream, as data events. A trail records data events only after you enable them. For details, see Monitor Amazon Bedrock API calls using CloudTrail.
Release instruction changes one tenant at a time
Amazon Bedrock doesn’t route traffic between versions. Keep a release configuration for each tenant, pin its version on every request, and canary, promote, or roll back by changing that pin. The trace confirms which version served each request, not whether the new version answers better, so gate each promotion on your own checks. This release configuration is from the repo’s router:
To change one tenant, update its instruction, wait for the review, create a version, and move only that tenant’s pin. For example, moving the support tenant to version 2 leaves the other five tenants on version 1:
A pin fixes the instruction, not the exact wording of each answer. During an update review, DRAFT keeps serving the previous content. A version create or a second update during the review fails with HTTP 409, so poll until the review finishes, as the retrieval instruction rollout steps describe.
More ways to use retrieval instructions
Retrieval instructions aren’t only for multi-tenant setups. The same fields work for a single application, such as an assistant that has to return JSON for downstream code or keep one voice across every answer. The repo has code for the first three.
Return structured JSON
An answerFormat can replace your own generation step:
With this answerFormat, agentic retrieval can return the JSON directly, so you don’t need a separate generation step. Validate the JSON in your code before you use it.
Serve several audiences
Give each audience its own persona and answerFormat, such as a customer answer and a ticket note, so the same knowledge bases can serve them all without mixing their formats.
Apply one instruction across knowledge bases
Several retrievers can share one instruction version:
Keep a consistent brand voice
Set identity, tone, and language once in persona, such as “Use a friendly, concise tone. Reply in the language of the question.”
Add disclaimers or citation formats
Put required lines in answerPolicy and citation forms in answerFormat, and give a realistic citation example, such as Source: central-returns-addendum.md, instead of a placeholder.
Hand off questions outside scope
Use answerPolicy to name the fallback, such as “If the documents do not answer the question, say so and give the support contact.”
Teach domain vocabulary
Use retrievalGuidance for acronyms and preferred sources, such as “Treat model numbers as exact-match terms.” Check the Planning trace events to see how the agent searched. Use filters, not guidance, to limit what it retrieves.
Best practices for writing retrieval instructions
Follow these practices when you write and roll out retrieval instructions:
- Add a tenant line to the message. It helps the answer quote the tenant’s own values.
- Bind filters to the authenticated tenant on the server. Amazon Bedrock applies whatever filter the request sends.
- Pin versions in production. Test on DRAFT, then promote by changing the pin.
- Wait for each review to finish. After a create or update, poll until the review succeeds before you create a version. A version create during a review fails with HTTP 409.
- Treat answer policies as best effort. To keep a documented fact out of answers, filter out the document that contains it.
- Validate formats your code depends on. Formats such as a ticket note aren’t guaranteed on every answer.
Clean up
To avoid ongoing charges, delete the retrieval instructions with the following commands. Then follow the cleanup steps in the repo README for the knowledge base, data source, S3 bucket, and roles.
Conclusion
Retrieval instructions give each tenant its own voice, answer format, date and money formats, and answer policy on shared managed knowledge bases. Pair them with metadata filters to keep tenant data apart and pinned versions to roll out changes one tenant at a time. The trace shows which version answered, and CloudTrail can record the AgenticRetrieveStream calls. Tag conditions add a check when tenants have their own credentials.
To get started, see the AgenticRetrieveStream API reference and the GitHub repo. To learn more, read Agentic retrieval for Amazon Bedrock Managed Knowledge Base.
