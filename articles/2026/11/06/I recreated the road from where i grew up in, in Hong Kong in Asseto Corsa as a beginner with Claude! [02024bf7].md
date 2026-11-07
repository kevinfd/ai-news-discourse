---
id: "02024bf7c31bd5d4"
title: "I recreated the road from where i grew up in, in Hong Kong in Asseto Corsa as a beginner with Claude!"
url: "https://reddit.com/r/ClaudeAI/comments/1xpldyb/i_recreated_the_road_from_where_i_grew_up_in_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xpldyb/i_recreated_the_road_from_where_i_grew_up_in_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T19:12:26Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Fuzzy_Pea6262"]
language: "en"
summary: "I lived in Hong Kong for about 10 years, and I wanted to see if I could recreate the street i grew up on in the racing game Asseto Corsa. The Hong Kong Lands Department publishes free 3D data (terrain, buildings with photo textures), but I haden't really used blender much and earlier attempts with other AI tools got nowhere. Naming the files correctly so that they could be imported in the game…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["policy & regulation"]
content_source: "post"
word_count: 375
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpldyb/i_recreated_the_road_from_where_i_grew_up_in_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I recreated the road from where i grew up in, in Hong Kong in Asseto Corsa as a beginner with Claude!

Reddit · Fuzzy_Pea6262 · 2026-11-06

I lived in Hong Kong for about 10 years, and I wanted to see if I could recreate the street i grew up on in the racing game Asseto Corsa. The Hong Kong Lands Department publishes free 3D data (terrain, buildings with photo textures), but I haden't really used blender much and earlier attempts with other AI tools got nowhere. Naming the files correctly so that they could be imported in the game properly also seemed to be a pain. So I worked it out with Claude, step by step, in Blender. It wrote Python scripts and I tested everything and reported what I saw. Some of the things that went wrong: My first test came out 100× too big (a hidden scale in the FBX export) In the game the buildings came out pitch black and the terrain glowing white, even though Blender looked perfect. ksEditor gives every material almost no ambient light and a lot of gloss. A small Custom Shaders Patch config file that overrides those values per material fixed it. The car spawned upside down (wrong axis on the start marker) The game refused to start without an AI line, so we wrote the file format ourselves A file got named .kn5.kn5 because Windows hides extensions ksEditor (the software that imports the 3d files into the game) froze for ages until a hidden error showed that it refuses any mesh over 65,536 vertices. The fix was splitting the terrain into chunks map 100× too big Lighting before fix It ended as one script that goes from the government files to a drivable track (almost, claude cannot use KsEditor to import the Blender model into the game and the user first needs to specify a few variables). It’s very specific to this data, so I’m not sure how useful it is to others but if you are interested i could ask claude to write something more general although im not sure how well that will work. P.S. I know its not that pretty yet, I had to get rid of lots of detail to get KsEditor to load Data: Lands Department, Government of the Hong Kong SAR, via the CSDI Portal (portal.csdi.gov.hk). The Government owns the intellectual property rights in the data.
