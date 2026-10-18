---
id: "412c19a2ddb03229"
title: "Self-improve skill / LESSONS_LEARNED.md"
url: "https://reddit.com/r/ClaudeAI/comments/1x8a2m2/selfimprove_skill_lessons_learnedmd"
link: "https://reddit.com/r/ClaudeAI/comments/1x8a2m2/selfimprove_skill_lessons_learnedmd"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T13:19:13Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["AdNo4170"]
language: "en"
summary: "How we turned 225 \"lessons learned\" into real guardrails for our AI coding agents. How do you do it? Solo founder here, building a SaaS mostly with Claude Code: one hub session plans, sub-agents build in parallel, and a fresh skeptic agent reviews anything touching money, data or auth. Over a few months we built a lot of \"learn from mistakes\" process. Today I audited it and most of it wasn't…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "safety & ethics"]
content_source: "post"
word_count: 588
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8a2m2/selfimprove_skill_lessons_learnedmd/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Self-improve skill / LESSONS_LEARNED.md

Reddit · AdNo4170 · 2026-10-17

How we turned 225 "lessons learned" into real guardrails for our AI coding agents. How do you do it? Solo founder here, building a SaaS mostly with Claude Code: one hub session plans, sub-agents build in parallel, and a fresh skeptic agent reviews anything touching money, data or auth. Over a few months we built a lot of "learn from mistakes" process. Today I audited it and most of it wasn't doing what I thought. What we had: - LESSONS_LEARNED.md: every bug became a written lesson. 224 of them. - RETRO.md: a friction diary per session. - A /self-improve skill: every ~5 days it read logs and proposed rule/hook changes. What the audit found: - Nobody read the lessons at the moment it mattered. Not loaded at start, sub-agents never opened it. - A script said 139 lessons had no protection. Checking by hand against the code: only 26. The rest already had a test or rule that didn't cite the ID. - The retro was 92% duplicate (273 of 296 items already lived elsewhere). - Self-improve did work: 83% of proposals landed. But ~15 "landed and didn't stick" (the gate measured the wrong thing), and each run cost ~6 agents. Some of the bugs behind those lessons: - SQLAlchemy `FOR UPDATE` takes the lock but reads a stale object from the identity map. Needs `populate_existing`. - A TS fallback `?? "Free"` on a plan label told a paying customer they were on the free plan. - `umask 077` from one deploy step leaked into the next `git checkout`. - `psql -tA` without `-q` captures the command tag along with the value. - `gh api ... | length` without `--paginate` counted only page one. - First request to a "healthy" container returns 000, and our single-shot post-deploy check could roll back a good deploy. - `"123456".isupper()` is False in Python. - A gate's parser stopped at a blank line, checked 100 of 224 rows and reported green. What we changed: Each lesson has a state: OPEN, BARRED (a test/hook/lint rejects it), ABSORBED (short rule), ARCHIVED. A validator checks the barrier points to a function that exists; a comment doesn't count. Lessons arrive by file path. Before editing, the agent runs a script with the files it will touch and gets up to 3 lessons and 2 past bugs for those files. Found a problem? Fix it, add the guard and record the lesson as BARRED, all in the same change. No approval queue. We mutate the code on purpose to prove the test catches it. Self-improve runs on metrics at session close: a barred lesson that recurred (the guard doesn't work), an open lesson recurring, a gate failing repeatedly, the skeptic flagging the same pattern twice. First run flagged a "barred" lesson that came back twice. Demotion too: a lesson whose files nobody touched in 45 days and whose guard never fired becomes an archive candidate. Retro retired. Today: 123 barred, 98 absorbed, 2 open. Barring the open ones found and fixed 25 real violations. My takeaway: writing it down isn't learning. Agents reliably follow tests and hooks; written rules only help if they arrive at the moment of the edit. Questions: - How do your agents actually use past mistakes? CLAUDE.md , rules per path, RAG, hooks? - Has anyone measured whether a written rule reduces repeat bugs vs. a hard gate? - Do you ever delete rules? How do you keep the files from bloating? - In multi-agent setups, who is allowed to write the lessons?
