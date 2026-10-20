---
id: "bf50eaf098d16dee"
title: "A local 27B model reads my lease and finds a leak in my bills | Row-Bot + qwen3.8 on Ollama"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xaokp3/a_local_27b_model_reads_my_lease_and_finds_a_leak"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xaokp3/a_local_27b_model_reads_my_lease_and_finds_a_leak"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T10:31:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Acceptable-Object390"]
language: "en"
summary: "Row-Bot 5.0 with qwen3.8:27b in Ollama, on my own GPU. No API keys, no cloud. Gave it a year of bills, a tenancy agreement, an insurance policy and a rent increase letter (all made up). It spotted a likely leak in the water bills and showed the rent rise breaks the lease. What it actually did: - charted the CSV inline (Plotly) - read the PDFs and quoted clauses 4.1 to 4.3: a 10% rise against a…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["chips & infrastructure", "policy & regulation", "agents & coding"]
content_source: "post"
word_count: 144
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xaokp3/a_local_27b_model_reads_my_lease_and_finds_a_leak/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# A local 27B model reads my lease and finds a leak in my bills | Row-Bot + qwen3.8 on Ollama

Reddit · Acceptable-Object390 · 2026-10-20

Row-Bot 5.0 with qwen3.8:27b in Ollama, on my own GPU. No API keys, no cloud. Gave it a year of bills, a tenancy agreement, an insurance policy and a rent increase letter (all made up). It spotted a likely leak in the water bills and showed the rent rise breaks the lease. What it actually did: - charted the CSV inline (Plotly) - read the PDFs and quoted clauses 4.1 to 4.3: a 10% rise against a 5% cap, with 5 weeks' notice instead of 2 months - saved 8 linked memories to a local knowledge graph drafted the email to the agent and set a reminder The honest numbers: a dense 27B does about 15 tok/s on my 5090, so some turns took 2+ minutes. The amber badges in the video show where I sped it up. Runs on Windows, macOS and Linux.
