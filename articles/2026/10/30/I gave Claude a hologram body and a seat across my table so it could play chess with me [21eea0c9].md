---
id: "21eea0c953adc21b"
title: "I gave Claude a hologram body and a seat across my table so it could play chess with me"
url: "https://reddit.com/r/ClaudeAI/comments/1xj764h/i_gave_claude_a_hologram_body_and_a_seat_across"
link: "https://reddit.com/r/ClaudeAI/comments/1xj764h/i_gave_claude_a_hologram_body_and_a_seat_across"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T05:40:22Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["devaddict247"]
language: "en"
summary: "I built a chess game for Apple Vision Pro where the opponent is a hologram wizard powered by Claude Haiku. He sits across your real table, reaches over to move his own pieces and talks with you out loud the whole game. The part I think this sub will find interesting is the split between engine and model. A chess engine produces a handful of candidate moves with a one-line fact for each. Claude…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["models & research"]
content_source: "post"
word_count: 226
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj764h/i_gave_claude_a_hologram_body_and_a_seat_across/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude a hologram body and a seat across my table so it could play chess with me

Reddit · devaddict247 · 2026-10-30

I built a chess game for Apple Vision Pro where the opponent is a hologram wizard powered by Claude Haiku. He sits across your real table, reaches over to move his own pieces and talks with you out loud the whole game. The part I think this sub will find interesting is the split between engine and model. A chess engine produces a handful of candidate moves with a one-line fact for each. Claude picks one in character and says one line about the actual position. It is never allowed to invent a move, so it cannot hallucinate an illegal one. Anything late or off-list falls back to the engine's best move. The personality is all Claude and the chess strength is all engine. A few things I learned: Strict JSON through a schema mattered more than the prompt. Without it Haiku reasoned in prose and ran out of tokens before answering. Giving it one concrete fact per candidate ("takes knight, check") is what made the trash talk about the real game instead of generic. Handing back its last few lines stopped it repeating itself. It is free to download and playing the on-device engine is free. Games against the wizard are $0.99 since each costs real model and voice time. Link in the comments. Happy to go deeper on the prompt or the latency budget.
