---
id: "d41e6885a08966f6"
title: "Learning to Play Like a Pro: Adaptive Motion Planning and Tracking for Humanoid Robots"
url: "https://content.knowledgehub.wiley.com/learning-to-play-like-a-pro-adaptive-motion-planning-and-tracking-for-humanoid-robots"
source: "IEEE Spectrum"
domain: "content.knowledgehub.wiley.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-12T10:00:03Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Noitom Robotics"]
language: "en"
summary: "This White Paper provides roboticists and control engineers with a comprehensive overview of how motion planning and motion tracking can be decoupled to preserve professional athletic style in humanoid robots, and why adaptive, speed-aware control is essential for closing the gap between simulation and real-world deployment. What you will learn about: Why combining a professional athlete’s…"
tags: ["Type-whitepaper", "Humanoid-robots", "Motion-tracking", "Motion-planning"]
orgs: []
topics: ["robotics & autonomy", "models & research"]
content_source: "fulltext"
word_count: 353
paywalled: false
image: "https://assets.rbl.ms/68382463/origin.png"
discussion_url: null
score: null
comments: null
community: null
---

# Learning to Play Like a Pro: Adaptive Motion Planning and Tracking for Humanoid Robots

IEEE Spectrum · Noitom Robotics · 2026-10-12

Download this complimentary White Paper today!
This White Paper provides roboticists and control engineers with a comprehensive overview of how motion planning and motion tracking can be decoupled to preserve professional athletic style in humanoid robots, and why adaptive, speed-aware control is essential for closing the gap between simulation and real-world deployment.
What you will learn about:
- Why combining a professional athlete’s motion style with reliable task performance remains an open challenge in humanoid ball-sports robotics, and how separating a high-level planner from a low-level tracker addresses this trade-off.
- How motion data extracted from broadcast video and motion-capture recordings can be reconstructed, retargeted, and physically corrected into reference motions a humanoid robot can safely track.
- Why the sim-to-real transition introduces compounding tracking errors, and how training a tracker on randomized execution speeds, paired with a learned motion-speed adapter in the planner, improves robustness on physical hardware.
- How this adaptive framework was validated across two humanoid platforms, including full-size, in-the-wild serving performed without any motion-capture system.
Click ‘LOOK INSIDE’ to Download Now.
LOOK INSIDE
IEEE Spectrum and Wiley are proud to bring you this White Paper, sponsored by Noitom Robotics
More Information
Humanoid robots have begun to show real capability in ball sports, but preserving a professional athlete’s motion style while maintaining reliable task performance is still an unresolved problem. This guide examines an adaptive motion planning and tracking framework that learns tennis serving and rally styles directly from broadcast video and motion-capture data. A hierarchical design separates a planner, which generates stylistic kinematic motion, from a tracker, which executes that motion with minimal interference. Because tracking performance inevitably degrades when a policy trained in simulation moves to physical hardware, the framework trains its tracker on randomized execution speeds and conditions its planner on a learned motion-speed representation, reducing the compounding errors introduced by autoregressive planning and noisy perception. The paper documents real-world validation on a research humanoid platform and transfer to a full-size humanoid robot, including serving in an uncontrolled environment without motion capture, and closes with practical, transferable lessons for engineers building future humanoid ball-sports systems.
Sponsored by
