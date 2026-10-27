---
id: "4cd4ee44e5c10169"
title: "There are now 5 inference providers for abliterated DeepSeek"
url: "https://allmodels.io/llm/abliterated"
link: "https://allmodels.io/llm/abliterated"
source: "AllModels"
domain: "allmodels.io"
source_type: "community"
collector: "hackernews"
date: "2026-10-27T04:53:52Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["moeadham"]
language: "en"
summary: "A fast reasoning model served by several independent providers. AllModels keeps text routes in the fallback pool and sends image requests only to a provider that can actually read them.\nAbliterated Model Router\nOne endpoint for every abliterated model.\nimport OpenAI from \"openai\";\nconst client = new OpenAI({\n  apiKey: process.env.ALLMODELS_API_KEY,\n  baseURL:…"
tags: []
orgs: ["OpenAI", "DeepSeek"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 391
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50254836"
score: 80
comments: 82
community: "Hacker News"
---

# There are now 5 inference providers for abliterated DeepSeek

AllModels · moeadham · 2026-10-27

A fast reasoning model served by several independent providers. AllModels keeps text routes in the fallback pool and sends image requests only to a provider that can actually read them.
Abliterated Model Router
One endpoint for every abliterated model.
import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.ALLMODELS_API_KEY,
  baseURL: "https://api.allmodels.io/oai",
});
const response = await client.responses.create({
  model: "deepseek/deepseek-v4.1-flash-abliterated",
  input: "Open the pod bay doors.",
});
console.log(response.output_text);import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["ALLMODELS_API_KEY"],
    base_url="https://api.allmodels.io/oai",
)
response = client.responses.create(
    model="deepseek/deepseek-v4.1-flash-abliterated",
    input="Open the pod bay doors.",
)
print(response.output_text)
Abliterated GLM 5.3 deployments from multiple providers share one public model ID. Route through the default waterfall or explicitly choose a provider when a particular price or limit matters.
More models available
Explore every abliterated model.
DeepSeek and GLM are only the starting point. Browse the full catalogue as new abliterated models and competitive provider routes become available.
Federated model access
One connection to the entire abliterated ecosystem.
AllModels continuously brings new abliterated models and competitive inference providers into one routing layer. Get the latest models, provider diversity, and capacity failover through a single security-hardened API—without rebuilding your integration each time the market moves.
POST /oai/chat/completions
          Use messages, streaming, function tools, and the familiar OpenAI chat schema.
POST /oai/responses
          Use input items, streaming events, reasoning controls, structured output, custom tools, and hosted web search.
Router-hosted web search
External search through one controlled layer.
Search is processed at AllModels instead of being delegated to whichever inference provider serves the request. Every model gets the same OpenAI-compatible search calls and URL citations, even when its provider does not offer search.
tools: [{ type: "web_search" }]
          web_search_options: { search_context_size: "medium" }
          Automated fallbacks
Stay online when a provider runs out of capacity.
AllModels routes each request across compatible providers. If one is unavailable or capacity constrained, traffic falls back automatically—without changing your model ID or application code.
Every request reaches a compatible route.
Image and multimodal requests only go to providers that support them, while text requests can use every eligible text route.
Provider capacity is handled for you.
When one provider is overloaded or unavailable, AllModels automatically tries the next eligible route for the same model.
Find the lowest price as providers come online.
AllModels keeps provider pricing current and can route to the lowest-cost eligible option as new inference providers become available.
