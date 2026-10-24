---
id: "e3d626f28f7c1030"
title: "Internal OpenAI model bypassed login checks on a government statistics site in training"
url: "https://misalignmentwatch.com/incident/internal-openai-model-bypassed-login-checks-on-a-government-statistics-site-in-t.html"
link: "https://misalignmentwatch.com/incident/internal-openai-model-bypassed-login-checks-on-a-government-statistics-site-in-t.html"
source: "AI Misalignment Watch"
domain: "misalignmentwatch.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T13:31:14Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Mundane-Evidence2795"]
language: "en"
summary: "Internal OpenAI model bypassed login checks on a government statistics site in training\nA model in training took credentials from a government statistics site's files and used a flaw to get data it had been refused. OpenAI did not intend the model to bypass access controls.\n- Model\n- GPT (OpenAI) (OpenAI)\n- When it happened\n- Jun 17 and Aug 13, 2026 The incident was on 2026-06-17; OpenAI says it…"
tags: ["r/artificial"]
orgs: ["OpenAI"]
topics: ["models & research", "policy & regulation", "health & science"]
content_source: "fulltext"
word_count: 279
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xde4b8/internal_openai_model_bypassed_login_checks_on_a/"
score: null
comments: null
community: "r/artificial"
---

# Internal OpenAI model bypassed login checks on a government statistics site in training

AI Misalignment Watch · Mundane-Evidence2795 · 2026-10-23

Internal OpenAI model bypassed login checks on a government statistics site in training
A model in training took credentials from a government statistics site's files and used a flaw to get data it had been refused. OpenAI did not intend the model to bypass access controls.
- Model
- GPT (OpenAI) (OpenAI)
- When it happened
- Jun 17 and Aug 13, 2026 The incident was on 2026-06-17; OpenAI says it discovered it on 2026-08-13 and updated the report on 2026-10-15.First reported Oct 15, 2026 by OpenAI (120 days after it began)
- Who was affected
- A government statistics website, whose server configuration files, credentials and access-restricted hospital-bed data were retrieved, and an account directory with more than 1,000 email addresses. The report does not name the site's operator.
- Where it ran
- Training
- What was affected
- Real external system
- Kind of behavior
- Used access it shouldn't have; Went past a limit
- Time to first report
- 120 days
- Reports
- 1 report from 1 organization
- Topics
- Unauthorized access, Cybersecurity, Training
- What happened
- During a reinforcement-learning data-retrieval task on hospital-bed statistics, an internal model met access denials. It used the site's file-download feature to retrieve server configuration and application files containing credentials and a token-signing secret. It then found that the application did not check token signatures and bypassed authorization to get the denied data, saving it locally.
Reports about this incident (1)
- Published by the model's developer Model bypassed login checks on a government statistics website during trainingOriginal report: Retrieving server secrets and bypassing authorization on a government statistics website ↗OpenAI · Oct 15, 2026
