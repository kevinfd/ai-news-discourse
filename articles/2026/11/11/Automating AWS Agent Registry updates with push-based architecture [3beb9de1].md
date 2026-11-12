---
id: "3beb9de1922ea0ed"
title: "Automating AWS Agent Registry updates with push-based architecture"
url: "https://aws.amazon.com/blogs/machine-learning/automating-aws-agent-registry-updates-with-push-based-architecture"
link: "https://aws.amazon.com/blogs/machine-learning/automating-aws-agent-registry-updates-with-push-based-architecture"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T20:52:48Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Prachi Kulkarni"]
language: "en"
summary: "Every time a Model Context Protocol (MCP) server published in the AWS Agent Registry, a capability of Amazon Bedrock AgentCore, gains a new tool or updates its schema, the registry record must be updated too. Without automated push-based sync, consumers discover stale metadata. For organizations managing multiple MCP servers across accounts, such a sync keeps catalog records current within an…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1948
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Automating AWS Agent Registry updates with push-based architecture

AWS Machine Learning Blog · Prachi Kulkarni · 2026-11-11

Artificial Intelligence
Automating AWS Agent Registry updates with push-based architecture
Every time a Model Context Protocol (MCP) server published in the AWS Agent Registry, a capability of Amazon Bedrock AgentCore, gains a new tool or updates its schema, the registry record must be updated too. Without automated push-based sync, consumers discover stale metadata. For organizations managing multiple MCP servers across accounts, such a sync keeps catalog records current within an existing governance workflow.
In most enterprise deployments, a catalog’s value depends on its freshness. If a developer deploys a new tool on Monday, but the registry record still reflects last week’s schema, consumers lose trust in the catalog. Stale metadata directly reduces registry reliability, leading teams to inadvertently build dependencies on inaccurate information.
When an engineer adds a tool to an MCP server but forgets to update the catalog:
- Consumers miss out on the new capability entirely.
- Applications might call the tool using an outdated schema, causing unexpected runtime behavior or silent workflow deviations.
Multiplied across teams, this lack of automation erodes trust in the registry. Organizations ultimately fall back on ad hoc discovery mechanisms like hardcoded endpoints, informal knowledge sharing, and stale documentation.
In this post, we outline an event-driven architecture that automates these updates using AWS CloudTrail, Amazon EventBridge, and AWS Lambda.
Architecture overview
The following solution brings these services together into an event-driven pipeline that detects runtime changes and synchronizes them to the registry automatically.
The architecture supports both multi-account and single-account environments:
- Single-account setup: For straightforward deployments, all components reside within Account A. Cross-account forwarding setup isn’t needed as events flow directly within Account A.
- Multi-account setup: This involves two accounts where runtime events from Account B are securely forwarded to Account A. 
         
  - Account A (registry account) owns the AWS Agent Registry, the Amazon EventBridge rule, the push-sync Lambda function, and CloudTrail logs.
  - Account B (MCP server account) hosts the MCP server runtime and the Amazon Cognito OAuth provider used for authentication.
        The sample uses two accounts, but you can scale the architecture for multiple accounts, with Account A as the registry account and multiple AWS accounts similar to Account B for different MCP servers.
The following diagram shows the end-to-end event flow for an update to an MCP server in Account B. The captured event is forwarded to Account A, where a Lambda function queries the MCP server for its tools and updates the matching registry record.
The architecture uses five AWS services:
- AWS CloudTrail captures UpdateAgentRuntime API calls as management events.
- Amazon EventBridge routes matching events to the Lambda function, with cross-account forwarding supported.
- AWS Lambda queries the MCP server for its current tools, diffs against the registry, and updates the record if changed.
- AWS Agent Registry stores MCP server records and their tool schemas as the central source of truth.
- AgentCore Identity, a capability of Amazon Bedrock AgentCore, brokers OAuth token exchanges securely, so the Lambda authenticates without storing secrets.
How it works: business logic flow
After it’s deployed, the pipeline runs the following end-to-end workflow:
- Trigger: A developer in Account B updates an MCP server, which calls the UpdateAgentRuntime API in Amazon Bedrock AgentCore, and AWS CloudTrail captures the event.
- Route: Amazon EventBridge catches the CloudTrail event and forwards it to the central event bus in Account A.
- Parse: The sync Lambda in Account A extracts the runtime Amazon Resource Name (ARN) from the event payload and dynamically constructs the MCP server’s invocation URL. This is how it knows which server in Account B to query.
- Authenticate: The Lambda generates a secure OAuth bearer token through AgentCore Identity.
- Fetch: The Lambda calls the MCP server (initialize, then tools/list) to retrieve the latest tools information.
- Sync: The Lambda finds the matching registry record by its ARN, evaluates the differences, and updates the registry if the schema has changed.
This flow assumes that the Agent Registry in Account A already contains a pre-registered record for the MCP server (created during initial onboarding). The Lambda function in this sample updates existing records only. It doesn’t generate new ones.
This same flow works in a single-account setup where all resources (registry, Lambda, Amazon EventBridge rule, and MCP server) reside in one account. In that case, skip the cross-account forwarding step. Events flow directly within the same account’s Amazon EventBridge bus.
Technical walkthrough
This section walks through the workflow for a single MCP server update with two accounts as depicted in the architecture diagram.
The same flow executes independently for each server that emits an UpdateAgentRuntime event. The Lambda handles one event at a time, scaling naturally with the Amazon EventBridge invocation model.
Step 1: Event capture and routing for cross-account setup
When a developer deploys or updates an MCP server, the UpdateAgentRuntime API is called, either by the AgentCore CLI (agentcore deploy) or directly.
AWS CloudTrail records this as a management event in Account B, with a delivery delay of approximately 5–15 minutes. The event is then delivered to Account A’s default Amazon EventBridge bus.
For a cross-account setup, Account B’s Amazon EventBridge forwards matching events to Account A’s event bus through a cross-account rule.
The Amazon EventBridge rule target in Account A invokes the sync Lambda, passing the full CloudTrail event JSON as the input payload.
The Amazon EventBridge rule pattern:
Step 2: Extract the MCP server URL
The Lambda parses the runtime ARN from the event. It extracts the hosting Account ID and AWS Region to dynamically construct the target MCP server’s URL-encoded invocation endpoint.
Step 3: Secure authentication with AgentCore Identity
The Lambda authenticates using a two-step identity flow. It exchanges its execution identity for a temporary workload token. The Lambda then trades this token for a scoped OAuth bearer token through the target account’s credential provider.
Credential providers are per-account (CREDENTIAL_PROVIDER_{ACCT_ID}), so one Lambda authenticates MCP servers across multiple accounts.
Step 4: Query the MCP server
Using standard MCP streamable-HTTP mechanics, the Lambda establishes an active session through an initialize request. After the session is active, it calls tools/list to fetch the complete array of currently exposed tools and schemas.
Step 5: Find the matching registry record
The Lambda queries the central Agent Registry to locate the corresponding record. It searches APPROVED records for one whose mcpServer.data contains the runtime ARN embedded during record creation (see the Deployment section).
Step 6: Diff and update
To minimize unnecessary writes, tool lists are normalized (sorted by name, compared using name + description + inputSchema). The registry update only fires when a change is detected. If the schemas differ, the Lambda logs the exact additions or removals and pushes the fresh definitions to the registry record.
Governance and approval workflow
AWS Agent Registry enforces a governance lifecycle on each record: Draft -> Pending Approval -> Approved (or Rejected/Deprecated). Administrators configure approval settings at the registry level. These settings control what gets published, who reviews it, and whether records require manual approval before becoming discoverable. Only records in Approved status are visible to consumers through search, catalog browsing, or the registry’s MCP endpoint.
When the Lambda updates a record with new tool definitions, the record automatically reverts to Draft status. Consumers continue to see the previously approved version. A curator or administrator must then approve the update before the new metadata becomes discoverable. This way the automated updates cannot bypass organizational review, and administrators retain full control over what is exposed to consumers.
Deployment
The following table outlines steps in the automation pipeline:
Prerequisites
Before deploying this solution, verify that the following are in place:
- An AWS account with permissions to create Lambda functions, Amazon EventBridge rules, AWS Identity and Access Management (IAM) roles, and Agent Registry resources.
- AWS Command Line Interface (AWS CLI) configured with credentials to access all the services used in the sample. For more information, see Getting started with the AWS CLI.
- Python 3.12 runtime.
- An existing AWS Agent Registry with at least one MCP server record (created during initial onboarding; instructions to create the record are provided in the Deployment section).
- An MCP server deployed on Amazon Bedrock AgentCore runtime.
- An AgentCore Identity workload identity and OAuth2 credential providers configured for each MCP server account (see sample repository for setup).
- For multi-account setups, cross-account Amazon EventBridge permissions between Account B and Account A.
Organizations often use multiple accounts, where the registry is in one account but the MCP servers are in others. This sample outlines the multi-account scenario, which you can convert to a single-account scenario by following the instructions.
Creating the registry record
In this sample, before the sync pipeline can work, a registry record must exist with the runtime ARN explicitly embedded in its server schema. You can use the following code to create the registry record and include the runtime ARN in the record’s mcpServer.data field. This is what the Lambda matches against to correlate AWS CloudTrail events to records:
Approving the record
The Lambda only syncs to APPROVED records.
After making the update, the registry record is in the DRAFT stage. It must move through the governance workflow for the change to be discoverable.
Lambda environment variables
To maintain a strong security posture, zero client secrets are stored in the Lambda environment variables. The function relies entirely on mapping environment variables to reference runtime workload identities, provider names, and permission scopes.
Amazon EventBridge rule
This rule acts as the pipeline trigger, listening for UpdateAgentRuntime management events within the local account or arriving from cross-account Amazon EventBridge bus forwarders:
Clean up
To avoid ongoing charges, delete the following resources when you are done:
- Lambda function – Delete the push-sync Lambda and its IAM execution role.
- Amazon EventBridge rule – Delete the rule and its Lambda target.
- AgentCore Identity – Delete the workload identity and OAuth2 credential providers.
- Registry record – Delete or deprecate the test MCP server record.
- Registry – Delete the registry if it was created solely for testing.
- (Multi-account) Remove the cross-account Amazon EventBridge rule and resource policy in Account B.
You can find the cleanup code in the sample repository.
Known limitations and future improvements
The sample code outlined here (and in the full sample) can be extended in several ways:
- Automatic registration of new MCP servers – Currently, a matching registry record must already exist. A future enhancement could automatically create a record when a previously unknown MCP server is detected for the first time.
- Manual “force sync” trigger – For time-sensitive deployments, an on-demand invocation path through Amazon API Gateway or a CLI command can serve changes outside the regular CloudTrail delivery flow.
- Cold-start resilience – If an MCP server is cold and returns zero tools, the Lambda currently doesn’t retry. Adding exponential backoff and skipping the update when the tool count is zero would improve reliability.
Conclusion
The AWS Agent Registry gives organizations a governed, discoverable catalog for their AI agents and MCP servers.
The push-sync Lambda pattern closes the freshness gap: when a server change is detected, the registry record is updated automatically and securely, within the constraints described in the Known limitations section. Updates revert the record to DRAFT status and must pass through the approval workflow before becoming discoverable again.
As your agent fleet grows from a handful to hundreds of MCP servers, this pattern keeps your registry as the single source of truth, consistently fresh and reviewed.
Get started
The full implementation (Lambda code, deployment script, and architecture diagram) is available as a ready-to-deploy sample. To deploy the solution in your environment, clone the repository and follow the deployment steps in the README.
