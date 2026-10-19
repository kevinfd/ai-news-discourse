---
id: "4401f9753df742fc"
title: "A Super Mario 64 demake for the GBA built with Claude. Mario’s physics are bit-identical to the original"
url: "https://reddit.com/r/ClaudeAI/comments/1x99sel/a_super_mario_64_demake_for_the_gba_built_with"
link: "https://reddit.com/r/ClaudeAI/comments/1x99sel/a_super_mario_64_demake_for_the_gba_built_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T18:00:42Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Nervous_Cold8493"]
language: "en"
summary: "I built this with Claude as an experiment: how far can an LLM take a demake if I steer it but don’t write the code? I chose the project, the direction and the trade-offs. Claude wrote the code, the tests and the tooling. Repo: https://github.com/Kodoque1/sm64-gba (MIT, free) What it is SM64’s movement and collision code running under GBA constraints: a 16.8 MHz ARM7 with no FPU. A playable demo:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 287
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x99sel/a_super_mario_64_demake_for_the_gba_built_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# A Super Mario 64 demake for the GBA built with Claude. Mario’s physics are bit-identical to the original

Reddit · Nervous_Cold8493 · 2026-10-18

I built this with Claude as an experiment: how far can an LLM take a demake if I steer it but don’t write the code? I chose the project, the direction and the trade-offs. Claude wrote the code, the tests and the tooling. Repo: https://github.com/Kodoque1/sm64-gba (MIT, free) What it is SM64’s movement and collision code running under GBA constraints: a 16.8 MHz ARM7 with no FPU. A playable demo: 4 levels, software 3D, Mario animated with the game’s own animation data. An optional libsm64-style import: it reads your ROM to build in Mario’s real model and the real level meshes. The repo contains nothing from Nintendo. How Claude was used My instructions were short (“bit-exact first”, “now optimize”, “make a fluid demo, degrade gracefully”). Claude worked in an agentic session with a toolchain and a headless emulator, profiling, rewriting and checking on its own. The design discussions were the best part. When I asked whether an animated Mario was possible, Claude declined to draw Mario’s likeness but built a wooden mannequin posed by the real animations. I suggested one sprite per body part; it proposed ellipsoids, because an ellipsoid’s outline is always an ellipse, which is exactly what GBA affine sprites can draw. When I suggested a sprite atlas, it explained why that can’t work and proposed rendering the real low-poly mesh, taken from my own ROM. Try it (free) make fetch && make demo builds a ROM that runs in mGBA (mannequin version). With your own ROM: make import ROM=sm64.z64 && make demo make demo-check re-checks the physics. No ROM is distributed. Limits Tested in mGBA only, not on real hardware. 30 fps on 98% of frames. No enemies or objects, flat colors instead of textures.
