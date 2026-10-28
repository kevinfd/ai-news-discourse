---
id: "087169873a97fffd"
title: "I made an online WW2 dogfight game that runs in the browser with Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1xgw3vd/i_made_an_online_ww2_dogfight_game_that_runs_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xgw3vd/i_made_an_online_ww2_dogfight_game_that_runs_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T15:47:02Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Pretend_Jackfruit173"]
language: "en"
summary: "Hi there, I’ve liked planes since I was a little kid. I played a lot of flight sims, then World of Warplanes and War Thunder. Two things always bothered me: Hundreds of hours of time-consuming grind before you get to fly what you actually want + P2W Or you need a really good PC to play. So I decided to build my own online dogfight game. It’s live here: https://dogfighter.io Simplier graphics for…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 478
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgw3vd/i_made_an_online_ww2_dogfight_game_that_runs_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made an online WW2 dogfight game that runs in the browser with Claude

Reddit · Pretend_Jackfruit173 · 2026-10-27

Hi there, I’ve liked planes since I was a little kid. I played a lot of flight sims, then World of Warplanes and War Thunder. Two things always bothered me: Hundreds of hours of time-consuming grind before you get to fly what you actually want + P2W Or you need a really good PC to play. So I decided to build my own online dogfight game. It’s live here: https://dogfighter.io Simplier graphics for bigger air battles. Physics as close as real life as I can make them on a browser. An escort/interception dynamic that adds some strategic component to the simulator/dogfight gameplay. You can also play with your friends in a squadron, attacking together and protecting each other. It took me approximately two weeks to get to the current version. My background: some experience as a mod dev on games like Minecraft, but no big coding background. What Claude helped me with: Flight physics. This would have been impossible for me alone. It would have taken thousands of tests and hours of historical research for specific data, then compiling that data into something usable. World generation. Maps are generated from a seed, and they’re never exactly the same from one game to the next. Server and online architecture. One authoritative server per match. Your own plane is predicted on your side and corrected by the server, so the game stays responsive without letting a bad connection give anyone an advantage. Coding, testing and checking as a whole. What you still have to do yourself: Game design. Claude can’t think up your game and the way you want it to feel. You need to be somewhat knowledgeable about how games similar to yours work. Same goes for the thinking behind the mechanics. Same as above: letting Claude decide everything for you will result in very generic, basic gameplay. You need to let it know your own vision. Balance and control feel. Claude can measure things and propose numbers, but it does so as an AI, not as a player. You have to play (a lot) and decide. Saying no. Claude will happily build whatever you ask for, and will even want to do more than necessary, which becomes a problem at some point. A game that has too much feels too much ; and at some point it's not enjoyable to play it anymore. You have to keep it small to keep it playable. Managing Claude. You have to check regularly how Claude works, to spot inefficient processes and repeated mistakes. Looking periodically at how sub-agents handle specific tasks gives you what you need to write efficient rules (it also helps a lot with saving tokens). I’d love feedback on the flight feel and the missions (lot of things to improve here). And if you’ve built a game with Claude, I’m curious how you handled game feel and balancing.
