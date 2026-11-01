---
id: "9166a403ff1605c9"
title: "What is Physical AI? - Differences from Generative AI in 3 Minutes"
url: "https://note.com/right_finch9592/n/n4468b8d8bf9a?hl=en"
link: "https://note.com/right_finch9592/n/n4468b8d8bf9a?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-31T02:18:00Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Play S"]
language: "en"
summary: "Embedded Linux Porting Starting from Datasheets\" Part 1About this article (Disclosure of AI usage and stance)This series is a \"learning record\" that the author is supervising and publishing while ..."
tags: []
orgs: ["OpenAI", "Nvidia", "Meta"]
topics: ["models & research", "health & science", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2330
paywalled: false
image: "http://www.bing.com/th?id=ONUT.LgKWfIzpUKGhBDV0TDZG1w&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# What is Physical AI? - Differences from Generative AI in 3 Minutes

note · Play S · 2026-10-31

What is Physical AI? - Differences from Generative AI in 3 Minutes
Series: "Building the 'Brain and Nerves' of Physical AI - Embedded Linux Porting Starting from Datasheets" Part 1
What you will be able to do with this article
- Explain the meaning of the term "Physical AI" in your own words, in line with definitions from public institutions and companies.
- Explain the difference between "Generative AI" like ChatGPT and Physical AI using a single diagram.
- Acquire the perspective of viewing Physical AI by dividing it into three parts: "Perception → Judgment → Action," and understand which part this series covers.
Prerequisites
- None in particular. If you have used a computer or smartphone, you can read this.
- All technical terms will be explained either in the "Glossary" below or in the main text before they are used.
Verification Environment
Since this installment is for reading and organizing materials, there is no command execution. The materials researched and the access dates are as follows.
- Work Content: Comparing public documents (no command execution)
- Date of access to materials: 2026-10-30
- Materials referenced: NVIDIA Glossary, explanatory articles from the National Institute of Advanced Industrial Science and Technology (AIST), and strategic proposals from the Japan Science and Technology Agency (JST) Center for Research and Development Strategy (CRDS) (see references at the end for details)
Labels (Legend) for this article
In this series, the following labels are attached so that the "source" of the information can be seen at a glance.
- 【QEMU Results】: Results actually run on "QEMU" (software that mimics another computer inside a PC; explained in detail in Part 3) on the author's work Linux.
- 【Host Results】: Results executed on the author's work Linux (host) itself.
- 【Real Machine Data (Public Documents)】: Results obtained from real machines (evaluation boards or products) introduced from public documents. The author has not measured them on actual hardware.
- 【From Materials】: Information written in datasheets, official documentation, public institution materials, etc. Sources will always be provided.
- [Speculation]: Things the author has speculated about but has not yet verified
Since this session is for reading materials, the label used will primarily be [From the materials].
Glossary (terms appearing for the first time in this session)
- AI (Artificial Intelligence): A general term for technologies that enable computers to perform functions like humans, such as "perceiving, judging, and learning."
- Generative AI: AI that newly "creates" text, images, audio, etc. ChatGPT is a prime example.
- Large Language Model (LLM): The internal mechanism (model) of AI that learns from vast amounts of text to understand and generate language. Examples include GPT and Llama.
- Model: A "bundle of calculation methods" obtained as a result of AI learning. It receives input and produces an answer.
- Sensor: A component that measures conditions in the real world—such as light, sound, distance, or tilt—and converts them into electrical signals. Cameras are also a type of sensor.
- Actuator: A component that receives electrical commands and actually produces "movement." Motors are a prime example.
- Robot: A machine that perceives its surroundings with sensors, makes judgments with a computer, and moves using actuators.
- Autonomy: The ability to make judgments and act on one's own without needing human operation for every step.
- Simulation: Replicating and testing real-world movements within a virtual space inside a computer.
- Reinforcement Learning: A method of learning through repeated trial and error, where "rewards" are given for successful actions.
- Imitation Learning: A method where a robot learns by imitating actions demonstrated by a human.
- Multimodal (Multimodal): Handling different types of information together, such as images, text, sound, and sensor values.
1. Comparing the definition of "Physical AI" across three documents
1-1. Background and Purpose
The term "Physical AI" is increasingly being used in corporate announcements and explanations by research institutions (all three documents we will read next use this term in their headings). However, as it is a relatively new term, the scope it refers to varies slightly depending on the user. Since this series will eventually progress to "embedding Linux into computers that run Physical AI," I will first clarify "what we call Physical AI."
Reading only one document can lead to being swayed by that organization's position (for example, the position of a company selling a product). Therefore, we will compare three documents from different perspectives.
- Corporate: NVIDIA (An American company that makes semiconductors for AI)
- Research Institution: National Institute of Advanced Industrial Science and Technology (AIST; a Japanese national research and development agency)
- Policy Proposal: Japan Science and Technology Agency, Center for Research and Development Strategy (JST CRDS; an organization that compiles proposals on national science and technology policy)
1-2. Preparation
I will write down the steps so that readers can check the same documents.
- Open a web browser (an app for viewing web pages, such as Chrome or Safari) on your computer or smartphone.
- Open the three URLs listed in the "References" section at the end in new tabs respectively.
- The JST CRDS document is a PDF (a file format that can be distributed while maintaining the appearance of a paper document; the extension is .pdf). You can open it directly in your browser. Look for the "Executive Summary" (the summary page) at the beginning.
1-3. Procedure: Lining up the three definitions
I searched for the sections in each document that describe "what Physical AI is" and summarized the key points in a table. Instead of copying long passages from the documents, I have summarized the key points in my own words (please check the original sources for the full text).
1-4. Results
1-5. Discussion and Impressions
Although the wording in the three documents differs, I have interpreted that they share the following two points.
- Having a body (physical mechanism). It does not end within the screen; it measures reality with sensors and moves reality with actuators.
- Making decisions and acting on its own (autonomy). Instead of a person operating it step-by-step, the AI observes the situation and decides how to move.
On the other hand, there are differences. NVIDIA includes things that do not move themselves, such as "systems that monitor the movements of people and robots using factory cameras," as examples. JST CRDS calls not just the robot itself, but also the operational environment that moves it, a "system." In this series, we will treat the narrowest and most common definition—"a machine that measures with sensors, makes its own decisions, and moves with actuators"—as the core of Physical AI.
2. Organizing the differences from Generative AI
2-1. Background and Purpose
For many people, the AI they are familiar with is "Generative AI" like ChatGPT. Understanding how Physical AI differs from Generative AI helps clarify why special ingenuity (such as the Linux embedded systems and real-time control covered in this series) is required for robot computers.
2-2. Preparation
We will use the NVIDIA and AIST pages opened in 1-2. Please look for the heading "How Physical AI Works" on the NVIDIA page and the heading "Definition of Physical AI" on the AIST page.
2-3. Procedure: Comparing by "What to learn from" and "What to output"
When comparing AI differences, it is easier to understand if you look at them from the following two perspectives.
- Input and training data: What is used as material for learning?
- Output: What is ultimately produced (text or movement)?
I have extracted what is written in the materials regarding these two points.
2-4. Results
Summarizing this into a table results in the following (the organization of the table is by the author).
- Main learning materials / Generative AI (e.g., ChatGPT): Text and images on the internet / Physical AI (e.g., autonomous mobile robots): Real-world sensor data, data created in simulations, and human demonstration movements
- Main output / Generative AI (e.g., ChatGPT): Text, images, and audio / Physical AI (e.g., autonomous mobile robots): Actual "movement" (commands to motors)
- Impact when a mistake is made / Generative AI (e.g., ChatGPT): Incorrect answers on the screen (can be read and corrected by a person) / Physical AI (e.g., autonomous mobile robots): Colliding with objects, injuring people, or breaking things
- Time constraints / Generative AI (e.g., ChatGPT): It is often not a problem to wait a few seconds / Physical AI (e.g., autonomous mobile robots): If it does not respond within a set time, it will fall over or collide
2-5. Observations and Impressions
The two lines at the bottom of the table ("Impact when wrong" and "Time constraints") are not written directly in the materials, but are thoughts I had because the output is "movement".
This leads to the reason why the latter half of this series covers Linux "real-time optimization" and "task sharing with small computers for motor control."
3. Looking at it by dividing it into three: "Perception -> Decision -> Action"
3-1. Background and Purpose
Physical AI machines look complex, but if you divide their functions into three, it becomes easier to organize which parts are doing what. In this series, I will use this three-part division as a map until the end.
3-2. Preparation
Recall that in the table in 1-4, NVIDIA's definition stated "perceive, understand, reason, and execute actions." I will apply this flow to robot parts.
3-3. Procedure: Mapping functions to parts
I will think in the following order.
- What parts does the machine use to "know its surroundings" (Perception).
- What parts "decide how to move" based on the information learned (Decision).
- What parts turn the decided actions into "actual movement" (Action).
3-4. Results
My organization is as follows. Specific examples of parts are selected from those that appear in the actual product materials introduced in the second installment.
- Perception / What it does: Measures surroundings and own posture / Examples of main parts: Camera, LiDAR (sensor that measures distance to surrounding objects with laser light), IMU (sensor that measures tilt and acceleration), encoder (sensor that measures motor rotation angle)
- Decision / What it does: Decides how to move next based on measured information / Examples of main parts: CPU (the central computing device of a computer) and "SoC" (System-on-Chip), which combines a CPU and dedicated circuits that speed up AI calculations into a single chip
- Action / What to do: Actually perform the decided movement / Examples of main components: Motors, motor drivers (circuits that finely adjust the current flowing to the motor)
And what connects these three is "communication." Data is exchanged between sensors/motors and computers using rules (communication standards) such as UART, I2C, SPI, and CAN. These will be explained one by one in Part 2.
3-5. Observations and Impressions
This series mainly deals with the computer that handles the "judgment" in the middle, and the parts where it connects to the "perception" and "action" components. Specifically, it will proceed in the following flow:
- Running Linux as the OS (the basic software that manages the entire computer) on the SoC that handles judgment.
- Writing drivers (programs that bridge the OS and components) to operate the communication circuits connected to sensors and motors from Linux.
- Proceeding with these while reading the datasheets (component specifications) published by the manufacturers.
The theme of this series is not "creating AI models," but "creating the foundation (brain and nerves) for AI to operate."
4. Why is Physical AI attracting attention now?
4-1. Background and Purpose
Robots and autonomous driving have existed for a long time. So why is it attracting attention now under the new term "Physical AI"? Knowing the reasons will make it easier to understand "what is new" when reading materials in this field.
4-2. Preparation
Open the "Reasons for Attention" section on the AIST page and the "Role of Reinforcement Learning" heading on the NVIDIA page.
4-3. Procedure: Extracting the reasons written in the materials
Extract the parts corresponding to "why now" from the two materials and list them in bullet points.
4-4. Results
4-5. Observations and Impressions
In summary, it can be read that it is attracting attention because the "way of learning (simulation, video, imitation learning) has advanced" and there is a "demand to entrust real-world tasks due to labor shortages, etc." are overlapping.
However, no matter how much learning progresses, what ultimately runs inside the robot's body is a computer with limited power and size. NVIDIA's documentation also mentions a "runtime computer" (an execution computer) to be mounted on the robot, separate from the computer used for learning. This "computer mounted on a robot" is the protagonist of this series.
Summary
- Physical AI is AI that measures reality with sensors, makes its own judgments, and moves reality with actuators. The core common to the three documents (NVIDIA, AIST, JST CRDS) lies here.
- The biggest difference from Generative AI is that the output is "movement" rather than text. Therefore, safety and time constraints become stricter (this is the author's speculation, which will be verified in Part 2).
- Physical AI is easier to organize when divided into "perception → judgment → action." This series covers the integration of Linux into the computer responsible for the middle part, "judgment," and connecting it to the components of perception and action.
Next Episode Preview
In Part 2, "Examples of Physical AI and the Fields Where It Is Used," we will take up examples of humanoids, drones, autonomous driving/AMR, and service robots, and verify what kind of computers are inside each of them using publicly available manufacturer documents.
References (all accessed on 2026-10-30)
- NVIDIA "What is Physical AI?" https://www.nvidia.com/ja-jp/glossary/generative-physical-ai/
- National Institute of Advanced Industrial Science and Technology (AIST) "What is Physical AI?" (2026-05-13) https://www.aist.go.jp/aist_j/magazine/20260513.html
- Japan Science and Technology Agency (JST) Center for Research and Development Strategy (CRDS) "Strategic Proposal: Research and Development of Physical AI Systems - Fusion of AI with Embodiment and Robotics -" CRDS-FY2025-SP-01 (April 2025) https://www.jst.go.jp/crds/pdf/2025/SP/CRDS-FY2025-SP-01.pdf
Update History
- 2026-10-31: Part 1 published
