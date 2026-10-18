---
id: "36ba0aef514a47f2"
title: "Meet Kyutai REKI: The 2.4B VLA Model Bringing Efficient Memory to Robot Manipulation"
url: "https://marktechpost.com/2026/10/17/meet-kyutai-reki-the-2-4b-vla-model-bringing-efficient-memory-to-robot-manipulation"
link: "https://marktechpost.com/2026/10/17/meet-kyutai-reki-the-2-4b-vla-model-bringing-efficient-memory-to-robot-manipulation"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-17T20:22:11Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Kyutai, with Inria and École des Ponts, has released REKI , a 2.4B vision-language-action model (VLA) for robot manipulation. The REKI vision-language-action model is pretrained only on public data. It also carries a cheap memory of its recent past. On three out-of-distribution benchmarks, only models about twice its size beat it. All weights are live on Hugging Face today. \n\n TL;DR \n\n Size:…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Embedding Model", "Harness", "Language Model", "Large Language Model", "New Releases"]
orgs: ["Alibaba", "Nvidia", "Hugging Face"]
topics: ["models & research", "robotics & autonomy", "chips & infrastructure", "policy & regulation"]
content_source: "summary"
word_count: 877
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Kyutai REKI: The 2.4B VLA Model Bringing Efficient Memory to Robot Manipulation

MarkTechPost · Asif Razzaq · 2026-10-17

Kyutai, with Inria and École des Ponts, has released REKI , a 2.4B vision-language-action model (VLA) for robot manipulation. The REKI vision-language-action model is pretrained only on public data. It also carries a cheap memory of its recent past. On three out-of-distribution benchmarks, only models about twice its size beat it. All weights are live on Hugging Face today. 

 TL;DR 

 Size: 2.4B parameters (2.2B Qwen3.5-2B VLM + 0.2B flow-matching action expert). Memory covers the last 3 frames, 1 s apart. 

 Runs on: Benchmarked on 1 NVIDIA H100. 21.8 ms per action chunk, compiled, from 2 cameras at 256×256. Weights ship in BF16. No quantized variants announced. 

 Performance: Best among VLAs pretrained on public data on LIBERO-Plus and RoboTwin Clean2Rand. 

 Best: 90.4% on LIBERO-Plus, the top score in Kyutai’s comparison. 

 Worst: 38.4% on RoboCasa365, well behind Xiaomi-Robotics-1 (57.4%). 

 What is REKI? 

 REKI is a vision-language-action model from Kyutai that maps camera views and an instruction to robot actions. It pairs a Qwen3.5-2B backbone with a 200M-parameter action expert. The expert generates action chunks by flow matching, integrated in 10 Euler steps. Robot state and flow time enter through adaptive RMSNorm. Each robot state layout gets its own small state MLP. 

 How does REKI’s memory work? 

 Most VLAs act on the current frame alone. Prior memory methods feed past frames to the VLM, unroll training, or add modules. Each option adds cost. 

 REKI places memory inside the action expert instead. Before each frame’s action tokens sit 32 learned register tokens . They cross-attend the encoded prompt and views of that frame. They also self-attend the registers of earlier frames. 

 Registers never read action tokens. So they depend only on observations, not flow time or robot state. They are computed once per frame and cached in a rolling window. 

 The cost is small, per the project page : 

 Reading cached registers adds 0.1 ms to a 21.8 ms chunk. 

 The cache uses about 2 MiB of GPU memory per past frame. 

 Training packs a 3-frame window into 1 batched pass. 

 Memory also fixes a failure mode. Without it, arms often oscillate between 2 poses. On RoboTwin, oscillating episodes fall from 18.6% to 4.1% with memory. Kyutai attributes this to perceptual aliasing. 

 How does REKI perform on benchmarks? 

 REKI is pretrained once, then finetuned separately per benchmark. Scores below come from the model card and project page. 

 LIBERO-Plus: 90.4%, ahead of Qwen-RobotManip (89.0%) and π0.5 (85.7%). 

 RoboTwin Clean2Rand: 65.8%, behind only Qwen-RobotManip (68.5%). 

 RoboCasa365: 38.4%, ahead of RLDX-1 (36.0%) and Qwen-RobotManip (35.9%). 

 LIBERO (4 suites): 97.6%. 

 RoboTwin 2.0 Easy / Hard: 85.9% / 84.6%. 

 Pretraining helps most out of distribution. It adds 13.8 points on Clean2Rand and 30.3 under clutter. Memory adds 1.5 points on LIBERO-Plus and 5.4 on RoboCasa365. 

&

 How does REKI compare with other VLAs? 

 Feature REKI ( Kyutai ) Qwen-RobotManip ( Qwen ) π0.5 ( Physical Intelligence ) ABot-M0 ( AMAP ) Total size 2.4B 4.7B ( per Kyutai ) 3.3B ( per Kyutai ) 4.6B ( per Kyutai ) VLM backbone Qwen3.5-2B Qwen3.5-4B Gemma-based Not disclosed Pretraining data Public only Open-source + human video Includes own robot data Open-source (UniACT) Memory 32 registers, 3 frames In-context variant None None LIBERO-Plus 90.4 89.0 85.7 ( Kyutai eval ) 80.5 RoboTwin Clean2Rand (mean) 65.8 68.5 63.8 55.7 RoboCasa365 38.4 35.9 16.9 Not disclosed H100 latency, compiled 21.8 ms Not disclosed 33.8 ms ( openpi, Kyutai ) 46.1 ms ( Kyutai ) Weights Open, CC BY-NC-SA 4.0 Not released Open, Apache-2.0 repo Open, Apache-2.0 repo 

 Notes: Clean2Rand means are computed from the 6 conditions in Table 5 of the Qwen-RobotManip report . The Qwen report lists π0.5 at 84.4 on LIBERO-Plus. 

 What data was REKI trained on? 

 The mixture holds 1.0B frames plus 12.2M vision-language samples. Real-robot teleoperation provides 639.8M frames, simulation 193.9M and egocentric human video 170.9M. Sources include DROID, BridgeData V2, AgiBot World, EgoDex and EgoVerse. Pretraining ran 200,000 steps on 32 H100 GPUs. Kyutai keeps each dataset’s native control convention rather than remapping actions. 

 How do you deploy REKI? 

 Six checkpoints are listed: the pretrained base plus finetunes for LIBERO, RoboTwin (2 variants), RoboCasa365 and RoboCasa-GR1. Real-robot deployment uses the LeRobot async-inference gRPC protocol. On a UR5 arm, REKI was finetuned for 3k steps (1 hour) on 50 demonstrations per task. 

 Copy Code Copied Use a different Browser from reki import RekiPolicy

policy = RekiPolicy.from_pretrained("kyutai/reki-2b-libero", device="cuda")
policy.reset() # clears the register cache at episode start
actions = policy.predict(images={"camera_top": img0, "camera_wrist_left": img1},
 state=proprio, task="put the bowl on the plate") 

 Key Takeaways 

 REKI is a 2.4B VLA pretrained only on public data. 

 It scores 90.4% on LIBERO-Plus, top in Kyutai’s comparison. 

 32 cached register tokens give memory for 0.1 ms extra. 

 Memory cuts pose oscillations from 18.6% to 4.1% on RoboTwin. 

 Weights are open but non-commercial (CC BY-NC-SA 4.0). 

 Check out the Paper , Project Page , Model Weights and GitHub Repo . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Meet Kyutai REKI: The 2.4B VLA Model Bringing Efficient Memory to Robot Manipulation appeared first on MarkTechPost .
