---
id: "669162c73b41696b"
title: "Mistral’s Le Chonk is now a top open model for coding, ranking alongside Codex GPT-6.1 Terra"
url: "https://zdnet.com/innovation/mistral-large-4-weights-release"
link: "https://zdnet.com/innovation/mistral-large-4-weights-release"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T14:00:31Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "Mistral has released the weights for Large 4, along with some impressive Artificial Analysis scores."
tags: ["Artificial Intelligence"]
orgs: ["Mistral", "OpenAI", "Anthropic", "Nvidia", "Google", "DeepSeek", "Hugging Face", "China"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 650
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-2293676090.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Mistral’s Le Chonk is now a top open model for coding, ranking alongside Codex GPT-6.1 Terra

ZDNet · Radhika Rajkumar · 2026-10-29

ZDNET’s key takeaways
- As planned, Mistral has released the weights for its ML4 model.
- ML4 sets a new bar for Western open models.
- Open models are increasingly competitive with proprietary models.
French AI lab Mistral shipped its latest model, Mistral Large 4 (ML4), nicknamed “Le Chonk” for its trillion-parameter size, in preview on Oct. 6. As promised, the lab has released the model’s weights, alongside some new benchmark scores that show Western open models gaining ground over their Chinese peers.
Also: Open weights vs. closed: An AI civil war’s afoot
New coding performance ranking
ML4’s score on the agentic coding benchmark Terminal-Bench 4.0 jumped to 41% from its preview version’s 28% to 41%, beating Opencode’s GLM-5.3 by one small but important point. On the overall Index, however, which shows a model’s composite score across three relevant benchmarks, ML4 is a point behind GLM-5.3, scoring a 48 to GLM-5.3’s 49. Codex GPT-6.1 Terra also scores a 48 overall.
As a reminder, benchmark scores themselves should be taken with a grain of salt, especially considering how many models cheat.
Still, that improvement in performance is meaningful for just a few weeks of extra training. As proprietary AI remains expensive to use, economical models that don’t sacrifice performance are eye-catching. ML4 “rivals top open models such as GLM-5.3 on the Artificial Analysis Coding Agent Index while using 47% less tokens per task on average,” Mistral said.
Cybersecurity prowess
When Mistral released ML4 in preview earlier this month, it touted how the model prioritizes cyber defense capabilities, advertising customizable control and data sovereignty. The company has spent the last few weeks working with developers and leaders to assess the model’s cybersecurity capabilities, a practice that’s becoming commonplace for proprietary American labs like OpenAI, Google, and Anthropic as concerns about model security mounts.
Similarly to Anthropic’s Project Glasswing and OpenAI’s rollout of Astra, Mistral’s initial testing partners got access to a less guardrailed version of ML4 with “expanded cybersecurity capabilities.”
At least by some measure, ML4’s promises seem to have come true: Le Chonk scored just above DeepSeek V4.1 Flash on the CyberGym benchmark for defensive cybersecurity, which measures how well models find “real memory-safety vulnerabilities in C/C++ open-source projects, reproducing them with proof-of-concept inputs, and patching them without breaking the projects’ tests.”
Recent AI security incidents have somewhat pitted open and proprietary models against each other. Initially framed as less safe because of their malleability, open models are viewed as a new option for cyber defense after proprietary models from Anthropic and OpenAI proved just as risky.
Mistral said ML4 is built for security that stays under user control — unlike proprietary models, which frontier labs can technically rescind access to at any time.
“The cyber defense capabilities will enable enterprises and governments to defend themselves against threat actors that are jailbreaking closed models to perform cyberattacks,” Mistral co-founder Guillaume Lample said during a briefing for the Oct. 6 preview release.
Following the Hugging Face breach, Mistral was one of many companies that signed Nvidia’s Open Secure AI Alliance, a cross-industry partnership that argues open models are crucial to democratizing defenses against increasingly common AI security incidents.
Also: This new ChatGPT scam tricks you into installing malware
By Nvidia’s logic, and its Alliance that aims to democratize AI security tools, the race is between Mistral and other open models to achieve state-of-the-art security prowess.
More for less compute
Training a competitive model in a compute shortage is no small task for a trimmer lab like Mistral, which doesn’t have the same resources as a pre-IPO giant like Anthropic.
Also: These Claude Enterprise features let you track AI ROI
“ML4 was trained from scratch on 4,000 Nvidia Grace Blackwell GPUs over two months, deployed in Mistral’s own data centers in Europe,” the company said. For context, Nvidia CEO Jensen Huang said on X that OpenAI trained GPT-6 Astra on roughly 100,000 GPUs.
