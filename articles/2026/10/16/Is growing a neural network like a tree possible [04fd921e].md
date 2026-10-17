---
id: "04fd921edd4a97a7"
title: "Is growing a neural network like a tree possible?"
url: "https://reddit.com/r/OpenAI/comments/1x7eutp/is_growing_a_neural_network_like_a_tree_possible"
link: "https://reddit.com/r/OpenAI/comments/1x7eutp/is_growing_a_neural_network_like_a_tree_possible"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T12:26:37Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Sevdat"]
language: "en"
summary: "I got the idea from Tree graphs and Genetic Algorithms. Instead of training an AI, what if we just start from a node that branches outwards until a branch that yields a successful result is obtained. We then can destroy the branches that weren't successful and keep the one that succeeded. We could use the Predictive coding algorithm where Layer1 predicts Layer2 while the errors for Layer1 are…"
tags: ["r/OpenAI"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 142
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1x7eutp/is_growing_a_neural_network_like_a_tree_possible/"
score: null
comments: null
community: "r/OpenAI"
---

# Is growing a neural network like a tree possible?

Reddit · Sevdat · 2026-10-16

I got the idea from Tree graphs and Genetic Algorithms. Instead of training an AI, what if we just start from a node that branches outwards until a branch that yields a successful result is obtained. We then can destroy the branches that weren't successful and keep the one that succeeded. We could use the Predictive coding algorithm where Layer1 predicts Layer2 while the errors for Layer1 are stored at Layer2, but in this case it would be the nodes of the branches. Each node would need to contain 3 values. Value1 is for the input path, Value 2 is for output path and Value3 is for protecting the branch against destruction. The inputs are inserted from the root of the tree and sent back out after traversing each node of the tree. I think this could result in an evolving/learning AI.
