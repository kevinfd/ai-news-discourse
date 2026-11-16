---
id: "31e471c6af5c5ba4"
title: "I built Replicator (3d workshop) with Fable 5.2 and Claude Opus 5.5"
url: "https://reddit.com/r/ClaudeAI/comments/1xx8mec/i_built_replicator_3d_workshop_with_fable_52_and"
link: "https://reddit.com/r/ClaudeAI/comments/1xx8mec/i_built_replicator_3d_workshop_with_fable_52_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T22:25:13Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Distinct-Pie2389"]
language: "en"
summary: "I built Replicator, your local first 3d workshop and research center with Fable 5.2 as the planner (1 prompt on what I wanted - detailed meta prompt from Astra) then I switched from plan to Opus 5.5 and let it rip with subagents. Built over the last week, testing and still doing more! You specify it, you build it. Describe a thing in a sentence: a house with a floor plan, a circuit board, a desk…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 384
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx8mec/i_built_replicator_3d_workshop_with_fable_52_and/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built Replicator (3d workshop) with Fable 5.2 and Claude Opus 5.5

Reddit · Distinct-Pie2389 · 2026-11-15

I built Replicator, your local first 3d workshop and research center with Fable 5.2 as the planner (1 prompt on what I wanted - detailed meta prompt from Astra) then I switched from plan to Opus 5.5 and let it rip with subagents. Built over the last week, testing and still doing more! You specify it, you build it. Describe a thing in a sentence: a house with a floor plan, a circuit board, a desk lamp, a rocket engine, a liquid-cooled PC, a concept nobody has built yet. A language model plans it from engineering knowledge and writes a build program. A solid-modelling kernel builds that program one step at a time, and thirteen measured checks test the result. You can stop at any step, change it, take it apart, measure it, draw it, and send it to CAD, a renderer, Blender or a printer. Replicator is an engineer's workshop first and a research tool second. The design is a validated program, not a picture or generated code, so every part has a size, a material and a mass. Reverse mode works the other way: it takes an existing model apart into pieces, with an evidence ledger that says what was measured, what was inferred and what nobody can tell. It is built for all kinds of work, and most of it needs neither a model nor a printer: You want to Replicator gives you **Design a building** Walls, openings and a roof from one sentence; a floor plan and elevations on the drawing sheet; checks that the roof covers the walls **Lay out electronics** Boards and parts at real scale from knowledge cards, ready for an enclosure **Engineer a machine** Formula-driven ops (a Rao bell nozzle, involute gears, NACA wings), mass, centre of gravity, STEP for CAD **Simulate it** URDF and MJCF with mass, centre and inertia measured from the exact solid, ready for MuJoCo or ROS **Understand an object** Import any of 24 formats and take it apart in Reverse; Explain writes a checked explanation, Present narrates it **Make a replica** Scale and orient to fit any printer bed, refused rather than clipped when it does not fit **Train or test a model** A seeded benchmark scored by measuring the solid, and a corpus export where every row re-verifies REPO: https://github.com/T-Crypt/replicator
