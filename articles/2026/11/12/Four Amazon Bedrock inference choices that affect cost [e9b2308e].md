---
id: "e9b2308e4ac312d9"
title: "Four Amazon Bedrock inference choices that affect cost"
url: "https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost"
link: "https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-12T20:51:55Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Sai Pavan Kasani"]
language: "en"
summary: "Your Amazon Bedrock inference bill can keep climbing after you tune prompts and application logic. Request-level choices can still change how many tokens the service processes and the rate applied to them. Cache duration, service tier, reasoning effort, and maxTokens can affect cost without changing your model or prompt. \n Each choice depends on the model and workload. This post shows how we…"
tags: ["Advanced (300)", "Amazon Bedrock", "Best Practices"]
orgs: ["Amazon", "Anthropic", "OpenAI"]
topics: ["models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 1794
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Four Amazon Bedrock inference choices that affect cost

AWS Machine Learning Blog · Sai Pavan Kasani · 2026-11-12

Artificial Intelligence
Four Amazon Bedrock inference choices that affect cost
Your Amazon Bedrock inference bill can keep climbing after you tune prompts and application logic. Request-level choices can still change how many tokens the service processes and the rate applied to them. Cache duration, service tier, reasoning effort, and maxTokens can affect cost without changing your model or prompt.
Each choice depends on the model and workload. This post shows how we tested each choice and how to verify its effect from response metadata, logs, and billing data.
To try these settings yourself, start with the Amazon Bedrock Samples notebooks Mixed TTL Caching and Tenant Isolation with Prompt Caching. For maxTokens and reasoning effort, see the 01-low-effort folder of the sample-code-for-genai-cost-management-workshop GitHub repo. Each sample sets its own model ID, so change it, and the inference parameters, to match the model you call. For model availability by AWS Region, refer to Models at a glance. For broader decisions such as model selection, batch inference, routing, and distillation, see Effective cost optimization strategies for Amazon Bedrock.
Where inference cost comes from
Every Amazon Bedrock response carries usage metadata. Input and output tokens bill at the rate for the model and tier that served the request. Cache reads and writes use separate token counters, and reasoning tokens count as output tokens.
Prompt cache duration
Repeated system instructions, tool definitions, or reference context can be processed again when the cache expires before the next request. The Prompt caching for faster model inference guide lists 5-minute and 1-hour time-to-live (TTL) values for supported Anthropic models. It also lists a 30-minute minimum TTL for supported GPT-5.6 models. Support and API fields depend on the model, so check the current support matrix before selecting a duration.
For supported models, Amazon Bedrock also offers implicit prompt caching, which attempts to reuse eligible prompt prefixes without cache controls in your request. Because implicit caching is best effort and doesn’t guarantee a cache hit, the duration choices in this section apply to explicit caching.
This Converse API signature requests a 1-hour entry on models that support it:
For supported Anthropic models, InvokeModel places the same ttl value in cache_control.
A longer duration is not automatically cheaper. The Amazon Bedrock Pricing page lists separate rates for 5-minute writes, 1-hour writes, and cache reads. For Anthropic Claude Sonnet 5 and Anthropic Claude Opus 5 on Amazon Bedrock, a 5-minute write costs 1.25 times the input rate. A 1-hour write costs 2 times, and a cache read costs 0.1 times.
These rates set the break-even, assuming each request reuses the exact prefix and each cache read refreshes the TTL. A 5-minute cache pays back on the first reuse within 5 minutes. When requests for the same prefix arrive more than 5 minutes apart, it rewrites at 1.25 times on every request. The 1-hour cache is then cheaper from the second request within the hour.
Cache rates and checkpoint minimums differ by model. Check the Amazon Bedrock Pricing page and the prompt caching guide for the model you call. Rerun the comparison for your model, then confirm it with cache read and write tokens after rollout.
Keep stable content before dynamic content, meet the model’s checkpoint minimum, and use on-demand inference because prompt caching doesn’t work with batch inference.
Changing a cached prefix, including a system instruction or tool definition, causes a miss and a new write. Checkpoints are evaluated in the order tools, system, then messages, so a change in an earlier section also invalidates the later ones. Version prompts that change often so each version gets its own cache entry. We ran six calls on Claude Sonnet 5 with a 1-hour checkpoint, changing the system prompt once and the tool definition once. Each change produced zero cache reads and a new write.
AWS describes cache entries as scoped to your account and Region, not to your tenants. In a multi-tenant application, prepend a tenant-specific SHA-256 hash to the cacheable prefix. The Optimizing cost and latency with Amazon Bedrock prompt caching for Anthropic models post describes this pattern. Enforce tenant authorization before you build the prompt. The hash partitions entries inside one account. If a regulated workload needs a hard data boundary, keep each tenant in a separate AWS account.
Keep the 5-minute default for frequent reuse. Move from it to a longer supported duration when the same prefix recurs at least twice an hour with gaps longer than 5 minutes. To beat no caching at all, the 1-hour cache needs three requests an hour.
Service tiers for latency-tolerant workloads
Background jobs, evaluation harnesses, nightly summarization, and backfills don’t always need the latency profile used by interactive requests. For models that support Flex, select it with this request signature:
Use default, not standard, to request the Standard tier. You can also omit serviceTier:
Tier support is model-specific, so record support by exact model version. The Amazon Nova 2 Lite and OpenAI gpt-oss-120b model cards list Flex as supported. The cards for Anthropic Claude Sonnet 5 and Anthropic Claude Opus 5 on Amazon Bedrock list it as not supported. A Flex request to an unsupported model fails with a ValidationException instead of silently running on Standard. Our request to Anthropic Claude Sonnet 5 returned that error.
If your policy allows Standard as a fallback, catch the unsupported-tier error and retry once with default. Don’t retry every ValidationException, because malformed requests raise it too. Cap application-level retries. The bounded retry strategy of the AWS SDK handles throttling and transient errors.
Set your own deadline for Flex requests. A supported response reports the resolved tier, which you can also verify with Amazon CloudWatch ResolvedServiceTier. See Service tiers for optimizing performance and cost and the Amazon Bedrock Pricing page for the exact model you call.
We tested Flex on Amazon Nova 2 Lite with 200 default requests and 200 flex requests, sent in interleaved pairs. Both tiers processed the same number of input and output tokens. All 400 requests resolved to the requested tier, and the median latency difference was too small to separate from noise. At the time of writing, the published Flex rate for Nova 2 Lite in us-west-2 is half the Standard rate, and our bill reflected that. Check the Amazon Bedrock Pricing page for current rates. Keep latency-sensitive traffic on default.
Adaptive thinking effort
Reasoning tokens bill as output tokens. Claude Sonnet 5 and Claude Opus 5 use adaptive thinking at high effort by default, even when a request omits the thinking field. An application moved from Claude Sonnet 4.6 without changes starts billing thinking tokens, and maxTokens now caps thinking plus response text. Claude Haiku 5.5 defaults to medium. All three models support low, medium, high, xhigh, and max. Lower the effort for a task with this request signature:
Keep effort in output_config, not inside thinking. Check Adaptive thinking whenever you change models.
We tested a tool-calling agent on Claude Opus 5. Its three tasks follow the design in Build long-horizon agents with Grok 4.7 on Amazon Bedrock, and each has one correct answer. We ran each task eight times at every effort level. The table shows median output tokens:
Accuracy at lower effort depends on the model and the task. Measure on tasks shaped like yours.
On the Amazon Bedrock Samples Invoke Bedrock model for code generation workload, median output tokens were 676 at low and 743 at high, a difference within run-to-run variation. The programs we graded passed at each effort level.
Use per-request output-token counts, CloudWatch AWS/Bedrock OutputTokenCount, invocation logs, and a task pass rate to evaluate the choice. Start below high for routine, well-bounded tasks. Keep high where your quality tests show that the task needs it. A token reduction that breaks the task is not a saving.
Output token limits
maxTokens is an application output ceiling. It limits the output that a bad prompt, regression, or loop can produce before the request stops. The quota rule is documented in How tokens are counted in Amazon Bedrock. Amazon Bedrock deducts your input tokens plus maxTokens when a request starts, so an oversized value reduces concurrency.
An output ceiling isn’t a safety control. Use Amazon Bedrock Guardrails as a standard responsible AI control in production generative AI workloads. Guardrails can filter content, detect prompt attacks, and check grounding on supported inputs and responses. See Detect and filter harmful content by using Amazon Bedrock Guardrails.
Set maxTokens per task type after observing a representative output-token distribution:
See Inference using Converse API for the request parameters.
In our test on Claude Sonnet 5, five normal outputs peaked at 103 tokens, so we set an illustrative fence of 155 tokens with headroom. We then sent the same deliberately verbose prompt with adaptive thinking disabled, once under a 2,048-token ceiling and once under the 155-token fence. The first request generated 2,048 output tokens and the second generated 155, so the fence avoided 1,893 output tokens. Both stopped at max_tokens, so both responses were truncated. The fence limits spend but does not make an unsuitable prompt useful, and in a multi-turn or agentic chain a truncated turn can break the steps after it.
For production calibration, compare the 95th and 99th percentiles (P95 and P99) for each task type and add headroom to the selected percentile. With adaptive thinking on, maxTokens also caps thinking tokens, so calibrate with thinking enabled. P95 limits exposure more aggressively but accepts more truncation risk. P99 preserves more valid long-tail responses at a higher ceiling. Monitor max_tokens stops and investigate the request before raising the task’s limit.
Putting it together
Use the same test loop for each setting: confirm model support, change one request choice, measure tokens or cost, and track quality or completion. If you route across models, keep a capability record for each model version, Region, and API: supported cache duration, service tiers, reasoning levels, and output ceiling. Validate each request against that record before you send it, then check the response for the resolved tier and cache counters.
Signals to watch
Derive P95 and P99 for each task type from task-tagged application telemetry or invocation logs.
Conclusion
All four choices live in the inference request. Recheck support when you change models, then change one setting at a time and measure the result in your application.
Use these resources to evaluate the choices for your workload:
- Amazon Bedrock console: console.aws.amazon.com/bedrock.
- Prompt caching: Prompt caching for faster model inference.
- Service tiers: Service tiers for optimizing performance and cost.
- Adaptive thinking: Adaptive thinking.
- Responsible AI controls: Detect and filter harmful content by using Amazon Bedrock Guardrails.
- Related reading: Effective cost optimization strategies for Amazon Bedrock.
- Related samples and posts: Invoke Bedrock model for code generation and Build long-horizon agents with Grok 4.7 on Amazon Bedrock.
