---
id: "26933cbdc3d2f98d"
title: "Nvidia Expands CUDA-X Tools for AI Semiconductor Manufacturing"
url: "https://advancedmanufacturing.org/news-desk/nvidia-expands-cuda-x-tools-for-ai-semiconductor-manufacturing/article_dd437ee8-0df3-44e7-a057-9525638b7792.html"
link: "https://advancedmanufacturing.org/news-desk/nvidia-expands-cuda-x-tools-for-ai-semiconductor-manufacturing/article_dd437ee8-0df3-44e7-a057-9525638b7792.html"
source: "Advanced Manufacturing"
domain: "advancedmanufacturing.org"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-15T12:41:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["PRESS RELEASE Nvidia"]
language: "en"
summary: "NVIDIA announced semiconductor leaders are adopting NVIDIA CUDA-X libraries — including the new NVIDIA cuPotential library, which developers can use to build AI agents that simulate how atoms and mole ..."
tags: []
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "agents & coding", "models & research", "robotics & autonomy"]
content_source: "fulltext"
word_count: 1256
paywalled: false
image: "http://www.bing.com/th?id=ONUT.jRrUHEXd9XKHSLHEbD-B9A&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Nvidia Expands CUDA-X Tools for AI Semiconductor Manufacturing

Advanced Manufacturing · PRESS RELEASE Nvidia · 2026-10-15

NVIDIA announced semiconductor leaders are adopting NVIDIA CUDA-X libraries — including the new NVIDIA cuPotential library, which developers can use to build AI agents that simulate how atoms and molecules interact — to advance AI-defined fabs.
AI-defined fabs are semiconductor factories where AI helps engineers optimize processes, solve production issues and improve production efficiency. As demand for advanced chips rises, such fabs must expand production while managing increasingly complex manufacturing processes. Engineers need new ways to model materials, analyze inspection data and test process changes in digital twins before applying them in production.
The expanded CUDA-X portfolio gives AI agents and engineering applications accelerated tools for semiconductor simulation, 3D data processing and image analysis, helping automate more engineering work across chip design and manufacturing so fabs can predict process behavior and improve yield.
“The semiconductor industry made the AI revolution possible. Now, AI is transforming how chips are built,” said Tim Costa, vice president and general manager of industrial and computational engineering at NVIDIA. “As fabs race to meet demand for advanced chips, NVIDIA CUDA-X and Omniverse libraries give AI agents accelerated simulation and inspection tools to help engineers manage complexity, improve yield and advance AI-defined fabs.”
NVIDIA cuPotential Accelerates How Researchers Model Atomic Interactions
Understanding how atoms and molecules interact is critical to modeling semiconductor materials and manufacturing processes, but these calculations can take significant amounts of time, even in software already optimized for GPUs.
NVIDIA cuPotential accelerates atomic-scale simulation with specialized GPU-accelerated functions developers can add to existing software. It helps researchers model electrical forces and other interactions across large numbers of atoms to test and refine simulations faster. Synopsys is among the early adopters using cuPotential to accelerate materials simulations.
By making these modeling capabilities available to AI agents, cuPotential helps agents run, evaluate and iterate on advanced molecular simulations. In early-access testing, the library accelerated already GPU-optimized workflows by an additional 2-3x.
Semiconductor Leaders Advance AI-Defined Fabs With NVIDIA CUDA-X
AI-defined fabs require faster ways to model chip designs, materials behavior and manufacturing processes before changes reach production. NVIDIA CUDA-X libraries — including NVIDIA cuPotential for simulating atomic interactions, NVIDIA cuEST for modeling electronic behavior and NVIDIA cuDSS for solving complex engineering simulations — accelerate these workloads to help make fabs more autonomous.
Synopsys is using cuPotential, cuEST and cuDSS to accelerate semiconductor simulations, with early QuantumATK results showing a potential 30x speedup using cuEST, and S-Device benchmarks showing a 12x speedup using cuDSS. The company’s AgentEngineer solutions interoperate with NVIDIA Nemotron open models and NVIDIA NeMo to support AI agents for chip design and verification.
Cadence is using NVIDIA accelerated computing, NVIDIA Nemotron open models and CUDA-X libraries to bring agentic AI to the design and simulation of electromechanical systems — from semiconductors to advanced packaging and printed circuit boards. Examples include Cadence AuraStack AI Super Agent optimizing advanced packages for heat and stress 8x faster using cuDSS with Cadence Celsius, and Nemotron with ChipStack AI Super Agent for semiconductor design and verification.
COMSOL is accelerating semiconductor multiphysics simulations with NVIDIA cuDSS, delivering up to 10x faster simulations to help engineers optimize equipment and processes. Its upcoming COMSOL MCP Server will use the NVIDIA Nemotron Ultra open model to enable AI-assisted modeling and design exploration.
Voltai accelerates advanced chip packaging with Voltaire, its agentic multiphysics platform for 3D-IC design and simulation. Voltaire combines AI agents with GPU-accelerated solvers powered by NVIDIA cuDSS and CUDA-X libraries, compressing complex electro-thermal-mechanical simulation workflows from months to a day.
ChipAgents uses NVIDIA AI infrastructure and NVIDIA model-training and optimization software to develop specialized AI models for chip design. The company is also working with NVIDIA to develop Build-A-Chip Bench, a new AI benchmark that evaluates agents across end-to-end workflows from specification to graphic data system. The benchmark gives the industry a comprehensive measure of progress toward fully autonomous semiconductor engineering.
NVIDIA Open Libraries Help Prepare and Optimize Manufacturing Workflows
Fabs depend on thousands of process steps that must be modeled, refined and validated before production. The NVIDIA cuLitho library accelerates calculations for printing chip patterns; NanoVDB — an open source library for working with 3D data — accelerates chipmaking simulations; and the open NVIDIA PhysicsNeMo framework helps train physics AI models to predict how physical systems behave.
Siemens is using cuLitho to speed up Calibre software for chip-pattern refinement and mask preparation. Its Solido team is also developing agent-driven characterization workflows with Nemotron open models and NVIDIA NeMo open libraries.
Lam Research intends to integrate NanoVDB into its advanced semiconductor process modeling platform SEMulator3D, part of the company’s Semiverse Solutions family of virtual products. The addition of NanoVDB is expected to accelerate select wafer-etch modeling by up to 30x, while using NVIDIA PhysicsNeMo has been demonstrated to assist in reducing plasma-prediction simulation time to as little as milliseconds instead of days.
Luminary is applying NVIDIA PhysicsNeMo to semiconductor package design, training physics AI models to predict temperature, pressure drop and thermal stress across package configurations — enabling engineers to explore 100x more designs in the same schedule without running a new simulation for every option.
AI-Defined Fabs Inspect and Test Chips With NVIDIA CUDA-X Libraries
AI-defined fabs need to analyze inspection images and test data quickly enough to catch defects, maintain equipment and improve yield. NVIDIA NPP, a library for processing images on GPUs, and NVIDIA RAPIDS cuDF, a library for processing large datasets on GPUs, help accelerate test and quality-control workflows.
Using NVIDIA AI and accelerated computing, imec is removing noise from scanning electron microscope images used for sub-nanometer chip measurements and using NVIDIA cuLitho to enable computationally intensive process-window optical proximity correction — achieving a 30% improvement in the lithography process window.
KLA applied insights from its highly optimized production kernels to a new NPP NCC kernel that achieved performance levels 50x faster than earlier CPU versions, comparable with KLA’s hand-tuned implementations.
Teradyne is using NVIDIA NPP and accelerated computing to accelerate image-sensor testing, and RAPIDS cuDF and CuPy for GPU calculations, to deliver approximately 85x faster probe-maintenance inference, helping identify degrading probes before they affect yield.
Advantest has integrated NVIDIA Nemotron and NVIDIA Kumo-Anomaly into ACS RTDI to enable AI-driven semiconductor production analytics. Powered by NVIDIA Grace Blackwell systems, ACS delivers real-time diagnostics and inferencing that recommend corrective actions for test cells. Advantest is also using NVIDIA NeMo Switchyard AI agents to automate model selection, streamline semiconductor test workflows and reduce response times from hours to minutes.
NVIDIA Technologies Advance Fab Operations and Automation
In an AI-defined fab, equipment data must move from instruments into AI systems fast enough to support operational decisions.
Applied Materials is using NVIDIA Omniverse and NVIDIA CUDA-X libraries, including cuDSS, cuEST and PhysicsNeMo, across materials discovery, process development and fab optimization — enabling up to 35x faster chamber simulations and fab digital twins that help optimize layouts and material flow.
Analog Devices Inc. is combining Synopsys physics simulation with the NVIDIA Isaac Sim framework and Omniverse libraries to develop high-fidelity sensing simulations and robotic benchmarks, helping engineers evaluate how sensors behave within complete robotic systems.
FANUC and Foxconn are connecting their robot models to the Mega NVIDIA Omniverse Blueprint, enabling manufacturers to simulate and validate robotic operations in factory digital twins before physical deployment.
OMRON is using NVIDIA Cosmos open world models and the NVIDIA Metropolis Blueprint for video search and summarization in its inspection equipment to develop agents that combine visual data, equipment documentation and manufacturing knowledge. These agents help engineers analyze printed circuit board results, investigate potential defect causes, and support troubleshooting and quality control.
