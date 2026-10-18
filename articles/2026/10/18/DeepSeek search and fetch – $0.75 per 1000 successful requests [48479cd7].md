---
id: "48479cd7194ad72c"
title: "DeepSeek search and fetch – $0.75 per 1000 successful requests"
url: "https://api-docs.deepseek.com/guides/search"
link: "https://api-docs.deepseek.com/guides/search"
source: "DeepSeek"
domain: "api-docs.deepseek.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-18T06:50:36Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["fagnerbrack"]
language: "en"
summary: "Search & Fetch\nThe Search API and the Fetch API give agents and RAG applications access to live web content:\n- Search API finds web pages for a query and returns structured results. It is powered by DeepSeek's in-house search engine.\n- Fetch API retrieves a single web page and returns its content as Markdown.\nBoth are raw JSON APIs. They use the same bearer authentication as the DeepSeek…"
tags: []
orgs: ["DeepSeek", "OpenAI", "Anthropic", "China"]
topics: ["search & media", "models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 633
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50138531"
score: 261
comments: 119
community: "Hacker News"
---

# DeepSeek search and fetch – $0.75 per 1000 successful requests

DeepSeek · fagnerbrack · 2026-10-18

Search & Fetch
The Search API and the Fetch API give agents and RAG applications access to live web content:
- Search API finds web pages for a query and returns structured results. It is powered by DeepSeek's in-house search engine.
- Fetch API retrieves a single web page and returns its content as Markdown.
Both are raw JSON APIs. They use the same bearer authentication as the DeepSeek API.
The base URL is https://api.deepseek.com:
See the Search API Reference and Fetch API Reference for the complete request and response schemas.
Authentication
Send your API key and the JSON content type in the request headers:
Search API
Request
curl https://api.deepseek.com/v1/tools/search \
-H "Authorization: Bearer <DeepSeek API Key>" \
-H "Content-Type: application/json" \
-d '{
"query": "DeepSeek V4 release",
"count": 5,
"need_content": true
}'
import requests
response = requests.post(
"https://api.deepseek.com/v1/tools/search",
headers={
"Authorization": "Bearer <DeepSeek API Key>",
},
json={
"query": "DeepSeek V4 release",
"count": 5,
"need_content": True,
},
)
response.raise_for_status()
for result in response.json()["results"]:
print(result["title"], result["url"])
print(result["summary"])
Request fields:
Unknown fields in the request body are ignored.
Query Operators
The query is forwarded with its search syntax intact. The examples below combine operators with a search term; you can combine multiple operators in one query.
For example:
{
"query": "DeepSeek site:github.com OR site:huggingface.co lang:en after:2025",
"count": 10
}
Response
A successful request returns HTTP 200 with a results array. A normal search with no matches returns an empty array.
{
"results": [
{
"rerank_score": 2.4,
"title": "DeepSeek V4 model released",
"url": "https://example.com/deepseek-v4",
"snippet": "DeepSeek V4 is now available, with tool calling and long-context support.",
"summary": "DeepSeek has released the V4 model. The release adds improved tool calling and long-context support for agent workflows.",
"content": "DeepSeek V4 is now generally available...",
"site_name": "Example News",
"site_icon": "https://example.com/favicon.ico",
"date": "2026-06-01T00:00:00+00:00",
"authority": 3
}
]
}
Each item in results contains:
Fetch API
Request
curl https://api.deepseek.com/v1/tools/fetch \
-H "Authorization: Bearer <DeepSeek API Key>" \
-H "Content-Type: application/json" \
-d '{
"url": "https://example.com/article"
}'
import requests
response = requests.post(
"https://api.deepseek.com/v1/tools/fetch",
headers={
"Authorization": "Bearer <DeepSeek API Key>",
},
json={"url": "https://example.com/article"},
)
response.raise_for_status()
page = response.json()
print(page["title"])
print(page["content"])
Request fields:
Response
{
"title": "Example article",
"content": "# Example article\n\nArticle content."
}
Fetching is subject to the target site's availability and access policies.
Errors
Errors follow the OpenAI-compatible error format. The param field is always null.
{
"error": {
"message": "'count' must be between 1 and 50",
"type": "invalid_request_error",
"param": null,
"code": "invalid_request_error"
}
}
Search and Fetch are read-only. For HTTP 408, 429, or 5xx errors, wait and retry. For HTTP 402, top up your account before retrying. Do not retry other 4xx errors without changing the request.
Billing
Search and Fetch are billed per successful request, not by tokens or by the number of returned results:
A request is billable only when it returns HTTP 200 and produces a result (Search must return a non-empty results array, and Fetch must return page content). Failed requests, empty search results, and timeouts are not billed. count only controls how many results are returned and does not affect the per-request price.
Note: when you use the DeepSeek API through DeepSeek Harness, Claude Code, or Codex, server-side tool calls already hit the Search and Fetch APIs. These calls are currently free of charge; per-request billing starts at 00:00 Beijing time on November 1, 2026.
Rate Limits
For each account, Search and Fetch are limited independently, and traffic to one does not consume the other's quota:
The QPS (requests per second) limits are calculated at the account level, regardless of which API key is used, and are separate from the model concurrency limits. Requests above the account-level QPS limit receive HTTP 429. In addition to the account-level limit, Fetch is also subject to a per-domain QPS limit, and requests above that limit also receive HTTP 429.
