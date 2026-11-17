---
id: "7381db88317ca659"
title: "Use prompt caching with open-weight models on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T15:42:41Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Dustin Liu"]
language: "en"
summary: "Many generative AI applications send the same long context with every request, and prompt caching avoids processing it again each time. That context can be a system prompt, reference documents, tool definitions, or the conversation so far. Open-weight models on Amazon Bedrock can reuse it across requests, which helps reduce input costs and response latency. \n Prompt caching reuses the computed…"
tags: ["Amazon Bedrock", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon", "OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 2310
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Use prompt caching with open-weight models on Amazon Bedrock

AWS Machine Learning Blog · Dustin Liu · 2026-11-16

Artificial Intelligence
Use prompt caching with open-weight models on Amazon Bedrock
Many generative AI applications send the same long context with every request, and prompt caching avoids processing it again each time. That context can be a system prompt, reference documents, tool definitions, or the conversation so far. Open-weight models on Amazon Bedrock can reuse it across requests, which helps reduce input costs and response latency.
Prompt caching reuses the computed state of a matching prompt prefix, so repeated context is read from cache instead of being processed again. Amazon Bedrock manages the cache for you. Depending on the model, you can use implicit caching, which works automatically, explicit caching, where you mark the reusable prefix, or both. The more context you reuse, and the more often you reuse it, the more you can save.
As with other models on Amazon Bedrock, your prompts and outputs aren’t shared with the model provider or used to train models. For more information, see Data protection in the Amazon Bedrock User Guide.
Open-weight models on Amazon Bedrock now support explicit prompt caching. In this post, we use both modes with an open-weight model through the Chat Completions API and show how to read cache usage from each response. We then apply implicit caching to an OpenCode coding agent session on the same API and close with best practices.
Prompt caching for open-weight models on Amazon Bedrock
When a request starts with the same content as an earlier one, Amazon Bedrock reads that prefix from cache and processes only the rest. Cache reads are billed at a lower rate than standard input, so the savings can grow each time a prefix is reused. Depending on the model, cache writes can be billed at a higher rate than standard input. See Amazon Bedrock pricing for the rates of each model.
Supported modes depend on the model and the API. For each model’s caching modes, minimum prefix length, and how long entries stay cached, see Models at a glance. The two modes compare as follows:
Implicit caching: Amazon Bedrock reuses eligible prefixes automatically, on a best-effort basis. In a conversation, each request resends the full context, so the previous request becomes the cached prefix of the next one (Figure 1). As the prompt caching guide recommends, put static content first and dynamic content last. Keeping the start of the prompt stable lets every later request reuse it. If an early part changes, as in turn 4 of Figure 1, the cache is rebuilt from that point.
Explicit caching: You mark the end of each reusable prefix with a cache breakpoint. You can add several breakpoints, up to the maximum that the model supports, to cache layers that change at different rates, as Figure 2 shows. Content up to each breakpoint is written to cache once and then read on later requests, and content after the last breakpoint is processed on each request. Check the model card for the minimum token count before a breakpoint, the maximum number of breakpoints, and the time to live (TTL), which resets with each cache hit.
With implicit caching, Amazon Bedrock can also write content to cache that later requests never reuse, such as a question that’s different each time. When the content after a shared prefix changes on every request, use explicit caching to limit cache writes to the shared prefix. Content after the last breakpoint is billed at the standard input rate. On models that charge more for cache writes, you don’t pay the higher write rate for content that’s never read back.
Solution overview
The following diagram shows how both examples in this post reach Amazon Bedrock through the same Chat Completions API endpoint.
- The Python application and the OpenCode coding agent send requests to the Amazon Bedrock Runtime endpoint in your Region, authenticated with a short-term Amazon Bedrock API key.
- Amazon Bedrock checks the prompt cache for a matching prefix. It reads a matching prefix from cache, and writes new cacheable content to cache.
- Amazon Bedrock sends the request to the selected open-weight model and returns the response, including the cache usage fields that the following sections show you how to read.
Prerequisites
To run the samples, you need the following:
- An AWS account with access to your selected model on Amazon Bedrock. Model availability and prompt caching support vary by AWS Region, so check the model card for the Regions that your model supports.
- AWS credentials for an AWS Identity and Access Management (IAM) identity that has permission to invoke your selected model on Amazon Bedrock.
- Python 3.12 with the openai (3.26.0 or later) and aws-bedrock-token-generator (1.1.0 or later) packages.
- For the coding agent example, npm to install OpenCode 1.18.35.
Before you use a model, review its license and service terms, linked from its model card. Your use of the model is also subject to the AWS Responsible AI Policy.
Cache a product manual through the Chat Completions API
The example is a support assistant for a fictional water filter, the AnyCompany AquaPure 500. The system prompt holds a one-line instruction and the owner’s manual, which is the reusable prefix. Each request asks a different customer question.
Set up the client
The samples use the OpenAI Python SDK with the Amazon Bedrock Chat Completions endpoint. For authentication, the provide_token() function from the aws-bedrock-token-generator package turns your AWS credentials into a short-term Amazon Bedrock API key, valid for up to 12 hours. You don’t need to create or store a long-term key.
1. Create a virtual environment and install the packages:
2. Create the manual. Ours is about 4,000 tokens of Markdown. The following excerpt shows its format:
Save it as manual.md and add sections until it’s longer than the minimum prefix length on your model card. Placeholder text works, because the cache only needs an identical prefix. Keep the three sections shown, which answer the sample questions.
3. Save the following setup code as common.py in the same directory. The samples that you create next import from it.
If your model returns reasoning tokens, they count toward max_tokens. The samples set max_tokens=1024 so that short answers have room to finish.
Implicit caching
Implicit caching takes no cache controls. Put the manual in the system message and the question in the user message. Sending both as parts of one user message got no implicit cache hits. Save the following as implicit.py and run it with python implicit.py:
Verify implicit caching
Each response reports cache activity in usage.prompt_tokens_details. Figure 4 shows how to read these fields and the pattern to expect across the three calls of each sample.
In implicit mode, call 1 writes the prompt to cache. Calls 2 and 3 read the system message, with the instruction and the manual, back from cache. They also write a few tokens each, because implicit mode extends the cached prefix to cover each new question. A few tokens after the last message stay uncached on every call. This is the pattern for the first run. If you run the sample again within the TTL, every call reads from cache, and none writes.
Explicit caching
Choose explicit caching to control exactly what is cached. As Figure 4 shows, calls 2 and 3 of the implicit run each write a few tokens to cache, whereas the same calls with explicit caching write nothing. With several breakpoints, you can cache layered prefixes, such as shared instructions and tools followed by a per-customer document (Figure 2).
For explicit caching, add the following to the request:
- prompt_cache_options with mode set to explicit selects explicit mode. It’s an Amazon Bedrock request field, and the OpenAI SDK sends it through extra_body.
- prompt_cache_breakpoint on a text content part marks the end of the reusable prefix. Content up to and including that part is cached, and content after it’s processed again on every request.
Save the explicit version of the same loop as explicit.py:
Set both parts together. Explicit mode without a breakpoint caches nothing, and a breakpoint without explicit mode behaves like implicit caching. For the optional ttl field of prompt_cache_options, check the model card for supported values.
Verify explicit caching
If you run explicit.py right after implicit.py, its first call is already a cache hit. For a cold first call, add a unique first line to the system prompt, for example SYSTEM_PROMPT = f"Run ID: {uuid.uuid4()}\n" + SYSTEM_PROMPT (with import uuid at the top of explicit.py).
As the explicit bars in Figure 4 show, only the first call writes. Each repeat reads the whole prefix up to the breakpoint and writes nothing, and the question after the breakpoint makes up the uncached remainder.
Use prompt caching with the OpenCode coding agent
Coding agents resend a large, stable prefix on every step: the system prompt, tool definitions, and the conversation so far. That makes them a natural fit for implicit caching. OpenCode is an open source coding agent. It can call any Chat Completions endpoint through a custom OpenAI-compatible provider, so it can use the same Amazon Bedrock endpoint as the Python samples. Figure 5 shows the requests that OpenCode sends during one turn and which parts Amazon Bedrock reads from cache.
In one turn, OpenCode sends request 1 with its system prompt, tool definitions, and your prompt, and Amazon Bedrock writes it to cache. The model responds with a tool call, which OpenCode runs on your machine. OpenCode then sends request 2, which contains request 1 plus the tool call and its result. Amazon Bedrock reads request 1 from cache, writes only the new tail, and returns the response.
Configure OpenCode
Install OpenCode and check the version:
Next, add the following opencode.json to the root of your repository, or save it as ~/.config/opencode/opencode.json to apply it to every project. It defines a provider named bedrock that uses the OpenAI-compatible package to call the Amazon Bedrock Chat Completions endpoint:
OpenCode uses small_model for session titles, so pointing it at the same model keeps every request on a model that you’ve enabled. The provider reads its key from BEDROCK_API_KEY. Set it to a short-term Amazon Bedrock API key from provide_token(), in the virtual environment from the first example. If the key expires, run the command again to get a new one:
Confirm that OpenCode lists the model:
Verify implicit caching in a coding session
We ran a three-turn session against a small repository that holds one short Python file. Turn 1 asks for a bug review, turn 2 for a fix, and turn 3 for a short follow-up:
Replace <sessionID> with the sessionID value from the JSON output of turn 1. The opencode export <sessionID> command lists each request’s token usage: cache.read holds the cached_tokens value from Amazon Bedrock, and input holds the rest. OpenCode 1.18.35 doesn’t record cache_write_tokens for an OpenAI-compatible provider, so cache.write stays at 0.
Figure 6 shows how much of each request in the session is read from cache.
The first request processes the whole prompt, most of it the OpenCode system prompt and tool definitions, and Amazon Bedrock writes it to cache. Each later request reads everything up to the end of the previous request from cache, so only the new tail of the conversation is processed. This works with no caching configuration.
Best practices
These practices apply to any model that supports prompt caching:
- Put static content first, in both modes. Place the system prompt, tool definitions, and reference documents before content that changes, and keep them identical between requests. In explicit mode, place each breakpoint after the static content that it covers. Timestamps and request IDs belong at the end of the prompt.
- Make the prefix long enough. Prefixes that meet the minimum token count on the model card are eligible for caching.
- Confirm hits with the usage fields. Check the cache reads and writes in each response, in either mode. Across a workload, track the CacheReadInputTokenCount and CacheWriteInputTokenCount runtime metrics.
- Keep the cache warm. Steady traffic keeps a prefix cached, because the TTL resets with each hit. After an idle gap longer than the TTL, the next request writes the prefix again.
- Cache what you reuse. Savings come from cache reads, so cache content that later requests read again, especially where cache writes cost more than standard input. With cross-Region inference, expect some extra cache writes at times of high demand.
Clean up
The examples make inference calls only and create no resources in your AWS account. Cache entries expire after they go unread for the TTL. The short-term API key from provide_token() also expires on its own, and the samples never write it to disk. To clear it from your shell sooner, run unset BEDROCK_API_KEY.
To remove the local files:
1. Delete the sample directory and its Python virtual environment.
2. Delete opencode.json from your repository, or ~/.config/opencode/opencode.json if you saved it globally.
3. If you no longer need OpenCode, delete ~/.local/opt/opencode.
Conclusion
Prompt caching lets open-weight models on Amazon Bedrock reuse repeated context with little or no change to your code. In this post, implicit caching covered the support assistant and the OpenCode session with no cache settings at all. Explicit caching gave precise control with one request option and a breakpoint for each reusable layer. In every case, the usage fields on each response show what came from cache, so you can measure the benefit on your own traffic.
To get started, choose an open-weight model on Amazon Bedrock that supports prompt caching. Run the samples from this post with your own reference content, and compare the cache reads with your uncached input. The prompt caching guide covers the limits and options for each model, and the Amazon Bedrock runtime metrics let you track cache reads and writes across your applications. For questions, reach out through AWS Support or the AWS re:Post community.
