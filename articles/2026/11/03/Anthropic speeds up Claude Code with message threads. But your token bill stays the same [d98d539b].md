---
id: "d98d539be988c252"
title: "Anthropic speeds up Claude Code with message threads. But your token bill stays the same."
url: "https://thenewstack.io/anthropic-claude-message-threads"
link: "https://thenewstack.io/anthropic-claude-message-threads"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T13:46:14Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Anthropic has announced a new feature that aims to speed up long-running Claude Code sessions by reducing the amount of conversation data repeatedly sent to its API, helping developers get responses faster as their coding sessions grow. \n\n Message threads , as it’s called, is available now in public beta for Anthropic’s Messages API and is already enabled by default for “most” Claude Code users,…"
tags: ["AI", "AI Agents", "AI Engineering", "Developer tools"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 1353
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic speeds up Claude Code with message threads. But your token bill stays the same.

The New Stack · Paul Sawers · 2026-11-03

Anthropic speeds up Claude Code with message threads. But your token bill stays the same.
Anthropic has announced a new feature that aims to speed up long-running Claude Code sessions by reducing the amount of conversation data repeatedly sent to its API, helping developers get responses faster as their coding sessions grow.
Message threads, as it’s called, is available now in public beta for Anthropic’s Messages API and is already enabled by default for “most” Claude Code users, according to an article published by Anthropic on Monday.
The company says that the feature has reduced median time to first token (TTFT) — the time it takes Claude to begin generating a response — by approximately 35% for Claude Code requests containing between 500,000 and 1 million tokens.
Given that it’s now part of the Messages API, the feature also extends beyond Claude Code to developers building their own AI agents, particularly those handling lengthy conversations, repeated tool calls, and large amounts of data.
How message threads works
To understand what’s changed, it’s worth looking at how the Messages API has traditionally handled conversations.
Every time an agent sends a new request to Claude, it includes the entire conversation history. That means all messages and tool calls must be transmitted again, even though the API has previously received them.
For example, a coding agent working through a complex task will likely entail hundreds of API calls. As it reads files and modifies code, the conversation history grows, and by the time that history reaches 500,000 tokens, every subsequent request requires sending those 500,000 tokens again, along with whatever new information has been thrown into the mix.
The API then has to validate and tokenize the incoming data before Claude can begin responding. This rinse-and-repeat processing can add significant latency, particularly during lengthy coding sessions.
And so message threads switches things up by allowing Anthropic to temporarily retain the conversation history on its servers. The first request still sends the complete conversation, including any system prompts and tool definitions. But subsequent requests need only contain new messages and a reference to the previous response.
Behind the scenes, Anthropic reconstructs the full conversation on its servers before passing it to Claude, negating the need for the client to keep uploading the same information. This detail is important, because Claude still processes the entire conversation on every turn — if the history contains 500,000 tokens, the model still receives that context, even though the client has transmitted only the latest messages.
“While each request is smaller with message threads, Claude still reads the full conversation on every turn, so token usage stays the same.”
As such, message threads doesn’t inherently reduce API costs — Anthropic continues to charge for the tokens Claude processes. “While each request is smaller with message threads, Claude still reads the full conversation on every turn, so token usage stays the same,” the company notes.
Developers can, however, combine message threads with Claude’s existing prompt caching feature, which allows previously processed content to be reused at discounted token rates. The two features can work in tandem to reduce latency and processing costs respectively.
Anthropic identifies several use-cases where message threads could be particularly useful. These include long-running coding agents that accumulate file edits and tool results, computer-use agents that repeatedly capture screenshots, and applications handling large volumes of documents or images. In each case, avoiding repeated uploads reduces the amount of data transmitted during a session.
Guillaume Lebedel, co-founder and CTO of AI agent infrastructure company StackOne, took to LinkedIn on Tuesday to illustrate the potential benefits of message threads for computer-use agents, using a simulation to estimate how much data could be saved.
His calculations assume an agent captures one 150 KB screenshot at each step. Without message threads, the 50th request would need to upload approximately 7.5 MB of accumulated screenshots. With message threads, that request would carry just the latest screenshot, approximately 0.15 MB.
Across the entire 50-step session, the cumulative screenshot data uploaded would fall from roughly 191 MB to 7.5 MB — a reduction of approximately 25 times.
While these figures aren’t based on a live API test, they illustrate the potential benefits for agents that repeatedly upload large files. Indeed, Lebedel predicts that computer-use agents could spearhead adoption of the feature, with widespread uptake before the end of the year.
“My bet — computer-use agents adopt it before coding agents do, since a screenshot per step is what makes the resend heavy.”
“My bet — computer-use agents adopt it before coding agents do, since a screenshot per step is what makes the resend heavy, and most have it on by the end of December,” he writes.
How to use message threads
To implement the feature, Anthropic has introduced a new thread parameter to the Messages API. The initial request creates a thread by including thread={"type": "create"}, alongside the full conversation history, system prompt, and any tools being used.
Subsequent requests use thread={"type": "continue", "previous_message_id": first.id}, where first.id refers to the response ID returned by the initial request.
These follow-up requests contain only the new messages. The API retains the earlier conversation and its original system prompt and tool definitions.
Because the feature remains in beta, developers making requests directly must also include the anthropic-beta header with the value message-threads-2026-08-12. In the Python SDK, this can be supplied through betas=["message-threads-2026-08-12"].
Anthropic also provides a simpler approach through its SDK thread helper, which manages the conversation history and API parameters automatically.
Using the Python SDK, developers first create a client with client = anthropic.Anthropic(), before initialising a thread through client.beta.messages.thread(). The latter accepts the model, maximum output tokens and initial system prompt, among other parameters.
Once configured, developers use thread.send() to submit messages. The SDK thread helper automatically creates the thread on the first request, then continues it on subsequent turns, supplying the necessary parameters and retaining a local copy of the conversation history.
The SDK thread helper also adds the required beta header automatically, removing the need for developers to specify it with each request.
Message threads expire
There is, however, one notable limitation in all of this. Message threads expire after just five minutes of inactivity. And as one user observed on X, “Five minutes at the coffee machine and the thread expires.”
Another user went further, writing: “Only 5 minutes for cache expires is almost useless.” The user appears to be referring to the message thread expiry, which is separate from Claude’s prompt caching feature.
“Five minutes at the coffee machine and the thread expires.”
That might seem like an unforgiving restriction for a feature designed to improve lengthy coding sessions, however the implications are perhaps not so dramatic. If a developer steps away for ten minutes, say, the thread will indeed have expired. However, provided the client has retained the conversation history, the SDK helper automatically resends it to establish a new thread when they return. So the first request after a break may therefore take longer, but the coding session can continue without losing its previous context.
For agents operating continuously, the limitation may be even less consequential. Every successful request stored in the thread refreshes the five-minute expiry period, meaning an agent making regular API calls can maintain the same thread throughout a lengthy task.
Developers managing threads directly must handle expiry themselves. An attempt to continue an unavailable thread returns a 404 error, requiring the client to resend the complete conversation and establish a new thread.
There are also some data-handling considerations. Anthropic says thread contents are encrypted and held in server memory without being written to persistent storage. Although threads expire after five minutes of inactivity, their contents may remain in memory for up to an hour after their last use.
The feature is currently ineligible for zero data retention and HIPAA, which could restrict its use in environments with stringent data-handling requirements. Certain context-management capabilities, including on-demand compaction, are also unsupported.
Message threads is available across all Claude models in beta, including through Claude Platform on AWS, Claude in Microsoft Foundry, and Anthropic-managed Claude Models on Google Cloud.
Learning Path
