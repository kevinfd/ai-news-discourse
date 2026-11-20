---
id: "4b5d8bade0536cca"
title: "Voice AI Benchmarks Are Not Scoreboards"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/20/voice-ai-benchmarks-are-not-scoreboards"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/20/voice-ai-benchmarks-are-not-scoreboards"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-20T12:00:00Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Sidhant Kabra, Forbes Councils Member"]
language: "en"
summary: "Treat every voice AI benchmark as an experiment, and read it for the gap, not the number."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 1001
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/63dd0eccf313d2f53b4ba740/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Voice AI Benchmarks Are Not Scoreboards

Forbes · Sidhant Kabra, Forbes Councils Member · 2026-11-20

Sidhant Kabra is a Co-Founder of Cekura, a company that is pioneering Voice AI evals and benchmarks.
Every few days, a new voice AI model ships with a chart that puts it on top: fastest reply, lowest error rate, most human.
As the co-founder of Cekura, a company that tests voice agents and publishes voice AI benchmarks, my advice is to use the rank to build a shortlist, not to make the decision. Picking the top three to five is a good starting point. Past that, in my view, the ranking is about 2% of a benchmark’s value. The other 98% is the specific finding: where an agent breaks, compared with whom and under what conditions.
Benchmarks are experiments. Change the line quality, the caller’s accent, the workflow or how slowly a tool responds, and the order changes. Absolute numbers don’t transfer to your business. Specific gaps do.
Why A Benchmark Is An Experiment
Start by holding the agent constant. In one public experiment, we deployed the same Medicare insurance agent on six voice platforms and ran 23 scenarios three times on each. Workflow scores ranged from 65.2% to 95.7%. Same prompt, same tools, same workflow.
Now change what you count. One platform passed 69.6% of scenarios when we scored only whether the agent took the right actions. Once we also counted infrastructure failures, such as long silences during tool calls that left callers unable to finish, it passed 8.7%. Neither number is wrong. They answer different questions.
Swap the language model and the story flips again. With everything else held fixed, an open-source model beat an established proprietary one on reliability (88.1% vs. 76.3%) and replied a second faster at the median. But the proprietary model won red-team safety, 100% vs. 80%. Which is “better” depends on whether your agent books haircuts or moves money.
Where Agents Lag: Against Each Other And Against Humans
Composite scores hide the split. We ran 70 scripted calls through each of four production voice agents in healthcare and financial services. One led its peers on 7 of 13 behaviors: It kept talking through a caller’s “mm-hm” 89% of the time, versus 31% to 40% for the others.
The same agent was the slowest to stop when a caller genuinely talked over it (71% vs. 92% to 97%), and it read a value back before using it only about half the time. On the recordings: A child’s shriek masked one digit of a card number, and the agent guessed instead of asking, then sent the wrong digits to the bank’s system. A caller said her mother had died three weeks earlier, and the agent went straight to the hold without empathy.
None of that shows up in a single score. All of it decides whether a caller trusts the agent.
Humans are the other baseline. We recorded experienced support agents handling 70 calls with real callers, then played the same caller lines to seven speech-to-speech models. Human agents answered in about 11 words; the models used 20 to 60. Human agents slowed down for numbers, dates and times in 16% of those stretches, and no model did so even half as often. When a cough covered one digit of a number, no model asked for it again in more than a third of calls.
No model was human-like across the board. What separated them was which human cue each one missed. Two models were rated more human-sounding than the human agents, yet still read numbers at full speed. Another sounded written rather than spoken in 75% of its replies.
The Truest Benchmark: Built On What You Care About
Public leaderboards are a starting point. The truest benchmark is built on the parameters you care about: the test conditions your callers face, the workflows your agent runs and the metrics your business tracks. If you have real-world examples, such as recordings of calls that went wrong, build from those first. Two things make that possible.
The first is structured test cases. Each scenario has a defined caller, a goal and an explicit expected outcome, rather than an LLM judge reading a transcript and guessing. Voice agents don’t behave the same way twice, so a scenario counts as passed only if it passes three runs in a row.
The second is simulating the real world, not just calling an endpoint: interrupting at exact timestamps, playing background speech and hold music, dropping packets, switching languages mid-call and making tools respond slowly.
We split that work into three tracks, because each one fails differently:
• Workflow: Does the agent take the right action with the right data, and confirm it before acting?
• Infrastructure: Does the call survive latency, noise, line dropouts and slow tools without dead air?
• Red Teaming: Does the agent hold up under multi-turn pressure, where an attacker builds trust over several turns before trying a jailbreak? One-shot attacks miss most of the risk.
A finding is only worth something if you can reproduce it, fix it and rerun the same scenario to prove the fix held.
How To Read Any Voice AI Benchmark
Before you trust a chart, ask five questions:
1. What was held fixed? If the prompt, model or voice changed between rows, you’re comparing configurations, not platforms.
2. What was counted? Look for task accuracy and end-to-end completion side by side.
3. Do the conditions match your callers? Noise, accents, holds and language switching all move rankings.
4. How many runs? One pass on a system that behaves differently every time is an anecdote.
5. Can you hear the failures? A recording of the exact moment an agent broke beats any composite score.
Why You Should Stop Chasing The Rank
This month’s leader can trail next month. The insight is what lasts: This agent guesses digits under noise; that one talks over a grieving caller. That tells you what to fix before your customers find it.
Treat every benchmark as an experiment, and read it for the gap, not the number.
