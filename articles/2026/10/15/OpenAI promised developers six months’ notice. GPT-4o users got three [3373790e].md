---
id: "3373790e23385b27"
title: "OpenAI promised developers six months’ notice. GPT-4o users got three."
url: "https://thenewstack.io/openai-gpt4o-api-shutdown"
link: "https://thenewstack.io/openai-gpt4o-api-shutdown"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T17:52:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "OpenAI is retiring four GPT-4 models from its API on January 14, 2027. The deprecation notice the company sent developers Wednesday covers GPT-4o, GPT-4o mini, GPT-4.1, and GPT-4.1 mini, along with their dated snapshots and every fine-tuned model built on top of them. \n\n With just three months to migrate production traffic, OpenAI’s recommended replacement, GPT-6 Luna, handles reasoning and tool…"
tags: ["AI Engineering", "AI Models", "Large Language Models"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 705
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI promised developers six months’ notice. GPT-4o users got three.

The New Stack · Amanda Caswell · 2026-10-15

OpenAI promised developers six months’ notice. GPT-4o users got three.
OpenAI is retiring four GPT-4 models from its API on January 14, 2027. The deprecation notice the company sent developers Wednesday covers GPT-4o, GPT-4o mini, GPT-4.1, and GPT-4.1 mini, along with their dated snapshots and every fine-tuned model built on top of them.
With just three months to migrate production traffic, OpenAI’s recommended replacement, GPT-6 Luna, handles reasoning and tool calls differently enough that swapping the model ID may be the easiest part of the migration.
GPT-4o’s long goodbye
GPT-4o arrived on May 13, 2024, as OpenAI’s flagship and built a following loyal enough to change the company’s plans. When GPT-5 replaced it in August 2025, Reddit filled with complaints, and OpenAI brought it back for paying ChatGPT subscribers the very next day. That reprieve lasted until February 13, 2026, when GPT-4o and GPT-4.1 disappeared from ChatGPT. Both remained available through the API, but that access now is sunsetting.
By then, OpenAI said just 0.1% of daily ChatGPT users were still choosing GPT-4o, although the model continued serving API requests for applications built around it.
GPT-4.1 was a different kind of release, arriving on April 14, 2025, as an API-only family that skipped ChatGPT entirely and went straight after developers with stronger coding, better instruction following, room for up to a million tokens of context, and more reliable diff formats for anyone letting a model loose on large files.
Kevin Weil, OpenAI’s chief product officer, called them models “trained just for developers” during the launch livestream, and Sam Altman went on X to say developers “seem very happy” with them.
Luna pricing has fine print
Luna is the fastest and cheapest tier of GPT-6, and on paper it covers the basics GPT-4.1 offered, with a 1.05 million-token context window, structured outputs and function calling. At $0.10 per million input tokens and $0.50 per million output tokens, it’s cheaper than GPT-5.6 Luna, which charged twice as much for input and $1.20 per million output tokens.
Once a prompt passes 272,000 input tokens, the input rate doubles the output rate raises by 50% for the entire request. That could eat into the savings for RAG pipelines and coding agents working with large codebases.
OpenAI’s migration guide says GPT-6 Luna defaults to medium reasoning effort but supports function calling through Chat Completions only with reasoning_effort=none. Combining reasoning and tool calls requires the Responses API. Enabling reasoning also rules out temperature, top_p, top_logprobs, and logprobs, all supported by GPT-4.1.
The company recommends using its Docs skill in Codex to update API calls across a project, but those changes won’t account for differences in model behavior. Anthropic ran into a similar problem last month when Opus 5.5 introduced four breaking changes, causing 400 errors in existing agent integrations. Other changes altered how agents behaved without triggering errors, making those regressions harder to catch.
No fine-tuning on Luna
New self-serve fine-tuning jobs end on January 6, 2027, eight days before the GPT-4 models retire. Existing fine-tuned models will continue serving inference requests until January 14, leaving a short window to run replacements alongside them.
New self-serve fine-tuning jobs end on January 6, 2027, eight days before the GPT-4 models retire.
Six months’ notice, three delivered
Other deadlines are on OpenAI’s deprecation schedule, which includes GPT-4.1 nano, the first GPT-4o snapshot, and older GPT-3.5, GPT-4, and o-series models retiring October 23. GPT-5 and o3 snapshots follow December 11, with selected legacy audio, real-time, and transcription models scheduled for January 20, 2027. GPT-5.1, GPT-5.3-Codex and GPT-5.4-Nano are set to retire April 1.
The List models API now includes a shutdown_date field, making it possible to check upcoming retirements automatically. Customers who need more time may be able to keep older models running through dedicated capacity, although they’ll have to arrange that with OpenAI’s sales team.
The three-month warning also falls short of OpenAI’s own deprecation policy, which promises at least six months’ notice for generally available models. The policy allows exceptions for safety or compliance reasons, but there’s no explanation for why GPT-4o and GPT-4.1 are getting only half that time.
The three-month warning also falls short of OpenAI’s own deprecation policy, which promises at least six months’ notice for generally available models.
