---
id: "a3f9078912ac05de"
title: "How AI Helps Recyclers Turn Mixed Waste Into Reusable Material"
url: "https://blogs.nvidia.com/blog/ai-recycling-startups"
link: "https://blogs.nvidia.com/blog/ai-recycling-startups"
source: "NVIDIA Blog"
domain: "blogs.nvidia.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-11T03:00:20Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Katie Michel"]
language: "en"
summary: "Skip to content\n\t\n\t\n\t\t\n\t\t\t\n\t\t\t\n\t\n\t\t\t\n\t\nAs world leaders gather for COP31 in Türkiye, the event’s emphasis on zero waste puts a practical challenge in focus: how to keep products and materials in use for longer. Globally, less than 7% of the materials entering the economy come from recycled or reused sources. Municipal solid waste generation accounts for over 2 billion tons of trash per year — a…"
tags: ["AI", "Robotics", "AI for Good", "Computer Vision", "Healthcare and Life Sciences", "Inception", "Jetson", "Sustainability", "TensorRT"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "business & funding", "robotics & autonomy", "jobs & society"]
content_source: "fulltext"
word_count: 1164
paywalled: false
image: "https://blogs.nvidia.com/wp-content/uploads/2026/11/recycling-company-grid-1920x1080-1.png"
discussion_url: null
score: null
comments: null
community: null
---

# How AI Helps Recyclers Turn Mixed Waste Into Reusable Material

NVIDIA Blog · Katie Michel · 2026-11-11

Skip to content
	
	
		
			
			
	
			
	
As world leaders gather for COP31 in Türkiye, the event’s emphasis on zero waste puts a practical challenge in focus: how to keep products and materials in use for longer. Globally, less than 7% of the materials entering the economy come from recycled or reused sources. Municipal solid waste generation accounts for over 2 billion tons of trash per year — a figure that could nearly double by 2050.
AI and robotics are helping change this trajectory, as innovators around the globe improve sorting to recover resources that would otherwise end up in landfills.
“A more circular economy relies on making better use of what we already have,” said Josh Parker, head of sustainability at NVIDIA. “AI can help us understand what’s in a waste stream, identify what can be recovered and automate the work of sorting it. We’re giving innovators the computing tools to make those processes more effective and bring them to more places.”
See how four members of the NVIDIA Inception program for startups are applying AI to keep valuable materials in circulation.
AIRECO Gives Plastic Waste New Life
Recycled plastic is only used if its cost and quality can compete with new material. Too often it can’t: Incoming waste is of inconsistent quality, sorting depends on hard-to-find manual labor and mixed scrap ends up downcycled into low-grade products.
The founders of AIRECO, a Taiwan-based startup, believe that AI sorting can cut down the cost and improve the quality of recycling to make these materials more commercially useful. The company uses vision AI to sort plastics more finely, enabling materials to be plucked out of mixed scrap piles for closed-loop recycling, where used items are reprocessed into new versions of the same product. 
“The finer you sort, the more you can recycle,” said Chun-Feng Liu, founder and CEO of AIRECO. “With finely sorted material, it’s more likely that an item can stay in the loop — a plastic bottle recycled back into a bottle again and again, rather than ending up in other products that are hard to recycle further.”
The company uses NVIDIA Jetson Orin NX modules to run inference across its pilot line at a recycling plant in Tainan, including to drive robotic arms that pick targets off a conveyor belt. Recognition accuracy on the test line tops 95%.
In a full production line planned for next year, the team aims to nearly triple annual waste processing capacity from 18,000 to 48,000 tons while cutting operating costs by 85%.
EverestLabs AI Puts Robotics on the Recycling Line
At material recovery facilities, the plants that separate household recyclables, sorting must be done in real time at fast-moving conveyor belts — requiring rapid analysis to identify and sort items.
EverestLabs AI, a U.S. startup, deploys computer vision-guided robots on those sorting lines. About 150 robots are currently deployed in facilities across North America and Australia. 
“Other robots have infinite time to finish their tasks,” said R. Paul Singh, CEO of EverestLabs AI. “We don’t have that luxury because our conveyor belts are going to come in at a certain speed, and we have to act at a fast clip before the material moves. It’s a real-time game.”
EverestLabs runs AI inference on NVIDIA RTX GPUs at the edge and trains its models on NVIDIA data center GPUs, optimized using NVIDIA CUDA. The company estimates its deployed systems have so far identified about 40 billion objects, recycled roughly 25,000 tons of material and avoided about 30,000 metric tons of carbon dioxide emissions. 
Their team is constantly working to improve its models to correctly classify and pick every kind of object while capturing metadata about the material type, brand and packaging of each. They’re also shipping agentic AI tools to provide actionable data to recycling facility staff, from floor managers to executives responsible for multiple facilities — and are looking to extend that capability to adjacent industries.
Greyparrot Gives Recyclers a Clear View of the Waste Stream
Recycling plants can process tens of thousands of tons of waste a day, yet operators have long judged what’s on the belt by manually sampling less than 1% of it. 
U.K. startup Greyparrot built its Analyzer platform to change that. Mounted above conveyor belts, it uses computer vision to identify each passing object by material and brand, even in dusty environments or poor lighting on belts moving up to 4 meters a second.
“Waste changes all the time. It shifts by hour, by season, by supplier,” said Ambarish Mitra, cofounder of Greyparrot. “Before, operators guessed based on a tiny sample, and now they can see exactly what’s on the belt.” 
Greyparrot uses NVIDIA GPUs to train AI models on billions of objects, while NVIDIA Jetson modules run rapid detection at the edge. More than 300 Analyzer systems, operating in over 20 countries, have made over a trillion bounding box detections to date — reducing the time needed to check 15 tons of waste from 375 hours to just six. 
Facilities using the real-time data from Analyzer report efficiency gains of 10% to 30%. At global packaging company Amcor, the solution helped increase the yield of food-grade plastics by 12%. Brands including Coca-Cola, Colgate-Palmolive and Kenvue also use Greyparrot technology to measure how their packaging is recycled in real sorting plants.
reverse.fashion Gives Discarded Garments a Second Look
Europe generates nearly 7 million tons of used textiles a year. About a quarter of these textiles are collected separately and sorted by hand into hundreds of categories, destined for uses ranging from vintage resale to downcycling as furniture filling or cleaning cloths. The work is slow, costly and hard to staff, which keeps the value of reusable garments buried.
reverse.fashion, a Berlin-based startup, is helping automate the job with high-resolution computer vision. Its system identifies product type, defects, color, size, brand, fabric construction, season and style and assigns each garment to its most valuable category.
“Compared to classical waste sorting, our AI models have to run at very high resolution because humans are picky with textiles,” said Karsten Pufahl, cofounder and chief technology officer of reverse.fashion. “The computer vision pipeline needs to spot small defects to determine the quality and potential value of each garment.” 
As it moves across a conveyor belt at 3 meters a second, each textile analyzed by Reverse Fashion passes through over a dozen vision AI models optimized with NVIDIA TensorRT software and running on NVIDIA Jetson modules at the edge. The models are trained on NVIDIA GPUs in workstations and the cloud.
The system sorts in an hour what would’ve previously taken a week to sort, Pufahl estimates, and is currently rolling out to facilities in Europe.
Explore more NVIDIA-powered sustainability applications.
Related News
		
			
	
	
		NVIDIA Announces New Planned Investments in Korean Startups at the MSIT-NVIDIA AI Startup Partnership Forum	
	
	
	
		Korea’s AI Ecosystem Advances and Secures Agentic AI With NVIDIA	
	
	
	
		From Chips to Skills, NVIDIA and Korea Expand Sovereign AI Collaboration	
	
	
	
		NVIDIA Dynamo Recipes Bring Korea’s Leading Open Models to Production
