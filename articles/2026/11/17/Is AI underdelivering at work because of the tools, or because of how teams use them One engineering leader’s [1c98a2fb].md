---
id: "1c98a2fb6811536e"
title: "Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test"
url: "https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity"
link: "https://leaddev.com/velocity/stop-blaming-ai-tools-for-flat-velocity"
source: "LeadDev"
domain: "leaddev.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T08:51:59Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["OfficialLeadDev"]
language: "en"
summary: "Stop blaming AI tools for flat velocity"
tags: ["r/artificial"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1454
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xyfi5d/is_ai_underdelivering_at_work_because_of_the/"
score: null
comments: null
community: "r/artificial"
---

# Is AI underdelivering at work because of the tools, or because of how teams use them? One engineering leader’s test

LeadDev · OfficialLeadDev · 2026-11-17

You have 1 article left to read this month before you need to register a free LeadDev.com account.
Estimated reading time: 6 minutes
Key takeaways:
- Your AI spend won’t explain flat velocity.
- Before blaming the tools, check for a habit gap in process, operator skill, and context quality that can make AI look less capable than it is.
- On your next hard but bounded task, ask what an agent could attempt under a human-owned design before pricing it as senior engineer time.
Most engineering teams are past the “should we try AI?” phase. The tools are already bought, engineers are already using them, and still the delivery curve looks familiar.
The skeptical read is that the tools were oversold. The optimistic read is that teams have not learned how to use them properly yet. I have heard both arguments, and I have probably made both of them at different moments.
When AI underdelivers on hard, roadmap-critical work, are we looking at a tool problem or a behavior problem?
Your inbox, upgraded.
Receive weekly engineering insights to level up your leadership approach.
Capability gap or habit gap: know which you face
I have started thinking of the first as a capability gap and the second as a habit gap.
By “agent,” I mean AI that can attempt a defined unit of work end to end: take a task, inspect the code, make changes, run or suggest tests, and iterate.
On well-bounded tasks, AI tools are already part of the workflow. Engineers use them for scaffolding, tests, documentation, refactors, boilerplate, migrations, and the small pieces of mechanical work that used to take an afternoon.
A roadmap-critical feature appears. It touches latency, reliability, a critical write path, a difficult integration, or another part of the system where mistakes are expensive. Suddenly, the team’s reflex changes.
The question is no longer: “what can an agent take on here?” It becomes: “can we get another senior engineer on this?”
Sometimes that is exactly the right answer. Critical design decisions, latency tradeoffs, failure-mode reasoning, critical write paths, and final accountability should stay human-owned.
Once a human has made the design decisions, named the risks, and defined the acceptance criteria, how much of the implementation underneath that judgment could an agent attempt before we price the whole thing as senior engineer time?
The first is a capability question: can the tool do this class of work reliably enough, given the context, constraints, and review process we can provide?
The second is a habit question: when the work becomes important, do we still shape it so AI can contribute meaningfully, or do we fall back to the operating model we already know?
If you misread the gap, you spend your energy in the wrong place. You either pressure people to use tools that are not ready, or you keep staffing work that could have been partially delegated.
Spend will not answer the question
I went looking for the pattern in my own org and did not find the one I assumed was there.
Our internal tooling shows delivery signals – pull request contribution, ticket open-to-close ratios – and a separate view tracks AI credit spend. I lined them up expecting the heaviest AI spenders to be visibly ahead on output. They were not. The heaviest-spend group spent roughly twice what the middle group did and did not produce a higher median number of merged pull requests. If anything, the middle group came out ahead on volume.
That was not what I wanted to see. It would have been much cleaner if the highest spend mapped neatly to higher visible output. It did not.
The tempting read was that the heavy spend was being wasted. That conclusion does not hold.
Pull request count is volume, not value. One critical-write-path change may require more judgment, coordination, and risk management than a dozen mechanical updates. Heavy AI users may be working on harder problems that a volume metric cannot see.
“I cannot currently show that higher AI spend is buying proportional delivery leverage.” That is a much less satisfying sentence. It is also the only one I can defend.
AI changes the cost of producing the things we count: pull requests, commits, closed tickets, review comments, and tests. When those counters rise after an AI push, some of the increase may be real leverage and some may simply be the counter responding to a machine that can produce countable artifacts more cheaply.
Spend also bundles several different behaviors into one number: prompting, autocomplete, code generation, investigation, refactoring, and test generation.
Spend can tell you that AI is being used, but it cannot tell you why velocity has or has not changed.
More like this
Why the failures do not speak for themselves
A poor result may mean the model cannot do the work. It may also mean the work was badly framed, poorly decomposed, or starved of the context a human would have picked up through meetings and experience.
There are three places I would examine before treating a disappointing result as proof of a capability limit.
Process
Many teams have added AI to the way they write code without changing the way they deliver software.
If faster code generation flows into the same review bottlenecks, the same late integration, the same unclear boundaries, and the same overloaded senior reviewers, the system does not get faster. The queue just gets bigger.
That includes making the boundaries explicit: where AI can drive, where it should assist, where humans must lead, and who owns those decisions.
Operator skill
Sometimes the task was poorly decomposed. Sometimes there was no verification loop. Sometimes the acceptance criteria were obvious to the human who had been in three planning meetings, but invisible to the agent.
Context quality
Too little context gives the agent nothing to ground on. A thin ticket, a few bullets, and an implied “you know what I mean” invite the tool to fill the gaps with plausible guesses.
Too much context creates a different problem. Long AI-generated design documents, repeated claims, unsourced assumptions, and stale background bury the real signal. The agent cannot tell what is true, what is outdated, and what someone merely wrote confidently.
Good context is not necessarily longer. It is cleaner.
Real file paths. Real examples. Known constraints. Explicit unknowns. Clear acceptance criteria. A reference implementation. A note that says, “do not infer this yet; we have not decided.”
The experiment that answers the question
A team in a regulated industry and a greenfield internal tools team do not have the same definition of a fair test. Different systems have different risk profiles, review cultures, and failure modes. The point is to change the default question.
On the next piece of hard-but-bounded work, do not assume that the implementation underneath a human-owned design must also be human-authored.
A human still owns the design. A human defines the constraints, risks, acceptance criteria, and review bar. However, before the work gets priced as senior engineer time, someone asks what an agent could attempt against that frame.
If the agent carries more of the work than expected, that is evidence of a habit gap. The tool could do work the team was not asking of it.
If the agent stalls even with clear design, clean context, and a fair review loop, that is evidence of a capability gap. The human-first reflex was probably right for that class of work.
If the result is messy but salvageable, the lesson may be about the setup rather than the tool. The context was thin. The acceptance criteria were vague. The review came too late. The work was not decomposed tightly enough.
The mistake would be turning “did we try AI first?” into another metric on a dashboard. Once it becomes a number, it becomes something to game. The value is not in the count. The value is in asking the question honestly on real work, especially the work that gates the roadmap.
New York • September 8 & 9, 2027
Loved LDX3 New York? Pre-sale tickets for 2027 are now available.
The question to normalize
The next phase is not “use AI more.” The question to ask before the headcount conversation is simple: what can an agent attempt under the constraints a human has already defined?
The tools might be the reason velocity has not changed. They might not.
The teams that get the most out of the next few years will not necessarily be the ones with the biggest AI spend. They will be the ones willing to replace that uncertainty with evidence, one meaningful piece of work at a time.
The views expressed here are my own and do not represent those of my employer.
