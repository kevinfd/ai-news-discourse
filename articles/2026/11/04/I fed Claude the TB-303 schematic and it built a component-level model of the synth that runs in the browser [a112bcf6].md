---
id: "a112bcf64a27c1b1"
title: "I fed Claude the TB-303 schematic and it built a component-level model of the synth that runs in the browser (early taster)"
url: "https://reddit.com/r/ClaudeAI/comments/1xnk5zf/i_fed_claude_the_tb303_schematic_and_it_built_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xnk5zf/i_fed_claude_the_tb303_schematic_and_it_built_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T09:45:53Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["SnuGnu"]
language: "en"
summary: "I've been playing with an idea: instead of asking Claude to \"make something that sounds like a 303\", give it the actual electronics and have it model the circuit. 🎥 Demo: https://www.youtube.com/watch?v=lbUobvWWS9k What I fed it • The Roland TB-303 service manual schematics (oscillator, VCF, envelopes, VCA, accent circuit) • Component values: resistors, capacitors, transistor and diode behaviour…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "search & media"]
content_source: "post"
word_count: 472
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnk5zf/i_fed_claude_the_tb303_schematic_and_it_built_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I fed Claude the TB-303 schematic and it built a component-level model of the synth that runs in the browser (early taster)

Reddit · SnuGnu · 2026-11-04

I've been playing with an idea: instead of asking Claude to "make something that sounds like a 303", give it the actual electronics and have it model the circuit. 🎥 Demo: https://www.youtube.com/watch?v=lbUobvWWS9k What I fed it • The Roland TB-303 service manual schematics (oscillator, VCF, envelopes, VCA, accent circuit) • Component values: resistors, capacitors, transistor and diode behaviour • Details of TD-3-MO features I wanted, like its filter keyboard-tracking knob What it did with them Rather than generic DSP blocks, each stage is built from the parts on the schematic. The filter cutoff comes from the actual resistor network, the accent comes from the real cap and resistor values, and so on. Every part value is exposed, so you can swap a capacitor and hear what changes. When I asked for new features like key tracking, it worked out where they'd sit in the circuit, like a new pot and resistor feeding the cutoff node, instead of bolting on an effect. It then added a RAT distortion (also modelled from its schematic), delay, a compactor and four reverbs, including convolution with real EMT 140 plate recordings. There's a 64-step sequencer too, and a C++ port running as a VST3/AU plug-in that's checked sample for sample against the web version. How I worked Almost all of it was Claude Code, often several threads at once (one on the sound engine, one on the UI, one on the plug-in), with me listening, poking at it and giving notes like "low notes should get darker" or "I don't like the Lexicon". It merges and deploys to Cloudflare on its own, so I just refresh and play. Lots of listening tests This wasn't one-shot. We went through rounds and rounds of sound tests and comparisons. I don't own a real 303, so the references were my TD-3 and classic tracks that use one. We rendered the same pattern through different versions of the engine, A/B-ed them against those, and tweaked part values until the squelch, the accent punch and the slides felt right. Claude would render audio and I'd listen and report back ("too bright", "the accent isn't snapping"). It would trace that back to a stage of the circuit and adjust it. When a change sounded worse, we kept the old engine and parked the new one on a branch. What I learned • Schematics are a fantastic spec. They're unambiguous in a way a prose description of a sound never is. • Ears are still the final test. A couple of "more accurate" schematic changes sounded worse, so we reverted them. • Keeping the JS and C++ engines in sync with an automated parity test saved a lot of pain. ⚠️ It's an early taster and a work in progress, so things will change. Try it: https://tb303-circuit-model.pages.dev Happy to answer questions about the workflow.
