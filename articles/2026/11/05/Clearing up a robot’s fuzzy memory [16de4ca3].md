---
id: "16de4ca3c25d3eed"
title: "Clearing up a robot’s fuzzy memory"
url: "https://news.mit.edu/2026/clearing-up-robot-fuzzy-memory-1105"
link: "https://news.mit.edu/2026/clearing-up-robot-fuzzy-memory-1105"
source: "MIT News"
domain: "news.mit.edu"
source_type: "research"
collector: "rss"
date: "2026-11-05T05:00:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Adam Zewe | MIT News"]
language: "en"
summary: "In an emergency, a human might someday ask a robotic assistant to fetch a wall-mounted defibrillator located down the hall. But if the robot has incorrectly labeled the defibrillator as a fire extinguisher in its stored memory, it may not know where to find the life-saving device. This robotic assistant could benefit from a new memory system created by MIT researchers. The system identifies…"
tags: ["Research", "Computer science and technology", "Algorithms", "Artificial intelligence", "Machine learning", "Robotics", "Computer vision", "Aeronautical and astronautical engineering", "Laboratory for Information and Decision Systems (LIDS)", "Electrical engineering and computer science (EECS)", "School of Engineering", "MIT Schwarzman College of Computing"]
orgs: ["OpenAI"]
topics: ["robotics & autonomy", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 999
paywalled: false
image: "https://news.mit.edu/sites/default/files/styles/news_article__cover_image__original/public/images/202611/MIT-Confident-Mem-01-press.jpg?itok=N_4ApjRl"
discussion_url: null
score: null
comments: null
community: null
---

# Clearing up a robot’s fuzzy memory

MIT News · Adam Zewe | MIT News · 2026-11-05

In an emergency, a human might someday ask a robotic assistant to fetch a wall-mounted defibrillator located down the hall. But if the robot has incorrectly labeled the defibrillator as a fire extinguisher in its stored memory, it may not know where to find the life-saving device.
This robotic assistant could benefit from a new memory system created by MIT researchers. The system identifies entries in a robot’s memory that might be wrong and corrects the descriptions of mislabeled objects.
In the future, this method could make household or industrial robots better able to perform complex, multistep tasks, such as clearing a dining room table or working alongside human collaborators to assemble a piece of machinery.
Called UQ-DAAAM (which stands for Uncertainty Quantification for Describe Anything, Anywhere, at Any Moment), the system compares multiple descriptions of the same object, seen from different viewpoints, to quantify the robot’s uncertainty about what it saw.
It then selects additional views to reduce the uncertainty and combines these captions into a more accurate description of the object, which it saves to memory.
The researchers also employed a special technique to streamline this process so a mobile robot can continually update uncertain memory entries in real time.
When compared to baseline methods, UQ-DAAAM boosted the robot’s confidence and improved the accuracy of its answers to questions about objects, their locations, and when it saw them.
“Contrary to ChatGPT, when we think about physical AI, it is not enough to simply put a disclaimer cautioning that sometimes the robot might be wrong. Allowing a robot to know what it doesn’t know is going to be essential for this technology to be deployed safely and have a positive impact on society,” says Luca Carlone, an associate professor in MIT’s Department of Aeronautics and Astronautics (AeroAstro), principal investigator in the Laboratory for Information and Decision Systems (LIDS), director of the MIT SPARK Laboratory, and the senior author of the paper presenting UQ-DAAAM.
He is joined on the paper by co-lead authors and MIT graduate students Harry Zhang and Nicolas Gorlo. The research will be presented at the Conference on Neural Information Processing Systems.
Amending memory
This new method builds on the researchers’ prior work, DAAAM, a robot memory system that uses a vision-language model (VLM) to richly describe objects in scenes a robot captures with its onboard cameras. These descriptions are stored as detailed captions in a 3D map-based representation of the robot’s environment that it can call upon later to answer questions.
But the robot sometimes sees objects only partially or from far away, or its camera might capture blurry or poorly lit images. In these cases, DAAAM might describe these objects incorrectly, such as by mistaking a gray chimney for a squirrel perched on a rooftop.
“With no way to correct itself, this wrong memory would persist as the robot proceeds in its environment, which could impact downstream applications,” Zhang says.
UQ-DAAAM integrates uncertainty quantification into the DAAAM framework. It allows the robot to measure its confidence in the accuracy of object descriptions and fix incorrect captions as it travels through an environment.
While on the move, the robot constantly collects and stores images of the world around it. Many of these images show the same objects captured from different angles. UQ-DAAAM uses these additional viewpoints to identify and correct unreliable descriptions.
First, it calculates the VLM’s confidence level in the words it generated to describe a potentially mislabeled object. Then, it measures consistency by comparing this description to captions of images that describe the same object from different vantage points.
“We fuse both sources of uncertainty into a single number that captures how certain the VLM is in its overall understanding of the object,” Carlone explains.
If that number exceeds a certain threshold, the uncertainty is too high, and UQ-DAAAM will refine the caption by using additional images of the object.
It does this using a heuristic, or simple rule, that determines which additional viewpoints will reduce the robot’s uncertainty about the object. For instance, it might choose an image captured a few frames later that clearly shows smoke emanating from the chimney.
The researchers mathematically proved that this heuristic can identify the best frames to select without rerunning the VLM, dramatically reducing the amount of computation.
“The key challenge Nico and Harry had to overcome is how to combine VLMs with uncertainty quantification into something that is running in a fraction of a second on a robot that is moving,” Carlone says.
Remembering with confidence
Once it has identified additional captions that will reduce its uncertainty about the object, the system uses an LLM to fuse them into a single object description. To boost accuracy, the LLM puts more weight on new captions and those with less ambiguity.
This refinement step is able to resolve ambiguities for about 92 percent of the objects in the robot’s environment, while only requiring two additional captions per object. It increased the accuracy of object descriptions by 5 percent compared to the state of the art.
UQ-DAAAM also provided more accurate answers to questions about the objects it observed, where it saw them, and when it last encountered them than baseline methods.
“Performing this uncertainty quantification procedure across the entire map the robot generates allows it to improve its understanding of what it has observed,” Gorlo says.
Next, the researchers want to use UQ-DAAAM to guide different types of robots, like mobile robotic manipulators, and apply their uncertainty quantification techniques to other domains.
In addition, they are studying the use of UQ-DAAAM to identify areas of high uncertainty the robot could revisit to improve its understanding of the environment. They are also exploring uncertainty quantification in systems that predict the future state of a robot’s environment.
This research is supported, in part, by the U.S. Army Research Laboratory and the U.S. Office of Naval Research. Carlone is currently on sabbatical as an Amazon Scholar; this article describes work performed at MIT and is not associated with Amazon.
