---
id: "d51f496c409c266f"
title: "IBM Announces IBM Quantum Nighthawk r3: A New Processor to Support 10k Quantum Operations on 520 Programmable Qubits"
url: "https://marktechpost.com/2026/11/12/ibm-quantum-nighthawk-r3-520-qubits-1040-qubit-system-2027"
link: "https://marktechpost.com/2026/11/12/ibm-quantum-nighthawk-r3-520-qubits-1040-qubit-system-2027"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T08:42:21Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Michal Sutter"]
language: "en"
summary: "IBM has announced IBM Quantum Nighthawk r3 , its next superconducting quantum processor. It is designed to run 10,000 quantum operations accurately across 520 programmable qubits. In 2027, IBM plans to link 2 r3 chips into a single 1,040-qubit system. For developers, the announcement is speed. The current Nighthawk r2 already runs workloads up to 19x faster than IBM’s earlier processors. \n\n…"
tags: ["AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Hardware", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["IBM", "Google", "Hugging Face"]
topics: ["chips & infrastructure", "products & launches", "agents & coding", "business & funding"]
content_source: "summary"
word_count: 904
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# IBM Announces IBM Quantum Nighthawk r3: A New Processor to Support 10k Quantum Operations on 520 Programmable Qubits

MarkTechPost · Michal Sutter · 2026-11-12

IBM has announced IBM Quantum Nighthawk r3 , its next superconducting quantum processor. It is designed to run 10,000 quantum operations accurately across 520 programmable qubits. In 2027, IBM plans to link 2 r3 chips into a single 1,040-qubit system. For developers, the announcement is speed. The current Nighthawk r2 already runs workloads up to 19x faster than IBM’s earlier processors. 

 TL;DR 

 Size: Nighthawk r3: 520 programmable qubits, 2,034 physical qubits, 10 l-couplers. Nighthawk r2 (live today): 120 programmable qubits, 218 couplers. 

 Runs on: IBM Quantum Platform cloud (r2 as ibm_phoenix ). Superconducting chips in dilution refrigerators, paired with laptop-to-supercomputer classical compute. 

 Performance: r2 executes 100,000+ circuits per second, about 25x Heron, with Heron-class gate fidelity. 

 Best: Up to 19x speedup over earlier IBM processors on partner workloads; E.ON reports 15x. 

 Worst: r3 is a design, not shipping hardware. Chip-to-chip links average 99% state transfer fidelity, short of the 99.9% target. 

 Bottom line: Best: real throughput gains on a cloud chip you can use now. Worst: the 1,040-qubit system is a 2027 plan, not a result. 

 What is IBM Quantum Nighthawk? 

 Nighthawk is IBM’s square-lattice processor family built for quantum advantage workloads. Most qubits connect to 4 nearest neighbors, versus 2 or 3 on earlier designs. That connectivity lets circuits express more entangling structure with fewer swap operations. 

 The current production chip is Nighthawk r2 . It has 120 programmable qubits, 218 couplers and 120 reset elements. That is 458 physical quantum elements in total. 

 How does Nighthawk r2 get 25x more throughput? 

 The bottleneck was qubit reset. Heron uses conditional reset: measure, then flip any qubit found in the excited state. That method cannot fix leaked qubits, so the chip idles for hundreds of microseconds between shots. 

 Nighthawk r2 replaces this with a dissipative reset gadget per qubit. A tunable coupler links each qubit to a cold environment on demand. This drops effective T1 from about 200 microseconds to roughly 25 nanoseconds. Idle time between runs falls to as little as 1 microsecond. 

 The result is 100,000+ circuits per second. Heron manages roughly 4,000. IBM also reports about 25x lower initialization error, while neighbors stay undisturbed. 

 What speedups are partners reporting? 

 According to IBM, clients have run 34 billion circuits on Nighthawk r2 so far. The figures below are self-reported by IBM and its partners. 

 E.ON: 15x speedup in quantum machine learning for energy grid optimization, versus Heron. 

 Oak Ridge National Laboratory: 12x speedup on a magnetic materials simulation matching neutron scattering data. 

 Algorithmiq: circuits ran 8x faster than the original Heron experiment. IBM estimates tensor-network methods need 240x more memory to match. 

 Q-CTRL: a 60-qubit fermionic simulation with 4,497 two-qubit gates. Runtime fell from 4 minutes 25 seconds to 23 seconds. Deviation from the Heron r3 baseline stayed under 1%. 

 IBM also reports accurate observable estimation on circuits with 7,500+ gates, a 2026 roadmap milestone. 

&&

 What changes in Nighthawk r3? 

 Nighthawk r3 keeps r2’s square lattice and fast operations. It scales to 520 programmable qubits from 2,034 physical qubits. It adds 10 chip-to-chip interconnects called l-couplers. 

 Those links are the path to 1,040 qubits. IBM connected 2 Nighthawk r1 chips with 4 l-couplers, each using an 80 cm cable. State transfer fidelity reached up to 99.3%, averaging 99%. IBM also linked 2 cryogenic modules , reaching below 15 millikelvin in under 5 days. 

 How does IBM Quantum Platform mix quantum and classical compute? 

 IBM Quantum Platform now runs HPC and quantum jobs in one managed environment. Users can attach classical compute from a laptop, a supercomputer or the platform itself. 

 IBM and RIKEN reran a sample-based quantum diagonalization workflow roughly 5x faster with 100x more computations. Cleveland Clinic and RIKEN processed 608 million samples 33x faster with workflow automation. Pulse-level controls are also available for error correction research. 

 How does Nighthawk compare with other quantum processors? 

 Spec IBM Nighthawk r2 IBM Nighthawk r3 (planned) IBM Heron r3 Google Willow Quantinuum Helios Qubit type Superconducting Superconducting Superconducting Superconducting Trapped ion Programmable qubits 120 520 156 105 98 Physical elements 458 2,034 physical qubits Not disclosed Not disclosed Not disclosed Connectivity Square lattice, 4 neighbors Square lattice + 10 l-couplers 2 to 3 neighbors Avg 3.47 All-to-all Circuit throughput 100,000+ circuits/s Not disclosed ~4,000 circuits/s Not disclosed Not disclosed Accurate circuit size 7,500+ gates 10,000 operations (target) Not disclosed Not disclosed Not disclosed 2-qubit gate fidelity Heron-class (no figure) Not disclosed Not disclosed Not disclosed 99.921% Availability IBM Quantum Platform 2027 (2-chip system) IBM Quantum Platform Not disclosed Not disclosed 

 Key Takeaways 

 Nighthawk r3 targets 10,000 operations on 520 programmable qubits. 

 2 linked r3 chips should form a 1,040-qubit system in 2027. 

 Nighthawk r2 runs 100,000+ circuits per second, about 25x Heron. 

 Partners report up to 19x speedups across 34 billion circuits. 

 Chip-to-chip links average 99% fidelity, still below the 99.9% goal. 

 Check out the IBM press release , the Nighthawk r2 technical blog and the l-coupler paper . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post IBM Announces IBM Quantum Nighthawk r3: A New Processor to Support 10k Quantum Operations on 520 Programmable Qubits appeared first on MarkTechPost .
