---
id: "fbcaca7364460da2"
title: "Using an MCP inside of the Claude.ai sandbox"
url: "https://reddit.com/r/ClaudeAI/comments/1xmw2g6/using_an_mcp_inside_of_the_claudeai_sandbox"
link: "https://reddit.com/r/ClaudeAI/comments/1xmw2g6/using_an_mcp_inside_of_the_claudeai_sandbox"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T15:32:28Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["g1ven2fly"]
language: "en"
summary: "I run a free MCP server that provides publicly available oil and gas data. And one of my limitations has always been around large datasets (bigger than the model context). There isn't a real good way for me to provide the user data inside of their Claude sandbox... programmatic tool calling doesn't support tools provided by an MCP. I'm not sure why, but it's clear as day inside of the docs.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 170
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmw2g6/using_an_mcp_inside_of_the_claudeai_sandbox/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Using an MCP inside of the Claude.ai sandbox

Reddit · g1ven2fly · 2026-11-03

I run a free MCP server that provides publicly available oil and gas data. And one of my limitations has always been around large datasets (bigger than the model context). There isn't a real good way for me to provide the user data inside of their Claude sandbox... programmatic tool calling doesn't support tools provided by an MCP. I'm not sure why, but it's clear as day inside of the docs. Well, I did some digging last night and it seems like there is already a workaround. Because the Claude.ai sandbox is really just a claude code cloud session, the mcp already has this built in: successful results that exceed the default threshold are persisted to disk and replaced with a file reference in the conversation. source So now when the MCP returns too much data, Claude writes it to a disk, then reads it within it's sandbox. I know this is incredible niche, but it's been a problem for me for a while and figured I'd at least share.
