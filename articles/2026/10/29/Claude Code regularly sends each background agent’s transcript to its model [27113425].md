---
id: "271134257c4af766"
title: "Claude Code regularly sends each background agent’s transcript to its model"
url: "https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce"
link: "https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce"
source: "GitHub"
domain: "gist.github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-29T03:33:42Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["NikZaal"]
language: "en"
summary: "by Flamerix AI · MIT License\nTested on Linux, Claude Code 2.1.257–2.1.312 (see Tested versions). The binary is not modified (BUN_OPTIONS=--preload). An update can silently undo it, so see Verify.\ncurl -fsSL https://gist.githubusercontent.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce/raw/no-agent-summary.js -o ~/.local/share/no-agent-summary.js\nclaude daemon stop…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1271
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50284255"
score: 430
comments: 162
community: "Hacker News"
---

# Claude Code regularly sends each background agent’s transcript to its model

GitHub · NikZaal · 2026-10-29

by Flamerix AI · MIT License
Tested on Linux, Claude Code 2.1.257–2.1.312 (see Tested versions). The binary is not modified (BUN_OPTIONS=--preload). An update can silently undo it, so see Verify.
curl -fsSL https://gist.githubusercontent.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce/raw/no-agent-summary.js -o ~/.local/share/no-agent-summary.js
claude daemon stop --any
BUN_OPTIONS="${BUN_OPTIONS:+$BUN_OPTIONS }--preload $HOME/.local/share/no-agent-summary.js" claude
To make it permanent for every Claude Code process, see Install.
Every ~30 seconds, for every background agent, Claude Code sends that agent's entire transcript to the agent's own model (usually Opus) and asks it to "describe your most recent action in 3-5 words". The answer only updates the agent's status line in the agents panel; it never reaches the model or your conversation. There is no setting that turns it off, and since 2.1.232 (August 2026) it has been on by default.
The anomaly was detected by DRIM in Claude Code's OpenTelemetry export:
grouping claude_code.api_request events by query_source showed agent_summary costing more than the main conversation itself.
Spend here means Claude Code's own per-request estimate (cost_usd), not an invoice: on a
subscription, what you lose is rate-limit headroom. We are not the only ones who measured it:
#86879 collects four independent
measurements of 18–26 %.
no-agent-summary.js is a Bun preload (~80 lines of code). It wraps setTimeout/setInterval;
when a callback's source text contains a summarizer anchor (e.g. the [AgentSummary] Timer fired
log line), it returns an inert handle instead of arming the timer. Every other timer passes
through untouched. In the OpenTelemetry export the suppressed requests are
claude_code.api_request events with query_source = agent_summary.
Why a timer hook rather than something simpler: the module ships as precompiled Bun bytecode, so
editing its JS text inside the binary changes nothing, and the API client does not go through a
wrapped globalThis.fetch. But Function.prototype.toString still returns a callback's source
even when it runs from bytecode, so the timer can be recognised by a string inside it. The inert
timer uses exactly 2³¹−1 ms: Node and Bun treat a larger delay as 1 ms, so an "infinite" delay
would fire at once.
- Put no-agent-summary.js somewhere stable; note its absolute path.
- Set BUN_OPTIONS globally so every Claude Code process gets it. One of:
# ~/.profile, ~/.bashrc, ~/.zshrc export BUN_OPTIONS="${BUN_OPTIONS:+$BUN_OPTIONS }--preload /abs/path/no-agent-summary.js" # ~/.config/fish/config.fish set -gx BUN_OPTIONS "--preload /abs/path/no-agent-summary.js" # ~/.config/environment.d/50-no-agent-summary.conf (systemd user env; also reaches # user services and timers; applies when the user manager next starts, usually next login) BUN_OPTIONS=--preload /abs/path/no-agent-summary.js Or a wrapper named claude earlier on PATH (the case keeps it idempotent when one Claude
Code process starts another):
#!/bin/sh HOOK=/abs/path/no-agent-summary.js case " ${BUN_OPTIONS-} " in *" --preload $HOOK "*) ;; *) export BUN_OPTIONS="${BUN_OPTIONS:+$BUN_OPTIONS }--preload $HOOK" ;; esac : "${CC_AGENT_SUMMARY_LOG:=${XDG_RUNTIME_DIR:-/tmp}/no-agent-summary.log}" export CC_AGENT_SUMMARY_LOG exec /path/to/the/real/claude "$@"
- Restart the daemon and every already-running session, then start Claude Code from an
environment that has BUN_OPTIONS:
claude daemon stop --any
- Restart the daemon after install. The daemon, pty host and pre-warmed bg-spare sessions
inherit the environment of the client that started the daemon, so a daemon started before BUN_OPTIONS was set keeps spawning unhooked sessions. Hence claude daemon stop --any.
- Headless runs need it too: claude -p, cron, CI, editor integrations.
- Platform: Linux tested, macOS and Windows untested. On Windows the /$bunfs/ gate most
likely never installs the hook.
- A/B: CC_AGENT_SUMMARY_MODE=pass loads the hook but arms every timer; the summaries come back, which shows the off result is the hook's doing.
- Background processes: daemon, pty host and bg-spare must carry --preload in their environment (/proc/<pid>/environ on Linux); if not, restart the daemon.
- Preload loads: BUN_OPTIONS="--preload $HOME/.local/share/no-agent-summary.js" CC_AGENT_SUMMARY_LOG=/tmp/nas.log claude --version && cat /tmp/nas.log Expect preload active mode=off …. No line: BUN_OPTIONS did not reach the process, or the
path is not absolute.
- Timer suppressed: with the same BUN_OPTIONS and CC_AGENT_SUMMARY_LOG=/tmp/nas.log, run
a background subagent for a minute or two. The log shows summary timer #1 suppressed (setTimeout, delay=30000) and the agent's panel status stops
updating. If you export OpenTelemetry, query_source = agent_summary should stay at zero; this
is the only check that catches every failure mode.
Matching is by source text: an anchor must sit inside the callback passed to the timer. If an update breaks that, the hook matches nothing and summaries silently come back. Ways it can happen:
- the log line or query-source id is renamed;
- the callback is passed via fn.bind(...) (no source in toString) or another wrapper;
- the strings move to a shared constant outside the callback;
- the timer moves to an unwrapped API (timers/promises, a scheduler loop).
So re-run Verify after every update.
- We run it under every Claude Code process on our machine (2.1.301). Since then there have been
zero agent_summary requests, and no other side query grew to take its place.
- Subagents, background agents, forked skills and background sessions run normally; only the summary fork is skipped.
- Visible change: the per-agent panel status stops updating; SDK task_progress has no summary.
- Overhead: one Function.prototype.toString per distinct timer callback, cached in a WeakMap. claude --version: ~10 ms → ~17 ms (one measurement).
Linux x64 binary from npm @anthropic-ai/claude-code-linux-x64 (its sha256 equals the native
installer's manifest.json checksum). Static: the extracted bundle's summary timer callback
carries a hook anchor. Live: claude -p --model haiku with
CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES=1, one subagent doing 8 steps of ~20 s, counting
[AgentSummary] Forking in --debug-file.
5 / 5 / 0 = the fork happens on this version, merely loading the hook changes nothing, and off
removes it.
- The documented switch only turns it on. The SDK option agentProgressSummaries defaults to false, but in the bundle it is one term of an OR, and every code path that writes it sets true. So false changes nothing, and the undocumented CLAUDE_CODE_AGENT_PROGRESS_SUMMARIES can only enable summaries too.
- The interval belongs to the server. It comes from a per-model-family server flag and is clamped to 30–240 s. The default is already the minimum, and no value disables the timer.
- The obvious env vars miss. DISABLE_NON_ESSENTIAL_MODEL_CALLS, which some packagers set,
does not occur in the binary at all. CLAUDE_CODE_FORK_SUBAGENT=0 and CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1 do stop it, but only by taking fork subagents or
background agents with it.
- The prompt cache makes it cheaper, not cheap. About 98 % of these calls re-read the transcript from cache; the ~2 % that hit a cold cache carry over a third of its cost.
- Cost tools that read transcripts don't see it. These requests are not written to the session logs on disk (#104358); only the OpenTelemetry export shows them. The docs section on background token usage doesn't list it either, while Agent View's row summaries are documented as a Haiku-class model refreshing every few minutes.
- A cheaper variant already exists, switched off. 2.1.310 ships a short mode: about 2k
tokens of notes instead of the full transcript, optionally written by a smaller model. The
default is still the full transcript, and only server flags can change it.
In our telemetry its weekly share of spend went from 3.5–7 % in July (the fork gate was already open for us) to 7.3 % and then 11.8 % in the week we picked up 2.1.233, and to about 16 % by mid-October.
MIT © 2026 Flamerix AI. Provided as is, without warranty of any kind; you use it at your own risk. Flamerix AI is not liable for any damage, data loss or account action arising from its use. Changing a client's runtime behaviour may conflict with the terms of the service you use it with; checking that is on you.
"Claude" and "Claude Code" are trademarks of Anthropic, PBC. This project is independent and is not affiliated with, sponsored or endorsed by Anthropic.
