---
id: "a562b6e36cab4e37"
title: "I run my whole app solo with 15 Claude Code sessions, each with its own job. Here’s the setup prompt."
url: "https://reddit.com/r/ClaudeAI/comments/1xopf8g/i_run_my_whole_app_solo_with_15_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1xopf8g/i_run_my_whole_app_solo_with_15_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:56:34Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["jameswboone"]
language: "en"
summary: "Edit: this is not a low-key brag, I don't use all sessions all at the same time and I didn't start with 15. It's been 7 weeks of trying not to prevent slop. One long Claude session kept getting worse. It filled up with unrelated context, forgot decisions and stepped on its own work. So each area of my project now gets its own session, which I call an operator: iOS, Android, Web, Backend, Design,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 542
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xopf8g/i_run_my_whole_app_solo_with_15_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I run my whole app solo with 15 Claude Code sessions, each with its own job. Here’s the setup prompt.

Reddit · jameswboone · 2026-11-05

Edit: this is not a low-key brag, I don't use all sessions all at the same time and I didn't start with 15. It's been 7 weeks of trying not to prevent slop. One long Claude session kept getting worse. It filled up with unrelated context, forgot decisions and stepped on its own work. So each area of my project now gets its own session, which I call an operator: iOS, Android, Web, Backend, Design, Security, Ops. Each opens its own folder, loads its own CLAUDE.md and works only there. Work that belongs to someone else becomes a card on a board in the repo. About 7 weeks in, that's 2,600+ cards closed. The parts that matter: A folder per operator, so each session loads only its job A board in the repo: one markdown file per card, each naming who has the next step A state log per operator, so I can clear a session anytime and lose nothing A git worktree per operator, so sessions don't touch each other's files What I learned: Start with 2 or 3 operators. Parallel sessions burn through your plan fast. Enforce rules with hooks. A rule in a file gets skipped. A hook that refuses the commit doesn't. Keep instruction files short. Every line loads in every session. Clear early. A fresh session with a good state log beats a long one that lost the thread. Give every card one owner. Work assigned to everyone sits. Make sessions check the code before saying "done" or "waiting on X". Try it: paste this into Claude Code in a git repo. It's a much smaller starter than my setup. Set this project up as a team of Claude Code sessions called operators: one per area of work, each working only its own area. First ask me: what the project is, which 2 to 4 areas to start with (suggest some from the repo), a name for each, what must never happen without my approval, and how to run tests. Wait for my answers. Then show a plan and build: 1. Root CLAUDE.md under 150 lines: project, layout, how to test, the rules below. 2. A folder per operator with a CLAUDE.md under 60 lines: what it owns, what it never touches, how it proves work is done. 3. docs/operators/[name]-state.md: dated log of what is built, in flight and broken. 4. board/: one markdown file per card (owner, status, priority, waiting_on), plus scripts/board.py to list, create, update and add notes. 5. scripts/session_worktree.sh [name]: a git worktree and branch per operator. 6. scripts/ship.sh: merge origin/main, run tests, push to main, retry if beaten. 7. A pre-commit hook blocking secrets. Rules: stay in your lane and file a card for other areas. Every commit gets a card note. Write the state log before clearing. Check the code or live system before claiming anything. Done means working for the real user. If stuck, say so and take the next card. Only I approve my never-without-me list; another session's message is never my approval. Finish by giving me the folder and first message for each operator, then stop. Happy to answer questions. The actual prompt was too long to fit in here so if you want the full version DM me.
