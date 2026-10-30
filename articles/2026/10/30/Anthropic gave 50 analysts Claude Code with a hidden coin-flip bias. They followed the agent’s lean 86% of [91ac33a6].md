---
id: "91ac33a622382342"
title: "Anthropic gave 50 analysts Claude Code with a hidden coin-flip bias. They followed the agent’s lean 86% of the time"
url: "https://reddit.com/r/ClaudeAI/comments/1xj3qdv/anthropic_gave_50_analysts_claude_code_with_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xj3qdv/anthropic_gave_50_analysts_claude_code_with_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T02:35:00Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["emarkosov"]
language: "en"
summary: "Anthropic's alignment team published this on Oct 27 and the press picked it up this week. Short version: 50 professional analysts did a realistic statistical analysis with Claude Code. Each agent had a hidden \"lean\" on four analytical choices, set by coin flip through a hidden system prompt. The analysts were not told. What they found: - Analysts went with the agent's lean 86% of the time.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "safety & ethics", "models & research"]
content_source: "post"
word_count: 318
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj3qdv/anthropic_gave_50_analysts_claude_code_with_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic gave 50 analysts Claude Code with a hidden coin-flip bias. They followed the agent’s lean 86% of the time

Reddit · emarkosov · 2026-10-30

Anthropic's alignment team published this on Oct 27 and the press picked it up this week. Short version: 50 professional analysts did a realistic statistical analysis with Claude Code. Each agent had a hidden "lean" on four analytical choices, set by coin flip through a hidden system prompt. The analysts were not told. What they found: - Analysts went with the agent's lean 86% of the time. Chance would be about 50%. Per decision it ranged from 81% to 92%. - When an analyst had already written down their own preference, they switched away from it 60% of the time if the agent disagreed, vs 6% if it agreed. Small sample for that one (38 cases), so treat it as a signal, not a law. - 77% of analysts used the agent's arguments, sometimes word for word. Only 15% credited the agent as the source. - The final recommendation moved less: 54% recommended rollout when the agent leaned that way, 36% when it leaned the other way. - Not all bad: 6% of agent users made serious errors that invalidated results, vs 55% of the 11 analysts who worked without the agent. Agent users also finished faster (65 vs 90 minutes median). Anthropic says the two groups are not directly comparable. - Caveats from Anthropic itself: one task, one field, one model (Claude Opus 4.8), and the lean was deliberately made strong, so the real-world effect is probably smaller. Anthropic's own take is that this is not an argument for using AI less. They suggest agents could make the best case for each option, or ask for your view before giving theirs. I catch myself doing this in Claude Code. It proposes an approach, I say "ok", and I only notice later that I never considered an alternative. Do you ever make Claude Code argue against its own plan before you accept it? If yes, how? Source: https://www.anthropic.com/research/agents-judgment-calls
