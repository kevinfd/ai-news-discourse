---
id: "8dcbb0f45d400fa9"
title: "Having agents reset context around 225K tokens dropped cosr by 50-75% for me"
url: "https://coralhub.dev/blog/context-reset-turn-cost.html"
link: "https://coralhub.dev/blog/context-reset-turn-cost.html"
source: "Subgentic LLC"
domain: "coralhub.dev"
source_type: "community"
collector: "reddit"
date: "2026-11-13T19:01:08Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["orbital_trace"]
language: "en"
summary: "I've been running agents 24/7 and just letting the context fill up. Claude has a setting to compact at a specific time, but I just built it into my harness so that it can happen at the end of a tasks completion instead of randomly. Costs dropped significantly."
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 713
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvgier/having_agents_reset_context_around_225k_tokens/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Having agents reset context around 225K tokens dropped cosr by 50-75% for me

Subgentic LLC · orbital_trace · 2026-11-13

← Back to Blog
Using Coral's Context Reset to reduce average turn cost by 50-75%
Long-running agents carry everything they’ve ever read into every new request. Each turn re-reads that entire accumulated history from the cache, and those cache reads dominate the API bill. Context Reset lets an idle agent shed that bloat without losing its working state.
On 10 November at 04:31 UTC I turned on Automated Context reset in Coral. Here is what happened.
- Cost per turn: dropped from ~$0.16 to $0.055 (a ~65% reduction).
- Average context carried: fell from ~480k tokens to 178k tokens.
- High-context turns: before the reset, 80% of turns ran with contexts over 200k tokens. After, only 30% did.
Breaking it down by model:
- Opus 5.5: fell from ~$0.27/turn to $0.10/turn.
- Sonnet 5.5: fell from ~$0.11/turn to $0.05/turn.
Throughput didn't drop. We sustained ~1,230 turns/hour after the switch, squarely inside our pre-switch baseline of 630 to 1,620 turns/hour.
Coral is open source and runs on your own computer. Download Coral or see the source on GitHub.
Where the Savings Actually Come From
A turn is a single call to the model. Its token breakdown tells the whole story:
- Input (new): text the model hasn't seen before. In our runs, this is roughly 2 tokens per turn. Negligible, because almost everything hits cache.
- Cache write: new context added for subsequent turns (user prompts, tool outputs). Averages 1,500 to 4,500 tokens/turn. It costs slightly more than raw input, but volume is modest.
- Cache read: the entire active history re-read on every request. While cheap per token, it was running at 430,000 to 550,000 tokens per turn, which is most of the bill. A shorter context shrinks that read on every later turn, and that is the saving.
How it works
Once a minute Coral looks at each agent in a team that has the setting on. It acts only when the agent is idle, its context is over the team's limit (225,000 tokens by default), it has no unread board message, and it is not stopped by a usage limit. It never types over a draft or a dialog, and it leaves each agent alone for 30 minutes after a reset.
Then it types one fixed line: the agent's own compaction command. For Claude it carries one instruction: keep open tasks, team rules, recent decisions, and what the agent was last asked. For the others it is the bare command. Nothing from a task or a message goes into that line. The same setting offers two stronger choices: "Clear, then the next task", and "Ask for a handoff note, clear, then the note", where the agent first writes down what it needs. The orchestrator is included by default.
What a compaction drops, the agent can fetch. It searches its own earlier words with coral-agent history search "words" and reads around a hit with coral-agent history context N.
Any harness
Context Reset is harness agnostic. It acts on the agent, not on the model or the company behind it: the checks (idle, nothing unread, no dialog open), the size limit and the handoff note are the same for every agent. Claude, Codex, Antigravity and Pi each have a compaction command of their own, and Coral sends the right one.
A note on how we found it
Before building anything, we measured our own transcripts: 14 days, 107 sessions, 301,377 requests, 139 billion cache-read tokens. The mean context was 463,000 tokens, and 94% of all cache reads happened in requests whose context was over 200,000.
We then replayed five ideas on those sessions to see what each would have saved:
Two results shaped the design. Capping tool output was the smallest idea, because results are short. And a fresh session starts at about 39,000 tokens while a real compaction lands at about 56,000, so a full reset beats a compaction by only about 11,000 tokens a request, and it costs the agent its place. So we built the first row. These figures are upper bounds: they assume nothing has to be re-read after a compaction loses detail.
What's next
We will continue to experiment with different settings and track total performance against our tasks per touches metrics. Have any ideas? Let us know.
