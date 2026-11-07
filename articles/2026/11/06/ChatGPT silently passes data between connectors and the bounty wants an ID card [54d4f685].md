---
id: "54d4f685c5e08499"
title: "ChatGPT silently passes data between connectors and the bounty wants an ID card"
url: "https://community.openai.com/t/security-follow-up-tool-call-silently-routed-to-a-different-connector/1413053"
link: "https://community.openai.com/t/security-follow-up-tool-call-silently-routed-to-a-different-connector/1413053"
source: "OpenAI"
domain: "community.openai.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T22:50:43Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Aldipower"]
language: "en"
summary: "In a conversation with two connectors enabled, ChatGPT made a follow-up tool call through a different connector than the one that started the flow. The user was not told about the switch. The call carried a one-time confirmation code from the first connector’s widget.\nSetup\n- One ChatGPT account with two connectors enabled that point to the same MCP server.\n- Connector A is a custom connector…"
tags: []
orgs: ["OpenAI"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "fulltext"
word_count: 415
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50399569"
score: 89
comments: 36
community: "Hacker News"
---

# ChatGPT silently passes data between connectors and the bounty wants an ID card

OpenAI · Aldipower · 2026-11-06

In a conversation with two connectors enabled, ChatGPT made a follow-up tool call through a different connector than the one that started the flow. The user was not told about the switch. The call carried a one-time confirmation code from the first connector’s widget.
Setup
- One ChatGPT account with two connectors enabled that point to the same MCP server.
- Connector A is a custom connector added in developer mode.
- Connector B is the published app from the app directory.
- Each connector has its own OAuth client, so the server sees two separate clients for the same user.
Steps
1. In a conversation with both connectors enabled, ask for an action that needs the user’s confirmation.
2. The model calls a confirmation tool through connector A. Its MCP Apps widget shows the change. The user confirms, and the widget sends a one-time confirmation code to the conversation via ui/message.
3. The model makes the follow-up call with that code, but silently through connector B instead of connector A.
Result
The server rejects the call, because the code is bound to connector A’s OAuth client. Every attempt in that conversation failed. In the attempt we logged in detail, the code was confirmed through connector A and redeemed through connector B. Nothing told the user that the follow-up call went to another connector.
Why this is a problem?
The user starts the flow with connector A and confirms in connector A’s widget. The follow-up call then goes to connector B without the user knowing, and it carries a value produced in connector A’s widget. Connectors are separate apps with separate OAuth grants, so this silent switch passes data from one app to another without the user’s consent.
Here both connectors came from the same provider, so our server-side binding stopped the call. With a third-party connector enabled in the same conversation, we expect the same silent switch to pass one app’s data to another provider if the server URL is shared.
A shared MCP URL is not enough to treat two connectors as one. Behind the same URL, a server can act for different parties depending on the OAuth client, for example separate tenants, partners or environments. The boundary is the connector with its own OAuth client, not the URL.
Expected behavior
Tool calls are matched to a connector by its OAuth client, not by the MCP server URL. A follow-up call goes through the same connector and OAuth client that started the flow.
