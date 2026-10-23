---
id: "d49fb06684af59e0"
title: "OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation"
url: "https://thenewstack.io/openai-donates-open-responses"
link: "https://thenewstack.io/openai-donates-open-responses"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T16:01:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "OpenAI on Thursday announced that it is donating the Open Responses API specification to the open source Agentic AI Foundation (AAIF). \n\n In addition to Open Responses, OpenSandbox , Anthropic’s Agent Skills , and HuggingFace’s OpenEv framework for agent environments are also joining the AAIF. \n\n The join other AAIF projects like the MCP and A2A protocols, AGENTS.md (also from OpenAI), the open…"
tags: ["AI", "AI Agents", "Large Language Models", "Open Source"]
orgs: ["OpenAI", "Anthropic", "Hugging Face", "Amazon", "Google", "Meta", "Nvidia", "DeepSeek"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 550
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation

The New Stack · Frederic Lardinois · 2026-10-22

OpenAI donates Open Responses, its spec for a common LLM API, to the Agentic AI Foundation
OpenAI on Thursday announced that it is donating the Open Responses API specification to the open source Agentic AI Foundation (AAIF).
In addition to Open Responses, OpenSandbox, Anthropic’s Agent Skills, and HuggingFace’s OpenEv framework for agent environments are also joining the AAIF.
The join other AAIF projects like the MCP and A2A protocols, AGENTS.md (also from OpenAI), the open source AI agent goose, agentgateway, and Agent Router. The foundation, which is part of the Linux Foundation, launched in December 2025, with MCP, goose, and AGENTS.md as its first projects.
As for Open Responses, the core idea here is to provide developers with a set of core API calls that should work across LLM providers. When OpenAI first announced the specification in January, the team behind the project noted that virtually all LLM providers now offer the same building blocks (messages, tool calls, function calling, etc.), but that they also all represent them differently in their APIs.
Open Responses aims to create a spec that standardizes these primitives so that developers don’t have to translate between each vendor’s idiosyncratic API when they switch between models.
“When we co-founded AAIF, we contributed AGENTS.md, a way to give coding agents project-specific instructions,” an OpenAI spokesperson told The New Stack. “Open Responses addresses another part of building agents by giving developers a shared format for working with models across endpoints that support it, so they have fewer provider-specific integrations to maintain. Vercel AI Gateway and Databricks Model Serving already implement it, and AAIF will provide a neutral home for developers and providers to continue developing the specification together.”
Why a neutral home matters
It’s this neutral home that is generally the reason why companies donate projects to a foundation. The AAIF is part of the Linux Foundation, which has become somewhat of the de facto standard for providing vendor-neutral homes for popular open source projects, with a technical steering committee, which will initially be made up of project maintainers, handling the technical discussions.
Who already supports it — and who doesn’t
There is already wide support for the spec, with the likes of AWS (in Bedrock), Databricks, LM Studio, Ollama, Hugging Face, Nvidia, OpenRouter, Red Hat, Vercel, and open source projects like vLLM and OGC (previously Llama Stack) supporting it.
Among the names that are missing from this list is OpenAI’s rival Anthropic, which defines its own Messages API for giving developers access to its models. Anthropic is a member of the AAIF, so maybe we’ll see the company adopt this spec at some point in the future.
With the Interactions API, Google, too, has its default for letting developers work with its models.
Open Responses doesn’t hide its lineage. The project’s own contributor guide notes that its core schema files are copied from OpenAI’s API. And while OpenAI’s earlier Chat Completions API became an early standard that others used to model their offerings after, Anthropic’s Messages API has now also left a clear mark (in large part thanks to the success of Claude Code), with the likes of DeepSeek, Moonshot, Z.ai, MiniMax, and others exposing Anthropic-compatible endpoints, too.
That split is exactly the kind of fragmentation a vendor-neutral spec like this is meant to fix, of course.
