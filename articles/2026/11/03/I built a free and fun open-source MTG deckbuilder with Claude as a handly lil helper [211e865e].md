---
id: "211e865e2527da5b"
title: "I built a free and fun open-source MTG deckbuilder with Claude as a handly lil helper"
url: "https://reddit.com/r/ClaudeAI/comments/1xn78r2/i_built_a_free_and_fun_opensource_mtg_deckbuilder"
link: "https://reddit.com/r/ClaudeAI/comments/1xn78r2/i_built_a_free_and_fun_opensource_mtg_deckbuilder"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T22:27:33Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Imparat0r"]
language: "en"
summary: "Lately, I have been struggling a lot with inspiration and could not come up with fun and engaging decks to play with. I started looking for deckbuilders and went the usual way of checking Scryfall and EDHREC and various other deckbuilding sites, but these were mostly decks already made up by other people. Then I started experimenting with Claude, asked it questions about Magic and various cards…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 342
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn78r2/i_built_a_free_and_fun_opensource_mtg_deckbuilder/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free and fun open-source MTG deckbuilder with Claude as a handly lil helper

Reddit · Imparat0r · 2026-11-03

Lately, I have been struggling a lot with inspiration and could not come up with fun and engaging decks to play with. I started looking for deckbuilders and went the usual way of checking Scryfall and EDHREC and various other deckbuilding sites, but these were mostly decks already made up by other people. Then I started experimenting with Claude, asked it questions about Magic and various cards and what not, and although not perfect, it did give me some ideas. I then built a little Claude Skill called [mtg-master]( https://github.com/m-sahin/mtg-master ) and had a great time with it talking about Magic and possible decks. I thought, this is awesome and started building a little webapp around it where you can give Claude 5 cards and it then builds out the rest of the decks, based on your requirements. After a while I also added a workshop where you can build your own deck with just a little bit of help from Claude and you can draw hands based on what Claude thinks would work. I used Supabase for storing decks and user profiles and authentication, and typescript for the app itself. One thing I really did struggle with is how to allow visitors to play around and have to sign up or subscribe to use the api. So I give everyone a few free builds , where I set the model to haiku 5.5 and effort to medium. Costs around 0.02 per deck. Based on IP, you would get 10 free decks per day and a site total maximum of 300. You can fork the app and run it in your own environment, you just need to connect supabase and fill in the env. Then you can use your own apikey for unlimited deckbuilding, and even set the model to opus 5.5 , which takes longer to build decks , but you would get far stronger decks than with haiku 5.5 or Sonnet. Im still tweaking it and making it better everyday , would love your opinion on it! https://www.hundredfoldz.app/ Repo: https://github.com/M-Sahin/hundredfoldz
