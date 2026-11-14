---
id: "773ec8d2db34b976"
title: "Cost attribution and controls for AI developer and productivity tools on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/cost-attribution-and-controls-for-ai-developer-and-productivity-tools-on-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/cost-attribution-and-controls-for-ai-developer-and-productivity-tools-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-13T18:44:02Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Aamna Najmi"]
language: "en"
summary: "Amazon Bedrock provides built-in, zero-instrumentation cost attribution that traces every inference call back to the IAM principal that made it. The identity flows along with organizational tags, into AWS Cost and Usage Reports (CUR 2.0) and AWS Cost Explorer while keeping data inside the AWS security boundary. This post shows you how to use these capabilities to answer three questions that…"
tags: ["Advanced (300)", "Amazon Bedrock", "Technical How-to"]
orgs: ["Amazon", "Anthropic", "OpenAI", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 2303
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Cost attribution and controls for AI developer and productivity tools on Amazon Bedrock

AWS Machine Learning Blog · Aamna Najmi · 2026-11-13

Artificial Intelligence
Cost attribution and controls for AI developer and productivity tools on Amazon Bedrock
Amazon Bedrock provides built-in, zero-instrumentation cost attribution that traces every inference call back to the IAM principal that made it. The identity flows along with organizational tags, into AWS Cost and Usage Reports (CUR 2.0) and AWS Cost Explorer while keeping data inside the AWS security boundary. This post shows you how to use these capabilities to answer three questions that every FinOps and AI Platform leader asks as AI tool adoption scales: What is the real per-user cost? Which teams generate the most spend, and does that spend correlate with the value they deliver? How should next year’s budget scale with headcount and adoption?
The approach works identically regardless of which AI coding or productivity tool makes the call. Claude Code, Claude Desktop, OpenAI Codex, ChatGPT Work, and OpenCode all invoke Amazon Bedrock through one of two inference endpoints: bedrock-runtime or bedrock-mantle, and Bedrock’s attribution mechanism operates at the endpoint layer, beneath any tool-specific logic. You configure identity propagation once, and every tool that routes inference through Bedrock inherits per-user cost visibility automatically.
By the end of this post, you will have AWS IAM Identity Center configured with your external identity provider for per-user attribution, session tags (team, cost center) flowing into CUR 2.0, Amazon Athena queries and dashboard options for ongoing cost visibility, and a clear understanding of Bedrock-native usage controls to enforce spending limits.
How Amazon Bedrock attribution works
Amazon Bedrock records the IAM identity of every inference caller with no changes required to your API calls. When a user invokes a model through either the bedrock-runtime or bedrock-mantle endpoint, Bedrock captures the caller’s full IAM ARN, including the session name for federated users and publishes it to CUR 2.0 in the line_item_iam_principal column. In billing data, usage is aggregated per principal and per usage type for each export interval: one hour in an hourly export, one day in a daily export. CUR does not contain per-request cost. For per-prompt detail, use model invocation logs or request metadata tagging.
Optionally, you can attach tags to IAM principals or pass session tags during federation to add organizational dimensions. These tags appear in CUR 2.0 with the iamPrincipal/ prefix and in Cost Explorer as filterable dimensions. The mechanism supports four access patterns: IAM users, per-application roles, federated identities, and large language model (LLM) gateways proxying to Bedrock. For a comparison of all four, see Introducing granular cost attribution for Amazon Bedrock. This post follows the federated identity pattern, which is the natural fit for AI coding and productivity tools where each developer or knowledge worker authenticates individually.
Amazon Bedrock offers additional attribution mechanisms beyond IAM principal tracking that organizations can layer depending on their needs (see Appendix A for a comparison). With Application Inference Profiles, you can tag spend by workload on the bedrock-runtime endpoint. With Projects and Workspaces, you can isolate and tag spend on the bedrock-mantle endpoint. Per-request metadata tagging provides per-prompt token-level detail in model invocation logs for workloads that need granularity finer than finer than CUR 2.0’s per-usage-type aggregation per export interval. You can combine these, for example, IAM principal attribution for per-user dollars on your invoice alongside per-request metadata tags for per-prompt detail in logs. The choice depends on your goal (see Track usage and costs in Amazon Bedrock).
The attribution problem
The developer and productivity tools run on each user’s machine and call Amazon Bedrock directly, or through an LLM gateway. Users authenticate by assuming a shared IAM role, so every API call appears as assumed-role/<role>/<session-name> in billing. If every user assumes the role with the same fixed session name, or calls go through a gateway’s own role, CUR aggregates spend to a single principal. With IAM Identity Center, the session name is the user’s sign-in name, so each user gets their own principal. You can further enrich it with session tags (team, cost center, project). These fields flow into CUR 2.0’s line_item_iam_principal column and cost allocation tags with the iamPrincipal/ prefix, making per-user spend queryable alongside the dollars, with zero changes to your Bedrock API calls.
Claude Platform on AWS and Claude for Enterprise route inference through Anthropic-managed infrastructure. For Claude Platform on AWS, usage is visible by workspace and API key in Anthropic’s admin console, and workspace tags flow to AWS billing. For Claude for Enterprise, per-user usage is visible in Anthropic’s admin console and Usage and Cost API. Spend limits are enforced natively by Anthropic.
Prerequisites
Before starting, make sure you have:
- An AWS account with IAM permissions to access Bedrock models you intend to use.
- AWS IAM Identity Center enabled in your management account.
- An external identity provider (Okta, Microsoft Entra ID, or Ping Identity) with SCIM provisioning capability.
- AWS CLI v2 configured on developer machines.
- AWS Cost and Usage Report (CUR 2.0) enabled with IAM principal data and delivered to an S3 bucket.
- Cost allocation tags activated from the management (payer) account.
- An Athena table configured to query CUR 2.0 data (see the GitHub sample to get started).
Step 1: Configure IAM Identity Center with your external IdP
Configure your external identity provider as the identity source in AWS IAM Identity Center. Navigate to IAM Identity Center → Settings → Identity source → Change identity source. Select “External identity provider” and configure SAML 2.0 or SCIM connectivity with your IdP. Enable SCIM provisioning to automatically synchronize users and groups, including organizational attributes like team and department.
Configure attribute mapping for session tags by navigating to Settings → Attributes for access control. Map your IdP’s organizational attributes to session tags that will flow into CUR 2.0. These attributes propagate as session tags (aws:PrincipalTag/Team, aws:PrincipalTag/CostCenter) on every API call the user makes, including every Bedrock invocation through both the bedrock-runtime and bedrock-mantle endpoints.
Step 2: Create a permission set for Bedrock access
Create a permission set in Identity Center that grants Bedrock invocation access. Each user gets their own session within this permission set. This is the foundation of per-user attribution. The specific IAM actions depend on which Bedrock endpoint the tool calls.
Tools that call the bedrock-mantle endpoint (such as Codex and ChatGPT Work) require bedrock-mantle:CreateInference and related actions scoped to a Project resource. Tools that call the bedrock-runtime endpoint (such as Claude Code and Claude Desktop) require bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream scoped to the relevant foundation model or inference profile ARNs. You can combine both in a single permission set if your organization uses tools across both endpoints.
Note: These resource patterns are a starting point. Narrow them to the specific inference profiles and Projects that you approve. Assign this permission set to the relevant groups synchronized from your IdP. Policy changes are instant and universal, audit is centralized through AWS CloudTrail with each user’s identity, and users do not receive long-lived AWS credentials.
Step 3: Configure user workstations
Users configure their AWS CLI profile once, no custom scripts, credential helpers, or browser automation required. The following ~/.aws/config entry establishes the SSO session:
Users authenticate by running aws sso login --profile bedrock, which opens the browser, authenticates through the IdP, and caches credentials locally. The AWS CLI and SDKs refresh the access token automatically until the IAM Identity Center session ends (8 hours by default). The core trade-off in configuring session duration is between security posture and operational convenience.
Step 4: Point tools at Amazon Bedrock
Each AI tool needs only a standard configuration change to route inference through Bedrock. Because Bedrock attribution operates at the endpoint layer, no tool-specific instrumentation is required. The tool authenticates using the AWS credential chain established in Step 3, and Bedrock captures the caller identity automatically.
Claude Desktop reads third-party inference settings from OS-native managed preferences (/Library/Managed Preferences/com.anthropic.claudefordesktop.plist on macOS, HKLM\SOFTWARE\Policies\Claude on Windows). Author the configuration once in the in-app window (Developer → Configure Third-Party Inference) and choose Export to produce a .mobileconfig or .reg for your mobile device management (MDM) system. For per-user attribution, use in-app AWS sign-in, each user authenticates against IAM Identity Center inside the application, with no AWS CLI on the device:
Configuration is read at launch. Users must quit and reopen the application. If developers already run AWS CLI v2, set inferenceBedrockProfile instead and the app runs aws sso login for them.
Claude Code CLI reads the standard AWS SDK credential chain, including SSO profiles. If AWS_BEARER_TOKEN_BEDROCK is set, Claude Code authenticates with that key and does not use the credential chain, so calls are attributed to the IAM user behind the key. Disable it when you want per-user SSO attribution.
Set awsAuthRefresh in the settings file to automatically re-authenticate when credentials expire:
Pin model versions before fleet rollout so a new release doesn’t change what users invoke:
Codex and ChatGPT Work read ~/.codex/config.toml. Both the desktop app and CLI consume the same configuration layers. For the bedrock-mantle endpoint:
For the bedrock-runtime endpoint, use inference profile IDs:
Set AWS_PROFILE in the environment for both endpoints. For the desktop app, place environment variables in ~/.codex/.env since desktop applications may not inherit shell environment variables. If AWS_BEARER_TOKEN_BEDROCK is set, Codex uses it before the SSO profile and calls are attributed to the IAM user behind that API key. Unset it when you want per-user SSO attribution.
Step 5: Enable cost attribution in CUR 2.0
From the AWS Billing Console (Billing → Data Exports → Create export), configure delivery to S3 in Parquet format with hourly or daily granularity. Select “Include caller identity (IAM principal) allocation data” to populate the line_item_iam_principal column. Bedrock’s IAM principal cost tracking works for both bedrock-runtime and bedrock-mantle endpoints.
Creating the export in the management account captures all accounts’ Bedrock usage. If you created a CUR 2.0 data export before IAM principal attribution launched, you must create a new export with the caller identity option selected.
Activate cost allocation tags after users have signed in and made at least one Bedrock call. Tags appear in Billing only after the principal has made a call. In the management account, open Billing → Cost allocation tags, filter by type IAM principal, and activate Team and CostCenter:
Allow up to 24 hours for tags to appear and up to 48 hours to see them in CUR 2.0 and Cost Explorer. Activation is not retroactive. Bedrock meters and bills input, output, cache-read, and cache-write tokens separately. A single hour of activity under one IAM principal typically produces four CUR rows.
Step 6: Query cost data with Amazon Athena
Once CUR 2.0 is delivered to S3 and an Athena table is configured, query usage and cost at your desired granularity. The following query extracts per-user cost:
For daily spend trend per cost center:
Athena charges by data scanned. Columnar Parquet and the billing_period filter keep queries inexpensive.
Step 7: Visualization
AWS Cost Explorer requires zero setup. Group by tags once they are activated. AWS Quick Sight connects to Athena for interactive dashboards with anomaly detection that alerts on unexpected spend spikes. You can integrate with the CUDOS dashboard, an open-source Cloud Intelligence Dashboards (CID) framework that provides detailed cost insights. Grafana with the Athena plugin renders CUR data as time series alongside existing infrastructure metrics.
Implementing per-user usage controls
Once per-user cost visibility is established through IAM principal attribution in CUR 2.0, organizations need enforcement mechanisms to help prevent uncontrolled accumulation. Numerous approaches exist today, each trading enforcement latency against operational complexity.
AWS Budgets with budget actions is the lightest option requiring no custom infrastructure. Set a budget threshold filtered by IAM principal tags, and attach an action (such as applying a deny policy) that triggers when the threshold is breached. The trade-off: AWS Budgets updates up to three times a day, and Bedrock charges can take up to 24 hours to appear in billing data, so a high-velocity user can overshoot by up to a day before enforcement takes effect.
Amazon CloudWatch alarms and AWS Lambda offer near-real-time enforcement using Bedrock’s native CloudWatch metrics (InputTokenCount, OutputTokenCount, Invocations) filtered by model ID or inference profile. Enforcement latency drops to 1–5 minutes. To get user-level granularity with this approach, use Application Inference Profiles or per-user roles.
Amazon DynamoDB-based quota tracking enforces limits at the authentication layer. A Lambda function increments per-user token counters in DynamoDB and withholds credentials once a limit is exceeded. Enforcement takes effect at the next credential refresh, not on individual API calls, but removes the billing-data lag inherent in budget-based approaches.
LLM gateway proxy delivers per-invocation blocking across Bedrock models and SDK workloads, at the cost of highest operational complexity and added latency on every request. See Multi-Provider Generative AI Gateway.
Organizations typically layer these options: CUR 2.0 for reporting, a gateway or DynamoDB-based enforcement for real-time control, and AWS Budgets as a backstop. For the full reference, see How to limit usage and cost on Amazon Bedrock.
Conclusion
Amazon Bedrock’s IAM principal attribution gives you per-user cost tracking for every AI developer and productivity tool that routes inference through Bedrock, with no custom credential scripts, per-user IAM roles, or additional infrastructure. Users authenticate with aws sso login, the same flow they use for other AWS access, and every Bedrock invocation automatically carries their identity into billing data.
Each component can be adopted incrementally. Start by connecting your IdP to Identity Center and assigning a Bedrock permission set to get session-level attribution in CloudTrail immediately. Activate cost allocation tags to surface that data in CUR 2.0. Add Athena queries and dashboards as reporting requirements grow. Layer usage controls, from AWS Budgets to real-time gateway enforcement, based on your organization’s tolerance for enforcement latency.
Regardless of which AI tools your organization adopts today or adds tomorrow, the attribution and control mechanisms described here operate at the Bedrock platform layer. Configure once, and every tool that calls Bedrock inherits the governance.
