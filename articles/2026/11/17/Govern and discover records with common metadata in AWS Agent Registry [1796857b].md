---
id: "1796857b9a1b2f79"
title: "Govern and discover records with common metadata in AWS Agent Registry"
url: "https://aws.amazon.com/blogs/machine-learning/govern-and-discover-records-with-common-metadata-in-aws-agent-registry"
link: "https://aws.amazon.com/blogs/machine-learning/govern-and-discover-records-with-common-metadata-in-aws-agent-registry"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-17T20:31:04Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Sana Iqbal"]
language: "en"
summary: "As organizations build more agents, Model Context Protocol (MCP) servers and skills, they need a consistent way to describe, govern, and find them. AWS Agent Registry provides a catalog for registering, approving, and discovering these resources and custom records. Each record carries a name, a description, a protocol descriptor, and an approval status. However, every organization has attributes…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "safety & ethics", "search & media", "models & research"]
content_source: "fulltext"
word_count: 1996
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Govern and discover records with common metadata in AWS Agent Registry

AWS Machine Learning Blog · Sana Iqbal · 2026-11-17

Artificial Intelligence
Govern and discover records with common metadata in AWS Agent Registry
As organizations build more agents, Model Context Protocol (MCP) servers and skills, they need a consistent way to describe, govern, and find them. AWS Agent Registry provides a catalog for registering, approving, and discovering these resources and custom records. Each record carries a name, a description, a protocol descriptor, and an approval status. However, every organization has attributes and facts that it wants to track, and some are unique to that organization, such as its business units, resource owners, risk classifications, and development environments. Organizations want one common definition for each of these attributes, and they want every agent, MCP server, and skill in the registry to carry these facts. Until now, organizations had no way to define these facts in AWS Agent Registry and store them on each record.
Custom metadata schemas are now available in AWS Agent Registry. A custom metadata schema is a set of organization-defined key-value pairs that records in an AWS Agent Registry carry. An administrator defines the schema and applies it to the registry, and all records within the registry must then adhere to the schema. When publishers create or submit records, they supply values for the fields specified in the applicable schema, and AWS Agent Registry validates those values against the schema set by the admin. Approvers can rely on the validated values when reviewing a record, and consumers and agents can use them to discover and filter records. Administrators, publishers, security and governance teams, approvers, consumers, and agents all work from a shared set of facts to govern, discover, and understand the resources in their agentic fleet.
In this post, we follow the AnyCompany organization publishing an MCP server with custom schema definition, enriching that record, and making it available for discovery by humans or agents. We use an MCP server as the example, but the same steps apply to other record types.
How custom metadata works
With custom metadata, an organization can use standardized vocabulary for describing its resources. The registry administrator defines the custom metadata schema: field names, types, allowed values, and whether each field is required or optional. The registry enforces the schema on every record, so a field such as environment has the same name and the same allowed values whichever team publishes the record.
The schema has common attributes that apply to every record type, and you can add dedicated fields that only apply to specific record types. Each field is Text, Enum, URL, or Boolean.
- When a record is created or updated, the registry validates the custom metadata against the schema set up by the admin. 
  - If a record is created without any custom metadata, AWS Agent Registry saves it as NON_COMPLIANT. A team can save work in progress this way, but it can’t submit the record for approval until it has the required fields and values.
  - If a record includes custom metadata with an unknown field, a missing required field, or an invalid value, AWS Agent Registry rejects it with a ValidationException.
- GetRegistryRecord returns the record’s custom metadata values and its compliance status. (COMPLIANT means that the values match the administrator’s schema. It is not an approval. The approvers make that decision.)
- Discovery APIs also allow filtering records based on custom attributes.
What custom metadata makes possible
Because teams can describe the AWS Agent Registry records with the same fields and values, the registry can support and scale governance and compliance.
Ownership and operations
Fields such as environment (prod, staging, or dev), businessUnit, ownerTeam, supportContact, and costCenter record where a resource runs, who is responsible for it, and who pays for it. A configuration management database (CMDB) ID links the record to your existing inventory, and a support-tier field sets expectations for anyone who depends on the resource.
Security and compliance
Data classification, compliance scope such as Payment Card Industry (PCI) or Health Insurance Portability and Accountability Act (HIPAA), risk tier, scan status, and a scan report URL turn an approval into a check of structured evidence. Your existing scanners, CMDB sync jobs, and classification tools write these values through the API before a record is submitted. You can build your record approval process or automation using these values, as this post shows.
Better discovery
Custom metadata values are indexed for search. A consumer or agent can combine a natural-language query with specific metadata filters, such as environment=prod AND businessUnit=payments AND securityScanStatus=PASSED. Only approved records are returned, so a record that matches the filters but hasn’t been approved stays out of the results. Figure 1 shows how each role, from administrator to consumer, moves a record through schema definition, registration, enrichment, approval, and discovery.
Walkthrough of an MCP record from registration to discovery
AnyCompany operates anycompany-governed-registry, an AWS Agent Registry without auto-approval. Its payments team publishes an MCP record, payments-ledger-mcp, a read-only server for ledger lookups. Existing security and inventory systems enrich this MCP record before an approval function decides whether consumers can discover it.
The five numbered steps in Figure 2 match the walkthrough: define, register, enrich and submit, review, then discover.
Prerequisites
To follow the walkthrough, you need:
- An AWS account in a supported AWS Region.
- AWS credentials available to Boto3 and AWS Identity and Access Management (IAM) permissions for AWS Agent Registry.
- Python 3.11 or later and boto3 1.43.113 or later.
- The sample implementation is in the GitHub repo.
The snippets are shortened: cp and dp are the agent-registry-control and agent-registry boto3 clients. The sample repository has the complete code.
Step 1: AWS Agent Registry admin defines the custom metadata schema for the registry
AnyCompany’s admin creates a registry with a custom metadata schema that every record must follow.
- Every record must have its environment, businessUnit, and securityScanStatus fields.
- Records can also carry optional fields that the publisher or automation fills in later: ownerTeam, cmdbId, dataClassification, and securityScanReportUrl.
- MCP servers also record their networkEgress, which is optional.
Figure 3 shows this schema and the values payments-ledger-mcp will carry once enrichment completes in Step 3. The empty autoApprovalRules list means that the registry approves nothing on its own. Every submitted record stays in Pending approval until someone or something approves it. You decide whether that is done by automated checks you build (Step 4 uses an AWS Lambda function), a human approver, or both.
Administrators can also review the schema in the AWS Agent Registry console. Figure 4 shows the common attributes and the MCP-specific field as they appear on the registry’s details page.
Step 2: The publisher registers the server
The payments team’s pipeline registers payments-ledger-mcp with its custom metadata. Its first attempt uses production instead of one of the administrator’s allowed values.
The registry rejects the record. After the pipeline sends prod, the record is created as a compliant draft. This is how the schema keeps every team using the same values.
Step 3: Automation adds additional metadata and submits
Next, AnyCompany’s automation adds what its own systems know: the result from its security scanner, the asset ID from its CMDB, and the approved data classification. It then submits the record for approval.
An update replaces the whole metadata map, so the automation reads the current values, adds its own, and writes them back together. In the sample, the scanner and CMDB calls are stubs that you replace with your own tools. The registry sends a pending-approval event to Amazon EventBridge. In Step 4, a rule that you create passes the event to your approval function.
Step 4: The approval automation decides from the evidence
When the record moves to Pending approval, AWS Agent Registry sends an event to Amazon EventBridge, and an Amazon EventBridge rule is set to invoke a custom AWS Lambda function. Figure 5 shows the console view of payments-ledger-mcp, with the custom metadata values that the approval function reads for its check.
The function reads the record’s custom metadata and compliance status to check that the record is COMPLIANT, the scan PASSED, a cmdbId is present, and the data is public or internal. payments-ledger-mcp passes all four, so the function approves. A record that fails a check is rejected, and the reason names the failed check. In your production systems, you can choose to route records that need a human review, such as those with confidential or restricted data, for manual review instead of being rejected.
Step 5: Consumers find the records from AWS Agent Registry with custom metadata fields as filters
A developer looking for a ledger tool searches the registry and filters on the same fields the administrator defined.
The search returns payments-ledger-mcp because it’s approved and matches all three filters. Agents can run the same search through the registry’s MCP endpoint, https://agentregistry.<region>.api.aws/registry/<registryId>/mcp, which offers search, list, and get as MCP tools. In the GitHub sample, a Strands agent connects to the AWS Registry MCP endpoint and uses a model on Amazon Bedrock. Its system prompt lists the custom metadata fields to filter records on. The agent turns a plain-language request, such as “a production MCP server for payments ledger lookups that passed its security scan”, into a filtered search. It answers with payments-ledger-mcp.
Developers and agents query the same fields the administrator defined, and the approval function checked, so both find only servers that meet your governance rules.
Design the schema for long-term use
Treat the schema as your organization’s shared vocabulary:
- Agree on the vocabulary first. Settle field names and allowed values with the teams that publish and approve records before you create the schema. Schema changes are additive: you can add fields, add allowed values, or make an optional field required, but you can’t rename, remove, or retype a field.
- Expect existing records to lag behind schema changes made after the records were added to the registry. Existing records aren’t rewritten. A record that no longer matches the schema is reported as NON_COMPLIANT and keeps its approval status. The record stays approved, but its next update must meet the new schema. Editing an approved record creates a draft that must be submitted for approval again, and the submit fails until every required field has a value. Until a curator approves the new revision, consumers keep seeing the approved one.
- Put each field at the right level. Use common attributes for questions that apply to every record type, and record-type fields for record-specific facts such as autonomy level for agents.
- Pick the type that fits the field. Use Enums for decision fields that need consistent spelling, Text for external identifiers, and URL for evidence stored behind the source system’s access controls.
- Make a field required only when the publisher can assign a value at registration. For a value that your continuous integration (CI) or automation provides after the record is published, allow an interim value, for example PENDING. In this post, the scan runs after registration, so securityScanStatus has three values: PENDING, PASSED, and FAILED. The publisher writes PENDING, and the enrichment automation replaces it.
- Keep sensitive details out. Leave secrets, internal endpoints, and detailed findings out of broadly readable metadata.
Conclusion
In this post, we showed how to add custom metadata in AWS Agent Registry to give every record a common set of facts, such as its environment, owning business unit, data classification, and security scan status. Using one MCP server, we showed an administrator defining the schema, a publisher and existing automation filling in the values, an approval function that you build in AWS Lambda deciding approval, and a consumer finding the approved server with metadata filters. Because the administrator owns the schema, every team uses the same fields and values, and that consistency is what makes approvals and searches in AWS Agent Registry dependable.
- Try it yourself: Use the sample at GitHub repo.
- Go deeper: Read the AWS Agent Registry Developer Guide and custom metadata API reference.
- Availability: See supported AWS Regions.
