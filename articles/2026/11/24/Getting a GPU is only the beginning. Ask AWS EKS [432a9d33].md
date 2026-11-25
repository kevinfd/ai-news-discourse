---
id: "432a9d3342893c68"
title: "Getting a GPU is only the beginning. Ask AWS EKS."
url: "https://thenewstack.io/kubernetes-gpu-inference-startup"
link: "https://thenewstack.io/kubernetes-gpu-inference-startup"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T17:17:12Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Chris J. Preimesberger"]
language: "en"
summary: "Eight minutes is a long time to wait for another copy of an AI model to start serving traffic. It feels longer when the requests are already coming in. And while Kubernetes can schedule another replica, there’s still hardware to provision, a container image to pull, model weights to load, and GPU code to compile.  \n\n The autoscaler got the message, but the model is still getting dressed. \n\n At…"
tags: ["AI Infrastructure", "Cloud Services", "Kubernetes", "Podcast", "sponsor-amazon-web-services-aws", "Sponsored", "sponsored-podcast", "Video"]
orgs: ["Amazon", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "agents & coding"]
content_source: "summary"
word_count: 598
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Getting a GPU is only the beginning. Ask AWS EKS.

The New Stack · Chris J. Preimesberger · 2026-11-24

Eight minutes is a long time to wait for another copy of an AI model to start serving traffic. It feels longer when the requests are already coming in. And while Kubernetes can schedule another replica, there’s still hardware to provision, a container image to pull, model weights to load, and GPU code to compile.  

 The autoscaler got the message, but the model is still getting dressed. 

 At KubeCon + CloudNativeCon this month in Salt Lake City, The New Stack’s Matt Burns asked Sajjan Gundapunnedi , a senior engineering manager for Amazon Elastic Kubernetes Service (EKS) , what developers can do in those eight minutes. Their conversation starts with the scramble to find GPUs and gets into the engineering decisions that determine how much work those GPUs actually do. 

 “Demand for GPU capacity or any accelerated capacity is outpacing supply everywhere,” Gundapunnedi told TNS.  

 Give Kubernetes more to do 

 In our interview, Gundapunnedi describes two ways to line up accelerated capacity through EKS Auto Mode and Karpenter , the Kubernetes node provisioner. On-Demand Capacity Reservations secure capacity in a specific Availability Zone , subject to availability. Capacity Blocks let teams book capacity for a fixed future window. That gives teams planning a training or fine-tuning run a way to schedule the job around a reservation. 

 “What this lets you do is faster communication for your job,” Gundapunnedi told TNS. 

 Once the hardware is in place, device placement matters. With Dynamic Resource Allocation support for NVIDIA GPUs and Elastic Fabric Adapters in EKS Auto Mode, developers can specify which devices a workload needs and request a GPU and an adapter on the same PCIe route. 

 “What this lets you do is faster communication for your job,” Gundapunnedi told TNS . 

 Training and fine-tuning jobs repeatedly exchange data. Time spent waiting for those exchanges can leave GPUs idle, even though the meter is running. Giving Kubernetes a way to account for hardware topology when it places a workload can help shorten that wait. 

 Where the eight minutes went 

 Inference brings a different scheduling problem. Traffic arrives in bursts, and a new replica has to become useful while demand for it still exists. 

 Gundapunnedi walks us through what his team tried, beginning with capacity buffers in Karpenter so replicas can land on existing nodes during a spike. He also describes using seekable OCI to pull and unpack container images in parallel and using vLLM with Run:ai Model Streamer to download model weights in parallel. 

 For smaller models in the example, compilation was particularly expensive. Each replica on a node was redoing the same work. The team cached the compiled artifacts on the node so subsequent replicas could reuse them. Gundapunnedi called out the payoff. 

 “It was the cheapest configuration tuning for us, which gave the largest benefits.” 

 “It was the cheapest configuration tuning for us, which gave the largest benefits,” Gundapunnedi said. 

 The discussion also covers how much infrastructure a team wants to own. In Auto Mode, AWS manages worker-node images, bundled add-ons and their upgrade lifecycle, and runs the Karpenter controller. Gundapunnedi points to standalone Karpenter for teams that need configurations Auto Mode hasn’t picked up.  

 For an application developer, the distinction matters when the work shifts from deploying a model to maintaining the machinery that keeps it running. 

 Watch the full interview on The New Stack’s YouTube channel for Gundapunnedi’s walkthrough of the startup bottlenecks and his take on what comes next for GPU sharing, workload queues, and inference routing. 
 The post Getting a GPU is only the beginning. Ask AWS EKS. appeared first on The New Stack .
