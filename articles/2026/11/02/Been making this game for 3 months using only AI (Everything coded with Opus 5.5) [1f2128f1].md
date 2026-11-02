---
id: "1f2128f18a19a998"
title: "Been making this game for 3 months using only AI (Everything coded with Opus 5.5)"
url: "https://reddit.com/r/ClaudeAI/comments/1xlr3u8/been_making_this_game_for_3_months_using_only_ai"
link: "https://reddit.com/r/ClaudeAI/comments/1xlr3u8/been_making_this_game_for_3_months_using_only_ai"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T07:43:48Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["RUSuper"]
language: "en"
summary: "Hello there again :) As I post weekly updates here probably a lot of people already saw this. I recently finished entire zone 1 and with that Demo is completely done. Fishing and exploration game that I'm making with primarily using AI tools. You can play it for free here: DEMO LINK DOWNLOAD - FREE Also whoever donated 5$ last week thank you very much, I was very happy when I saw it ☺️ What is…"
tags: ["r/ClaudeAI"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 896
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlr3u8/been_making_this_game_for_3_months_using_only_ai/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Been making this game for 3 months using only AI (Everything coded with Opus 5.5)

Reddit · RUSuper · 2026-11-02

Hello there again :) As I post weekly updates here probably a lot of people already saw this. I recently finished entire zone 1 and with that Demo is completely done. Fishing and exploration game that I'm making with primarily using AI tools. You can play it for free here: DEMO LINK DOWNLOAD - FREE Also whoever donated 5$ last week thank you very much, I was very happy when I saw it ☺️ What is game about: Game is about fishing and exploration, you have progression kinda similar to RPG with talent per level, experience, questing and leveling, your boat is your character, it has 6 item slots and they vary in rarity. They are not too complex like items in real RPG would be, they still offer some variety. Exploration would probably be on par with fishing as importance, and there is literally "exploration" mechanic that you can use on certain spots. Other than that similar to dredge style of inventory management, main story, events at the sea and moral dilemmas are big part of the game. Dynamic weather that have some gameplay implications, but nothing too major. Also dangers at night (pirates sharks etc). For those who do not want dangers at night, you can play "cozy mode" at the creation of the captain in new game, but you can't switch later. What was done this week: Black Market is done look wise, it still needs entire scene when docked like other docking places have so it is not fully done, shops, characters and so on. Also I feel like it might need a little bit more green, but also I kinda wanted it to be more rocky so hard to say if look will change a bit as I test play more. Keep in mind Black Market is not part of the demo that you can download. Also new main docking site for zone 2 is being built. Originally this was planned as zone 3, but I decided to swap tropical zone with this one as this is more similar to original zone where player starts. This is city with a big bridge that reminds of Golden Gate Bridge and also totally not statue of liberty in the front. Look of this city is not finished and more work is to be done, especially reflections of the sun and shadows also colouring. I also didn't do any polishing yet or other times of the day except day time. Considering you can't really get to the city and it is only to visually be there and have a docking spot, I won't go too much into details in the city itself. Workflow : Engine is Godot and this week required Gauntlet-Loop way of building things for both new places. I use /goal and /loop when creating new zones so that rough sketch that I have gets closer to the mockup that ChatGPT generates as image. After that everything is built with Opus 5.5 . The way I use Opus 5.5 this week is different to how it was used before, I use Jev for every task that I give to Opus then Jev decides on effort level depending on the task and we go with. If task requires higher than "extra" effort it asks for my approval first. I honestly can't tell you guys if it saves any usage in the long run, to me it all seems more or less similar, it certainly is better than running things on Ultracode. I still use decisions.md where every decision is tagged by either [user] or [proposed] (Ai). And user tags take priority over ai ones. They also help with AI not gaslighting you, in fact it can be annoying with saying like "oh but you decided against it back in early september in decision #4" so I have to be like "Yeah that was too long ago and game evolved since then". So this helps me a lot. Models were done either in Blender or by TripoAI . I often use now TripoAI as it helps with textures, but I do not always use those textures, sometimes I ask Opus to build some itself as materials. Often it just fits style of the game better. Some models are done in TripoAI and then fixed by Opus in Blender with MCP. Especially fishing rods. Those are almost never seen as models in game, as you fish from your boat and can only be seen as small model on the ship panel or if player chooses to look at 3D model of the Rod, but I still want them to look "properly". I noticed that TripoAI works best when you have all 4 sides of the model so I often just create 1 single image with all 4 sides (front,back, left and right), ask Opus to split it into 4 images, upload those images into TripoAI and if it requires some fixing - ask for that also, or if you think model is good enough as it is, just implement it. That would be it for this week, any feedback is appreciated :) Total cost: Claude Max 200$ x 3 = 600$ Astra 100$ x 1 = 100$ ElevenLabs x 11$ = 11$ TripoAI 20$ x 2 = 40$ OpenAI API credits 80$ = 80$ Other things I forgot about 100$ = 100$ (around) Around 900-950$
