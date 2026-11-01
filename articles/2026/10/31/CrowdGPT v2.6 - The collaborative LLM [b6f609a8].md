---
id: "b6f609a8b6f77ab1"
title: "CrowdGPT v2.6 - The collaborative LLM"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkibxw/crowdgpt_v26_the_collaborative_llm"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkibxw/crowdgpt_v26_the_collaborative_llm"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T18:57:36Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Vxtzq1"]
language: "en"
summary: "For those who saw the original post , a week ago, I'm glad to announce CrowdGPT v2 (more precisely v2.6), a massive update to the original CrowdGPT project :D (scroll down to see what's new) For the newcomers: CrowdGPT is a project aiming to create a LLM without datacenters and without the usual millions of dollars spent by AI companies. The project aims to train a 1 billion parameter model…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "products & launches", "chips & infrastructure", "business & funding"]
content_source: "post"
word_count: 663
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkibxw/crowdgpt_v26_the_collaborative_llm/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# CrowdGPT v2.6 - The collaborative LLM

Reddit · Vxtzq1 · 2026-10-31

For those who saw the original post , a week ago, I'm glad to announce CrowdGPT v2 (more precisely v2.6), a massive update to the original CrowdGPT project :D (scroll down to see what's new) For the newcomers: CrowdGPT is a project aiming to create a LLM without datacenters and without the usual millions of dollars spent by AI companies. The project aims to train a 1 billion parameter model collaboratively and openly, as a proof of concept (it is possible to scale to bigger dense models or even MoE architectures with this project) This project implements a protocol where everyone gets a say in the direction the project takes. Anyone can use their PC to train the AI independently, then add their contributions to the global model. There's other things that makes this project appealing for the open-source community, but i won't state these again as you will be able to check that out on the GitHub or on the original post. Of course, any advice / feedback on the project is still welcome (please stay polite and roast me with strong evidence only 👍), feel free to run experiments of data poisoning to point at the limits of our approach :) Here's the project website: https://www.crowdgpt.net/ Or the GitHub if anyone wants to check out the code https://github.com/Vxtzq/CrowdGPT As for the v2.6 changelog: We tried to implement mostly of the feedback you guys gave (mostly on security related points). Even though implementing this was hard and caused many breaking changes (which made some training contributions stale), we still achieved to train the model on 4.5B new tokens in 6 days!! Which is roughly what i achieved to train in two months for the project on my personal GPU 🤯 Here's a quick summary of what we implemented: - Robust server-side checking logic (see more at the end of the post). - Way better client mechanics (better ergonomy, more robust installation, GPU selection, no more crashes) - Many bugfixes (on server and client code, as the various issues/pull requests on GitHub suggest) - Activated Engrams on the Crowd-v1 model , which will make the model better at fact-recalling - Implemented a data submission pipeline in order to create a collaborative dataset for CrowdGPT : https://www.crowdgpt.net/#submit All the data will be verified / curated before training. Already 400kb of data was submitted. - Client releases cryptographic signing : some users reported that the auto-update mechanism in the client code allowed arbitrary code execution, and that would have allowed people stealing my GitHub credentials to execute malicious code on your device. Well not anymore, since the client code is now signed with a key that is only present on my device 😄 Like some comments on the original post pointed out, the architecture of the project at the time of my first post here was nowhere near good: clients could fake their contributions , could submit poison to the model, could crash the server by sending fake contributions every millisecond without any checks; and finally clients could very easily train the model to contain malicious backdoors . We therefore implemented byzantine cross-checks between clients training the model, at the cost of redundancy (3 clients training on exactly the same data). I am not claiming that this creates a 100% perfect Federated learning framework, but that makes malicious contributions way harder . For example, even a malicious client could only train on 2-3% malicious data per round without getting banned, against 100% before. For people that dared to read until the end, i'm also releasing CrowdBench, the open-source collaborative benchmark, where everyone can add general intelligence questions with deterministic answers to test LLMs :D Even though the codebase is currently early-stage and work-in-progress, it's already something working, and i coded it without using any AI (for those in the original post who wanted me to turn towards less ambitious projects😂) tell me what you think about CrowdGPT and CrowdBench in the comments. Thanks in advance.
