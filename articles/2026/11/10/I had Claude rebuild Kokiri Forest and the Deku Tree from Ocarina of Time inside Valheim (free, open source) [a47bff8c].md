---
id: "a47bff8cea73ee7c"
title: "I had Claude rebuild Kokiri Forest and the Deku Tree from Ocarina of Time inside Valheim (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xsq0s2/i_had_claude_rebuild_kokiri_forest_and_the_deku"
link: "https://reddit.com/r/ClaudeAI/comments/1xsq0s2/i_had_claude_rebuild_kokiri_forest_and_the_deku"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T15:37:34Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Any-Explanation3814"]
language: "en"
summary: "This is a Valheim mod that turns Kokiri Forest and the Deku Tree from OoT into a playable world. Claude wrote all of the code, I played it a lot and told it what was off. It doesn't ship any Zelda files. You point it at your own ROM, it uses the zeldaret/oot decompilation to pull out the level geometry, collision, actor positions, texts, cutscene cameras and music, and rebuilds it all with…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 324
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsq0s2/i_had_claude_rebuild_kokiri_forest_and_the_deku/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I had Claude rebuild Kokiri Forest and the Deku Tree from Ocarina of Time inside Valheim (free, open source)

Reddit · Any-Explanation3814 · 2026-11-10

This is a Valheim mod that turns Kokiri Forest and the Deku Tree from OoT into a playable world. Claude wrote all of the code, I played it a lot and told it what was off. It doesn't ship any Zelda files. You point it at your own ROM, it uses the zeldaret/oot decompilation to pull out the level geometry, collision, actor positions, texts, cutscene cameras and music, and rebuilds it all with Valheim's terrain, textures, plants and lighting. So it's more of a remaster than a 1:1 copy. What Claude actually did: - wrote a small N64 display list interpreter so the models come out as meshes with the right textures - turned the collision floor into Valheim terrain and swapped the textures for Valheim ones - ported Link's moves, the enemies (Deku Babas, Skulltulas, Deku Scrubs, Gohma larvae) and the puzzles from the decomp's C code into the C# mod - replays the intro and cutscenes frame by frame from the game's cutscene data - renders the music from the ROM's sequences and soundfonts - it could control the game itself through a small command file in the mod (teleport, take screenshots, read the log), so it tested a lot on its own The clip shows the first try from Nov 6 next to the original, then where it is now. Playable: title screen, the intro, Kokiri Forest with the NPCs and their original texts, the Kokiri Sword, and the Deku Tree up to burning the web. Not there yet: Queen Gohma and everything after. Singleplayer only, some animations are basic, the camera in tight corridors is clunky. Try it (free, MIT): https://github.com/moritzfh/valheim-game-importer The mod DLL is on the releases page: https://github.com/moritzfh/valheim-game-importer/releases You need Valheim with BepInEx, your own OoT ROM (only the GameCube Collector's Edition EU version for now) and Linux or WSL for the build step. Steps are in the README. Happy to answer questions about how it was built.
