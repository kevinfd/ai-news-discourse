---
id: "dae75617acd590fe"
title: "I built a Claude skill that turns an arcade ROM you own into a 3D browser remaster, with the original game code still running underneath"
url: "https://reddit.com/r/ClaudeAI/comments/1x4vye1/i_built_a_claude_skill_that_turns_an_arcade_rom"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T12:59:13Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["-muzbox-"]
language: "en"
summary: "Repo (free, MIT): https://github.com/muzbox1973/arcade-rom-3d-remaster You give Claude a MAME zip you legally own (e.g. galaga.zip) and the skill walks it through building a browser remaster. The original program ROMs run unmodified on an emulated board, and only the picture is swapped for a Three.js voxel renderer. The sound chip output gets re-rendered in higher quality, and you can press O to…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 332
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4vye1/i_built_a_claude_skill_that_turns_an_arcade_rom/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Claude skill that turns an arcade ROM you own into a 3D browser remaster, with the original game code still running underneath

Reddit · -muzbox- · 2026-10-13

Repo (free, MIT): https://github.com/muzbox1973/arcade-rom-3d-remaster You give Claude a MAME zip you legally own (e.g. galaga.zip) and the skill walks it through building a browser remaster. The original program ROMs run unmodified on an emulated board, and only the picture is swapped for a Three.js voxel renderer. The sound chip output gets re-rendered in higher quality, and you can press O to go back to the raw cabinet sound or V to flip back to the original 2D view. Why emulate instead of re-creating: my first attempt was a hand-made look-alike, and it just didn't play the same. Running the real code fixes that, and the 3D layer only reads video RAM / sprite RAM, so it can't break the game. How Claude was involved: Claude Code built the Galaga reference end to end: a Z80 core, a ZIP reader, the 3x Z80 board, HLE for the Namco 06XX/51XX/54XX custom chips, the WSG sound synth and the Three.js front end. The skill is basically what we learned from that, written down as a workflow: read the MAME driver, check the graphics decode visually, bring the board up in 2D first, then audio, then 3D, with a measurable gate at every step. The biggest lesson was "measure, don't assume." Claude's first guess at sprite rotation direction looked fine on screen but was mirrored in 232 of 240 cases. A pixel-overlap (IoU) test caught it. Another one: the emulator ran ~16x too fast with sound on, because a buffer length was read after the buffer had been transferred to the AudioWorklet. All of these are in references/pitfalls.md so Claude doesn't repeat them. Install for Claude Code: git clone https://github.com/muzbox1973/arcade-rom-3d-remaster ~/.claude/skills/arcade-rom-3d-remaster There's also a .skill file in Releases for Claude.ai. Limits: only a Z80 core is bundled so far, and Galaga is the only game built end to end. No ROMs are included and the skill tells Claude never to download any. Happy to hear feedback, especially from anyone who tries it on another Z80 board.
