---
id: "316c11d5287d1364"
title: "Measured audio feedback for an AI assistant controlling a synthesizer"
url: "https://reddit.com/r/ArtificialInteligence/comments/1x53ir7/measured_audio_feedback_for_an_ai_assistant"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T17:48:39Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["sporeman456"]
language: "en"
summary: "I’m Max, Ratio9’s developer. Ratio9 exposes a synthesizer’s controls and audio analysis through a local stdio MCP connection. A compatible assistant can read/change parameters, choose wavetables, shape modulation, trigger notes and request fresh measurements before revising a preset. The useful distinction is between a parameter proposal and evidence from the resulting audio. The spectrum…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 174
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1x53ir7/measured_audio_feedback_for_an_ai_assistant/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Measured audio feedback for an AI assistant controlling a synthesizer

Reddit · sporeman456 · 2026-10-13

I’m Max, Ratio9’s developer. Ratio9 exposes a synthesizer’s controls and audio analysis through a local stdio MCP connection. A compatible assistant can read/change parameters, choose wavetables, shape modulation, trigger notes and request fresh measurements before revising a preset. The useful distinction is between a parameter proposal and evidence from the resulting audio. The spectrum describes frequency energy for the captured window; the spectrogram adds its movement through time. This helps inspect a revision, but is not a perceptual-quality score and does not establish that a patch will work musically across every register or velocity. The instrument remains usable manually, and the saved patch is independent of the chat. A measurement snapshot is not automatically part of the preset file; the analysis can be exported separately. The two screenshots show the interface at INIT and a separate growl-preset analysis example, not a controlled before/after experiment. This is a project explanation rather than a model-quality benchmark. Demo context: https://www.youtube.com/watch?v=sfC5ZhBpHxo — the earlier development recording has waiting edited out, so it is not an uncut timing test.
