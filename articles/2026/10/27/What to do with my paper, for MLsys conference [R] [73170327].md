---
id: "7317032785161525"
title: "What to do with my paper, for MLsys conference? [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xguzyz/what_to_do_with_my_paper_for_mlsys_conference_r"
link: "https://reddit.com/r/MachineLearning/comments/1xguzyz/what_to_do_with_my_paper_for_mlsys_conference_r"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T15:05:38Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Significant_Bee_2025"]
language: "en"
summary: "For my master’s thesis I built an accelerator for diffusion-based action generation in robotics policies. Offline, it looks great: the median absolute deviation between the accelerated output and the original model’s output is extremely small, so I concluded it reproduces the model’s behavior faithfully. When I deployed it on a real robot for a task (picking up a book and placing it on a shelf),…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "robotics & autonomy"]
content_source: "post"
word_count: 198
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xguzyz/what_to_do_with_my_paper_for_mlsys_conference_r/"
score: null
comments: null
community: "r/MachineLearning"
---

# What to do with my paper, for MLsys conference? [R]

Reddit · Significant_Bee_2025 · 2026-10-27

For my master’s thesis I built an accelerator for diffusion-based action generation in robotics policies. Offline, it looks great: the median absolute deviation between the accelerated output and the original model’s output is extremely small, so I concluded it reproduces the model’s behavior faithfully. When I deployed it on a real robot for a task (picking up a book and placing it on a shelf), it did not work as well as the original model. The offline numbers did not predict the real-world result. I want to submit this to MLSys. My offline results are strong, but the deployment result is negative. My questions: Is it acceptable to submit with only the offline results, or should I include the failed deployment? If I include it, how do I frame it so it adds to the paper instead of sinking it? Why might a tiny median deviation still lead to task failure? My guesses are tail errors and error compounding in closed loop, but I would like other views. What additional metrics would you report (percentiles, per-step error, closed-loop success rate in simulation)? Any experience from people who have submitted systems papers with negative real-world results is very welcome.
