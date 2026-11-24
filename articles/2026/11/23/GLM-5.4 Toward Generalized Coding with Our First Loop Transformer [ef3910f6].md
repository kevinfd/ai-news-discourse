---
id: "ef3910f6a7af585b"
title: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer"
url: "https://simonwillison.net/2026/Nov/23/glm-54"
link: "https://simonwillison.net/2026/Nov/23/glm-54"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-23T23:40:49Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Simon Willison"]
language: "en"
summary: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer \nGLM 5.4 is now available from Chinese AI lab Z.ai. It's their first model to use a looped transformer architecture, which they describe like this: \n \n In a standard Transformer, each layer runs once per forward pass. In a Loop Transformer, a group of weight-shared layers runs for multiple iterations, refining the hidden states…"
tags: ["ai", "generative-ai", "llms", "llm", "pelican-riding-a-bicycle", "llm-release", "ai-in-china", "glm"]
orgs: ["OpenAI", "Anthropic", "China", "Thinking Machines"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 436
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# GLM-5.4: Toward Generalized Coding with Our First Loop Transformer

Simon Willison · Simon Willison · 2026-11-23

23rd November 2026 - Link Blog
GLM-5.4: Toward Generalized Coding with Our First Loop Transformer. GLM 5.4 is now available from Chinese AI lab Z.ai. It's their first model to use a looped transformer architecture, which they describe like this:
In a standard Transformer, each layer runs once per forward pass. In a Loop Transformer, a group of weight-shared layers runs for multiple iterations, refining the hidden states from the previous pass. This gives us a deeper network without increasing the parameter count.
This is the second mention of looped transformers I've seen in the past week - the first was Inkling 2 Mini from Thinking Machines Lab on November 20th, who said:
Inkling 2 Mini is a looped transformer, running the middle layers of the model three times for every token. This allows the model to apply more reasoning and reach the right answer with fewer tokens, especially on tasks such as agentic coding that depend on reasoning quality.
GLM 5.4 is not (yet?) available as open weights. I tried it out using the Z.ai API, for which I had to sign up for their Coding Plan subscription because 5.4 cannot currently be accessed through the regular API.
It turns out both coding plan and regular API share the same OpenAI-compatible Responses API (at https://api.z.ai/api/v1), and the API key for the coding plan worked with that and gave me access to the new model.
I built a llm-glm plugin, then realized that llm-zai by Tommy Hughes already exists! I've shipped mine purely because llm-zai doesn't yet support the new model, but I'll likely retire mine once that plugin catches up.
Here are pelicans for GLM-5.4 on low, high, and max. This is the max one:
I realized I never ran pelicans for GLM-5.3, so here those are for the same effort levels. They look similar in quality to 5.4.
It's interesting how GLM 5.1 and GLM 5.2 produced radically different pelicans from other models. The pelicans for 5.3 and 5.4 are much more comparable to those I get from OpenAI or Anthropic models - the previous generations had their own distinctive look.
I made a comparison grid showing the four generations of GLM pelicans all in one place. The style transition between 5.2 and 5.3 is pretty stark.
Recent articles
- Ladybird's first alpha release - 23rd November 2026
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
