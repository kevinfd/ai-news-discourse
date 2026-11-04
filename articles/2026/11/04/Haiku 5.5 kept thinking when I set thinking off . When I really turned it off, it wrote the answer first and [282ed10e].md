---
id: "282ed10e9465153e"
title: "Haiku 5.5 kept thinking when I set thinking \"off\". When I really turned it off, it wrote the answer first and argued with it afterwards."
url: "https://reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off"
link: "https://reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T00:44:02Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Hardicecream17"]
language: "en"
summary: "I've been running LLMs against each other in a word-association game I'm building (one model gives a one-word clue, its teammate guesses). I was picking a cheap model for the free tier: Haiku 5.5 vs GPT-6 Luna, both with thinking off. Haiku won 9-7. Then I found that on the API route I was using, Haiku 5.5 thinks by default, and my \"off\" never sent the setting that disables it. It had been…"
tags: ["r/ClaudeAI"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["models & research"]
content_source: "post"
word_count: 507
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Haiku 5.5 kept thinking when I set thinking "off". When I really turned it off, it wrote the answer first and argued with it afterwards.

Reddit · Hardicecream17 · 2026-11-04

I've been running LLMs against each other in a word-association game I'm building (one model gives a one-word clue, its teammate guesses). I was picking a cheap model for the free tier: Haiku 5.5 vs GPT-6 Luna, both with thinking off. Haiku won 9-7. Then I found that on the API route I was using, Haiku 5.5 thinks by default, and my "off" never sent the setting that disables it. It had been reasoning the whole time and I wasn't seeing it. Once thinking was really off, Haiku lost its first two games to illegal clues (a clue can't be a word on the board): "Shoe 2", with Shoe on the board. Its reasoning, written after the clue: "Shoe is risky. I avoided it by choosing a different clue. Treat this candidate as recorded only." "Bedroom 2", with Bed on the board: "Bedroom is not a clean fit, so I'll switch to a stronger option... I record it only as a fallback." On the same board with its default thinking, it had opened with a legal "Golf 4". What was going on: my output format was JSON with "clue" first and "reasoning" second. With no thinking pass, the clue is the first thing it writes, so it commits before thinking. The reasoning field then becomes its thinking: it notices the clue is bad, tries to take it back in text, and that does nothing because the clue is already written. The fix was swapping the fields so reasoning comes first. On those two positions, 5 samples each: illegal clues went from 2 of 10 to 0 of 10, and the average clue grade from 30 to 64 (out of 100). GPT-6 Luna on the same test didn't change (0 illegal either way, 66 vs 66). Two takeaways if you run Claude with thinking off: Check that it's really off on your route. For Haiku 5.5 on mine it needed an explicit no-reasoning setting. With thinking off, the field order in your structured output is the chain of thought. If the answer comes first, the "reasoning" is a justification written after the fact. Small sample (10 samples per model on 2 positions); a full 16-game rerun is going now and I'll post the numbers. Edit: the full 16-game rerun finished. With thinking really off, GPT-6 Luna beat Haiku 5.5 14-2. Illegal clues: Haiku 6, Luna 1, and each illegal clue ends the game on the spot, so 6 of Haiku's 14 losses came from that. Average clue grade: Haiku 38, Luna 48. Guesses: Luna found 80 of its own words to Haiku's 40, with 1 assassin hit each. This was the original clue-first format, so it's the failure described above at full scale; the reasoning-first fix isn't in these games yet. More broadly, OpenAI's GPT-6 models have graded higher than Claude 5.x at giving clues in every run I've done. With thinking on high: GPT-6.1 Terra 64, Astra 63, Sol 61, against Opus 5.5 58, Sonnet 5 57, Fable 5.1 56. Google's Gemini 4 Argon (67) tops both.
