---
id: "5da64e98b51748c1"
title: "I had Opus 5.5 plan my project and pick the model + effort for each session. It worked great"
url: "https://reddit.com/r/ClaudeAI/comments/1xpk6uw/i_had_opus_55_plan_my_project_and_pick_the_model"
link: "https://reddit.com/r/ClaudeAI/comments/1xpk6uw/i_had_opus_55_plan_my_project_and_pick_the_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T18:25:50Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Throwaway_SQ2"]
language: "en"
summary: "I tried a workflow on my last project and it went really well, so I'm sharing it. What I did: **Planning with Opus 5.5 on max effort.** I described the whole project and asked it to make a full plan. **Splitting into sessions.** I had it break the plan into separate sessions, each a self-contained chunk of work. **Rating each session.** For every session it rated how hard the task was, then told…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 264
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpk6uw/i_had_opus_55_plan_my_project_and_pick_the_model/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I had Opus 5.5 plan my project and pick the model + effort for each session. It worked great

Reddit · Throwaway_SQ2 · 2026-11-06

I tried a workflow on my last project and it went really well, so I'm sharing it. What I did: **Planning with Opus 5.5 on max effort.** I described the whole project and asked it to make a full plan. **Splitting into sessions.** I had it break the plan into separate sessions, each a self-contained chunk of work. **Rating each session.** For every session it rated how hard the task was, then told me exactly which model (Haiku, Sonnet or Opus) and which effort level that session needed. **Making a build .md file.** All of this went into one markdown file covering the plan, the sessions, and the model/effort for each. How I ran it: * Each session is a new Claude Code conversation. * I upload the build .md file first so Claude has the full context. * I set the model and effort the plan recommended, then tell it which session to work on. Why it worked: * I didn't burn Opus max on simple stuff like boilerplate, renaming or small fixes. Haiku or Sonnet handled those fine. * The hard parts got the heavy model and high effort. * Starting each session fresh with the .md file kept the context clean. I wasn't dragging one giant conversation along. * The sessions were consistent because they all worked from the same plan. It's basically using the smartest model as a project manager and the cheaper models as the workers. Has anyone else tried something like this? I'm curious if you split sessions differently or let Claude pick the model on its own.
