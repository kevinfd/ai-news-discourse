---
id: "5b86f8f625a5ed48"
title: "Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself."
url: "https://reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it"
link: "https://reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T02:25:56Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons…"
tags: ["r/artificial"]
orgs: ["Microsoft", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 148
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xy8mj7/microsoft_tested_a_codingagent_memory_plugin_it/"
score: null
comments: null
community: "r/artificial"
---

# Microsoft tested a coding-agent memory plugin. It cost more at first, then paid for itself.

Reddit · shoumikgoswami · 2026-11-17

In a Microsoft Research and UC Berkeley experiment, Claude Code worked through tasks from the same repos in sequence. After five completed tasks in a repo, 30% of its tool calls repeated actions from earlier tasks there. Repeated doesn't automatically mean unnecessary, but it gave the researchers something to investigate. They built TokenEconomizer, an open-source plugin that carries lessons between sessions, trims the available tools and nudges the agent when it gets stuck. The catch: learning the repo initially added cost. In their tests, cumulative spending fell below the unmodified agent by the sixth task in every repo. Across five agent-model combinations, mean cost per task fell 18.4-30.9%, including the plugin's own model calls. Task success improved in four of the five. I'd be interested in trying this on a repo I work in regularly. A one-off task wouldn't tell you whether the memory is earning its keep.
