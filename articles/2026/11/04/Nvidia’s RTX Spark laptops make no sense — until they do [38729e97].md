---
id: "38729e97cc2f955e"
title: "Nvidia’s RTX Spark laptops make no sense — until they do"
url: "https://pcworld.com/article/3275866/nvidias-rtx-spark-laptops-make-no-sense-until-they-do.html"
link: "https://pcworld.com/article/3275866/nvidias-rtx-spark-laptops-make-no-sense-until-they-do.html"
source: "PCWorld"
domain: "pcworld.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-04T05:00:00Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Brad Chacos"]
language: "en"
summary: "We’ve tested Nvidia’s wild new chips for AI, gaming, and everyday work. Here’s where RTX Spark kicks ass—and where it doesn’t."
tags: []
orgs: ["Nvidia", "Microsoft", "OpenAI", "Meta"]
topics: ["chips & infrastructure", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 1551
paywalled: false
image: "http://www.bing.com/th?id=ONUT.0o98CmgyTZz5VJGX_Y-pTw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia’s RTX Spark laptops make no sense — until they do

PCWorld · Brad Chacos · 2026-11-04

We’ve tested Nvidia’s wild new chips for AI, gaming, and everyday work. Here’s where RTX Spark kicks ass—and where it doesn’t.
Nvidia makes laptop CPUs now. That still feels weird to type!
Over the past month, PCWorld has been hammering on several laptops powered by Nvidia’s new RTX Spark platform, including Microsoft’s Surface Laptop Ultra, HP’s OmniBook Ultra, and the absolutely insane $7,000 Asus ProArt P16 I reviewed with 128GB of unified memory. We’ve tested everyday performance, played games, and run local AI models ranging from relatively petite LLMs all the way up to OpenAI’s gargantuan 120-billion-parameter gpt-oss model. I even pitted the top-of-the-line ProArt against my monstrous GeForce RTX 5090 desktop in an AI cage match.
So after weeks of poking, prodding, benchmarking, and generally trying to make these things sweat, what should you actually expect from an RTX Spark laptop?
Quite a lot—just probably not in the ways you’d expect.
AI is RTX Spark’s superpower
RTX Spark laptops are AI PCs in the most literal sense—not because Windows has a Copilot button or somebody sprinkled “AI” across a marketing slide, but because the hardware itself is designed to run serious AI workloads locally.
The secret sauce is memory, and how it behaves with Nvidia’s RTX 5070-class integrated graphics. Traditional gaming laptops pair system memory with a discrete GPU packing its own much smaller pool of ultra-fast VRAM. RTX Spark instead wraps its 20-core Arm CPU and beefy Blackwell GPU around one big pool of unified memory that both can access. That unusual architecture is also why you can’t build an equivalent RTX Spark desktop yourself. RTX Spark laptops can pack up to 128GB of the stuff, and the ProArt 16 let me devote roughly 96GB of that to the GPU.
That sounds like an esoteric technical detail. But it lets RTX Spark do some wild stuff.
My desktop also has 128GB of total system memory, along with a GeForce RTX 5090—the fastest consumer graphics card Nvidia has ever made. But only 32GB of its memory is attached directly to the GPU in the form of VRAM—once that’s filled, it needs to bounce to much slower general PC RAM. When I threw the same sprawling research workload at OpenAI’s 120-billion-parameter gpt-oss model on both systems, the ProArt chewed through 472,084 total tokens in 33 minutes and 13 seconds. My fire-breathing RTX 5090 desktop needed 52 minutes and 51 seconds.
A 3.9-pound laptop beating my RTX 5090 desktop by almost 20 minutes is bonkers. But RTX Spark didn’t win because its GPU is faster—it flat-out isn’t. Give both systems a workload that fits comfortably inside the RTX 5090’s screaming-fast 32GB of GDDR7 and the desktop GPU can run wild. This particular workload needed an enormous amount of GPU-accessible memory, and that’s precisely what RTX Spark was built to provide.
Much like Liam Neeson in Taken, RTX Spark excels at “a very particular set of skills.” If you’re running enormous local AI models, this thing can do jobs that conventional laptops simply can’t. You can run them without paying for every cloud token, with your data staying on your own PC. If you’re asking ChatGPT questions in a browser or dabbling with smaller local models, though, you don’t need this. And if you’re thinking about dropping $7,000 on an RTX Spark laptop for AI, you’d better have workloads that can actually use all that memory. Seven thousand dollars buys an awful lot of cloud AI.
Yes, RTX Spark can game
Michael Crider/Foundry
RTX Spark’s integrated Blackwell GPU is also damned powerful, especially considering it’s sitting in the same package as the CPU. PCWorld’s Michael Crider spent days gaming on RTX Spark with HP’s RTX Spark-powered OmniBook Ultra, while Mark Hachman put Microsoft’s Surface Laptop Ultra through its paces. These machines can absolutely play modern games, roughly keeping pace with Nvidia’s GeForce RTX 5070 discrete graphics. That’s wild in and of itself!
You also get Nvidia’s full bag of RTX tricks. DLSS upscaling and frame generation can dramatically boost performance in supported games; Mark saw Cyberpunk 2077 leap into triple-digit frame rates once he started flipping those switches. That’s mighty impressive for integrated graphics.
But if you’re primarily looking for a gaming laptop, don’t buy one of these.
Michael Crider/Foundry
Mike’s testing found conventional GeForce laptops delivering better gaming performance for far less money. We even compared his results against my 128GB ProArt to see whether all that extra unified memory helped games, and—spoiler alert—it didn’t make a lick of difference. That’s hardly surprising: Cyberpunk doesn’t need 96GB of GPU-accessible memory, but a 120-billion-parameter AI model sure does.
Consider the gaming chops a very nice bonus. RTX Spark is powerful enough to let you fire up demanding games after you’re done crunching AI workloads, but spending RTX Spark money specifically to play games makes about as much sense as buying a Threadripper workstation to browse Facebook.
It’s also a surprisingly normal laptop
Mark Hachman / Foundry
One of the strangest things about RTX Spark is how ordinary it can feel when you’re not throwing exotic workloads at it. For all the unusual hardware lurking under the hood, you can open one of these machines and just use Windows 11 like you would with any other PC.
Mark spent more than a week putting Microsoft’s Surface Laptop Ultra through PCWorld’s traditional testing and found its 20 Arm CPU cores delivered excellent multicore performance, while single-core performance was considerably less impressive. That’s important for everyday use because having 20 cores doesn’t magically make every interaction 20 times faster. Plenty of common tasks still lean heavily on one or a handful of threads, including many office tasks and general app responsiveness.
Battery life isn’t some Arm-powered miracle, either. Mark saw roughly 10 hours from the Surface Laptop Ultra in PCWorld’s office-work testing—perfectly respectable, but nothing revolutionary. But once you actually unleash RTX Spark’s defining capabilities, physics comes knocking hard. During one of my monster AI runs, the ProArt 16’s fans sounded like they were trying to achieve low Earth orbit while the workload devoured 46 percent of a full battery charge in just 33 minutes.
The fact that you can run a 120-billion-parameter model locally on a thin laptop is still amazing. Just don’t wander too far from an outlet while you’re doing it.
Windows on Arm remains the big asterisk
RTX Spark’s other wrinkle is its Arm architecture. Windows on Arm is in a much, much better place than it used to be, with Microsoft’s Prism translation layer handling a huge amount of traditional x86 Windows software and native Arm support continuing to expand. Most of the time, you can simply use your computer without thinking about what instruction set lives underneath it. That’s significantly better than the state of Windows on Arm just a year or two back.
We’re not completely at “never think about it” territory yet, though. Mark ran into some software wrinkles during Surface testing, including needing a beta version of Adobe Premiere because the shipping version didn’t properly support RTX Spark’s GPU.
That shouldn’t scare everybody away, but I’d absolutely investigate your specific software stack before spending several thousand dollars on one of these machines, especially if your livelihood depends on specialized utilities, drivers, plug-ins, or some obscure Windows software written when Bill Clinton was president. RTX Spark is a first-generation platform doing some unusual things. Expect some first-generation growing pains.
So who should actually buy RTX Spark?
Mark Hachman / Foundry
After weeks of several staffers across PCWorld intensively testing this hardware, trying to find THE TRUTH about RTX Spark, I think the answer is pretty clear. Heavy AI developers and researchers should absolutely pay attention, especially if they regularly run models that overwhelm conventional GPU memory or spend serious money on cloud inference. Creative professionals experimenting heavily with local AI could also find a lot to like here, assuming their crucial software works properly on the platform.
Gamers should look elsewhere unless gaming is secondary to those AI workloads. The gaming performance is much better than I expected, but conventional GeForce laptops deliver more bang for your gaming buck, albeit in thicker form factors. And normal people who simply want a really fast premium laptop don’t need to spend RTX Spark money at all; there are phenomenal conventional laptops available for less. So much less.
That narrow audience doesn’t make RTX Spark any less fascinating. For years, PC hardware has mostly advanced by giving us faster versions of things we already had: faster CPUs, faster GPUs, faster SSDs. RTX Spark’s massive pool of unified memory lets a portable PC tackle workloads that previously didn’t make much sense on a portable PC at all.
My $7,000 Asus ProArt P16 certainly didn’t convince me that everybody needs an RTX Spark laptop. Quite the opposite. Most people absolutely don’t. Absolutely avoid RTX Spark if you can’t clearly articulate why having that sort of local AI prowess is crucial for you.
But if you’re one of the relatively small number of people who can put a giant Blackwell GPU and up to 128GB of unified memory to serious work, Nvidia has created something genuinely new here. And after spending decades testing PCs, genuinely new is pretty damned exciting.
Just save some of that precious RAM for the rest of us please, Nvidia.
