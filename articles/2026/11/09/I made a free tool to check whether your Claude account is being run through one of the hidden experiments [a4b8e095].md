---
id: "a4b8e09555012bfc"
title: "I made a free tool to check whether your Claude account is being run through one of the hidden experiments people are talking about"
url: "https://reddit.com/r/ClaudeAI/comments/1xrxiru/i_made_a_free_tool_to_check_whether_your_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xrxiru/i_made_a_free_tool_to_check_whether_your_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T17:15:27Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["electricshadows4"]
language: "en"
summary: "I've seen a lot of threads on here about Anthropic nerfing or at least doing A/B testing on people's accounts without them knowing. There's a way to actually look to see if your account is affected, so I had it packaged into something anyone can run in about a minute. Repo (free, MIT): https://github.com/electricshadows44/am-i-nerfed Claude Code caches an experiment assignment in a local config…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 472
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrxiru/i_made_a_free_tool_to_check_whether_your_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a free tool to check whether your Claude account is being run through one of the hidden experiments people are talking about

Reddit · electricshadows4 · 2026-11-09

I've seen a lot of threads on here about Anthropic nerfing or at least doing A/B testing on people's accounts without them knowing. There's a way to actually look to see if your account is affected, so I had it packaged into something anyone can run in about a minute. Repo (free, MIT): https://github.com/electricshadows44/am-i-nerfed Claude Code caches an experiment assignment in a local config file and sends it to Anthropic with every request. Recent posts on r/ClaudeCode found that under some assignments the same model behaves differently — more tool calls per reply, much longer shell commands, less narration — and one assignment even added text to the system prompt. This tool shows you whether your account has one. Three ways to check Plugin — install the repo as a Claude Code plugin, then type /am-i-nerfed in any session. Claude runs the check and explains the result. Script — clone the repo and run ./am-i-nerfed.sh check in a terminal. One-liner, no install — paste this into a terminal (needs jq ): jq -r '(.clientDataCacheSlots // {}) | to_entries[] | "\(.value.model // "-") | \(.value.entrypoint // "-") | \(((.value.at // 0)/1000|floor)|todate) | \(.value.data.atis[0:3] // "none") | \(.value.data.experimentKey // "-")"' ~/.claude.json none on every line = not enrolled as of the newest slot time. What the script does check — verdict per model: ENROLLED (with the ID and experiment name), CLEAN as of the last cache refresh, or INCONCLUSIVE. history — tallies experiment IDs recorded in your past session transcripts by date, so you can see which sessions ran under one (transcripts are kept ~30 days). optout — backs up the config file, removes only the assignment keys, and prints the env var people report blocks re-enrollment, with the trade-offs. restore undoes it. statusline — shows exp:<id> / exp:none in your Claude Code status line so you'll see it the moment it changes. Bash + jq only, macOS/Linux/WSL, no network calls, never prints your login token or account IDs. Unofficial. The measurements show behaviour changes, not proven quality loss. Whether an experiment made your results worse is for you to judge — this just tells you whether you were in one. How I built it with Claude Code Single Claude Code session on Opus 5.5 xhigh. Claude Code wrote the bash script, the test suite with synthetic config files, the Claude Code plugin/skill wrapper, and the docs. It also found something I didn't know to ask for: while scanning my own session transcripts it discovered that Claude Code writes an atis-latch record into every session, which is what makes the history command possible. I then had a separate Claude chat (Fable 5.1 medium) audit the code against the spec (token leakage, file scope, that opt-out removes only the two assignment keys and backs up first), and fed the findings back for one fix round.
