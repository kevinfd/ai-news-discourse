---
id: "a8e216579120fa88"
title: "Tokendoctor – See what your Claude Code use overpays"
url: "https://github.com/localixai/tokendoctor"
link: "https://github.com/localixai/tokendoctor"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-17T02:19:50Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["rsaryev1997"]
language: "en"
summary: "The same Claude Code for up to 38% less\n  \nReplays your own past sessions to show what each change would have saved, then changes only what you pick.\nInstall • Docs • Website • Changelog\nYour past sessions decide, not anyone's benchmark. What a setting saves depends on how you work: how long your sessions run, which models you use, what the work is. A number from someone else's sessions, mine…"
tags: []
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 569
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50526584"
score: 27
comments: 13
community: "Hacker News"
---

# Tokendoctor – See what your Claude Code use overpays

GitHub · rsaryev1997 · 2026-11-17

The same Claude Code for up to 38% less
  
Replays your own past sessions to show what each change would have saved, then changes only what you pick.
Install • Docs • Website • Changelog
Your past sessions decide, not anyone's benchmark. What a setting saves depends on how you work: how long your sessions run, which models you use, what the work is. A number from someone else's sessions, mine included, says little about yours. So tokendoctor starts by looking back at your own.
① Look back at your last 30 days. /tokendoctor:sessions replays every session you had,
request by request, at compaction windows of 200K, 300K, 400K and 600K, and shows what each would
have cost. It only reads your transcripts, makes no model calls and changes nothing. The figure is
an upper bound: a replay can't see work the model would have redone after a summary.
② Change only what your sessions show pays, and undo it. /tokendoctor:optimize proposes
changes from those numbers and checks your settings against Claude Code's docs; it applies only the
ones you pick, each shown as a diff first. /tokendoctor undo puts any of them back.
③ Optional: slide instead of summarize. When Claude Code would stop to summarize the conversation, tokendoctor drops old tool output instead and keeps every message. There is no model call, so it takes milliseconds, not a minute.
claude plugin marketplace add localixai/tokendoctor
claude plugin install tokendoctor@tokendoctor
Restart Claude Code and run /tokendoctor:sessions to see what your last 30 days would have cost
at each window. Nothing changes until you pick it.
Every request sends the whole conversation to the model. On models with a 1M window, Claude Code compacts only near 967K tokens, so the end of a long session is the expensive part. For me, two thirds of main-thread cost went to requests with more than 400K in context.
So I set a 400K window and Sonnet for subagents. Comparing the month before with the week after, about 23K and 19K main-thread requests, context per request went from 412K to 219K and cost per request fell 38% at API list prices. That's one person's before and after, not a controlled experiment.
The catch is more summaries, and each is a pause: 79 seconds on average in my sessions. That's what the slide is for. Your sessions may show something else entirely, which is the point of looking at them first.
On the benchmark, Claude Code builds a TypeScript project against tests it can't change, so a run counts only if the tests pass. Cost is per task, on Haiku 5.5:
Every test passed in every run. The advice alone didn't pay here because these tasks rarely pass 400K, which is where the window starts to matter. If your sessions don't either, your replay will show it, and you should leave your window alone. Every run, the losing ones too, is in bench/HISTORY.md.
  
/tokendoctor:dashboard: where every token went, by day, model, subagent and project. One local file; this one is mine.
Nothing leaves your machine: the only network call is to two public pages of Claude Code's docs, once a day. It never switches your models on its own.
tokendoctor.localix.ai/docs has the rest: the 38 checks, every setting, how the slide works (and Team and Enterprise logins), the commands from a shell, the measurements and the limits. To work on tokendoctor itself, see CONTRIBUTING.md.
MIT
