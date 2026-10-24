---
id: "e63b952430266c0f"
title: "Probability of backdoors in popular harnesses and LLM inference engines"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdeg0n/probability_of_backdoors_in_popular_harnesses_and"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdeg0n/probability_of_backdoors_in_popular_harnesses_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T13:44:17Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Ori_553"]
language: "en"
summary: "Let's put things into perspective: Remember, for example, the xz utils ssh backdoor in 2024? They almost managed to pull it off, and that was in the most observed codebase of the planet. It was caught almost by chance by someone working on something unrelated. Read about it if you don't realize how fragile the whole ecosystem is, open source or not. Now imagine what can happen, and possibly have…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 218
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdeg0n/probability_of_backdoors_in_popular_harnesses_and/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Probability of backdoors in popular harnesses and LLM inference engines

Reddit · Ori_553 · 2026-10-23

Let's put things into perspective: Remember, for example, the xz utils ssh backdoor in 2024? They almost managed to pull it off, and that was in the most observed codebase of the planet. It was caught almost by chance by someone working on something unrelated. Read about it if you don't realize how fragile the whole ecosystem is, open source or not. Now imagine what can happen, and possibly have already happened, to less observed repos like agent harnesses, LLM inference engines and LLM models themselves. There's a new one every week. And no, your Opus 5.5 subscription will not easily catch them. It's the wild west, you don't even need the llamacpp, strata or other new engine's repo maintainers to be malicious, you just need a perfectly legit-looking pull request (in any of the thousands packages/libraries these tools install) that is approved and sits there silently for months or years. The new rapidly changing LLM ecosystem is the perfect new fertile ground for this. I estimate the probability of at least one backdoor already sitting in popular harnesses and/or inference engines to be 100%. Insult me now, but deep down you know that chances are I'm right. . Thank you for reading, and please be anxious. (I typically write like this, this is not an LLM-generated post)
