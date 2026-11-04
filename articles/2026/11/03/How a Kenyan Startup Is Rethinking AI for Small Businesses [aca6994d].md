---
id: "aca6994d762728b1"
title: "How a Kenyan Startup Is Rethinking AI for Small Businesses"
url: "https://spectrum.ieee.org/ai-small-business-mobile-money-startup"
link: "https://spectrum.ieee.org/ai-small-business-mobile-money-startup"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T14:30:02Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Lucila Pinto"]
language: "en"
summary: "The first time Mutembei Kariuki thought about how AI models could work in Kenya, his home country, was in 2019. He was attending a conference at the University of Tokyo on the future of AI, and kept hearing about how this technology was going to transform the world. “But nobody mentioned Africa at all,” he says. Even then—before AI giants like OpenAI and Anthropic had launched their chatbots to…"
tags: ["Africa", "Kenya", "Mobile-phones", "Digital-divide", "Ai-models"]
orgs: ["Anthropic", "Microsoft", "OpenAI", "Google", "Nvidia"]
topics: ["models & research", "products & launches", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1227
paywalled: false
image: "https://spectrum.ieee.org/media-library/a-photo-shows-a-smiling-man-in-a-barbers-chair-with-a-smiling-man-standing-over-him.jpg?id=68563378&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# How a Kenyan Startup Is Rethinking AI for Small Businesses

IEEE Spectrum · Lucila Pinto · 2026-11-03

The first time Mutembei Kariuki thought about how AI models could work in Kenya, his home country, was in 2019. He was attending a conference at the University of Tokyo on the future of AI, and kept hearing about how this technology was going to transform the world. “But nobody mentioned Africa at all,” he says.
Even then—before AI giants like OpenAI and Anthropic had launched their chatbots to the public—Kariuki could see significant obstacles to AI adoption in Africa. Internet access was slow and unequal, computing resources for training models were scarce, and there was little high-quality, structured training data. Most people, meanwhile, reached the internet through outdated, low-memory cellphones rather than computers or high-end phones.
Together with cofounders Jude Mwenda and Stephanie Njerenga, Kariuki created Fastagger, a startup that builds AI models that can run offline and on low-power cellphones. Its first big product, Auni, is a business-intelligence assistant that launched in 2024; it got a big push when it was integrated into the business app of M-Pesa, Kenya’s largest mobile money service. Since then, about 6,000 businesses have signed up. Auni helps small and medium businesses like barbershops, restaurants, and small manufacturers analyze their transaction data and gives them marketing recommendations.
Peter Chege, owner of a salon and barbershop in Nairobi, started using Auni last year. Before that, he recorded all his sales on paper. “We were not able to translate that information into a graph,” he says. Now, the app helps him identify his busiest days and hours, as well as his loyal customers. If a regular customer stops coming, for example, he can send a personalized message encouraging them to return.
Fastagger is part of an emerging effort to build AI around the technological realities of users in developing economies, rather than adapting products designed for wealthier markets. In Fastagger’s case, that meant finding a way to make their models work despite inexpensive phones, unreliable internet connections, and business records that may consist of little more than mobile-money transactions.
Designing AI for Kenya’s Small Businesses
Before developing Auni, Kariuki and his cofounders started by tackling the problem of data availability for AI training. They asked themselves: “How do we get Africa to catch up fast? How do we create training data fast enough, and then how do we actually get it into people’s hands fast enough?”
Mutembei Kariuki cofounded Fastagger to develop AI systems that can run offline and on basic phones. Afrikanna Production/Microsoft
They decided to focus on mobile phones, and specifically on mobile money apps. With more than 80 percent of Kenya’s adults using them, they offer a rich source of data.
One of Fastagger’s first steps was to adapt an open-source optical character recognition (OCR) model to read financial statements produced by mobile money apps. Existing models struggled with the low quality of the PDFs, which had unfamiliar formatting and sometimes contained stamps and errors. And because Fastagger’s prospective users often had unreliable internet connections, they made sure that key steps, like organizing the extracted data into tables, could run on-device.
Once they had a model that could process these documents, they began exploring how that structured financial data could help businesses. They spent entire days watching small-business owners work and interact with their customers. One challenge quickly became clear: Owners had little time or resources to think beyond day-to-day operations.
“They are standing up the whole day cutting hair,” Kariuki says of salon owners, who are now among Auni’s main users. “You have to think about that dynamic of the user journey, and how they live, and what will be going on in the background.”
The Fastagger app helps salon owner Peter Chege better manage his time and keep track of loyal customers.Afrikanna Production/Microsoft
For Chege, one of Auni’s biggest benefits was helping him manage his time. A simple chart showed him that mornings were his slowest hours, so he realized that he could run errands then or keep fewer barbers in the shop until around 1 p.m., when business picked up.
The founders also saw how much time businesses spent on manual processes and how automation could simplify those tasks. At a fish restaurant in Nairobi, for example, identifying loyal customers to offer them discounts required going through SMS sales receipts one by one, a tedious task that rendered client-retention marketing impractical. Now, with the help of Auni, the restaurant identifies its top customers automatically and offers them discounts.
Some of Auni’s functions—such as reading sales statements, analyzing data, and visualizing results—can happen offline on low-cost phones, without making cloud queries. These functions involve both AI tools and conventional software; for example, standard OCR software extracts the text and a small neural network identifies how each document is structured. More detailed analyses and answering questions about the data, however, require an internet connection.
Daniel Björkegren, an economist at Columbia University who studies AI’s implications for developing economies, says sub-Saharan Africa’s prevalence of basic phones rather than smartphones and computers could open the door to different kinds of AI use. “The history of technology should suggest that this is not going to be people running Claude Code or Codex on their laptop,” he says. “You will have people like that, but for much of the population, we’re going to have to figure out different usage modalities.”
How Local Needs Are Shaping AI
Despite Auni’s integration into M-Pesa, Fastagger remains a small startup. It has received support from Google, Microsoft, and Nvidia accelerator programs, but still has just three employees: Kariuki, Mwenda, and Njerenga, the original founders. Currently, they’re working on adding agents to Auni that could automatically implement marketing actions for business owners.
Fastagger has also developed a workforce management tool for Kenya’s security companies, which employ hundreds of thousands of people. Security guards often work in remote locations without reliable internet and use low-end phones. Fastagger’s AI agent communicates with them via SMS to track their routes, detects anomalies, and generates actionable alerts for operations teams.
Fastagger isn’t alone in tailoring AI models for the usage conditions in emerging economies. Other examples include an app for rural schools without internet in Chile; a medical triage chatbot for rural patients in India, and translation models for African languages that run on basic phones. Such innovations, which emerge from constraints, could help democratize access to AI. But that doesn’t mean the constraints themselves disappear or stop limiting development.
While Björkegren sees great potential in systems built for populations that have been poorly served by Silicon Valley, he believes there’s a risk in establishing too clear a division between small models designed for emerging economies and increasingly large, powerful models for wealthier regions. “I am worried that that could lead to a bifurcation,” he says. “We need to enable a large menu of different options and really make sure that we have access and then see what works.”
- These AI Workstations Look Like PCs but Pack a Stronger Punch ›
- The AI Boom Is Giving Rise to “GPU-as-a-Service” ›
- Invences Empowers Small Businesses With Smart Telecom Networks ›
Lucila Pinto is a bilingual journalist from Argentina who writes about AI, trust in science, and economic development, among other topics. Her work has appeared in Nature, Science, Rest of World, La Nación, and other publications. She holds a master's degree in science and technology journalism from Columbia University.
