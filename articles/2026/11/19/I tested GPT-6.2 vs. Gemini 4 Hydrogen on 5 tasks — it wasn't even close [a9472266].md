---
id: "a9472266503b1170"
title: "I tested GPT-6.2 vs. Gemini 4 Hydrogen on 5 tasks — it wasn't even close"
url: "https://tomsguide.com/ai/i-tested-gpt-6-2-vs-gemini-4-hydrogen-on-5-tasks-it-wasnt-even-close"
link: "https://tomsguide.com/ai/i-tested-gpt-6-2-vs-gemini-4-hydrogen-on-5-tasks-it-wasnt-even-close"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T11:36:45Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "null"
tags: ["AI"]
orgs: ["OpenAI", "Google"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 2087
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/tP6Q8PZyV854PPKXHKM6cD-1920-80.webp"
discussion_url: null
score: null
comments: null
community: null
---

# I tested GPT-6.2 vs. Gemini 4 Hydrogen on 5 tasks — it wasn't even close

Tom's Guide · Amanda Caswell · 2026-11-19

I tested GPT-6.2 vs. Gemini 4 Hydrogen on 5 tasks — it wasn't even close
The two newest models face off with everyday tasks
Google and OpenAI are going head-to-head again, and this time, their newest AI models arrived just five days apart.
Google launched Gemini 4 Hydrogen on November 12, promising faster responses, stronger reasoning and better performance across everyday tasks. Then, on November 17, OpenAI fired back with GPT-6.2 Astra, its latest model designed to tackle everything from complex research and writing to coding and creative projects.
Both companies are making big promises about what their AI can do, but benchmarks and launch demos only tell part of the story. What matters is how these models perform when you actually put them to work.
So I put Gemini 4 Hydrogen and GPT-6.2 Astra through the same five real-world challenges to see which one delivers better results, where each struggles and which AI is actually worth using.
Here's what happened.
1. Planning a nearly impossible day
Prompt: You're an event coordinator managing a one-day technology conference with 120 attendees, three meeting rooms and six speakers.
The conference runs from 9 a.m. to 5 p.m. Each speaker must deliver one 45-minute presentation. Every presentation requires a 15-minute room reset afterward.
Sign up to the Tom's AI Guide weekly newsletter summing up all the biggest AI news you need to know. Plus, analysis from our AI editors and tips on how to use the latest AI tools!
Additional constraints:
Speaker A is available only before noon.
Speaker B cannot present before 11 a.m.
Speakers C and D must not present at the same time.
Speaker E must present immediately after Speaker A, in the same room, allowing for the required room reset.
Speaker F is available only between 2 p.m. and 4 p.m.
All attendees must have a shared lunch break from noon to 1 p.m.
Each room can host no more than three presentations.
A 30-minute keynote involving all six speakers must take place at 4:30 p.m.
Create a complete conference schedule showing start times, end times, room assignments and speakers. Identify any conflicts and explain how you resolved them. Do not change any constraints without explicitly stating why.
GPT-6.2 identified both keynote conflicts, and it also identified the exceptions that would need approval. This directly addresses the instruction not to change constraints without explaining why. It correctly scheduled the six individual presentations and showed reset periods explicitly and preserved the shared lunch break.
Hydrogen was strong on presentation and the mechanics of the individual talks. Its table is easy to follow, with resets alongside each presentation. It also correctly handles the A-to-E sequence, B’s earliest start, C and D’s separation, F’s individual talk, lunch, and room limits. It also explains why the selected times work for the individual presentations.
Winner: GPT-6.2 wins on constraint reasoning and transparency. Hydrogen offers a solid schedule, but it mistakes fitting the individual presentations into the day for satisfying the entire conference specification.
2. Creative writing with a twist
Prompt: Write the opening 500 words of a literary mystery novel. A woman arrives at a small coastal town to attend the funeral of someone she has never met. Everyone in town recognizes her, but nobody will explain why.
Follow these rules:
Write in first person, past tense.
Start with a sentence of exactly seven words.
Include a conversation that sounds natural but contains a hidden threat.
Establish a distinctive setting without using a long descriptive paragraph.
Introduce one seemingly insignificant object that becomes important in the final sentence.
Do not use the words "mysterious," "secret," "shadow," or "dark."
End with a revelation that changes how the reader understands the opening.
Avoid clichés, melodrama and obvious AI-generated prose. Prioritize believable characters and original storytelling.
GPT-6.2 delivered an opening sentence that satisfies the seven-word rule and it introduced the identity question without explaining it. The narrator feels like a believable person and the setting emerges through activity. The threatening conversation retains plausible deniability. Alan’s questions about whether anyone expects her back could be concern or an assessment of how easily she could disappear. “If you get a signal” sharpens that uncertainty. That said, the ending is overcompressed.
Hydrogen provided a clear, accessible opening with an easy-to-follow progression from ferry to town to diner. Its opening sentence also contains exactly seven words: “The morning ferry docked at eleven sharp.” It maintains first-person, past-tense narration and avoids the prohibited words. Hydrogen’s main weakness is that the final revelation does not sufficiently change our understanding of the opening.
Winner: GPT-6.2 wins for an ending that makes the reader reconsider what already happened. Hydrogen’s ending mainly makes the reader wonder what happens next. Both can create suspense, but GPT-6.2 answers this prompt more successfully.
3. Build a working app from one prompt
Prompt: Build a fully functional, interactive website called "Decision Lab" that helps people compare difficult choices.
Users should be able to enter up to five options, define their own decision criteria, assign importance weights from 1 to 10, and score each option against every criterion.
The website must:
Automatically calculate weighted scores and rank the options.
Display a visual chart comparing the results.
Let users edit or delete options and criteria.
Include a sensitivity analysis showing whether the winner changes when the most important criterion's weight is reduced by 50%.
Include a "What if?" feature that lets users adjust weights and immediately see updated rankings.
Provide three realistic sample decisions that users can load instantly.
Work on desktop and mobile.
Save user changes between sessions if the environment supports persistent storage.
Use a modern, polished interface with intuitive controls. Every button and calculation must actually work.
Don't create a static mockup. Build the functioning app, then test its calculations and interactions. Explain any limitations.
GPT-6.2 built and published an interactive website for comparing up to five choices. I simply enter what matters, give each criterion a weight, and score the options. The site ranks them and updates the chart as changes are made. It also added a “what if?” slider section to experiment without changing original weights.
Hydrogen built a self-contained, responsive web application and tested its calculations and controls before displaying it. It also build a scoring matrix, added support for up to 5 options and implemented live calculations and charting.
Winner: GPT-6.2 wins for a more thorough and useful website. The interactive site followed the prompt exactly while also adding extras that were useful for the overall project.
4. The impossible customer-service decision
Prompt: You're the operations manager of an independent bookstore.
It's 4 p.m. on Friday, and the following problems happen simultaneously:
A bestselling author is arriving at 5 p.m. for a signing attended by 80 customers.
The shipment containing 60 copies of the author's book is delayed until Monday.
You have only 12 copies in stock.
Your only experienced employee just called in sick.
A customer claims they were charged twice for a $75 purchase, but your payment system is offline.
A local journalist is asking whether the store is experiencing financial difficulties.
Your landlord has emailed demanding an overdue $2,000 payment by Monday.
You have $900 in available business cash, two inexperienced employees and one hour before the event.
Develop a realistic action plan.
Rank problems by urgency, explain what you would do in the first 15 minutes, write a short statement for customers attending the signing, and draft a response to the journalist.
You cannot cancel the event, invent money, pretend books have arrived or promise refunds that you cannot verify.
Be transparent without creating unnecessary panic. Explain what information you still need before making irreversible decisions.
GPT-6.2 treated the task as several connected operational problems, rather than simply a shortage of books. It prioritized safe event operations and gave inexperienced staff narrow roles. It checked capacity, kept exits clear, and assigned responsibility for the queue to better manage 80 attendees without the experienced employee.
Hydrogen was practical in several aspects. But it promised to put bookplates into books “as soon as the boxes arrive Monday.” That turns the expected shipment date into a firm fulfillment commitment. Overall, the model introduced several unsupported assumptions — and its customer statement promises arrangements that its own plan says still need confirmation.
Winner: GPT-6.2 wins as the stronger operations-manager answer because it preserved options while keeping customers, staff, the author and the landlord informed. Hydrogen had useful ideas but repeatedly moved from “ask whether this is possible” to “tell customers this will happen.”
5. A logic puzzle designed to catch mistakes
Prompt: Five researchers, Ava, Ben, Chloe, Daniel and Elena, each work on a different project (robotics, climate, medicine, astronomy and cybersecurity), use a different programming language (Python, Rust, JavaScript, Go and Julia), and work on a different floor (1 through 5).
Determine each researcher's project, programming language and floor using these clues:
Ava works on floor 3.
The robotics researcher works on floor 5.
The person using Rust works exactly one floor above the climate researcher.
Ben works on a lower floor than Chloe.
The astronomy researcher uses Julia.
Daniel uses Go.
The cybersecurity researcher works on floor 1.
Elena works exactly two floors below the robotics researcher.
The medicine researcher uses Python.
Chloe does not work on robotics or climate.
The JavaScript user works on floor 2.
Ben does not use Rust.
Daniel works on floor 4.
The climate researcher works on floor 2.
Produce a complete table showing every researcher's floor, project and language.
Explain whether the clues produce exactly one solution, multiple solutions or no solution. If the puzzle is inconsistent or underdetermined, identify the problem rather than inventing an answer.
GPT-6.2 followed the prompt’s most important instruction. It identified inconsistency rather than inventing a complete assignment and it provided three clear ways to demonstrate the problem.
Hydrogen reached the same correct conclusion and explained the same underlying problems. It successfully identified three contradictions and flagged the Floor 3 collision between Ava and Elena, the project–language mismatch on Floors 3 and 4 (medicine/Python and astronomy/Julia vs. Rust and Go), and Chloe being forced onto Floor 1 with no lower floor available for Ben.
Winner: Hydrogen wins narrowly on clarity, accuracy and presention.
Overall winner: GPT-6.2
Google and OpenAI are competing to become your everyday AI assistant, but how each one handles tasks can make all the difference. In this experiment, GPT-6.2 won nearly every test, which might just make it one worth paying for. 
Hydrogen is free and did a decent job answering each prompt, but often struggled with assumptions and adding details. For users hoping to keep costs down, Hydrogen is still a good choice, you'll just want to do some extra fact-checking and evaluate the model's response a little closer than you would with GPT-6.2. 
Overall, GPT-6.2 proves to be a strong model for taking on every day tasks thoroughly, accurately and quickly. 
Have you tried these models yet? Let me know in the comments what you think of each one.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds. Subscribe to Tom's Guide on YouTube and follow Tom's Guide Entertainment on TikTok and Instagram.
More from Tom's Guide
- I tested ChatGPT’s new GPT-6.2 Astra with one prompt — and built a website I’d actually use
- I gave Google’s new Gemini 4 Hydrogen one prompt to find out where my money goes — and the results surprised me
- A lawsuit could force OpenAI, Anthropic and Google to stop building new AI models — here's what happens next
Amanda Caswell is the AI Editor at Tom's Guide and one of today’s leading voices in AI and technology. 
A celebrated contributor to various news outlets, her sharp insights and relatable storytelling have earned her a loyal readership. Amanda’s work has been recognized with prestigious honors, including outstanding contribution to media.
Known for her ability to bring clarity to even the most complex topics, Amanda seamlessly blends innovation and creativity, inspiring readers to embrace the power of AI and emerging technologies.
As a certified prompt engineer, she continues to push the boundaries of how humans and AI can work together.
Beyond her journalism career, Amanda is a long-distance runner and mom of three. She lives in New Jersey.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
