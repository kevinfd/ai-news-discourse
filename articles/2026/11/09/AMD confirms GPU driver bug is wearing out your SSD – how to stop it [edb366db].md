---
id: "edb366dbbd318358"
title: "AMD confirms GPU driver bug is wearing out your SSD – how to stop it"
url: "https://zdnet.com/tech/amd-confirms-gpu-driver-bug-is-wearing-out-your-ssd-how-to-stop-it"
link: "https://zdnet.com/tech/amd-confirms-gpu-driver-bug-is-wearing-out-your-ssd-how-to-stop-it"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T18:30:49Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Taylor Clemons"]
language: "en"
summary: "AMD has admitted a bug within its External Events Utility is wearing out SSDs, and promises a fix."
tags: ["Storage"]
orgs: ["AMD", "Nvidia"]
topics: ["chips & infrastructure", "products & launches", "health & science"]
content_source: "fulltext"
word_count: 597
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/amd33-2259262667.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# AMD confirms GPU driver bug is wearing out your SSD – how to stop it

ZDNet · Taylor Clemons · 2026-11-09

ZDNET’s key takeaways
- An AMD utility is causing drives to continuously write and rewrite data.
- A Reddit user reported that their drive’s health was being degraded.
- Workarounds are in place while AMD works on a permanent fix.
Under normal circumstances, an SSD might go all day without needing to access or write files. But for some AMD Radeon users, anything but normal circumstances are causing drives to continuously write and re-write data. The External Events Utility (EEU) that AMD installs alongside its CPU and GPU drivers is reportedly the culprit.
Also: Nvidia RTX 50 GPUs hit with more price hikes
SSD death by a thousand cuts
Reports of the issue first surfaced in July on AMD’s official PC user forum, with one user stating that the External Events Client Module and EEU were constantly writing information to their SSD after installing a Radeon 9060XT graphics card. Subsequent comments on the thread this month confirm that the issue has persisted despite several bug fixes and patch updates, with two users reporting hard numbers for data usage ranging from 0.3 MB/s to as much as 1.5 MB/s.
Also: The best laptops: Expert tested and reviewed
This week, Reddit user darklinkpower posted that the AMD Adrenaline Edition desktop application also had the EEU driver bug, using up to 1% of their drive health per month for around 16 months. That might not sound like much, but it can cause catastrophic problems if left unchecked.
AMD seems to be aware of the issue; a company official who goes by AMD_Vik on Reddit commented that it will “hopefully [be] fixed in the next [update].” While there’s little indication of how quickly a permanent, official patch will be pushed to users, there are a few ways you can protect yourself from the bug and prevent your storage drive from collapsing.
The workarounds
Solution 1: Disable EEU
- Press the Windows key + R, type in services.msc, and press Enter.
- Locate AMD External Events Utility.
- Open the properties menu, end the service/process, and change the startup behavior to Disabled.
This seems to be the most consistent fix for most AMD users reporting issues, but disabling the EEU can cause its own problems, such as disabling AMD FreeSync support or introducing display glitches if you hot-swap screens while your PC is powered on.
Solution 2: Disable ReBAR
The AMD Adrenalin Edition desktop app lets you control how your PC components communicate with one another, and it might be another facet of a complex problem. By allowing your CPU to access your graphics card’s memory, you can temporarily boost performance, but the EEU bug seems to let it and your GPU run rampant, eating up every bit of memory they can find. Changing a few settings within the app may help:
Also: I tried local AI on HP’s Omnibook Ultra
- Open the AMD Adrenalin Edition desktop app.
- Click the gear icon in the program, then go to Settings.
- Look for Smart Access Memory to be Enabled, Disabled, or Not Available.
- If it’s enabled, toggle it off to prevent your CPU and GPU from eating up your system’s storage and RAM.
This is a more niche solution that carries its own risk of introducing communication issues between your CPU and GPU, so I only recommend trying this route if disabling the EEU itself doesn’t resolve the issue. AMD’s official fix may be in the works, but without a firm timeline for release, users are left twisting in the wind trying to stop their PCs from hemorrhaging storage capacity.
