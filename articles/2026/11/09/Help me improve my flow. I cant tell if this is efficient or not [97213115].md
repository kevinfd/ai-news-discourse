---
id: "97213115887caf25"
title: "Help me improve my flow. I cant tell if this is efficient or not"
url: "https://reddit.com/r/ClaudeAI/comments/1xroaqh/help_me_improve_my_flow_i_cant_tell_if_this_is"
link: "https://reddit.com/r/ClaudeAI/comments/1xroaqh/help_me_improve_my_flow_i_cant_tell_if_this_is"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T10:29:53Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Individual_Age_3889"]
language: "en"
summary: "I am trying to determine if this is a good way to structure Claude and improve efficiencies and token usage. It is kinder working *Most of the time* the issue is when handovers take place sometimes the Orch goes off the rails and ignore owner rules. It just tends to do its own thing. I have limited the Orch levels to a maximum of 8, thereafter I start the Orch again manually. Context handover:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 610
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xroaqh/help_me_improve_my_flow_i_cant_tell_if_this_is/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Help me improve my flow. I cant tell if this is efficient or not

Reddit · Individual_Age_3889 · 2026-11-09

I am trying to determine if this is a good way to structure Claude and improve efficiencies and token usage. It is kinder working *Most of the time* the issue is when handovers take place sometimes the Orch goes off the rails and ignore owner rules. It just tends to do its own thing. I have limited the Orch levels to a maximum of 8, thereafter I start the Orch again manually. Context handover: Windows are 250k = Wind down = 280k start preparing for handover. Failure Guard: Sonnet First on Low/Med and tasks - First fail move to Opus - Second fail dead stop. Opus on High/Schema and tasks - First fail move to Fable Review/Audit - Second test Opus with fable guideline - Third fail dead stop - log for redesign. Here is an overview of the setup at the moment, Orchestrators control a project and managers each task per agent. Route: Owner -> Orch -> Builder -> Reviewer -> Orch merger -> Gate -> dev + Owner 1. Orch: Task logged. It gets a row on the task list and the task board, usually from the owner's testing notes or a review finding. Only the owner sets the order. 2. Owner Go: Nothing starts without the owner's yes for that task. 3. Orch / Builder: Live check first. The screen is opened as it is today on dev (by the Orch, or from the builder's first screenshot) and its current state is written into the task's gap table and the live-state notes. If it already meets the target, the task is closed, not built. 4. Builder: Spec. Acceptance criteria are written before any build. For screens, the target is the concept image (or a drawing in the clickable prototype) with a target-vs-live gap table. 5. Builder: Build. One fresh worker (usually Sonnet) builds one task on its own branch off dev. It runs the type checks, the tests for what it touched (in its own test database, never live data) and takes screenshots of changed screens, then pushes the branch. 6. Reviewer: Review. A separate reviewer reads the actual diff and re-runs the checks. Opus reviews security, permissions, children's data and database changes; Sonnet reviews everything else. A FAIL sends it to a fresh fix worker, and the next review is Opus; two FAILs pause the task until the owner decides. 7. Orch: Verify, don't trust. Reads the real commit, the test numbers and the screenshots before believing a "done" report. 8. Orch (merger): Merge-result check. Merges the passed branches together and re-runs type checks, the full app tests and lint on the combined result. A branch that breaks the combination gets its own fix; the rest carry on. 9. Owner: Yes, where it matters. Database changes, anything touching live data, and the production branch each need the owner's yes, one action at a time. 10. Gate: Full suite. After up to four merges, and always before the owner tests, one gate runs everything on dev: all API tests, app tests, database migrations from scratch and lint. Red means the culprit is fixed first and nothing else merges. 11. Orch (merger): Merge to dev and update the docs. In the same step the task list, board, live-state notes and owner test page move the task from "Built, not merged yet" to Done / Ready. 12. Owner: Device check. The owner tests on a phone. Anything found becomes a new logged task, and the cycle starts again. Can I improve this further or is this over complicating the application design process? We close to production / Launch so that's the reason for reviewers and gates full suite tests.
