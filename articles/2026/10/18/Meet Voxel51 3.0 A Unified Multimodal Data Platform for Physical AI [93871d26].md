---
id: "93871d267ad005f4"
title: "Meet Voxel51 3.0: A Unified Multimodal Data Platform for Physical AI"
url: "https://marktechpost.com/2026/10/17/voxel51-3-0-physical-ai-data-platform"
link: "https://marktechpost.com/2026/10/17/voxel51-3-0-physical-ai-data-platform"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-18T04:06:33Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Voxel51 has released Voxel51 3.0 , a very important update to its data platform. Voxel51 3.0 is an end-to-end multimodal data platform that puts search, curation, annotation and evaluation in one system. It targets teams training models on sensor data from robots, vehicles and factories. The release adds Voxel51 Agent, a data provenance layer and free self-service access . \n\n TL;DR \n\n Scale:…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "New Releases", "Physical AI"]
orgs: []
topics: ["agents & coding", "models & research", "search & media", "products & launches"]
content_source: "summary"
word_count: 873
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Voxel51 3.0: A Unified Multimodal Data Platform for Physical AI

MarkTechPost · Asif Razzaq · 2026-10-18

Voxel51 has released Voxel51 3.0 , a very important update to its data platform. Voxel51 3.0 is an end-to-end multimodal data platform that puts search, curation, annotation and evaluation in one system. It targets teams training models on sensor data from robots, vehicles and factories. The release adds Voxel51 Agent, a data provenance layer and free self-service access . 

 TL;DR 

 Scale: Voxel51 Agent ships with 45+ MCP tools, 80+ operators and 18 open-source skills. 

 Runs on: Hosted web app at app.voxel51.com, or self-hosted in cloud, hybrid, on-prem and air-gapped setups. No local GPU requirement disclosed. 

 Performance: No product benchmarks published. Voxel51 cites its own survey data instead. 

 Best: Free tier includes Voxel51 Agent, 30,000 inference requests and 30 compute hours per month. 

 Worst: Free tier caps at 3 datasets of 10,000 samples each and 20 GB of storage. 

 What is new in Voxel51 3.0? 

 Voxel51 3.0 expands the platform beyond its roots in visual data with 3 core additions. 

 Time-series multimodal support : Teams can view multiple sensor streams on 1 timeline. Segment-level embeddings find specific moments inside long recordings. 

 Unified annotation : Labeling covers 2D, 3D, video and multimodal data. It includes automated QA, annotator metrics and human-in-the-loop review. 

 Agentic Labeling : Vision-language models generate labels from natural-language instructions and examples. 

 Supported modalities include MCAP, images, video, 3D point clouds, meshes, DICOM, NIfTI, geospatial data and audio. 

 How does Voxel51 Search work? 

 Voxel51 Search is a persistent hybrid index. It indexes datasets and computes embeddings automatically, so search works from day 1. 

 Semantic retrieval finds visually or semantically similar moments, even without shared labels. Lexical and structured queries handle exact terms, timestamps, sensor fields and metadata. Embeddings and structured fields stay in native form and are combined at retrieval time. 

 Vector retrieval runs on LanceDB. It supports vector, scalar and full-text indexes, and separates storage from compute. Teams choose what to embed, which model and compute to use, and when. Incremental updates avoid full rebuilds when samples arrive or schemas change. 

 What can Voxel51 Agent do? 

 Voxel51 Agent chains search, curation, annotation and evaluation into repeatable workflows. 

 Example workflows: 

 A robotics team searches behaviors across thousands of episodes, then curates balanced training sets. 

 A perception team starts from a model failure and pulls similar long-tail scenarios for labeling. 

 The agent can also write code to build custom plugins. All workflows inherit the organization’s permissions and governance controls. 

 How does data provenance work in Voxel51 3.0? 

 Voxel51 3.0 adds 4 provenance layers : 

 Deployment-level activity log: who did what, and when, across the deployment. 

 Dataset-level activity log: how a single dataset evolved. 

 Sample-level edit history: label, metadata and property changes per sample. 

 Dataset versioning: immutable snapshots to reproduce training and evaluation runs. 

 Events flow through fiftyone-mq for job scheduling and Activity Core for event tracking. 

 Can teams bring their own models? 

 Yes. The platform is model-agnostic across embeddings, auto-labeling, inference and evaluation. A team can bootstrap with a foundation model, then swap in its own domain model. 

 Why does Voxel51 argue data work decides outcomes? 

 Voxel51 cites its 2026 State of Physical AI survey . 58% of “exceptional” teams spend more than half their project time on data work. Only 21% of struggling teams do the same. This is vendor-run research, so read it as directional. 

&&

 How does Voxel51 3.0 compare with Encord and Foxglove? 

 Feature Voxel51 3.0 Encord Foxglove Core focus Search, curate, annotate, evaluate multimodal data Annotation, curation and data management Robotics visualization, observability and data management Free tier 3 datasets, 10,000 samples each, 20 GB Not disclosed 10 GB storage, 3 users, 5 devices Paid entry Team: 8 seats, 2,800 compute hrs/mo (price not disclosed) Starter (price not disclosed) Pro: $20/mo + usage, 1 TB storage Built-in agent Voxel51 Agent Data agents (Team plan) Agent sidebar MCP 45+ MCP tools Not disclosed Foxglove MCP (local MCP on paid plans) Search Hybrid semantic, lexical and metadata Multi-modal search, querying, filtering Semantic Search (beta) plus structured search Annotation 2D, 3D, video, multimodal, Agentic Labeling Image, video, audio, documents; 3D and LiDAR add-on Events on time segments Time-series sensor data MCAP, synced streams, segment embeddings Sensor streams (see note) MCAP, ROS 1, ROS 2 native Provenance Activity logs, edit history, versioning Not disclosed Audit logs (not on Free) Self-hosted On-prem and air-gapped available VPC and on-prem (add-on or Enterprise) Self-hosted data on Enterprise; BYO storage on Pro 

 Encord’s sensor-stream support is stated in its Series C release . Prices verified October 17, 2026. 

 Key Takeaways 

 Voxel51 3.0 merges search, curation, annotation and evaluation in 1 platform. 

 Voxel51 Agent ships with 45+ MCP tools, 80+ operators and 18 skills. 

 Activity logs, edit history and versioning make training data traceable. 

 Free tier: 3 datasets, 10,000 samples each, no credit card. 

 Check out the official blog post , the press release and the Voxel51 docs , or try it at app.voxel51.com . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Meet Voxel51 3.0: A Unified Multimodal Data Platform for Physical AI appeared first on MarkTechPost .
