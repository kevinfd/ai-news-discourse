---
id: "20b2c538903292e3"
title: "Why AI Data Center Compressors Need to Work Efficiently at Both Ends of the Operating Range"
url: "https://datacenterfrontier.com/sponsored/article/55413314/why-ai-data-center-compressors-need-to-work-efficiently-at-both-ends-of-the-operating-range"
link: "https://datacenterfrontier.com/sponsored/article/55413314/why-ai-data-center-compressors-need-to-work-efficiently-at-both-ends-of-the-operating-range"
source: "Data Center Frontier"
domain: "datacenterfrontier.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-20T17:00:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: []
language: "en"
summary: "Experts from the Research Institute at Midea Building Technologies, explain how a dual-rotor compressor architecture addresses the efficiency and continuity challenges that ..."
tags: []
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "business & funding", "safety & ethics"]
content_source: "fulltext"
word_count: 858
paywalled: false
image: "http://www.bing.com/th?id=ONUT.mJUeC7xAWrnRUzDGr5EePQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Why AI Data Center Compressors Need to Work Efficiently at Both Ends of the Operating Range

Data Center Frontier · 2026-10-20

Why AI Data Center Compressors Need to Work Efficiently at Both Ends of the Operating Range
At the OCP Global Summit 2026, we presented a compressor architecture designed around a problem that does not get enough attention: what happens when the cooling plant is not running at peak load.
Most data center cooling conversations focus on peak capacity. But most cooling plants spend a significant share of their operating hours nowhere near it. Mild weather, seasonal transitions, and cold-plate supply temperatures rising toward 45°C push the system toward low-lift conditions, where the pressure ratio across the compressor is low but refrigerant flow remains high. This is where conventional compressor architectures lose their efficiency advantage, and where operators quietly burn energy they do not need to. As the industry moves toward air-cooled systems to reduce water dependence, the compressor faces a wider operating envelope than ever before.
Conventional two-stage centrifugal compressors lock both impellers to a single shaft speed, and at their design point they perform well. But the fixed speed ratio between stages limits how precisely the pressure split can be optimized, and at low lift near the free-cooling boundary, pushing high refrigerant flow through two compression stages when only one is needed creates parasitic losses at exactly the operating points where the plant spends much of its time.
Decoupling the Rotors
The architecture we presented takes a different approach. Instead of coupling both impellers to a single shaft, the design uses two independent magnetic-bearing rotors, each driven by its own motor and variable-speed drive. The two stages can run at different speeds, and the second stage can be isolated entirely when it is not needed.
This gives operators two distinct operating regions. Under high ambient temperatures, both stages run together with independently tuned speeds, improving stage matching and peak isentropic efficiency by 2% to 3% over a coupled-speed reference. Near the free-cooling threshold, integrated bypass valves switch the system to single-stage operation, eliminating redundant compression work. At representative duty points, this reduces compressor power from 80 kW to 48 kW at the same cooling capacity, a 40% reduction, while improving low-lift efficiency by up to 15% and increasing usable low-lift flow by 70%.
At a pressure ratio of 1.6 and 22% of reference inlet flow, the architecture reaches 81% isentropic efficiency without inlet guide vanes, compared with 73% for a coupled-speed compressor fitted with inlet guide vanes.
Keeping Cooling Continuous During Mode Transitions
For facilities that prioritize refrigerant-pump free cooling backed by mechanical cooling, the transition between modes is where things can go wrong. In liquid-cooled AI environments, even brief interruptions can trigger server thermal throttling or downtime.
The risk during a mechanical-to-free-cooling transition is well understood: rapid depressurization can cause stored liquid to flash at the pump inlet, starving flow and creating a transient capacity gap. The independent-speed architecture addresses this by preconditioning the refrigerant in single-stage mode before pump takeover, reducing inlet mixture volume by 78.4% compared with a direct two-stage-to-pump handover.
The reverse transition carries its own risk. Conventional compressors require an iterative startup sequence, slowing condenser fans to raise condensing pressure before the compressor can reach its operating envelope. Single-stage startup eliminates that delay: the compressor begins operating at a low pressure ratio and builds capacity before ramping up to the second stage, while also supporting faster restarts after power restoration.
Fitting Two Shafts into One Footprint
A conventional dual-shaft arrangement would be approximately 25% longer than a single-shaft unit, and in space-constrained air-cooled chillers, that extra length comes directly out of the space available for heat exchangers, fans, and service access. The architecture we developed maintains the axial footprint of a conventional single-shaft compressor by placing outboard magnetic bearings inside volute recesses and combining seals, sensors, and backup bearings into integrated function units, alongside compact motors rated up to 70 kW at 41,000 rpm.
At the OCP Global Summit 2026, our compressor technology received the “2026 GW-Scale Open AIDC Excellent Technical Presentation Award,” recognizing its contribution to more efficient and reliable thermal architectures for next-generation AI data centers.
From Compressor Innovation to Full-Chain Cooling
A compressor is only one part of the cooling system. Clivet brings this core cooling-source technology into a full-chain liquid cooling approach that spans cooling sources, high-capacity coolant distribution units (CDUs), fan walls and terminal units. Designed to prioritize free cooling while retaining dependable mechanical-cooling backup, this integrated portfolio supports scalable thermal management across different climates and AI infrastructure requirements.
At this year’s OCP Global Summit, Midea also appeared in the list of participating companies in the NVIDIA MGX ecosystem. The inclusion highlights Midea’s growing role in the broader AI computing infrastructure ecosystem, where effective thermal management increasingly depends on coordination across equipment, systems and industry platforms.
As AI facilities move toward gigawatt-scale computing, we see the next step as bringing core cooling innovations together with system-level engineering and open ecosystem collaboration. Building on Midea and Clivet’s “equipment + systems + ecosystem” approach, our goal is to help deliver more efficient, reliable and sustainable cooling infrastructure for the next generation of AI data centers.
For more information about Clivet's liquid cooling portfolio for AI data centers, visit www.clivet.com.
