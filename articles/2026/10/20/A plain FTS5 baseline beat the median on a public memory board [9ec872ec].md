---
id: "9ec872ec9f4cecb0"
title: "A plain FTS5 baseline beat the median on a public memory board"
url: "https://reddit.com/r/LocalLLaMA/comments/1xayt9l/a_plain_fts5_baseline_beat_the_median_on_a_public"
link: "https://reddit.com/r/LocalLLaMA/comments/1xayt9l/a_plain_fts5_baseline_beat_the_median_on_a_public"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T17:42:57Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["No_Issue_8224"]
language: "en"
summary: "On a public text leaderboard from August, SQLite-FTS-Baseline reached 41.79 and rank 22 of 50, with the board median at 40.78. Its README calls it a minimal deployable baseline and says it does not target the top score: SQLite holds the raw messages, FTS5 handles full text retrieval, and BM25 supplies the ranking. On the same board, just-a-BM25 scored 38.47, rank 35 of 50; per its README it…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["search & media", "models & research"]
content_source: "post"
word_count: 220
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xayt9l/a_plain_fts5_baseline_beat_the_median_on_a_public/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A plain FTS5 baseline beat the median on a public memory board

Reddit · No_Issue_8224 · 2026-10-20

On a public text leaderboard from August, SQLite-FTS-Baseline reached 41.79 and rank 22 of 50, with the board median at 40.78. Its README calls it a minimal deployable baseline and says it does not target the top score: SQLite holds the raw messages, FTS5 handles full text retrieval, and BM25 supplies the ranking. On the same board, just-a-BM25 scored 38.47, rank 35 of 50; per its README it stores each message verbatim in SQLite and runs BM25 within the exact user_id, with no LLM, embedding model or reranker in Add or Search. I like this as a reminder that a baseline should be something I actually run, not a number I assume. Both are open-source entries on the Agent Memory Leaderboard's Cycle 1 text board. For a local assistant, my history contains exact names, commands, paths and old requests mixed together. Before adding more retrieval machinery, I should know how often simple search finds the message I meant and whether anything extra improves the same queries. Otherwise I am mostly collecting pleasant demos. I have been keeping a small set of questions whose answers I can find manually in my logs, but I have not finished that comparison. What do you use for memory locally, and have you measured it against plain full text search on your own chat history?
