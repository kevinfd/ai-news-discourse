---
id: "d40435cdc9d5f792"
title: "Building a Spore-inspired evolution game in Godot 4 with Claude - Some Updates"
url: "https://reddit.com/r/ClaudeAI/comments/1xt6xni/building_a_sporeinspired_evolution_game_in_godot"
link: "https://reddit.com/r/ClaudeAI/comments/1xt6xni/building_a_sporeinspired_evolution_game_in_godot"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T03:11:42Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Ouvolk"]
language: "en"
summary: "Previous r/ClaudeGameDev post & context here Hey everyone, I’m developing Primordium solo in Godot 4 alongside Claude. It’s an evolution and strategy game inspired by Spore : you evolve from a single cell, swim through a reef lagoon, crawl ashore, design your creature in a procedural 3D editor, and lead a tribe. The cell stage is free to download and play on itch.io (links below). When I shared…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 463
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xt6xni/building_a_sporeinspired_evolution_game_in_godot/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Building a Spore-inspired evolution game in Godot 4 with Claude - Some Updates

Reddit · Ouvolk · 2026-11-11

Previous r/ClaudeGameDev post & context here Hey everyone, I’m developing Primordium solo in Godot 4 alongside Claude. It’s an evolution and strategy game inspired by Spore : you evolve from a single cell, swim through a reef lagoon, crawl ashore, design your creature in a procedural 3D editor, and lead a tribe. The cell stage is free to download and play on itch.io (links below). When I shared the initial trailer, I got very helpful feedbacks and updating since. Here is what Claude and I built: How Claude Helped (The Technical Side) Because I'm building this solo, I rely heavily on Claude for systems architecture and procedural math: Procedural IK & Locomotion: Claude helped write the multi-legged inverse kinematics and foot-planting algorithm. It dynamically adapts stride frequency and gait across arbitrary body plans—from 2-legged bipeds to 16-legged millipede crawlers and webbed swimmers. The Aquatic Stage Math: Claude implemented the 3D swimming physics ( SwimLocomotion ), drag, and the transition logic where lobed fins become legs when crawling onto the beach. Tribe Stage Unit Possession: We built a feature allowing the player to swoop down from the RTS strategy camera into any tribe member in third person (WASD/jumping/combat) using metadata task-stashing so unit AI seamlessly resumes when you exit. Automated Headless Test Bots: Claude maintains headless test suites ( --test ) and autoplay bot scripts that run the simulation at high speed to catch regressions and physics bugs. What’s New in the Gameplay The Aquatic Stage: Instead of jumping straight from a cell to land, you swim in a reef lagoon. You hunt, filter plankton, unlock gills, lures, and electric organs, and only walk onto the sand once you've evolved lungs and lobed fins. Parts That Physically Matter: Parts aren't just stat sticks. Webbed feet let you swim into deep water where land predators can't follow; a burrowing snout lets you dig for grubs or bury yourself to hide; stilt legs let you wade through water but make you easier to knock down in combat. World Memory & Reactivity: A living ecosystem. Nearby species remember your actions-prey you overhunted will flee on sight or hold grudges, while befriended species greet you and warn you of predators. Island events like a volcano shake the terrain and force migrations, leaving fertile soil for fruit trees generations later. Third-Person Tribal Possession: Command your village from a bird's-eye view, or press F to drop directly into your Chieftain or any tribe member to fight, fish, harvest, or perform music manually. Links & Feedback Free Demo (Cell Stage for Windows & Mac): https://akinjigames.itch.io/primordium (The later stages shown in the video are currently in active development). If you are interested you can follow on Kickstarter for the launch: https://www.kickstarter.com/projects/primordium/primordium-evolve-your-own-creature-from-a-single-cell What feels good and what would you want to see expanded?
