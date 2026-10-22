---
id: "a6ca975a8f2cf5b7"
title: "Oblivion Remastered Mod Built Using Claude AI Boosts FPS By Over 40% And Drastically Reduces Stuttering Without Sacrificing Visual Quality"
url: "https://wccftech.com/oblivion-remastered-mod-built-using-claude-ai-boosts-fps-by-over-40-and-drastically-reduces-stuttering-without-sacrificing-visual-quality"
link: "https://wccftech.com/oblivion-remastered-mod-built-using-claude-ai-boosts-fps-by-over-40-and-drastically-reduces-stuttering-without-sacrificing-visual-quality"
source: "Wccftech"
domain: "wccftech.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T19:27:31Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["PikaPikaDude"]
language: "en"
summary: "The Elder Scrolls IV: Oblivion Remastered has struggled with CPU bottlenecks, inconsistent frame rates and frame times, not to mention traversal stuttering since launch, especially on NVIDIA GPUs. However, one particularly dedicated fan has apparently managed to address many of these issues with the help of Anthropic's Claude AI, achieving some rather impressive performance improvements without…"
tags: ["r/singularity"]
orgs: ["Anthropic", "OpenAI", "Google", "Nvidia", "AMD"]
topics: ["chips & infrastructure", "products & launches", "models & research", "search & media"]
content_source: "fulltext"
word_count: 536
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xbwun6/oblivion_remastered_mod_built_using_claude_ai/"
score: null
comments: null
community: "r/singularity"
---

# Oblivion Remastered Mod Built Using Claude AI Boosts FPS By Over 40% And Drastically Reduces Stuttering Without Sacrificing Visual Quality

Wccftech · PikaPikaDude · 2026-10-21

The Elder Scrolls IV: Oblivion Remastered has struggled with CPU bottlenecks, inconsistent frame rates and frame times, not to mention traversal stuttering since launch, especially on NVIDIA GPUs. However, one particularly dedicated fan has apparently managed to address many of these issues with the help of Anthropic's Claude AI, achieving some rather impressive performance improvements without compromising the game's visual fidelity.
Reddit user LTSharpe recently shared his experience, explaining how even upgrading from a GeForce RTX 2070 SUPER to a Radeon RX 9070 XT failed to resolve the game's performance problems on his Ryzen 7 5800X system. Frustrated by the situation, he turned to Claude Opus 5.5, which reportedly identified several fundamental inefficiencies within the game's code.
What followed was roughly two and a half weeks of AI-assisted reverse engineering, profiling, and optimization. Despite having no professional software development background, LTSharpe directed Claude through the process, ultimately producing approximately 40 engine-level optimizations packaged into an open-source mod called Oblivion Remastered Performance Fix.
Interestingly, many of the identified problems stemmed from inefficient CPU utilization. For example, the game was reportedly rebuilding its sun and moon lighting systems every frame, even when nothing had changed. Other bottlenecks included redundant memory allocations, DirectX 12 command preparation largely confined to a single thread, and expensive world-streaming operations that could stall entire frames.
The mod tackles these issues through improved multithreading, more efficient memory management, and better distribution of expensive operations across multiple frames. Crucially, these changes reportedly preserve the original graphics quality, including complex Nanite Virtualized Geometry, Lumen ray-traced lighting, Virtual Shadow Maps, high draw distances, and other visual settings.
The performance improvements are particularly noteworthy. In an Imperial City flythrough at 4K output with FSR Performance and Frame Generation enabled, average FPS increased from 72 to 102 (+41%), while 1% lows improved from 33 to 45 FPS. The number of traversal hitches exceeding 50 ms also dropped from 19.5 to just 4.8 per run.
Meanwhile, another benchmark in Cheydinhal demonstrated an increase from 64 to 91 FPS (+43%), with 1% lows climbing from 50 to 68 FPS. A separate test without FSR Frame Generation saw 1% lows improve from 26 to 43 FPS, illustrating the mod's potential benefits beyond simply increasing average frame rates.
Additional improvements include reduced loading-related stutters, faster menu interactions, several crash fixes, and optimized FSR Frame Generation scheduling. The mod also introduces support for AMD's newer machine-learning-based FSR Frame Generation on Radeon RX 9000 GPUs, provided the appropriate FSR 3.1.4 library is installed.
The developer has published the v1.0.0 beta release, alongside its source code and reproducible benchmarking tools. Installation involves extracting the supplied files into the game's directory.
Of course, these impressive results currently come from testing primarily on a single Ryzen 7 5800X/RX 9070 XT system. Performance improvements will vary depending on hardware and whether the game is CPU- or GPU-limited, while broader compatibility remains to be established.
Nevertheless, this is a fascinating demonstration of what AI-assisted development can accomplish, particularly when applied to optimizing existing games. Hopefully, subsequent releases and community testing will confirm similarly impressive results across a wider range of PC configurations.
News Source: r/ChatGPT subreddit
Follow Wccftech on Google to get more of our news coverage in your feeds.
