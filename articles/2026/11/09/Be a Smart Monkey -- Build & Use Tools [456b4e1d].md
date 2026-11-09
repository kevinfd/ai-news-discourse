---
id: "456b4e1d00a0b4e6"
title: "Be a Smart Monkey -- Build & Use Tools"
url: "https://reddit.com/r/ClaudeAI/comments/1xrmgl3/be_a_smart_monkey_build_use_tools"
link: "https://reddit.com/r/ClaudeAI/comments/1xrmgl3/be_a_smart_monkey_build_use_tools"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T08:33:17Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["PraxicalExperience"]
language: "en"
summary: "I'm a noob to using Claude (and using agentic AI in general,) but one tip I can give to other noobs is the above -- tell Claude to build tools that can be run locally when you're gathering and processing large batches of data, doing extensive simulation runs, or other stuff that doesn't require intelligence to guide it once the process starts. In my current project I was having claude ingest PDF…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 410
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrmgl3/be_a_smart_monkey_build_use_tools/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Be a Smart Monkey -- Build & Use Tools

Reddit · PraxicalExperience · 2026-11-09

I'm a noob to using Claude (and using agentic AI in general,) but one tip I can give to other noobs is the above -- tell Claude to build tools that can be run locally when you're gathering and processing large batches of data, doing extensive simulation runs, or other stuff that doesn't require intelligence to guide it once the process starts. In my current project I was having claude ingest PDF record sheets from a tabletop game. It took a relatively long time due to tool runs, and it was certainly not nothing when it came to token usage. I got about 600 sheets processed over a few days, and it did a pretty decent job, but there were still dozens of bits that it had queued up for me to check by eye. Then I realized that I was being stupid. I told claude to whip me up a script to do everything that could be done locally, show its progress, ensure it would resume if interrupted, and run any tests and cross-checks that it could do independently. I also told it to use local AI if that would help. After downloading Ollama and running a .bat as it told me to, about five minutes later I had a python script, twenty minutes after that Ollama finished downloading models, and then about an hour after that the script finished tearing through about 4200 record sheets. It'll still take probably another 10-11 agent runs to classify, check, and integrate everything, but that's far cheaper than how it was going before. Once I get everything incorporated and working in the game, I'm going to have it spin up a script to use the game to run a lot of simulations because I want to analyze in a rather detailed way how the existing units perform compared to their point-value in the game. It already has the simulation environment set up, I'll just need to to set up the battles, run an ass-ton of them, and record stuff for a good long while before handing the data off to claude to analyze. Similarly, while Claude will respect bots.txt on websites and not connect to them, it will gleefully (in my experience at least) write a python script that will crawl the site and scrape anything relevant. Or the whole damned thing, if necessary. And then it will just as gleefully go through that glob of files to find what you want.
