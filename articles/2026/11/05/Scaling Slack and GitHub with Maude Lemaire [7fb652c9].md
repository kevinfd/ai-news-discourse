---
id: "7fb652c9ef37fd7e"
title: "Scaling Slack and GitHub with Maude Lemaire"
url: "https://newsletter.pragmaticengineer.com/p/scaling-slack-and-github-with-maude"
link: "https://newsletter.pragmaticengineer.com/p/scaling-slack-and-github-with-maude"
source: "The Pragmatic Engineer"
domain: "newsletter.pragmaticengineer.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-05T15:58:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Gergely Orosz"]
language: "en"
summary: "Listen and watch now on YouTube , Apple , and Spotify . See the episode transcript at the top of this page, and timestamps for the episode at the bottom. Brought to You by • turbopuffer – The tpuf eng team is completely redesigning their storage architecture from first principles. And they’re documenting all of it! They made epic progress; take a look: turbopuffer.com/v3 • Antithesis – use AI…"
tags: []
orgs: ["Apple", "Microsoft", "Cursor"]
topics: ["agents & coding", "search & media"]
content_source: "fulltext"
word_count: 1355
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Scaling Slack and GitHub with Maude Lemaire

The Pragmatic Engineer · Gergely Orosz · 2026-11-05

Listen and watch now on YouTube, Apple, and Spotify. See the episode transcript at the top of this page, and timestamps for the episode at the bottom.
Brought to You by
• turbopuffer – The tpuf eng team is completely redesigning their storage architecture from first principles. And they’re documenting all of it! They made epic progress; take a look: turbopuffer.com/v3
• Antithesis – use AI agents to work on critical systems without worrying about correctness. Antithesis runs your complete system in a hostile environment, analyzes its behavior, and reproduces every issue perfectly. Learn more
• Entire – Entire launched its own Git forge, shipped Continuous Memory, and reinvented the pull request (called Trails). Trails are a much more natural workflow when agents keep pushing new changes, after iterating on feedback – and you have more context and control on when a change is ready to merge. Check it out
In this episode
What is involved in scaling up large, popular products at places like Slack and GitHub?
We get an insider’s view on this from Maude Lemaire, a principal engineer and author of ‘Refactoring at Scale: Regaining Control of Your Codebase.’ She spent nearly eight years at Slack, where she led the backend performance infrastructure team, before joining GitHub to tackle database scaling challenges. Most recently, she worked on improving performance at Cursor – including time to first token.
In this episode of The Pragmatic Engineer, Maude and I dig into the challenges of scaling some of the world’s largest software products. We explore how Slack handled growing numbers of enterprise customers, how it evolved its approach to load testing, and the lessons Maude learned during nearly eight years of scaling Slack’s infrastructure.
She also tells us what it was like joining GitHub in 2024 when Copilot was taking off, the challenges of working with GitHub’s gigantic Rails monolith, and how Maude uses AI in her work – while keeping judgment calls and decision-making firmly in her own hands.
Takeaways from the conversation with Maude
Here are eight interesting points from our discussion:
1. Performance should matter even if there’s no competition. In 2015, the homepage of Rent the Runway took up to 10 seconds to fully load due to a high-resolution hero image on the site. Maude was told it wasn’t an issue because there were no competitors to worry about. She thought differently: “The best competition is competition with yourself, knowing that you can do better, knowing that you can drive a better experience, ” she said. Maude spent some free time on speeding up the website without asking for permission to do so because it was the right call.
2. Slack limits custom emojis to 23 to avoid thundering herds. Here’s an example of a thundering herd: the CEO of a 100,000-member Slack channel posts “everyone gets Friday off!” In response, people start posting custom emojis – hundreds of them. The problem is that every single custom emoji has to fan out to all 100,000 users. With 10 custom emojis, that’s 1,000,000 fan-outs, with 100 it’s 10,000,000; a lot of network load! Slack limits custom emojis to 23 to avoid this problem. In reality, the absent 24th custom emoji is not missed.
3. Event floods can cripple the machines of Slack’s power users. Event floods are the cousin of thundering herds: they occur when a single client is overwhelmed by events coming through its own WebSocket. For example, when an IT worker is logged into lots of busy channels and they all receive the “everyone gets Friday off!” message – along with all the associated custom emojis and messages. This “power user” gets a sudden influx of messages with no deduplication and they struggle.
4. Load testing 500,000 WebSocket connections the simple way would have cost $150,000 per run. A new customer with 500,000 users was about to sign up to Slack, and Maude needed to run a load test to confirm the service could handle the load. Initially, she planned to spin up headless Chrome instances – each instance running a Slack session, and that would have cost $0.37 per five-hour session, per instance. The total price would’ve been crazily expensive. Instead, Maude built a tool called Koi Pond that spins up slimmed-down versions of Slack (‘Koi’), written in Go to establish the WebSocket connections.
5. Active Record downside: too much database load! GitHub used to be a Ruby on Rails monolith, which used Active Record as a database abstraction layer. This caused unexpected load: GitHub’s home page fetched live data from the database for most reloads, and loading the home page regularly triggered 100 SQL queries across three database clusters. This revealed a downside of abstractions like Active Record to Maude: when devs used it, they didn’t know or care about the additional load they unwittingly placed on the database while fetching data for whatever they were working on.
6. GitHub could not add more than 16 database shards because of scatter query problems. A scatter query is one without a primary key (a sharding key), and it needs to be run across all shard instances. But more shards make such queries slower.
Back in the day at GitHub, lots of queries made through Active Record (many on the homepage) were scatter queries. This limitation prevented GitHub from adding more than 16 shards. I find this detail fascinating: it shows why a developer-friendly abstraction (Active Record) can actually cause severe pain at the infra level!
7. For platform work, Maude personally verifies everything she gets from an LLM. When doing foundational work, Maude pays close attention to verifying the output of LLMs because she believes that ambitious structures can only be built on stable foundations. It’s an interesting approach to separate “foundational” and “non-foundational” work in order to give more attention to the former, most critical, type.
8. Platform and product engineers should rotate more. The best platform engineers Maude has worked with are product engineers who reimplemented similar features a few times, grew frustrated with the repetitive toil, and so built tools to remove it once and for all. But an issue arises when platform engineers become detached from product development and drift away from engineers’ experience of using the product. To remedy this, Maude suggests rotation cycles where a platform engineer joins a product team to build a feature, and a product engineer joins the platform team.
The Pragmatic Engineer deepdives relevant for this episode
• Real-world engineering challenges: building Cursor
• Pushing software engineering limits with “napkin math”
• What is happening with code reviews?
• Why reliability is hard at scale: learnings from infrastructure outages
• What is Reliability Engineering?
• The Platform and Program Split at Uber
• The present, past and future of GitHub
• Why performant code matters (but gets widely ignored), with Casey Muratori
• Designing Data-intensive Applications with Martin Kleppmann
Timestamps
00:00 Intro
03:15 Early years and path to software engineering
07:32 First job at Rent the Runway
09:17 The HipChat data leak
10:54 Joining Slack and the challenges of scaling
26:30 Load testing and thundering herds
32:29 Event floods
38:30 Evolving load testing at Slack
48:38 Joining GitHub in 2024
56:52 The challenges of the Rails monolith
1:02:26 How Maude uses AI
1:12:40 Advice for engineers interested in product/platform work
References
Where to find Maude Lemaire:
• LinkedIn: https://www.linkedin.com/in/lemairemaude
• Website: https://maudethecodetoad.com
Mentions during the episode:
• The Manager’s Path: A Guide for Tech Leaders Navigating Growth and Change: https://www.amazon.com/dp/1491973897
• Building Koi Pond: Simulating Millions of Slack Clients: Strange Loop, LeadDev, Presentation PDF
• Load Testing with Koi Pond: https://slack.engineering/load-testing-with-koi-pond/
• Thundering herd problem: https://en.wikipedia.org/wiki/Thundering_herd_problem
• Flamework: https://github.com/exflickr/flamework
• Vitess: https://vitess.io/
• Prisma: https://www.prisma.io/
• Uchat: https://www.uber.com/us/en/blog/uchat/
• Mattermost: https://mattermost.com/
• Rent the Runway: https://www.renttherunway.com/
• Year 2038 problem: https://en.wikipedia.org/wiki/Year_2038_problem
• HipChat: https://en.wikipedia.org/wiki/HipChat
• Refactoring at Scale: Regaining control of your codebase: https://www.oreilly.com/library/view/refactoring-at-scale/9781492075523
• Thread about building uChat on X:
• Cal Henderson on X: https://x.com/iamcal
• GitHub: https://github.com
• The present, past and future of GitHub: https://newsletter.pragmaticengineer.com/p/github
• Azure: https://azure.microsoft.com
• Cursor: https://cursor.com
• Real-world engineering challenges: building Cursor: https://newsletter.pragmaticengineer.com/p/cursor
—
Production and marketing by Pen Name.
