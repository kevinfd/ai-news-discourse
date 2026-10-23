---
id: "63c31ca523f91ccf"
title: "What FDE means at OpenAI"
url: "https://openai.com/index/forward-deployed-engineering-means"
link: "https://openai.com/index/forward-deployed-engineering-means"
source: "OpenAI"
domain: "openai.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-22T06:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: []
language: "en"
summary: "What forward deployed engineering means at OpenAI"
tags: ["AI Adoption"]
orgs: ["OpenAI"]
topics: ["models & research", "jobs & society", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1944
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# What FDE means at OpenAI

OpenAI · 2026-10-22

What FDE means at OpenAI
What we do, how we work, and how we solve enterprise’s toughest problems to deliver real impact.
By: Colin Jarvis, Head of Forward Deployed Engineering at OpenAI
When Codex came out, someone on the team asked me, “What do we do when Codex can just one-shot the use cases we spent the last few months building?”
That question gets to the heart of what FDE means at OpenAI. We work alongside customers to understand their hardest problems and build solutions they can depend on. What we learn helps shape our products and gives Research concrete problems to solve.
That is progress. If we make ourselves obsolete every couple of months, our FDE team is doing its job.
I founded the team in early 2025 to close what we call “the deployment gap”: the distance between what models appear capable of and what people can reliably use to do their work.
Model capabilities have moved faster than the systems and processes needed to put them to use. Sometimes the missing piece is a product. Sometimes a model performs well on a benchmark but cannot do the job with real-life variables and constraints.
We focus on customers’ hardest problems. Where our models can do the job today, we work with Product and our customer to make the solution repeatable and, where they fall short, we work with customers and Research to define the gap and make improvements. Our goal is for each engagement to leave the next customer with a better starting point—if we raise the floor to the point our customers don’t need FDEs to solve this class of problem the next time, we have done our job well.
The challenge for John Deere, a 200 year-old agriculture business, was how to scale personalized advice for farmers.
One example is See & Spray, its precision weed-control technology, which uses cameras and machine learning to identify and spray weeds rather than treating entire fields to reduce chemical use by up to 70%.
But realizing those benefits depends on farmers knowing how to configure the technology, plan their season, and adjust their practices as conditions change.
John Deere deployed OpenAI’s APIs to help make that support personalized and scalable.
AI can answer farmers’ questions in natural language, provide tailored setup guidance and recommendations, identify when equipment may not be delivering its full potential, and help farmers understand the value they’re getting from the technology.
The opportunity extends beyond any single interaction: to deliver relevant guidance throughout the customer journey, helping farmers make better use of their equipment while improving efficiency and sustainability.
This is the kind of challenge OpenAI FDEs work to solve: helping organizations move from AI capabilities to systems that deliver practical value in complex, real-world environments.
But the problems are often wide open, there may be no established ground truth, and there is no playbook. Everyone wants to build something that has never existed. Fewer people want to do what it takes to get there.
Finding talented FDEs while raising the baseline for “good enough” has meant constant experimentation and application.
At the start of every FDE team session, I put up a slide with one core value: “Start with the outcome, do what it takes to succeed, then follow with scale”.
An impressive demo can go a long way before anyone asks whether it works in the real world.
Our job is to solve the customer’s problem to a standard we can stand behind in production.
In mid-2025, we had around 15 FDEs working with a large semiconductor customer on 10+ use cases. The ambition was to make their verification process AI-native, covering:
- Directed test generation
- Root cause analysis and debugging
- An architecture assistant
Verification can account for ~70% of a project’s effort in this industry. The opportunity was enormous, and there were many possible places to start.
Some FDEs had joined OpenAI just days earlier and had never worked in semiconductors. They embedded with the customer’s verification team, studied chip design in their spare time, and built evals with the engineers to test whether the AI could generate useful tests and correctly diagnose chip failures.
Alongside that learning, we built custom harnesses for the individual use cases. Over the first 3-6 months, all of them reached production and early user adoption. The payoff was seeing the metrics:
- ~48% time saved through AI-based directed test generation.
- 22% median performance improvement through kernel optimisation.
- Weeks of debugging compressed into hours
When we played this all back the Chief Hardware Officer asked, “Did you guys work as chip designers before coming here?”
Our FDEs don’t need to know the industry on day one but it is their responsibility to learn it.
As coding assistants make software faster to build, understanding the customer’s business becomes even more important. We build teams with a mix of generalists and domain experts.
You need enough knowledge to make sound judgments, and enough curiosity to question assumptions about the status quo.
In life sciences, for example, our FDEs’ scientific backgrounds help them earn trust with researchers working on pre-clinical drug discovery tasks such as target validation and prioritization, gene-expression analysis, and chemical synthesis-route reconstruction. That expertise lets them contribute informed judgment about how those workflows could improve.
We had shown that these workflows could deliver value, but each still required too much custom integration to extend to another team. The next challenge was to preserve those results while making the software easier to deploy and maintain.
By then, Codex had grown in capability. One FDE tested rebuilding their application around it, then worked with the team to move the use cases onto a common harness with Codex at its core.
Custom applications became plugins and skills built on common Codex primitives. Codex also became the interface, allowing us to retire the separate terminal UIs and CLIs we had written for individual use cases.
We were able to remove roughly 90% of the custom code from each project, and this changed how we built, maintained and scaled these workflows:
- We could benefit from centralized improvements to Codex, reducing the amount of glue code required for each individual use case
- Key functionalities were bundled as skills and plugins, making them easier to share with each other and to be centrally controlled by the AI CoE. This meant that extending from one team to the next could be as simple as swapping in new connectors/MCP servers, building fresh evals (which we also had a skill for) and getting up and running.
- In one August 2026 example, the initial deployment took two months. Extending the solution to a second team took one day. The next teams onboarded faster as we scaled—this has continued, with a use case in August 2026 taking 1 day for the second team after the initial deployment took 2 months.
That is one version of making ourselves obsolete. The work we had done to reach production established what mattered. As the underlying product improved, we could replace much of our custom implementation and keep the value it delivered.
This is why the order matters. LLMs let us build fast. Use that speed to get something valuable into users’ hands, learn what holds up in practice, and then scale what works.
The same principle applies across all engagements.
OpenAI Presence, our product for enterprise voice and chat agents, grew out of real customer deployments. The work began with Swarm(opens in a new window) and evolved through the Agents API, and today one customer now handles more than half of its calls with AI.
Getting those deployments into production taught us which problems needed a custom solution and which building blocks other teams could use. We brought those building blocks into Presence, making it easier for developers to automate regulated workflows without rebuilding the underlying infrastructure. Each deployment helped shape the product and gave the next customer a better starting point.
With Thrive Holdings, OpenAI FDEs and researchers worked alongside engineers and accountants to build Tax AI for Crete’s accounting firms. During its pilot, Tax AI processed 7,000 tax returns and increased throughput by about 50%.
One of the hardest challenges was automating rental-property returns, which required six weeks of engineering and practitioner review to reach 90% precision and recall. The work created reusable patterns that made it easier to extend Tax AI to other complex tax schedules.
The teams are now applying the same approach to bookkeeping, audit, and IT support—building systems that improve through practitioner feedback and real-world use.
Sometimes a better product lets us simplify what we built but sometimes the model itself cannot yet do the job.
If we only build what today’s models already make possible, we will not uncover the intelligence gaps Research needs to close next. Therefore a lot of our important engagements start at those limits with the customer, FDE and Research committed to working through them together.
We had already developed a customer-service platform with a large telecommunications customer, and they wanted to extend it to voice.
Voice accounted for around 90% of their customer-service volume. These cases were more expensive to contain than chat, and brought a range of new technical challenges in getting accents, tone and latency/accuracy up to production grade. Getting it right would make a substantial difference to their business.
During scoping, our model scored around 60% on the key evals we used to assess whether it could do the job in production. We had reached the limits of its capabilities. Function calling and instruction following in customer-service scenarios needed to improve.
We explained that to the customer and brought Research into the work. FDE worked with the customer to build the platform and define what the model needed to do. Research worked on closing the capability gaps, with successive model snapshots letting us test progress against the customer’s requirements.
Over six months, performance on the key evals rose from around 60% to 80% and then 90%+, reaching the levels needed for production.
The resulting voice model now supports that customer’s deployment, other custom customer-service deployments, and managed deployments through Presence. A problem encountered in one customer’s business helped identify improvements that could serve many others.
Each part mattered. The customer committed to working on a problem the model could not yet solve. FDE stayed close enough to frame that problem, build the platform and drive the engagement from start to finish. Research improved the underlying model capabilities.
This is the other version of making ourselves obsolete: helping turn a problem today’s models cannot solve into a capability future models can deliver. The return on our work extends beyond the hours we spend with any one customer.
I joined OpenAI to help make AI useful in people’s everyday work. That still guides the team. I often say to the team that in most cases in LLM development, Occam’s Razor applies—the simplest solution is the best. In a company that is defined by its cutting edge research and in an industry that is tainted by hyperbole, we want to build stuff that works reliably which people in the field can depend on.
The goal is for each engagement to improve what comes next: a product that is easier to deploy, a model that can handle a harder task, or less custom work for the next customer.
If you have a hard problem you want to solve, we’d love to work with you. If you want to help solve those problems, we’d love you to join us.
So what do we do when Codex can handle the work we spent months building?
Go find the harder problem.
