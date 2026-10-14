---
id: "05be2cee25de4f1a"
title: "Deft: an open-source, self-hosted workspace for chat, tasks and knowledge + MCPs and experimental sideloadable apps"
url: "https://reddit.com/r/ClaudeAI/comments/1x5mxe7/deft_an_opensource_selfhosted_workspace_for_chat"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T09:41:04Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["maneek21"]
language: "en"
summary: "GitHub: https://github.com/Maneek21/Deft Walkthrough: https://youtu.be/7z9EH4c9k2o Deft brings chat , tasks and knowledge into one self-hosted workspace. The bit I care most about is keeping the discussion behind the work connected to what happens next. The screenshots show: A full feature company chat. (There we can see the user invoking an agent in chat to create a task and its approval card.)…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "post"
word_count: 314
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5mxe7/deft_an_opensource_selfhosted_workspace_for_chat/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Deft: an open-source, self-hosted workspace for chat, tasks and knowledge + MCPs and experimental sideloadable apps

Reddit · maneek21 · 2026-10-14

GitHub: https://github.com/Maneek21/Deft Walkthrough: https://youtu.be/7z9EH4c9k2o Deft brings chat , tasks and knowledge into one self-hosted workspace. The bit I care most about is keeping the discussion behind the work connected to what happens next. The screenshots show: A full feature company chat. (There we can see the user invoking an agent in chat to create a task and its approval card.) A full feature task management app (with the task that agent created from screenshot 1) The interconnected web of knowledge that's auto created based on chat, tasks, CRM, connected apps that all agents, ai assistants, and humans can use as context. A claude MCP connector proof. Platform Architecture Diagram. You can connect Claude and ChatGPT through MCP. The core workspace works without an AI provider. I'm working on an experimental App Kit for building and sideloading apps into Deft, so custom tools can live alongside the work they're meant to support. CRM is the first example of the sideloadable app architechure, and it works smoothly enough. But a CRM in essence is just a fancy CSV, so i am making an Email client next, because if a sideloaded email client works, I feel any app would work. It's still alpha but you can run for free it with Docker Compose on a VPS to create a workspace for your team to replace slack, linear, notion and more. + the code is AGPL-3.0. If you try running it, I'd love to hear any feedback you may have, where setup gets annoying or the workflow stops making sense. How i used claude to build it: I started building Deft with Claude Code, then moved to mixed model approach. (Right now its Opus+Astra+Sol 6.1) Main planning and coding work has been Opus. P.S. The walkthrough has an AI voiceover: I have a stutter and spent a week trying to record it myself, but couldn't get through it.
