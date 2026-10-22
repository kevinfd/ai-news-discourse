---
id: "6d5c1c643bcb2fbd"
title: "Exploring Opus 5.5’s potential in real-time VFX"
url: "https://reddit.com/r/ClaudeAI/comments/1xbsxxm/exploring_opus_55s_potential_in_realtime_vfx"
link: "https://reddit.com/r/ClaudeAI/comments/1xbsxxm/exploring_opus_55s_potential_in_realtime_vfx"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T17:06:23Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Excifroge"]
language: "en"
summary: "I’m a VFX artist, and I built these Unity effects with Claude Code (Opus 5.5) over the past two weeks: a fire explosion, a lightning strike and ice spikes. They’re real Shuriken particle systems in Unity, not video. How Claude was used: Build: Claude Code writes Unity editor scripts that create the prefab: particle systems, materials and texture assignments. Review: another script captures…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 241
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbsxxm/exploring_opus_55s_potential_in_realtime_vfx/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Exploring Opus 5.5’s potential in real-time VFX

Reddit · Excifroge · 2026-10-21

I’m a VFX artist, and I built these Unity effects with Claude Code (Opus 5.5) over the past two weeks: a fire explosion, a lightning strike and ice spikes. They’re real Shuriken particle systems in Unity, not video. How Claude was used: Build: Claude Code writes Unity editor scripts that create the prefab: particle systems, materials and texture assignments. Review: another script captures frames with a fixed camera, random seed and timestamps, and tiles them into one sheet. Claude reads the sheet, decides what to change and edits the build script. The early rounds are its own; later rounds follow my notes. Each effect took 10 to 15 rounds. Rules: a skill I wrote from my VFX experience, with production steps and visual guidelines. This made the biggest difference. Textures: Claude writes the prompts, generates them through a Codex worker (codex exec with image gen) and reviews every result. (I wish Claude could generate images itself.) Meshes: for the ice, Claude writes Python for Blender and runs it through Blender MCP: procedural high-poly crystals, decimated, with normal and mask maps baked in Cycles, then exported to Unity. The gallery shows the three effects, then the ice spike’s iteration history, crystal models, textures and Unity setup. Free to try: every material uses VFX Essential, my Unity VFX shader, which I refactored with Claude and released for free (MIT): https://github.com/excifroge/VFX-Essential-Shader Next I might try combat VFX on animated characters. Updates on X: https://x.com/excifroge
