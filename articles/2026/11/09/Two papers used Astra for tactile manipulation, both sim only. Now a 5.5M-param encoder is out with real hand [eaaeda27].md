---
id: "eaaeda274e1cb557"
title: "Two papers used Astra for tactile manipulation, both sim only. Now a 5.5M-param encoder is out with real hand results"
url: "https://reddit.com/r/singularity/comments/1xs07lh/two_papers_used_astra_for_tactile_manipulation"
link: "https://reddit.com/r/singularity/comments/1xs07lh/two_papers_used_astra_for_tactile_manipulation"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T18:53:53Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Alternative_Set4042"]
language: "en"
summary: "Last month two preprints fed GPT-6 Astra tactile images and got decent sim results, but both were simulation only and one had a median of about 14 seconds per model call. Robbyant just released LingBot-Touch, a 5.46M-parameter tactile encoder trained on magnetic, piezoresistive and camera-based sensors, tested on real five-finger hands. Code and weights are on GitHub and Hugging Face. Plugged…"
tags: ["r/singularity"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 107
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xs07lh/two_papers_used_astra_for_tactile_manipulation/"
score: null
comments: null
community: "r/singularity"
---

# Two papers used Astra for tactile manipulation, both sim only. Now a 5.5M-param encoder is out with real hand results

Reddit · Alternative_Set4042 · 2026-11-09

Last month two preprints fed GPT-6 Astra tactile images and got decent sim results, but both were simulation only and one had a median of about 14 seconds per model call. Robbyant just released LingBot-Touch, a 5.46M-parameter tactile encoder trained on magnetic, piezoresistive and camera-based sensors, tested on real five-finger hands. Code and weights are on GitHub and Hugging Face. Plugged into pi0.5 it bumped 26-task scores from 48 to about 70 (partial credit, not binary success rates). Only two hand types tested so far, and there's basically no palm coverage. These feel complementary to me: the big model does the planning, the small encoder handles contact.
