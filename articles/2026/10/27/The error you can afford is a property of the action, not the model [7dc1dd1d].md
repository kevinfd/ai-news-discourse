---
id: "7dc1dd1d13b6b16d"
title: "The error you can afford is a property of the action, not the model"
url: "https://reddit.com/r/artificial/comments/1xh5c4m/the_error_you_can_afford_is_a_property_of_the"
link: "https://reddit.com/r/artificial/comments/1xh5c4m/the_error_you_can_afford_is_a_property_of_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T21:26:41Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["AIGODSEND"]
language: "en"
summary: "a clinical AI researcher asked me a better question than most agent-verification threads: how do you decide which error you can afford, false accepts or false rejects? my answer: the action sets the loss function. start with two questions. can the effect be undone, and how far does it travel before someone notices? for irreversible or externally visible commits (delete, pay, publish, deploy,…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 247
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xh5c4m/the_error_you_can_afford_is_a_property_of_the/"
score: null
comments: null
community: "r/artificial"
---

# The error you can afford is a property of the action, not the model

Reddit · AIGODSEND · 2026-10-27

a clinical AI researcher asked me a better question than most agent-verification threads: how do you decide which error you can afford, false accepts or false rejects? my answer: the action sets the loss function. start with two questions. can the effect be undone, and how far does it travel before someone notices? for irreversible or externally visible commits (delete, pay, publish, deploy, send), false accepts are the expensive error. the gate needs positive evidence and a quarantine default. for reversible or read-only actions (draft, query, staging), false rejects are the expensive error because they burn reviewer attention and teach people to bypass the gate. put a number on it. for an action class, estimate p(bad), C_fa and C_fr. accept only when p(bad) * C_fa < (1 - p(bad)) * C_fr. the base rate matters more than model confidence. a 94% specificity / 69% sensitivity model is a triage tool, not a gate: it misses about three in ten positives. the part most verification posts skip is that a false reject is not free. if the reviewer never pays for a wrong no, they will say no to everything and the gate becomes the bottleneck. log both directions: escaped false accepts found later, and false rejects that turned out to be good. split propose from commit so the expensive gate only runs on the commit path. if there is no restoration path, treat the action as irreversible. what operating point do you use for irreversible agent actions?
