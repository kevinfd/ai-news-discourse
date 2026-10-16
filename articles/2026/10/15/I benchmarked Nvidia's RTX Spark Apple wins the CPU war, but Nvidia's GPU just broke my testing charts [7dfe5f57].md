---
id: "7dfe5f57ac4f62b2"
title: "I benchmarked Nvidia's RTX Spark: Apple wins the CPU war, but Nvidia's GPU just broke my testing charts"
url: "https://tomsguide.com/computing/cpus/nvidia-rtx-spark-benchmarks"
link: "https://tomsguide.com/computing/cpus/nvidia-rtx-spark-benchmarks"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T18:46:07Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Jason England"]
language: "en"
summary: "<p>Jason brings a decade of tech and gaming journalism experience to his role as a Managing Editor of Computing at Tom's Guide. He has previously written for Laptop Mag, Tom's Hardware, Kotaku, Stuff and BBC Science Focus. In his spare time, you'll find Jason looking for good dogs to pet or thinking about eating pizza if he isn't already.</p>"
tags: ["CPUs", "Laptops", "Computing", "Computing Hardware"]
orgs: ["Nvidia", "Apple", "Microsoft", "Intel"]
topics: ["chips & infrastructure", "search & media"]
content_source: "fulltext"
word_count: 1864
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/3LkD4AgudgNF36g8bsRMiL-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# I benchmarked Nvidia's RTX Spark: Apple wins the CPU war, but Nvidia's GPU just broke my testing charts

Tom's Guide · Jason England · 2026-10-15

I benchmarked Nvidia's RTX Spark: Apple wins the CPU war, but Nvidia's GPU just broke my testing charts
Big on the GPU!
The embargo has lifted on Nvidia's RTX Spark platform, and the internet is currently doing what it always does: arguing over spreadsheet math. I've done something different with my diary of a first week living with Spark, but I've been busy benchmarking too!
For months, the tech industry (myself included) hyped up this Arm-based Grace CPU and Blackwell RTX GPU combo as the ultimate "MacBook Pro killer." Reviewers (also like me) have spent the past seven days squinting at Geekbench scores to see if Nvidia finally dethroned Apple's M-series silicon.
Let me save you some time: it didn't.
But judging RTX Spark purely by its single-core CPU speeds is like judging a Ferrari by its cup holders. And after a week of stress-testing the Microsoft Surface Laptop Ultra with Spark — running every synthetic and real-world test we can throw at it — it's clear that this is so much more.
Those numbers tell a very different, far more complicated story. Let me explain.
Where to buy RTX Spark laptops
- MS Surface Laptop Ultra: $2,599 @ MS Store
- HP OmniBook X AI 14: $2,999 @ HP
- HP OmniBook Ultra AI 16 OLED: $3,199 @ Best Buy
- Lenovo Pro 9n: $2,999 @ Lenovo
- Lenovo Yoga 9n 2-in-1: $2,999 @ Lenovo
- MSI Prestige N16 Flip AI+ OLED 2-in-1: preorder for $3,299 @ MSI
- Dell XPS 16: $3,799 @ Best Buy
- Asus ProArt P14: $6,499 @ Asus
- Asus ProArt P16: $4,499 @ Asus
CPU reality check: Apple is still king, but other Windows laptops don't stand a chance
So let's start with the first benchmark everybody goes to. If you were hoping Nvidia's Arm-based Grace CPU was going to embarrass the M5 Pro, you need to adjust your expectations.
Given how long it took to make this, it's fair to say this was the main bit I felt nervous about. In short, not terrible, but underwhelming.
Get instant access to breaking news, the hottest reviews, great deals and helpful tips.
That being said, this was one of the first chances I had to test Nvidia's claims of getting the same performance on and off the charger.
Now I know there's a difference maker in here — Windows power settings. Putting it to best efficiency will probably starve the chip of power to match it. With that in mind, I've just done the test in both this mode and best performance to see what I get.
Certainly a surprise to see it gain a few points when unplugged, but this falls within the window of variability in the test results I've been getting. So the answer is a resounding "yes," provided you slap on best performance.
To dig deeper into that multi-core performance, I went to Handbrake. One of the tests we run across all systems is transcoding a copy of Tears of Steel from 4K down to 1080p. This is a solid real-world test of video encoding and real-world multi-core processing.
As you can see, it clearly leads the way in Windows laptops (Intel caught napping there), but Apple silicon reigns as champ.
The GPU flex: Comparable to an RTX 5070 laptop
Gaming is where Nvidia gets its lick back against the competition. It has a massive Blackwell RTX GPU in it, after all, and when you look at the 3DMark numbers, it matches up to something you’d see in an RTX 5070 gaming laptop — even when tasked with x86 emulation in some of these tests.
And to check it's not just the CPU getting that same performance on and off the charger...
Once again, same performance on and off the battery. This is consistent with what Nvidia's been telling us, and it's one of the features gatekept by Apple MacBooks that is now in the hands of Windows users!
Now, let's get into the games.
Forza Horizon 6
Forza Horizon 6 is one of my favorite racing games of the past decade, so it only makes sense I start here. Let's max it without DLSS tech and see what we get.
Bear in mind this is a stress test of epic proportions, but you can see how it struggles. That 1% low is a good indicator of the consistency of the frame rate, which is highly volatile here.
Interestingly, as I tried this push to Extreme + RT settings, I noticed some rubberbanding in the gameplay — probably down to the CPU having to work overtime translating the x86 code of the game while also sending the instructions to the GPU.
You can see that as Frametime spikes can be seen anywhere from 60ms up to 140ms. The game feels sluggish.
But now let's hone it. Thinking about this like an RTX 5070 laptop, I'll drop it down to Ultra + RT (same resolution) and stick with DLSS 4.5 set to auto with dynamic frame generation.
Immediately, this feels so much better to play! There are still some latency spikes here and there, but none that are hardly noticeable.
Also interesting to note, the temperatures on the GPU dropped too by one degree (71 C in the first run, and 70C in the second).
And the cherry on top — here's performance on battery.
Yep, same performance on and off the charger here!
Cyberpunk 2077
Listen up, choombas! It wouldn't be an Nvidia laptop test if we didn't touch on Cyberpunk 2077. For context on this one, I'm gonna compare it against gaming laptops with different GPUs, so you can see where it lands.
And if you're curious, I got 38.9 FPS when unplugged (basically 39).
Black Myth: Wukong
Is this a safe space? ...I'm really not a fan of Black Myth: Wukong.
OK, I get it! I can appreciate the craft of it, and I get why people love it. I've just never got on with it. That being said, I did benchmarks for this too.
...you spotting a pattern? This maxed-out RTX Spark is lining up pretty much neck-and-neck with the RTX 5070, while also running cooler and more efficiently. Nifty!
Gears of War: E-Day
This came out recently, and I saw it being played at the Surface Laptop Ultra event in San Francisco, so of course I had to push it further here.
This is running at 2180x1453 Ultra settings with DLSS 4.5 Dynamic and RTX Mega Geometry turned on.
Some observations here — this is clearly a scalable engine on PC that can run fast here. But there were some micro-stutters when I pushed it to the bleeding edge.
That being said, the average frame time and response to controller inputs meant this all felt smooth with virtually zero latency.
Creative apps is where RTX Spark starts to shine
There are several ways to test creative performance, so I'll dive into them one by one. PugetBench is a good way of seeing how a laptop will fare in your standard creative prosumer workload across Photoshop and Premiere Pro. Here's how RTX Spark fared in my testing.
The finely-tuned cores of the M5 Pro take the win here, but RTX Spark does take a leap ahead of its Windows competition in creator performance.
Let's get to Cinebench
Unfortunately, there isn't any GPU testing available here yet (the OptiX driver for the chip isn't there), so this is a straight CPU comparison.
These numbers put it ahead of Intel, AMD, and Qualcomm's latest flagships, but Apple M5 Pro (again) comes out on top. It's the best of the Windows bunch.
AI performance is where RTX Spark takes the lead
To put some numbers to Nvidia's advantage here, I ran it through UL Procyon AI benchmarks.
This isn't a test that has been normally run on other laptops in the Tom's Guide lab, so I've had to ask around my friends/fellow nerds for insights on this.
In their experience, RTX Spark seems to be surpassing the M5 Pro's AI prowess, exceeding the capabilities of AMD Ryzen AI Max+ and blowing past Intel Core Ultra X9. Once I can do these tests myself, I'll do a follow-up.
Also, for what it's worth, here's the comparison to my RTX 5060 Ti 16GB desktop GPU.
A reduction is always expected between the raw wattage of desktop parts and a laptop chip, but the Spark does get impressively close.
Battery life is a mixed bag
So what about stamina? Nvidia promised all-day battery life, and technically that’s true. But it doesn’t come close to the efficiency king of Apple’s MacBook Pro.
When it comes to gaming or running local AI at full pelt, this falls in line with what you’d expect from an RTX gaming laptop (our gaming test result got one hour and thirty-eight minutes) — give or take about 20-30 minutes depending on how much power the internals soak up.
Meanwhile, if you're expecting that same all-day battery life claim to extend to gaming, that's not the case. You do indeed get more stamina than your average gaming laptop, but not by much.
Who should buy RTX Spark, and who should buy a gaming laptop?
That battery equivalency does raise another question — who is RTX Spark for?
Because for all intents and purposes, an RTX 50-series gaming laptop could do a lot of this workload, whether it’s gaming, creative work, or some of the local AI stuff. And depending on how efficient that gaming laptop can run, you could get a similar battery life.
The real differentiator comes in that unified memory. With there being two pools of memory between the RAM and the GPU’s VRAM in a gaming laptop, it’s not as efficient as having one giant tub of it that can be divided depending on job priority.
That means on RTX Spark, you can run vastly larger local AI models, and larger projects in the likes of Blender than you could elsewhere. This is definitely for the prosumer market.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds.
More from Tom's Guide
- I didn’t believe an Nvidia RTX Spark laptop would have the same performance both on and off the charger — so I put it to the test
- Forget RTX Spark: The Surface Laptop Ultra’s magnetic USB-C charger is a game-changer that makes Apple’s MagSafe look obsolete
- I just tested Windows 11 26H2 — here’s how to update now and why Microsoft finally fixed the two worst things about Windows 11
Jason brings a decade of tech and gaming journalism experience to his role as a Managing Editor of Computing at Tom's Guide. He has previously written for Laptop Mag, Tom's Hardware, Kotaku, Stuff and BBC Science Focus. In his spare time, you'll find Jason looking for good dogs to pet or thinking about eating pizza if he isn't already.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
