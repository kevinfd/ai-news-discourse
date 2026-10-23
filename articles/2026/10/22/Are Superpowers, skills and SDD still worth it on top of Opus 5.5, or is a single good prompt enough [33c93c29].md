---
id: "33c93c292999d8c1"
title: "Are Superpowers, skills and SDD still worth it on top of Opus 5.5, or is a single good prompt enough?"
url: "https://reddit.com/r/ClaudeAI/comments/1xckkpr/are_superpowers_skills_and_sdd_still_worth_it_on"
link: "https://reddit.com/r/ClaudeAI/comments/1xckkpr/are_superpowers_skills_and_sdd_still_worth_it_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T14:46:20Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Mithrandir_Solo"]
language: "en"
summary: "⚠️ Disclaimer: please don't read this as \"a good prompt beats Superpowers, skills or SDD\". These are early results from one build per approach, on one task, with one operator . The ranking could change with more runs or a different kind of project / approach. I'm sharing it to discuss the method and to compare these results with what you've seen in your own projects, not to crown a winner. Why I…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "post"
word_count: 664
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xckkpr/are_superpowers_skills_and_sdd_still_worth_it_on/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Are Superpowers, skills and SDD still worth it on top of Opus 5.5, or is a single good prompt enough?

Reddit · Mithrandir_Solo · 2026-10-22

⚠️ Disclaimer: please don't read this as "a good prompt beats Superpowers, skills or SDD". These are early results from one build per approach, on one task, with one operator . The ranking could change with more runs or a different kind of project / approach. I'm sharing it to discuss the method and to compare these results with what you've seen in your own projects, not to crown a winner. Why I did this: I've been using the popular, highly starred Claude Code plugins and skill packs (Superpowers, Ponytail, Matt Pocock's skills and so on) and kept wondering whether they're really worth it with a model as strong as Opus 5.5. Almost everything I found was anecdotal, so I tried to measure it. Context that matters: I started with a full requirements document (SOW), an initial spec and the architecture already decided. The arms didn't have to work out what to build, only how to build it. I know many people use Superpowers mainly to brainstorm and shape a project from a vague idea, and this test didn't cover that at all. Still, the core promise of these tools is less human effort and better quality, whether or not the brainstorming has already been done, so I expected them to help here too. The four arms: D: the prompt only, no plugins. A: the prompt + a spec-driven development method. B: spec-driven development + Matt Pocock's skills + Ponytail. C: Superpowers. How the prompts differed: every arm got the same detailed prompt. The only change was a short section at the end that named the approach explicitly. For A, the prompt said to follow spec-driven development. For B, it named Matt Pocock's skills and Ponytail and said to use them in a set order. For C, it named the Superpowers skills to use. D got the prompt with nothing added. The task: a full-stack app (Python, React/TS, an LLM agent, Terraform, ...), run locally on cloud emulators. Each arm wrote its own tests. I graded them with a hidden test suite, a blind code review and hands-on tasks, and I measured human effort from the transcripts (this is an internal project, so I can't share the code, the spec or details about the product. Please take this as a first idea of what I've found so far, not as a finished study). What I measured , in four groups, each scored 0–100 relative to the best arm: Quality (40%): hidden test scenarios and rule-based checks, safety checks, hidden UI journeys, accessibility and Lighthouse, a fault-recovery test, a small load test, issues found during acceptance and defects that escaped it, a blind code review of the anonymised code, and hands-on tasks I did myself on each app. Human effort (25%): how many times I had to step in, how many questions the agent asked, rework rounds, and time spent waiting for me. Speed (20%): active minutes to the first "done" and total active hours. Cost (15%): Claude Code cost and the running cost of the app's own LLM. https://preview.redd.it/3gezh7ph61xh1.png?width=808&format=png&auto=webp&s=03d0373a804a0eaf90a752951cceab45aadaace3 My questions: With a spec in hand: when you already have the requirements, the spec and the architecture, are Superpowers, skills or SDD still worth it, or is a single detailed prompt enough? With only a vague idea: is it better to just write down what's in your head for plain Opus 5.5, saying what you expect, or to use Superpowers and let it ask you lots of questions first? Your experience: if you use these tools every day, where do they actually pay off for you, and did you get less human effort and better quality out of them? The method: how would you design this benchmark? Which metrics would you measure (and how would you weight them), how many runs per arm, what kinds of tasks, and how would you measure human effort fairly? The gap: why is there no benchmark like this yet? SWE-bench and similar test models, not ways of working.
