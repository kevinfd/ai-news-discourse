---
id: "865643480fce5848"
title: "Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens"
url: "https://tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens"
link: "https://tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-claims-four-gemini-4-agents-beat-minecraft-in-27-hours-by-writing-2-783-programs-of-their-own-the-ai-team-died-605-times-on-easy-difficulty-and-ran-up-an-estimated-usd520-in-tokens"
source: "Tom's Hardware"
domain: "tomshardware.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T12:18:10Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["ControlCAD"]
language: "en"
summary: "Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens\nAbout half the run was spent fighting the dragon, solved by stacking dirt to reach its crystals.\nThe game of Minecraft is no match for a team of four Gemini 4 Argon agents, as they were able to defeat it in 27…"
tags: ["r/artificial"]
orgs: ["Google", "OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research", "search & media", "business & funding"]
content_source: "fulltext"
word_count: 1094
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xaqlya/google_deepmind_says_four_ai_agents_beat/"
score: null
comments: null
community: "r/artificial"
---

# Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens

Tom's Hardware · ControlCAD · 2026-10-20

Google DeepMind says four AI agents beat Minecraft in 27 hours by writing 2,783 programs of their own — AI team died 605 times on Easy difficulty and ran up an estimated $520 in tokens
About half the run was spent fighting the dragon, solved by stacking dirt to reach its crystals.
The game of Minecraft is no match for a team of four Gemini 4 Argon agents, as they were able to defeat it in 27 hours with 2,783 self-written programs, a paper from Google DeepMind reveals. The agents did die 605 times, even on Easy, and about half the run was spent fighting the Ender Dragon, the final boss of the game. The run finally came to completion when the End was solved by stacking dirt to reach the boss’s crystals, at an estimated cost of around $520 in tokens.
The experimental run was designed from the get-go with one goal: kill the Ender Dragon. The playthrough involved a random, shared survival world on Easy with four agents — a fifth agent existed only for reporting — from Gemini 4 Argon, Google’s latest frontier model. Each agent had its own player through the open-source Mineflayer JavaScript library for Minecraft bots, but they were able to coordinate through in-game chat and shared notes. Every program used in the run was written by the agents themselves, and the emphasis is on coding and teamwork rather than game-playing.
The authors say this is the “first end-to-end autonomous completion of Minecraft by AI agents,” at least “to our knowledge,” qualified by the use of Mineflayer “without pre-scouted seeds or other game-specific tools written by humans.” Mineflayer tells the agents where blocks and creatures are, with a pathfinding plugin to plan routes. There was “no human input during the run” and “no one assigned roles or wrote game logic.” The run, starting with the first program and ending with the dragon's death, took 27 hours and 14 minutes.
Although the agents were not given roles, within about 10 minutes a division of labor was proposed in chat by bot janesick. Bot Auratian offered an alternative plan while Bot Gyldenia acknowledged it. The roles ended up being: Gyldenia for food, beds, and flint; Bulicame for diamonds; Janesick for iron and tools; Auratian for the Nether portal. Moments of losses, such as a Ghast fireball destroying dropped items, led the team to diagnose the cause and write rules to prevent it in the future.
Finding the stronghold involved janesick, who threw two Eyes of Ender from different spots and sampled each eye’s flight once every 50 ms, triangulating the location. Carrying the eyes involved its own dire moment when Auratian drowned during the task, but the spot was noted, and the eyes were rescued.
The eventual fight with the dragon led to 69 deaths, and the ten crystals kept regenerating the boss until Auratian discovered they could use dirt pillars to reach the crystals. Four hours and 40 minutes later, all ten crystals were downed, and the dragon was dead 39 minutes after that.
The agents operated by writing short JavaScript programs, almost 2,800 in total, with 42 helper functions kept alive between programs, while a Mineflayer bot ran them in the shared world. Text was returned with status data, not pictures. This is a shared approach to the non-screenshot GPT-6 Astra clear of the Orc starting zone in World of Warcraft earlier this month. AI agents playing games is an ongoing trend, with Pokémon Red probably being the most popular, a game defeated in multiple ways, including with a Jev decision model layer.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
Minecraft has also been a popular target, and the authors admit this, highlighting two earlier community dragon kills: a planner with an action-selection model on a fixed speedrun seed in Peaceful mode, and a single Claude Opus 5 agent that used 37 ready-made, high-level tools on Normal, versus Mineflayer alone for the Gemini team. AI Bengineering’s Claude run, relying mostly on Opus 5 at high effort, took 3 hours and 56 minutes from start — “no human input after the prompt” — to kill with 388 tool calls and only one death. The cost in that case, at API-equivalent rates, was about $93.
Google’s Minecraft run, using Gemini 4 Argon’s 50% introductory pricing, which runs from initial API access that followed the model announcement through Nov. 30, cost more than half a grand; at normal pricing, that’s more than a grand. A GPT-6 Astra Portal run last month, which took about 24 hours, came in at $571 in tokens.
Google’s run took about 1.35 billion input tokens with 91% served from cache. About 24,000 model calls involved around 16 million output tokens, a quarter of them thinking. In total, if we’re also including the observer agent, the session would be estimated at $810, or $1,620 after the promotion, at list prices.
Each player is driven by a “general-purpose Gemini 4 Argon coding agent,” which is a fancy way of saying that it’s not specialized for Minecraft. Gemini 4 Argon itself is a frontier model for “real-world software engineering, enterprise knowledge work like legal and finance, and cybersecurity defense,” according to a company blog. With Minecraft, 22% of the agents’ programs ended in an error, with more than 600 deaths.
Although the model was used for a game here, the run was designed to show that Argon is capable of “complex, long-horizon workflows” for complex real-world tasks and agent coordination. Such long projects can involve decompiling a game back into source code, as we covered recently with a Modern Warfare 2 rebuild that now has 83% of its functions matching the original byte for byte.
Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.
Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
- PEnns Now, that's an amazing scientific achievement...../s
" by writing 2,783 programs of their own "
How come the game's anti cheat system didn't notice all that cheating?? People don't treat in Minecraft? I never played that game so maybe there is no anti-cheat overlord?? Reply
- AnInternetUser This reply is to the first one, because for some reason this site won't allow me to quote-reply: Offline single-player modes don't have anticheat. The game is also known for its modding community too, as is GTA V. I'll even throw in Black Ops 3 Zombies in that group too.Reply
