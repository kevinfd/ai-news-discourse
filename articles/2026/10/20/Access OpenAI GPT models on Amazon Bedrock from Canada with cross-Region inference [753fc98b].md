---
id: "753fc98bb47cb9f3"
title: "Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference"
url: "https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference"
link: "https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-20T16:42:53Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Roopesh Ramklass"]
language: "en"
summary: "Canadian organizations building generative AI applications on Amazon Bedrock often need the latest foundation models (FMs), such as OpenAI GPT-6.1, OpenAI GPT-6, and GPT-5.6, accessible from the Canadian AWS Regions. With Amazon Bedrock cross-Region inference (CRIS), you can now access these models from Canada. OpenAI GPT-5.6 models (Sol, Terra, and Luna), GPT-6 (Astra, Sol, and Luna), and…"
tags: ["Amazon Bedrock", "Announcements", "Intermediate (200)"]
orgs: ["Amazon", "OpenAI"]
topics: ["models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 2074
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference

AWS Machine Learning Blog · Roopesh Ramklass · 2026-10-20

Artificial Intelligence
Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference
Canadian organizations building generative AI applications on Amazon Bedrock often need the latest foundation models (FMs), such as OpenAI GPT-6.1, OpenAI GPT-6, and GPT-5.6, accessible from the Canadian AWS Regions. With Amazon Bedrock cross-Region inference (CRIS), you can now access these models from Canada. OpenAI GPT-5.6 models (Sol, Terra, and Luna), GPT-6 (Astra, Sol, and Luna), and GPT-6.1 Sol are available from the Canada (Central) and Canada West (Calgary) Regions. Inference is processed in North America, with data-residency controls described later in this post.
Cross-Region inference is a capacity mechanism. Your application calls the Amazon Bedrock Runtime endpoint in your source Region. Amazon Bedrock then routes the request to a supported destination Region for processing. With this approach, you get access to a broader capacity pool that can help your application sustain throughput during demand spikes. You don’t need to manage destination Region routing in your application.
In this post, we walk through the GPT-5.6, GPT-6, and GPT-6.1 models available from Canada and the cross-Region inference profiles that serve them. We then show how to set up permissions and invoke the models with the OpenAI Responses API, Chat Completions API, and the Amazon Bedrock Converse API. For the Responses API, we include streaming and tool-use examples. Finally, we cover how to request quota increases, review the observability signals available in your source Region, and clean up when you are done.
Models available from Canada
With Amazon Bedrock, you can access three families of OpenAI models in Canada through cross-Region inference. The following table summarizes each model and its positioning.
These models accept text and image inputs, return text, and support a 1-million-token context window, reasoning mode, and tool calling. GPT-6.1 Sol supports the same context window and tool calling, with additional input and output modalities documented in its model card. GPT-5.6, GPT-6, and GPT-6.1 also support prompt caching on Amazon Bedrock (see the Prompt caching section). These models are available through the OpenAI Responses API, the OpenAI Chat Completions API, and the Amazon Bedrock Converse API on the bedrock-runtime endpoint.
For pricing, see Amazon Bedrock pricing. For per-model Region availability, see the model cards in the Amazon Bedrock User Guide.
Cross-Region inference profiles from Canada
Amazon Bedrock inference profiles are logical identifiers you pass in place of a raw model ID. Each profile defines a model and the set of Regions to which Amazon Bedrock can route a request. Two profile types are available from Canada:
- US geographic (prefixed us.) routes requests to your Canadian source Region and US Regions. Choose this profile when your workload requires inference processing to remain within North America (Canada and the US).
- Global (prefixed global.) routes requests to supported commercial AWS Regions where the model is deployed. This draws on a broader capacity pool at the time of the request.
Endpoint availability differs by model and source Region, as shown in the following table.
Profile membership and model availability can change. The global profile for the GPT-5.6 models is available only from ca-central-1. From ca-west-1, use the US geographic profile for GPT-5.6. Verify the active profiles for your source Region before deployment, either with the AWS Command Line Interface (AWS CLI) or on the console (see the following section), or see the Cross-Region inference support documentation.
Getting started
The following sections walk through the setup and code needed to invoke these models from your Canadian source Region.
Prerequisites
Before you begin, confirm that you have the following:
- An AWS account with the Canada (Central) ca-central-1 or Canada West (Calgary) ca-west-1 Region enabled as your source Region.
- An AWS Identity and Access Management (IAM) role or user with permissions to invoke the inference profiles (see Set up permissions).
- A service control policy (SCP) that allows the inference profiles in your source Region, if your organization enforces SCPs (see SCP considerations).
- Python 3.9 or later with the openai, boto3, and aws-bedrock-token-generator packages installed.
Set up permissions
For quick exploration, attach the AWS managed policy AmazonBedrockLimitedAccess. For deployed workloads with stricter access controls, use a least-privilege custom policy. The following example grants access to the GPT-6 Astra global profile from ca-central-1:
If you authenticate through the API-key path (bearer token for the OpenAI SDK), also grant bedrock:CallWithBearerToken. For the Responses API, add bedrock:InvokeModel on arn:aws:bedrock:ca-central-1:*:project/default.
SCP considerations
If your organization restricts Regions through SCPs, use the bedrock:InferenceProfileArn condition key to allow CRIS traffic while blocking direct calls to unapproved Regions. The following SCP denies Amazon Bedrock inference outside your approved source Regions unless the request uses a CRIS inference profile:
With this condition, Amazon Bedrock can route to the profile’s destination Regions even when those Regions are otherwise denied by your SCP. Every destination Region in your chosen profile must be allowed for the request to succeed. For more detail, see Set up cross-Region inference in multi-account environments.
Verify active inference profiles
Before invoking a model, you can verify which profiles are active in your source Region with the AWS CLI. The following command lists the active OpenAI profiles from ca-central-1. To run the same check from Calgary, replace ca-central-1 with ca-west-1.
The Amazon Bedrock console offers the same view. Open the console, choose Canada (Central) or Canada West (Calgary) as your Region, choose Cross-Region inference under Inference, and review the available profiles.
The following screenshot shows the active OpenAI inference profiles listed on the Amazon Bedrock console for the Canada (Central) Region.
Invoke the models through Amazon Bedrock Runtime
GPT-5.6, GPT-6, and GPT-6.1 support three access paths on the bedrock-runtime endpoint: the OpenAI Responses API, the OpenAI Chat Completions API, and the Amazon Bedrock Converse API. The OpenAI-compatible APIs are called on the /openai/v1 paths of the endpoint. The endpoint accepts either AWS Signature Version 4 (SigV4) or an Amazon Bedrock API key.
The following examples use the Amazon Bedrock token generator for Python to create a short-term Amazon Bedrock API key from your current AWS credentials, so your application does not need to store a static key.
OpenAI Responses API
For applications that already use the OpenAI SDK with the Responses API, point the client at the Regional Amazon Bedrock Runtime endpoint and pass the inference profile ID as the model.
For streaming output, set stream=True and iterate over the response events, printing text as it arrives:
OpenAI Chat Completions API
The OpenAI Chat Completions format works through the same endpoint.
For the full list of supported parameters, including reasoning effort levels, see the model cards in the Amazon Bedrock User Guide.
Amazon Bedrock Converse API
Use the Converse API when your application calls Amazon Bedrock through an AWS SDK. Boto3 resolves credentials through the standard AWS credential chain.
The same call works for GPT-6 Sol, GPT-6 Luna, and GPT-6.1 Sol by changing the inference profile ID. The following example uses the US geographic profile for GPT-6 Sol and the global profile for GPT-6 Luna. Both were validated from ca-central-1.
Tool use
These models support client-side tool use (function calling). Define tools in the tools parameter, and the model returns a structured tool-call request for your application to execute.
Prompt caching
GPT-5.6, GPT-6, and GPT-6.1 support prompt caching on Amazon Bedrock to reduce the cost and latency of repeated prompt prefixes. Implicit caching requires no changes to your code: Amazon Bedrock automatically caches eligible prefixes of 1,024 tokens or more. Cached tokens read on subsequent requests are billed at a discounted rate and do not count against your tokens-per-minute quota. Cached tokens appear in the response usage object and in Amazon CloudWatch metrics so you can track usage. For cache-write pricing, minimum prefix sizes, and support for explicit cache breakpoints, see the prompt caching documentation and the individual model cards.
Quota management
Cross-Region inference quotas on the bedrock-runtime endpoint are measured in tokens per minute (TPM) per model. Each quota combines input and output tokens against a single limit. US geographic and global inference profiles have separate quota allocations, so switching between them changes the pool you draw from.
Token consumption combines input tokens, cache-write input tokens, and output tokens. Output tokens are multiplied by the model’s burndown rate, so output-heavy workloads consume quota faster than raw token counts suggest. Before a production rollout, request quota increases early and monitor quota utilization. Test with representative prompts, output lengths, streaming behavior, concurrency, and peak traffic.
To request a quota increase, follow these steps:
- Open the Service Quotas console in ca-central-1 or ca-west-1.
- Choose Amazon Bedrock, then select the quota named “Cross-Region InvokeModel tokens per minute” for the model that you need.
- Choose Request increase at account level, enter your target value, and submit the request.
For details on how token usage and costs are tracked, see Track usage and costs in Amazon Bedrock.
Observability
Because these models run through the Amazon Bedrock Runtime API, requests made through an inference profile appear in your observability tooling the same way on-demand requests do. Invocation logs and Amazon CloudWatch metrics are recorded in your source Region. This holds regardless of where the request was processed. Your observability stays in one place.
- AWS CloudTrail logs every request, recording which destination Region served it in the additionalEventData.inferenceRegion field. For example:
- Amazon CloudWatch metrics are published per inference profile, covering invocation count, token count, latency, throttles, and errors.
- Model invocation logging delivers full request and response payloads to Amazon Simple Storage Service (Amazon S3) or Amazon CloudWatch Logs. To activate it on the Amazon Bedrock console, choose Settings, then choose Model invocation logging. You can also call the PutModelInvocationLoggingConfiguration API. It is off by default.
- AWS Data Exports itemizes spend by model and profile.
Amazon CloudWatch Coding Agent Insights
If you use these models to power AI coding assistants such as OpenAI Codex, Amazon CloudWatch Coding Agent Insights provides a dedicated dashboard. It surfaces token usage, API request counts, active users, and cost attribution across dimensions such as department, team, and environment. To activate it, configure your coding agent to export telemetry to Amazon CloudWatch. For the setup steps, see Set up OpenTelemetry for OpenAI Codex.
Clean up
To avoid ongoing charges after testing, remove the resources you created:
- Turn off model invocation logging. On the Amazon Bedrock console, choose Settings, then choose Model invocation logging, or call DeleteModelInvocationLoggingConfiguration. This stops delivery of logs to Amazon S3 and Amazon CloudWatch Logs.
- Delete or detach the IAM policies and any Amazon Bedrock API keys that you created for testing.
The inference profiles themselves are system-defined and incur no cost when they aren’t in use.
Security and compliance
Cross-Region inference is designed to protect your data in transit and at rest. Requests travel over the AWS private backbone encrypted with TLS 1.2+ rather than the public internet. For Canadian customers, your data at rest stays in your source Region by default. This includes invocation logs, knowledge bases, and configurations. Only the transient inference computation happens in the destination Region, and by default model providers don’t have access to your prompts or completions.
There’s one consideration specific to OpenAI models. Content flagged by automated abuse classifiers might be retained for up to 30 days in the destination Region for review. If you want to constrain processing to North America (Canada and the US), you can choose the US geographic profile. We recommend reviewing Amazon Bedrock abuse detection with your compliance team.
For a more detailed look at Canadian data residency patterns, see Cross-Region Inference and Canadian Data Residency: A Technical Architecture Guide.
Conclusion
In this post, we showed how to access OpenAI GPT-5.6 (Sol, Terra, and Luna), GPT-6 (Astra, Sol, and Luna), and GPT-6.1 Sol from Canada. These models are available from the Canada (Central) and Canada West (Calgary) Regions using cross-Region inference on Amazon Bedrock. We covered the available inference profiles, how to set up permissions and an example SCP, and how to invoke the models with the Responses, Chat Completions, and Converse APIs. For the Responses API, we included streaming and tool-use examples. We also showed how to request quota increases, review usage, and clean up your test resources.
To get started, review the OpenAI model cards in the Amazon Bedrock User Guide, then open the Amazon Bedrock console and send a test prompt through an inference profile. For pricing, see the Amazon Bedrock pricing page.
If you have questions or feedback, leave a comment on this post.
