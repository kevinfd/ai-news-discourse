---
id: "da8c0f5a50456c53"
title: "I'm a PM and I've started mocking up my own ideas in Figma with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1x4rj6m/im_a_pm_and_ive_started_mocking_up_my_own_ideas"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T08:53:52Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["ashadis"]
language: "en"
summary: "Alot of my job is \"can you show me what that would look like?\" Our designers are swamped with roadmap work (fair enough), and I didn't want to keep adding my half-baked ideas to their queue. We already have a design system and I have access to our repos, so I figured Claude could just use them. I tried Claude Design first, but it was slow, and moving each version over to Figma held up every…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society", "agents & coding"]
content_source: "post"
word_count: 192
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4rj6m/im_a_pm_and_ive_started_mocking_up_my_own_ideas/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I'm a PM and I've started mocking up my own ideas in Figma with Claude Code

Reddit · ashadis · 2026-10-13

Alot of my job is "can you show me what that would look like?" Our designers are swamped with roadmap work (fair enough), and I didn't want to keep adding my half-baked ideas to their queue. We already have a design system and I have access to our repos, so I figured Claude could just use them. I tried Claude Design first, but it was slow, and moving each version over to Figma held up every round of changes. The Figma MCP was painfully slow too. So a couple of weeks back I hacked together Figment, a ClaudeCode skill plus a small Figma plugin. Claude writes the screens as code using our design system. A quick check catches anything that would look broken, like text spilling out of a button, before it ever reaches Figma. Then one click builds a real Figma file you can edit. Most of the PMs at my company use it now, and it's been working really well. When an idea sticks, our designers get a proper file to work from instead of a screenshot. It's free and open source if anyone wants to poke at it: https://github.com/Ashad001/figment
