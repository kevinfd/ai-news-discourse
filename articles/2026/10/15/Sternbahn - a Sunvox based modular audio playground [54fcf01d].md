---
id: "54fcf01de74992e3"
title: "Sternbahn - a Sunvox based modular audio playground"
url: "https://reddit.com/r/ClaudeAI/comments/1x6cj85/sternbahn_a_sunvox_based_modular_audio_playground"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T04:42:15Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["jharsem"]
language: "en"
summary: "Sternbahn is a modular synth and groovebox for macOS, built on the SunVox engine by NightRadio. All 42 SunVox module types sit as cards on a canvas, connectable with 'audio cables'. Synths, effects, filters, LFOs and live audio input are all there. \"+ Add Module\" opens a shelf with every module, grouped by what it does musically, and each one comes with a note on what it's for. Modulation works…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 254
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6cj85/sternbahn_a_sunvox_based_modular_audio_playground/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Sternbahn - a Sunvox based modular audio playground

Reddit · jharsem · 2026-10-15

Sternbahn is a modular synth and groovebox for macOS, built on the SunVox engine by NightRadio. All 42 SunVox module types sit as cards on a canvas, connectable with 'audio cables'. Synths, effects, filters, LFOs and live audio input are all there. "+ Add Module" opens a shelf with every module, grouped by what it does musically, and each one comes with a note on what it's for. Modulation works through sockets: drag an LFO onto any control and it starts moving, and you can see the knobs turn as it plays. A built-in sequencer handles patterns and switching between slots, so you can perform with it as well as patch. The app is native SwiftUI, uses about 10–12% of one CPU core while playing, and is in a free private beta at sternbahn.com . I built it with Claude Code. Claude wrote most of the Swift: the patching UI, the CoreAudio layer around the SunVox C engine, undo/redo, the sequencer, a headless self-test suite and the in-app user guide. It also helped with the release pipeline (signing, notarization, Sparkle updates) and the website. My part was mostly direction, sound design and taste: deciding what it should feel like to play, then testing it on real hardware. One of the trickier problems we solved together was CPU use. Live animations were making SwiftUI redraw the whole window several times a second. Moving the scopes, meters and modulated knobs to Core Animation brought the app down to roughly a tenth of one core while playing.
