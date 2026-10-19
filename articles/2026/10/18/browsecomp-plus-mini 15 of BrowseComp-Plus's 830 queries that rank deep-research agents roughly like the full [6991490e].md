---
id: "6991490e2cff1c06"
title: "browsecomp-plus-mini: 15 of BrowseComp-Plus's 830 queries that rank deep-research agents roughly like the full set, no LLM judge"
url: "https://reddit.com/r/LocalLLaMA/comments/1x94mu0/browsecompplusmini_15_of_browsecomppluss_830"
link: "https://reddit.com/r/LocalLLaMA/comments/1x94mu0/browsecompplusmini_15_of_browsecomppluss_830"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T14:30:57Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["asankhs"]
language: "en"
summary: "I needed a cheap way to compare search agents on BrowseComp-Plus without burning hours of agent time every run. So I built a 15-query subset of the full 830 that ranks systems roughly the way the full benchmark does. - weighted Spearman rank agreement 0.88 averaged over 30 splits, versus 0.75 for a random 15 - two runs more than 10 points apart on the full benchmark keep their order about 96% of…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "agents & coding", "search & media"]
content_source: "post"
word_count: 107
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x94mu0/browsecompplusmini_15_of_browsecomppluss_830/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# browsecomp-plus-mini: 15 of BrowseComp-Plus's 830 queries that rank deep-research agents roughly like the full set, no LLM judge

Reddit · asankhs · 2026-10-18

I needed a cheap way to compare search agents on BrowseComp-Plus without burning hours of agent time every run. So I built a 15-query subset of the full 830 that ranks systems roughly the way the full benchmark does. - weighted Spearman rank agreement 0.88 averaged over 30 splits, versus 0.75 for a random 15 - two runs more than 10 points apart on the full benchmark keep their order about 96% of the time; 5 to 10 points apart, about 75% - all answers are 1-4 words, so it grades by normalized exact match, no LLM judge - costs under 2% of a full run https://huggingface.co/datasets/LocalLLaMA/browsecomp-plus-mini
