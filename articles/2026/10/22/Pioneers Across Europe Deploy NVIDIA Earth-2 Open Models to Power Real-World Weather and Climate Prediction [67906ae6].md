---
id: "67906ae6df39627e"
title: "Pioneers Across Europe Deploy NVIDIA Earth-2 Open Models to Power Real-World Weather and Climate Prediction"
url: "https://blogs.nvidia.com/blog/europe-earth-2-open-models-weather-climate-prediction"
link: "https://blogs.nvidia.com/blog/europe-earth-2-open-models-weather-climate-prediction"
source: "NVIDIA Blog"
domain: "blogs.nvidia.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-22T05:00:19Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Mike Pritchard"]
language: "en"
summary: "Weather forecasts shape more than daily plans; timely weather information is crucial for energy producers, insurers and transport operators to plan around changing conditions. A global forecast can show a storm taking shape, but decisions about solar farms, shipping routes or insured property depend on what happens locally. \n NVIDIA Earth-2 gives developers and researchers a family of open AI…"
tags: ["AI", "Climate", "GTC 2026", "NVIDIA Earth-2"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "safety & ethics"]
content_source: "fulltext"
word_count: 516
paywalled: false
image: "https://blogs.nvidia.com/wp-content/uploads/2026/10/Earth-2-Open-Models-Climate-Prediction.png"
discussion_url: null
score: null
comments: null
community: null
---

# Pioneers Across Europe Deploy NVIDIA Earth-2 Open Models to Power Real-World Weather and Climate Prediction

NVIDIA Blog · Mike Pritchard · 2026-10-22

Weather forecasts shape more than daily plans; timely weather information is crucial for energy producers, insurers and transport operators to plan around changing conditions. A global forecast can show a storm taking shape, but decisions about solar farms, shipping routes or insured property depend on what happens locally.
NVIDIA Earth-2 gives developers and researchers a family of open AI models and tools they can customize with their own data. Running on NVIDIA computing, these technologies support global weather prediction, detailed regional forecasts and environmental research.
StormScope EU is the latest model to join Earth-2 — a regional version of the StormScope model for short-term forecasting, trained over Europe weather and climate data. It uses EUMETSAT satellite observations to predict evolving cloud conditions across 16 Meteosat channels at 10-minute intervals.
At GTC Berlin, NVIDIA is showcasing a live StormScope EU pipeline in an interactive weather demo built in partnership with Earthmover. The demo uses Earth2Studio to run forecasts and Earthmover’s data platform to manage and serve the real-time results, which are updated as soon as new satellite observations come in, every 10 minutes. Earthmover serves these results as map tiles, letting visitors explore predictions across Europe without downloading entire datasets.
Developers can combine Earth-2 models in workflows tailored to regional needs, using StormScope for short-term forecasting and CorrDiff to add local detail to coarser weather data. Developers can also pick up these model architectures and train them for new environmental applications such as air-quality modeling. The open source NVIDIA PhysicsNeMo framework provides training and customization tools so teams can build applications that incorporate proprietary data and domain expertise to meet regional needs.
Organizations building on Earth-2 capabilities include:
AXA is using NVIDIA Earth-2’s FourCastNet 3 to study regional cyclone risk beyond the historical record across more than 1,000 simulated seasons, generating insights that can inform risk assessments and help customers target prevention efforts.
Vaisala Xweather is combining Earth-2 with its proprietary observations, lightning data and forecasting expertise to enhance its weather intelligence platforms for government, energy, maritime, transportation and insurance customers. Its work includes adapting StormScope with lightning data to advance short-term forecasting lead time and make these warnings accessible through Vaisala Xweather’s software-as-a-service offerings and AI-assistant integrations.
Video courtesy of Vaisala Xweather.
University of Manchester researchers adapted the Earth-2 CorrDiff model for U.K. air-quality modeling. It trained the model on the NVIDIA-powered Isambard-AI supercomputer and ran it locally on NVIDIA DGX Spark systems, bringing environmental modeling from a national supercomputer to the desktop.
TotalEnergies is exploring NVIDIA Earth-2 for solar-energy forecasting, evaluating StormScope-based solar-radiation nowcasts at two photovoltaic sites and developing models to provide weather information at subhourly intervals. The work explores how more detailed forecasts could help anticipate changes in solar-power generation.
Space42 developed SARDiff4Height using CorrDiff and NVIDIA PhysicsNeMo. The research estimates surface heights from a single radar image and produces uncertainty maps, helping analysts understand where estimates need closer scrutiny.
Explore NVIDIA Earth-2 open models and tools, and explore with Earth2Studio’s forecasting examples. Read AXA’s hurricane-risk case study and Manchester’s air-quality story to learn how teams are adapting weather AI to specialized challenges.
