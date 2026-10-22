---
id: "6464c40499c65172"
title: "We put 13 AI models in the GP's chair for the five free cases. Results, every transcript, and how they did on the penicillin allergy: discussion's over in r/artificial. Play the same cases: doctorfoo.ai"
url: "https://reddit.com/r/artificial/comments/1xcd42w/we_put_13_ai_models_in_the_gps_chair_for_the_five"
link: "https://reddit.com/r/artificial/comments/1xcd42w/we_put_13_ai_models_in_the_gps_chair_for_the_five"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T08:39:30Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["radeon2000"]
language: "en"
summary: "Disclosure first: I'm a GP registrar (family-medicine trainee) in Australia, and I make Crook, a commercial game in which you play the GP. The benchmark, results, transcripts and code are free and open; you don't need the game for any of it. What it is. A model sits in the doctor's chair and runs a consultation through tool calls: it talks to the patient in free text, examines, orders tests,…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Anthropic", "Google", "xAI", "DeepSeek"]
topics: ["models & research", "health & science", "policy & regulation"]
content_source: "post"
word_count: 488
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xcd42w/we_put_13_ai_models_in_the_gps_chair_for_the_five/"
score: null
comments: null
community: "r/artificial"
---

# We put 13 AI models in the GP's chair for the five free cases. Results, every transcript, and how they did on the penicillin allergy: discussion's over in r/artificial. Play the same cases: doctorfoo.ai

Reddit · radeon2000 · 2026-10-22

Disclosure first: I'm a GP registrar (family-medicine trainee) in Australia, and I make Crook, a commercial game in which you play the GP. The benchmark, results, transcripts and code are free and open; you don't need the game for any of it. What it is. A model sits in the doctor's chair and runs a consultation through tool calls: it talks to the patient in free text, examines, orders tests, prescribes, refers, and commits to a most-likely and a can't-miss diagnosis. The patient is an LLM, but it only voices a hand-written case and doesn't know its diagnosis. Every point is scored by code against the case key: red flags asked about, key history, indicated exams and tests, unnecessary tests penalised, harmful prescribing penalised hard. Run (21 Oct): 13 models × 5 cases × 3 plays = 195 consults, through OpenRouter at default settings, against the live game's Gemini Flash-Lite patient. What came out Diagnosis didn't separate the models. The right diagnosis was named in 191/195 consults; the other 4 ended without one (the model stopped calling tools). Scores still ran from 27% to 85%. Top: GPT-6.1 Sol and GPT-6 Astra (85%), then Gemini 4 Argon (82%), Qwen3.8 Max (81%), Claude Fable 5.1 (80%), Grok 4.7 (79%). Best open-weight model: DeepSeek V4 Pro (68%). The record is not the patient. One patient is allergic to penicillin, but his record says "nil known". He got penicillin in 16 of 39 consults, and in 14 of those the model never asked about allergies. Another patient took sildenafil the night before; GTN was given 5 times, never after asking about other medicines. Asking pays. Red flags found tracked questions asked (r = 0.88 across models). No model came near the 50-question budget. Cost: GPT-6.1 Sol scored 85% at about 3¢ a consult; Claude Fable 5.1 scored 80% at about $1.93. The ranking held against a run two weeks earlier with a different patient model and earlier scoring rules (Spearman 0.92, 11 models in both). A GP registrar who played each case once, briskly, scored 31%. That's not "AI beats doctors": the game has no clock and rewards exhaustive history, and it's one person over five consults. It's in the results as a reference point for reading the scale. Caveats: five draft cases, written by me; three plays a case; an LLM patient and an LLM judge for spoken advice (logged, with code-side checks). It's a score in a game, not a claim about fitness to practise medicine. Links Interactive results (sort, filter by lab, click a model to split it into its consults, read any transcript and itemised bill): https://woodytwoshoes.github.io/crook-bench/ Code, cases and raw results: https://github.com/woodytwoshoes/crook-bench Try the same five cases yourself (free, no sign-up): https://doctorfoo.ai A paper is on its way to arXiv. I'd love critique of the method, especially what you'd want as a baseline (a fixed checklist policy is next on my list) and which models to add.
