---
id: "f63f0781eeef1f19"
title: "Nvidia's new AI laptop runs nearly 80% slower on Linux — but only when it's plugged in"
url: "https://tomsguide.com/ai/nvidias-new-ai-laptop-runs-nearly-80-percent-slower-on-linux-but-only-when-its-plugged-in"
link: "https://tomsguide.com/ai/nvidias-new-ai-laptop-runs-nearly-80-percent-slower-on-linux-but-only-when-its-plugged-in"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T13:00:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "null"
tags: ["AI", "Laptops", "Computing"]
orgs: ["Nvidia", "OpenAI", "Google"]
topics: ["chips & infrastructure", "search & media", "models & research"]
content_source: "fulltext"
word_count: 1042
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/CxvjAewa4xS3be2otk3Neg-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia's new AI laptop runs nearly 80% slower on Linux — but only when it's plugged in

Tom's Guide · Amanda Caswell · 2026-11-05

Nvidia's new AI laptop runs nearly 80% slower on Linux — but only when it's plugged in
MindStudio shows that skipping the charger could speed things up
We all know that plugging in your laptop is supposed to make it faster, but new testing of an Nvidia-powered laptop found the exact opposite, with AI performance dropping by nearly 80% when running Linux.
The surprising discovery comes from MindStudio, which tested an MSI Prestige N16 Flip AI+ powered by Nvidia's RTX Spark platform. The team wanted to see whether Linux could run on the machine without sacrificing the performance available through Windows.
It could, but there was a major catch. When running OpenAI's GPT-OSS-120B model, the laptop generated 65.4 tokens per second on Windows. Running Linux directly on the same hardware while plugged into a charger brought that figure down to just 13.9 tokens per second.
That's a nearly 79% reduction in AI performance simply from changing the operating system. But even stranger, unplugging the laptop brought much of that performance back.
The surprising problem with Nvidia's AI laptop
Nvidia's RTX Spark platform is designed to bring powerful AI capabilities to laptops. The MSI laptop tested by MindStudio supports up to 128GB of unified memory, allowing users to run large AI models directly on their devices instead of relying on cloud services.
However, MindStudio found that the laptop's AI performance varied dramatically depending on whether it was running Windows or Linux.
Here's how the same AI model performed across the tested configurations:
Sign up to the Tom's AI Guide weekly newsletter summing up all the biggest AI news you need to know. Plus, analysis from our AI editors and tips on how to use the latest AI tools!
The performance gap showed up in other tests, too. Windows completed one AI workload in roughly eight minutes, while Linux took 37 minutes to finish the same task.
MindStudio initially considered whether overheating might be responsible, but temperatures stayed between 40 and 47 degrees Celsius. Instead, the team found that the GPU was running at much lower clock speeds under Linux.
On Windows, the GPU reached approximately 2.2 GHz. But when running Linux while plugged in, that speed dropped to around 780 MHz, helping explain the dramatic difference in performance.
Why plugging in makes things worse
The researchers traced the problem to an Nvidia component called Platform Controllers and Framework.
On Windows, this component manages how the laptop distributes power between its CPU and GPU. Linux doesn't currently have equivalent support for the system tested, leaving the GPU unable to reach its expected speeds when plugged in.
MindStudio tested that explanation by disabling the controller in Windows. Performance immediately dropped, and GPU clock speeds fell to approximately the same levels seen under Linux. Restoring the controller brought performance back.
The team also reported that the firmware's power-management information is encrypted, preventing Linux from accessing the settings needed to control the GPU properly. That helps explain the strangest discovery of all: when running Linux on battery power, the laptop produced roughly 61 to 67 tokens per second in separate testing. Plugging it in dropped performance to around 15 tokens per second. So, yea, the laptop actually performed substantially better when disconnected from its charger.
There's a workaround, but it involves Windows
The good news is that users who want Linux-based AI tools don't necessarily have to sacrifice performance. MindStudio found that Windows Subsystem for Linux, better known as WSL, delivered almost identical performance to running Windows directly.
That's because WSL uses the Windows driver system, including the power-management components that allow Nvidia's GPU to reach its full speed.
There are some limitations. The researchers had to adjust WSL's memory allocation to accommodate larger AI models. Installing Linux directly also required additional workarounds for hardware support and memory configuration.
For now, WSL appears to offer the better experience on the tested hardware.
What this means for Nvidia laptop buyers
Keep in mind that these findings are from one study and do not mean that every Nvidia-powered laptop will slow down when running Linux. The testing focused on a specific RTX Spark system, and the results haven't been independently replicated across other laptop models.
It's also important to distinguish these laptops from Nvidia's DGX Spark desktop, which runs Linux and performed substantially better in the same benchmark.
Still, the results raise questions about software support for a new generation of PCs designed to run powerful AI models locally.
For consumers considering an RTX Spark laptop specifically for Linux-based AI workloads, the operating system could make an enormous difference to the performance they actually get.
Until Nvidia provides equivalent power-management support for Linux, buyers may find that keeping Windows installed is the fastest option.
Tom’s Guide has reached out to Nvidia for comment and will update this story if the company responds.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds.
More from Tom's Guide
- Living near an AI data center might not hurt your home's value — here's what new research found
- ChatGPT has a clever new way to fight back against election deepfakes — I tried it and it actually works
- A few tech leaders are rebranding AI as ‘superintelligence’ — calling it that doesn’t make it accurate
Amanda Caswell is the AI Editor at Tom's Guide and one of today’s leading voices in AI and technology. 
A celebrated contributor to various news outlets, her sharp insights and relatable storytelling have earned her a loyal readership. Amanda’s work has been recognized with prestigious honors, including outstanding contribution to media.
Known for her ability to bring clarity to even the most complex topics, Amanda seamlessly blends innovation and creativity, inspiring readers to embrace the power of AI and emerging technologies.
As a certified prompt engineer, she continues to push the boundaries of how humans and AI can work together.
Beyond her journalism career, Amanda is a long-distance runner and mom of three. She lives in New Jersey.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
