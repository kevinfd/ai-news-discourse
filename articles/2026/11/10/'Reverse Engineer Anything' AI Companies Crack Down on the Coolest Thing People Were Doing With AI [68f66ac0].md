---
id: "68f66ac0cbd7169a"
title: "'Reverse Engineer Anything': AI Companies Crack Down on the Coolest Thing People Were Doing With AI"
url: "https://404media.co/reverse-engineer-anything-ai-companies-crack-down-on-the-coolest-thing-people-were-doing-with-ai"
link: "https://404media.co/reverse-engineer-anything-ai-companies-crack-down-on-the-coolest-thing-people-were-doing-with-ai"
source: "404 Media"
domain: "404media.co"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T14:21:37Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Jason Koebler"]
language: "en"
summary: "It was a fun few weeks while it lasted. People using both Anthropic’s Claude and OpenAI’s Codex to do AI-powered “reverse-engineering” or decompiling are now hitting guardrails or having their accounts limited while trying to do things like unbrick their internet-of-things devices or remove surveillance ads from their smart TVs.  Several people have reported triggering “safety checks” in Claude…"
tags: ["AI"]
orgs: ["Anthropic", "OpenAI", "Samsung", "China"]
topics: ["safety & ethics", "models & research", "policy & regulation", "search & media"]
content_source: "fulltext"
word_count: 1189
paywalled: false
image: "https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/2026/11/CleanShot-2026-11-10-at-6.20.18-AM@2x.png"
discussion_url: "https://news.ycombinator.com/item?id=50441618"
score: 10
comments: 6
community: "Hacker News"
---

# 'Reverse Engineer Anything': AI Companies Crack Down on the Coolest Thing People Were Doing With AI

404 Media · Jason Koebler · 2026-11-10

It was a fun few weeks while it lasted. People using both Anthropic’s Claude and OpenAI’s Codex to do AI-powered “reverse-engineering” or decompiling are now hitting guardrails or having their accounts limited while trying to do things like unbrick their internet-of-things devices or remove surveillance ads from their smart TVs.
Several people have reported triggering “safety checks” in Claude Code that prevented them from doing AI-powered reverse engineering; a highly upvoted Reddit post in r/ClaudeCode reads “The Dream is dead. Reverse Engineer Anything (REA) is not likely to work with Claude.” A thread in the Reverse Engineer Anything Discord from last week reads, “Claude is refusing to decompile anything,” with multiple users responding saying they have hit similar walls. And X user log4j, who used OpenAI’s Codex to reverse engineer Samsung TVs, reported having their OpenAI account banned for violating its rules on “cyber abuse.” Other users said they asked Codex to reverse engineer hardware or their own code now say they have either been warned by the company or had their accounts restricted. A project called Decomp.wtf that made it easier to reverse engineer software and games has also shut down in recent days.
As we reported last month, Reverse Engineer-Anything has made it easy for people to use AI tools to hack electronics that they own and replace a manufacturer’s software or operating system with an open source or vibecoded one. People have installed new operating systems on their smart TVs, have turned baby monitors into AI assistants, have unbricked internet-of-things devices that were abandoned by their manufacturers, and have installed new software on very old hardware. At the time, I wasn’t sure how I felt about the trend, but as I’ve seen people take ownership and control back over the devices that manufacturers have purposefully bricked, turned into spyware, or have placed artificial limitations on, I have come to see AI-powered reverse engineering of electronic devices as one of the few LLM uses genuinely worth getting excited about. And so big companies have immediately taken steps to restrict this behavior.
The policy tweaks show that big AI corporations will protect other big corporations when their users find ways to use LLMs to circumvent the artificial constraints that hardware manufacturers put on their devices. AI-powered copyright circumvention is OK with big tech when it’s a massive company scraping the entire internet to build their LLMs, but is not OK when people then use those tools to liberate their internet-of-things devices. It’s not the end of AI-powered reverse engineering, but people suddenly getting locked out of their accounts for asking AI to reverse engineer their gadgets suggests that the future of this practice lies in open weight, local, and uncensored models, making it less accessible to the masses and the people who could probably benefit from it most.
Tarun Gogineni, an OpenAI engineer, tweeted that people are not supposed to have their OpenAI accounts restricted for reverse engineering: “these blocks are mostly accidental and a result of difficult decision boundaries; there is no prohibition against reverse engineering with codex. it’s getting fixed,” he tweeted.
But people who are doing AI-powered reverse-engineering suggest that they are moving away from big companies’ models to alternatives where they aren’t going to have their accounts disabled or have to figure out how to work around AI company guardrails.
“My general experience about reverse-engineering getting blocked has been more or less 100% correlated with the ‘cyber’ category blocks I have received. My take is that the lab[s] are probably under pressure to not have their models take part in some kind of criminal hacking activities and their cyber guardrails are erring on the side of being too strict,” Matt Brown, principal consultant at Brown Fine Security and someone who has been using AI to reverse-engineer devices, told 404 Media. “I am investing in hardware and trying to stay up to speed because the frontier labs guardrails will randomly change without warning on the same model. For my security research and pentesting work I really don’t want to invest tooling and energy into an ecosystem that will eventually lock me out. These guardrails on the frontier side have come at the same time as open weight models from (mostly) China are getting better and better.”
Brown posted a YouTube video last week explaining how he found hidden Bluetooth commands in an internet-of-things gas monitor attached to his propane tank with the open weight model GLM 5.3. He has explained in various posts that the guardrails big companies are putting on reverse engineering are why local AI and open weight models are important.
AI-powered reverse-engineering isn’t going anywhere, but it does look like it’s going to become much harder to use the most popular frontier models from OpenAI and Anthropic for it. It’s unclear how much longer it will be possible for you to open an OpenAI Codex window, ask it to find a smart TV hooked up to your network, and tell it to install a new operating system on it. Moving forward, it looks like this type of work will be best done with open source, open weight, uncensored, and local models. That’s a bummer, because one of the things that was so exciting about the Reverse Engineer-Anything trend was how easily accessible it had become.
Last month, researchers and law professors at Cornell Tech, Columbia University, and New York University published a paper about how cheap, AI-assisted reverse-engineering is challenging big manufacturers’ dominance over the devices their make, and is challenging existing intellectual property law.
“AI systems can identify hardware components, extract firmware, decompile object code, and clone entire apps. The resulting struggle between technology vendors and reverse engineers will challenge a wide range of laws, including trade secret, copyright, anti-circumvention, computer misuse, and contract,” they write. “The law of reverse engineering was built for a world where opening a device took time, tools, and rare expertise. That friction is vanishing as agents whittle endless, precise picks for the many little locks that fill our digital lives.”
In recent days, people have started modifying older digital cameras with new, vibe-coded operating systems. In a video about hacking old cameras, the YouTuber Breno Loves Cameras explains why it’s such a big deal and why camera companies don’t like it; that same logic can be applied to any device manufacturer.
“Camera companies have this practice of keeping features to release on newer cameras, and having distinctions [in features] in camera lines,” the YouTuber Breno said in one video. “This is breaking that from those big companies, which are going to lose a lot of money if this becomes a big thing.”
Through that lens, it’s easy to see why big companies are protecting other big companies. People finally found a thing to do with AI tools that gives consumers a bit more control over the devices they bought; it must be immediately stamped out.
“This vibe-code hacking is only called ‘reverse’ when somebody who lacks a trillion dollars is doing it,” the science fiction author Bruce Sterling tweeted. “When you ‘reverse engineer’ the entire Internet Common Crawl, you just built a nice AI model.”
