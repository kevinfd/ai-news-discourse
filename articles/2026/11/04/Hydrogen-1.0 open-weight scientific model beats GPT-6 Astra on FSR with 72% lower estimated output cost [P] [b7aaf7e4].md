---
id: "b7aaf7e4bc34ba84"
title: "Hydrogen-1.0: open-weight scientific model beats GPT-6 Astra on FSR with 72% lower estimated output cost [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xnjhdd/hydrogen10_openweight_scientific_model_beats_gpt6"
link: "https://reddit.com/r/MachineLearning/comments/1xnjhdd/hydrogen10_openweight_scientific_model_beats_gpt6"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T09:00:29Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["AKAMA199"]
language: "en"
summary: "Hey everyone— we’re the Deep Principle team behind Mira AI Scientist. We just released Hydrogen-1.0 , an open-weight model post-trained from GLM-5.3 for chemistry, materials science, and life sciences. Here’s how it performed in our evaluations: FrontierScience Research: 38.3% pass rate vs. 33.3% for GPT-6 Astra at max thinking—a 5 percentage point lead . Estimated output-side cost on FSR: $0.25…"
tags: ["r/MachineLearning"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "health & science", "search & media"]
content_source: "post"
word_count: 489
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xnjhdd/hydrogen10_openweight_scientific_model_beats_gpt6/"
score: null
comments: null
community: "r/MachineLearning"
---

# Hydrogen-1.0: open-weight scientific model beats GPT-6 Astra on FSR with 72% lower estimated output cost [P]

Reddit · AKAMA199 · 2026-11-04

Hey everyone— we’re the Deep Principle team behind Mira AI Scientist. We just released Hydrogen-1.0 , an open-weight model post-trained from GLM-5.3 for chemistry, materials science, and life sciences. Here’s how it performed in our evaluations: FrontierScience Research: 38.3% pass rate vs. 33.3% for GPT-6 Astra at max thinking—a 5 percentage point lead . Estimated output-side cost on FSR: $0.25 per problem vs. $0.88 for Astra at max thinking—about 72% lower under our evaluation setup. GPQA Diamond: 92.9% accuracy, compared with Kimi K3’s 93.5% . On separate internal task sets, Hydrogen also scored higher than GPT-6 Astra at max thinking on scientific computing (+5.13 percentage points) and single-step forward reaction prediction (+4.76 points). It trailed Astra on NMR structure elucidation (−3.33 points). The write-up covers the evaluations and five workflow examples. Why we built it If you’ve used LLMs for research, you’ve probably spent a fair amount of time connecting the steps yourself: turning a question into a plan, preparing inputs, running tools, checking the output, and figuring out what to try when something breaks. We wanted to see whether training on scientific workflows could make the model better at handling those connected decisions. How we trained it We used supervised fine-tuning and reinforcement learning with domain data, scientist feedback, records from our own labs, and discovery trajectories. The lab records keep the research goal, procedure, observations, and outcome together. The discovery trajectories include how the next step changes after feedback, failed attempts, or unexpected results. SFT gives the model worked examples of scientific reasoning, experiment planning, protocol design, and analysis. RL uses feedback on research outcomes to improve its decisions. What the workflows look like The article walks through five cases: Polymer molecular dynamics: Builds a polyethylene melt with Python, runs GROMACS, checks and repairs the topology, and restarts the simulation. Outputs include a corrected 40 ns trajectory and analyses of density, molecular packing, diffusion, and chain dimensions. Reaction networks: Explores connected molecular structures, competing pathways, and recorded energy barriers. NMR interpretation: Compares seven candidate structures against a supplied proton NMR spectrum. Experiment planning: Generates a machine-readable protocol for a 12-vial Suzuki coupling study , with virtual checks of equipment capabilities and action prerequisites. Materials search: Uses feedback over five rounds to guide a search for transition-metal complexes with larger HOMO–LUMO gaps. A bit of context: these are selected model-plus-tool walkthroughs, not an overall autonomous-research success rate. GROMACS does the MD calculations, and the protocol validation is virtual—it doesn’t mean the physical experiment was carried out. The attached video gives a quick look at the research interactions. The article has the detailed walkthroughs, evaluations, and training approach. Links Weights and model card: Hydrogen-1.0 on Hugging Face Technical write-up, evaluations, and cases: Introducing Hydrogen-1.0 Try it: Mira AI Scientist We’d especially like to hear from people working in computational chemistry and materials science. What would you try it on first, and what would you check before trusting the result?
