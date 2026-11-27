---
id: "02aad8ee60b59f7e"
title: "[2026/11/27 AI News] Google \"Cogentic\", OpenAI, and Anthropic Compete in Proving Hard Problems — Direct Hit from US-China AI Regulations and Anti-Distillation Measures, plus ..."
url: "https://note.com/gifted_snail5503/n/nc7287a0edefc?hl=en"
link: "https://note.com/gifted_snail5503/n/nc7287a0edefc?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-27T01:24:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Sabafish"]
language: "en"
summary: "Line Summary A flurry of advances emerged at the intersection of AI and mathematics, including the release of six theoretical papers via Google's multi-agent proof system \"Cogentic\", OpenAI's proof of ..."
tags: []
orgs: ["OpenAI", "Anthropic", "Google", "China", "Nvidia", "Meta", "Alibaba", "Intel"]
topics: ["models & research", "chips & infrastructure", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1169
paywalled: false
image: "http://www.bing.com/th?id=ONUT.3wp6I7B3lR8SYfj6c1USug&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [2026/11/27 AI News] Google "Cogentic", OpenAI, and Anthropic Compete in Proving Hard Problems — Direct Hit from US-China AI Regulations and Anti-Distillation Measures, plus ...

note · Sabafish · 2026-11-27

[2026/11/27 AI News] Google "Cogentic", OpenAI, and Anthropic Compete in Proving Hard Problems — Direct Hit from US-China AI Regulations and Anti-Distillation Measures, plus the Arrival of a 5.9GB 27B Model
This Morning's 3-Line Summary
- A flurry of advances emerged at the intersection of AI and mathematics, including the release of six theoretical papers via Google's multi-agent proof system "Cogentic", OpenAI's proof of the matrix multiplication exponent ω=9/4, and Anthropic's compression down to a 300,000-line Lean proof.
- US semiconductor regulations against China (requiring permits for computing resources in overseas data centers) and strengthened anti-distillation measures by OpenAI and Anthropic are causing delays in the development schedules of Z.AI's "GLM-5.5" and Moonshot AI's "Kimi K4".
- PrismML released "Ternary Bonsai 2.5 27B," which compresses a 27B model down to 5.9GB using ternary (-1/0/+1) quantization, presenting a new option for running local agents on laptops.
This Morning's Featured Topic (Deep Dive)
Google's "Cogentic", OpenAI, and Anthropic: Breakthroughs in Formal Proofs and Computational Theory
- Overview & Technical Highlights: From November 25 to 26, 2026, a series of announcements regarding AI-driven proofs and formal verification in pure mathematics and computational complexity theory attracted significant attention within the developer community ( Agent Tools Today 11/26 Edition ). Google Research published six theoretical papers in a single commit using its Gemini 4-based multi-agent proof system "Cogentic", presenting a deterministic sub-exponential time integer factorization algorithm that eliminates the smoothness assumption upon which the Number Field Sieve (NFS) relied. Additionally, OpenAI published a lower bound proof for the matrix multiplication exponent `ω = 9/4` complete with a Lean proof, and Anthropic's Luke Sernau released a repository (`https://www.google.com/search?q=github.com/lsernau/grh-lean`) that refactored into roughly 300,000 lines (about 1/50th) the approximately 17-million-line Lean 4 formal proof of the Generalized Riemann Hypothesis (GRH) that made headlines last week.
- Differences from Conventional Approaches & Breakthroughs:
- Previous Challenges: Even when LLMs generated advanced mathematical proofs, major bottlenecks remained: the results often turned into redundant proof code spanning tens of millions of lines that humans could not fully verify, or lingered as unverified preprints prior to peer review, leaving their correctness uncertain.
- The Current Approach: Anthropic's compression to 300,000 lines signifies the introduction of software engineering lifecycles—specifically "codebase refactoring, review, and line-count budget management"—into mathematical discovery using formal proof languages (Lean 4). Meanwhile, Google's Cogentic was released after undergoing prior peer review by human experts, and alongside OpenAI's release with an accompanying Lean certificate, a new research pipeline is emerging: "AI derives, and formal verifiers or human experts audit and compress."
- Impact on Practice and Application: While the integer factorization paper represents a significant theoretical computer science advancement that does not immediately break current TLS/RSA cryptography, it demonstrates that AI can discover unknown, efficient structures and rigorous proofs in areas such as Fast Fourier Transforms (FFT), optimization algorithms, and formal verification of mission-critical software.
- Adoption Status & Future Outlook: `leanprover-community/riemann-hypothesis` broke into the top 10 on GitHub Trending (reaching 1,302 stars), and an ecosystem where mathematicians, AI agents, and engineers collaboratively maintain and verify formal proofs on GitHub is rapidly expanding.
Other Notable AI News
1. US Overseas Data Center Regulations and "Anti-Distillation" Measures Directly Hit Chinese AI Development — Causing Delays for Z.AI and Moonshot
- Overview: According to a Reuters report on November 27, 2026, new US Department of Commerce regulations that took effect on November 19 (requiring permits to utilize computing clusters exceeding the equivalent of 750 NVIDIA H100s even in data centers outside the US, as well as restricting advanced chip exports to countries like Malaysia and Singapore), combined with tightened measures by OpenAI and Anthropic to block unauthorized "distillation," are delaying the development plans of Chinese firms. Z.AI (Zhipu) now expects the launch of its next-generation 3-trillion-parameter flagship "GLM-5.5" to slip from this year into Q1 2027 or later, while Moonshot AI estimates that if its access to overseas compute resources is cut off, the release interval for flagship models like the upcoming "Kimi K4" will double from the previous 6 months to over a year.
- Key Takeaways: The two main pillars that have allowed Chinese AI companies to develop competitive models at low cost—"procuring GPUs in overseas clouds" and "distillation using outputs from cutting-edge US models"—are both beginning to face constraints simultaneously. In addition to exploring European clouds and domestic Chinese chips, the fact that Moonshot AI is shifting its training data sources away from OpenAI/Anthropic toward the latest models from Google and Meta represents a critical shift that could sway the geopolitical landscape of future model development competition.
2. "Ternary Bonsai 2.5 27B", a 27B Model Ternary-Quantized to 5.9GB, and the Pure Assembly OS "Bare Metal Qwen" Generate Buzz
- Overview: On November 25–26, 2026, PrismML released "Ternary Bonsai 2.5 27B," which compresses all weights of a Qwen3.8-27B base into ternary values of `-1 / 0 / +1`, shrinking what would be an approximately 54GB model in FP16 down to just 5.9GB. It allows loading a 128k context into memory on laptop-class local devices, boasting support for both NVIDIA and Intel hardware. Additionally, on the 26th, "`alesha-pro/llm.asm`", which runs Qwen3-0.6B purely on x86-64 assembly (a 12KB inference engine and a 24KB bootable OS) without using any C language or libc, also attracted attention on Hacker News.
- Key Highlights: While giant cloud-side models face the walls of computational resources and safety reviews, in the local LLM space, approaches that push the inference footprint to the absolute minimum—such as "keeping a 27B-class agent resident on a laptop via ternary quantization" and "bare-metal inference that even eliminates the OS layer"—are becoming a reality.
Today's Editorial Note: The Current State of AI Trends
Today's news indicates that the evolution of AI has entered a new phase in both "computational resources/geopolitical constraints" and "software engineering/extreme efficiency." While U.S. regulations on overseas data centers and distillation countermeasures raise physical and institutional hurdles for giant model development, mathematical research by Google, OpenAI, and Anthropic is establishing methods to refactor and verify AI-generated proofs with Lean, and ultra-small footprint technologies like 5.9GB 27B models and 24KB assembly OSs are emerging in the local domain. We are transitioning from an era solely focused on scaling to one centered on how to verify, compress, and fully utilize intelligence under constraints.
Today's In-Depth Articles (Detailed Topics)
- Paradigm Shift in Development Brought by AI-Driven Proofs and Formal Verification in Mathematics and Theoretical Computer Science
- How the Double Blockade of Computational Resources and "Distillation" Changes AI Development Assumptions: Unpacking Next-Gen Model Strategies from Z.AI and Moonshot Delays
- A 27B Model Down to Just 5.9GB, Plus Pure Assembly Inference Requiring No OS: A New Era for Local LLMs Forged by Extreme Lightweighting
For Those Who Want to Receive the Latest AI News by Email Every Morning
We also deliver a free newsletter (Substack edition) providing the same content as this article straight to your inbox every morning. Please consider subscribing as well.
Subscribe to the free Substack edition (https://sabafish38.substack.com/)
#AINews #GenerativeAI #GoogleCogentic #OpenAI #Anthropic #Lean4 #FormalProofs #SemiconductorRegulations #LocalLLM #LatestTech
