---
id: "d18ddef895ab8451"
title: "Running PR reviews on a local model: what i learned building an open-source code reviewer"
url: "https://reddit.com/r/LocalLLaMA/comments/1x79hfw/running_pr_reviews_on_a_local_model_what_i"
link: "https://reddit.com/r/LocalLLaMA/comments/1x79hfw/running_pr_reviews_on_a_local_model_what_i"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T07:09:51Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["mattjcoles"]
language: "en"
summary: "i built lgtmaybe, an open-source code reviewer, and a lot of the work went into making it usable on a local model. Big files get reviewed a hunk at a time, and big diffs get split to fit the context window, so a 27B model copes fine. The default is five model calls per review, which is fine on one GPU. Which local models have you found actually good at code review? Keen to pick better defaults.…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 78
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x79hfw/running_pr_reviews_on_a_local_model_what_i/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Running PR reviews on a local model: what i learned building an open-source code reviewer

Reddit · mattjcoles · 2026-10-16

i built lgtmaybe, an open-source code reviewer, and a lot of the work went into making it usable on a local model. Big files get reviewed a hunk at a time, and big diffs get split to fit the context window, so a 27B model copes fine. The default is five model calls per review, which is fine on one GPU. Which local models have you found actually good at code review? Keen to pick better defaults. https://github.com/MattJColes/lgtmaybe
