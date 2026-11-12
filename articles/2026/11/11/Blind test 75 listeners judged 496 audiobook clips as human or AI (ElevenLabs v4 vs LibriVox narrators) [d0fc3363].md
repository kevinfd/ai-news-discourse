---
id: "d0fc3363963b19c8"
title: "Blind test: 75 listeners judged 496 audiobook clips as human or AI (ElevenLabs v4 vs LibriVox narrators). Accuracy 48.8%, and 'very confident' answers were no better"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xtvyjt/blind_test_75_listeners_judged_496_audiobook"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xtvyjt/blind_test_75_listeners_judged_496_audiobook"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T22:39:05Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["antiochIst"]
language: "en"
summary: "A study I ran and am sharing with the numbers so it stands on its own. Results Overall accuracy 48.8% (242/496), 95% CI 44.0 to 53.8. On AI clips 46.7%, on human clips 51.7%. d' = -0.04. Listeners said \"human\" 52.6% of the time; the true human share was 41.7%. Clip length did nothing: 15 s 49.1%, 30 s 48.1%, 60 s 49.1%. The 60 s minus 15 s difference is 0.0 points (CI -8.9 to +8.9). Confidence…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: []
content_source: "post"
word_count: 469
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xtvyjt/blind_test_75_listeners_judged_496_audiobook/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Blind test: 75 listeners judged 496 audiobook clips as human or AI (ElevenLabs v4 vs LibriVox narrators). Accuracy 48.8%, and 'very confident' answers were no better

Reddit · antiochIst · 2026-11-11

A study I ran and am sharing with the numbers so it stands on its own. Results Overall accuracy 48.8% (242/496), 95% CI 44.0 to 53.8. On AI clips 46.7%, on human clips 51.7%. d' = -0.04. Listeners said "human" 52.6% of the time; the true human share was 41.7%. Clip length did nothing: 15 s 49.1%, 30 s 48.1%, 60 s 49.1%. The 60 s minus 15 s difference is 0.0 points (CI -8.9 to +8.9). Confidence did not help: "just guessing" 54.7%, "slightly confident" 52.5%, "confident" 43.8%, "very confident" 48.7%. Of 58 very-confident errors, 36 were AI clips called human. Per speaker it is all over the place. The voice most often called human was a real narrator (81%), then ElevenLabs "Eric" (80%). Three real narrators were called human less than a third of the time (30%, 23%, 18%). How it was run One clip per trial, no reference, forced choice: "Human reading" or "AI-generated", then a confidence label. 210 clips (180 AI, 30 human) cut to 15, 30 and 60 seconds from ten calm nonfiction passages. AI side: ElevenLabs v4 at default settings, six stock voices. Human side: ten LibriVox volunteer narrators from the Hi-Fi TTS corpus. Each clip played once, no replay. Listeners never heard the same passage or speaker twice, got no feedback, and were not told the mix. Paid per second of audio regardless of answer. US residents only. 75 listeners, 496 judgments (41% of the planned 1,200, so this is interim). The part I found most useful. Before launch I trained a tiny classifier on acoustic features of the two stimulus sets. Spectral tilt alone separated AI from human with AUC 0.815: the LibriVox recordings had a different recording chain, not a different kind of speech. The human clips were equalised (+0.34 dB and a tilt correction) until the classifier dropped to AUC 0.51, and only then did the listening start. Without that step, any "humans can tell" result would have been measuring microphones. Limitations (the report lists more): interim snapshot, intervals not adjusted for repeated looks; one TTS system at default settings; volunteer readers rather than professional narrators, and their recordings were processed; 180 AI vs 30 human clips; one genre (calm nonfiction), no dialogue or emotional prose. It does not show synthetic speech is undetectable in general. The v1.0 write-up said very-confident answers were well below chance (33%); that did not hold as the sample grew, and the report says so. Why it matters: most "can people tell" claims come from unblinded listening or from clips with different recording chains. On matched material, with the chain difference removed, the answer for this one system and this one genre is no. Disclosure: I operate the listener panel (Woodstitch); funded by an audiobook producer. Full report with per-speaker and calibration tables: https://woodstitch.com/research/ai-vs-human-narration-blind-test
