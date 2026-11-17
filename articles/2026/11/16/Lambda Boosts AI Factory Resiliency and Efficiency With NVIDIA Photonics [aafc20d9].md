---
id: "aafc20d9f2a085c9"
title: "Lambda Boosts AI Factory Resiliency and Efficiency With NVIDIA Photonics"
url: "https://blogs.nvidia.com/blog/lambda-photonics"
link: "https://blogs.nvidia.com/blog/lambda-photonics"
source: "NVIDIA Blog"
domain: "blogs.nvidia.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-16T16:00:51Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Brian Sparks"]
language: "en"
summary: "To train an AI model, thousands of GPUs have to work together, requiring a network that’s fast, efficient and resilient. \n \n Lambda is tackling the network piece of the puzzle with NVIDIA Photonics co-packaged optics (CPO) switches. The cloud provider is using the switches to connect NVIDIA GB300 NVL72 racks with more than 10,000 GPUs, delivering lower power, higher resiliency and longer mean…"
tags: ["Networking", "Supercomputing", "AI Factory", "Artificial Intelligence", "Hardware"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 462
paywalled: false
image: "https://blogs.nvidia.com/wp-content/uploads/2026/11/ethernet-lambda-blog-1920x1080-1.jpeg"
discussion_url: null
score: null
comments: null
community: null
---

# Lambda Boosts AI Factory Resiliency and Efficiency With NVIDIA Photonics

NVIDIA Blog · Brian Sparks · 2026-11-16

To train an AI model, thousands of GPUs have to work together, requiring a network that’s fast, efficient and resilient.
Lambda is tackling the network piece of the puzzle with NVIDIA Photonics co-packaged optics (CPO) switches. The cloud provider is using the switches to connect NVIDIA GB300 NVL72 racks with more than 10,000 GPUs, delivering lower power, higher resiliency and longer mean time between interruptions (MTBI) to an AI factory at scale.
“Networking has to keep pace with the demands of increasingly large AI clusters,” said Dave Ward, president of cloud services at Lambda. “Bringing co-packaged optics into a deployment of this scale is an important step toward building the infrastructure needed to support the next generation of AI.”
In the company’s tests using the switches, network latency — the time needed for moving data — dropped by about 4% at rack scale and by up to about 10% at pod scale. Across rack, scalable unit and pod configurations, the network maintains the same throughput as conventional pluggable optics.
Delivering Power Efficiency and Resiliency at Scale
Improving power efficiency and resiliency matters because the network sits at the center of AI factory productivity.
In a large training job, one interrupted link can stall thousands of GPUs. With agentic inference, one network disruption can introduce cascading latency effects on many agents. Every interruption costs time, and every watt spent on networking is a watt not available for compute.
NVIDIA Photonics addresses both power efficiency and resiliency. By replacing pluggable transceivers with co-packaged optical engines on the switch package, it delivers up to 5x better power efficiency and up to 15x higher reliability than conventional pluggable optics. It also uses 4x fewer lasers, which means fewer components that can fail.
Cooler Optics, Replaceable Light Sources Increase Resiliency
Lambda’s deployment uses NVIDIA Photonics switches, each with 144 ports running at 800Gb/s. Liquid cooling carries heat away from the switch chip and optical engines.
The company reports a median optics temperature of 36°C, compared with 51°C for conventional pluggable optics, and its tests find more stable signal integrity.
NVIDIA Photonics also brings the electrical-to-optical conversion closer to the switch chip. Each switch has 18 removable external light sources, which supply light to the optical engines. Optical engines sit alongside the chip on the same package and convert electrical signals into light that carries data over fiber between parts of the cluster.
Technicians can replace the light-source modules in the field, unlike traditional pluggable optics, which require replacing the entire module if a laser fails.
Co-packaging shortens the electrical path from inches to millimeters, which reduces signal loss. It also removes the need for retimer chips, cutting both power draw and the number of parts in the signal path.
Explore NVIDIA Photonics and read Lambda’s deployment announcement.
