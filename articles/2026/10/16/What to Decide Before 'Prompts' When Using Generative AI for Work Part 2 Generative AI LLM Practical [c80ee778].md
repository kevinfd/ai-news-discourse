---
id: "c80ee778d7110d39"
title: "What to Decide Before 'Prompts' When Using Generative AI for Work | Part 2: Generative AI/LLM Practical Applications Released"
url: "https://note.com/minato_systems/n/n280c5209dce9?hl=en"
link: "https://note.com/minato_systems/n/n280c5209dce9?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-16T03:48:00Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["ミナト｜実務特化の自動化戦略"]
language: "en"
summary: "Even though you are using generative AI, for some reason, your work doesn't seem to get much easier.Having ChatGPT write text. Having it summarize documents. Having it generate ideas.There is no doubt ..."
tags: []
orgs: ["OpenAI"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 1406
paywalled: false
image: "http://www.bing.com/th?id=ONUT.6zeR6fWuOveIdaYjrKJoVg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# What to Decide Before 'Prompts' When Using Generative AI for Work | Part 2: Generative AI/LLM Practical Applications Released

note · ミナト｜実務特化の自動化戦略 · 2026-10-16

What to Decide Before 'Prompts' When Using Generative AI for Work | Part 2: Generative AI/LLM Practical Applications Released
Even though you are using generative AI, for some reason, your work doesn't seem to get much easier.
Having ChatGPT write text. 
Having it summarize documents. 
Having it generate ideas.
There is no doubt that it is convenient.
However, when you try to use it continuously for work,
“The output is different every time,” 
“In the end, a person has to check everything,” 
“I don't know how much I should leave to the AI,” 
“I keep having to fix the prompts.”
It is easy to end up in this state.
The cause is not just how you write your prompts.
It is that what you are actually delegating to the AI has not been designed in the first place.
This is a major point.
📌From Generative AI as a 'Tool for Asking Questions' to a 'System for Delegating Work'
If you are only using generative AI personally,
is fine.
However, if you are incorporating this into business operations, the story changes.
For example, in handling inquiries,
Receive inquiry
↓
Classify content
↓
Extract necessary information
↓
Draft a reply
↓
Human review
↓
Send
There is a sequence of steps like this.
Which parts of this should you delegate to the AI?
What information should you provide?
In what format should you have it returned?
What constitutes a 'passing' result?
What should be done if the AI cannot make a judgment?
Only after deciding these things does it become AI utilization that can be used in practical work.
❶ First, decide on the 'input'
When AI responses are unstable, many people modify the prompt.
However, what you should look at before that is the input.
If every time,
- the amount of information provided is different
- the format is different
- necessary information is missing
- the prerequisites are different
then the output will not be stable even with the same prompt.
For example, if you are organizing meeting details,
- customer name
- meeting date and time
- meeting content
- customer requests
- product information
and so on, you should standardize the information passed to the AI.
AI quality is influenced not only by instructions but also by input design.
❷ Next, decide on the 'output'
'Please summarize this clearly'
means different things to different people, so the expected results will vary.
In practical work,
Customer issues
XX
Requests
XX
Concerns
XX
Next actions
XX
Person in charge
XX
It is easier to use if you decide on the necessary items in advance, like this.
Furthermore, if you are passing it to a system, you can also make it structured data like JSON instead of plain text.
To connect AI output to the next task,
you need to design not just 'what to have it write,' but also 'in what format to receive it'
as well.
❸ Decide on the criteria for a 'correct answer'
This is surprisingly often overlooked.
Even if you have the AI generate an answer,
what criteria must be met to use that answer
is often left undecided.
For example,
- do not make up numbers
- label unknown content as 'unknown'
- output all required items
- stay within the specified character count
- do not add content not present in the source information
and so on.
These are the evaluation criteria.
If you are integrating AI into your workflow, you need to think not just about generation, but also about evaluation.
❹ Decide which tasks not to leave to AI
As generative AI evolves,
you might start thinking,
'Can't I just leave everything to the AI?'
However, complete automation is not always the best approach.
For example,
- high-value contracts
- Responses to key clients
- Legal judgments
- Final hiring decisions
- Handling serious complaints
and so on.
Even if you leave drafting or organizing information to AI, a human should check it in the end.
There are tasks for which this approach is more appropriate.
Utilizing AI does not mean eliminating people.
It means handing over the parts that don't require human thought to AI, and creating a state where you can focus on work that requires human judgment.
❺ Create prompts last
Once you have decided this much, prompts become much easier to create.
What you need is:
- Role
- Objective
- Input
- Processing rules
- Output format
- Prohibitions
- Handling of uncertainties
.
In other words, a prompt is not a magic spell.
It is a specification document for communicating business design to AI.
Rather than 'searching for a good prompt',
deciding what kind of work to entrust to the AI and under what conditions
is far more important in practical business.
📘Part 2 'Generative AI/LLM Practice' has been released.
At Minato | Practical Automation Strategy,
Part 2 | Generative AI/LLM Practice
has been released.
In addition to the 25 materials in Part 1, 25 new materials have been added.
Currently,
Part 1 | Automation Strategy/Business Design
Part 2 | Generative AI/LLM Practice
a total of 50 materials are available.
In Part 2, rather than just using generative AI, we cover:
- Basics of Generative AI/LLM
- Prompt Engineering
- Summarization, Classification, Extraction, and Conversion
- Structured Output
- AI Knowledge
- RAG
- Evaluating AI output
- Countermeasures for incorrect generation
- AI quality control
We cover the concepts and design for incorporating these into practical work.
The 5 courses of Part 2
Course 1 | Generative AI/LLM Basics
What can AI do, and what is it bad at? 
We will organize the necessary foundation before incorporating it into practical work.
Course 2 | Prompt Engineering
Instead of one-off 'clever instructions,' we will design prompts that can be used repeatedly.
Course 3 | Text and Information Processing with AI
We will use AI for information processing, such as summarization, classification, extraction, conversion, and structuring.
Course 4 | AI Knowledge Systems
Learn the concepts for enabling AI to utilize external information and your company's own data.
Course 5 | AI Quality Control
We cover how to evaluate AI output, reduce errors, and operate it stably.
🌱Building skills that can be implemented, one part at a time
At Minato Implementation Lab, we do not use a method of handing over 250 teaching materials all at once.
Month 1 | Part 1
Month 2 | Part 2
Month 3 | Part 3
...
Month 10 | Part 10
We release them in stages in this format.
Rather than gathering a large amount of information at once,
Learn → Try → Build → Move Forward
This is because we prioritize these steps.
In Part 1, we designed 'what to automate'.
In Part 2, we move to the stage of adding new processing capabilities called Generative AI on top of that.
And moving forward, we will connect this to:
Data Processing
API
Python
No-code
AI Agents
Digital Assets
Sales Automation
Production Operations
to build further.
🔗Currently Available Courses
Part 1 and Part 2, a total of 50 teaching materials are now available.
▶ Minato Course Site
You can search for materials that match your goals by title, course, or keyword.
🏠Minato Implementation Lab
For those who want to go deeper into actual design and implementation.
3,980 yen per month includes:
- Release of 1 part, 25 materials every month
- All 10 parts, 250 materials over 10 months
- Password provided individually via DM
- DM support for up to 3 questions per month regarding material content, design, and implementation
- Continuous provision of revised materials and additional resources
is provided.
▶ Minato Implementation Lab
In free articles, we cover the 'concepts.' In our courses, we cover the 'completion.'
In this article, I introduced the basic mindset for making decisions in practical work.
In the Minato Implementation Lab materials, we go further from here to cover:
- Ready-to-use templates
- Completed examples with entries and settings
- Implementation procedures
- Practical assignments
- Decision criteria and checklists
- Failure examples and correction methods
.
Don't just learn; complete deliverables you can use in your own work.
This is the difference between free articles and practical courses.
Moving from 'being able to use' generative AI to 'being able to design it for work.'
Not just knowledge, but implementation.
Part 2 will also build upon this foundation.
#GenerativeAI #AI #ChatGPT #Automation #WorkEfficiency #Prompt #LLM #AIUtilization #DX #AIAgent
