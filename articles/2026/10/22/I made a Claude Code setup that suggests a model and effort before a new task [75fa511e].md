---
id: "75fa511ee0f10464"
title: "I made a Claude Code setup that suggests a model and effort before a new task"
url: "https://reddit.com/r/ClaudeAI/comments/1xc916a/i_made_a_claude_code_setup_that_suggests_a_model"
link: "https://reddit.com/r/ClaudeAI/comments/1xc916a/i_made_a_claude_code_setup_that_suggests_a_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T04:32:55Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["vamshikk111"]
language: "en"
summary: "I wanted Claude to give me a quick model recommendation before starting a new task, instead of leaving me to remember to reassess the model and effort every time. Yesterday I used Claude Code to put together Claude Model Guide. It's free and open source. The setup script adds a marked block to ~/.claude/CLAUDE.md, and the accompanying skill handles setup, status, removal, and on-demand…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 244
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xc916a/i_made_a_claude_code_setup_that_suggests_a_model/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Claude Code setup that suggests a model and effort before a new task

Reddit · vamshikk111 · 2026-10-22

I wanted Claude to give me a quick model recommendation before starting a new task, instead of leaving me to remember to reassess the model and effort every time. Yesterday I used Claude Code to put together Claude Model Guide. It's free and open source. The setup script adds a marked block to ~/.claude/CLAUDE.md, and the accompanying skill handles setup, status, removal, and on-demand recommendations. The rule asks Claude to look at the scope and difficulty, then suggest the lightest available model and effort that seem suitable. The starting idea is Haiku for focused work, Sonnet for everyday coding and research, and Opus for harder reasoning, subject to what's actually available in your setup. I still control the switch through /model and /effort. After the recommendation I can switch and say `go`, or say `continue` to stay where I am. This is an instruction convention, so it isn't a guaranteed interceptor or an automatic router. Non-interactive runs are meant to proceed without waiting for that reply. The installer previews changes, backs up the file, and removes only its own marked block when uninstalled. There's also preference text for the Claude apps, which use a different setup from Claude Code. I haven't benchmarked savings. The extra pause may be annoying on tiny tasks, and the recommendation itself uses tokens. That's the part I'd most like feedback on. My Claude-specific repo: https://github.com/vamshicreates/claude-model-guide Would you want this nudge before every new task, or only for larger changes?
