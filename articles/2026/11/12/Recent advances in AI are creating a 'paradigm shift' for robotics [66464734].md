---
id: "66464734b1d1a922"
title: "Recent advances in AI are creating a 'paradigm shift' for robotics"
url: "https://news.berkeley.edu/2026/11/09/recent-advances-in-ai-are-creating-a-paradigm-shift-for-robotics"
link: "https://news.berkeley.edu/2026/11/09/recent-advances-in-ai-are-creating-a-paradigm-shift-for-robotics"
source: "Berkeley News"
domain: "news.berkeley.edu"
source_type: "community"
collector: "reddit"
date: "2026-11-12T17:00:35Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["LiminalEntityX"]
language: "en"
summary: "TLDR: UC Berkeley robotics professor Ken Goldberg says recent AI advances are creating a “true paradigm shift” in robotics. AI agents can now generate robot-control programs, build physics simulations, test them, learn from failures and improve their own code before deploying it on real machines. After witnessing a robot use its own failed attempt to improve its simulation and try again,…"
tags: ["r/singularity"]
orgs: ["Nvidia", "OpenAI"]
topics: ["robotics & autonomy", "agents & coding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1043
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xui5dq/recent_advances_in_ai_are_creating_a_paradigm/"
score: null
comments: null
community: "r/singularity"
---

# Recent advances in AI are creating a 'paradigm shift' for robotics

Berkeley News · LiminalEntityX · 2026-11-12

Recent advances in AI are creating a ‘paradigm shift’ for robotics
Professor Ken Goldberg has long had doubts about how quickly robot capabilities could advance. But new AI models are leading to robotic innovations that give him "goosebumps."
November 9, 2026
In recent months, artificial intelligence agents that can reason, plan and use external tools to accomplish multistep tasks have already reshaped computer coding, online shopping, dinner reservations and cyberattacks.
Robotics might be next.
Ken Goldberg, a UC Berkeley roboticist and professor of engineering, said new models make it possible for teams of AI agents to develop robot-control programs, test them in simulated environments and revise the code when something doesn’t work.
Goldberg, with Spencer Huang, director of robotics engineering at NVIDIA, and a team of researchers call the new approach “agentic robotics.” They said it could offer a way around two obstacles in the field: the enormous amounts of data needed to train robots and the intense engineering efforts required to program them, both of which can demand vast amounts of physical and technical resources to accomplish.
“Agentic robotics is a fundamental shift in how robots are controlled,” Goldberg said. “Instead of collecting massive amounts of data and hand-tuning every behavior, teams of agents can quickly generate, test and refine robot programs that allow human engineers to interpret how the programs work for fine-tuning and verification.”
Goldberg, who was recently inducted into the National Academy of Engineering, is presenting the new approach and results from months of testing this week at the Conference on Robot Learning. He and his team are also releasing open-source code for other roboticists to experiment with, built on NVIDIA’s Isaac open simulation framework for developers, as well as an industry-standard benchmark for evaluating the performance of robots across industrial tasks.
Goldberg and Huang said the goal is to make robot programming faster and more adaptable while preserving the structure needed for reliable industrial systems.
“Robots are advancing quickly, but developing them for real-world environments remains slow, data-intensive and difficult to scale,” Huang said. “Working with UC Berkeley, NVIDIA is helping advance a new approach combining agentic AI, simulation and open industrial task-focused benchmarks to help developers rapidly test and improve robot behavior before deployment.”
Traditionally, engineers can directly program the software that tells robots how to perceive objects, plan movements and control their actions, a process called model-based robotics. Or, with model-free robotics, they can train robots to learn behaviors from demonstrations through imitation learning. The first approach requires extensive engineering, while the second needs enormous amounts of data and time.
The problem is there’s no easy way to collect that much information to train robots on. In an attempt to reset public expectations last year, Goldberg said that a “100,000-year data gap” would prevent robots from gaining real-world skills as quickly as AI agents have gained language fluency over the past several years. Those AI agents, after all, were trained on an immense amount of internet text and image data for which there is no parallel in robotics.
“I was discouraged by the daunting amount of data that we would need to collect,” Goldberg said. “Agentic robotics provides a missing link between model-based and model-free methods. It’s a way forward that doesn’t require any additional data.”
Earlier this year, he and his team began experimenting with a change to the way the robot code is organized. Using a framework they called Graph-as-Policy, robot tasks are segmented into individual skills, such as finding an object, planning a grasp and moving the gripper without collisions. Goldberg likened it to individual building blocks that fit together into something much larger.
Then, AI agents generate and connect these skills into a robot program. Using NVIDIA’s Isaac simulation libraries, the agents autonomously rehearse the program across task variations, identify where failures happen and refine the approach before deployment.
OpenAI’s recent release of its Astra model made the process even more promising, Goldberg said. His postdoctoral students Eric Kaiyuan Chen and Shuangyu Xie gave Astra access to their simulation interface and a short video of a real robot whose assignment was using a sponge to wipe ink off a metal bar. In less than an hour, the AI tool created and fine-tuned a physics simulation that accurately reproduced the video, including very realistic deformations of the sponge.
The researchers then gave the AI that simulation and their Graph-as-Policy framework. The AI generated a robot-control program and repeatedly tested and improved it in simulation. When the researchers ran the resulting code on a real robot, it worked.
In one trial, Goldberg said, the robot pushed over the metal bar because it did not reliably infer its mass. The misstep created new evidence for the agent to review and illustrated the edge provided by agentic robotics: The AI could use video of the failed attempt to improve its simulation, revise the robot’s control program and test a new approach.
“This is when I got goosebumps,” Goldberg said.
Berkeley-based Ambi Robotics, which specializes in logistics and warehouse order fulfillment, applied the new methods earlier this year to analyze parcel sorting data and test updates to robot behavior. Tests showed an increased capacity of over 15,000 packages sorted annually per robot; the change is now deployed across 30% of the company’s U.S. fleet.
“AI-powered industrial robots must continuously improve reliability and performance,” said Jeff Mahler, Ambi Robotics’ co-founder and chief technology officer. “Agentic robotics converted production data into robot behavior updates, increasing throughput across our U.S. fleet while keeping engineers in control.”
Goldberg said the implications are already promising in industrial settings, where tasks are repetitive and at-scale. He said not to expect home assistants to fold laundry — yet — but the ability to self-improve key elements of tasks is a major leap forward in the field.
It’s also an exciting time for him and his students. He said he can think of only two moments in his 40-year robotics career that have elicited similar feelings: the public release of the World Wide Web in 1993 and the debut of ChatGPT in 2022.
“Agentic robotics combines classical control theory and physics with rapidly evolving agentic coding,” Goldberg said. “It’s fast and practical for real engineering applications. My sense is that it’s a true paradigm shift.”
