---
id: "7bff3ad3cf63bad1"
title: "Claude’s new rules against game cloning won’t stop the AI copying boom"
url: "https://arstechnica.com/ai/2026/11/claudes-new-rules-against-game-cloning-wont-stop-the-ai-copying-boom"
link: "https://arstechnica.com/ai/2026/11/claudes-new-rules-against-game-cloning-wont-stop-the-ai-copying-boom"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-02T18:05:31Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Kyle Orland"]
language: "en"
summary: "Last week, Anthropic introduced a new system prompt designed to stop its Claude models from re-creating specific, existing video games. While that move could help shield Anthropic from some liability, it's unlikely to slow much of the massive wave of AI-assisted game porting and copying that has emerged in recent months. \n A social media user and AI decompilation enthusiast going by the name…"
tags: ["AI", "Gaming", "Anthropic", "Claude", "clones", "copying", "decompilation", "prompts"]
orgs: ["Anthropic"]
topics: ["search & media"]
content_source: "fulltext"
word_count: 303
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/11/GettyImages-1180626096-1152x648.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Claude’s new rules against game cloning won’t stop the AI copying boom

Ars Technica · Kyle Orland · 2026-11-02

Last week, Anthropic introduced a new system prompt designed to stop its Claude models from re-creating specific, existing video games. While that move could help shield Anthropic from some liability, it’s unlikely to slow much of the massive wave of AI-assisted game porting and copying that has emerged in recent months.
A social media user and AI decompilation enthusiast going by the name “chasm” was among the first to note the prompt change late last week, saying a new rule seemed to be added to the Claude Code prompt on or around October 27. That rule—included in a json file under the name “tengu_heron_brook”—reads as follows:
Do build original games, games in a genre, and games from the user’s own designs and assets. Don’t build a recreation of a specific existing game, even if it is renamed or called original.
XDA later independently verified that the new rule appears in version 2.1.314 of the Claude Code binary, which was released on October 30. XDA also reported that the “tengu_heron_brook” rule had been used for other purposes in earlier versions and that the Claude Opus 5.5 model specifically seemed to have its own distinct and independent instructions restricting game recreations as part of its system prompt bundle.
Following chasm’s initial report, Anthropic software engineer Addy Osmani confirmed on social media that the company had “added two sentences to Claude Code’s prompt on Opus 5.5 to steer it away from recreating someone else’s specific game because using Claude to infringe IP is against our usage policy.”
He added that the new prompt was designed to still allow “original games, genre games, and games built from your own designs and assets,” even as a handful of issue reports on Anthropic’s GitHub suggest the new prompt is getting in the way of some game development use cases.
