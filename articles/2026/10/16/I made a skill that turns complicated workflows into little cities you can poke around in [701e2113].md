---
id: "701e21139b86ce0c"
title: "I made a skill that turns complicated workflows into little cities you can poke around in"
url: "https://reddit.com/r/ClaudeAI/comments/1x7v49y/i_made_a_skill_that_turns_complicated_workflows"
link: "https://reddit.com/r/ClaudeAI/comments/1x7v49y/i_made_a_skill_that_turns_complicated_workflows"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T23:20:34Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Bamberg"]
language: "en"
summary: "I've been working on CityVisualizer, because apparently my response to a complicated process is “this needs buildings and tiny people.” It’s a skill that turns descriptions of services, workflows and technical systems into interactive isometric maps. You can follow animated journeys, click into locations and explore what happens inside them. Now you can watch the handoffs and see where things…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 248
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7v49y/i_made_a_skill_that_turns_complicated_workflows/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a skill that turns complicated workflows into little cities you can poke around in

Reddit · Bamberg · 2026-10-16

I've been working on CityVisualizer, because apparently my response to a complicated process is “this needs buildings and tiny people.” It’s a skill that turns descriptions of services, workflows and technical systems into interactive isometric maps. You can follow animated journeys, click into locations and explore what happens inside them. Now you can watch the handoffs and see where things get stuck. I think this breaks down ideas and complicated stuff and makes it appear a lot easier. It supports cities, parks, buildings and technical systems. You can also prompt it to increase the things it supports. The output is a standalone HTML file that works offline, so you can share it without accidentally acquiring a hosting side quest. Credit where it’s due: it builds on the MIT-licensed geometry core from Ryan’s Anatomy skill , with my own map layouts, visual styles and interactive storytelling around it. It’s also inspired by Bo Meyer’s work in visual modelling. GitHub repo, examples and setup instructions I used Claude to help write the skill instructions and map code, then worked through example maps with it to refine the visuals and interactions. I steered what each map should explain; Claude helped turn that into something clickable. There was a fair amount of “yes, but can we make what’s happening here actually understandable?” Curious what people would use this for and whether it makes a messy process easier to understand, or just gives the mess better urban planning. Hope you find it interesting!
