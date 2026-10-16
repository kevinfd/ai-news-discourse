---
id: "cf72d6df7f51fa50"
title: "Windows Central review of RTX Spark, including local LLM benchmarks"
url: "https://windowscentral.com/hardware/nvidia/rtx-spark-review-benchmarks-2026"
link: "https://windowscentral.com/hardware/nvidia/rtx-spark-review-benchmarks-2026"
source: "Windows Central"
domain: "windowscentral.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T14:12:15Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["SkyFeistyLlama8"]
language: "en"
summary: "Absolutely everything I learned while testing RTX Spark for a week: It's a beast, but not at everything\nThe first RTX Spark PCs launch tomorrow, and I've spent the last week testing what this new chipset from NVIDIA is good at.\nRTX Spark is finally here. After years of rumors, NVIDIA has re-entered the Windows silicon game with the MediaTek N1X, a tailor-made 18/20-core SoC with 5,120 or 6,144…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Apple", "Intel", "Microsoft", "AMD"]
topics: ["chips & infrastructure", "agents & coding", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 3110
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6mqed/windows_central_review_of_rtx_spark_including/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Windows Central review of RTX Spark, including local LLM benchmarks

Windows Central · SkyFeistyLlama8 · 2026-10-15

Absolutely everything I learned while testing RTX Spark for a week: It's a beast, but not at everything
The first RTX Spark PCs launch tomorrow, and I've spent the last week testing what this new chipset from NVIDIA is good at.
RTX Spark is finally here. After years of rumors, NVIDIA has re-entered the Windows silicon game with the MediaTek N1X, a tailor-made 18/20-core SoC with 5,120 or 6,144 GPU cores, up to 128GB of unified memory, and a heck of a lot of power for apps, games, and AI experiences under the hood.
It's not every day that Windows gains a new silicon partner, which is why everyone seems to be involved with ensuring this launch goes as smoothly as possible. Microsoft has worked closely with NVIDIA on optimizing the Windows platform, especially for RTX Spark, and third-party app vendors like Adobe, Blender, anti-cheat software, and more have mobilized to optimize their products and frameworks for the new chipset.
But the big play with RTX Spark is on-device AI. LLMs and agentic workflows have become all the craze over the last year, and NVIDIA believes the RTX Spark is the first chipset for Windows that has been designed from the ground up for running local AI experiences locally and securely, without sacrificing performance.
NVIDIA has 6 hardware partners lined up to ship RTX Spark hardware starting this week, and all of them are aimed at the high-end content creator or developer crowd. NVIDIA has set its sights on competing head-to-head with the MacBook Pro, and is eager to win over AI developers who flocked to that platform thanks to Apple Silicon.
I've been testing out the top configuration of RTX Spark over the last week on a Surface Laptop Ultra, and here's what I discovered it's good at, and what it's not so good at. FYI, today's embargo only allows us to detail the RTX Spark's performance and benchmarks, not the Surface Laptop Ultra itself. So battery life, thermal performance, and laptop-specific variables are not included in this piece. That information will be shared in the full laptop review, coming soon.
NVIDIA RTX Spark Overview
If you're looking for a quick rundown of what RTX Spark is and how it compares, here's what you need to know:
RTX Spark is a powerful SoC with good CPU performance and great GPU performance. Its CPU is comparable to the Apple M4 Pro and Qualcomm's Snapdragon X2 Elite, with multi-thread performance being its stronger asset in the CPU department, though it trails behind the Apple M4 Max and Snapdragon X2 Elite Extreme.
All the latest news, reviews, and guides for Windows and Xbox diehards.
The GPU is the star of the show, with great performance thanks to its 6,144 GPU cores that deliver smooth framerates (with help from DLSS and framegen), faster rendering times, and very capable AI performance. Its quantized INT8 tensor execution, unified memory sharing, and computer vision acceleration easily leapfrog mobile discrete GPUs in its power class for AI workflows, which it excels at.
I don't believe RTX Spark is for everyone. It's very good at key things, and shines primarily for those who are knee-deep in local AI workflows and experiences. If you're not a mobile content creator, software developer, or utilize local LLMs often, RTX Spark probably isn't for you.
Mobile efficiency varies depending on power profile. The GPU is hungry and will drain power fast when at full pelt, but in day-to-day usage that only occasionally leans on the GPU, it should last the workday. The good news is, you should see the same performance regardless of plugged-in state.
Compared with most integrated Snapdragon, Intel, and AMD systems, RTX Spark is substantially faster in AI image generation and local inference, while matching or approaching dedicated RTX 4070/5060/5070 class GPU performance in most workloads outside of AI.
The latest generation of high-end Apple Silicon retains an advantage in peak single-thread CPU performance, but RTX Spark’s strength is its GPU, with TensorRT execution and high-speed memory providing advantages in diffusion, quantized models, and sequential data access.
NVIDIA RTX Spark CPU Performance
The RTX Spark CPU was co-designed by NVIDIA and MediaTek. The N1X, as it's known, comes in either 18- or 20-core configurations and is relatively efficient while delivering good performance. With that said, it's not leading in its class, leaving something to be desired when it comes to raw benchmarks.
In Cinebench 2026, the 20-core N1X achieved a single-core score of 558 and a multi-core score of 6,885. To put that into perspective, its single-core score beats the first-gen Snapdragon X Elite X1E-80-100 at 519, but falls short compared to Qualcomm's Snapdragon X2 Elite Extreme, which achieves a score of 662 for single-core. Multi-core fares better, with a score of 6,885, which is only just behind the X2 Elite Extreme and Apple M4 Max.
These scores do place it ahead of Intel's and AMD's latest flagship mobile workstation chips, but the chipset simply doesn't compete with Apple's latest Max chips, consistently trailing behind the Apple M4 Max and the M3 Ultra. This is a little disappointing given that the RTX Spark is directly targeting Apple Silicon.
It's a similar story with our Geekbench 7 results, achieving a single-core score of 2,718 and a multi-core score of 23,571. It's clear that multi-core performance is the N1X's stronger asset, competing with the likes of the Apple M4 Pro or Intel Core Ultra 9 285K, and is well ahead of the last-gen Snapdragon X Elite and Intel Lunar Lake, as it should be.
Outside of benchmarks, in day-to-day use the N1X feels fine. This isn't a slow CPU by any means, and will chew through even complex workflows with no sweat. Most day-to -day apps are Arm native these days, but for the few that do require Microsoft's Prism emulation layer, you won't even notice it. RTX Spark makes it so emulated apps feel just like native ones.
All our benchmarks were run with the Best Performance setting enabled, and in our tests we ran them a number of times in both plugged-in and unplugged states to see if there's any performance drop when away from a wall outlet. The good news is the RTX Spark delivers pretty much the same power regardless of plugged-in state, which mimics Apple Silicon.
NVIDIA RTX Spark GPU Performance
The star of the show with RTX Spark is the Blackwell RTX GPU with either 5,120 or 6,144 cores. We benchmarked the top-end, 6,144-core configuration for these benchmarks, and it does impress, outputting performance in workflows like video editing, model rendering, and gaming similar to an RTX 4070 or 5060, but in an efficient package with all-day battery life.
For what is essentially an integrated GPU, it outputs dedicated GPU performance in pretty much all workflows. But it really excels at AI workflows, especially when optimized for tensor and CUDA.
The 128GB configuration is set to split that memory evenly between system RAM and the GPU, meaning in our default configuration and for how we ran most of our benchmarks, the GPU had 64GB of video RAM to make use of. In this configuration, it's more than capable for most tasks, with the only exception being running AI models that surpass this size. In that situation, you can allocate more memory to the GPU so that it will fit.
In our 3DMark tests, we found that the RTX Spark performs similarly to an RTX 4070. It's very capable at 1440p gaming with high settings in most titles, though more demanding games will need to lean on DLSS and frame generation for smooth 60+ FPS gaming. In most titles we benchmarked, games ran without a hitch and looked great.
Gaming is not the main reason to buy an RTX Spark laptop, but it is an additional benefit. It's the first Windows on Arm platform that does gaming relatively well, supporting the usual breadth of gaming technologies and frameworks such as:
- Ray tracing
- DLSS 5
- Multi Frame Generation
- Neural Rendering
- Reflex
- G-SYNC
- RTX Remix
Most games run under emulation on RTX Spark, as the platform is Arm64, and most games are compiled for x86. However, in most titles, this isn't a problem. Most mainstream anti-cheat software is now compatible with Windows on Arm, and the Prism emulation layer has been tuned specifically for RTX Spark to ensure most games run without a hitch, though there are exceptions.
Some games, such as Red Dead Redemption 2, will require you to change settings to get them to run successfully. For example, by default Red Dead Redemption 2 was set to run with Vulkan, which caused it to crash at launch. Switching it to DirectX12 fixed this for me. Most games run without needing to change any settings first, however.
View Original
View Original
View Original
View Original
I tried Cyberpunk 2077, which runs pretty well right out of the box. The game analyzed my system and decided that Ray Traced Ultra settings were a perfect fit for the RTX Spark. Running at 1440p with frame gen enabled, the game was easily able to maintain 60fps while looking good doing it with these graphics settings enabled.
Shadow of the Tomb Raider also works great, but it takes quite a while to actually load up. But once the game is running and you're in-game, it looks great and runs well above 60fps at high settings at 1440p. Marvel's Spider-Man 2 and The Witcher 3 Remastered ran without a hitch, reaching close to 90fps in high settings at 1440p.
For content creators, RTX Spark is a great choice. Whether you are editing photos or rendering videos using apps like Adobe Photoshop and Premiere Pro, or rendering 3D environments in Blender, the RTX Spark is well suited for those tasks.
Adobe and NVIDIA say the Adobe Creative Cloud Suite has been optimized specifically for RTX Spark. These optimizations include:
- Photoshop on-device AI object removal
- Premiere Pro TensorRT acceleration
- Blender support for DLSS 4.5 Ray Reconstruction
When it comes to video rendering times, the RTX Spark trails the current-gen RTX 50 series GPUs. We benchmarked it against three other laptops with an RTX 5060, 5070 Ti, and 5080, in which it trailed the RTX 5060 in video rendering performance, finishing a few seconds later in most instances. In this benchmark, we ran Premiere Pro Beta, as that version includes necessary optimizations for RTX Spark.
Dedicated GPU performance can vary depending on laptop chassis size, cooling solution, and thermal envelope, which is why the 5070 Ti frequently trailed the 5060 in our testing.
The RTX Spark GPU is very performant and is capable of pretty much handling anything you'd want to throw at it on a mobile workstation. Where it really shines, however, is running local AI models directly on it. It's the reason NVIDIA built this platform to begin with, and it does this very well.
We ran several Procyon AI benchmarks to see how well the GPU performs when running on-device AI workflows. Text generation LLMs ran very fast, with Spark delivering responsive time-to-first-token results, including 0.27 seconds on Phi and 0.39 seconds on LLaMA3, but its sustained decoding rates trail higher-wattage discrete GPUs.
But quantized AI performance is where RTX Spark truly leads. In Stable Diffusion 1.5 INT8, the RTX Spark scored 11,294 and generated images in 2.77 seconds, substantially outperforming the tested RTX 5080, RTX 5070 Ti, and RTX 5060, on which we ran the same tests.
AI Workflows
The GPU is best suited for running large on-device AI models such as Qwen 3.8 27B, Gemma 4 31B, or even 120B-parameter models such as Nemotron or GPT-OSS.
NVIDIA is touting local agentic capabilities with this GPU, leaning on apps like Hermes Agent and OpenClaw to achieve this. We tested Hermes Agent, as OpenClaw failed to connect to the gateway once setup was complete.
The selling point of running LLMs and agents locally is that you are no longer constrained by usage limits or the amount of tokens you have available. When the AI runs locally, it's yours. You can run it for as long and as hard as you like.
It's also good for security and privacy reasons. You may have confidential documents, audio recordings, intellectual property that you need summarized or explained to you, and feeding that data to a cloud-based LLM or agent is giving that data away to the host.
With RTX Spark, you can feed whatever data or task you want to your local AI running off the GPU, and that data will never leave the device. You can build up your own personal agent that is capable of managing your local files, creating documents, making edits, and in some cases even controlling your PC.
Hermes Agent is a great tool for beginners, as it offers local AI compute experiences and makes setting it up a breeze. You open the app, choose to run AI locally, and it recommends the best model for the specs you have. Once downloaded, you're good to start chatting with your own AI locally.
Hermes Agent is particularly good at automating tasks. The first thing I did was tell it to clean up and organize my large, cluttered downloads folder. It moved images to my photos library, deleting any old executables, and organizing and categorizing PDFs and Word documents appropriately. It did all this without sending any of my data to the cloud, all processed by the GPU.
I also asked it to build me a basic website that included all my benchmark results so that I could refer back to them more easily. It ran that process entirely off my GPU, and came up with a pretty nice looking webpage design in the process. Zero cloud-based tokens used:
NVIDIA has even built MCP support into NVIDIA Broadcast and NVIDIA Control Panel, allowing you to hook it up to your local LLM and issue commands that allow it to configure your NVIDIA PC's settings.
Windows and RTX Spark
In addition to raw CPU and GPU performance, Microsoft has worked closely with NVIDIA to optimize RTX Spark for Windows 11. This partnership runs deep, and there are a lot of things going on behind the scenes that will aid the performance of Windows and support for apps on RTX Spark over the coming months and years.
For those unboxing a new RTX Spark laptop this fall, the Get Started app on Windows 11 will present a step that makes downloading and installing apps that can handle AI agents super easy. Hermes Agent will even go a step further and recommend a suitable model to download once up and running, meaning the user has to do zero research to get started.
With that said, I still find these recommended apps quite complex and convoluted. Many beginners will feel overwhelmed by these apps, especially OpenClaw, which I could not get working properly after it failed to open a gateway to allow the AI model to communicate with the OpenClaw chat interface.
Microsoft has optimized the system scheduler specifically for RTX Spark to squeeze out as much performance across Windows, menu flyouts, app launches, and more as possible. It has also made changes and enhancements to how Windows handles unified memory so that it's faster and more reliable at feeding that memory to where you need it.
TensorRT is now supported by Windows ML, and DirectX 12 has neural rendering support. The Prism emulation layer has also been tuned for RTX Spark, which results in emulated apps that simply do not feel like they are being emulated.
Microsoft is also keen to position Windows as the platform for local AI and agentic workflows. It has built safeguards and security into the Windows platform to ensure the local agents you run on Windows aren't capable of making severe changes or causing damage to your files, apps, and more.
This is a direct attempt at combating the sudden rise in local AI developers flocking to the Mac. Apple has made little optimizations to macOS to adopt and safeguard local AI and agentic workflows on that platform, whereas Microsoft is moving to make agents a native extension of the Windows platform.
RTX Spark is a Copilot+ PC certified chip, but you won't find any Copilot+ PC features at launch. Microsoft says it's working with NVIDIA to bring features like Windows Recall, Click To Do, and on-device Semantic Search to the RTX Spark platform in the coming months, which will run off the RTX Spark's 50 TOPS NPU.
Conclusion
RTX Spark is a super interesting chipset. It's forward leaning in a lot of ways, built on the Arm64 architecture that delivers serious performance and great efficiency. While its N1X CPU is just okay, its Blackwell RTX GPU really shines.
This is the first time we've seen RTX 4070-5070 level performance in an SoC that is this small and efficient. It's optimized for AI workloads, which is its strongest workflow by far. Quantized AI models run great, and with up to 128GB of unified memory, most mainstream models will fit entirely on the GPU without a hitch.
It's also great for content creators, and is very capable at gaming also. But at the prices that these devices are launching at, I think most people would be better served getting an Intel or AMD laptop with a dedicated NVIDIA GPU instead, as these often cost less than the cheapest RTX Spark laptops right now.
But if your workflow involves running AI models locally all day, software development, or complex data crunching and source code management, the RTX Spark is one of the better choices in the Windows space right now, especially for laptops that are thin-ish and (relatively) lightweight.
These RTX Spark laptops are more efficient and portable than typical laptops with a dedicated NVIDIA GPU, which is one of the key benefits of an SoC like this. The power this GPU outputs, for what is essentially integrated graphics, should not be understated.
Of course, just how efficient RTX Spark is will depend entirely on the hardware you choose to buy, as OEMs are free to feed the GPU more or less power depending on the chassis and thermal envelope. Keep that in mind.
Benchmarks
All benchmarks ran on RTX Spark 20-core CPU configuration with 128GB RAM and 6,144 GPU cores. All tests ran connected to power with Best Performance profile enabled, unless stated otherwise. We are still running benchmarks and new tests, and will update accordingly.
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
