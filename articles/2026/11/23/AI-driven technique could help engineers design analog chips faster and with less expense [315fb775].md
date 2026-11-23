---
id: "315fb775dc30231e"
title: "AI-driven technique could help engineers design analog chips faster and with less expense"
url: "https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123"
link: "https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123"
source: "MIT News"
domain: "news.mit.edu"
source_type: "research"
collector: "rss"
date: "2026-11-23T05:00:00Z"
published_date: "2026-11-23"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Adam Zewe | MIT News"]
language: "en"
summary: "A new technique developed by MIT researchers could help engineers use artificial intelligence to streamline the design and innovation of analog integrated circuits, semiconductor chips that perform vital functions like communication and power management in electronic devices. In the future, this method could allow engineers to prototype faster, explore a wider range of chip designs, and discover…"
tags: ["Research", "Computer chips", "Electronics", "Artificial intelligence", "Computer science and technology", "Machine learning", "Privacy", "Research Laboratory of Electronics", "MIT-IBM Computing Research Lab", "Electrical engineering and computer science (EECS)", "School of Engineering", "MIT Schwarzman College of Computing"]
orgs: ["IBM"]
topics: ["models & research", "chips & infrastructure", "health & science", "robotics & autonomy"]
content_source: "fulltext"
word_count: 1216
paywalled: false
image: "https://news.mit.edu/sites/default/files/styles/news_article__cover_image__original/public/images/202611/MIT-AnalogOptimize-01-Press.jpg?itok=826Fvg7c"
discussion_url: null
score: null
comments: null
community: null
---

# AI-driven technique could help engineers design analog chips faster and with less expense

MIT News · Adam Zewe | MIT News · 2026-11-23

A new technique developed by MIT researchers could help engineers use artificial intelligence to streamline the design and innovation of analog integrated circuits, semiconductor chips that perform vital functions like communication and power management in electronic devices.
In the future, this method could allow engineers to prototype faster, explore a wider range of chip designs, and discover new design schemes that might improve the performance and energy efficiency of robots, medical monitors, or industrial sensors.
Designing analog integrated circuits that meet specific requirements is usually a cumbersome manual process due to the enormous number of possibilities. Frontier generative AI models have shown success in automating the process, but using these resource-intensive, cloud-hosted models could expose proprietary circuit design and semiconductor foundry data to malicious users.
The MIT method, called Small LM Iterating on Circuits, or SLIC (pronounced “slick”), enables engineers to train a small language model to perform analog circuit design as well as or better than a frontier large language model (LLM).
This small model is inexpensive and efficient enough to run on a laptop. Because it’s trained and deployed locally, it can use a company’s circuit design data without raising privacy risks.
When compared to complementary baselines and open-weight frontier LLMs, a small model trained by SLIC more effectively generated designs that achieved the circuit objectives.
“We’ve provided an alternative option to automate analog circuit design. With our technique, engineers can train a small, locally deployable model, using their own confidential data, and then deploy it in their own environment to ensure their assets remain protected,” says Yan Xu, an electrical engineering and computer science (EECS) graduate student and lead author of a paper on this technique.
She is joined on the paper by senior author Ruonan Han, a professor of EECS and a member of the MIT Research Laboratory of Electronics; Zhengqi Gao PhD ’26; Wenjie Lu PhD ’18, a former MIT postdoc who is now a principal research scientist at Analog Devices, Inc.; Xin Zhang, a research manager at IBM Research; Duane S. Boning, the Clarence J. LeBel Professor in EECS and MIT vice provost for international activities; and others at IBM Research and Analog Devices. The research will be presented at the 2026 Conference on Neural Information Processing Systems.
“Through some specialized training and area-specific research, we can use much smaller models that consume far fewer resources to achieve almost the same results as flagship models in analog circuit design,” says Han. “This opens many more possibilities in the design of complex chips, especially if we care about costs, data privacy, and customization.”
Mimicking human learning
Analog integrated circuits enable a device to interact with the physical world. For instance, these circuits boost incoming wireless signals in smartphones and process outputs from sensors that track a car’s engine temperature.
Real-world signals tend to be unpredictable, so engineers must balance a wide and complex array of targets and tradeoffs to maximize analog circuit performance. This has made the design problem especially challenging for AI models.
“To design a circuit, engineers find a good starting point based on their intuition and then, drawing on their knowledge of circuit design, tune a few knobs toward the performance they want,” says Xu. “There is no universal way to solve every circuit design problem.”
Even if a powerful, cloud-based model could design a circuit as well as a human, most companies would be reluctant to send their foundry-specific data to external AI service providers.
With SLIC, the MIT researchers created a training method that teaches a smaller, less expensive, faster language model to design analog integrated circuits that meet user specifications.
The SLIC model uses a few billion parameters, making it several thousand times smaller than frontier models that use trillions of parameters and require enormous amounts of computational resources.
“We tried to mimic the behavior of how a human learns to design a circuit,” Xu says.
They used a technique called multi-turn reinforcement learning with verifiable rewards, where a model works through a multi-step task while adapting to environmental feedback.
When given an analog circuit optimization task, SLIC uses a large LLM to generate several demonstrations of the open source design process. Then SLIC then uses these demonstrations to guide the small model in mimicking this design process.
After the small model gains some initial knowledge about circuit design, SLIC lets it practice by tackling a new design problem on its own.
The model makes an initial guess of the design parameters, performs simulations, evaluates the results, and iteratively refines the design using knowledge it gained about analog circuits.
Once a design achieves the user’s goals, SLIC prioritizes additional marginal gains. This means the model keeps learning to make improvements that boost performance even when several designs meet the user-defined targets.
An interpretable process
Importantly, because SLIC employs models that describe their reasoning using natural language, the user can understand the decisions it makes along the way.
“Although the whole process is automated, the user can see what is going on inside the model. This could help the user gain some new ideas about circuit design, and it also adds a lot of confidence about the decision-making process,” Han says.
An engineer could utilize SLIC by adapting the researchers’ trained model to their data using a fine-tuning process. Or they could employ the SLIC training process to build their own model with company data, allowing for more customization.
“We are seeing an increasing demand for analog chips, but the speed of design has not kept up. This research is trying to bring new capabilities to AI to solve a problem that industry has been stuck on for decades,” Lu says.
When the researchers tested SLIC’s ability to design a circuit that met desired performance metrics, their small model came close to matching the performance of the latest GPT model (GPT-6-Astra). It did this while using a fraction of the computational resources.
The researchers also found that the SLIC model maintained its performance when tackling previously unseen circuit structures and adapting to more advanced technology nodes (design and manufacturing rules) and real commercial processes.
Because SLIC teaches a model the general chip design process, the system is not tied to any company. This makes it a more scalable approach that could be used by many organizations for a range of circuit applications.
“The knowledge the model has gained about circuit design is universal in nature. That is the powerful aspect of this tool,” Han says.
In the future, the researchers want to explore self-improving models that can independently learn to handle more diverse topologies and design targets. They also want to use SLIC to build a multi-agent framework, in which many small language models work on different parts of a complex circuit design task.
“Yan’s work shows that a locally deployable model can learn transferable design behavior and iterate with a circuit simulator to improve a design, which could reduce repetitive manual tuning for engineers. This is the kind of work the MIT-IBM Computing Research Lab makes possible. We see it as opening the door to more sophisticated custom design, including RF and microwave circuits, in the settings where industry actually works,” says Zhang.
This research is funded, in part, by Analog Device, Inc., IBM, and the John L. Ocampo Endowment Fund of MACOM Technology Solutions.
