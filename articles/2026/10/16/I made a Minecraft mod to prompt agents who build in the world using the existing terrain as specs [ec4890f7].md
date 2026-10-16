---
id: "ec4890f76ad5ed9a"
title: "I made a Minecraft mod to prompt agents who build in the world using the existing terrain as specs"
url: "https://reddit.com/r/ClaudeAI/comments/1x76saz/i_made_a_minecraft_mod_to_prompt_agents_who_build"
link: "https://reddit.com/r/ClaudeAI/comments/1x76saz/i_made_a_minecraft_mod_to_prompt_agents_who_build"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T04:28:37Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Acclynn"]
language: "en"
summary: "This mod is basically WorldEdit but with AI : First off you select your region (by picking two corners or just by looking where you want your structure to be), then you prompt in a chat command. That prompt is sent to the agent along with the selected region, and the agent work in the background then deliver its result and you get a reconstitution of what it did. You can even use books in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 284
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x76saz/i_made_a_minecraft_mod_to_prompt_agents_who_build/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Minecraft mod to prompt agents who build in the world using the existing terrain as specs

Reddit · Acclynn · 2026-10-16

This mod is basically WorldEdit but with AI : First off you select your region (by picking two corners or just by looking where you want your structure to be), then you prompt in a chat command. That prompt is sent to the agent along with the selected region, and the agent work in the background then deliver its result and you get a reconstitution of what it did. You can even use books in lecterns to give additional spatial context. Opus 5.5 is incredibly good at following precise instructions while also bringing its own creativity, so I think it can be more than just something to toy with and may be an actual reliable tool for builders who want to complete side-stuff. The way it works is that the mod is calling a separate program running on the system (called the "core") which handles connecting to your Claude or Codex CLI, you even have a nice UI to configure everything from it (what AI provider, what model, effort etc). The mod is purely server-side, so you can even toy with it in multiplayer and your friends don't need to install anything as long as the host has it. Vibe-coded with GPT-6 Astra at the beginning, then I pivoted to Claude Opus 5.5 which did much better, I still took some decisions for the overall architecture and API tho. I also care about having something clean, shareable and that doesn't feel janky. The design and ideas are from me. Despite having to install two things to install to make it work (the Core program and the mod itself) I hope it's easy enough to pick up. Fully open-source and forkable: https://github.com/Ni-Cobra/worldprompt Longer showcase video:
