---
id: "560f41cdd142a45e"
title: "I asked claude code a simple question and it gave me very useful setup"
url: "https://reddit.com/r/ClaudeAI/comments/1xj9xik/i_asked_claude_code_a_simple_question_and_it_gave"
link: "https://reddit.com/r/ClaudeAI/comments/1xj9xik/i_asked_claude_code_a_simple_question_and_it_gave"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T08:38:05Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Weird_Inevitable_199"]
language: "en"
summary: "I was tired off claude code forgetting things between switching sessions, then I asked one question, why do you rediscover things after every session and waste time and tokens? Claude code literally said stop using `/clear`, it makes me rediscover again, and also claude code said done even use `/compact` either, it makes me forget small details as well. After a long discussion with claude code,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "jobs & society"]
content_source: "post"
word_count: 639
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj9xik/i_asked_claude_code_a_simple_question_and_it_gave/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I asked claude code a simple question and it gave me very useful setup

Reddit · Weird_Inevitable_199 · 2026-10-30

I was tired off claude code forgetting things between switching sessions, then I asked one question, why do you rediscover things after every session and waste time and tokens? Claude code literally said stop using `/clear`, it makes me rediscover again, and also claude code said done even use `/compact` either, it makes me forget small details as well. After a long discussion with claude code, we found one solution together. - Turn off claude code memory. - Turn off project memory the `.remember` folder. - Build global knowledge base (about my taste, how I want things, global rules, basically anything I want each project to inherit). - Build knowledge base for each local project. - keep track of session context. - turn off auto session compact. - write a detailed session handoff file and at 80% close current session and start a fresh one to continue working. Btw: under 80% I could run for hours, most my work are done by subagents. Each subagent has its own context. - a hook runs at the start of every session that reads the session handoff file, so claude never have to do rediscovery again and knows exactly what do for the new session. the knowledge base (local one for projects) has few things: This is whar my knowledge base looks like in summary. ``` core/ company.md // about the company. decisions.md // all decisions I make goes here. glossory.md // explains concepts and wordings. orchestration.md // explains who does what task. product-truth.md // product's current state. source-of-truth.md // two things disappear who wins? agents/ // specific knowledge for each agent. // files CHANGELOG.md // changes made to the knowledge. README.md // how the knowledge works and who own which part, how to consume it and so on... ``` I only use monorepos for my projects. Cuz lf that I have dedicated agents: - main agent: plans and works with me directly. - designer: after planning, main agents sents designer to Figma. - developer: works after desginer designs, and works on web apps and sites only. - mobile-developer: works only on expo+rn. - db-architect: preps anything related to db so no developers directly interacts with the DB. - advisor: takes a strong stand of their own opinion with facts packed. - analyst: runs every morning. Check all socials, analytics and brings numbers and stats. - researcher: deep dive researcher. - content-reviewer: a cold read. Before I has script-writer and blog writer agents, then claude code suggested that he does anything related to writing and so on, because it knows my taste, how I want things (which is also saved in the user level knowledge base where all projects share), when main agent writes it, it send to the content-reviewer that reads it from a stranger who discovered our content online. we reffer that as cold reads. - producer: the producer makes videos, carousels and so on, it uses approved scripts. Plan: this is a backbone as well and helps me achieve so many things. - plans: main folder. - plan.md: has the whole plan of the project broken down into phases. - plan-phase-[n].md: a step by step detailed plan for each phase, where N is the phase number. - a detailed plan for a phase is written when working on that phase only, each phase or a step has a status of pending, inprogress or completed. There are so many things about my setup, all too me a while to build them, this is not something I built overnight, rather months. I canr cover all of it: there's a meetings folder, the docs folder and so on... At this point, I can say Im happy with my workflow, while im still hungry for improvements. What do you do differently? If you any suggestions, tips or anything lmk, I'm willing to improve.
