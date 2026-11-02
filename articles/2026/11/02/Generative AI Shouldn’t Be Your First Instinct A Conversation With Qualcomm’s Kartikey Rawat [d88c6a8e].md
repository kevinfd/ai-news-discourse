---
id: "d88c6a8e98e93451"
title: "Generative AI Shouldn’t Be Your First Instinct: A Conversation With Qualcomm’s Kartikey Rawat"
url: "https://circuitdigest.com/interview/qualcomm-kartikey-rawat-edge-ai-quantization-local-inference-cloud-processing"
link: "https://circuitdigest.com/interview/qualcomm-kartikey-rawat-edge-ai-quantization-local-inference-cloud-processing"
source: "Circuit Digest"
domain: "circuitdigest.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-02T02:08:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["November 2"]
language: "en"
summary: "Closing the discussion, Rawat said it is needed, but it depends on the use case. He estimated that 50 to 60% of use cases don't need generative AI and can be handled by classical models, while others ..."
tags: []
orgs: ["Amazon", "Hugging Face"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1496
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Generative AI Shouldn’t Be Your First Instinct: A Conversation With Qualcomm’s Kartikey Rawat

Circuit Digest · November 2 · 2026-11-02

Kartikey Rawat, senior AI and ML engineer and developer advocate at Qualcomm, talks about what to consider when building for Edge AI, from quantization and hardware to local versus cloud processing, and whether generative AI needs to run on edge devices at all.
About the event
This conversation was recorded at electronica India and productronica India 2026, South Asia's leading trade fair for the electronics industry. Held September 16-18 at the Bangalore International Exhibition Centre in Bengaluru and organized by Messe Muenchen India, the show covered the complete electronics value chain. It brought together 793 exhibitors and over 52,000 business visitors under the theme "India's Powerplay in Electronics."
Get the model running first
Asked what hardware specifications engineers should look at for Edge AI, Rawat said they don't need to focus on hardware too heavily. His advice was to start from a model and get it running on the target device. He pointed to quantization, which makes a model smaller, and said there are many techniques for reducing model size, but that this is just one part of the process. Hardware still matters, he added, because it is where the model will run.
Quantization can also cost accuracy. As an example, he said that when he applied a wrong quantization to MobileNet, a small, classical model, its accuracy dropped from 97% to 50%. He described post-training quantization (PTQ) techniques as checking, after training, whether something like dropping neurons in pruning affects accuracy significantly.
He said engineers outside core machine learning are often unfamiliar with quantization and pruning, and that many senior and principal engineers he talks to have little idea about Edge AI. He also expects hardware and software to merge. Hardware engineers can do software and software engineers can do hardware, he said, because coding agents have made coding less of a barrier. The harder skill is structuring the architecture, and he said that holds for mechanical engineers moving into mechatronics or robotics too.
A smart parking example
Asked how he would approach a CCTV-based smart parking lot that detects parked cars and reads number plates, Rawat split the problem into day and night. At night, when there is no light, he would use thermal imaging. In daylight, a basic object detection model would work, with a classification model separating plate from non-plate. Classical models can also pull out the plate details, he said, which can be stored in a simple table-format database. A car with no plate could not be registered, so an alarm would be raised, signalling that an unknown person has entered.
He said the two models, one for thermal imaging and one for basic object detection or plate classification, can run separately or be combined into one, and that the whole pipeline can run on the edge. Before choosing hardware, he said, you first decide the parameters the model has to handle, such as whether the car is parked properly inside its marked box and what the thermal readings show. These are classical models, he said, and they are not costly to run.
Generative AI on the edge
Rawat’s advice was to keep it simple and think like an engineer first. An engineer is hired so that a product’s cost can come down, he said, and generative AI should be used when the use case supports it. Qualcomm, he said, has two dedicated parts for model inferencing: one for classical models such as classification, object detection and thermal imaging, and one for generative models. Generative AI suits phones well, since apps there are largely chat-based, though it can also run on IoT devices if the use case makes sense.
He said anyone can now run Edge AI at home without internet, and that he could vouch for it. For home automation, a basic soldered setup can run locally instead of buying voice-assistant devices such as Alexa. He noted that Snapdragon chips are now available on laptops, and that a spare laptop with a GPU and NPU can run a larger model locally.
As an example, he described a web IDE he built that generates code using a Gemma model running locally. It uses his local GPU through the WebGPU standard, and he said he generally uses TensorFlow.js or LiteRT.js for this. Models such as Gemma 4 can be downloaded from Hugging Face, he said. He said local code generation is possible, and that running it locally means paying only for hardware and not for the cloud, though he stressed that he is not against the cloud and sees it as part of the integration.
What runs locally and what goes to the cloud
For simpler tasks, including simple agentic ones, Rawat said local execution works. Opening the camera or changing system settings can be done on the device. A task such as ordering a regular item like poha from Zomato every day at 10 a.m. through an MCP connection would be hybrid: the instruction, including converting speech to text, is handled on the device, while the MCP part loads from the cloud.
He said personal topics people raise with chatbots are better handled locally if possible, while complex problems can go to the cloud. He suggested that models may eventually decide for themselves whether a task is simple enough to run locally or needs the cloud, so the user never has to think about it.
That may be why many companies are moving more work onto the chip, he said: it can reduce their own costs, because the hardware cost is borne by users, not companies. And if costs come down, he added, it could increase AI adoption.
Where developers struggle
Rawat said many developers struggle simply to get started. A good portion are software developers who have never worked with hardware, so it is a very different aspect for them, and they are interested but don't know how to begin. Bugs also come up, he said, and the hardware ecosystem is not a unified framework. RISC-V is now available on the open-source side, but generally everything is proprietary, so developers end up asking whether a problem is a kernel issue, which specific version they need, or why a particular sensor doesn't work with a particular API. Even so, he said developers are loving being able to run things locally without internet that they couldn't before.
Asked for the Edge AI equivalent of blinking an LED, the usual first step in embedded work, he suggested running an object detection model. A beginner can start with two classes, such as person and non-person, car and non-car, or cat and dog. With Edge Impulse, he said, you add images to each class, the tool fine-tunes the model for you, and you can run it locally without writing code.
Why models fail outside the lab
When the host described training a tomato-versus-potato model in Edge Impulse that worked in the lab but struggled once the lighting changed, Rawat said this is an industry-wide problem, not a personal one. The outcome depends on the data and on how the model is packaged, he said, not only on the model itself, and you won't capture all the data from the real environment up front.
He described a personal experiment in keeping data local: using data generated at the edge to fine-tune the local model after deployment, through a reinforcement-learning agent or environment running locally, an approach he called meta-learning. How such a closed loop would label the data is still a research question, he said. The priority, he said, is privacy: data should stay in the user's hands, and sharing it with a cloud service or another company should be the user's choice.
Who is adopting Edge AI
Rawat pointed to several sectors. Manufacturing has been in the game for a long time because those companies don't want to share their data and at least store it locally. Healthcare is another, where sensitive data calls for on-premises solutions, and where data may be processed in metadata form to improve models. He added that app companies can build customer trust by showing that only part of a user's data leaves the device, and said startups with dedicated mobile apps are already using this, though he acknowledged there is a long way to go.
Tools to learn
For people moving into machine learning, including hardware engineers, Rawat recommended PyTorch, a framework started by Meta, as a good starting point, and said Google's TensorFlow is also worth testing. He guessed that about 90% of the models in industry use PyTorch. He called the two the frameworks most used by industry, and both are open source.
Is generative AI needed on the edge?
Closing the discussion, Rawat said it is needed, but it depends on the use case. He estimated that 50 to 60% of use cases don't need generative AI and can be handled by classical models, while others do call for it. On IoT devices it can run, he said, but again it depends on the use case.
