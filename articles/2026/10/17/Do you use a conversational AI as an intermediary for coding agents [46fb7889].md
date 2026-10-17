---
id: "46fb7889cf25d4e9"
title: "Do you use a conversational AI as an intermediary for coding agents?"
url: "https://reddit.com/r/ChatGPT/comments/1x80bnd/do_you_use_a_conversational_ai_as_an_intermediary"
link: "https://reddit.com/r/ChatGPT/comments/1x80bnd/do_you_use_a_conversational_ai_as_an_intermediary"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T03:49:56Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["noborutkhs"]
language: "en"
summary: "I've been using coding agents in two different ways, and I'm curious how common my current workflow is. At work, I originally used Amazon Q Developer directly, giving it instructions myself. Later, for a personal project, I asked ChatGPT how I should work with Codex. ChatGPT suggested a workflow where I discuss tasks with it first, have it prepare detailed instructions for Codex, and then bring…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI", "Amazon", "Microsoft"]
topics: ["agents & coding"]
content_source: "post"
word_count: 316
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x80bnd/do_you_use_a_conversational_ai_as_an_intermediary/"
score: null
comments: null
community: "r/ChatGPT"
---

# Do you use a conversational AI as an intermediary for coding agents?

Reddit · noborutkhs · 2026-10-17

I've been using coding agents in two different ways, and I'm curious how common my current workflow is. At work, I originally used Amazon Q Developer directly, giving it instructions myself. Later, for a personal project, I asked ChatGPT how I should work with Codex. ChatGPT suggested a workflow where I discuss tasks with it first, have it prepare detailed instructions for Codex, and then bring the results back to ChatGPT for review and further discussion. I started using this ChatGPT → Codex → ChatGPT loop, and it seemed to work well. So I tried applying the same approach at work, using Copilot as the conversational layer and Amazon Q Developer as the coding agent. I felt similar benefits there too. One advantage is that the conversational AI turns my rough intentions into more specific instructions. This seems to reduce the chances of the coding agent heading in an unintended direction. It also helps prepare more detailed verification steps after implementation. But I've found this approach particularly useful for investigating bugs , rather than just writing code. The clues needed to solve a problem aren't always in the source code that the coding agent can access. They might be in external logs, my own notes, or information I've gathered from elsewhere. In those cases, discussing the broader problem with a conversational AI, then asking it to direct the coding agent to investigate specific parts of the code, seems to make it easier to reach an answer. I didn't invent this workflow. ChatGPT suggested it when I asked how to use coding agents, and I've simply continued using it because it seems effective. Is this a common way of working? What advantages or disadvantages have you experienced compared with interacting directly with a coding agent? I'm particularly interested in whether others find it useful for debugging and investigation, where the relevant information is spread across multiple sources.
