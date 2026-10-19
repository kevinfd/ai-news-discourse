---
id: "b38fad49c7c0e70f"
title: "I built a browser city builder with Claude Code: every citizen is simulated, and there's a London demo you can watch for free"
url: "https://reddit.com/r/ClaudeAI/comments/1x9d2ek/i_built_a_browser_city_builder_with_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1x9d2ek/i_built_a_browser_city_builder_with_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T20:10:35Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["ragmondo"]
language: "en"
summary: "I built Civitas, a 3D city builder that runs in the browser, as an experiment. The question was how far Claude Code can take a big game project if I steer it but don't write the code. I picked the features, set the priorities and made the trade-offs. Claude wrote the code, the tests and the tooling. Live demo (free, nothing to install): https://civitas.reneo.app Source:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 520
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9d2ek/i_built_a_browser_city_builder_with_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a browser city builder with Claude Code: every citizen is simulated, and there's a London demo you can watch for free

Reddit · ragmondo · 2026-10-18

I built Civitas, a 3D city builder that runs in the browser, as an experiment. The question was how far Claude Code can take a big game project if I steer it but don't write the code. I picked the features, set the priorities and made the trade-offs. Claude wrote the code, the tests and the tooling. Live demo (free, nothing to install): https://civitas.reneo.app Source: https://github.com/reneodlt/civitas What it is - A multiplayer city builder in three.js and TypeScript, with a Node server. You buy land, lay roads, zone it, and the city grows. - Every citizen is simulated individually: a home, a job, shifts, a household, a car or a bus pass, and a daily commute. Click anyone to see their day, or ride along in first person. - Transport: buses with routes you draw, rail and freight, a metro with an underground view, ferries, planes, helicopters and boats. Tower Bridge lifts on a schedule, and the road barriers come down first. - The public demo is a read-only London, laid out from real coordinates: the main roads, the Thames and its bridges, about 30 real landmarks, the Central, Northern and Jubilee lines, and river buses. About 30,000 citizens are simulated. How Claude was used - One Claude Code session acted as coordinator. It broke each feature into tasks on a kanban board through an MCP server, then handed them to subagents: Opus for simulation and networking, Sonnet for rendering and UI. - Each subagent worked in its own git worktree and ran the project's own checks before handing back: a typecheck, a building-catalogue validator, a demo check that seeds every demo twice and compares hashes, and load tests for tick cost. The coordinator merged their work, re-ran the checks, put the build on a test server for me to play, and deployed when I said so. - My instructions were short ("boats and ports next", "the roads look dreadful", "we've broken zoom"). The useful part was the back-and-forth. For example: - I asked for trackpad support, then said the mouse wheel was broken. Claude found that a browser can't reliably tell a trackpad from a smooth-scrolling mouse. It replaced the guesswork with the standard scheme other builders use, plus one setting. - When Tower Bridge first lifted, cars were still driving on it. I pushed back, and Claude tied the road barriers to the bridge's lift schedule. A test now checks that no vehicle is on a leaf while it lifts. - I asked how Civitas compares to other city builders. Claude wrote a frank audit: the simulation is strong, the game around it is thin. It turned the gaps into cards with acceptance tests, which is what we're working through now. Try it (free) - Watch: open https://civitas.reneo.app . You join London as a visitor and can follow anyone, ride in first person, and take the guided tour. - Play: git clone https://github.com/reneodlt/civitas && cd civitas && npm install && npm run dev, then open http://localhost:5173. That gets you the full game, with building, test cities and a "Play offline" mode. Limits - The public site is read-only.
