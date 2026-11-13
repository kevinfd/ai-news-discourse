---
id: "07a330d96dcab8f2"
title: "I built a 6-axis browser synth for my old 3Dconnexion SpaceNavigator with Claude Code (free, open source, and works with mouse)"
url: "https://reddit.com/r/ClaudeAI/comments/1xv5mv1/i_built_a_6axis_browser_synth_for_my_old"
link: "https://reddit.com/r/ClaudeAI/comments/1xv5mv1/i_built_a_6axis_browser_synth_for_my_old"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T11:39:25Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["BloodSteyn"]
language: "en"
summary: "I built AETHER·6, an ambient synth that runs in the browser and is played with a 3Dconnexion SpaceNavigator, the 3D mouse normally used for CAD. Mine is an old \"for Notebooks\" model that's out of active support, and I wanted a more fun use for it. FYI, it works with Mouse input too . What it does The browser reads the puck directly over WebHID, and all six axes control the sound: Push down to…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 348
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xv5mv1/i_built_a_6axis_browser_synth_for_my_old/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a 6-axis browser synth for my old 3Dconnexion SpaceNavigator with Claude Code (free, open source, and works with mouse)

Reddit · BloodSteyn · 2026-11-13

I built AETHER·6, an ambient synth that runs in the browser and is played with a 3Dconnexion SpaceNavigator, the 3D mouse normally used for CAD. Mine is an old "for Notebooks" model that's out of active support, and I wanted a more fun use for it. FYI, it works with Mouse input too . What it does The browser reads the puck directly over WebHID, and all six axes control the sound: Push down to play, slide left/right for pitch (snapped to a key and scale) Slide forward/back for brightness Tilt for octave shimmer, sub bass and stereo pan Twist for pitch bend Pull up for random "sparkle" notes It also has a 16-step drum and bass sequencer, a MIDI file import that detects the song's key and tempo so you can play over it in tune, and a three.js visualiser that reacts to the audio and follows the puck. How Claude Code helped I built it with Claude Code in a single session. I started by asking what else I could do with the device, picked the synth idea, and described what I wanted: a three.js instrument with drums, bass, MIDI import and a visualiser. Claude Code Fable 5.2 wrote the whole thing as one HTML file (WebHID input, Web Audio synth, sequencer, MIDI parser, shaders), tested it in a browser with simulated input, and fixed the visuals when the first version was washed out. It also wrote the README, recorded the demo video with a scripted performance, and set up the GitHub repo and hosting. My part was the idea, steering it, and testing with the real hardware, which worked on the first try. Free to try It's completely free and MIT licensed, with no account or install: Play it here: https://bloodsteyn.github.io/aether-6/ Source and demo video: https://github.com/BloodSteyn/aether-6 Use Chrome or Edge, since WebHID isn't in other browsers. Click Start, then Connect SpaceNavigator. If you don't have a 3D mouse, you can play it by clicking and dragging. I'd like to hear from anyone with a newer SpaceMouse about whether it connects and the axes feel right.
