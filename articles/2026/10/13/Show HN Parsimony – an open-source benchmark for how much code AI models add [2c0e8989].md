---
id: "2c0e898929da0804"
title: "Show HN: Parsimony – an open-source benchmark for how much code AI models add"
url: "https://parsimony.lasu.dev"
source: "Parsimony"
domain: "parsimony.lasu.dev"
source_type: "community"
collector: "hackernews"
date: "2026-10-13T19:50:31Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["lasu"]
language: "en"
summary: "Existing benchmarks measure solve rate and token output/cost, but don't punish excess code, which makes a codebase harder to work with in the long term. I wanted to measure this since it matters most for long-term projects. Method: it takes the patches that benchmarks already publish (DeepSWE, SWE-bench Verified, SWE-bench Live) and counts \"coding units\": syntax elements like statements, calls,…"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 367
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50077619"
score: 70
comments: 14
community: "Hacker News"
---

# Show HN: Parsimony – an open-source benchmark for how much code AI models add

Parsimony · lasu · 2026-10-13

def has_negative(values):
    found = False
    for value in values:
        if value < 0:
            found = True
    return found
Parsimony
Existing benchmarks measure solve rate and cost, but don't punish excess code, which makes a codebase harder to work with in the long term. Parsimony measures how much code AI models add.
It takes the patches that benchmarks already publish and counts coding units: syntax elements like statements, calls, comparisons, names and literals. Lines aren't counted, so cramming code isn't rewarded, and deleted code is subtracted: net units = added − removed.
Compare models
How to read this
Models are ranked by mean net units added on the tasks they solved, lowest first. "Net units added (mean)" also includes failed attempts. Solved comes from SWE-bench Verified; tests aren't rerun. Measured is how many solved attempts could be measured.
The Artificial Analysis Intelligence Index is an outside score, matched by model and reasoning effort. It doesn't affect the rank.
Faded models were run by me on the first 3–10 DeepSWE Python tasks (OpenAI models with pi, Anthropic models with Claude Code) and graded with each task's own tests. They aren't verified or ranked. GPT-5.6 Sol ran both ways: my run added 0.88× the code of its published run.
Leaderboard
Data sources
Hashes
Method
- Each patch is applied to the task's code, and both versions of every changed file are parsed. Nothing is run.
- Tests, docs and generated files are left out. Only Python is measured.
- Pass/fail comes from SWE-bench's published results; tests aren't rerun.
Limits
- Smaller isn't always better: units measure size, not readability or design.
- Models that write more code also tend to solve more tasks (Spearman 0.33–0.60 on the boards with 26+ models).
- Every model uses the same agent (mini-SWE-agent), but the agent still affects how much code gets written.
Add your own benchmark
Have code-size numbers from another benchmark? Download the example file, fill in your results and open it to get the same chart and table. The file stays in your browser. Format and how to share it.
Example: check for a negative number
Both return the same result.
def has_negative(values):
    return any(value < 0 for value in values)
