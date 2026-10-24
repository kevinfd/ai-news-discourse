---
id: "99a3d5a0be254ec2"
title: "OpenAI opens Decisions API at $0.10 per million input tokens, targets TypeSafe's Jev category"
url: "https://vectorwire.ai/article/openai-opens-decisions-api-at-0-10-per-million-input-tokens-targets-typesafe-s-j-3fa377"
link: "https://vectorwire.ai/article/openai-opens-decisions-api-at-0-10-per-million-input-tokens-targets-typesafe-s-j-3fa377"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-10-23T14:45:41Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["VectorWireAI"]
language: "en"
summary: "OpenAI made its Decisions API generally available on October 22, 2026, pricing the endpoint at $0.10 per million input tokens with no charges for output tokens, cache reads, or cache writes2,4. The move puts OpenAI in direct competition with TypeSafe, the startup whose Jev model created the category of fast, structured \"decision\" or \"System One\" models that act as super-classifiers1.\nThe…"
tags: ["r/artificial"]
orgs: ["OpenAI"]
topics: ["models & research", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 355
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xdg1x1/openai_opens_decisions_api_at_010_per_million/"
score: null
comments: null
community: "r/artificial"
---

# OpenAI opens Decisions API at $0.10 per million input tokens, targets TypeSafe's Jev category

Vector Wire · VectorWireAI · 2026-10-23

OpenAI made its Decisions API generally available on October 22, 2026, pricing the endpoint at $0.10 per million input tokens with no charges for output tokens, cache reads, or cache writes2,4. The move puts OpenAI in direct competition with TypeSafe, the startup whose Jev model created the category of fast, structured "decision" or "System One" models that act as super-classifiers1.
The Decisions API runs on ChatGPT-Luna, reconfigured to accelerate inference rather than trained as a purpose-built decision model. It returns typed outputs — predicates estimating whether a condition is true, choices among predefined options, and scores against a rubric — rather than open-ended prose3. A single request can carry up to 400 questions, a ceiling raised from the beta period.
Speed and new modalities
OpenAI claims the endpoint runs up to 10 times faster than routing the same bounded decisions through the standard Responses API, with demonstrated latency of approximately 150 milliseconds. Nikunj Handa, OpenAI's API product lead, said the service shrank response times from one to three seconds down to 100–180 milliseconds. Other initial trial customers include Box, Datadog, Ramp, and Speak.
Between the beta, first announced at OpenAI's developer day on September 29, and general availability, OpenAI added native GPT-Live integration, prompt caching, and support for image and JSON inputs. Voice and visual modalities are new to the public release.
Competitive positioning
TypeSafe, founded by a former OpenAI researcher, reached a $7.6 billion valuation on the strength of Jev.
Handa told TechCrunch that colleagues saw Jev and identified numerous internal use cases, prompting a sprint to ship a competing product. He acknowledged that dedicated training could improve the model further but said ChatGPT-Luna handles the workload adequately today. OpenAI's own developer documentation recommends calibrating decision thresholds against labeled examples and weighing false-positive and false-negative costs before deployment.
ANALYSIS The pricing structure — input-only billing at $0.10 per million tokens — undercuts the economics of using general-purpose LLMs for classification and routing tasks, which is the core value proposition TypeSafe established with Jev. OpenAI's approach of repurposing an existing frontier model rather than training a specialized one trades benchmark standing for speed to market.
