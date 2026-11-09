---
id: "86e5193269dc8217"
title: "Can coding agents build interactive 3D worlds? Frontier3DBench evaluates 11 configurations across objects, scenes, and worlds [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xrhg3a/can_coding_agents_build_interactive_3d_worlds"
link: "https://reddit.com/r/MachineLearning/comments/1xrhg3a/can_coding_agents_build_interactive_3d_worlds"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T03:41:21Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["OliviaYii"]
language: "en"
summary: "Can the same coding agent build a detailed 3D object, assemble a scene, and make an interactive world actually work? Our team at Einsia released Frontier3DBench to test that progression: 145 tasks across 9 categories, with 11 model–harness configurations producing editable Blender projects and runnable Unreal Engine worlds. Evaluation covers appearance, structure, and behavior through rendered…"
tags: ["r/MachineLearning"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 151
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xrhg3a/can_coding_agents_build_interactive_3d_worlds/"
score: null
comments: null
community: "r/MachineLearning"
---

# Can coding agents build interactive 3D worlds? Frontier3DBench evaluates 11 configurations across objects, scenes, and worlds [R]

Reddit · OliviaYii · 2026-11-09

Can the same coding agent build a detailed 3D object, assemble a scene, and make an interactive world actually work? Our team at Einsia released Frontier3DBench to test that progression: 145 tasks across 9 categories, with 11 model–harness configurations producing editable Blender projects and runnable Unreal Engine worlds. Evaluation covers appearance, structure, and behavior through rendered views, scene inspection, and runtime tests. A few results: GPT-6.1-sol leads overall and on objects and scenes, while GPT-6-astra leads interactive worlds. MiniMax-M3.1-Flash ranks sixth overall but second on scene editing. Every configuration scores lower on reference-based reconstruction than text-driven generation in both object and scene tasks. Across 165 world submissions, local mechanisms score much higher than stateful workflows: 83.08 vs. 30.26 out of 100. The interesting question is how well an agent’s strengths carry over from individual assets to environments with coordinated interactions and persistent state. Project and examples: https://lab.einsia.ai/frontier3dbench Paper: https://lab.einsia.ai/frontier3dbench/Frontier3DBench.pdf GitHub: https://github.com/Einsia/Frontier3D
