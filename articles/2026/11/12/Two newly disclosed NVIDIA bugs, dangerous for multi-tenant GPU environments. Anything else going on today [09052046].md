---
id: "0905204650eb7a44"
title: "Two newly disclosed NVIDIA bugs, dangerous for multi-tenant GPU environments. Anything else going on today?..."
url: "https://reddit.com/r/ArtificialInteligence/comments/1xulyk6/two_newly_disclosed_nvidia_bugs_dangerous_for"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xulyk6/two_newly_disclosed_nvidia_bugs_dangerous_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T19:20:21Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["SirJerryLion"]
language: "en"
summary: "Yh yh, not the typical NVIDIA news or meme, but, super interesting research. Neoclouds sell GPU slices on the promise that every tenant is isolated. These two vulns reveal that promise is broken. Both of these go from unprivileged to root. ForgePtr (CVE-2026-47501) takes an unprivileged process in a GPU container to root on the host, then switches off kernel lockdown and module signing on a…"
tags: ["r/ArtificialInteligence"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research", "search & media"]
content_source: "post"
word_count: 136
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xulyk6/two_newly_disclosed_nvidia_bugs_dangerous_for/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Two newly disclosed NVIDIA bugs, dangerous for multi-tenant GPU environments. Anything else going on today?...

Reddit · SirJerryLion · 2026-11-12

Yh yh, not the typical NVIDIA news or meme, but, super interesting research. Neoclouds sell GPU slices on the promise that every tenant is isolated. These two vulns reveal that promise is broken. Both of these go from unprivileged to root. ForgePtr (CVE-2026-47501) takes an unprivileged process in a GPU container to root on the host, then switches off kernel lockdown and module signing on a Secure Boot machine. NvRoot (CVE-2026-47591) lets the GPU rewrite files the OS has marked read-only, from any tenant on the node. Essentially this means attackers are able to rent their way to accessing someone else’s production AI. They both sat in NVIDIA’s open-source driver for 4+ years, and are now patched. NVIDIA scores them 7.8 as “local” bugs, though, on neocloud rented GPU nodes, local means everyone. nvroot Forgeptr YItMatters
