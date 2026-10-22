---
id: "212fb1b641ad01cc"
title: "I built 5 Claude Code skills that make game assets as code: pixel art, vector art, 3D, textures and sound (one scene made with all of them)"
url: "https://reddit.com/r/ClaudeAI/comments/1xc30xk/i_built_5_claude_code_skills_that_make_game"
link: "https://reddit.com/r/ClaudeAI/comments/1xc30xk/i_built_5_claude_code_skills_that_make_game"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T23:37:34Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Informal_Piano9406"]
language: "en"
summary: "I've been building a family of Claude Code skills where Claude makes game assets by writing code: no image model. Each one is a small JavaScript DSL with a live viewer, and Claude checks its own previews and fixes what it sees. The five tools: - pxl: pixel art (my fork of claude-pxl, adding hue-shifted shading, selective outlines and a lint that flags common pixel-art mistakes) - vex: 2D vector…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "models & research"]
content_source: "post"
word_count: 322
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xc30xk/i_built_5_claude_code_skills_that_make_game/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built 5 Claude Code skills that make game assets as code: pixel art, vector art, 3D, textures and sound (one scene made with all of them)

Reddit · Informal_Piano9406 · 2026-10-21

I've been building a family of Claude Code skills where Claude makes game assets by writing code: no image model. Each one is a small JavaScript DSL with a live viewer, and Claude checks its own previews and fixes what it sees. The five tools: - pxl: pixel art (my fork of claude-pxl, adding hue-shifted shading, selective outlines and a lint that flags common pixel-art mistakes) - vex: 2D vector art, with skeletal animation, Spine export, Tiled maps, particle effects and UI kits - kiln: low-poly and voxel 3D, exported as GLB with animation, rendered in Blender - loom: seamless PBR textures (albedo, normal, height, roughness, AO), which kiln models can now use directly - chirp: sound effects and music, synthesized, with seamless loops and audio sprites What's in the images: - The Dragon's Hoard: a 3D vault in kiln where every surface is a loom material. Lava pit, torches, a dragon egg, gold. - LAST CUP: one cyberpunk cafe, a lonely robot drinking coffee in the rain, made three ways (pixel art, vector, 3D) with a chirp soundtrack synced to the animation. The neon buzz cuts out on the exact frames the sign flickers. - A pixel-art eldritch portrait, a forest platformer kit and the texture set. The best part is the feedback loop. Every viewer has an annotate mode: paint on the art, pin notes, hit "send to Claude", then say "check the feedback". Claude gets the exact spot plus what's there. In kiln that's the 3D point and the line of code that built that face; in chirp it's the bar, the beat and which track is loudest. The portrait was directed that way, mark by mark. All MIT: https://github.com/uilianks/pxl https://github.com/uilianks/vex https://github.com/uilianks/kiln https://github.com/uilianks/loom https://github.com/uilianks/chirp Big credit to crsolver for claude-pxl, which started all of this. Every tool shares its architecture: sandboxed source files, errors that point at the line, and a live viewer. Which one should I push further?
