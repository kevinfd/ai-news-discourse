---
id: "9d7b8116750dd430"
title: "We built a way to plan and book flights and hotels by chatting with Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1xukoti/we_built_a_way_to_plan_and_book_flights_and"
link: "https://reddit.com/r/ClaudeAI/comments/1xukoti/we_built_a_way_to_plan_and_book_flights_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T18:33:37Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Efistoffeles"]
language: "en"
summary: "Hi everyone. I work with a small team and we built a connector for Claude that lets you search and book flights and hotels by just chatting, instead of jumping between ten travel tabs. It started because I always hated searching through tens of websites for a good offer. The first version was not a website or a connector at all. It was a Claude agent I made for myself. I would describe a trip,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media", "products & launches", "business & funding", "agents & coding"]
content_source: "post"
word_count: 450
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xukoti/we_built_a_way_to_plan_and_book_flights_and/"
score: null
comments: null
community: "r/ClaudeAI"
---

# We built a way to plan and book flights and hotels by chatting with Claude

Reddit · Efistoffeles · 2026-11-12

Hi everyone. I work with a small team and we built a connector for Claude that lets you search and book flights and hotels by just chatting, instead of jumping between ten travel tabs. It started because I always hated searching through tens of websites for a good offer. The first version was not a website or a connector at all. It was a Claude agent I made for myself. I would describe a trip, and Claude would do the searching and comparing I used to do by hand. That showed me Claude was good at the exact part I hated: turning a messy request into real searches, and reading a pile of results. I wanted it on my phone, so I ended up putting it in Claude as a connector. After we got some funding from investors, I started building it further with a few friends, and we designed the tools around how Claude actually calls them. We tested every change the same way: by planning real trips through Claude and watching where it asks the wrong question or guesses. Every time Claude guessed, we changed the tool so it asks instead. It doesn't guess anymore. It works simply by you describing the trip in plain words like how many people are going, where, for how long, what you want vs don't want etc. Claude asks for what is missing, then searches flights from every airline and major travel sites, plus hotels from our inventory with live rates, the total price, rooms, reviews and cancellation terms. It compares everything, including bag prices and each flight's on time record, and explains the options in plain words. Claude never books on its own: booking starts only when you press "Continue to payment", which opens a checkout on a website. The payment goes through Revolut, so neither Claude nor we ever see your card. The connector is now ranked top 20th Travel after we published it officially in Claude around a month ago. It is free to try. Searching costs nothing. Link: https://claude.ai/directory/letsfg You will still be able to search flights and hotels without the connector if you are in Claude Code. Just make sure you put some limit on it because it will burn a lot of token as it requires a lot of scraping, and that will take some time. With normal Claude app, it can't do web scraping like the Claude Code, so a connector is a must as a tool for it. Regardless of using Claude Code or the Claude app with the connector, it is incredibly important to clearly tell Claude what you want. Otherwise you might not get the offers you expected to get. Enjoy :)
