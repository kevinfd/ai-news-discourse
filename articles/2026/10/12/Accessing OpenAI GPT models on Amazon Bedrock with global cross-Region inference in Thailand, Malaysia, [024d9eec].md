---
id: "024d9eece6c046fd"
title: "Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference in Thailand, Malaysia, Singapore, Indonesia, and Taiwan"
url: "https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-12T17:52:22Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Traci Lim"]
language: "en"
summary: "Single-Region inference can throttle when demand exceeds local capacity. Teams in Thailand, Malaysia, Singapore, Indonesia, and Taiwan need access to the newest OpenAI models beyond that capacity. Amazon Bedrock offers OpenAI GPT-6 Sol and GPT-6 Luna through global cross-Region inference from all five AWS Regions, and GPT-6 Astra from Asia Pacific (Singapore). This post shows you how to…"
tags: ["Advanced (300)", "Amazon Bedrock", "Technical How-to"]
orgs: ["OpenAI", "Amazon"]
topics: ["models & research", "agents & coding", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 1976
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference in Thailand, Malaysia, Singapore, Indonesia, and Taiwan

AWS Machine Learning Blog · Traci Lim · 2026-10-12

Artificial Intelligence
Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference in Thailand, Malaysia, Singapore, Indonesia, and Taiwan
Single-Region inference can throttle when demand exceeds local capacity. Teams in Thailand, Malaysia, Singapore, Indonesia, and Taiwan need access to the newest OpenAI models beyond that capacity. Amazon Bedrock offers OpenAI GPT-6 Sol and GPT-6 Luna through global cross-Region inference from all five AWS Regions, and GPT-6 Astra from Asia Pacific (Singapore). This post shows you how to configure the call, set permissions, and monitor inference from your source Region.
GPT-6 Sol, GPT-6 Luna, and GPT-6 Astra are all available through global cross-Region inference from the preceding Regions, on the bedrock-runtime endpoint. See Cross-Region inference in the Amazon Bedrock User Guide. For the full list of source and destination Regions in each profile, see Supported Regions and models for inference profiles.
In this post, we introduce the global cross-Region inference profiles and invoke them from Asia Pacific (Singapore) using the Converse API, the OpenAI-compatible APIs, and coding clients. We then cover the AWS Identity and Access Management (IAM) and service control policy (SCP) configuration, quota management, and monitoring.
Global cross-Region inference profiles for OpenAI GPT-6
The GPT-6 family offers three models, each available through global cross-Region inference.
- GPT-6 Sol brings strong reasoning and coding capabilities to complex tasks performed throughout the week.
- GPT-6 Luna makes focused, repeatable tasks practical at high volume.
- GPT-6 Astra handles complex reasoning, coding, and long-document work.
All three accept text and image input, client-side tool use, and prompt caching. They differ on reasoning effort. GPT-6 Sol and GPT-6 Luna accept none, low, medium, high, xhigh, and max. GPT-6 Astra accepts the same levels except none. For GPT-6 Sol and GPT-6 Luna, see Bring more intelligence to everyday work with GPT-6 Sol and GPT-6 Luna on Amazon Bedrock. For GPT-6 Astra, see Take on your most ambitious work with GPT-6 Astra on Amazon Bedrock.
Global cross-Region inference routes requests across supported commercial AWS Regions where the model is deployed, giving you broad access to Amazon Bedrock capacity. You invoke it by passing a global cross-Region inference profile ID in place of a model ID. Your source Region is where you make the API call. Amazon Bedrock selects the destination Region for processing. Billing, quota tracking, AWS CloudTrail, and Amazon CloudWatch all stay in your source Region.
The following table lists the global cross-Region inference profile IDs and the source Regions covered in this post.
Inference profile availability and Region support change as AWS adds Regions and profiles, so confirm both on the model card before you build: GPT-6 Sol, GPT-6 Luna, and GPT-6 Astra. For per-token rates, see Amazon Bedrock pricing.
Getting started with OpenAI models on Amazon Bedrock
Start with the prerequisites, then invoke any of the three profiles through the Converse API, the OpenAI-compatible APIs, or your existing coding client.
Prerequisites
- An IAM identity with permission to invoke the profile. The IAM policy in the Security and permissions section grants only what these examples need.
- Your source Region activated. Only the Region you call from needs activating. You do not activate destination Regions, which run on Amazon Bedrock managed capacity. Singapore (ap-southeast-1) is a Region that is enabled by default. Jakarta (ap-southeast-3), Malaysia (ap-southeast-5), Thailand (ap-southeast-7), and Taipei (ap-east-2) are opt-in Regions you must activate first. For more information, see Enable or disable AWS Regions in your account.
- A current AWS SDK or CLI. The OpenAI-compatible examples also require the OpenAI SDK and the Amazon Bedrock token generator. Install them with pip install boto3 openai aws-bedrock-token-generator.
The Amazon Bedrock console lists all three global cross-Region inference profiles under system-defined inference profiles. See Figure 1.
Invoke GPT-6 models through Amazon Bedrock Runtime
Each model supports three access paths on this endpoint: the Amazon Bedrock Converse API, the OpenAI Responses API, and the OpenAI Chat Completions API. The OpenAI-compatible APIs are called on the /openai/v1 paths rather than through the AWS SDKs, and the endpoint accepts either Signature Version 4 (SigV4) or an Amazon Bedrock API key. Pass the global cross-Region inference profile ID as the model in every case.
Converse API. This example calls GPT-6 Sol from Asia Pacific (Singapore) and logs the response. Set BEDROCK_PROFILE_ID to global.openai.gpt-6-luna or global.openai.gpt-6-astra to switch models, or call converse_stream for streaming.
OpenAI Chat Completions API. Point the OpenAI SDK at the Regional endpoint and pass the same profile ID.
When migrating an existing OpenAI client:
- Set the model parameter on every request, including those referencing a previous response.
- Use supported tool types: function, mcp, custom, namespace, and tool_search.
- Configure the inference profile ID directly in your client rather than querying the models endpoint.
Set up the ChatGPT desktop app and Codex CLI
The ChatGPT desktop app and the Codex CLI share ~/.codex/config.toml, so one change covers both. Of the two built-in Amazon Bedrock providers, only amazon-bedrock-runtime accepts an inference profile.
SigV4 signing means there is no key to rotate. Add profile = "<your-profile>" for a non-default profile, and set region explicitly, because the client otherwise falls back to AWS_REGION. Substitute another profile ID for model to change models.
Codex reports a 272,000-token window for these profiles, which is its own bundled figure rather than a service limit. Raise it with model_context_window. This configuration needs Codex CLI 0.148 or later.
Figure 2 shows the result in the app.
Security and permissions
Amazon Bedrock offers a range of controls over inference. Two of them matter here. AWS Identity and Access Management (IAM) policies control which roles can invoke which profiles, and service control policies (SCPs) apply organization-wide controls, including Region scope. This section covers both, and where request data lands.
IAM permissions for global cross-Region inference
To call any of these models through a global cross-Region inference profile, your IAM policy needs four statements:
- Access to the inference profile and the project/default resource in your source Region.
- Access to the foundation model in your source Region, scoped to the inference profile.
- The Region-agnostic Amazon Resource Name (ARN) for the foundation model, arn:aws:bedrock:::foundation-model/openai.gpt-6-sol, with aws:RequestedRegion set to unspecified to permit cross-Region routing.
- bedrock:CallWithBearerToken for API-key authentication.
This IAM policy grants permission to invoke GPT-6 Sol through global cross-Region inference from ap-southeast-1. Replace with your AWS account ID and ap-southeast-1 with your source Region.
If you use streaming (converse_stream or stream=True), add bedrock:InvokeModelWithResponseStream to the Action in the first three statements. Converse authorizes as bedrock:InvokeModel. If you only call Converse with SigV4 credentials, drop the fourth statement.
To switch models, replace openai.gpt-6-sol with openai.gpt-6-luna or openai.gpt-6-astra throughout. For the complete reference, see IAM policy requirements for global cross-Region inference.
Service control policy considerations for global cross-Region inference
A global cross-Region inference request carries no Region name. Amazon Bedrock sets aws:RequestedRegion to unspecified, so a Region allowlist in an SCP denies the call, and the error names only the policy type, not which policy. That is a common reason a first call fails in an enterprise account.
Rather than widening the allowlist, scope the exception. Amazon Bedrock populates the bedrock:InferenceProfileArn condition key during authorization, so an SCP can allow these profiles while keeping Region controls for everything else. The following SCP does that.
The first statement enforces your Region allowlist for every service except Amazon Bedrock inference. The second denies that inference outside those Regions unless it routes through a global cross-Region inference profile. For geographic profiles, add their prefix (for example inference-profile/us.*) to the ArnNotLike list, because geographic requests carry a real Region name. Keep your source Region in the allowlist, and add the global services your organization uses to NotAction.
A blunter alternative is to add unspecified to your existing allowlist, which works but opens the same exception to every other service. For a ready-to-use policy file, see the aws-samples service-control-policy-examples repository.
Data retention and abuse detection
For automated offline abuse detection, classifier-flagged traffic is retained by AWS for up to 30 days and processed programmatically. Under cross-Region inference that retention happens in the destination Region, which for a global profile is any supported commercial AWS Region where the model is deployed. Eligible customers might request full zero data retention through their AWS account team. For more information, see Amazon Bedrock abuse detection and Data retention.
If your organization has data residency requirements, take this to your risk and compliance team early. See the AWS Financial Services Compliance Center country pages for these five countries. We recommend you obtain your own advice on compliance with the requirements relevant to your business.
Quota management
GPT-6 quotas on bedrock-runtime are measured in tokens per minute (TPM), tracked against the source Region you call from. Input and cache-write tokens count 1:1, and each output token consumes 10 tokens of quota. For example, a request with 2,000 input tokens and 1,000 output tokens depletes 12,000 tokens from your quota.
Amazon Bedrock reserves the full max_tokens up front, so set it close to the completions you expect. One quota covers InvokeModel, Converse, Responses, and Chat Completions. Review and raise it on the Service Quotas console from your source Region. Before production, request increases early and alarm on EstimatedTPMQuotaUsage in the AWS/Bedrock namespace at 70–80 percent of your allocation. See How tokens are counted in Amazon Bedrock and Amazon Bedrock endpoints and quotas for current values.
Monitoring and logging
Your operational surface stays in your source Region. Amazon CloudWatch metrics, AWS CloudTrail events, model invocation logs, quota accounting, and billing all remain in the Region you called from. You pay that Region’s rates, not the processing Region’s.
CloudTrail records where each request was processed. AWS documents a global cross-Region inference profile’s destinations as its commercial Regions rather than enumerating them. GetInferenceProfile returns the Region-agnostic and source-Region model ARNs rather than a destination list. Your per-request record is additionalEventData.inferenceRegion in CloudTrail in your source Region. Inference on this endpoint is a management event, logged by default at no extra cost. CloudTrail Event History retains 90 days, so longer horizons need a trail or model invocation logging. Retrieve the CloudTrail events with this command.
Set the window around a call you just made, because CloudTrail delivery lags by a few minutes. If the most recent event was a failed call, it carries an errorCode and no inferenceRegion. Raise --max-results and pick an event without errorCode.
Metrics and coding-agent usage stay in CloudWatch. Where developers reach GPT-6 through a coding agent, CloudWatch Coding Agent Insights adds ready-made dashboards under GenAI Observability that break token use down by user, team, and cost center. The agents emit OpenTelemetry metrics natively. For Codex, see Set up OpenTelemetry for OpenAI Codex.
Clean up
This post adds an IAM policy and optionally an SCP statement and a logging destination. Detach or delete the IAM policy you attached, and revert the SCP entry if you added one. Delete the model invocation logging destination in Amazon Simple Storage Service (Amazon S3) or Amazon CloudWatch Logs if you created one, to avoid storage charges. The global cross-Region inference profiles are system-defined, so there is nothing to delete.
Conclusion
This post showed how to invoke GPT-6 Sol and GPT-6 Luna from five Asia Pacific source Regions, and GPT-6 Astra from Asia Pacific (Singapore), through global cross-Region inference on bedrock-runtime. Pass a global cross-Region inference profile ID as the model parameter, and configure the IAM policy and SCP exception from this post. The same endpoint serves the OpenAI-compatible APIs, so an existing OpenAI integration moves across by changing a base URL and a key.
To get started, attach the IAM policy from this post, and send a first request through global.openai.gpt-6-sol. Size your tokens-per-minute quota at the 10x burndown rate, and confirm in CloudTrail that additionalEventData.inferenceRegion appears on your calls.
For more information, see the Amazon Bedrock User Guide, Route model inference requests across AWS Regions with cross-Region inference, and Amazon Bedrock pricing.
