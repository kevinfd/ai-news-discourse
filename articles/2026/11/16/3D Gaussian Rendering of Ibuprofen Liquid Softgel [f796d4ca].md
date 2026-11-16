---
id: "f796d4ca5d754b8b"
title: "3D Gaussian Rendering of Ibuprofen Liquid Softgel"
url: "https://reddit.com/r/ClaudeAI/comments/1xxkcfx/3d_gaussian_rendering_of_ibuprofen_liquid_softgel"
link: "https://reddit.com/r/ClaudeAI/comments/1xxkcfx/3d_gaussian_rendering_of_ibuprofen_liquid_softgel"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T08:39:59Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Lunatic-BrainPower"]
language: "en"
summary: "I built a 3D Gaussian splat of an ibuprofen liquid softgel from 189 turntable photos, using Claude Code (Opus 5.5 on medium). It's free and open source (MIT): my github repo has the raw photos, every script, the exact settings, and an offline viewer (results/final-viewer.html) you can open in a browser. Training and rendering use ooosplat . **How Claude Code helped** I shot the photos and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xxkcfx/3d_gaussian_rendering_of_ibuprofen_liquid_softgel/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 3D Gaussian Rendering of Ibuprofen Liquid Softgel

Reddit · Lunatic-BrainPower · 2026-11-16

I built a 3D Gaussian splat of an ibuprofen liquid softgel from 189 turntable photos, using Claude Code (Opus 5.5 on medium). It's free and open source (MIT): my github repo has the raw photos, every script, the exact settings, and an offline viewer (results/final-viewer.html) you can open in a browser. Training and rendering use ooosplat . **How Claude Code helped** I shot the photos and directed the work. Claude Code wrote the Python pipeline and debugged it with me: * **Camera poses.** The usual route failed: COLMAP registered 2 of 156 frames on my first capture and VGGT's poses were too noisy, because the background never moves on a turntable and a clear capsule has almost no texture. Claude Code wrote a solver that recovers the cameras from the capsule's silhouettes instead (a differentiable voxel renderer in PyTorch) and exports them in COLMAP format for Brush. * **Debugging the solve.** The first run failed every quality gate. The cause was burst mode: once the camera's buffer filled, the shots were no longer evenly spaced. The fix reads each frame's capture time from EXIF, which took silhouette IoU from 0.96–0.98 to 0.99+. * **Keeping the reflection.** SAM 2 and BiRefNet both cut out the capsule but dropped its reflection on the table, so the pipeline keys the cyan glow by colour and keeps two mask sets: capsule only for the solver, capsule plus reflection for training. * **Working across sessions.** Handoff notes in docs/ carried the project between Claude Code sessions (written with the writing-for-agents skill), and I used the grilling skill to stress-test the plan. Result: 151K splats, 26.51 dB PSNR on 24 held-out views.
