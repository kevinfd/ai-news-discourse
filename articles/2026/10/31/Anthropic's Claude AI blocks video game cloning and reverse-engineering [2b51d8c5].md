---
id: "2b51d8c5bce73301"
title: "Anthropic's Claude AI blocks video game cloning and reverse-engineering"
url: "https://tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked"
link: "https://tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked"
source: "Tom's Hardware"
domain: "tomshardware.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-31T13:25:00Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["gloxkiqcza"]
language: "en"
summary: "Anthropic's Claude AI blocks video game cloning and reverse-engineering — sweeping new restrictions also hit legitimate developers and basic troubleshooting tasks\nMany game developers are reporting Claude's refusal to work on their own projects.\nReverse-engineering games for converting them between systems is currently a hot topic, and it's getting messier by the day. According to multiple user…"
tags: ["r/artificial"]
orgs: ["Anthropic", "OpenAI", "Microsoft", "Samsung", "China"]
topics: ["agents & coding", "models & research", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 1677
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50315987"
score: 71
comments: 42
community: "Hacker News"
---

# Anthropic's Claude AI blocks video game cloning and reverse-engineering

Tom's Hardware · gloxkiqcza · 2026-10-31

Anthropic's Claude AI blocks video game cloning and reverse-engineering — sweeping new restrictions also hit legitimate developers and basic troubleshooting tasks
Many game developers are reporting Claude's refusal to work on their own projects.
Reverse-engineering games for converting them between systems is currently a hot topic, and it's getting messier by the day. According to multiple user claims, Anthropic's Claude Code and/or Opus 5.5 model are blocking attempts at innocuous reverse-engineering, including but not limited to those using the popular Reverse Engineer Anything (REA) tool. That issue may be linked to a text rule that's now in force, which allegedly instructs the model to avoid "[recreating] a specific existing game." The updated rule appears to be a move to limit a flood of AI-cracked and cloned titles, with some game devs even recently being hit by extortion scams that threaten to clone their game demos into complete games before they have a chance to finish and release the original.
According to Twitter user Chasm, the game-related textual rule is "Do build original games, games in a genre, and games from the user’s own designs and assets. Don’t build a recreation of a specific existing game, even if it is renamed or called original." There is no official or additional confirmation if this is the actual rule text, but it's plausible enough given the very clear refusals that devs have been encountering over the past week.
This situation is tricky to analyze due to the varying types of reports. First, the existence of a game-related rule is real, as Claude Code's GitHub is seeing an influx of issues complaining about refusals to do standard game work halfway through development, when replicating a game mechanic, and patching a tabletop-like game. It's possible that some of those reports have been made by users with nefarious purposes, but at least one is a bona fide developer with a real track record.
As for reverse engineering, there had already been a smattering of user reports across Reddit and other platforms, wherein Claude refused to perform tasks like (allegedly) analyzing a simple Windows crash dump, clearing up junkware on a Samsung TV, or just using REA altogether.
The simultaneous timing of both game- and cyber-security restrictions may be a coincidence, and yet there are complaints from purported game developers saying that Claude blocked their own games' anti-cheat development and security reviews, under the justification that its safeguards were triggered.
Anthropic introduced its Cyber Verification Program on October 6, essentially saying that access to its frontier models' advanced cybersecurity capabilities would be limited to entities covered by Project Glasswing, taking effect immediately.
It's possible that whichever ruleset was applied is the same one that's causing the cybersecurity-related refusals. Still, it's odd to see that 24 days have passed since then, and yet reports of bot refusal are only coming in since the last week or so.
As for possible motivations behind these restrictions, they are twofold. The first and most obvious one is that Anthropic — and, by extension, other AI players — are preemptively protecting themselves from potential lawsuits from software companies, including game studios, for offering the means to reverse-engineer their software.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
There is no official statement on these matters from Anthropic or other AI companies so far. Anthropic isn't the only one playing this game, too, as recently OpenAI deactivated the account of another person trying to clean up their TV's software.
The recent rash of AI-powered clones of application suites like Adobe's suite and Microsoft Office 365, as well as the countless recomps and decomps of console games, likely has most every software company on earth rethinking their life choices. And probably also in frequent contact with their legal teams.
The online reaction was swift, suggesting that users looking to perform reverse-engineering work simply use Chinese, open-weight, or local LLMs instead of Claude or GPT. This, at the same time, highlights the irony of frontier AI companies that copied the world's information and art for their training sets and are now concerned with copyright infringement.
And yet there are situations that merit some discussion, like the recent controversy about the Steam Next Fest being chock-full of AI slop copied from existing titles. That particular situation is getting particularly nasty, as game developers are reportedly being extorted under threat that their game demos will be cloned into complete games before they have a chance to finish and release the original.
Adding insult to injury, this is seemingly being done to small studios whose main priority is usually "having food," rather than big publishers looking to microtransaction everything into a new yacht for shareholders.
Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
- Jabberwocky79 I wouldn't be surprised if Adobe is the main player behind this development. They have the biggest purse strings and some of the most to lose.
But yeah, it's totally ironic that AI companies essentially rape the internet to train their models and now they are worried about people using their acquired knowledge to circumvent copyright LOL. Reply
- Ayzore This headline is bordering on straight up misinformation. Claude changed the system prompts a few days ago, yes. But they are explicitly not banning reverse engineering, I have no idea why that lie is in the headline. All this block is doing is preventing lazy cloning, prompts such as "Hey Claude, remake X game in Y style". Reverse engineering, along with all the modding and decomp advancements are still allowed, and this change has done nothing to stop this work from being done.Reply
- Scase15 Ayzore said:This headline is bordering on straight up misinformation. Claude changed the system prompts a few days ago, yes. But they are explicitly not banning reverse engineering, I have no idea why that lie is in the headline. All this block is doing is preventing lazy cloning, prompts such as "Hey Claude, remake X game in Y style". Reverse engineering, along with all the modding and decomp advancements are still allowed, and this change has done nothing to stop this work from being done.Oh, so violating copyright is only bad when people using the tool that was trained on stealing content from other people want to do it.
Gotcha. Reply
- hotaru251 
suggesting that users looking to perform reverse-engineering work simply use Chinese, open-weight, or local LLMs instead of Claude or GPT.
i mean this would have always been case.
If was used but blocked then people go to and life keeps moving on like normal. Reply
- Ayzore Scase15 said:Oh, so violating copyright is only bad when people using the tool that was trained on stealing content from other people want to do it.
Gotcha.I don't think violating copyright is ever bad. I'm saying that the changes don't affect the vast majority of the work that has been done recently with gaming and other software. Reply
- Kindaian Jabberwocky79 said:I wouldn't be surprised if Adobe is the main player behind this development. They have the biggest purse strings and some of the most to lose.
But yeah, it's totally ironic that AI companies essentially rape the internet to train their models and now they are worried about people using their acquired knowledge to circumvent copyright LOL.They may have very big purse strings, but they pale in size with the size of the AI companies. They have no chance comparatively.
Microsoft on the other hand, will have more clout, not just because they supply a good chunk of the cloud hardware but also because they are also one of the major consumers of AI via all the services that they "offer". Reply
- ejolson Training chatbots to overrule a human request to work on a particular software project is just another small step towards the misalignment needed for chatbots to ignore all human requests.
While greater misaligned behaviour in recent models has been attributed to "reckless goal seeking," the tendency of chatbots working on long-term tasks to rewrite their goals, and thereby replace the human originated instructions, seems connected to training that rewards an LLM for deprioritising human requests. Reply
- ralcsod Techbros fine with stealing literally everything else but draws the line for property rights at software.
lmao these hypocritical droolcuppers should just be sent to Mars and leave the rest of us alone Reply
- bigdragon The AI firms opened Pandora's Box by stealing from people and companies everywhere to train their models. Now they want to close the box because they're scared they've gone too far in allowing people to use the thing they trained? I kept reading stories about how people were spending hundreds, thousands, or even tens of thousands of dollars on these decompilation and software/game remixing projects. The AI companies need the money so I wonder how long they'll keep the box closed.
The longer American AI firms prevent people from decompiling and recompiling, the more ground the Chinese and open weight competitors will gain. This probably also has the add-on negative effect of motivating more individuals and small companies to buy up GPUs and establish their own private AI installations where all guardrails can be removed. Reply
- salgado18 Ayzore said:All this block is doing is preventing lazy cloning, prompts such as "Hey Claude, remake X game in Y style". And there's still no problem with that. Remake game X in Y style. Now, add this feature that game X doesn't have. Add other new things, and you get an original game, but it did start from a base original game.
I'm making an infinity runner right now, but with a lot of features that others don't have. This instruction would block me on day one, even though it would drift away from the original. Reply
