---
id: "2be04bcaa0cad738"
title: "We tested two AI versions: 96.7% accuracy, same critical mistake"
url: "https://reddit.com/r/artificial/comments/1x922ye/we_tested_two_ai_versions_967_accuracy_same"
link: "https://reddit.com/r/artificial/comments/1x922ye/we_tested_two_ai_versions_967_accuracy_same"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T12:31:49Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Sosyaldijital"]
language: "en"
summary: "We recently ran a small experiment comparing JEV 1.13 and JEV 1.14 on Turkish-language intent classification. The goal was to identify whether a message came from someone looking to buy a service, someone offering a service, or neither. Here are the results: JEV 1.13: 29/30 correct (96.7%) JEV 1.14: 29/30 correct (96.7%) Buyer detection: 9/10 for both versions Average response time: 367 ms vs.…"
tags: ["r/artificial"]
orgs: []
topics: []
content_source: "post"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x922ye/we_tested_two_ai_versions_967_accuracy_same/"
score: null
comments: null
community: "r/artificial"
---

# We tested two AI versions: 96.7% accuracy, same critical mistake

Reddit · Sosyaldijital · 2026-10-18

We recently ran a small experiment comparing JEV 1.13 and JEV 1.14 on Turkish-language intent classification. The goal was to identify whether a message came from someone looking to buy a service, someone offering a service, or neither. Here are the results: JEV 1.13: 29/30 correct (96.7%) JEV 1.14: 29/30 correct (96.7%) Buyer detection: 9/10 for both versions Average response time: 367 ms vs. 352 ms Total API cost: approximately $0.00113 across 60 calls The interesting part? Both versions made the exact same mistake. A Turkish message explicitly expressing an intention to pay for product photo editing was classified as a seller rather than a potential buyer. This highlights an important limitation of relying on overall accuracy. A model can achieve 96.7% accuracy and still miss a valuable customer opportunity. In real-world lead detection, false negatives may be significantly more costly than false positives. A few important limitations: These results come from 30 synthetic Turkish scenarios, not a production dataset. Each version was tested once, so the sample is too small to establish reliable performance differences. We did not deploy either version based on these results. Our takeaway is simple: accuracy alone doesn't tell the full story. The impact of individual errors matters. I'm curious what others think: When evaluating AI classifiers for real-world applications, would you prioritize overall accuracy, recall for critical cases, or a cost-sensitive metric that penalizes missed opportunities? And how much testing would you consider sufficient before deploying such a system?
