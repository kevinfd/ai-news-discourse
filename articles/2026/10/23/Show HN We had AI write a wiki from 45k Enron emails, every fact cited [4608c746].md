---
id: "4608c746385aec63"
title: "Show HN: We had AI write a wiki from 45k Enron emails, every fact cited"
url: "https://thisandthat.chat/enron"
link: "https://thisandthat.chat/enron"
source: "thisandthat.chat"
domain: "thisandthat.chat"
source_type: "community"
collector: "hackernews"
date: "2026-10-23T12:02:53Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["jreynar"]
language: "en"
summary: "We built Enron a company brain\nWe gave an AI 45,047 of Enron's emails, and it wrote 214 pages about the companies, regulators and banks Enron dealt with. Every fact cites the email it came from. When the mail shows a fact stopped being true, the page expires it on that date. No one edited a page or a fact.\n    An email in the corpus\n    \n    \n    \n  \n    Entity page\n    Dynegy\n   …"
tags: []
orgs: []
topics: ["policy & regulation", "business & funding"]
content_source: "fulltext"
word_count: 665
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50207620"
score: 63
comments: 54
community: "Hacker News"
---

# Show HN: We had AI write a wiki from 45k Enron emails, every fact cited

thisandthat.chat · jreynar · 2026-10-23

We built Enron a company brain
We gave an AI 45,047 of Enron's emails, and it wrote 214 pages about the companies, regulators and banks Enron dealt with. Every fact cites the email it came from. When the mail shows a fact stopped being true, the page expires it on that date. No one edited a page or a fact.
    An email in the corpus
    
    
    
  
    Entity page
    Dynegy
    CompetitorTrading counterparty
    Relationship then: 
    
      ✓ Checked against the email
  
- Find the types
- Find the entities
- Build the page
- Verify
214pages
49,401facts, each citing its email
93%of sampled facts fully supported by their email
0of 500 sampled facts wrong at their core
The last two come from a held-out audit by a second AI; see how we checked it.
These are the most-discussed organizations in the corpus. Each page has a slider. Drag it and the page shows what was known on that date, with facts that were only true for a while expiring in front of you.
Facts on these pages are sentences, each with a date and a source, rather than fields like headcount or revenue. Fields belong in a CRM or another system of record, and a brain like this one sits beside it, holding what changes too often or doesn't fit in a field. We describe the three kinds of company knowledge, and where each one lives, in The missing middle of company knowledge.
The pipeline proposed 57 narrow types and a person kept 54 of them. Almost all were kinds of organization, so we group these lists by a coarser class and keep the pipeline's own type as a tag on each entity.
Companies, regulators, law firms, banks, newspapers. What the company deals with.
209 pages · 929 entities found
Enron's own business units, desks, platforms, systems and codenamed projects.
5 pages · 551 entities found
The pipeline also found 78 products and platforms, 76 facilities and market points, and 49 events, listed without pages. Choosing which kinds of entity deserve a page is the setup a person does when configuring a company brain, and we made that choice before building any page. Every company's mail names things it doesn't need to track, in categories that are a bit of a mess: restaurants from catered events, airports from travel, movies mentioned in passing. Enron's mail is no different. The facilities include trading hubs, Enron Field, a parking garage and two tankers. The events mix business conferences with charity bike rides and Cirque du Soleil. The products mix software with an exchange, a statute and trade associations.
The right choice depends on the company. An event company should have pages for its events, a property manager for its facilities, and a hardware maker for its products. For Enron we gave pages to organizations named in at least 25 messages, and to the five most-discussed parts of Enron itself: three business units, a trading platform and a trading system. A real company brain wouldn't filter by count. A customer you signed today might have sent one or two emails, and you'd still want its page. The cutoff stands in for the judgment a person makes about what's worth keeping in the brain.
We're this+that. We made these pages with a prototype of something we're building.
We wanted a corpus anyone can check our work against. Enron's mail is public because the Federal Energy Regulatory Commission (FERC) released it during its investigation, and Carnegie Mellon has maintained it since 2003. It's a large, free and widely used body of a real company's internal correspondence. The company's history is also settled, so a page claiming, for example, that Dynegy agreed to acquire Enron in November 2001 can be checked against the record rather than taken on trust.
The mail shows the story in pieces. For the whole of it, read The Smartest Guys in the Room by Bethany McLean and Peter Elkind, who covered Enron's rise and fall as senior writers at Fortune.
