---
id: "0ed98d3b2521f33b"
title: "Meet the Anthropic Engineer Keeping Its AI Agent Trustworthy"
url: "https://spectrum.ieee.org/anthropic-engineer-ai-agent"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-10-12T18:00:02Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Amanda Davis"]
language: "en"
summary: "If you’ve ever wondered how Claude and similar AI agents can answer complex questions in seconds and where they get the information, you’re not alone. Gurmeet Saran works to find that answer every day as an engineer at Anthropic in San Francisco, the AI research company behind Claude. The IEEE senior member is developing an infrastructure to understand the mechanics behind the chatbot’s behavior…"
tags: ["Ieee-member-news", "Artificial-intelligence", "Chatbots", "Careers", "Anthropic", "Type-ti"]
orgs: ["Anthropic", "Meta"]
topics: ["jobs & society", "agents & coding", "health & science", "models & research"]
content_source: "fulltext"
word_count: 1340
paywalled: false
image: "https://spectrum.ieee.org/media-library/an-indian-man-in-a-dress-shirt-smiling-in-front-of-the-entrance-to-an-office-building.jpg?id=68416593&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Meet the Anthropic Engineer Keeping Its AI Agent Trustworthy

IEEE Spectrum · Amanda Davis · 2026-10-12

If you’ve ever wondered how Claude and similar AI agents can answer complex questions in seconds and where they get the information, you’re not alone.
Gurmeet Saran works to find that answer every day as an engineer at Anthropic in San Francisco, the AI research company behind Claude. The IEEE senior member is developing an infrastructure to understand the mechanics behind the chatbot’s behavior and to ensure its underlying architecture produces reliable outputs.
Gurmeet Saran
Employer
Anthropic in San Francisco
Title
Member of technical staff
Member grade
IEEE senior member
Alma maters
University of Kalyani, in India; Birla Institute of Technology and Science, in Pilani, India
“My job is to make sure the data is accurate, structured, and trustworthy, and that private data stays private,” he says. “As I learned earlier in my career, privacy can’t be a layer you bolt on—it has to be part of the architecture from the start.” If you can’t trust the logic, he adds, you can’t make reliable claims about the behavior, and that has real safety implications.
Safety is a priority for Anthropic, he says. According to Claude’s mission statement, the company wants the AI agent to be “genuinely helpful to the people it works with or on behalf of, as well as to society, while avoiding actions that are unsafe, unethical, or deceptive.” Crucial to the mission is ensuring that researchers can observe and understand how AI models behave, a challenge that is especially acute for large language models, Saran says.
“We have decent tools to monitor databases and web services,” he says, “but for LLMs, we’re still figuring it out.”
Solving data quality problems at Yahoo, Intuit, and Meta
Saran’s interest in computing systems dates back to his childhood in Kolkata, where he logged as much time as he could in the school computer lab.
“I remember the first time I used one of the computers,” he says. “What struck me was that you could write instructions, and the machine would follow them exactly. No ambiguity.
“That felt magical to me.”
After graduating from high school in 1999, he stayed in India to pursue advanced degrees. He earned a bachelor’s degree in electronics and telecommunication engineering in 2004 at the University of Kalyani. In 2010, he earned a master’s degree in software engineering from the Birla Institute of Technology and Science in Pilani.
While a graduate student, he began his career in 2007 at Yahoo as a technical lead of the data team in Bengaluru, India. While there, he encountered the project that shaped his career trajectory: working on web analytics and business intelligence reporting solutions.
“We kept running into a frustrating problem,” he recalls. “Different teams would calculate the same website metric—something like daily active site users—using slightly different logic, and end up with conflicting answers. It sounds like a small issue, but when leadership is making decisions about resource allocation and product development using that data, not knowing which number is correct becomes a problem.”
The team built a central data repository with defined metrics, essentially serving as a single source of truth. Saran created a model that defined what “daily active site users” means, breaking down which events counted, how to handle edge cases (or when standard code fails), and more.
With the new model, data teams across the company could rely on a standard method to determine the number of daily active users for the projects and sites they were responsible for and obtain comparable results using the same logic.
From there, Saran and his team built Yahoo! Digits, an internal web analytics tool used for all the company’s products.
Saran left Yahoo in 2010 to join Intuit as a staff engineer in Mountain View, Calif. He helped build the analytics infrastructure that unified data across the company’s products, including TurboTax and QuickBooks accounting software. During his tenure, Intuit developed a feature that detected fraudulent tax filings in real time. It required Saran and other engineers to build a system to protect taxpayer data while adhering to strict U.S. Internal Revenue Service policies.
“IEEE operates in a lot of countries where engineers don’t have easy pathways into the global professional community. That kind of connection matters as AI development spreads beyond a handful of organizations.”
“This taught me that privacy and governance can’t be layers you bolt onto software after the fact,” he says. “They have to be part of the architecture from the start.”
Saran joined Meta (known as Facebook at the time) in 2016 as a lead software engineer in Menlo Park, Calif. The company was facing controversy over its video metrics: Meta publicly acknowledged an error that caused it to overstate the number of views for posted videos.
“This wasn’t a coding bug; it was an architectural problem,” Saran says. He built a system that worked similarly to what he had developed at Intuit, whereby one single truth was defined to govern all video view metrics across the site.
That system, Metric360, eventually became part of the site’s architecture. By the time he left Meta in 2021, he says, Metric360 was being used across the company to calculate video metrics.
He left the company to become a principal software engineer at Wealthfront, a financial services company in Palo Alto, Calif. He helped build the company’s data infrastructure.
Building trustworthy AI systems at Anthropic
Saran joined Anthropic in 2025 as a member of the technical staff.
To describe the implications of his work, he uses a medical analogy: “Imagine a doctor is monitoring a patient’s vital signs and making treatment decisions based on those numbers. What if one or a few of the medical devices used were slightly miscalibrated? Even if most readings are fine, it’s a serious problem because the difficult decisions happen in the margins.
“It’s the same with AI systems. My job is essentially to make sure the instruments are giving accurate readings—that the data means what it says it means.”
His job comes with high stakes and complex problems to solve.
“AI agents are especially tricky to observe,” he says. “When a system is taking sequences of actions [generating conversational responses with different users], you need a way to capture what it did, what information it was working from, and whether outcomes matched what the end user expected. And you have to do all of that without exposing anyone’s private information—the systems are designed to recognize sensitive data and keep it protected as it flows through. It’s a much more demanding observability problem than anything I’ve worked on before.”
Solving for system reliability while AI is still in its early days of adoption is both Saran’s passion and the problem that keeps him up at night, he says.
“I think making AI systems genuinely auditable and transparent is one of the more important engineering problems of the next decade,” he says, “and it doesn’t get talked about as much as model capabilities do.”
IEEE can play a role in shaping AI development
Saran joined IEEE in March 2025.
“After more than 20 years of building data infrastructure across organizations like Yahoo, Intuit, Meta, and Wealthfront,” he says, “I wanted to contribute back to the technical community through peer review, publishing, and engaging with the broader engineering research ecosystem.”
He says he believes IEEE can play an essential role in shaping the future of AI through its standards work.
“We have standards for everything, from building codes to software testing,” he says. “AI infrastructure needs something similar, and IEEE has the credibility and the reach to do that.”
Another problem that IEEE can solve for, he says, is access: “IEEE operates in a lot of countries where engineers don’t have easy pathways into the global professional community. That kind of connection matters, especially as AI development spreads beyond a handful of organizations in a few cities.”
- Why AI Chatbots Agree With You Even When You’re Wrong ›
- Claude Mythos Preview Requires New Ways to Keep Code Secure ›
- 12 Graphs That Explain the State of AI in 2026 ›
