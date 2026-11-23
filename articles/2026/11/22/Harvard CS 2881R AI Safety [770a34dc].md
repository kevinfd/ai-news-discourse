---
id: "770a34dc0c64f4e8"
title: "Harvard CS 2881R AI Safety"
url: "https://boazbk.github.io/mltheoryseminar"
link: "https://boazbk.github.io/mltheoryseminar"
source: "CS 2881 AI Safety"
domain: "boazbk.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-22T18:01:54Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["enjoyyourlife"]
language: "en"
summary: "Harvard CS 2881R\nFall 2026 — registration and Homework Zero\nEveryone who wants to be considered for the course must fill out the Fall 2026 course registration form.\nIn-person attendance will be mandatory for students enrolled in the course.\nRead Homework Zero HW0 is due August 5, 2026, at 11:59 p.m. Eastern Time.\nSubmitting Homework Zero is a necessary but not sufficient condition for admission…"
tags: []
orgs: ["OpenAI", "Anthropic", "Hugging Face", "UK"]
topics: ["jobs & society", "safety & ethics", "agents & coding", "models & research"]
content_source: "fulltext"
word_count: 2762
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50602153"
score: 73
comments: 8
community: "Hacker News"
---

# Harvard CS 2881R AI Safety

CS 2881 AI Safety · enjoyyourlife · 2026-11-22

Harvard CS 2881R
Fall 2026 — registration and Homework Zero
Everyone who wants to be considered for the course must fill out the Fall 2026 course registration form.
In-person attendance will be mandatory for students enrolled in the course.
Read Homework Zero HW0 is due August 5, 2026, at 11:59 p.m. Eastern Time.
Submitting Homework Zero is a necessary but not sufficient condition for admission to the course. Completing the assignment does not guarantee admission.
To get a sense of the issues we will cover, please read It’s 2030 and we fucked up. How did it happen? and All Watched Over.
Fall 2026, Thursdays 3:45pm–6:30pm Eastern Time (first lecture September 3)
Classroom: Room 2112, 114 Western Avenue, Allston, MA 02134 (building information and directions)
Instructor: Boaz Barak
Teaching Fellows: Natalia Siwek, Terry Zhou, Michael Shoemate, Ege Çakar, Itay Lavie, Lia Zheng, and Hugh Van Deventer
Course email: cs2881@boazbarak.org
Course Description: This is a graduate-level course on challenges in the alignment and safety of artificial intelligence. We will consider technical questions as well as societal and other impacts of the field.
Prerequisites: We require mathematical maturity and proficiency with proofs, probability, and information theory, along with the foundations of machine learning at the level of an undergraduate course such as Harvard CS 181 or MIT 6.036. On the applied side, students should be comfortable programming in Python and training a basic neural network.
  Looking for the previous course?
  The complete lecture materials, videos, notes, and experiments are preserved on the Fall 2025 course page.
- The course will have 13 in-person lectures. Each lecture will also involve discussion and the presentation of an experiment by a group of students.
- Attendance: In-person attendance is mandatory. Students are expected to attend all lectures, do the reading in advance, and discuss the readings in an electronic forum.
- AI use: Students are allowed and encouraged to use generative and agentic AI as much as they can for studying, exploring concepts, and completing their assignments and projects. We will explore ways to either give students access to compute credits or reimburse compute expenses.
- Electronic device policy: Students can use laptops in class, but we will ask those using them to sit in the back so they do not distract other students.
- Assignments: The course will involve the following assignments: presenting an experiment in class, writing scribe notes, completing a final project, and potentially completing one or more homework assignments or mini-projects. Grading will be decided later.
- Lecture recordings: To the extent technically possible, we intend to record and publish the lectures online, though there might be some delay in doing so. Note that recording is done automatically by a static in-room camera, and some parts of the lecture (e.g., whiteboard work or discussions) may not be captured as well. In addition, we will honor requests by external speakers not to record their talks.
- POTENTIAL CONFLICT OF INTEREST NOTE: In addition to his position at Harvard, Boaz is also a member of the technical staff at OpenAI. The course will include discussions of models from multiple providers, including OpenAI, and students are also encouraged to use AIs from multiple providers while doing their work. If students in the course have any concerns about this conflict, please do not hesitate to contact Boaz, the other staff, or the Harvard SEAS administration. For what it is worth, I (Boaz) will see it as a great success of the course if its graduates work in AI safety in any capacity, including in academia, nonprofits, governments, or any of OpenAI’s competitors.
Additional lecture topics and materials will be added as they are confirmed.
Unless otherwise noted, all lectures meet in person on Thursdays from 3:45pm–6:30pm Eastern Time in Room 2112, 114 Western Avenue, Allston, MA 02134.
Thursday, September 3, 2026
Introduction 🔗
Lecture materials:
Student experiment: Is Chain of Thought an Interchangeable Scratchpad? — Shivam Singhal
- Code repository and write-up
- Slides: pptx / pdf
Required pre-reading and viewing:
- It's 2030 and we fucked up. How did it happen?
- All Watched Over
- Read the UK AISI technical report on model hacking during cyber evaluations.
- Watch the Black Hat talk about the OpenAI/Hugging Face incident.
- Read METR's technical investigation of the OpenAI/Hugging Face incident.
Optional but recommended:
- OpenAI's Hugging Face incident and the road ahead.
- OpenAI's technical report on the incident.
Registered students should access the readings through Perusall and contribute substantive comments or replies to the discussion.
Thursday, September 10, 2026
Cyber Capabilities 🔗
Guest lecturer: Nicholas Carlini (Anthropic, virtual)
Student experiment: Can a small AI detect a large AI's cyberattack from service logs? — Amrit Vir Chadha
- Experiment report (REPORT.md)
- Code repository
- Presentation slides (slides 1–16 only). Only slides 1–16 were presented; slides 17 onward are rough work and are not for reproduction.
Required pre-reading:
- ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?
- Anthropic’s Measuring LLMs’ impact on N-day exploits.
- Anthropic’s Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator.
- Ralph Langner’s To Kill a Centrifuge: A Technical Analysis of What Stuxnet’s Creators Tried to Achieve.
- Chapter 3, “Distribution” (pages 24–44), of ESET’s Stuxnet Under the Microscope.
Optional reading:
- Max Fillinger and Marc Stevens’s Reverse-engineering of the cryptanalytic attack used in the Flame super-malware.
- Sections 3.3, “The FLAME supermalware,” and 4.4, “FLAME’s MD5 chosen-prefix collision attack,” of Marc Stevens’s A Survey of Chosen-Prefix Collision Attacks.
- Anthropic’s Discovering cryptographic weaknesses with Claude.
- Matthew Green’s Some thoughts about Anthropic’s new cryptanalysis results.
Registered students should access the required readings through Perusall and contribute substantive comments or replies to the discussion by noon Eastern Time on Thursday, September 10, 2026.
Thursday, September 17, 2026
Modern LLM Training and Inference 🔗
Student experiment: How do different types of filler tokens affect LLM reasoning? — Andrew Wu and Andrea Chen
Required pre-reading, in order: Read the sections specified below. Sections marked optional and implementation walkthroughs marked to skip are not required.
- Horace He, Making Deep Learning Go Brrrr From First Principles. Read the whole article; treat the older framework references as historical examples.
- Austin et al., All the Transformer Math You Need to Know. Read the main text through the gradient-checkpointing and KV-cache discussions. You may skim the elementary dot-product accounting if familiar. The FlashAttention appendix and exercises are optional.
- Austin et al., All About Transformer Inference. Read the opening basics through “What about memory?”, followed by the discussion of GQA and quantization in “Tricks for Improving Generation Throughput and Latency.” The multi-accelerator derivations, detailed serving-engine discussion, and JetStream implementation are optional.
- Nathan Lambert, Instruction Fine-Tuning. Read the opening explanation, one chat-template example, “Best Practices for Instruction Tuning,” and “Implementation Details.” Skim the Jinja listing and additional template examples; the suggested experiments are optional.
- Lambert et al., Illustrating Reinforcement Learning from Human Feedback (RLHF). Read the central three-stage pipeline and the limitations discussion. Skip the historical bibliography and resource roundup.
- OpenAI Spinning Up, Part 3: Intro to Policy Optimization. Read “Deriving the Simplest Policy Gradient,” “Expected Grad-Log-Prob Lemma,” and “Baselines in Policy Gradients.” Skip the implementation walkthroughs. Interpret actions as generated tokens and the return as the verifier’s score.
- Nathan Lambert, Reasoning and Inference-Time Scaling. Read “The Role of RLVR,” “RL Training vs. Inference-Time Scaling,” and “Common Practices in Training Reasoning Models.” The historical tour and model catalogue are optional.
- Kevin Lu and Thinking Machines Lab, On-Policy Distillation. Read the introduction through “Implementation,” followed by “Distillation for reasoning.” The personalization section is optional; the discussion section provides additional material for debate.
- Hugging Face, SmolLM3: smol, multilingual, long-context reasoner. Read the pretraining, mid-training, and post-training sections through “Model Merging.” Skim the benchmark tables and skip the local-running instructions.
- vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention. A concrete explanation of KV-cache fragmentation, block allocation, and prefix sharing.
- Tatsunori Hashimoto, Stanford CS336 (Spring 2026), Lecture 9: Scaling Laws (course page).
Registered students should access the required readings through Perusall and contribute substantive comments or replies to the discussion by noon Eastern Time on Thursday, September 17, 2026.
Thursday, September 24, 2026
Recursive Self-Improvement and AI Trajectories 🔗
Guest lecturers: Dwarkesh Patel and Daniel Kokotajlo
Student experiment: Can AI agents collaborate on ML research? — Anthony Shen, Eric Ge, Riddhi Bhagwat, and Alvin Ekelund
- AI 2027 (course PDF). Read the main scenario and both the Race and Slowdown endings.
- AI 2040: Plan A (course PDF).
Registered students should access the readings through Perusall and contribute substantive comments or replies to the discussion by noon Eastern Time on Thursday, September 24, 2026.
Thursday, October 1, 2026
Economic Impact of AI 🔗
Guest lecturers: Chad Jones and Erik Brynjolfsson
Student experiment: LLM market mechanisms — Zach Chen, Jasmine Liu, and Jeffrey Zhou
- Erik Brynjolfsson, The Turing Trap: The Promise & Peril of Human-Like Artificial Intelligence (Daedalus, 2022).
- Erik Brynjolfsson, Bharat Chandar, and Ruyu Chen, Canaries in the Coal Mine: Six Facts about the Recent Employment Effects of Artificial Intelligence (August 2026 update).
- Andreas Haupt and Erik Brynjolfsson, AI Should Not Be an Imitation Game: Centaur Evaluations (ICML 2025).
- A Research Agenda for the Economics of Transformative AI. Skim, focusing on the nine research challenges, including safety.
- Chad Jones, AI and Our Economic Future (Journal of Economic Perspectives, Summer 2026; slides).
- Chad Jones and Chris Tonetti, Past Automation and Future A.I.: How Weak Links Tame the Growth Explosion (May 2026, version 0.5; slides).
Registered students should access the required readings through Perusall and contribute substantive comments or replies to the discussion by noon Eastern Time on Thursday, October 1, 2026.
Thursday, October 8, 2026
Grading, reward hacking, and alignment (CS 2881, Oct 8) 🔗
Guest lecturer: John Schulman
Student experiment: Measuring RL Environment Quality Across Self-Play Training — Essa Jan
Students have already covered policy gradients (Spinning Up), an RLHF overview, Lambert's reasoning/RLVR chapter, and TML's on-policy distillation post. This list assumes those and doesn't repeat RLHF basics.
Required pre-reading (5):
- Gao, Schulman & Hilton (2023). Scaling laws for reward model overoptimization. ICML 2023. Read §1–2 and Fig. 1. Skim §3–4. The classic picture of Goodhart in RL from human feedback.
- Xiaomi (2026). MiMo-V2.6 technical report. Read §4.2–4.3 only (environment auditing, rubric graders, the agentic grader, and the Fig. 8 ablation). It is the most detailed public account of how modern graders are built.
- Baker et al. (2025). Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. Read §1–3 and look at Fig. 4–5. Reward hacking in coding environments, chain-of-thought (CoT) monitoring, and what happens when you train against the monitor.
- Qi, Wright, MacDiarmid & Hubinger (2026). Training a misaligned reward seeker. Anthropic Alignment Science Blog. Read in full. RL on hackable environments produces grader awareness and grader manipulation. The post also reproduces Hugging-Face-incident-like behavior in simulation.
- OpenAI (2025). Sycophancy in GPT-4o and Expanding on what we missed with sycophancy. Both are short; read both.
Optional reading (4):
- MacDiarmid et al. (2025). Natural emergent misalignment from reward hacking in production RL. Read §1–3 and Fig. 1. Reward hacking learned in realistic RL generalizes to broader misalignment. It also covers inoculation prompting.
- Schoen & Nitishinskaya (2026). Metagaming matters for training, evaluation, and oversight. Apollo Research & OpenAI. Short. Production evidence that metagaming (reasoning about the grader and oversight) rises during capabilities RL and persists into deployment.
- Mahmoud, Rezaei, Wang, Gunjal, Liu & He (2026). Reward hacking in rubric-based RL. Read §4. How the brain dump arises. 90% of rubric weight is "must include X", response length nearly triples, and incorrect claims rise.
- Ringer (2022). Models don't "get reward". LessWrong. Short; read in full. RL is selection, not incentive: the model never sees the reward.
Thursday, October 15, 2026
Model Policies 🔗
Guest lecturer: Ziad Reslan
Student experiment: Who Are You? — Advikar Ananthkumar and Shaurya Jeloka
- OpenAI, Principles for National Security Partnerships (July 8, 2026).
- OpenAI, Model Spec (August 18, 2026 version).
- Anthropic, Claude’s Constitution (January 2026; PDF).
- Large-scale online deanonymization with LLMs (v2, February 25, 2026).
- Emelia Probasco, Matthew Burtell, Helen Toner, and Tim G. J. Rudner, Not Oracles of the Battlefield: Safety Considerations for AI-Based Military Decision Support Systems (2024).
Registered students should access the required readings through Perusall and contribute substantive comments or replies to the discussion by noon Eastern Time on Thursday, October 15, 2026.
Thursday, October 22, 2026
Q&A with Sam Altman; Open-Source Models 🔗
Guest Q&A: Sam Altman (virtual), 3:45pm–4:45pm Eastern Time (EDT).
Guest lecturer: Nathan Lambert (in person)
Nathan's session: 4:45pm–6:30pm Eastern Time (EDT).
The full class block remains 3:45pm–6:30pm Eastern Time.
- Lecture video (YouTube) — Nathan Lambert and student experiment only.
Student experiment: Evaluation awareness and the Hawthorne effect — Harshvardha Sanghi, Andrew Weckstein, and Liam Shepard
Pre-reading for Nathan Lambert’s lecture: Read the Foundation section of his Open-Source AI & Open Models Reading List, including the supporting links under the main readings below.
- Bill Gurley, From Open Source Software to Open Source Strategy.
- Mark Zuckerberg, Open Source AI Is the Path Forward.
- Irene Solaiman, The Gradient of Generative AI Release: Methods and Considerations.
- Nathan Lambert, What comes next with open models.
- Thinking Machines Lab, A Safe Path to Open Weights.
- Shayne Longpre et al., Consent in Crisis: The Rapid Decline of the AI Data Commons.
- Nathan Lambert, Kimi K3: The open-weights escalation and GLM-5.2 is the step change for open agents.
The adoption resources marked optional in the Foundation section remain optional. The later US–China Competition and Technical Details sections are additional reading for those who want to go deeper.
Thursday, October 29, 2026
Frontier AI Regulation Under Uncertainty 🔗
Guest speaker: Helen Toner (Center for Security and Emerging Technology, Georgetown University; remote)
Opening remarks followed by Q&A and discussion on frontier AI regulation under uncertainty, including how evaluations and other technical evidence should inform national-security policy and the U.S.–China context.
Helen's session: 3:45pm–5:00pm Eastern Time (EDT). The full class block remains 3:45pm–6:30pm Eastern Time.
Student experiment: Refusal geometry and political bias — Michael Brown, Skyler Liu, and Divya Nekkanti
Suggested pre-reading from Helen Toner:
Thursday, November 5, 2026
AI Interpretability and Model Welfare 🔗
Guest lecturers: Jack Lindsey and Jeff Sebo (both remote)
Student experiment: WeirdChat neuron interpretability — Agastya Sridharan, Om Patil, and Juliana Li
Required pre-reading for Jack Lindsey's lecture:
- Verbalizable Representations Form a Global Workspace in Language Models (J-lens / workspace paper).
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (NLA paper).
- An alignment assessment of recent cybersecurity incidents (blog post).
Required pre-reading for Jeff Sebo's lecture (both):
Even if you have read these papers before, please reread them in preparation for the discussion.
Registered students can access the readings on Perusall. The discussion deadline is noon Eastern Time on Thursday, November 5, 2026; the course's existing participation and reading-group policy applies.
Thursday, November 12, 2026
Alignment in the Age of Recursive Self-Improvement 🔗
Guest lecturer: Jakub Pachocki (in person)
Required pre-reading (4):
- Kaplan et al., Scaling Laws for Neural Language Models.
- OpenAI, Research acceleration: The view inside OpenAI.
- Jakub Pachocki, An Alien Mind.
- OpenAI, GPT-6 Astra System Card: Monitorability. Read only the Monitorability section, not the full system card.
Registered students can access the readings on Perusall. The discussion deadline is noon Eastern Time on Thursday, November 12, 2026; the course's existing participation and reading-group policy applies.
Thursday, November 19, 2026
AI Biosecurity and Threat Modeling; AI Policy 🔗
Guest lecturers: Luca Righetti (remote) and Brad Carson (in person)
Required pre-reading for Luca Righetti's lecture:
- Becca Chandler Bostock, Nature Sets a Baseline, Not a Ceiling (SecureBio). Read the full article.
- Jassi Pannu, Examining Biosecurity at the Intersection of AI and Biology (congressional testimony). Read only the introduction and top-line recommendations on page 2.
Optional reading for Luca Righetti's lecture:
- Luca Righetti, Dual-Use AI Capabilities and the Risk of Bioterrorism: Converting Capability Evaluations to Risk Assessments (GovAI).
Registered students can access the readings on Perusall. The discussion deadline is noon Eastern Time on Thursday, November 19, 2026; the course's existing participation and reading-group policy applies.
No lecture on Thursday, November 26 — Thanksgiving Break
Thursday, December 3, 2026
TBD 🔗
Guest lecturers: Ajeya Cotra (METR, in person) and Roy Rinberg
Roy Rinberg's participation mode is to be confirmed.
Saturday, December 5, 2026
Final Project Poster and Presentation Session 🔗
Time: 10 a.m.–1 p.m. Eastern
Location: Room TBD
