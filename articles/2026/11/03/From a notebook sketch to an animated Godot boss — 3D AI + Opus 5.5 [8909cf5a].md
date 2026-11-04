---
id: "8909cf5a0123ccf3"
title: "From a notebook sketch to an animated Godot boss — 3D AI + Opus 5.5"
url: "https://reddit.com/r/ClaudeAI/comments/1xn7jti/from_a_notebook_sketch_to_an_animated_godot_boss"
link: "https://reddit.com/r/ClaudeAI/comments/1xn7jti/from_a_notebook_sketch_to_an_animated_godot_boss"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T22:40:11Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Delicious-Shower8401"]
language: "en"
summary: "After my first post about After the Wind , I stayed in touch with the developer and asked how he makes his characters. He shared the process behind this penguin boss, from two notebook sketches to a rigged character with 22 animations . The stack Claude Opus 5.5 + Blender — rigging, weight painting and animation. Tripo P2 — 3D model generation and texturing. Godot — gameplay integration and the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 340
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn7jti/from_a_notebook_sketch_to_an_animated_godot_boss/"
score: null
comments: null
community: "r/ClaudeAI"
---

# From a notebook sketch to an animated Godot boss — 3D AI + Opus 5.5

Reddit · Delicious-Shower8401 · 2026-11-03

After my first post about After the Wind , I stayed in touch with the developer and asked how he makes his characters. He shared the process behind this penguin boss, from two notebook sketches to a rigged character with 22 animations . The stack Claude Opus 5.5 + Blender — rigging, weight painting and animation. Tripo P2 — 3D model generation and texturing. Godot — gameplay integration and the jiggle shader. 1. Sketches and references The character started as two pencil doodles. He explored body shapes and tested the wings folded against the belly and extended during an attack, then prepared front and side references for 3D. 2. Model and textures He generated four options at a time in Tripo P2. The first 5k quad mesh didn’t work well for this creature, so he switched to 25k triangles and textured that mesh directly in Tripo. 3. Rigging with Opus 5.5 Working with Claude in Blender, he built a rig with 58 bones , including one for each flight feather, 12 per wing . The feathers can fan out during attacks and fold against the belly. The belly has its own bone so it follows the body a beat later. 4. Animation with Opus 5.5 His role was to describe the weight, feel and purpose of each movement, then give feedback. For the wing slash, he wanted the swing to start at the hips, using the longer feathers to extend the attack’s reach. For the recovery after a belly slide, he used footage of a real gentoo penguin pushing off the ice with its flippers and getting its feet underneath it. The boss now has 22 animations , including waddling, sliding, throwing a tantrum and napping on his feet so you can sneak up and poke him. 5. Movement in Godot A jiggle shader uses a softness map baked from the rig weights. The wings and feathers stay firm while the belly, chest and cheeks wobble. When he pushes himself up, his belly squishes against the ground under his weight.
