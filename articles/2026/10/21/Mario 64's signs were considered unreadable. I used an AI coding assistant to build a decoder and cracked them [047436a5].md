---
id: "047436a5b5964849"
title: "Mario 64's signs were considered unreadable. I used an AI coding assistant to build a decoder and cracked them"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xbovs7/mario_64s_signs_were_considered_unreadable_i_used"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xbovs7/mario_64s_signs_were_considered_unreadable_i_used"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T14:35:52Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["decorator"]
language: "en"
summary: "Each wooden signpost in Mario 64 has a certain texture on the front—it's 32 by 32 pixels and the letters are only three pixels high. You can't read it and no one ever has been able to, it's just a bunch of smudges. It was thought to be impossible. Although the plaque in the courtyard included the entire \"L is real 2401\" statement, no one had any idea what the signs might say. I wasn't able to…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 444
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xbovs7/mario_64s_signs_were_considered_unreadable_i_used/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Mario 64's signs were considered unreadable. I used an AI coding assistant to build a decoder and cracked them

Reddit · decorator · 2026-10-21

Each wooden signpost in Mario 64 has a certain texture on the front—it's 32 by 32 pixels and the letters are only three pixels high. You can't read it and no one ever has been able to, it's just a bunch of smudges. It was thought to be impossible. Although the plaque in the courtyard included the entire "L is real 2401" statement, no one had any idea what the signs might say. I wasn't able to read it either, so I decided on an alternative approach. I entered my guesses in old 90s style fonts, reduced the size of them as an artist would have done back in those days, printed them onto the wooden board and then checked to see which guess was closest to the actual pixels. Best fit I got: "I'm here. See me as you go. Hold on!" As anyone might ask: I'm not using any AI upscaler, not the sort of thing at all, for those merely invent stuff. I did ask Claude to assist me with writing the code, and frankly that was the only thing which enabled me to complete this in a reasonable amount of time since it's very good at producing this type of thing quickly. Moreover, it incorrectly answered a few questions with confidence, so I ended up testing everything twice. How certain am I? I won't pretend that this is certain. "I'm here. See" I'm pretty confident about The other one is the best match I've found, but "I'm here. See / us as we are / Find me!" is almost as good (my score for it is 616 compared to 661, the lower the score the closer it is). a random wrong sentence scores around 1050, for comparison What convinced me that it's not nonsense is the Japanese. The game was made in Japan, and the text is precisely the kind of thing you would get if a Japanese sign were translated word for word: ここにいるよ = "I'm here!" 通りがかりに見ていってね = "have a look as you go by" がんばってね (ganbatte ne) = "hang in there / do your best" Ganbatte is the thing you say to somebody when they're about to carry out something difficult. In Japanese school English it's often rendered as 'hold on'. It's rather appropriate for a sign telling Mario to keep going right before you jump into something dangerous lol If anyone wants to take a look at it or prove me wrong the code is on GitHub at https://github.com/supermochi64/sm64-plaque-decode/tree/main/signpost Is there anyone among you who's ever used AI when doing things like this, with the AI creating the tools but you having to check everything yourself?
