---
id: "8b3dad4b108f7d4d"
title: "Solo Developer Rebuilds Adobe Creative Suite in Rust Using Claude"
url: "https://tomshardware.com/software/video-editing-graphic-design/solo-developer-rebuilds-adobe-creative-suite-in-rust-using-claude-releases-it-free-to-all-targets-100-percent-parity-in-one-month-despite-piracy-claims-and-safety-warnings"
source: "Tom's Hardware"
domain: "tomshardware.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T12:39:26Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["ianbooker"]
language: "en"
summary: "Solo developer rebuilds Adobe Creative Suite in Rust using Claude, releases it free to all — targets 100% parity in one month despite piracy claims and safety warnings\nTransitioning from Adobe to a free alternative without an adjustment period sounds like a dream.\nControversially named Reddit user u/ai_art_is_art posted on r/creativecloud about their suite of alternatives for the most-used Adobe…"
tags: []
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "safety & ethics", "search & media"]
content_source: "fulltext"
word_count: 1636
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50005127"
score: 15
comments: 9
community: "Hacker News"
---

# Solo Developer Rebuilds Adobe Creative Suite in Rust Using Claude

Tom's Hardware · ianbooker · 2026-10-08

Solo developer rebuilds Adobe Creative Suite in Rust using Claude, releases it free to all — targets 100% parity in one month despite piracy claims and safety warnings
Transitioning from Adobe to a free alternative without an adjustment period sounds like a dream.
Controversially named Reddit user u/ai_art_is_art posted on r/creativecloud about their suite of alternatives for the most-used Adobe products recreated using Claude. Their post has since been removed, but their comment with links to their GitHub page remains. PhotoCraft, LightCraft, ImageCraft, FilmCraft, and more are equivalents to multiple Adobe products and are available for download, but commenters warn of safety concerns and actual functionality.
Adobe’s dominance in creative tools is nothing new; it has been the industry standard for decades, with entire workflows depending on it. The Redditor wanted to create an open-source version with all the familiar layouts and functions for each product, planning to reach 100% parity within a month. The projects were all built in Rust, as the creator emphasizes multiple times in their GitHub repositories.
There is no shortage of free alternatives to Adobe products; however, the alternatives often have largely different layouts and workflows. Affinity does its best to compete with Photoshop, and it doesn’t fall short; however, Affinity still has a learning curve, and it doesn’t offer an integrated suite of products like Adobe. It seems that the developer’s goal with this is to unify the experience, unlike having multiple free creative products all built by different developers. The developer is also focused on AI integration and has also made it so that the creative software is agent-native, allowing AI to easily use the tools and menus over a JSON control channel and an MCP server, essentially intending for users to let the AI create art directly using the software.
This project has had mixed reactions, with some saying it is stealing from Adobe and warning the developer of a lawsuit; responses to those warnings state that it is a clean-room reimplementation and no Adobe source code was used or copied in the creation of the software. One commenter sarcastically responded to a post on X sharing the developer’s Reddit comment: ‘“Something really cool is happening:” Piracy,’ while others are in support, saying Adobe deserves this due to its shady buisness practices.
Skeptics also warn of safety concerns with vibecoded software; a single person has generated potentially hundreds of thousands of lines of code for multiple pieces of software very quickly, and verification of the code becomes a mountain of a task for a developer without a team; a 2026 State of Code Developer Survey of 1,100 professionals by Sonar indicates that 96% of developers do not fully trust AI-generated code. Privacy problems, malicious code, unsafe file handling, and more are among the list of concerns.
Excited testers say this could be a legitimate Adobe alternative, but others claim it may just be more vibecoded AI slop. It remains to be seen how many will collaborate to improve upon this project and fill in the missing features that it plans to replicate.
Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.
- bit_user I'd be curious to know if it's actually good to use. Second only to malware concerns, that would be my worry about using something potentially sketchy. Third, I'd bet it's a lot more resource-intensive than the actual Adobe tools and is missing lots of features. Finally, and especially if it is feature-rich, I wouldn't be at all surprised if someone found the AI essentially lifted chunks of code from stuff like Gimp.Reply
- ezst036 Some of the interest here is to get off of Windows.(or stay off, for those who just could not stay and gave up Adobe in the process) Just saying. Some people feel trapped like a wild animal, and its actually Adobe which is the sharp metal teeth on their ankle. Some users will use VMs and various wrappers or WINE or other ultimately gimmicky solutions but the steel hinged trap is still there, clinched on tightly and painfully.
Adobe by itself alone is probably worth a point or two. Maybe more. Reply
- bit_user ezst036 said:Some of the interest here is to get off of Windows.(or stay off, for those who just could not stay and gave up Adobe in the process) Just saying. Some people feel trapped like a wild animal, and its actually Adobe which is the sharp metal teeth on their ankle. Some users will use VMs and various wrappers or WINE or other ultimately gimmicky solutions but the steel hinged trap is still there, clinched on tightly and painfully.Yeah, they have some web-based tools, but their functionality is still quite a lot less than the full-fat native versions. Reply
- USAFRet There are a multitude of free or inexpensive alternatives to "Adobe Photoshop". Have been for years.
The only time real Photoshop is needed would be in a paying gig, where the business pays for it. IMHO, of course.
Otherwise....
paint.net, GIMP, Paintshop Pro, etc, etc, etc. Reply
- JamesJones44 The clean room argument will only hold water if code used by the agent didn't appear in some mail chain somewhere that the agent got ahold of it (or worse hacked Adobe to get it). The issue is, the developer likely doesn't know where the code came from, so it could be clean room or it could be infringing. The laws around this are super tricky and if I was the dev I would fully expect a letter.Reply
- nrdwka JamesJones44 said:The clean room argument will only hold water if code used by the agent didn't appear in some mail chain somewhere that the agent got ahold of it (or worse hacked Adobe to get it). The issue is, the developer likely doesn't know where the code came from, so it could be clean room or it could be infringing. The laws around this are super tricky and if I was the dev I would fully expect a letter.would be hilarious if ai agent decided to hack adobe, done it and made that apps 😂 Reply
- sadsteve USAFRet said:There are a multitude of free or inexpensive alternatives to "Adobe Photoshop". Have been for years.
The only time real Photoshop is needed would be in a paying gig, where the business pays for it. IMHO, of course.
Otherwise....
paint.net, GIMP, Paintshop Pro, etc, etc, etc.Yep. I ditched Photoshop when they went to the subscription model. I settled on Affinity Photo which was on sale for $25 at the time. It does all I need and is relatively easy to use. On a positive note, you can get Affinity Photo for free now. They were purchased by Canva awhile back and they made it free if you don't need/want the advanced Canva features. Reply
- hotaru251 essentially intending for users to let the AI create art directly using the software. 
idk which i hate more...Adobe or ai "art"...
while others are in support, saying Adobe deserves this due to its shady buisness practices. 
oh they would 100% deserve it.
Adobe is the of the few actual anti consumer corpo that they could cure cancer and it wouldnt make them liked as their rep is THAT hated. Reply
- eklipz330 JamesJones44 said:The clean room argument will only hold water if code used by the agent didn't appear in some mail chain somewhere that the agent got ahold of it (or worse hacked Adobe to get it). The issue is, the developer likely doesn't know where the code came from, so it could be clean room or it could be infringing. The laws around this are super tricky and if I was the dev I would fully expect a letter.the repercussions of Adobe trying to sue a person for AI generated code would be VAST and DAMNING. The entire industry would reel from breech of copyright law, which doesn't seem to apply to AI for whatever reason. It would open the door for any person to sue for theft, whether it's their likeness or their wording. Imagine all the books they're trained on. So it won't happen, ever.
Regarding the question of whether it's safe and reliable, it is open-source. So you get to check it yourself. Reply
- DS426 USAFRet said:There are a multitude of free or inexpensive alternatives to "Adobe Photoshop". Have been for years.
The only time real Photoshop is needed would be in a paying gig, where the business pays for it. IMHO, of course.
Otherwise....
paint.net, GIMP, Paintshop Pro, etc, etc, etc.Right, and pretty much every Adobe app has at least one good alternative, but the article is saying that the integrated content creation suite that Adobe provides makes it harder to come off as then two or three or however many separate app vendors have to be utilized depending on the user's end-to-end workflow.
I also think Adobe's policies and dark patterns (like make it hard to cancel subscriptions, etc., raise prices ~40% year-over-year, etc.) are despicable and thus would love to see others rise up and create affordable alternatives to their entire suite, not just individual apps. As much as Adobe charges these days, I feel like the risk would be worth the reward. Until then, we can only hope that OSS and focused proprietary software vendors continue to chip away at Adobe's market share. Reply
