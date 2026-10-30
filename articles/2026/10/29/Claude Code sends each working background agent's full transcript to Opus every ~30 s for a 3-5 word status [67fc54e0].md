---
id: "67fc54e0782a2b03"
title: "Claude Code sends each working background agent's full transcript to Opus every ~30 s for a 3-5 word status line. No off switch. Data + workaround"
url: "https://reddit.com/r/ClaudeAI/comments/1xiozm7/claude_code_sends_each_working_background_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xiozm7/claude_code_sends_each_working_background_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T16:36:59Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["NickZaal"]
language: "en"
summary: "What happens: For every background agent that is actively working, Claude Code sends that agent's entire transcript to its active model (usually Opus) about every 30 seconds and asks it to \"describe your most recent action in 3-5 words\" . The answer only updates the status line in the agents panel. It has been on by default since 2.1.232 (August) and ships in the stable channel. Our numbers…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 467
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xiozm7/claude_code_sends_each_working_background_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code sends each working background agent's full transcript to Opus every ~30 s for a 3-5 word status line. No off switch. Data + workaround

Reddit · NickZaal · 2026-10-29

What happens: For every background agent that is actively working, Claude Code sends that agent's entire transcript to its active model (usually Opus) about every 30 seconds and asks it to "describe your most recent action in 3-5 words" . The answer only updates the status line in the agents panel. It has been on by default since 2.1.232 (August) and ships in the stable channel. Our numbers (Claude Code's own per-request cost estimate in its OpenTelemetry export, not an invoice): 16.4% of all Claude Code spend in one week, about 1 in 5 API requests Weekly share grew from 3.5-7% in July to about 16% by mid-October : a jump when it went default-on, then steady growth as we moved more of our work into subagents About 96% of input tokens are cache reads , yet cache reads are still about half of all spend, and about two-thirds of the cost of the summary calls themselves. Cached doesn't mean cheap. Our workload is subagent-heavy (we're building an orchestration layer, DRIM, on top of it), so we're above average. Others in the GitHub issue (#86879) measured 18-26% . Anthropic replied on HN : About 2% of cost across telemetry users, about 6% in the terminal; a fix for summaries that miss the cache shipped in 2.1.311+, and a cheaper mode with a smaller model is in progress. Thanks for that. But an average over all users also counts everyone who never runs a background agent, and the fix makes each call cheaper, not rarer: on 2.1.312 it still fires every ~30 s per working agent. Why you can't just turn it off: The SDK option agentProgressSummaries: false changes nothing, and the CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES env var can only turn it on DISABLE_NON_ESSENTIAL_MODEL_CALLS doesn't exist in the binary CLAUDE_CODE_FORK_SUBAGENT=0 or CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 stop it, but take fork subagents or background agents with them The interval (30-240 s) and the cheaper short mode are server flags These requests don't show up in the session transcripts on disk (#104358), so transcript-based cost tools don't see them Workaround: A small Bun preload that keeps the summary timer from firing. The binary is not modified. Tested on Linux 2.1.257-2.1.312; another user confirmed it on macOS ( darwin-arm64 , 2.1.312). It fails open if Claude Code renames things, so re-verify after updates. Changing client behavior may conflict with the terms of service; that's your call. Gist (full write-up + script): https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce What I'd like: A real user-side switch for a stable, default-on feature. The simplest one would be making agentProgressSummaries: false actually turn it off. If you export OpenTelemetry, you can check your own share: group the api_request events by query_source and look for agent_summary . I'd like to see numbers from other setups and does my hook works on windows (works on mac and linux).
