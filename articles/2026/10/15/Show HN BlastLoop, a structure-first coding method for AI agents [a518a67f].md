---
id: "a518a67fbae77614"
title: "Show HN: BlastLoop, a structure-first coding method for AI agents"
url: "https://github.com/rlshaw-ml/BlastLoop"
link: "https://github.com/rlshaw-ml/BlastLoop"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-15T16:26:39Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["rossleeshaw"]
language: "en"
summary: "BlastLoop is Ross Shaw's practical coding framework for AI agents: Blast, Mid, and Inner write code at different altitudes, then T1 structural, T2 bug/ops, and T3 adversarial test it in order.\nWhy it exists: AI coding agents make teams faster, but they also make failure faster. BlastLoop applies an operations mindset to agent work: each change has an owner at the right altitude, and every result…"
tags: []
orgs: []
topics: ["agents & coding", "jobs & society"]
content_source: "fulltext"
word_count: 782
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50106062"
score: 14
comments: 1
community: "Hacker News"
---

# Show HN: BlastLoop, a structure-first coding method for AI agents

GitHub · rossleeshaw · 2026-10-15

BlastLoop is Ross Shaw's practical coding framework for AI agents: Blast, Mid, and Inner write code at different altitudes, then T1 structural, T2 bug/ops, and T3 adversarial test it in order.
Why it exists: AI coding agents make teams faster, but they also make failure faster. BlastLoop applies an operations mindset to agent work: each change has an owner at the right altitude, and every result passes structural, operational and adversarial gates in a fixed order before it ships.
Open newsletter / public write-up is live. Fuller BlastLoop explanation: WORLDWRIGHT Issue 3, AI Did Not Remove Engineering Failure. It Made It Faster.
Version: 1.0.0 Tagline: structure first, function second, attack third.
- Clone this repo into the project where you want agent help.
- Point your agent at AGENTS.md.
- Load one build prompt based on the altitude of the work:
  - system or repo shape -> prompts/blast.md
  - subsystem or feature slice -> prompts/mid.md
  - local file or unit change -> prompts/inner.md
- Have the agent write code at that altitude. BlastLoop is not spec first, plan first, then one implementer. The build layer should produce code at its own scope.
- Run the test loop in order:
- If T3 finds a structural problem, restart through T1, route correction back to Blast, Mid, or Inner, then run T2 and T3 again.
That is the whole public cut: load the right prompt, write at the right altitude, then test in the right order.
See docs/HANDOFFS.md for the required handoff packet and routing rules. A stage may recommend a fix from its own vantage, but the owning altitude still decides and implements the change.
Blast writes system-level code and structure.
Use Blast when the job changes repo shape, service boundaries, top-level interfaces, shared contracts, deployment structure, or the skeleton of a new capability.
Mid writes subsystem code.
Use Mid when the job is bigger than a local patch but smaller than a system redesign: a feature slice, a service module, an integration surface, or a subsystem refactor.
Inner writes local unit code.
Use Inner when the job is contained to a few files, functions, tests, or adapters. Inner is the local-unit altitude in BlastLoop: focused scope, clear ownership, and direct completion of the change.
Run tests in this order.
T1 looks for structural issues: wrong boundaries, logic at the wrong altitude, leaky abstractions, broken file ownership, missing interfaces, or misplaced cross-cutting concerns.
T1 does not behave like a general bug fixer. Its job is to decide whether the code is shaped correctly and to route correction back to the right writer: Inner, Mid, or Blast.
T2 fixes bugs and operational issues directly when the structure is already sound.
If T2 discovers the issue is actually architectural, it escalates back to T1 instead of papering over the problem locally.
T3 attacks the result: edge cases, misuse, race conditions, weird inputs, brittle assumptions, security posture, rollback paths, and failure behavior.
If T3 finds a structural problem, the loop restarts like this:
T3 -> T1 -> B/M/I correction -> T2 -> T3
That restart rule matters. Structural breakage should be repaired structurally, not patched over as a local bug.
- Not a fact-checker. BlastLoop is a coding and testing framework, not a truth engine.
- Not GitHub Spec Kit. Spec Kit is spec -> plan -> tasks -> implement -> converge. BlastLoop is multiple coding altitudes plus a staged test loop.
- Not a competing "agent style." BlastLoop can work with Spec Kit, vibe coding, focused local implementation prompts, or red/blue testing. Those can sit inside an altitude or a test layer; BlastLoop is the structure-first loop that routes them.
- Not a multi-agent org chart. This public cut does not define management layers, bot hierarchies, or private automation.
- Not red/blue testing alone. Adversarial testing is T3 only, not the whole method.
BlastLoop does not require one coding style or one planning school.
- Spec Kit can shape planning before code is written.
- Vibe coding or other implementation styles can operate inside Blast, Mid, or Inner, depending on scope.
- Focused local implementation prompts can be used inside Inner when they fit the task.
- Red/blue testing fits naturally in T3 adversarial work.
BlastLoop's job is to route the work: choose the right altitude, then run T1 -> T2 -> T3 in order.
See docs/COMPARISON.md for a short side-by-side.
- AGENTS.md - routing card for which prompt to load
- prompts/ - loadable instructions for each build and test role
- docs/HANDOFFS.md - required handoff packet and ownership rules
- docs/COMPARISON.md - short comparison to adjacent public methods
- examples/session.md - fictional walkthrough of a small feature through the loop
MIT. See LICENSE.
