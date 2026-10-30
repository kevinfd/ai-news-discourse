---
id: "cce4cc9ba440e659"
title: "I'm a guitarist who used Claude to build a full guitar-theory web app and it's now teaching itself to write melodies"
url: "https://reddit.com/r/ClaudeAI/comments/1xingk9/im_a_guitarist_who_used_claude_to_build_a_full"
link: "https://reddit.com/r/ClaudeAI/comments/1xingk9/im_a_guitarist_who_used_claude_to_build_a_full"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T15:41:29Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Jon_Henderson_Music"]
language: "en"
summary: "I play guitar in a Pittsburgh jam band (Chalk Dinosaur) and do a live-looping solo project. I've always wanted a theory tool that thinks the way guitarists play: shapes, voicings, what to solo with over these chords. Since spring I've been building one with Claude, and it's grown into something I use every day. What it is: Fretbot , a free interactive guitar theory app in the browser. Fretboard:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 552
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xingk9/im_a_guitarist_who_used_claude_to_build_a_full/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I'm a guitarist who used Claude to build a full guitar-theory web app and it's now teaching itself to write melodies

Reddit · Jon_Henderson_Music · 2026-10-29

I play guitar in a Pittsburgh jam band (Chalk Dinosaur) and do a live-looping solo project. I've always wanted a theory tool that thinks the way guitarists play: shapes, voicings, what to solo with over these chords. Since spring I've been building one with Claude, and it's grown into something I use every day. What it is: Fretbot , a free interactive guitar theory app in the browser. Fretboard: a full 24-fret neck that shows any scale, mode or arpeggio, across tunings, with note names or intervals. Tap any note to hear it, play or loop the scale, and use one-, two- and three-notes-per-string shapes. Chords: a voicing engine that finds playable shapes for anything from triads to Dm9 or A7#9. It favours shapes a human hand can actually make, with honest barres and no awkward skipped strings. There's also a chord designer where you place dots and it names the chord. Progressions: describe a vibe or a key ("dreamy neo-soul in E♭"), and Claude writes progressions. Each chord gets scale suggestions to solo with, colour-coded voicings and a plain-English explanation of why it works. There's also a library of 240 progressions across pop, jazz, blues, modal, borrowed-chord and advanced styles. Backing Track: a band built from scratch in Web Audio, with no samples: drums, bass and a strummed guitar or pad. Hit "Jam over this" on any progression and the fretboard follows each chord's scale while it plays. There's a full-screen Stage mode for playing live, plus MIDI export and MIDI out to a DAW. Melody (in progress): a songwriting tab that writes three melodies over your chords. You can follow them as a scrolling tab, loop them, redo them, save them and export MIDI. How it was made: I can't really code. Everything was built in conversation with Claude, first in Claude Code and now in Claude's Cowork desktop app, working directly in the repo on my machine. A few things made it work: Diagnosis before fixes. For every bug, Claude explains the cause first, then proposes a fix. Nothing changes without my OK. Claude builds in a scratch copy, runs the tests, shows me the diff and screenshots, and I say "apply". I deploy to Vercel myself and Claude checks the live site before we commit. Real tests instead of vibes. Over time we built a music-theory "exam" for the harmony engine, a scorecard of hundreds of progressions, and rule checks that write 28,800 melodies and verify every note against the scale. I bring the ears. Claude can't hear the audio, so I listen and push back ("that note sounds wrong over that chord", "this sounds robotic"), and it digs into why. Recently I gave it two of my own recordings. It transcribed them, measured how much of my playing is pentatonic, how often I start phrases off the beat and how far I sit behind the beat, and used those numbers to rework the melody engine. The harmony side has gone way deeper than I expected: key detection that handles key changes, borrowed chords, secondary dominants, harmonic and melodic minor, and per-chord scale choices. It's free to try. I'd love feedback, especially from guitarists and anyone into theory. And if you've built something real with Claude without a dev background, I'd love to hear how you approached it.
