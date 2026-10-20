---
id: "627a7a57a189cc8d"
title: "World's fastest AI-powered racing drone outflies the best human pilots"
url: "https://livescience.com/technology/robotics/the-worlds-fastest-ai-powered-racing-drone-outflies-the-best-human-drone-pilots"
link: "https://livescience.com/technology/robotics/the-worlds-fastest-ai-powered-racing-drone-outflies-the-best-human-drone-pilots"
source: "Live Science"
domain: "livescience.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T11:51:43Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["JackFisherBooks"]
language: "en"
summary: "World's fastest AI-powered racing drone outflies the best human pilots\nAn AI-operated drone learned to fly from scratch and navigated a race course at speeds over 60 mph, using a single camera.\nA drone powered by artificial intelligence (AI) has completed a championship race course faster than some of the world's best human drone pilots.\nIn a study published Oct. 14 in the journal Science…"
tags: ["r/singularity"]
orgs: []
topics: ["robotics & autonomy", "models & research", "health & science", "chips & infrastructure"]
content_source: "fulltext"
word_count: 967
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xaq1yl/worlds_fastest_aipowered_racing_drone_outflies/"
score: null
comments: null
community: "r/singularity"
---

# World's fastest AI-powered racing drone outflies the best human pilots

Live Science · JackFisherBooks · 2026-10-20

World's fastest AI-powered racing drone outflies the best human pilots
An AI-operated drone learned to fly from scratch and navigated a race course at speeds over 60 mph, using a single camera.
A drone powered by artificial intelligence (AI) has completed a championship race course faster than some of the world's best human drone pilots.
In a study published Oct. 14 in the journal Science Robotics, scientists created an AI system capable of pushing a quadcopter through a demanding course at over 60 mph (100 km/h), using little more than a single forward-facing camera, an inertial measurement unit, and a tiny onboard computer.
The system, called MonoRace, even won the 2025 Abu Dhabi Autonomous Racing League drone racing competition, outperforming every rival autonomous team and posting faster times than three former human world-champion drone pilots.
MonoRace accomplished this without the aid of GPS, external motion-capture systems, stereo cameras, or a preloaded map of the course. The system is an onboard autonomous flight model created by researchers at the Delft University of Technology's Micro Air Vehicles Lab in the Netherlands. Its name reflects its central design feature; "mono" refers to its monocular vision. The drone relies on a single rolling shutter camera and monitors its own motion with an internal measurement unit (IMU) that gauges acceleration and rotation.
Flying at breakneck speeds
The limited sensor package feeds a neural network, a machine-learning model that uses interconnected artificial neurons to learn patterns from data. This neural network identifies racing gates and estimates the drone's position and motion to generate motor commands. Then, it sends the commands to the four propellers at a rate of 500 times per second through the drone's flight controller.
The system fits a drone that weighs a mere 966 grams (2.13 pounds) and measures approximately 11.8 x 11 x 3.9 inches (30 x 28 x 10 centimeters). Because the MonoRace hardware was so compact, lightweight and computationally efficient, the team was able to operate it entirely aboard the drone.
On the Abu Dhabi course, MonoRace completed two laps around 11 gates in 16.56 seconds, hitting a top speed of approximately 63 mph (102 km/h).
Get the world’s most fascinating discoveries delivered straight to your inbox.
A recently released video tracks MonoRace's development and performance in the competition, with real flight sequences demonstrating how the drone banks sharply, accelerates through gates, and navigates a course without human assistance.
However, some of the sequences are computer-generated. Study co-author Guido de Croon, a professor at the Delft University of Technology, said those are intentional visual effects. The only fully simulated imagery appears at about the two-minute mark, during the segment showing the training process.
"Here we show the gates in a visual simulator for the video but the real training happened in a stripped-down, pure physics simulator that ran really fast," de Croon told Live Science in an email. "Simulating vision was not done during training, as the control neural network receives an estimated state as input, which comes from a different perception and state estimation process."
The rest of the footage is real, although some shots include overlays showing how the drone interprets its camera feed. A convolutional neural network segments the white gates, sometimes displaying them as red in the normal camera image. Small circles mark detected gate corners, red lines indicate gate edges, and a blue overlay shows the portion of the image where the drone expects to find the next gate.
How the AI learned to race
Scientists trained the MonoRace model with reinforcement learning, a machine learning method in which an agent repeatedly attempts a task and receives feedback based on its success or failure.
"The reinforcement learning ran in simulation, because it needs lots of trial and error — like millions of tries," de Croon said. "It actually learns to fly from scratch."
The network learned to translate the drone's position on the track, velocity and orientation directly into motor commands. According to de Croon, early training focused on the basics, like avoiding crashes and reaching the first gate. As the training progressed, the system learned to advance farther along the course and fly at higher speeds.
The researchers didn't train the system on a single aircraft. Instead, they varied dimensions such as weight, voltage, drag, sensor noise and propeller condition so the AI model could cope with real-world variations and imperfections.
"That ensures that the trained network can control different drones," de Croon said.
Related stories
MonoRace could become a training tool for human drone pilots, "a bit like powerful chess programs have also inspired humans playing the game," de Croon said.
Its broader significance lies in demonstrating advancements in physical AI, especially how a robot can perceive, decide and act at high speeds despite limited sensing and computing power. The control network runs on a microcontroller-class chip, meaning that sophisticated control doesn't require a large computer.
De Croon noted that a similarly sized network could optimize for minimal energy use rather than minimum lap time. Because most machines rely on small processors and conventional controllers, energy-optimal neural control could eventually reduce power consumption in everyday robotics, he said.
Bahnam, S. A., Ferede, R., Blaha, T. M., Lang, A. E., Lucassen, E., Missinne, Q., Verraest, A. E. C., De Wagter, C., & De Croon, G. C. H. E. (2026). MonoRace: Robust monocular AI for champion-level drone racing. Science Robotics, 11(119). https://doi.org/10.1126/scirobotics.aee9250
Alan is a freelance tech and entertainment journalist who specializes in computers, laptops, and video games. He's previously written for sites like PC Gamer, GamesRadar, and Rolling Stone. If you need advice on tech, or help finding the best tech deals, Alan is your man.
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
