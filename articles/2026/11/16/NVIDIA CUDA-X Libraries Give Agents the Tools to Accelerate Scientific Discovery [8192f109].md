---
id: "8192f1094925b873"
title: "NVIDIA CUDA-X Libraries Give Agents the Tools to Accelerate Scientific Discovery"
url: "https://blogs.nvidia.com/blog/cuda-x-libraries-agents-accelerate-scientific-discovery"
link: "https://blogs.nvidia.com/blog/cuda-x-libraries-agents-accelerate-scientific-discovery"
source: "NVIDIA Blog"
domain: "blogs.nvidia.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T16:00:16Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Kibibi Moseley"]
language: "en"
summary: "With expanded NVIDIA CUDA-X libraries, including cuPhoton, cuPotential and cuSpa, researchers can sift through vast amounts of data to accelerate research, from astrophysics and materials science to single-cell biology. \n The speedups are helping scientists analyze larger datasets and model more complex systems. \n The new libraries give AI agents the tools to help researchers make discoveries…"
tags: ["AI Infrastructure", "Hardware", "Software", "Supercomputing", "CUDA-X", "DGX Spark", "Nemotron", "Science"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "health & science", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 772
paywalled: false
image: "https://blogs.nvidia.com/wp-content/uploads/2026/11/hpc-for-dev-tech-blog-cuda-x-sc26-1920x1080-5818376.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA CUDA-X Libraries Give Agents the Tools to Accelerate Scientific Discovery

NVIDIA Blog · Kibibi Moseley · 2026-11-16

With expanded NVIDIA CUDA-X libraries, including cuPhoton, cuPotential and cuSpa, researchers can sift through vast amounts of data to accelerate research, from astrophysics and materials science to single-cell biology.
The speedups are helping scientists analyze larger datasets and model more complex systems.
The new libraries give AI agents the tools to help researchers make discoveries faster than ever.
Bringing Black Holes Into Focus
Seeing a black hole takes a telescope the size of Earth. The Event Horizon Telescope links radio dishes worldwide, generating petabytes of data that can take months to process.
With NVIDIA cuPhoton.xBeam, a module within the cuPhoton Toolkit, black hole observations from the Event Horizon Telescope can now be correlated orders of magnitude faster than ever. Analysis that once took over a month now takes eight minutes.
By combining global radio dishes into Earth-sized aperture, cuPhoton delivers unprecedented astronomical imaging resolution. cuPhoton successfully correlated observations of powerful black hole jets J1924 and 3C279 in the night sky — making it a reality to reconstruct a Messier 87* black hole galaxy in real time.
The entire pipeline, from data loading and processing to visualization, runs on distributed multi-GPU systems or a compact NVIDIA DGX Spark system, helping scientists study how gas spirals inward under a black hole’s powerful gravitational pull.
Steering Fusion Simulations
Sustaining plasma at millions of degrees is essential to achieving stable, continuous fusion energy. But simulating its behavior is costly: on petascale systems, a single time step can take days, with simulations running for weeks. Experiments also generate data faster than traditional pipelines can process it, often leaving scientists waiting until experiments end to analyze results.
Pacific Fusion researchers used NVIDIA cuPhoton.xLens module to extract insights while plasma simulations run, helping them visualize what’s happening as results emerge.
The NVIDIA cuPhoton.xLens module extracts insights while plasma simulations run, helping researchers understand what’s happening as results emerge. Researchers can couple the entire pipeline with an NVIDIA Nemotron-powered agent running locally on the same system, enabling interactive analysis that can help steer simulations in real time to inform fusion reactor target and chamber design.
Exploring Potential Medicines
Molecular simulations help scientists evaluate drug designs before costly laboratory experiments. NVIDIA cuPotential, built on work by researchers at Simons Foundation’s Flatiron Institute and D. E. Shaw Research, accelerates existing simulation software by up to 3x while improving calculation stability and accuracy. It expedites synthetic data creation for generative AI models, finding previously unknown molecular binding sites and calculating the strength of molecular interactions.
NVIDIA is working with Schrödinger and the AMBER, NAMD, GROMACS, LAMMPS and Open Molecular Software Foundation communities to bring cuPotential acceleration to molecular dynamics engines and workflows.
Cadence, Fathom Therapeutics, Topos Bio, Genesis Molecular AI and Terray Therapeutics are adopting it for drug discovery.
Accelerating Materials Research
Daviator, a collection of batched GPU kernels for the widely used Vienna Ab initio Simulation Package, is coming to NVIDIA ALCHEMI — delivering quantum-mechanical calculations up to 22x faster and at up to 75% lower cost. With Daviator, researchers building simulation models can now use GPU acceleration across atomistic systems of all sizes to generate the millions of calculations of atomic interactions needed for model training and inference, including for small systems that previously ran faster on CPUs.
At Lawrence Berkeley National Laboratory, the NVIDIA DAQIRI networking library connects a high-speed electron microscopy detector to GPU processing, moving analysis into the experiment itself. Researchers can identify useful signals, discover previously unknown regions of interest and decide what to measure next while measurements are being taken.
The workflow supports atomic-resolution materials studies that can distinguish elements, laying the groundwork for future automated experiments.
Revealing Biology at Scale
The newly open source cuSpa accelerates cell polygon calculations, enabling developers to generate massive spatial graphs for next-generation patient and cancer models at Memorial Sloan Kettering Cancer Center, with a 900x speedup compared with using CPUs.
Codeveloped with scverse, the rapids-singlecell framework accelerates single-cell analysis — and is now available in a single, agent-ready container. Using the tool, Therna Biosciences processed data 200x faster for therapeutic design. 10x Genomics integrated rapids-singlecell in its new Sentira platform, helping academic researchers, biopharma teams and foundation model builders accelerate the path from large-scale spatial data to biological insights.
And the NVIDIA GPU-accelerated HMMER library, also open source, accelerates the annotation of predicted protein sequences, supporting data preparation for biological foundation models. At Basecamp Research, benchmark searches ran up to 84x faster than with standard HMMER, reducing the time required to annotate the large biological datasets used to train the company’s therapeutic design models.
Explore NVIDIA CUDA-X libraries. Learn more in this technical blog on GPU-powered black hole reconstruction.
