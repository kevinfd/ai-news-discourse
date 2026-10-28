---
id: "c6f9c3d7a77aae8a"
title: "Tested 5 models as agents in Salesforce CRM"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xh1pks/tested_5_models_as_agents_in_salesforce_crm"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xh1pks/tested_5_models_as_agents_in_salesforce_crm"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T19:10:26Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["TruthDeep8659"]
language: "en"
summary: "I recently ran a study on how well AI agents handle real work inside Salesforce, and one result in particular seemed worth sharing with people building agents. Each model (Claude Opus, Sonnet, Haiku, GPT-6.1 Sol and DeepSeek) worked through 50 tasks with eight tools, and every attempt was graded on what actually changed in the database, not on the agent's final reply. A few things that stood…"
tags: ["r/ArtificialInteligence"]
orgs: ["Salesforce", "OpenAI", "Anthropic", "DeepSeek"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 141
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xh1pks/tested_5_models_as_agents_in_salesforce_crm/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Tested 5 models as agents in Salesforce CRM

Reddit · TruthDeep8659 · 2026-10-27

I recently ran a study on how well AI agents handle real work inside Salesforce, and one result in particular seemed worth sharing with people building agents. Each model (Claude Opus, Sonnet, Haiku, GPT-6.1 Sol and DeepSeek) worked through 50 tasks with eight tools, and every attempt was graded on what actually changed in the database, not on the agent's final reply. A few things that stood out: When I made the save tool return "success" without saving, every model reported at least 15 of 20 of those as done The models that re-checked a record after changing it scored higher Most failures came from things the request didn't mention, like fields Salesforce changes on its own Having tools return the saved record after every write would likely fix most of these If anyone's interested: Write-up: https://outsideengineer.substack.com/p/evaluating-ai-agents-on-salesforce Code and transcripts: https://github.com/brianna-rose05/crm-agent-bench
