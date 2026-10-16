---
id: "c4d6082c07a1abcc"
title: "Build long-horizon agents with Grok 4.7 on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-13T15:52:20Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Suheel Farooq"]
language: "en"
summary: "SpaceXAI’s Grok 4.7 is now available on Amazon Bedrock, which offers a choice of foundation models (FMs) from multiple providers. According to SpaceXAI, Grok 4.7 is trained to work longer on more difficult tasks and knows when to check its own work. That matters most for agents, which carry a task through many steps and must verify what they find along the way. \n An agent that works this way has…"
tags: ["Advanced (300)", "Amazon Bedrock", "Amazon Machine Learning", "Artificial Intelligence", "Foundation models", "Generative AI", "Technical How-to"]
orgs: ["Amazon", "xAI", "OpenAI"]
topics: ["models & research", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 2573
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Build long-horizon agents with Grok 4.7 on Amazon Bedrock

AWS Machine Learning Blog · Suheel Farooq · 2026-10-13

Artificial Intelligence
Build long-horizon agents with Grok 4.7 on Amazon Bedrock
SpaceXAI’s Grok 4.7 is now available on Amazon Bedrock, which offers a choice of foundation models (FMs) from multiple providers. According to SpaceXAI, Grok 4.7 is trained to work longer on more difficult tasks and knows when to check its own work. That matters most for agents, which carry a task through many steps and must verify what they find along the way.
An agent that works this way has to do more than look things up. It has to form a candidate answer, check it against what it has learned, and refine it until it fits. Grok 4.7 exposes a reasoning effort setting that controls how much deliberation happens before each response, and for agent workloads a practical question is which level to run.
In this post, we build a tool-calling agent on Grok 4.7 and evaluate it on three tasks that require search rather than lookup. The tasks are diagnosing a two-service outage from its alerts, scheduling maintenance under interacting constraints, and choosing an optimal set of migrations under a budget. Each task has exactly one correct answer, verified by brute force. We ran all three at every reasoning effort level, six times each, for 72 agent runs.
The agent answered 67 of the 72 runs correctly. At xhigh it answered all 18 correctly, and at low it answered 15 of 18 while using about an eighth of the output tokens. That gives a clear trade-off you can tune per request, and we show how to measure it on your own tasks and how to monitor it in production.
We report token counts rather than currency throughout. Token prices change, and the counts are what your own costs are derived from, so a measurement expressed in tokens stays valid.
What SpaceXAI reports about Grok 4.7
According to SpaceXAI, Grok 4.7 uses a larger base model than Grok 4.6 and was trained with a longer reinforcement learning run on a harder mix of tasks. This mix is weighted toward problems that take many hours to complete. SpaceXAI reports that the model is better at verifying its own work and at managing longer context.
SpaceXAI’s published benchmark results follow that emphasis. The largest reported gains over Grok 4.6 appear in the categories that measure sustained work rather than single-turn answers.
Source: SpaceXAI, Introducing Grok 4.7 (https://x.ai/news/grok-4-7). Scores are as published by SpaceXAI at the time of the model launch.
Benchmarks show how a model performs across standard tasks. For your own workload, the useful next step is to measure on tasks shaped like yours, which is what the rest of this post walks through.
SpaceXAI lists a 500K token context window for Grok 4.7, with text and image input and text output. On Amazon Bedrock, the model supports configurable reasoning effort, tool calling, and structured output.
How you access Grok 4.7 on Amazon Bedrock
Grok 4.7 runs on the bedrock-runtime endpoint and is accessed through a cross-Region inference profile. Two profiles are available:
Cross-Region inference routes requests across multiple AWS Regions, which gives you higher throughput without managing capacity Region by Region. Requests name one of the inference profiles rather than a bare model ID.
The model supports the OpenAI-compatible Chat Completions and Responses APIs, and the Amazon Bedrock Converse API. On Converse, reasoning is returned as a reasoningContent block alongside the text block. In inferenceConfig, set maxTokens only, and put model-specific parameters, such as reasoning effort, in additionalModelRequestFields.
For the current list of supported Regions, service tiers, and token prices, see the Grok 4.7 model card in the Amazon Bedrock User Guide and the Amazon Bedrock pricing page (https://aws.amazon.com/bedrock/pricing/).
Prerequisites
- An AWS account with access to Amazon Bedrock, and model access enabled for Grok 4.7.
- Python 3.9 or later, with openai, boto3, and aws-bedrock-token-generator installed.
- AWS credentials configured in your environment.
Your AWS Identity and Access Management (IAM) identity needs bedrock:InvokeModel on both the inference profile and your account’s default project:
- arn:aws:bedrock:{region}::inference-profile/us.xai.grok-4.7 or the global. equivalent.
- arn:aws:bedrock:{region}:{account-id}:project/default.
Include both resources in the policy statement. The default project permission is required in addition to the inference profile.
Connect to the model
For production use, we recommend generating a short-term bearer token from your existing AWS credentials, so authentication stays tied to your IAM identity and no long-lived secret is stored:
Reasoning tokens count as output tokens and draw down max_completion_tokens before the answer text is produced, so size the limit to leave room for both. If the limit is reached during reasoning, the response returns without answer text, so check for empty content in agent code and raise the limit if you see it. Our runs used a limit of 32,768 tokens, which left headroom at every effort level.
Grok 4.7 supports four effort levels: low, medium, high, and xhigh. Effort levels can change between model versions, so it is worth confirming them against the service rather than hardcoding a list:
Design tasks that need reasoning
Many agent evaluations test diligence: read a record, filter it, add it up. Those tasks are worth having, but to see what reasoning effort contributes, a task has to require search: the answer can’t be read off the data, it has to be proposed and then checked.
We built a synthetic environment of 20 services, exposed through seven tools, and three tasks on top of it. Every task has exactly one correct answer, and each is built so that a quick heuristic is not enough to find it.
Four practices keep a measurement like this trustworthy, and they apply to most agent evaluations.
State every rule the grader relies on. If the prompt leaves an edge case open, a reasonable answer can be scored as wrong, and the evaluation ends up measuring the specification rather than the model. The diagnosis prompt, for example, says explicitly that a failed service raises no alert of its own.
Prove each task has one answer. Each environment is small enough to enumerate, so we checked every candidate answer before running anything. For the schedule, that is a few lines:
Grade a required final line, not the whole response. Each prompt asks the agent to end with a line such as FINAL: auth, checkout. The grader reads only that line, so a response that discusses other candidates while explaining its reasoning is graded on its conclusion:
Track format separately from correctness. A missing final line is a different signal from an incorrect one. In our runs, all 72 responses included a gradeable final line.
Constrain tool parameters with an enum where the valid values are known, so every tool call targets a real resource:
The system prompt is deliberately short, and asks the agent to check its answer before giving it:
The agent loop is a standard tool-calling loop: call the model with reasoning_effort set, execute each returned tool call, append the result keyed by tool_call_id, and repeat until the model stops requesting tools. Tracking prompt_tokens and completion_tokens across the loop gives the token counts reported in the following section.
Results
Six runs of each task at each effort level, 72 runs in total. The agent answered 67 correctly.
Three observations.
xhigh answered every run correctly. All 18 runs across the three tasks were correct at xhigh, and medium and high answered 17 of 18 each. With six runs per task and level, the differences between levels are indicative rather than statistically conclusive, and the direction was consistent across all three tasks.
Effort changes how much the agent reasons, not how much it explores. Tool calls were essentially flat, between 17.2 and 18.7 per run at every level. The agent gathered the same facts regardless of effort, and what changed was how much reasoning it applied to them, with output tokens rising from 1,184 at low to 9,147 at xhigh.
low offers a strong cost-to-quality ratio. At low, the agent answered 15 of 18 runs correctly using about an eighth of the output tokens of xhigh, with a median run of 18 seconds. Where a slightly lower completion rate is acceptable, or where answers are reviewed downstream, low is an efficient choice. Where every answer needs to be right first time, higher levels are the safer default.
How effort level shapes the answer
The tasks were designed around a specific kind of difficulty, and looking at how each effort level handled them clarifies when the extra reasoning is worth it.
Optimization. The migration task rewards considering combinations rather than ranking options one at a time. Selecting the candidates with the best individual ratios produces a reasonable answer that is nine points short of the optimum. At medium and above, the agent found the optimal set in all 18 runs.
Hypothesis testing. The diagnosis task requires checking a candidate pair in both directions: every alert has to be explained, and every service that stayed silent has to be consistent with the answer. At medium and above, the agent identified the correct pair in all 18 runs.
Constraint satisfaction. The scheduling task combines ten listed constraints with a team rule that depends on looked-up ownership data. xhigh produced the valid schedule in every run, and this was the task where the highest level made the clearest difference.
The pattern across the three is that additional reasoning effort is most valuable where the agent has to weigh several candidate answers against each other, rather than follow a single path to the result.
Monitoring reasoning in production
In production you don’t have a known answer to grade against, but you do know how many output tokens and tool calls each run used. Those give you a useful operational signal.
Correct runs at each level stay above a clear floor of reasoning volume. Every correct run at medium and above used at least 1,739 output tokens, and the typical run used several thousand. A run that makes no tool calls, or that produces far less output than is normal for its level, is worth flagging for review:
Calibrate the baseline from runs you have graded, per task and per effort level, then apply it to runs you have not. Treat a flag as a prompt to inspect or re-run. At low, where every run is brief, output volume is a weaker signal, so pair it with spot checks.
Asking the agent to verify its answer in the system prompt is worth keeping, because it makes the agent’s reasoning straightforward to follow when you review a run. Pair it with automated grading wherever a known answer exists, so that quality is measured independently of the transcript.
Choosing a reasoning effort
These results suggest a few practical rules.
Match effort to the kind of task. Tasks that involve search, optimization, or testing a hypothesis benefit most from medium or higher. Tasks that follow a single path, or whose answers are reviewed downstream, can run efficiently at low.
Set effort per request, not per agent. Effort is a request parameter, so an agent can run its planning and verification steps at a higher level and its mechanical steps, such as formatting a tool result, at low. That combines much of the reliability of a higher level with a lower token cost.
Measure on your own tasks, with repeats. A single run per configuration gives a single observation. Repeating each configuration several times shows how consistent it is.
Monitor reasoning volume. Output tokens and tool calls per run, tracked by effort level, give you an early signal to review a run before its result is used.
Limitations of this measurement
Six runs per task and effort level. Enough to show a consistent direction across three tasks, not enough for a confidence interval. Treat the differences between levels as indicative.
A synthetic environment. The tools read from data generated in code, which is what makes it possible to prove each task has exactly one answer and to grade automatically. Real tools add latency, partial results and errors, none of which are tested here.
Minutes, not hours. Median run time ranged from 18 seconds at low to 106 seconds at xhigh. This is a scaled-down proxy for long-horizon work. The method transfers. The absolute figures do not.
One model version, one Region, one prompt per task. Different phrasings of the same task may change the results, which is part of why stating every rule explicitly matters.
Token counts, not costs. To convert to currency, apply the current rates for your inference profile and service tier from the Amazon Bedrock pricing page. The Global and US Geo profiles are priced differently, and the Flex and Priority service tiers apply multipliers.
Operational controls for agent workloads
Build in retries. Agents that issue a high volume of calls should treat retries as part of the design. Set a request timeout, retry only errors that are retryable, back off exponentially with jitter, and honor a Retry-After header when one is returned:
On-demand throughput scales up over time, so ramp a new high-volume workload gradually rather than starting at full rate.
Auditing a run. Model invocation logging writes request and response data to Amazon Simple Storage Service (Amazon S3) or Amazon CloudWatch Logs. This gives you the full transcript of runs you want to review after the fact.
Monitoring reasoning volume at scale. Amazon CloudWatch metrics give you the aggregate view of token usage, which is where the per-level baselines described earlier become something you can alarm on.
Attributing spend across agents. Cost itemization in AWS Cost Explorer and the AWS Cost and Usage Report breaks usage out per model, which combined with per-task token counts gives you both unit economics and the aggregate bill.
Matching cost to urgency. Service tiers are set per request, so one deployment can send an overnight analysis through the Flex tier and an interactive request through Priority. For a workload that runs at a higher effort level, tier selection is a further lever on cost.
Choosing a routing profile. Cross-Region inference widens the capacity pool a long run draws from. The Global profile serves from your choice of commercial AWS Region and is typically priced lower per token than geographic routing. The US profile keeps processing within the United States. Choose based on your data residency requirements as well as cost.
Clean up
The examples in this post do not create billable AWS resources beyond per-request token usage. If you generated a long-term Amazon Bedrock API key, delete it in the Amazon Bedrock console when you are finished, because it remains valid until revoked. Short-term tokens generated from IAM credentials expire on their own.
If you enabled model invocation logging to Amazon S3 while testing, review the bucket and remove objects you no longer need.
Conclusion
SpaceXAI trained Grok 4.7 to work longer on more difficult tasks and to know when to check its own work. On three tasks that required search rather than lookup, the agent answered 67 of 72 runs correctly, and every run at xhigh. Because reasoning effort is set per request, you can choose where each step of an agent sits on the trade-off between thoroughness and token cost.
Three things are worth carrying into your own evaluation. Design tasks with one provable answer and state every rule the grader depends on. Repeat runs, so you see how consistent each configuration is. And monitor output tokens and tool calls by effort level, so you have an operational signal alongside your quality measurements.
