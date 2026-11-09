---
id: "8422634c9a069030"
title: "A single AI model simulates the behavior of many substances, from sliding sand to folding proteins"
url: "https://news.mit.edu/2026/single-ai-model-simulates-many-substances-behavior-1109"
link: "https://news.mit.edu/2026/single-ai-model-simulates-many-substances-behavior-1109"
source: "MIT News"
domain: "news.mit.edu"
source_type: "research"
collector: "rss"
date: "2026-11-09T05:00:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Adam Zewe | MIT News"]
language: "en"
summary: "Today, a scientist who wants to simulate a physical process must pick the right tool for that one job, such as a solver built for flowing water or another designed to model the way a protein folds. Each one is hand-coded around the specific equations that dictate how that process behaves. Researchers at MIT, the University of British Columbia (UBC), and elsewhere have now replaced that patchwork…"
tags: ["Research", "Computer modeling", "Artificial intelligence", "Machine learning", "Simulation", "Computer graphics", "Human-computer interaction", "Design", "Electrical engineering and computer science (EECS)", "Computer Science and Artificial Intelligence Laboratory (CSAIL)", "School of Engineering", "MIT Schwarzman College of Computing"]
orgs: ["UK", "OpenAI", "Meta"]
topics: ["models & research", "health & science", "jobs & society"]
content_source: "fulltext"
word_count: 1077
paywalled: false
image: "https://news.mit.edu/sites/default/files/styles/news_article__cover_image__original/public/images/202611/MIT-WorldParticle-01-Press.jpg?itok=kwMpBg6F"
discussion_url: null
score: null
comments: null
community: null
---

# A single AI model simulates the behavior of many substances, from sliding sand to folding proteins

MIT News · Adam Zewe | MIT News · 2026-11-09

Today, a scientist who wants to simulate a physical process must pick the right tool for that one job, such as a solver built for flowing water or another designed to model the way a protein folds. Each one is hand-coded around the specific equations that dictate how that process behaves.
Researchers at MIT, the University of British Columbia (UBC), and elsewhere have now replaced that patchwork with a single deep-learning system, called WorldParticle, that could help engineers model different physical phenomena, from sliding sand to folding proteins, with one unified artificial intelligence architecture.
Scientists and engineers could use this system to model processes that typically require separate simulators, such as a fluid sloshing against a deformable solid. This could offer a faster, more accurate way to simulate how sloshing oil might impact an elastic valve in a storage tank, for instance. It could also help engineers study where and how granular materials, like sand or soil, could move when a soft robot touches them.
The system represents every material it simulates, from a dune of sand to a protein molecule, as tiny particles and predicts where those particles will move one step at a time. Because it learns the underlying dynamics rather than being programmed with an equation, the model can adapt to materials, forces, and environments it never encountered during training.
In the long term, the researchers hope this work helps scientists discover new materials and explore physical processes they would be unable to effectively study with existing simulation methods.
“We want to have a GPT moment for simulation,” says Peter Yichen Chen, a former MIT postdoc who is now an assistant professor at UBC, and is a co-corresponding author of an open-access paper on this technique. “Every time people want to build a simulator for a particular physical phenomenon, they need to code it up from scratch. Our vision is to have a foundation model that works out of the box for any scenario you want to simulate. This is a first step in that direction.”
Chen is joined by co-corresponding and co-lead author Minghao Guo, an MIT postdoc; co-lead authors Caoliwen Wang and Siyuan Chen, UBC graduate students; Wojciech Matusik, an MIT professor of electrical engineering and computer science who leads the Computational Design and Fabrication Group within the Computer Science and Artificial Intelligence Laboratory (CSAIL); and others at UBC, Georgia Tech, Inria, Meta, the University of Pennsylvania, the University of Utah, the University of California at Los Angeles, and the University of Hong Kong. The research will be presented at the ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia.
Unified simulation
For this work, the researchers drew inspiration from world models. These powerful AI systems learn the rules that govern the physical world so they can predict how objects or environments will change over time in response to certain actions or conditions.
The researchers applied these concepts to develop a unified AI architecture that can simulate multiple types of physical phenomena.
“If you study deformable objects and fluids, you would need two simulators — one for each physical regime. But if you unify them into one model, maybe you could couple the physics of these two processes and gain insights into new problems?” Guo says.
WorldParticle breaks an object into thousands or millions of tiny, three-dimensional dots, or particles, using what is known as a Lagrangian representation. It tracks the movement and velocity of the particles over space and time to simulate the material’s dynamics.
Typically, when scientists model materials and physical processes using Lagrangian particles, they use a governing equation that defines the fundamental laws which control how that material behaves over time and space. They must convert that complex equation into a formula a numerical solver can handle, repeating these steps for each material and process they want to model.
Instead, the researchers designed a neural network that learns to solve governing equations in general, eliminating the need to design a new model and solver to handle each one.
Once WorldParticle converts an object into particles, a neural network takes the 3D positions and physical properties of the particles as inputs. It outputs their positions and properties for the next frame of the simulation, predicting the material’s motion over time and space in one-second increments.
“It is a similar architecture to ChatGPT. But instead of predicting one word at a time to write a piece of text, we are predicting how these particles will move, one step at a time,” Chen says.
Before each simulation step, WorldParticle separates the external forces that affect the physical system, like impulse forces that affect an ocean wave when it slams into a seawall.
After predicting the initial states of the particles, WorldParticle integrates the external forces back into the simulation, correcting its particle predictions based on how those forces affect the object’s behavior. In this way, the system can generalize to unseen materials, changing environmental conditions, and varied forces.
A general, scalable framework
But because a complex object could be broken into millions of particles, the problem quickly becomes too computationally intensive for the model to handle.
To streamline processing, the researchers employed a merging technique to combine and compress particles while still allowing WorldParticle to capture fine-grained details of their behavior.
“We needed to do a lot of detailed engineering and employ many tweaks to the architecture for it to be truly generalizable and scalable,” Guo says.
They demonstrated WorldParticle by modeling six different physical phenomena, including deformable objects, granular materials, and proteins, with higher accuracy than numerical simulation methods.
For instance, WorldParticle effectively captured how a granular object would collapse into a pile while some baseline methods left sand particles floating in the air. Their method also modeled how protein structures change over time about 100 times faster than numerical simulators, Guo adds.
The general-purpose framework could be applied to many materials and processes, including soft robot manipulation tasks, RNA evolution, and astrophysical phenomena like the merging of galaxies, the researchers say.
Moving forward, they want to adapt WorldParticle to simulate these and other physical systems. They also want to build on this work toward the development of a full, general-purpose simulation pipeline for scientific discovery.
“We see the unification of computation and science giving us new insights and tools to discover physical phenomena or explain some unexplainable physical phenomena,” Guo says. “With a unified model, we could unlock many discoveries that we can’t even imagine.”
