---
id: "46a1994cfe7f6ed4"
title: "My friends said AI can't play fantasy football because it can't watch the games. Claude finished in the top 1% of the World Cup one"
url: "https://reddit.com/r/ClaudeAI/comments/1xthusm/my_friends_said_ai_cant_play_fantasy_football"
link: "https://reddit.com/r/ClaudeAI/comments/1xthusm/my_friends_said_ai_cant_play_fantasy_football"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T13:33:36Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["HistoricalKiwi6139"]
language: "en"
summary: "My friends are huge football fans and we argue a lot. Their line was that AI can't play fantasy football. It can't watch a match, all it has is stats, and stats aren't everything. So last summer I took that as a challenge and played the World Cup fantasy game with Claude, just to prove them wrong. Opened Claude Code and started building a model. Stats in, simulations out, pick the team off the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "jobs & society"]
content_source: "post"
word_count: 468
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xthusm/my_friends_said_ai_cant_play_fantasy_football/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My friends said AI can't play fantasy football because it can't watch the games. Claude finished in the top 1% of the World Cup one

Reddit · HistoricalKiwi6139 · 2026-11-11

My friends are huge football fans and we argue a lot. Their line was that AI can't play fantasy football. It can't watch a match, all it has is stats, and stats aren't everything. So last summer I took that as a challenge and played the World Cup fantasy game with Claude, just to prove them wrong. Opened Claude Code and started building a model. Stats in, simulations out, pick the team off the numbers. It got out of hand. There are 69 scripts in that folder now, including one whose whole job was deciding between Jude and Enzo. Finished in the top 1% (that's the screenshot) and then wrote a postmortem. For a fantasy game. So yes, AI can play fantasy. A lot better than they thought. The one thing they had right is that it can't watch a match. Numbers miss stuff any fan can see. Right now the top scorer in FPL is listed as a defender and he's been playing on the wing for weeks. No stat sheet tells you that, your mate who watches every game does. So I gave Claude the closest thing I could find, heatmaps, where a player actually stood instead of where the team sheet put him. After that it sounded less like a spreadsheet and more like one of them. I got into football somewhere in there too, which nobody saw coming. Kept going when the club season started and it's turned into a real thing called Prevedo. It's an MCP server you plug into Claude, plus a site. Claude's the brain, Prevedo is the maths underneath: it runs the numbers and Claude works out what to do with them. You paste your team and ask who to captain or what to do with your one free transfer. All built with Claude Code. Two rules matter most. It'll happily compare two players and forget your budget and the other 13, so one tool rebuilds the whole squad and hands back a plan. And it always wants an opinion, so if two moves are within 2 points over six weeks it just says that's a tie, hold. Site's free, no account. There's a team check that plays your squad 10,000 times, also free, and a few free questions to the assistant. Having it inside your own Claude is the paid bit, £2.99 a month for the first 100 people then £4.99. https://prevedo.app Claude's picking my Premier League team this season too. Top 2% overall, third in our league, 20 points behind two of them. So, almost. That gap's on me tho, not Claude. For the first five gameweeks I was still learning how to do this and the tools doing the projections were full of bugs. If I'd built it right from day one I reckon it'd be higher.
