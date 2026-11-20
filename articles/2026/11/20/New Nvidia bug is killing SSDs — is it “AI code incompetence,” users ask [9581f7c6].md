---
id: "9581f7c63d780781"
title: "New Nvidia bug is killing SSDs — is it “AI code incompetence,” users ask?"
url: "https://tomsguide.com/computing/hardware/new-nvidia-bug-is-killing-ssds-is-it-ai-code-incompetence-users-ask"
link: "https://tomsguide.com/computing/hardware/new-nvidia-bug-is-killing-ssds-is-it-ai-code-incompetence-users-ask"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T00:04:18Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Scott Younker"]
language: "en"
summary: "<p>Scott Younker is the West Coast Reporter at Tom’s Guide. He covers all the latest tech news, including phones, computing and more. He’s been involved in tech since 2011 covering everything from cameras and swimming pool equipment to the latest gaming consoles and smart TVs. He is on a seemingly never ending hunt to build the easiest to use home media system. </p><p>Before Tom’s Guide, Scott…"
tags: ["Computing Hardware", "Computing"]
orgs: ["Nvidia", "OpenAI", "Google"]
topics: ["chips & infrastructure", "search & media", "products & launches"]
content_source: "fulltext"
word_count: 703
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/xWV7Xvua8aPb7TaLHKQ5Jj-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# New Nvidia bug is killing SSDs — is it “AI code incompetence,” users ask?

Tom's Guide · Scott Younker · 2026-11-20

New Nvidia bug is killing SSDs — is it “AI code incompetence,” users ask?
The latest in a string of bad days for Nvidia
If you haven't updated your Nvidia drivers recently, you may want to hold off. A newly discovered bug apparently can damage your PC by writing excessive amounts of data to solid-state drives (SSDs).
The bug was found in the two most recent Nvidia GPU driver updates — specifically 621.14 and 621.24 — for the Nvidia GeForce Game Ready Driver. The 621.24 update was released on November 12.
The bug was discovered by TroubleGrid who reported that the bug causes the NVDisplay.Container.exe to write (save data) far too much information to an Nvidia log file that can degrade the SSD. It can result in as much as 30GB per hour.
The executable already wrote log files before the updates but not that much. SSDs typically take years to degrade, but the excessive data written by this bug can speed up the process causing stuttering and mouse lag.
Conspiracy theories and Never Update
On Reddit, I've seen a few posts about the bug with users complaining that this is why you never update. "By principle I never ever update my drivers unless there are feature inclusions for let's say a new game I bought," one Redditor said.
Plenty of others agreed with that sentiment, and I'm inclined to say they're correct here.
The other half of the comments split between blaming AI-written code. Before his ouster, CEO Jensen Huang was pushing for Nvidia engineers to use more AI-generated code via chatbots and agents.
Get instant access to breaking news, the hottest reviews, great deals and helpful tips.
Or they were of the belief that Nvidia is purposely killing drives to force customers to pay more for new ones. Several called out Sam Altman and his recent claim that laptop RAM is a "terrible" allocation of a scarce resource.
"I honestly would not be surprised if they are doing this on purpose to kill our NVMe's," wrote a poster.
If we were to put blame on something, at this point, I'd say its AI-fueled incompetence, not AI-fueled greed, though that has led to said stupidity.
How to avoid the bug
The easiest fix is to rollback your graphics card driver to version 621.01, which is the last known patch to lack this bug.
TroubleGrid listed a manual fix that requires you to set the Nvidia Display Container LS service to manual. Though it'll cost you. Basically, this can disable the Nvidia Control Panel and Nvidia App, meaning G-Sync color settings, display scaling, resolution overrides and more will not rock. "Do not disable the service outright if you use G-SYNC or a custom colour profile," the report warns.
If you need a temporary fix, you can stop the service, delete the log file and start again. However, the file will return and continue to grow in size.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds.
More from Tom's Guide
- I spent a week with Nvidia's RTX Spark mini PC — it's brilliant, but unless you're Tony Stark, the AI tax is optional
- Is ‘RAMageddon’ a lie? A Judge just denied motion to dismiss RAM price fixing lawsuit, and the new evidence is potentially damning for them (and great for us)
- Who is Colette Kress? Meet Nvidia’s interim CEO
Scott Younker is the West Coast Reporter at Tom’s Guide. He covers all the lastest tech news. He’s been involved in tech since 2011 at various outlets and is on an ongoing hunt to build the easiest to use home media system. When not writing about the latest devices, you are more than welcome to discuss board games or disc golf with him. He also handles all the Connections coverage on Tom's Guide and has been playing the addictive NYT game since it released.
Something to share? Send secure tips on Signal: scyo1.55.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
