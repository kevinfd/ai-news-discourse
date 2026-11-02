---
id: "6c82a81acffbb877"
title: "19 LLMs played 376 games of a word-association game against each other. The team with the better guesser won 68% of the time, the one with better clues only 53%"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xld7w9/19_llms_played_376_games_of_a_wordassociation"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xld7w9/19_llms_played_376_games_of_a_wordassociation"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T20:16:16Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Hardicecream17"]
language: "en"
summary: "I built a browser word game inspired by Codenames (not affiliated) where any seat can be a person or an LLM, and had models play each other on a 5x5 board. Each model gives the clues and makes the guesses for its own team, against a different model. What came out of 376 games: Ambitious clues lose. The team that went for more words per clue won only 38% of 287 games. The guesser decides the…"
tags: ["r/ArtificialInteligence"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 248
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xld7w9/19_llms_played_376_games_of_a_wordassociation/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# 19 LLMs played 376 games of a word-association game against each other. The team with the better guesser won 68% of the time, the one with better clues only 53%

Reddit · Hardicecream17 · 2026-11-01

I built a browser word game inspired by Codenames (not affiliated) where any seat can be a person or an LLM, and had models play each other on a 5x5 board. Each model gives the clues and makes the guesses for its own team, against a different model. What came out of 376 games: Ambitious clues lose. The team that went for more words per clue won only 38% of 287 games. The guesser decides the game. The team whose guesser did better won 68% of games, and the team with better-graded clues won 53%. Either guessing is the skill that matters, or my clue grade measures the wrong thing. Going first doesn't help. The first team won 169 of 376, even though it has one extra word to find. Newer models are much better guessers: 71 to 93% good guesses against 49 to 71% for the older ones. The two groups ran with different settings, so read that as a direction, not a measurement. How a clue is graded: each board word gets an association score with the clue, one third from embedding similarity and two thirds from two LLM raters who don't know which words belong to which team. A guesser fitted on real games plays the turn out, and the expected value of the cards it reveals is scaled to 0-100. The games are replayable at wordspies.com , and the raw data is on Hugging Face (daluan/word-spies-llm-benchmark). I'd like to hear what you'd measure instead.
