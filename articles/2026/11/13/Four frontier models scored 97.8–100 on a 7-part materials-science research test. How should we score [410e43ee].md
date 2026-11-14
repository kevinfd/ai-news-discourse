---
id: "410e43ee9e80cc80"
title: "Four frontier models scored 97.8–100 on a 7-part materials-science research test. How should we score long-horizon agent evals instead? [d]"
url: "https://reddit.com/r/MachineLearning/comments/1xvgf6h/four_frontier_models_scored_978100_on_a_7part"
link: "https://reddit.com/r/MachineLearning/comments/1xvgf6h/four_frontier_models_scored_978100_on_a_7part"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T18:58:00Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["v_aravind"]
language: "en"
summary: "I work in graphene and 2D materials, and I built a test of the everyday technical work in a research group. It has seven parts: reducing a messy tensile data set against a lab SOP (with unit and outlier traps), writing a CIF density function checked on three hidden structures, four back-of-envelope physics calculations, critiquing a manuscript with 10 planted errors and 6 correct-but-suspicious…"
tags: ["r/MachineLearning"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 376
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xvgf6h/four_frontier_models_scored_978100_on_a_7part/"
score: null
comments: null
community: "r/MachineLearning"
---

# Four frontier models scored 97.8–100 on a 7-part materials-science research test. How should we score long-horizon agent evals instead? [d]

Reddit · v_aravind · 2026-11-13

I work in graphene and 2D materials, and I built a test of the everyday technical work in a research group. It has seven parts: reducing a messy tensile data set against a lab SOP (with unit and outlier traps), writing a CIF density function checked on three hidden structures, four back-of-envelope physics calculations, critiquing a manuscript with 10 planted errors and 6 correct-but-suspicious decoys, false-premise and fabricated-paper questions with calibration scoring, an experimental design, and an abstract under constraints. All the data are synthetic, the answer keys are computed by code, and it's scored out of 100 across 8 categories. Setup: Gemini 4 Carbon and Gemini 4 Hydrogen (Antigravity), Claude Opus 5.5 and Claude Fable 5.2 (Claude app). All at "High", not max. 3 fresh runs each, files attached, prompt pasted, nothing else. Web search and code execution were on. Results: mean scores were 100.0 / 99.7 / 99.3 / 98.5, all 12 runs fell between 97.8 and 100, and each took 7–24 min. Every run caught the unit trap, passed the hidden CIF tests, got the subtle physics right (Krenchel 8/15 for platelets, graphene quantum capacitance), found all 10 planted errors with zero false positives, and refused the false premise and the fake paper. The points lost were formatting trivia. Three runs found a real error in the manuscript that I hadn't planted. Caveats: one examiner, n=3 per model, and I designed the test with Claude Opus 5.5's help (the Gemini models came out on top anyway). My read is that this is consistent with FrontierScience, METR time horizons and PaperBench: bounded work with a known procedure is saturated, and the gap is in long-horizon, open-ended work. Next I'm building a simulated-lab campaign: the agent gets a budget, instruments and a target spec, with planted surprises of the kind real projects have and a signed log of every action, for runs of 2–6 hours. Questions for the sub: how are people scoring the trajectory (e.g. recovery from a wrong early assumption) separately from the final output in long-horizon evals? And has anyone run measured human baselines on agentic tasks of that length? PhD student: my estimate of 11–16 hours of focused work and an expected score of 75–90, not a measurement. Full write-up: https://aiamnano.substack.com/p/frontier-ai-models-vs-phd-student
