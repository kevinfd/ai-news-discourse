---
id: "10f67c4c7e32fd22"
title: "I missed a 20-year-old Quake 2 mod, so I made my own browser version with Claude Code. Not a dev, long post"
url: "https://reddit.com/r/ClaudeAI/comments/1xllvbm/i_missed_a_20yearold_quake_2_mod_so_i_made_my_own"
link: "https://reddit.com/r/ClaudeAI/comments/1xllvbm/i_missed_a_20yearold_quake_2_mod_so_i_made_my_own"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T02:46:58Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Knawlodgeable"]
language: "en"
summary: "There was a tiny Quake 2 mod called RailWarz I played as a kid: lightning-fast capture the flag with grappling hooks and one-shot railguns. To me it was the Formula 1 of shooters, and I've missed it for 20 years. I just had a baby, so in my downtime I made my own version that plays in a browser, but I added a little Italian twist (grappling -> Grappoli). It's free, nothing to install:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "jobs & society"]
content_source: "post"
word_count: 737
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xllvbm/i_missed_a_20yearold_quake_2_mod_so_i_made_my_own/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I missed a 20-year-old Quake 2 mod, so I made my own browser version with Claude Code. Not a dev, long post

Reddit · Knawlodgeable · 2026-11-02

There was a tiny Quake 2 mod called RailWarz I played as a kid: lightning-fast capture the flag with grappling hooks and one-shot railguns. To me it was the Formula 1 of shooters, and I've missed it for 20 years. I just had a baby, so in my downtime I made my own version that plays in a browser, but I added a little Italian twist (grappling -> Grappoli). It's free, nothing to install: https://playgrappoli.com/ (computer only for now: keyboard and mouse, or a controller) I was also interested in learning how to build a real-time multiplayer game and host it on my own server + web address. For context, I’m not a software engineer (I work in cpg/sales) so most of this was new to me. With Claude Code, you can stand up a basic version of your idea in ~30 minutes. I had players (basically beans with eyes) moving, hooking and shooting at each other on a local server I was hosting within an hour or two. From my experience vibecoding similar projects, the 'long tail' of the development is getting the right taste/look/feel and giving your game some personality. Art direction. I gave it an Italian twist: the look of an old travel poster, and every map a real kind of place (a Venetian canal, a vineyard, a kitchen, a marble quarry). Voice lines. Write a line for every big moment, generate a few takes with an AI voice tool, and pick by ear. Making the announcers characters (an old Italian chef and his granddaughter) helped a lot. Props in Blender. The pots in the Nonna's Kitchen map started as a plain cylinder drawn in code. Claude can write Python scripts that build models in Blender, so now it's a hammered copper pot. UI. I put the theme on every screen, added a character screen where you can see your avatar move, and made it one click to get into a match. Bots. I fell down a rabbit hole here. Make them play by human rules (same controls, a reaction delay, aim that settles) so they aren't superhuman. Then teach them to actually play capture the flag (attack, defend, escort the carrier) and give them different personalities so they don't all do the same thing. Map principles. Our first maps were too big, formulaic, and so busy with props they killed your momentum. We built tools that fly every route between the flags, and a scorecard against classic arena shooter maps: how long a capture takes, number of chokepoints, etc. Characters. To get realistic movement in our own chunky style, the models are built in Blender and the legs and body run on free motion-capture clips, blended by speed so the feet don't slide. Spectating. I wanted watching to feel like an esports broadcast, so the camera cuts to wherever the action is. It used to jump around too much, so now it glides between shots. Performance. I built a performance overlay and a benchmark for each map so I could see what was actually slow. It was mostly draw calls, so we merged hundreds of separate decorations per map and got each character from 69 draw calls down to 42. Phones. I couldn't get it to feel right on a phone. Aiming the hook and the rail with your thumbs just isn't the same, so it's keyboard and mouse for now (a controller works too). If anyone's seen a mobile game do swinging well, let me know. The basic tech stack: The game: three.js in the browser, built with Vite. No game engine. The server: Node.js with WebSockets. The server runs the game 125 times a second, and your browser predicts your own movement so it doesn't feel laggy. Voice chat runs over WebRTC. Hosting: one small Hetzner server, Caddy for HTTPS, and a domain name. Art and animation: Blender, driven by Python scripts Claude writes. The motion capture is Quaternius' Universal Animation Library (free, CC0). Voice lines : I used a $1 trial of ElevenLabs, but there are plenty of options out there. Community: a Discord server. The game posts there through a webhook when people start playing. Nothing was decompiled: the movement follows Quake 2's open-source code, and the classic community maps are credited to their authors. There's a game night this Thursday (5 Nov), 8 pm CT / 9 ET / 6 PT, and I'll be on all hour: https://discord.gg/kdKt3yzeN8?event=1565072015260655757
