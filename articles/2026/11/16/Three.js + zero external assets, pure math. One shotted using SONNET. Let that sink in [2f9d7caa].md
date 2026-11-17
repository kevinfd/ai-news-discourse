---
id: "2f9d7caafa51a71b"
title: "Three.js + zero external assets, pure math. One shotted using SONNET. Let that sink in"
url: "https://reddit.com/r/singularity/comments/1xy0d9p/threejs_zero_external_assets_pure_math_one"
link: "https://reddit.com/r/singularity/comments/1xy0d9p/threejs_zero_external_assets_pure_math_one"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T20:31:43Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["OnyxMonolith"]
language: "en"
summary: "I wanted to try the thing that everyone is doing with Claude :) Not Fable, not Opus, SONNET. fully open-source: https://github.com/DeadInternetStudios/three-js-claude-splatting-demo try it live: https://deadinternetstudios.github.io/three-js-claude-splatting-demo/ -- warning! it can crash your browser if you have a weak GPU. some interesting tech about the demo: Three.js + Spark 2.4 (Gaussian…"
tags: ["r/singularity"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 630
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xy0d9p/threejs_zero_external_assets_pure_math_one/"
score: null
comments: null
community: "r/singularity"
---

# Three.js + zero external assets, pure math. One shotted using SONNET. Let that sink in

Reddit · OnyxMonolith · 2026-11-16

I wanted to try the thing that everyone is doing with Claude :) Not Fable, not Opus, SONNET. fully open-source: https://github.com/DeadInternetStudios/three-js-claude-splatting-demo try it live: https://deadinternetstudios.github.io/three-js-claude-splatting-demo/ -- warning! it can crash your browser if you have a weak GPU. some interesting tech about the demo: Three.js + Spark 2.4 (Gaussian splatting renderer, WebAssembly depth sort in a worker) Zero assets. Every splat is generated on the GPU per frame from a seed, a clock and the camera. No models, textures, HDRIs, fonts or audio files Custom GLSL everywhere: one fused shader per layer turns a splat index into a lit surface element (2.7M slots, ~1M drawn) Foldable world with correct math: planet, corkscrew, hinge and ripple deformations carry each splat's covariance through the Jacobian, \(\Sigma' = J \Sigma J^T\) , checked against a double-precision CPU reference CPU twin of the terrain in TypeScript, bit-compared against the GPU height field at 4,000 random points, so walking, flying and camera all stand on exactly what is drawn Five procedural realms (paper dunes, glass forest, breathable sea, mirror flats, ember canyons) with their own terrain, sky shader, weather and generative Web Audio score Real planar reflections in the Mirror Flats from upside-down copies of the tall splat layers, generated only while water is in view Texture-cached cell fields so shared ground and flora values are computed once per cell, not once per splat View culling inside the generator: off-screen splats decline before lighting, keeping their sort slot so the picture never tears Cinematic post in HDR: dual-filter bloom with halation, filmic grade, sun shafts, lens flare, depth of field Deterministic everything: same seed, same world; share links encode seed and position Ships as one 1.83 MB HTML file that runs from file:// , with Spark's Wasm inlined gzipped prompt was: Build a three.js tech demo that does one thing: makes people stop scrolling. Codename "Reality Origami". Frame rate does not matter. Being impressive does. Rules - No external assets. No models, textures, HDRIs, fonts or audio files. The world, the sky, the creatures and the music are all generated at run time. - Use three.js and Spark (Gaussian splats). Generate millions of splats on the GPU every frame from a seed, a clock and the camera, with Spark's SplatGenerator. Upload nothing per frame. - The page shows no text while the player travels. The world - An endless world that looks like folded paper, glass and light. - Five realms with their own terrain, palette, sky, light, plants, creatures and music, blended where they meet: sand dunes, a glass forest, a deep sea you can breathe, a mirror salt flat, ember canyons. - Giant landmarks to walk toward: arches, gates, rib cages, spires, stone circles, floating isles, the odd paper crane the size of a stadium and, in the Dunes, the Flats and the Deep, a paper boat. Whales, mantas, jellyfish, flocks of paper cranes. - The same seed always gives the same world, and a link can share a place. The trick - Let the player fold the world: roll the ground into a small planet, twist it, bend it over their head, send a ripple through it. Every splat must keep its shape through the fold, so carry its covariance through the deformation's Jacobian. - Put the walker and camera on the exact ground the shaders draw. Sound - A procedural Web Audio score. A drone, a melody and footsteps for each realm. The wind opens as the player speeds up. Engineering - TypeScript, Vite, unit tests. A static build that works on GitHub Pages and as a single HTML file. Measure before you claim anything, and write down what you did not check. + my skill for iterating several times to improve quality and test Sonnet 5.5 extra-high 300k capped context.
