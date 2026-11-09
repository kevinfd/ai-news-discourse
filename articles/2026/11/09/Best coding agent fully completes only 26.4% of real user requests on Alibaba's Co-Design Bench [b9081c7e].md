---
id: "b9081c7e8db2b399"
title: "Best coding agent fully completes only 26.4% of real user requests on Alibaba's Co-Design Bench"
url: "https://vectorwire.ai/article/best-coding-agent-fully-completes-only-26-4-of-real-user-requests-on-alibaba-s-c-6d352b"
link: "https://vectorwire.ai/article/best-coding-agent-fully-completes-only-26-4-of-real-user-requests-on-alibaba-s-c-6d352b"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-11-09T01:42:26Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["VectorWireAI"]
language: "en"
summary: "GPT-6 Astra, the top performer among ten models tested on a new coding-agent benchmark built from real user requests, fully completed only 26.4% of 273 tasks, according to a paper posted to arXiv on October 26 by researchers from Alibaba Group Holding and several Asian universities"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI", "Alibaba", "Anthropic", "xAI"]
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "fulltext"
word_count: 491
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xrf430/best_coding_agent_fully_completes_only_264_of/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Best coding agent fully completes only 26.4% of real user requests on Alibaba's Co-Design Bench

Vector Wire · VectorWireAI · 2026-11-09

GPT-6 Astra, the top performer among ten models tested on a new coding-agent benchmark built from real user requests, fully completed only 26.4% of 273 tasks, according to a paper posted to arXiv on October 26 by researchers from Alibaba Group Holding and several Asian universities1,2.
The model passed 69.9% of each task's hidden acceptance criteria on average, but satisfied every criterion on roughly one in four tasks. The gap means that in most cases an agent handles the bulk of the work but leaves at least one detail unfinished, requiring a person to clean up by hand, as The Decoder reported.
How the benchmark works
Co-Design Bench draws on 37,463 deduplicated requests from 26,314 real coding sessions. The authors selected candidates partly on signals of past failure — a user rephrasing a request two or more times, repeated follow-ups, or an explicit rollback — then had experts refine each request and write hidden grading rubrics totaling 2,331 criteria. Each request is fixed, so agents cannot ask follow-up questions or receive mid-task corrections. Tasks fall into two tracks: localized multimodal edits and repository-level edits. Agents must rework existing web applications based on user requests, sometimes using images, audio recordings, videos, or documents as input.
The authors justified the new test by pointing to the saturation of existing benchmarks: when models can run, check, and fix their own code, they hit scores above 99% on those tests, and differences between models can barely be measured.
Model rankings and harness effects
Behind GPT-6 Astra, Claude Opus 5 and Qwen3.8 Max Preview took the next spots, while xAI's Grok 4.6 landed in last place. Multi-file repository edits proved hardest: GPT-6 Astra fully solved 17.9% of them, against 41.0% of localized multimodal edits. ANALYSIS The steep drop from localized edits to repository-level edits is consistent with the authors' finding that performance declined as tasks combined more types of changes.
The main comparison ran every model through Claude Code as the harness. Swapping the agent harness moved Qwen3.8 27B's repository score from 0.560 to 0.749, prompting the authors to recommend that model and harness be reported together.
Token consumption varied widely: GLM-5.2 used a median of about 7.29 million tokens per task on multimodal edits, nearly six times the roughly 1.24 million tokens consumed by GPT-6 Astra on smaller changes, yet still scored significantly worse.
ANALYSIS The results put benchmark saturation on older tests into sharper relief: partial completion is the norm on tasks drawn from real user struggles, even for the highest-ranked model. Together AI's recent work using coding agents to optimize GPU kernels illustrates how infrastructure teams are already absorbing agent-driven iteration loops[3]. Co-Design Bench's insistence on pairing model identity with harness identity adds a methodological constraint that, if adopted, would make future leaderboard comparisons more granular.
A separate study by METR found that the actual acceptance rate of AI-generated code by project leads was roughly 24 percentage points below scores on SWE-bench Verified.
