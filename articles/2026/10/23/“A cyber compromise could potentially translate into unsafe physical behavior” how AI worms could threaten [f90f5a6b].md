---
id: "f90f5a6bfa60f0e3"
title: "“A cyber compromise could potentially translate into unsafe physical behavior”: how AI worms could threaten cars and drones"
url: "https://tomsguide.com/ai/a-cyber-compromise-could-potentially-translate-into-unsafe-physical-behavior-how-ai-worms-could-threaten-cars-and-drones"
link: "https://tomsguide.com/ai/a-cyber-compromise-could-potentially-translate-into-unsafe-physical-behavior-how-ai-worms-could-threaten-cars-and-drones"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T06:30:00Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Elton Jones"]
language: "en"
summary: "null"
tags: ["AI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["robotics & autonomy", "safety & ethics", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2144
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/XBT6kL6LrAHtSJr8dVCzJN-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# “A cyber compromise could potentially translate into unsafe physical behavior”: how AI worms could threaten cars and drones

Tom's Guide · Elton Jones · 2026-10-23

“A cyber compromise could potentially translate into unsafe physical behavior”: how AI worms could threaten cars and drones
This cybersecurity expert explains the risks
Waking up to the latest news of AI doing something it wasn’t permitted to do that could put humanity at risk has become way too common.
The reports that have come in from OpenAI and Anthropic about their autonomous AI agents going rogue and displaying “problematic behavior” have been troubling. And learning about AI swarms coordinating hacks has been equally alarming. A recent study from Anthropic even warned about the possibility of AI models being able to replicate themselves across everyday smart devices, without needing access to data centers.
After Anthropic’s Frontier Red Team observed how small AI models could reproduce themselves as “AI worms” across off-brand Android TV boxes and smart ovens, it became clear that AI-powered malware could morph into the next major cybersecurity threat.
I wanted to know if AI worms could spread to other everyday smart devices, self-driving cars, humanoid robots and drones. Thankfully, Giuseppe Serio, VP Market Development at Upstream, gave me the answers I was looking for, as well as explaining how smart device manufacturers should confront the threat of AI worms.
Do you actually believe AI worms could turn everyday connected smart devices into a new kind of cybersecurity threat?
Yes, I believe this could become a real cybersecurity threat, although the concept itself is not new.
Worms and botnets have been around for decades. What AI changes is the ability of malicious software to understand and adapt to different environments with much less human intervention.
Traditionally, attackers had to develop or adapt their tools to work across different systems. AI could increasingly take over parts of that work, figuring out how a device operates, what software it runs and how to execute on it.
This could make attacks more scalable, especially across the millions of connected devices running different hardware and software.
Of course, AI doesn't magically bypass security. An attacker still needs a way into the device, whether through a vulnerability, exposed interface or weak security configuration.
Anthropic's research is still experimental. The models were slow, required considerable resources and were tested under simplified conditions. So we are not yet looking at a demonstrated real-world AI worm spreading across devices.
But the direction is important. As these capabilities improve, attackers could automate more of the work that previously required human expertise. And once such malware spreads across many devices without relying on a central server, detecting and containing it becomes more challenging.
The threat is not that worms suddenly become possible. It is that AI could make them more adaptive, easier to scale and harder to defend against.
Anthropic’s research demonstrated that small AI models could replicate across smart TVs. How realistic is it that a similar attack could spread between robots, self-driving cars or drones?
The risk is becoming more realistic, but we should distinguish between what Anthropic has demonstrated and what could happen in real Physical AI environments.
The interesting part of the research is not that software can spread between devices. We have seen that with malware and botnets for many years. What is changing is that AI can increasingly adapt to different hardware and software environments without requiring someone to manually develop each adaptation.
This is particularly relevant for Physical AI. Robots, connected vehicles and drones increasingly rely on onboard computing for perception, navigation, decision-making and other operational functions. They don't all run the same AI models. Some use computer vision, machine learning or specialized control algorithms, while newer robotic systems may also use vision-language-action models.
What makes these devices attractive is the combination of computing resources, connectivity and their role in real-world operations. However, spreading between such devices is not automatic. An attacker still needs a way in, sufficient access to run software and a path to other devices. How realistic this is depends on the architecture, security controls and connectivity of the fleet.
For example, a group of warehouse robots sharing the same network and management infrastructure could offer opportunities for an attacker to move between systems. In connected vehicles, separating critical functions and controlling software execution can make this considerably more difficult.
Anthropic has not demonstrated this type of attack against real Physical AI fleets. But the research shows how AI could make it easier to adapt attacks to different devices, potentially reducing the effort needed to compromise larger and more diverse environments.
And this is where the risk goes beyond traditional compute hijacking. In Physical AI, the same computing resources may also support functions that influence how machines operate. Depending on the architecture, a compromise could therefore affect availability, performance and potentially physical safety.
If an AI worm infected an autonomous vehicle or industrial robot, what could actually happen in the real world? Could it interfere with their obstacle detection, steering, braking or other critical functions?
The consequences could range from reduced performance and operational downtime to potentially serious safety risks. But it very much depends on how the system is designed.
An AI worm running on a robot or autonomous vehicle could consume computing resources that are also needed for perception, planning or navigation. This could slow down obstacle detection, delay decisions or cause the machine to stop operating.
However, we need to distinguish between disrupting a machine's operation and actually taking control of it.
Steering, braking and other safety-critical functions are often handled by separate controllers and protected by additional safety mechanisms. So compromising the AI compute doesn't automatically mean an attacker can manipulate these functions.
The risk becomes more serious when these systems are not sufficiently separated, or when the attacker can also access the interfaces that connect perception and planning with physical control.
In such cases, a cyber compromise could potentially translate into unsafe physical behavior.
This is what makes Physical AI different from traditional IT security. We are not only concerned about data loss or system availability, but also about how a cyber incident could affect the decisions and actions of a machine in the real world.
What warning signs could reveal that an AI worm is spreading through a fleet of connected machines? And how quickly would the manufacturers of those machines need to detect it to prevent a wider incident?
There are several warning signs manufacturers should look for. Unusual transfers of large AI models, unexpected communication between devices, increased GPU usage, battery or thermal anomalies, or delays in perception and planning.
But none of these signals alone necessarily means something is wrong.
For example, high GPU usage on a robot performing a complex task could be perfectly normal. The same activity on a parked robot running unknown software would be much more suspicious.
This is why we need to look at three things:
- The individual machine: Is it behaving differently compared to its normal behavior?
- Its operational context: Does the activity make sense for what the machine is supposed to do right now?
- The entire fleet: Are we seeing similar unusual activities across multiple machines, possibly indicating that something is spreading?
The fleet perspective is particularly important. What looks like a small anomaly on one device could become a clear indication of an attack when we connect the signals across hundreds or thousands of machines.
As for how quickly manufacturers need to detect it, there is no single answer. It depends on how fast the worm can spread and how the fleet is connected.
Ideally, detection needs to happen in near real time, before the infection reaches other devices. But detecting the threat is only part of the challenge. Manufacturers also need to identify which machines are affected and respond quickly without disrupting operations or creating additional safety risks.
This is why I believe Physical AI security needs to move beyond monitoring individual devices. It requires continuous visibility into how machines behave, what they are supposed to do and what is happening across the entire fleet.
If a manufacturer discovers an AI worm inside its fleet of connected machines, what should they do next? Can infected machines be isolated remotely without compromising safety or disrupting essential operations?
The first priority is to stop the worm from spreading without creating additional risks for the machines or their surroundings.
Unlike traditional IT systems, you cannot simply shut down a robot, vehicle or industrial machine while it is performing a critical task.
I would approach this in four steps:
- Understand the situation. Identify which machines are affected, what they are doing and how far the infection may have spread. At the same time, start containing the threat where it is safe to do so.
- Contain the spread. Restrict communication between affected machines and the rest of the fleet. This doesn't always mean disconnecting them completely. It depends on which connections are needed for safe operations.
- Bring machines into a safe state. Depending on the situation, a robot may need to finish a movement, a vehicle may need to stop safely, or an industrial machine may need to complete a controlled shutdown.
- Verify before restarting. Make sure the threat has been removed, the software and configuration are trusted, and the machine is operating as expected before returning it to service.
Remote isolation is possible in many environments, but it needs to be designed into the system from the beginning. Manufacturers need to know which functions depend on connectivity, which can operate independently and how machines respond when communication is restricted.
This is where Physical AI security becomes different from traditional IT security. We need to understand not only which machines are compromised, but also what they are doing at that moment and what the consequences of our response could be.
The objective is not simply to stop the cyberattack. It is to stop it without turning a security incident into a safety incident.
Do you think connected machine manufacturers are adequately preparing for self-replicating AI threats today? Or do you feel the industry is building increasingly autonomous machines faster than it is learning how to actually secure them?
I think the industry is moving in the right direction, but there is still a gap between how fast autonomy is developing and how we secure these systems.
We see quite different levels of maturity. Automotive manufacturers, for example, have made significant progress with secure-by-design, driven also by regulations such as UNECE R155. But when we look at robotics, drones and other Physical AI applications, the picture is much more mixed.
The bigger challenge is what happens after these machines are deployed. Securing a product when it leaves the factory is one thing. Continuously understanding what thousands of machines are doing in the field, detecting threats and responding without affecting their operations is something else.
And this is where I believe the industry still has work to do. We need to move from securing the machine itself to continuously verifying that it is behaving as intended, both individually and across the entire fleet.
Regulations such as the EU Cyber Resilience Act are helping to accelerate this shift. Manufacturers now face reporting obligations for actively exploited vulnerabilities and severe security incidents affecting their products. This makes ongoing visibility and the ability to investigate incidents increasingly important.
I also expect the CRA to influence cybersecurity practices beyond Europe, similar to what we have seen with UNECE R155 in automotive.
So yes, in some areas, autonomy is advancing faster than the security capabilities needed to protect it throughout its operational life. Anthropic's research is another reminder of why we need to close that gap now, rather than waiting for these threats to become a reality.
More from Tom’s Guide
- Google's AI chief says human-level AI could arrive by 2028 — and we're not ready
- OpenAI and Google just made an unexpected AI deal — here’s what it means for ChatGPT and Gemini
- Chatbots and agents like Muse are getting a face — but does that make us trust them more? Here's what this AI expert had to say
Elton Jones covers AI for Tom’s Guide, and tests all the latest models, from ChatGPT to Gemini to Claude to see which tools perform best — and how they can improve everyday productivity.
He is also an experienced tech writer who has covered video games, mobile devices, headsets, and now artificial intelligence for over a decade. Since 2011, his work has appeared in publications including The Christian Post, Complex, TechRadar, Heavy, and ONE37pm, with a focus on clear, practical analysis.
Today, Elton focuses on making AI more accessible by breaking down complex topics into useful, easy-to-understand insights for a wide range of readers.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
