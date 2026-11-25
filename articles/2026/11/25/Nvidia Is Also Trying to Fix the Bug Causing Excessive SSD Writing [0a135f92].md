---
id: "0a135f92cf7b9c73"
title: "Nvidia Is Also Trying to Fix the Bug Causing Excessive SSD Writing"
url: "https://cnet.com/tech/computing/nvidia-ssd-writing"
link: "https://cnet.com/tech/computing/nvidia-ssd-writing"
source: "CNET"
domain: "cnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-25T02:22:22Z"
published_date: "2026-11-25"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Omar Gallaga"]
language: "en"
summary: "Nvidia has issued software updates, but it’s unclear if the problem is completely fixed."
tags: ["Graphic cards"]
orgs: ["Nvidia", "AMD", "China"]
topics: ["chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 443
paywalled: false
image: "https://www.cnet.com/wp-content/uploads/sites/2/geforce-rtx-5070.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia Is Also Trying to Fix the Bug Causing Excessive SSD Writing

CNET · Omar Gallaga · 2026-11-25

Nvidia has had its share of drama lately, with the ousting and sudden un-ousting of CEO Jensen Huang after it was discovered he’d had multiple affairs, including one that involved an alleged member of a Chinese spy network. The fallout from the revelations was so significant that some worried Huang’s fate could be a major disruptor to the health of international markets and the future of the entire AI industry.
Given that, the world’s largest semiconductor company possibly wishes its biggest problem were software-related. But that won’t be much comfort to PC users affected by a software bug in Nvidia’s graphics driver that has caused some to experience excessive writes to their solid-state drives.
The issue began popping up in mid-November as posts on Nvidia’s support forums, as well as on Reddit and sites like HardForum, reported seeing as much as 30GB to 70GB of data per hour written to their SSDs. These types of drives wear down quickly over months of such use.
More from CNET
Nvidia didn’t immediately respond to a request for comment and hasn’t made any public statements on the issue, but did acknowledge it in a hotfix and subsequent software update for its Windows 11 GeForce Game Ready Driver 621.40, where it said under Fixed General Bugs, “Excessive writes to file nvlog.nvlgstg may occur in background.” The driver that appeared to have caused the problems was released on Nov. 12.
Some tech experts on social media had been suggesting rolling back to older graphics drivers before the hotfixes were released and warned that letting the problem go unchecked could cause an SSD to eventually fail.
Described by WCCF Tech as “a hotfix for the hotfix,” the new update appears to fix the issue in ways that the previous fix did not.
Nvidia’s software problem closely mirrors an issue AMD had with its own Adrenalin Edition graphics software just weeks ago. As of Nov. 18, AMD was still making tweaks to its graphics software to iron out any lingering problems.
What to check if you’re still concerned
PCGamer offered a way to check if your PC is affected by the excess writing issue.
Open Task Manager, click on the Details tab and right-click on the columns at the top to select “I/O write bytes” as one of your Task Manager columns. By doing that, you can see if the file “NVDisplay.Container.exe” is writing a huge amount of data to your data drive.
If that’s the case, you should update immediately to Nvidia’s latest drivers for the fix. In fact, it might be a good idea to update whether you’re experiencing high write rates or not, just to be safe.
