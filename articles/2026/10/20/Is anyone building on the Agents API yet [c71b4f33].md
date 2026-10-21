---
id: "c71b4f3341646ef1"
title: "Is anyone building on the Agents API yet?"
url: "https://reddit.com/r/OpenAI/comments/1xaqum8/is_anyone_building_on_the_agents_api_yet"
link: "https://reddit.com/r/OpenAI/comments/1xaqum8/is_anyone_building_on_the_agents_api_yet"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T12:30:11Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["apricot_dragon"]
language: "en"
summary: "We moved our agent backend onto the Agents API a few weeks ago, and I'm curious who else has. Why we bet on it: we watched Chat Completions go from one company's endpoint in 2023 to the shape almost every provider speaks now. OpenRouter, Groq, Ollama, vLLM, even Google and Anthropic for their own models. Nobody voted, developers just had code written against it and everyone followed. Agents feel…"
tags: ["r/OpenAI"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding"]
content_source: "post"
word_count: 174
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xaqum8/is_anyone_building_on_the_agents_api_yet/"
score: null
comments: null
community: "r/OpenAI"
---

# Is anyone building on the Agents API yet?

Reddit · apricot_dragon · 2026-10-20

We moved our agent backend onto the Agents API a few weeks ago, and I'm curious who else has. Why we bet on it: we watched Chat Completions go from one company's endpoint in 2023 to the shape almost every provider speaks now. OpenRouter, Groq, Ollama, vLLM, even Google and Anthropic for their own models. Nobody voted, developers just had code written against it and everyone followed. Agents feel like they're at the same point, and the Agents API already has the pieces a real agent needs: agents, sessions, turns, events, files, skills. How we use it: we dropped our own SDK and use the official openai package. Our code talks to agents and sessions in the API's shape, so changing where they run is a base URL change, not a rewrite. That alone made it worth it for us. It's still in beta, so I'm curious: Are you using it in production or still testing? What are you building with it? Anything missing that's kept you on Chat Completions or the Responses API?
