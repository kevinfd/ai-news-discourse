---
id: "19c5a770c7ad412e"
title: "6 months of Claude and I working on a tiny national park simulator"
url: "https://reddit.com/r/ClaudeAI/comments/1xg3uol/6_months_of_claude_and_i_working_on_a_tiny"
link: "https://reddit.com/r/ClaudeAI/comments/1xg3uol/6_months_of_claude_and_i_working_on_a_tiny"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T17:47:01Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["idun0"]
language: "en"
summary: "Hi! I posted a few months back about my game and got a fair bit of interest, so following up - This is \"Switchback: a tiny hiking and park simulator\" and I'm becoming really proud of this little game Claude and I made through many many hundreds of hours of back and forth and iteration and even some minor manual coding and design work on my end. It's cute, it's fun, it's dynamic, and it's…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 723
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xg3uol/6_months_of_claude_and_i_working_on_a_tiny/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 6 months of Claude and I working on a tiny national park simulator

Reddit · idun0 · 2026-10-26

Hi! I posted a few months back about my game and got a fair bit of interest, so following up - This is "Switchback: a tiny hiking and park simulator" and I'm becoming really proud of this little game Claude and I made through many many hundreds of hours of back and forth and iteration and even some minor manual coding and design work on my end. It's cute, it's fun, it's dynamic, and it's (nearly) what I've always wanted in a little diorama-y / building sim. It's been a joy to work on and wanted to share it. This video is a comparison of my first month of working with claude 20x and roughly 6 months later for the same level. I now have something like 30 levels and a few expansion packs as well. More context - this game is intended to feel kind of like Roller Coaster Tycoon but for National Parks. Theres a trail placing system, switchbacks, bridges, campgrounds, talks, horseback rides, boats, fishing, management of animals and lots of other stuff for management and maintenance. The general purpose is to solve little puzzles, create a world thats your own, and help your hikees reach viewpoints Every map has a lot of world meta data to work with. Everything form height mapping and steepness and biome/subbiome and rock type, to wetness, temperature, wind affect, lat-long, and much more. I purposely pursued a huge number of world values because this is something that I feel is now far more manageable as a solo dev that ever before with the help of AI. and the results end up being fairly dynamic and delightful to play with. Things like getting certain types of butterflies to spawn only in their exact conditions in their exact season or migration path, etc. is all fairly trivial to add and adds a level of detail to appreciate. Its three.js and voxel based, most of my time has honestly been spent optimizing and building custom solutions to things that likely already exist or have been solved... but thats kind of the joy of these AI primary projects in my view, finding unique solutions to problems that are uniquely yours Claude Specific Stuff! I love the 5.5 series for asset generation and I'm particularly proud of its results through my asset pipeline. It's a set of nested skills and standing requirements depending on asset type. I had claude build itsself a testing pipeline focusing on AI usability and controls including a viewing pipeline, and hearing pipeline to iterate with, performance analyzer, and a mass of smaller scripts and auto checks for things like angles being placed incorrectly or world units not being respected, or checking if a subagent made its own custom thing of a thing we already had. Every asset goes through at least 5 passes for completeness, correctness, intractability, variability in seed based generation, and most importantly, charm. Then it hands me a product sheet comparing what it build to my specs and I review. Also shoutout haiku 5.5 for translation services. Opus High spawned... wait for it.... 560 subagents.... of haiku for translation of every string over a couple hours to translate my whole app and check it and do the full i18n process I had spaced for it and it performed remarkably and used up like 1% of my 20x plan weekly usage. If you'd like to give it a try it's on both App Stores (FREE! for the first couple levels.) iOS - https://apps.apple.com/us/app/switchback-a-cozy-hiking-game/id6799833310 Android - https://play.google.com/store/apps/details?id=com.swanklabs.switchback . You can tell me it's slop if you'd like, but I'd like to think it's more of a AI bisque or warm AI broth at this point. if you have a windows PC or Mac, try out the desk top versions of the apps via android or iPad translation to Mac because it works best with mouse and keyboard. iPad is also good and then phone is ok, but it certainly takes a little more effort and doesn't look quite as good. If you have any questions I would love to discuss and will be in the comments :) would also love more feedback before I put on steam! I'm particularly proud of my asset process and map process. coming soon are more activities like rafting and paragliding and some new maps and biomes :)
