---
id: "f199f8967c6c8c09"
title: "I built a read-only monitor for Claude Code sub-agents: who's working, who's stuck, who's waiting on you, screensharing"
url: "https://reddit.com/r/ClaudeAI/comments/1x7iegx/i_built_a_readonly_monitor_for_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1x7iegx/i_built_a_readonly_monitor_for_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T14:55:40Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["stickygoose"]
language: "en"
summary: "I built Agent Standup, a free, open-source tool that shows your Claude Code sessions and their sub-agents as a live call: who's working, who's waiting on which sub-agent, and which session is sitting on a prompt for you. (Video above.) How Claude Code helped build it Most of the code was written in Claude Code sessions, with me deciding what to build and reviewing every change. The commits in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Mistral", "Cursor"]
topics: ["agents & coding", "products & launches", "models & research", "search & media"]
content_source: "post"
word_count: 367
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7iegx/i_built_a_readonly_monitor_for_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a read-only monitor for Claude Code sub-agents: who's working, who's stuck, who's waiting on you, screensharing

Reddit · stickygoose · 2026-10-16

I built Agent Standup, a free, open-source tool that shows your Claude Code sessions and their sub-agents as a live call: who's working, who's waiting on which sub-agent, and which session is sitting on a prompt for you. (Video above.) How Claude Code helped build it Most of the code was written in Claude Code sessions, with me deciding what to build and reviewing every change. The commits in the repo are co-authored by Claude. Claude Code's session files aren't documented, so Claude worked out the format from real transcripts on my machine, including the ones it was writing at the time. It did the same for Codex rollout files and both of Mistral Vibe's formats. Before each release, Claude Code runs the previous and the new version side by side on my ~120 real sessions and compares every API response. Then a sub-agent does an adversarial review whose only job is to prove the release breaks something for existing users. That review caught a bug that would have taken the whole session list down, which the tests had missed. The first video on the project's YouTube channel is a real Claude Code session, the one that made that video, replayed in the app. What it does It reads the files Claude Code already writes in ~/.claude/projects (read-only, no hooks) and gives you: a board of every session: working, waiting, or needs you tokens per agent, to spot the expensive sub-agent a flag when a command runs over a minute, or an agent goes quiet for 3 minutes replay of any past session, with a recap of commands and files changed a one-line status for tmux or the Claude Code status line It also reads Codex and Mistral Vibe sessions. It makes no model calls (zero tokens) and sends nothing anywhere. Free to try It's free and MIT licensed, with no account. Try it with a built-in demo (Node 18+): npx @double_geste/agent-standup --open Or search "Agent Standup" in the VS Code / Cursor extensions view. There's also a desktop app. An optional paid character pack exists; everything else is free. Repo: https://github.com/Atoll92/agent-standup Website: https://agent-standup.com What would you want to see per sub-agent that it doesn't show yet?
