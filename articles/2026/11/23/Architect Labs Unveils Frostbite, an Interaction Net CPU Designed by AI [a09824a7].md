---
id: "a09824a7f477e08e"
title: "Architect Labs Unveils Frostbite, an Interaction Net CPU Designed by AI"
url: "https://marktechpost.com/2026/11/23/architect-labs-frostbite-ai-designed-cpu-interaction-nets"
link: "https://marktechpost.com/2026/11/23/architect-labs-frostbite-ai-designed-cpu-interaction-nets"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T10:05:47Z"
published_date: "2026-11-23"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Architect Labs has introduced Frostbite , an AI-designed CPU with a new instruction set built around interaction nets. The company states that its AI agents designed Frostbite from interaction net theory down to final GDS. In pre-silicon tests, it reports 4.59x the performance per watt of a modern in-order CPU core. \n\n TL;DR \n\n Size: 1 quad (2×2 tiles) plus 4 L3 nodes takes 0.792 mm² on 7 nm. No…"
tags: ["AI Infrastructure", "AI Shorts", "Artificial Intelligence", "Editors Pick", "Staff", "Tech News", "Technology"]
orgs: ["Hugging Face"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 973
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Architect Labs Unveils Frostbite, an Interaction Net CPU Designed by AI

MarkTechPost · Michal Sutter · 2026-11-23

Architect Labs has introduced Frostbite , an AI-designed CPU with a new instruction set built around interaction nets. The company states that its AI agents designed Frostbite from interaction net theory down to final GDS. In pre-silicon tests, it reports 4.59x the performance per watt of a modern in-order CPU core. 

 TL;DR 

 Size: 1 quad (2×2 tiles) plus 4 L3 nodes takes 0.792 mm² on 7 nm. No parameter count (it is a CPU). 

 Runs on: Pre-silicon only. Final GDS closes at 500 MHz on 7 nm. An FPGA-hosted playground is planned. 

 Performance: 4.59x perf per watt (geomean, 25 workloads) and 8.77x perf per area vs 1 in-order core. 

 Best: 23.12x perf per watt on conv2d. 

 What is Frostbite? 

 Frostbite is a CPU from Architect Labs that executes programs as interaction nets in hardware. Programs are written in Vine , a Rust-like language, and compiled to an IR called Ivy. The chip is a mesh of tiles, each with its own small local memory. The launch post on X states that the AI agents co-designed the ISA and chip architecture given only interaction net theory. 

 How do interaction nets enable parallelism? 

 Interaction nets were introduced by Yves Lafont at POPL 1990 . A program is a graph of nodes. Computation rewrites pairs of nodes connected through their ports. Each node has 1 principal port, so active pairs never overlap and can fire in any order. Every value is used exactly once, so there is no shared mutable state to guard. 

 A 5-queens net has 3,183 interactions and a 262-step critical path. About 12 interactions are ready per step. Software runtimes such as HVM2 already run interaction nets on GPUs. Frostbite moves the model into the ISA itself. 

 How is the Frostbite hardware organized? 

 The chip is built from tiles grouped into 2×2 quads. Each tile has front end, engine, memory and system blocks. A runtime domain adds a frame manager, scheduler, work queue and outlet. Its ISA adds wide bundles, hardware loop counters, streams, and ops that take, peek or copy values. 

 Each tile runs its own queued work first. If idle, it takes work from a neighbor. If none is found, it goes inactive to save power. The company says this work stealing emerged during design and was not hand-specified. 

 How did AI agents design the chip? 

 Agents first synthesized papers and built Python models. Their output was a 141-page PDF. It was deleted after the first RTL pass because its estimates were physically unrealistic. 

 The research team then used ASL, an in-house, machine-checkable specification language. ASL is the single source of truth for the ISA, the Arcmodel system model, RTL and verification. The spec translates to Lean , and the project passed 800k lines of Lean. 

 Arcmodel first diverged from RTL by almost 250% in the worst case. An automated fitting pipeline cut that to under 6% worst case and about 1.5% median. Arcmodel simulates the full chip 660x faster than RTL. Across 4 searches and an ablation round, agents tried 58 ideas and kept 37. The design targets 7 nm, timing at 800 MHz in synthesis and 500 MHz in final GDS. 

 It follows Redwood , an edge AI accelerator the company announced in August 2026. 

 How does Frostbite perform on benchmarks? 

 The baseline is ‘TCPU,’ 1 core of a modern dual-issue, in-order superscalar CPU. Architect Labs does not name it, citing legal reasons. 1 Frostbite quad plus 4 L3 nodes occupies 0.792 mm². TCPU occupies 0.895 mm² on the same process. 

 Across 25 workloads, geomean performance per watt is 4.59x. The 10-workload search set scores 6.02x, and the 15-workload held-out set 3.83x. Results range from 23.12x on conv2d to 1.15x on fib. Performance per area averages 8.77x. 

 Fetch, decode and issue fall from 27% of TCPU energy to 6% in a quad. The on-chip network and scheduler take 26% instead. The fft, radixsort and LU kernels follow SPLASH-2 , scaled down 64x. 

&

 How does Frostbite compare with other approaches? 

 Metrics Frostbite TCPU baseline HVM2 Arm Cortex-A55 (same core class, not confirmed as TCPU) Type Research CPU, new ISA Commercial CPU core (name undisclosed) Software runtime Commercial CPU core Compute model Interaction nets in hardware Conventional ISA Interaction combinators on CPU/GPU ARMv8.2-A Pipeline / issue Tiled mesh, spatial pipelining Dual-issue, in-order Not applicable Dual-issue, in-order, 8-stage Unit compared 1 quad (2×2 tiles) + 4 L3 nodes 1 core Not applicable 1 core Area 0.792 mm² 0.895 mm² Not applicable Not disclosed Process 7 nm Same process Runs on existing chips Varies by licensee Clock 500 MHz (final GDS) Not disclosed Host dependent 1.25 to 2.31 GHz Parallelism source Program graph, work stealing Instruction-level, 2 slots Up to 32,768 GPU threads Instruction-level, 2 slots Headline number 4.59x perf/watt vs TCPU (pre-silicon) 1.0x baseline ~74,000 MIPS on RTX 4090 Not disclosed Status Pre-silicon, GDS Shipping silicon Open source on GitHub Shipping since 2017 

 Key Takeaways 

 Frostbite runs interaction nets in hardware, with no threads or locks. 

 AI agents took the design from theory to 7 nm GDS. 

 4.59x perf per watt geomean, but 3.83x on held-out workloads. 

 Best case 23.12x (conv2d), worst case 1.15x (fib). 

 Pre-silicon only, against an undisclosed baseline core. 

 Check out the full Frostbite technical post , the Vine language docs and Lafont’s original paper . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Architect Labs Unveils Frostbite, an Interaction Net CPU Designed by AI appeared first on MarkTechPost .
