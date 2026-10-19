---
id: "af8de657f4ed1d9f"
title: "Google Open Sources Harness2 for Self Improving AI Agents"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9gfnb/google_open_sources_harness2_for_self_improving"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9gfnb/google_open_sources_harness2_for_self_improving"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T22:33:51Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["chemist_slime"]
language: "en"
summary: "Google just released Harness2 as open source. It turns any AI harness into a system that improves itself over time. A harness is everything around the model. System prompt, tools, memory, skills, and subagents. Normally a person designs it once and the agent uses that fixed setup for every new task. With Harness2 the agent itself refines the harness for each task. It proposes changes, runs a few…"
tags: ["r/LocalLLaMA"]
orgs: ["Google"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 157
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9gfnb/google_open_sources_harness2_for_self_improving/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Google Open Sources Harness2 for Self Improving AI Agents

Reddit · chemist_slime · 2026-10-18

Google just released Harness2 as open source. It turns any AI harness into a system that improves itself over time. A harness is everything around the model. System prompt, tools, memory, skills, and subagents. Normally a person designs it once and the agent uses that fixed setup for every new task. With Harness2 the agent itself refines the harness for each task. It proposes changes, runs a few candidate versions, and picks a better one by comparing how they perform. No correct answers or graders are needed. The model weights stay the same. What it learns on one task carries over to the next. After finishing a task it saves the improved harness and useful lessons so future edits start smarter instead of from scratch. Google tested it with Gemini 3.5 Flash and GLM-5 on legal, office, and professional work benchmarks. Even one round of edits beat the original harnesses. More rounds pushed scores higher. GitHub https://github.com/google-research/harness2
