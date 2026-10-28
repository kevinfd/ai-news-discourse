---
id: "1698e31ea5a4be3f"
title: "Your Robot’s Safety Functions Already Work. What If the Input Lies?"
url: "https://spectrum.ieee.org/ai-robot-safety-cybersecurity-vicone"
link: "https://spectrum.ieee.org/ai-robot-safety-cybersecurity-vicone"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T16:14:39Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["VicOne"]
language: "en"
summary: "This article is brought to you by VicOne . A mobile robot slows for someone in a hallway. A collaborative arm eases its movement as a worker approaches. A humanoid pauses to let a person pass. Each response depends on information about the robot or its surroundings: a distance reading, a position estimate, or a stop signal. But what happens when one of those inputs is wrong, and the robot still…"
tags: ["Humanoid-robots", "Type-sponsored", "Cybersecurity", "Physical-ai", "Robot-safety", "Ai-robots"]
orgs: ["Nvidia", "China"]
topics: ["robotics & autonomy", "safety & ethics", "jobs & society", "models & research"]
content_source: "fulltext"
word_count: 1249
paywalled: false
image: "https://spectrum.ieee.org/media-library/humanoid-robot-and-robot-dog-meet-a-woman-on-a-sunny-terrace-at-sunset.jpg?id=68002098&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Your Robot’s Safety Functions Already Work. What If the Input Lies?

IEEE Spectrum · VicOne · 2026-10-27

This article is brought to you by VicOne.
A mobile robot slows for someone in a hallway. A collaborative arm eases its movement as a worker approaches. A humanoid pauses to let a person pass. Each response depends on information about the robot or its surroundings: a distance reading, a position estimate, or a stop signal.
But what happens when one of those inputs is wrong, and the robot still responds exactly as designed? The mobile robot reads the hallway as clear while someone is still there. The arm estimates that the worker is farther away. The humanoid does not receive a stop signal as a person crosses its path.
In each case, a fault could cause that mismatch. So could deliberate manipulation.
At VicOne LAB R7, we examine how manipulated inputs can change robot behavior — and what that means for the systems meant to keep people safe.
How an untrusted input can change a robot’s behavior
A robot does more than measure its surroundings. It may interpret what it sees and hears to decide what to do next. Information placed in its environment can therefore influence its actions.
Published research shows how this can happen. In a study of vision-language-action (VLA) models, a patch in a camera’s view reduced task success in simulated robot tests. FreezeVLA found that an adversarial image could cause tested models to ignore later instructions. Although the studies used different methods, both demonstrate how visual input can interfere with a robot’s intended task.
In a robot-dog test using Gemma 4 E4B, text on a poster was treated as an instruction and changed the robot’s movement.
VicOne LAB R7 also tested how untrusted inputs could change robot behavior. In a robot-dog test using Gemma 4 E4B, text on a poster was treated as an instruction and changed the robot’s movement. In a separate hospital-service-robot simulation using Nemotron on NVIDIA Jetson AGX Orin, crafted audio that is inaudible to people changed the robot’s simulated behavior. The assigned tasks did not change; the inputs did.
In a VicOne LAB R7 test, text on a poster changed a robot dog’s movement, illustrating how a crafted input can turn an unlikely outcome into a repeatable attack.VicOne
Safety-related decisions have inputs too
An independent protective system may still stop a dangerous action. But that system also depends on information: readings, estimates, and messages that tell it when to intervene. What happens if one of those inputs is manipulated?
At a robotics bug bounty event, VicOne LAB R7 researchers injected a ROS 2/DDS message into a robot that organizers expected to remain still under a safe-control setting. The robot moved.
A humanoid’s balance controller offers another example. If it relies on a vulnerable gyroscope, sound at the sensor’s resonant frequency could distort its reported rotation. The controller might correct for a tilt that never occurred. Researchers demonstrated the underlying acoustic attack against drones with vulnerable gyroscopes. The research did not demonstrate the same attack chain causing a humanoid to fall.
Other protections could interrupt either chain. The question for safety and security teams is whether those protections detect the danger independently or depend on the same manipulated information.
Figure 1. VicOne maps how accidental faults and deliberate cyber manipulation can lead to similar robot safety outcomes, from loss of control to physical harm.VicOne
Deliberate attacks challenge safety assumptions
A safety assessment may treat a combination of accidental faults as unlikely. Deliberate manipulation changes that assumption. An attacker can choose when to introduce a false input and repeat the same trigger. That does not make harm inevitable, but it may change how cyber risks should be assessed.
Redundant sensors also need an adversarial test. If one action can affect both inputs, their agreement may offer less reassurance than expected. In autonomous driving research, a crafted physical object misled a system combining camera and LiDAR perception. The study does not establish a weakness in a particular robot, but it shows why teams should test whether one manipulation can affect several checks at once.
Cyber threats add intent to the safety equation, so risk assessments based on accidental faults must be revisited to account for attacks that can be timed and repeated.
Security testing strengthens robot safety evidence
Safety teams set limits for speed, protective distances, and permitted operating areas. The evidence behind those limits should also show what happens when the information used to enforce them is deliberately manipulated.
That evidence can also support assessments against applicable requirements. China’s GB/T 45502-2025 addresses information security for service robots. IEC TS 63074 examines security threats that could affect safety-related control systems. The EU Machinery Regulation, which applies from January 20, 2027, includes requirements to protect safety-relevant systems and data against corruption. Each has its own scope, and teams still need evidence for their robot’s design and operating conditions.
Figure 2. Cybersecurity strengthens robot safety evidence throughout the lifecycle. VicOne helps teams test safety limits against manipulation before deployment and monitor the conditions behind safe behavior in operation.VicOne
Before deployment, safety and security engineers can compare normal and adversarial scenarios against the same safety limits. During operation, they can monitor for changes to software, models, sensor signals, or behavior that may call earlier results into question. Any response to suspicious behaviors should follow policies approved by the safety team.
VicOne supports that work across the robot lifecycle. Through the Robotic Hacking Community, VicOne LAB R7 works with researchers to investigate how cyber threats can change robot behavior. VicOne’s Radeis helps teams validate potential effects before deployment, while Rthena provides visibility into risks and behavior during operation.
Five questions safety and security teams should answer together
The central test is whether a robot’s safeguards still protect people when the information they rely on is manipulated. Safety and security teams can begin by tracing the inputs behind each protective decision, challenging them, and revisiting the evidence as the robot changes. They can start with these five questions:
1. What does each protective function read? Map the readings, estimates, messages, and confirmations. Identify which safeguards operate independently of the robot’s AI decisions.
2. How does that information arrive? Check how inputs are produced, transmitted, authenticated where appropriate, and handled when they are missing or implausible.
3. What happens if an input is manipulated? Test false distances, drifting position estimates, and other relevant scenarios against the robot’s safety limits.
4. Can one action mislead several inputs? Check whether sensor fusion or seemingly independent safeguards share a point of failure.
5. When should the evidence be revisited? Reassess after changes to software, models, sensors, or operating conditions. Agree on bounded responses to suspicious behavior with the safety team in advance.
The goal is not only to show that a protective function works. Teams also need evidence that it remains protective when the information behind its decision is wrong or deliberately manipulated — and that another safeguard can catch the resulting hazard when needed. As robots change, that evidence needs to change with them.
For a deeper look how cybersecurity can affect robot safety, download our white paper “Why Robot Safety Depends on Cybersecurity: Protecting the Information That Safety Decisions Rely On.”
VicOne is a Physical AI cybersecurity company protecting vehicles and robots from cyber threats that can alter behavior and compromise safety. Headquartered in Tokyo, Japan, the company provides automotive and robotics organizations with software and services to identify cyber risks early, assess their potential safety impact, and protect systems in operation, helping maintain safe, reliable behavior across real-world deployments.
