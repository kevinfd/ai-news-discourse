---
id: "e1da163523969220"
title: "The Pragmatic Engineer Essay Challenge: Category Winners (Part 1)"
url: "https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-essay-challenge"
link: "https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-essay-challenge"
source: "The Pragmatic Engineer"
domain: "newsletter.pragmaticengineer.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-24T19:16:38Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Gergely Orosz"]
language: "en"
summary: "Before we start, a Black Friday special. With Black Friday coming up, you can get 20% off the full subscription for the first year - which is $120 for the year, or $10/month. Paid subscribers get access to full deepdives, The Pulse on Thursdays, to resources for engineering managers and software engineers , and to the full archive . Get this special offer The offer is available until Tuesday, 1…"
tags: []
orgs: ["Anthropic", "OpenAI"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 6360
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!nbv5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F710bc15b-efad-4643-bb7d-fd4748f219ff_1672x941.png"
discussion_url: null
score: null
comments: null
community: null
---

# The Pragmatic Engineer Essay Challenge: Category Winners (Part 1)

The Pragmatic Engineer · Gergely Orosz · 2026-11-24

Before we start, a Black Friday special. With Black Friday coming up, you can get 20% off the full subscription for the first year - which is $120 for the year, or $10/month. Paid subscribers get access to full deepdives, The Pulse on Thursdays, to resources for engineering managers and software engineers, and to the full archive.
The offer is available until Tuesday, 1 December. You can also gift this offer.
To mark The Pragmatic Engineer’s fifth birthday in September, I launched an essay competition on the theme of how things have changed in building software since the emergence of AI models that are better than ever at coding. Engineers shared their experiences and observations, and a $10,000 grand cash prize for our favorite entry went to ‘How software engineering changed: a tale of two eras’ by Neil Kakkar.
There were also six category winners who each won $2,500 in prizes, and in this article we’re happy to share excerpts from the winners and runners-up in three of those categories, also linking to 40 more articles. These essays by hands-on engineers and engineering leaders impressed us with their details of hard-earned experience, and are refreshingly honest and raw. Thanks to everyone who entered the competition and congratulations to the winners.
Today, we check out essays on three different areas:
- What happens when AI writes all the code? How engineering practices have dramatically changed at startups and mid-sized tech companies in the twelve months since Opus 4.5 was released. The winner is ‘An engineering manager’s crazy year’ by Anton Zaides.
- Stories from solo builders. How one-person businesses and side projects that turn “AI-native” are building more, faster, and with higher quality. The winning essay is ‘I’m a 100x engineer now!’ by David Veszelovszki.
- Reflections on AI. What does this change mean for us human engineers? Thoughtful reflections which conclude that while agents can (and do!) write the code, engineers need to understand it to stay in control of systems and shape them. The winning piece is ‘The new core skills: agentic engineering at Granola’ by Jacob Bartlett.
1. What happens when AI writes all the code?
At the end of 2025, many of us in tech saw AI’s coding capability dramatically improve with Opus 4.5 and GPT-5.2, and the models suddenly become good enough to reliably write most of the code – and soon, almost all of it. In January, I asked: when AI writes almost all the code, what happens to software engineering?
All the entries in this category covered the new challenges of AI generating the code, and how practices at many tech companies have adapted. Many writers compare a “before” and “after” with data on PR rates, revert rates, build times, and more.
Winner: ‘An engineering manager’s crazy year’
Edited excerpt from the essay by Anton Zaides author of manager.dev, Engineering Manager at HoneyBook:
“It’s June 2026; a nice, sunny day outside when I sit at my computer, looking at a 10k-line PR opened by my team’s great designer, and I want to die inside.
It’s not a mock or a prototype; it’s code he wants to merge into production. Not only is it full of hacky solutions (not even talking about criminal useEffect abuses), it also has dummy data where backend calls were supposed to be. How the hell did I get here? Let’s back up a bit.
I joined HoneyBook as an Engineering Manager in October 2025. It’s a 13-year-old startup (raised ~$500M), a management platform for business owners (think CRM+contracts+admin, etc.). I joined to lead an existing team of seven experienced engineers responsible for the financial products like managing business expenses, loans, etc.
This past year has been a crazy ride, going in just a few months from classic engineering to pure vibe coding, ending with the launch of a real zero-to-one initiative at an established company.
Code review collapse
We split our work into three repositories: the shared ai-workflows codebase, our own backend repo, and a thin frontend layer called atlas-vibe. Each had a different code review approach:
- In AI-workflows, every PR was thoroughly reviewed by at least two people including the engineer who wrote the code.
- In atlas-vibe, there were barely any PRs. We vibe code on the frontend, slowly improving the skills in our repo, and reducing the amount of substandard code a bit.
- In the backend repo, we had optional code reviews. That’s an interesting one.
Slowly, it became more and more tempting to just not ask for reviews. It’s addicting to just develop a feature and immediately have it in production. There’s no need to have an open end in your brain.
But still, at that stage I didn’t accept an ‘I don’t know, Claude wrote it’ approach. Even if you don’t request a review from someone, it’s still your responsibility to read and understand it. You can’t let Claude make the decisions and ‘drive’ the work.
Output rose like crazy:
It took me a while to understand that the code review stage contains a lot of peer pressure. When you submit your code to someone, you feel responsible for understanding it better, and nobody likes getting tons of PR comments (senior engineers, least of all). But when you know that nobody will review it, it’s much easier to cut corners in your own understanding too.
So, in the span of a couple of months, we dropped from two people reviewing and understanding the code, to zero!
The result was what you’d expect: a buggy codebase full of duplications and non-optimal patterns.
Hands-on engineering managers (without giving up on the people side)
From last October until March this year, I averaged one PR a week. Currently, it’s 20+. But more importantly, the nature of those PRs has changed: in March-June, it was mainly small things and side features, but since then I’ve taken on some more serious work myself, and it keeps increasing:
I know there’s a lot of hate for the demand to go back to being hands-on from EMs, and I really understand it: I believe that people need us more than ever, and EMs who code all day are usually much less effective managers.
In May, when we started to work on MyCo, I felt I just had to understand what our new flow looked like, and what we can improve. I believe it’s almost impossible to do this from the outside. For example, a debate with my engineer about our reduced quality in which I couldn’t participate properly without seeing the output myself, and I experienced both the advantages and limitations of the new flow.
As our careers change, I believe that to be a good EM there is absolutely no other way than to join the building activity.
I strongly believe that today, I have found a balance that works for me. I got rid of a lot of tedious work, and I feel as “present” as a manager as always, but now 10x more productive in my hands-on work. On Tuesdays and Thursdays I work from home and there are no meetings, and I’m able to release multiple big features a day. I was able to ramp up my parallel sessions to around 6-8, from 2-3 to fix some bugs along the way.”
Read the full essay by Anton, where he gets into how non-engineers started to ship production code, why the team ditched their home-grown agentic solution for Eve by Vercel, and what Anton thinks about the future of building with AI
Runner-ups
We really enjoyed these five runner-up essays in this category about the “before” and “after” of AI and how it has changed software engineering:
Software engineers are becoming “machinists” who need to build their own tools:
PostHog engineer Paul D’Ambra makes an interesting point in his essay:
“Software engineers are turning into AI Engineers? No, we are turning into software machinists. Replacing handmade software with (increasingly) cheap, plentiful, machine-made software. Unlike tailors who handcraft each item, machinists build tooling and inspect samples and then produce in large numbers.
Two predictions:
- continuous integration and review will change next
- we make tools for our workshop
Okay, things have changed less for folks working on systems with critical safety requirements, or high performance systems where it is easy to cause an incident. But the majority of us now have a different job. It is no longer sufficient to pore over every line of code, following the practices of bespoke tailored software engineers. Now, we are software machinists.”
Read the full essay for details on tooling PostHog built like their deep review agents, and further predictions on change coming to CI.
Learning how to enjoy working with AI
Kira Howe is a Staff Engineer at analytics company Seeq and has been in a situation many of us can relate to. In her own words:
“At some point earlier this year, I realized I was not enjoying work the way I used to. I will admit that I was one of those software people who was very unimpressed by ChatGPT in the early days, and I found the hype and excitement around LLMs really insufferable back then.
Once it became obvious that these tools were becoming essential to how I work and not going anywhere, I decided I had to either accept my AI-centric fate and learn how to use them well, or leave the industry. I’ve come to believe that being a software engineer but resisting the increasing spread of AI tooling and applications is futile, and a recipe for misery.”
Read the full essay – titled ‘Enjoying software engineering in the age of AI’ – for details on how Kira came around to feeling good about working with AI, and how practices at her company for CI, observability, and tooling changed.
Bootstrapped company becomes AI-native
Marc-André Moreau is CTO at Devolutions, a bootstrapped Canadian company of 250 people that builds remote desktop management and IT operations software. He writes:
“October 2025. Claude Sonnet 4.5 has just come out, and everyone at Devolutions is going through AI training from Mindstone. The message from the CEO is clear: we are taking all the necessary steps to make the company AI-native. Employees are offered a voluntary departure package if they don’t want to be a part of this new “Devolutions 2.0”. Those who stay need to be committed and go all-in on AI with the rest of us. Here is the story of the profound shift that happened at Devolutions, and how a major migration originally estimated at three years was completed in just one.”
Read the full essay for data-driven details of a complex application with 1,500 screens, the internal hackathon that ended up producing 60 useful skills, and how the company’s AI spending grew to $2M per year.
Sixteen things AI changed in 2026
Carlo Beschi is a Lead Agile Coach at Treatwell, which employs 700 staff, and he shared a long list of what’s changed because of AI at the company in his essay:
- Paying off tech debt: Doing a lot more migrations and upgrades, and breezing through them.
- Prototyping: everyone is prototyping – not with Figma, Lovable, or Google AI Studio, but with Claude Design
- The “80/20 rule:” This says that 80% of the work is easy to get done alone with AI, but people are needed for the final 20%.
- Roles are blurring: devs are working outside of their domains and PMs are writing more code
- Mourning the craft: many engineers are having a hard time accepting that AI is taking over what they love in their job: writing well-crafted code
Read the full essay, ‘The Earth is not flat’, for all 16 changes.
Writing code became cheaper, but everything else became harder
Bruno Felix, CTO at the fully remote, 8-person AI visibility startup XEO360 writes:
“The last year was one of the most intense periods of my career.
We’re in a transition where the main activity of a software engineer is shifting from rowing (focusing on one thing at a time and producing good code) to steering (managing multiple workstreams, context switching all day, and exercising sound judgment throughout).
That is mentally taxing, and at times at odds with the skills, and sometimes the identities, we’ve built over the years.”
Read the full essay for plenty of data on commit volume, CI time, and how practices changed.
Shout outs
Below are some other essays sent in by readers that get into detail about how things have changed.
- ‘Rebuilding our Deterministic Tax Engine for an AI Native World’ by David Nisenbaum, Founding Engineer at Sphere, on how the company did it with agents.
- ‘A year of contrasts: how software engineering is changing at Pulumi’ by Levi Blackstone, Principal Software Engineer at Pulumi. Case studies of shipping features in days that used to take months, and how build systems and engineering practices have changed.
- ‘Gradually, then suddenly: from “learn to code” to “coding is solved”… and back again’ by Marcell Dietl, Tech Lead & Software Architect at Frontmark, on why non-functional requirements remain ones that humans make, and how engineering practices and hiring practices have changed.
- ‘What a small team with old code can do with AI (and what it can’t, yet)’ by engineering manager Ygor Cardoso, including interesting details on the extra work created for devs when non-engineers start to contribute code.
- AI transformed the work at Homie by Abdul Osman, Founding Engineer at Homie on how they rewrote the backend three times in a year, the move from IDEs to terminals, and how developer practices changed.
- The return of a software engineer. Victor Zhang studied software engineering in 2006, then moved to work in finance. In 2024, he returned to software engineering at a 50-person company to freshen it up in Python, using ChatGPT. He writes that 2026 “changed everything.”
- 10x what? by Krzysztof Maliszewski, Software Engineer at Coralogix. This is an interesting survey of 40 engineers at Coralogix – where half admit they’re addicted to agents!
2. Essays by solo builders and tiny teams
We were impressed by some stories from readers about how far a single dev or a team of just 2–4 people can get these days, with agents helping them build software more ambitious than ever.
Winner: ‘I’m a 100x engineer now!’
Edited excerpt from David Veszelovszki’s essay, the creator of Cmdr: ‘a file manager from 2026, the spiritual successor of Total Commander,’ and former Sourcegraph software engineer
‘After 30+ years of coding the old-fashioned way, I’m extremely enthusiastic and about 100x faster with AI! It has changed my entire workflow, and my life. While I’m writing this, I’m painting the kids’ room. Claude helped select the paint and calculate the amount I needed. I made all the decisions, I own everything that happened, while Claude did the research and prepared the decisions for me. That’s also exactly how I work.
Today, while I’m painting, Claude is fixing bugs, developing features, and preparing a release. I’m even considering getting a day job because I could run my current project, Cmdr, for an hour a day, with agents carrying the rest. What a time to be alive!
Speed!
Lines of code is far from a perfect metric to describe complexity but it’s easy to measure and it kinda correlates with complexity? So I’ll use it here.
An older snapshot of Sourcegraph’s main repo is still available so I know that my average output on the days when I pushed code was 194 LoC/day between 2022–2025 when I worked there. That many sweaty, reviewed, production-ready code lines from my own little fingers—okay, with the help of GitHub Copilot. And these were my active workdays. So, my real average output was closer to 100 LoC per calendar day.
In contrast, I started Cmdr 10 months ago, and it’s 1.4M LoC now, +800k lines of translations, docs, etc. It’s 1.4M lines of actual code, most of it production and the rest tests. That’s more than 4,500 LoC/day added on average, including weekends. Last 30 days? 12,000. It’s speeding up. Discount 33% to compensate for the AI bloat. Still, what, 60x faster than when I only used Copilot? And 80–100x faster than without AI. Plus, I run other projects too, including Prvw, mtp-rs, smb2, and gitstrata.
But if you don’t like the LoC metric, that’s fair, so let me add:
- 1,674 changelog entries over 10 months, each delivering a piece of user value. Increased from ~40/month in Jan–Feb to 230–350/month by Aug–Oct.
- 12,003 commits (avg. ~55/workday, but increased from ~15/workday in Jan to ~160/workday in Oct, so about 10x!).
- 67 releases so far, 7–10 a month, so ~2/week.
That’s all pretty nuts, isn’t it?
A glimpse of how I work these days:
- Claude Code with Opus 5.5 medium in a terminal, a single 20x Max plan
- Few-liner prompts and no specs
- No skills
- Almost no rule files now
- No reading specs/plans. Manual QA at the end
- No code reviews
- Claude-maintained dev&prod infra
- Grasping 100% of the product level, 0% of the code level
Enter Opus 5.5: Fixing bugs by the dozen
On October 1, I gave Claude a dozen issues at once. It went like this:
- I told it pretty much: “Hey, I’m painting a room today. Could you find 10 smaller tickets to do on your own, with subagents, then merge and push it at the end, make CI happy.” Claude shipped it in a few hours and closed the tickets.
- Then I said: “Nice work! Please take 10 more.” It was delivered the same way.
- In the third round, it brought me 8–12 UI bugs as a single category. I made the initial decisions, and it knocked them off in a few hours. We then did a fourth round the same way.
- On 2026-10-01, I closed these 42 GitHub issues total.
Note: this was all bug fixing and feature development that didn’t directly touch humans. When issues included UI copywriting, Claude always brought the new strings back to me and I took five minutes to edit them before shipping.
Why I work so fast – and you probably can’t
I know that at a multi-person org, you as a single engineer won’t contribute 10k lines of code per workday in a project because you need to coordinate with other people. You need to be somewhat careful, loop in some people on what you’re doing, build common mental models of the system, and maybe even review code. My advantage as a solo eng is that I don’t have any of that overhead.
The dark side of AI-assisted coding is that it makes sleep relatively costly, and building at crazy speeds can be addictive for avid builders. Take care of yourself.
High-level work
Lately, I’m much more of a product person and company leader than a software engineer. When I tell people what I do, I still say “I code” out of habit, but do I really?
Well, I don’t. Claude codes, debugs, automates processes, translates. It does all the dirty work. And I put all that time into strategy, product decisions, marketing, customer service. Which means caring about the user and the product.
I aim to be an expert on the product itself. I know all the parts of the app, I know exactly what each part can do and why. Every button, every dialog. But I don’t know the code.
I built the S3 connect feature in two days while painting the room. 50k LoC, fully tested with seven providers. Displays transfer costs based on current list prices. How nice is that?
Overall, I’m extremely, extremely glad and thankful to be alive at this time and to be able to work with this tooling! It’s incredibly rewarding. It’s an unbelievably nice feeling that I can turn the “100x engineer” advantage into delivering quality apps with care and respect. It’s just hard to choose to sleep, too.”
Read the full essay by David, where he gets into how he uses automated checks and balances architecture work to keep the code in order.
Runner-ups
Below are two essays that we all found to be very engaging reads in this category:
Four-person company with no more handwritten PRs
The founder of Heartbeat, a platform for running paid online communities, recounted the AI-related change at his business which generates $1M+ in monthly paid bookings. Mayhul Arora writes:
“We spent a lot of this year upgrading our development environment and systems to the agentic era. But it’s unclear to me how much of that work is left to be done.
I think there’s a good chance that the future of our team looks like 2-3 people maintaining the core agentic factory and software platform, while everyone else builds customer-facing features on top of that foundation.
Maintaining the core agentic factory looks like optimizing core primitives such as data fetching patterns, CI, the design system, scheduled agents, dev environments, etc. This is the work that’s easiest to scale up with agents.
Building customer-facing features are the engineers that are able to live in planning mode and consistently translate loosely-specified features into concrete technical implementations. People that have the patience to iterate alongside agents, the taste to make the right tradeoffs and the wisdom to know when the existing architecture needs to adapt.”
Read the full essay for more on dev tooling, CI bottlenecks, and why the team spends more time in meetings.
One developer turns trad IT department AI-native
Joshua Warren has been a software developer since 1999, and joined paint manufacturer Blend Supply to modernize its development process, as the only human developer. He writes:
“Blend Supply is a third-generation family company that has been on the forefront of the aerospace industry since 1946. The easiest way to understand what Blend does - think custom-mixed paint for everything from private jets to 737s and boats.
Blend previously relied on agencies to build and support their website, and I believe that agentic software development is going to disrupt development agencies.
Blend Supply’s leadership has given me a blank slate, the rare opportunity to build from the ground up whatever I feel is necessary to help Blend out-develop their competition [with AI-native approaches and workflows].”
Read the full essay for fascinating details on how Joshua built a software factory inside of a ‘traditional’ company on top of the Oh My Pi harness, agents attending weekly status meetings with sales and customer support people, and deploying 50+ times per day versus once a month.
Joshua’s essay is a reminder that massive disruption is happening in “traditional” industries where IT has long been a cost center. This story also suggests that development agencies might be in trouble: Blend Supply replaced several agencies with a single engineer to build out their software factory!
Shout outs
Below are some more entries from readers that we found interesting or inspiring in some way:
- ‘Sure-why-not-driven-development’ by Marius Maaland, CEO of three-person AI startup Drippa. Founded in January this year, the code has always been fully AI-generated.
- ‘Building Bencher in 2026: open source, bootstrapped, and agent-pilled.’ Staff software engineer Everett Pompeii builds Bencher, an open source continuous benchmarking platform on nights and weekends.
- I don’t miss coding. I missed building. Leslie Nguyen was formerly an engineering manager at Block, Uber, and Pinterest, and launched personal finance app Stridefly on her own. She documents the number of commits, tests, and lessons she’s learned along the way.
More shoutouts:
- ‘I am the bottleneck. We are’ – by Bogdan Deaky, founder of Bluemind Software. Bogdan runs his business with a single employee while teaching at a university. He argues that requirements gathering and verifying software output are the limiting factors in what one person can build.
- ‘Two years of change: how AI reshaped software engineering at a small company.’ Michal Gutowski is the solo developer at smAily, a bootstrapped remote company building an app to record in-person meetings. LLMs write all the code there.
- ‘Great product engineering in the AI era.’ Anirudh Ravichandra is cofounder of GP-LP Match, a real estate matchmaker. It’s a bootstrapped company of five people with two engineers. He writes about the importance of choosing the right tools.
- ‘Building an in-browser massively multiplayer (MMO) trading card game (TCG): and doing it all alone’ by Elijah Lee, creator of BattlerLegacyTCG. Elijah quit his job to build this game late last year. He used Elixir on the backend – despite never using it before AI – and in this essay, he goes through the tech stack, agent workflow. He’s honest on how hard it is to build a full-fledged game.
- ‘Engineering with concept art.’ Caer Mistral Sanders, founder of content studio With Caer, explains how she builds software as a solo founder, including Wrot, a writing tool he used to publish her essay. It’s a curious approach of creating lots of custom approaches and even data formats like Codas (similar to Markdown).
- ‘How I vibe coded a best-in-class communication app for my nonverbal child.’ This is a sweet story by Product Owner and father Andrew Peterson who built a communication app for his son after finding that commercial devices cost $1,700+ and are made for adults. Inspiring!
3. Reflections on AI
What does it mean that AI now writes most – if not all – the code? The essays below tackle this question not with data, but on the basis of how authors feel about this change.
Winner: ‘The new core skills: agentic engineering at Granola’
In his essay, Jacob Bartlett documents how each new major model release has altered his daily workflow – and things changed monthly!
- December 2025: GPT-5.2 and Opus 4.5
- January 2026: No major releases
- February 2026: GPT-5.3 and Opus 4.6
- March 2026: GPT-5.4
- April 2026: GPT-5.5 and Opus 4.7
- May 2026: Opus 4.8
- June 2026: Fable 5 (unleashed)
- July 2026: GPT-5.6 Sol, Opus 5, and Fable 5 (nerfed)
- August 2026: no major releases
- September 2026: GPT-6 Astra, Fable 5.1, and Opus 5.5
- October 2026: no major releases
This excerpt from Jacob’s essay details what happened in February:
“Typically, I’ve gotten into minor trouble at work for attempting to have my cake and eat it; trying to make a name for myself via 20% projects, but stacking it inclusively rather than on top of my regular hours. It’s the same line that I’ve heard throughout my education and career: focus and stop getting distracted.
But that was in the beforetimes.
The Granola iOS app began life as a side project by Jonathan, one of our fullstack engineers, to find out if meetings-on-the-go had legs. It did! Tom, our mobile lead, was hired to take it to production. Like all good startups, Granola optimised for speed-of-validation to get it into the hands of customers ASAP. This got the quick validation that was needed, but left a slightly rushed architecture in its wake.
The 11-month-old iOS codebase was simple enough that I could quickly stretch it across my cranial context window, and ripe for big architectural improvements. In short, this was my perfect playground: an Eden of low-hanging fruit which I was neurologically wired to pluck.
Could I resist this temptation? No. Did that get me in lots of trouble at Granola? Also, no.
Now I had access to pretty-good agents, and an environment with a relaxed attitude to token expenditure. I’d just learned to parallelise my work across multiple git checkouts, and I’d been honing my ability to define iOS verification steps. Tom and I, importantly, were in total agreement on the architectural destination we wanted to get to. I flexed my multi-agentic chops, indulging my best and worst impulses. And I was getting praised for it!
I dropped a just-one-more-thing slide in the all-hands and introduced the Meeting Bar™, a UI element that lets users dismiss meetings, and navigate through the app, without stopping their current transcription. Our product manager lamented about being trapped on the meeting screen, and I offered both a shoulder to cry on and a solution: an agentic skunkworks that toiled away in a secondary terminal tab alongside my standard day job, while I bounced a few early iterations off our designer. The Meeting Bar was delivered in 20% time.
Over time, I’ve become proficient at designing verification steps; planning work alongside my agents; and context switching. Now I can run multiple meaningful projects in parallel. Separate to product-market fit, this felt more like neurodivergence-company-technology fit.”
Check out the full essay for a more detailed breakdown of how each model release has impacted Jacob’s workflow. He concludes:
“While software engineering has been revolutionised, this doesn’t make engineering skills less valuable.”
Runner-ups
Here are four essays we particularly liked for the reflections they contain.
How AI changes software engineering
Daniel Silva is a Staff Software Engineer at fintech startup Coverflex. His grounded essay reflects on the massive change he saw and took part in over the last year, concluding:
“It seems that AI is really here to stay. It has transformed engineering for the foreseeable future. There are clearly eras before and after AI got good enough, where it now permeates every aspect of the development process.
I don’t think software engineering is doomed. I still think AI is a tool that requires human taste and ingenuity to make it work. We will most likely need more software engineers because more software is getting created than ever. Infinite problems in the world are waiting to be solved.
Engineers need to keep up with the times and be open to new ways of working with tools very different from the past. This has happened before: more powerful IDEs were created, high-level languages were created, and magnetic tapes replaced punched cards… We can do this again, for sure.”
Read the full essay for more thoughts about the importance of “putting in the reps” into AI usage, why Daniel sees hope for junior engineers, why he does not use AI to write down ideas, and more.
Nothing has changed about what it means to be a software engineer
Ben Cohen is a Software Engineer at Substack. But he never felt “home” in software engineering circles. Ben writes:
“My name is Ben Cohen. I am a software engineer at Substack, the company whose software powers the blog you are reading this (hopefully prize-winning) essay on. I use the phrase “am a software engineer” quite intentionally, because software engineering has always been much more of an identity than a job for me. (...)
Despite all of the above, I’ve never felt at home in many software engineering circles. You see, here’s my confession: I don’t really care about code. I’m a little convinced that the people who talk about “beautiful” code are lying, in the way that I also don’t really believe that the wine snobs are tasting dried apricot notes in their rieslings. I don’t have a favorite programming language and my favorite code editor is the one that’s already open.”
He closes with a feeling that not much has changed:
“Everything is, of course, different now. Different in the way that it was different when we stopped using punch cards, invented the compiler, started building websites, and switched to cloud infrastructure.
But also, nothing has changed about what it means to be a software engineer. Large language models have forced us, for the first time, to answer the question: “Is it still software engineering if you don’t write the code?” To that, my answer is an emphatic yes.”
Read the full essay for Ben’s full thoughts on how he sees this change, and why the story about a famous engineer charging $10,000 to know where to hit a machine with the hammer could be true for us software engineers.
A new grad software engineer’s impressions
Max Oliinyk is a 22-year-old Platform Engineer at F-Secure who spent 18 months at Hive Helsinki: a full-time, on-campus program where students learn by building software products in teams with no teachers. After a four-month internship at cybersecurity company F-Secure, he got hired fulltime. Max writes about his current working setup:
“Right now, I manage Jira, code writing, PR creation, documentation and research all through Claude. The only place where I will probably always prefer to do things on my own is communication. No one will get offended by code written by AI, especially if it follows all the standards established in the team and has the right ideas behind it. Getting a lengthy blob of text in response to your message or review comment is considered not nice, even beyond the industry. It is fine if the message is something functional; it is not if you wanted to hear something humane back.
So, my current stack is Claude Code, with a subscription provided by the company that gives access to all recent models. I add skills on top of it, including ones with team-specific context that help agents follow our conventions. I am genuinely not able to burn through the limits; I occasionally run out of the 5h limit a bit too early if I use too much thinking effort, a too-expensive model, or launch a dynamic workflow.”
Read his full essay for more observations on what it’s like in the industry at this time for an early-career engineer.
Hope for early-career software engineers
Fawziyah A is a software engineer with five years of experience, working at fintech Imprint. She tackles the important topic of what AI means for junior engineers. In her words:
“Despite worries that AI is de-skilling early career engineers, being empowered to work on so many more projects, and with so much more variety, has taught me way more about my company’s business problems, priorities, and systems design.
Less experienced engineers who charge at those challenges head on have the opportunity to learn faster than was possible a year ago. That is what makes me so excited to be working at a place like Imprint and working in this industry now.”
Read her full essay for more reflections on less interaction among devs, how domain experience is readily available with AI, and how the technology can be useful for learning faster.
Shout outs
- How software engineering at Hinge has changed. Jacob Voytko, Staff Backend Engineer at Hinge on how prototyping, on-call incident response, internal tooling, and design, coding and review changed with AI agents.
- What AI mustn’t take from us, Jachym Dvorak, Machine Learning Engineer at Productboard on which parts of engineering practice should be protected as AI changes the work.
- Software engineering in the LLM funhouse. Robert Lopez, Software Engineer writes about how AI changed development at Quizlet and Stellic. He argues that teams should return to first principles and do things like plan together, say no to scope creep, and measure more.
- How checking the math I didn’t write is going. Data engineer Sia Seko reflects on how data engineering has changed, and how her team changed habits while adapting AI.
- Back to coding after AI. Vitor Louzada, currently Head of Data Science at Grover returned to coding after a decade of being a manager.
- In a world of clankers, be a connoisseur. Duncan MacQuarrie, Senior Software Engineer at Infracost reflects on the tension between AI adoption and the growing cost of AI.
- The times they are a-changin’: software engineering in the age of agents. Software engineer Emma Gaubert argues that the value of a software engineer was never limited to writing code. She makes the point that engineers should broaden into product, design and soft skills.
- On the impact of artificial intelligence on my job and engineering identity. Jakub Niemiec, Senior Mobile Engineer and Creator of Beanie (a coffee companion app) works with Flutter and shares the downsides of AI: draining code reviews, fewer junior engineers, and the end of language-specific expertise. He closes with a hope that exciting times are to come.
- 5 new types of failures in AI-native development. Carly Rector, software engineer and founder shares her experience leading 8 AI-native projects in the last two years.
- Building a ladder of love (and trust). Maanas Sathaye, Systems engineer at Sightly, on how he and the team start to trust agents to do larger and larger pieces of work.
- Outsource the Work, Not the Thinking. Sara Spagnoletto, Software Engineer at Google, working on Waze, gives an interesting peek of adopting AI in her day-to-day work, and how she opened 3x as many PRs after starting to use Antigravity more.
- The work is changing. Christina Martinez, DX engineer at Resend on how non-engineers can ship code, experimentation becoming more frequent, and how work feels like it’s getting out of balance.
- Claude, the new kid in town. Dave Kiss, Staff Community Engineer at Mux, on how Claude changed engineering at the company.
Takeaways
In this issue, we went through the experience of 40 tech professionals – working from small companies to large companies; from building side projects to production software used by massive numbers of customers. Despite the variety the stories stayed pretty much the same: everyone recalled the massive change in pace with Opus 4.5 or 4.6, and how they’ve faced new problems to solve with the amount of code generated, with non-engineers coding, and so on.
When reflecting on this large change hitting our industry, many of the engineers were positive in how engineering basics remain important in building systems, and deciding what to build.
It’s worth noting that we had a “no AI” writing rule for this competition. Even though we delegate more of our coding to AI – when the target of that output is a machine interpreting it –, we still value the human voice when writing to fellow humans.
Thanks again to everyone who contributed an essay, and congratulations to the grand prize and category winners.
In part two of this mini-series, we’ll present the other half category-winning essays, and additional essays worth reading.
