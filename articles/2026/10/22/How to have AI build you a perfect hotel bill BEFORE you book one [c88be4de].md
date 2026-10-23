---
id: "c88be4dec9eb8e95"
title: "How to have AI build you a perfect hotel bill BEFORE you book one"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xcw1xd/how_to_have_ai_build_you_a_perfect_hotel_bill"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xcw1xd/how_to_have_ai_build_you_a_perfect_hotel_bill"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T21:56:12Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Calm_Cartographer324"]
language: "en"
summary: "The number on a hotel page is almost never the number on your final bill. So before I book, I have the AI build the bill for me line by line, as if I was already checking out. This is how it works, with real examples: Start with the room rate for the whole stay, not per night. Then have it add the nights up for the exact dates and guests. When I added two kids (5 and 9) to the same hotel…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic"]
topics: ["policy & regulation"]
content_source: "post"
word_count: 430
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xcw1xd/how_to_have_ai_build_you_a_perfect_hotel_bill/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# How to have AI build you a perfect hotel bill BEFORE you book one

Reddit · Calm_Cartographer324 · 2026-10-22

The number on a hotel page is almost never the number on your final bill. So before I book, I have the AI build the bill for me line by line, as if I was already checking out. This is how it works, with real examples: Start with the room rate for the whole stay, not per night. Then have it add the nights up for the exact dates and guests. When I added two kids (5 and 9) to the same hotel searches in Marrakesh, the room and the total changed at all 14 hotels, so the guests matter from the first line. Have it add the resort or destination fee per night. At The Cosmopolitan in Las Vegas it's about 55 a night, around 62 with tax. It's easy to miss because it's often shown separately from the room rate. Have it add the room tax on top. In that Las Vegas example it was 13.38% on the room itself. Tax rates differ by city, and for the same hotel one site showed the city tax and another didn't, so I make it say where each number came from. Have it add what you pay AT the hotel. When I looked at 2,702 hotel rates in Marrakesh, 45% had a fee you pay at the hotel on top of what you paid online. Then have it show the final total and the cancellation deadline, and say which lines it's sure about and which ones it guessed. This is the prompt: "I'm considering [hotel] in [city], [dates], [number of guests and ages]. Build the full bill as if I was checking out: room rate for the whole stay, resort or destination fee, room tax, city tax, anything I pay at the hotel, and the final total. For each line tell me the source and if you're sure or guessing. Also tell me the last day I can cancel for free. If you can't find a line, say it's missing, don't estimate it." It's best to use Claude for this task, but any AI is able to do it. Though Claude has an advantage because of its massive directory. Normal LLM apps can't do the price lookups from web, so you'd need a connector for that. Normally for other LLM you'd need to add custom connectors which is annoying and also risky. But Claude has a bunch of good ones for this task. You can use any one below: LetsFG: https://claude.ai/directory/letsfg Booking.com: https://claude.ai/directory/booking Tripadvisor: https://claude.ai/directory/tripadvisor Enjoy :) and if you have something better than this, drop it in the comments
