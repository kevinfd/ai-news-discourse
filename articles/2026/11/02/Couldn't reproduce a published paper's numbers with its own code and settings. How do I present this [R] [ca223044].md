---
id: "ca223044b496ab25"
title: "Couldn't reproduce a published paper's numbers with its own code and settings. How do I present this? [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xm64of/couldnt_reproduce_a_published_papers_numbers_with"
link: "https://reddit.com/r/MachineLearning/comments/1xm64of/couldnt_reproduce_a_published_papers_numbers_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T19:00:24Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["InsectActive95"]
language: "en"
summary: "I'm writing a machine learning paper. One of my baselines is a published method. I reran it with the authors' released code and the exact hyperparameters listed in their paper. On most benchmarks my numbers match theirs within noise, but on two benchmarks my reproduction is clearly lower, by several points, over three seeds. I've repeated the reproduction four different times, months apart, with…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 207
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xm64of/couldnt_reproduce_a_published_papers_numbers_with/"
score: null
comments: null
community: "r/MachineLearning"
---

# Couldn't reproduce a published paper's numbers with its own code and settings. How do I present this? [R]

Reddit · InsectActive95 · 2026-11-02

I'm writing a machine learning paper. One of my baselines is a published method. I reran it with the authors' released code and the exact hyperparameters listed in their paper. On most benchmarks my numbers match theirs within noise, but on two benchmarks my reproduction is clearly lower, by several points, over three seeds. I've repeated the reproduction four different times, months apart, with the same result. I plan to report both: their published numbers and my reproduction with the exact configuration, clearly labeled. My worry is that reviewers tend to trust the published number more than a submission's reproduction, and may assume I ran the baseline incorrectly. Questions: What makes a reproduction convincing to reviewers? So far I have: the authors' code unchanged, their hyperparameters, matching results on the other benchmarks as a sanity check, and multiple seeds. Should I contact the authors or open a GitHub issue first, and should I mention that in the paper? How do I word it so it doesn't read as an attack on the other paper, but my results also don't look weak next to the published numbers? Have reviewers accepted "published vs. reproduced" rows in a main table for you, or did they end up in the appendix?
