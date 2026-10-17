---
id: "dbfb9a2e3c4bc43b"
title: "Continuous accountability for Verified bots"
url: "https://blog.cloudflare.com/verified-bots-accountability"
link: "https://blog.cloudflare.com/verified-bots-accountability"
source: "Cloudflare Blog"
domain: "blog.cloudflare.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-16T13:00:00Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Chris Tsoukaladelis"]
language: "en"
summary: "A driver’s license tells you who someone is and that they passed a driving test, not whether they’ll drive responsibly in the future. The same is true for bots: verifying who operates it creates accountability, but trust depends on what it does next. A known bot can still ignore website preferences, overwhelm origins, or evade controls. It’s not always malicious — often it’s just a…"
tags: ["AI", "Bots", "Internship Experience", "Radar", "Security"]
orgs: ["Perplexity"]
topics: ["robotics & autonomy", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 1052
paywalled: false
image: "https://blog.cloudflare.com/_emdash/api/media/file/01M51ZPERWNWYTD7Z36YMY80A8.01M51ZPFH7VV8EHQTMPJG9FHZ4.png"
discussion_url: null
score: null
comments: null
community: null
---

# Continuous accountability for Verified bots

Cloudflare Blog · Chris Tsoukaladelis · 2026-10-16

Continuous accountability for Verified bots
A driver’s license tells you who someone is and that they passed a driving test, not whether they’ll drive responsibly in the future. The same is true for bots: verifying who operates it creates accountability, but trust depends on what it does next. A known bot can still ignore website preferences, overwhelm origins, or evade controls. It’s not always malicious — often it’s just a misconfiguration or a bug.
As we described in a previous blog post on bot behavior, we strive to verify two questions: “Are you who you say you are?” and “Can we trust you?” To be a Cloudflare Verified Bot, you broadly need to meet three criteria:
- Identify yourself accurately and securely
- Do only what you say you will do
- Don’t engage in abusive behavior
Bots use Web Bot Auth to sign requests that establish their identity, which BotBase then catalogues in an open format. With identification addressed, our focus shifts to the second cardinal rule of Verified bots: thou shalt do no harm.
Today we introduce a system to evaluate and report when Verified bot behavior starts to deviate from this rule, ensuring that the answer to “Can we trust you?” remains “Yes.”
This is where the distinction between risk and trust becomes important:
- Risk describes the likelihood that a particular request or point-in-time action may be harmful, and it can change from one moment to the next.
- Trust is built over time through repeated and consistent behavior.
For example, we de-listed Perplexity’s bot from our Verified bot list in 2025 when it sought to access resources on websites that opted out of scraping and subsequently attempted to circumvent controls when those requests were blocked.
Do not engage in abusive behavior
This simple requirement sounds like a freebie, but there is a lot of nuance in that statement. When crawlers don’t respect site preferences, that undermines trust. When sites request a crawler to not crawl or to slow down, and the crawler ignores these requests, that undermines trust.
We developed a system to measure how often a crawler respects site preferences. These observations will translate to an explainable trust band: a range showing how consistently a bot respects site preferences and which observed behaviors informed that assessment, rather than a permanent judgment about a bot or its operator. The initial signals we evaluate are:
- Does the bot respect instructions?
- Did it respond to direct feedback?
We consider these to be “common sense” rules, a courtesy to the operators who provide the information bots seek. In the future, we will be sharing these scores publicly on Radar, as well as expanding the ways we measure. This score gives responsible bot operators a way to demonstrate that trust is being upheld over time. Verify, but continuously re-verify.
When in Rome, do as the Romans do
A robots.txt file is the primary way to communicate site owner preferences. Our system considers whether a bot’s observed traffic is consistent with those published preferences over time.
Robots.txt tells all (or specific) bots to only crawl specific parts of a website. Isolated violations and other types of one-offs may not be significant. What we look for instead are repeated patterns of behavior that disregards site preferences. The expectation is simply for responsible bots to consult and honor the preferences that websites publish, in line with RFC 9309.
And just to be clear, a robots.txt sets the minimum rules for what bots and agents should not do. But there is no implication that anything not stated is allowed. For example, a robots.txt does not need to say that a bot must stop when the site can communicate that continued access is unwelcome through other signals.
What you do not wish for yourself, do not impose on others
Bots can remain entirely within allowed paths while still placing substantial load on the websites they visit. One of the clearest ways a website can push back is with an HTTP 429 (“Too Many Requests”) response. A 429 is a directive for the visitor to reduce its request rate, sometimes with guidance about how long to wait before trying again.
Our system considers whether the bot’s traffic adapts after receiving that signal. Does it slow down, pause, or does it continue sending requests at the same pace? We then incorporate that behavior into the bot’s trust band over time: consistently slowing down or pausing increases trust, while repeatedly ignoring the signal lowers it.
Building trust over time
Observing these signals is only a first step toward making verified automation accountable over time. By pairing bot identity with evidence of continuing behavior, we can give site owners more confidence that the bots they choose to allow are respecting their preferences, give bot operators a way to demonstrate they deserve trust, and provide context to website owners about the automated traffic reaching them.
This system, alongside Bot Preference Sync and Bot Management, forms an accountability loop for automated traffic. Bot Preference Sync helps website owners publish their preferences, and observing how bots interact with these preferences shows whether Verified bots consistently honor them over time. Bot Management lets website owners decide how that traffic is handled. Together, they help ensure that trust is earned through transparent, accountable behavior, not assumed from identity alone.
We are already using this system internally to evaluate how consistently Verified bots honor website preferences. Because trust is built over time, we assess sustained patterns rather than isolated events. We are using this initial phase to build that history and refine how those observations become useful guidance. Building on that foundation, we plan to make the system available to all Cloudflare customers, who will be able to choose the trust threshold used to decide how Verified bot traffic is handled. Our goal is straightforward: to keep website preferences meaningful, and ensure trust is earned through sustained behavior.
Want to learn more about how you can handle bots? Cloudflare customers can already use Bot Management to manage automated traffic and Bot Preference Sync to align their published preferences with their configured policies. To explore the ever-growing Verified bot population, see the trends on Radar.
And if you are interested in helping build the future of bot identity and accountability, explore open roles at Cloudflare.
