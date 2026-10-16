---
id: "71a62e6cb461aeb8"
title: "ROCprofGUI"
url: "https://reddit.com/r/LocalLLaMA/comments/1x61mja/rocprofgui"
link: "https://reddit.com/r/LocalLLaMA/comments/1x61mja/rocprofgui"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T20:06:45Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["ilintar"]
language: "en"
summary: "I've been tinkering / vibing myself an app that I think might be useful - since I've now used it on my own cases for some time and fixed most of the bugs I noticed, I'm risking a public announcement :) https://pwilkin.github.io/ROCprofGUI / https://github.com/pwilkin/ROCprofGUI ROCprofGUI The ROCprofGUI (aka rocprof studio) is a tool I made to be an alternative to ROCprof Compute Viewer and…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: ["agents & coding", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 221
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x61mja/rocprofgui/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# ROCprofGUI

Reddit · ilintar · 2026-10-14

I've been tinkering / vibing myself an app that I think might be useful - since I've now used it on my own cases for some time and fixed most of the bugs I noticed, I'm risking a public announcement :) https://pwilkin.github.io/ROCprofGUI / https://github.com/pwilkin/ROCprofGUI ROCprofGUI The ROCprofGUI (aka rocprof studio) is a tool I made to be an alternative to ROCprof Compute Viewer and other tools in the ROCm ecosystem - one that is user-friendly, has a modern UI and can be used with agentic help. Despite its name, the studio can analyze traces from all of the engines that AMD hardware supports: ROCm traces from rocprofv3, Vulkan traces from RADV (needs a patch to the driver currently) and HRX traces for Loom kernels. Coupled with the studio is an MCP server that allows tracing from your favorite LLM agent. The studio works in two modes - as a GUI (then, if you use the MCP, a popup appears telling you that the MCP server is currently driving operation) or fully headless - in which case there's no UI and just the service running the MCP server. I've been running it for over a week now while doing my optimization work on llama.cpp, so hopefully the most annoying bugs have been ironed out. I hope it's of use to someone :)
