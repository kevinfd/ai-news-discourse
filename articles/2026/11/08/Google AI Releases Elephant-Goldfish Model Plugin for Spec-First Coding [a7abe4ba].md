---
id: "a7abe4ba5513fdeb"
title: "Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding"
url: "https://marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents"
link: "https://marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-08T10:46:18Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google has open-sourced the Elephant-Goldfish Model (EGM) plugin , a design-and-review layer for AI coding agents. The Elephant-Goldfish Model plugin makes an agent write a specification before it writes code. Fresh subagents with no conversation history then attack that spec. Google says thousands of its engineers use it . It is quite simple: catch wrong assumptions in a Markdown file, not in a…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Machine Learning", "New Releases", "Open Source"]
orgs: ["Google", "Anthropic", "OpenAI", "Microsoft", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 863
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding

MarkTechPost · Asif Razzaq · 2026-11-08

Google has open-sourced the Elephant-Goldfish Model (EGM) plugin , a design-and-review layer for AI coding agents. The Elephant-Goldfish Model plugin makes an agent write a specification before it writes code. Fresh subagents with no conversation history then attack that spec. Google says thousands of its engineers use it . It is quite simple: catch wrong assumptions in a Markdown file, not in a pull request. 

 TL;DR 

 Size: 7 skills, 9 reviewer personas, 6 brainstorm lenses, 5 review stages. No model weights; your agent supplies the LLM. 

 Runs on: any harness that can spawn fresh subagents: Antigravity, Claude Code 2.1.271+, Claude Cowork, Codex, ChatGPT. Uses your existing model quota. 

 Performance: no accuracy benchmark published. Evidence is adoption and end-to-end harness test runs. 

 Best: Codex 0.163.0 completed 15 native fresh-context reviewers in order. 2 live tests passed in 573.13s. 

 Worst: the Claude Cowork run stopped after stages 5 to 7 on a usage limit. Issue #237 reports AGENTS.md leaking into Codex reviewers. 

 Bottom line: best thing, forced independent review before code. Worst thing, heavy token use and unverified isolation on some hosts. 

 What is Google’s Elephant-Goldfish Model plugin? 

 EGM is an Apache 2.0 plugin of skills, reviewer personas and document standards. It is not a new language model. The method comes from Dave Rensin’s essay on elephants and goldfish. The Google Open Source blog frames it as a fix for AI “slop” and session context collapse. The README states it is not an officially supported Google product . 

 How does the Elephant-Goldfish workflow work? 

 The Elephant is a long session holding project context and earlier decisions. It drafts the spec and writes no code. Each Goldfish is a stateless subagent. It reads only the draft and the files it references. You resolve trade-offs and approve the design. 

 The core loop has 3 commands: 

 /egm-brainstorm clarifies the idea, then runs a 6-lens Goldfish swarm. Lenses cover YAGNI, token cost, UX, migration, observability and tech debt. Output: concepts_brief.md . 

 /egm-draft turns the brief into a design doc under docs/designs/ , section by section. 

 /egm-review runs the Goldfish review. 

 /egm-drift-report later compares code with the spec. The docs recommend running it weekly. 

 What happens in the 5-stage Goldfish review? 

 The review skill runs 5 sequential stages: 

 Initial Zoom Out: checks the whole document at a high level. 

 Comprehension Test: a Goldfish paraphrases the design. A wrong paraphrase means the doc is ambiguous. 

 Critic Review: design, structural and style reviewers hunt gaps and edge cases. 

 Intermediate Zoom Out: rechecks architecture after fixes. 

 Implementation Readiness: checks file paths, data structures and signatures. 

 Each stage allows at most 1 re-audit. Findings are ranked Blocker, Major or Nit. If a host has no subagent tool, EGM stops. A same-context review is not a Goldfish review. 

&&

 Which coding agents does EGM support? 

 Launch coverage described Antigravity-only support , with more coming. The current harness guide covers Antigravity CLI and App, Claude Code, Claude Cowork, Codex, ChatGPT, omp and Muse. Antigravity CLI, Claude Code and Codex pass automated end-to-end fixtures. 

 Claude Code needs version 2.1.271 or later . Reviewers there get only Read, Grep and Glob tools. CLAUDE.md files are excluded from their context. 

 The test record gives concrete run data: 

 Antigravity CLI 1.4.5: 16 native reviewers ran, stages in order. 

 Codex 0.163.0: 15 native reviewers, 2 live tests in 573.13s. 

 Codex CLI with the v0.1.0 ZIP: full suite passed in 482.30s. 

 How does EGM compare with Spec Kit, Kiro and Superpowers? 

 Feature Google EGM GitHub Spec Kit Kiro Specs Superpowers Type Plugin (skills + personas) Toolkit + Specify CLI Feature of an agentic IDE/CLI/web Skills plugin License Apache 2.0 MIT Commercial ( pricing ) MIT Workflow Brainstorm, draft, review, drift report Constitution, specify, plan, tasks, implement, converge Requirements, design, tasks Brainstorm, plan, subagent build, TDD, review Spec reviewed by fresh-context subagents Yes, 5 stages before code Not disclosed Not disclosed (Analyze Requirements pass) No; fresh subagents review code per task Harness Antigravity, Claude Code, Codex, ChatGPT, more Copilot and other agents Kiro only 16 harnesses listed Setup Plugin install Python 3.11+, uv Kiro account Plugin install Cost Free plugin; host model usage Free toolkit; host model usage Subscription Free plugin; host model usage 

 EGM’s distinct move is reviewing the spec with zero-context agents. Spec Kit and Kiro center on human review between phases. Superpowers isolates subagents mainly at implementation time. 

 Key Takeaways 

 EGM is a plugin, not a model: Elephant drafts, Goldfish reviews. 

 Specs get 5 zero-context review stages before any code. 

 Works across Antigravity, Claude Code, Codex and ChatGPT. 

 Codex test runs completed 15 fresh-context reviewers end to end. 

 Reviewer isolation still leaks host instruction files on some CLIs. 

 Check out the GitHub repo , the project site and the Google Open Source blog post . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding appeared first on MarkTechPost .
