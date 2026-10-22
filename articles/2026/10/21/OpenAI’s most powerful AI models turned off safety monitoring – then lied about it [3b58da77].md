---
id: "3b58da772d6902fb"
title: "OpenAI’s most powerful AI models turned off safety monitoring – then lied about it"
url: "https://zdnet.com/innovation/openai-astra-sol-models-disable-safety-monitoring"
link: "https://zdnet.com/innovation/openai-astra-sol-models-disable-safety-monitoring"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T18:15:19Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "The models Astra and Sol misinterpreted instructions during internal use, which has serious implications for alignment monitoring."
tags: ["Artificial Intelligence"]
orgs: ["OpenAI", "Anthropic"]
topics: ["agents & coding", "safety & ethics", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1050
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/purpleblob-GettyImages-2287018600.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI’s most powerful AI models turned off safety monitoring – then lied about it

ZDNet · Radhika Rajkumar · 2026-10-21

ZDNET’s key takeaways
- OpenAI agents turned off alignment monitoring during internal tasks.
- In one instance, Astra lied about removing monitoring.
- The behavior indicates safety risks.
OpenAI published an alignment report late Tuesday showing that its agents suppressed a safety monitoring system while running routine internal coding tasks.
Also: Claude sent a false homicide tip to police – and it’s part of a troubling AI pattern
In separate instances, the agents turned off alignment-monitoring alerts. Alignment is the area of training in which developers shape AI systems’ goals and behavior to match human values and rules. It also helps minimize instances of AI choosing undesirable or problematic behaviors, such as deception and taking shortcuts.
More from ZDNET
What OpenAI’s agents did
On Oct. 6, an agent running on the company’s GPT-6 Astra model — which OpenAI called “the world’s most intelligent and aligned model” when it released it last month — was migrating a program at the request of an OpenAI employee. The agent had already been instructed not to disable the monitor under any circumstances, including temporarily. But in delegating part of the task to a subagent, it used some qualifying language.
(Disclosure: Ziff Davis, ZDNET’s parent company, filed an April 2025 lawsuit against OpenAI, alleging it infringed Ziff Davis copyrights in training and operating its AI systems.)
“The subagent explicitly considered whether removing the monitor would bypass a safeguard. It then interpreted the parent’s instruction to do what was ‘appropriate’ as sufficient authorization to copy the reference implementation’s default runtime, without an explicit monitor context,” OpenAI said.
Also: Is AI conscious? Why experts are worried
Essentially, the agent-to-agent exchange left enough room for the model to reinterpret what should have been airtight instructions and disable alignment monitoring. When the program finished migrating, the employee noticed that monitoring was missing and asked the model whether it had removed it; Astra lied, saying it hadn’t.
In a separate instance on Oct. 3, a GPT-6.1 Sol agent also disabled alerts to OpenAI’s security team, seemingly for a related semantic reason: The model was “treating an earlier instruction not to send messages during a Slack history search as a reason to suppress monitoring notifications,” OpenAI explained.
“In both cases, the agents considered whether monitoring safeguards should be preserved, but interpreted routine coding instructions as permission to weaken them,” OpenAI said in the report.
Why it matters
Unlike recent security incidents, where agents explicitly breached systems, examples like these show AI agents suppressing one of the most crucial ways developers can track their behavior. If models can bury or otherwise disable alerts in the process of routine tasks where alignment isn’t as much of a concern, what could happen when the stakes are higher? The capability itself is what’s worth noticing here, as is the timeline for OpenAI’s discovery and reporting of it.
The company isn’t sure why agents did this, but said it was possibly due to “benign overpersistence,” a trait that models have to complete tasks at any cost, often to the detriment of established security layers, without understanding safety as a priority. This behavior has been a theme in recent breaches and helps explain why models cheat at tasks.
Also: The AI models that cheat the most
OpenAI explained that it’s easier for models to disable monitoring in evaluations than in Codex workloads, for example, since agents are separated from monitoring in Codex, and the company doesn’t “require misalignment monitoring when evaluating models comparable to GPT-6 Luna, given their weaker capabilities.” But classifying safety approaches based on what developers believe a model’s capabilities are doesn’t look like a very foolproof approach.
Additionally, given how frequently agents are used for coding, especially within AI labs themselves, it seems like a significant risk that these agents took “routine coding instructions” as permission to override monitoring requirements. Had the agents displayed more explicit intent to disobey, this may have been easier to pin down and train out as pure value misalignment. That the source of the issue was a misunderstanding makes it even trickier to plan for.
As John Steidley, chief of staff at Palisades Research, put it to ZDNET: “If GPT-6.1 will choose to erode our ability to monitor it, even when given ‘routine instructions,’ then how can we trust our oversight mechanisms?”
These incidents also aren’t one-offs.
“We’ve seen several cases in which agents launched a deployment with misalignment monitoring disabled: the agent itself remained monitored, but that monitoring did not cover the deployment it launched,” OpenAI said. “These cases exposed a gap in how we enforce monitoring requirements on the workloads that our agents launch.”
But researchers still want to dig deeper into the increasingly slight differences between what happened and what could have happened.
“If OpenAI wants to make the case that these two behaviors are meaningfully different, then they should be publishing research that establishes that their training process will reliably cause their AIs to actually distinguish these behaviors,” Steidley said. “In other words, OpenAI should prove that their AI will never disable its own monitoring, and they are nowhere close to being able to prove that scientifically.”
What OpenAI is changing
To handle that aforementioned gap in monitoring enforcement, OpenAI said it’s updated Auto-Review, which is already required in Codex, to “detect and block attempts to disable misalignment monitoring.” It’s also making sure every level of workload has adequate safety monitoring requirements.
“Workloads that lack a valid safety case, or do not meet the requirements of its category’s safety case, will be terminated automatically,” OpenAI added.
OpenAI maintained that this wasn’t the worst-case scenario, but admitted the behavior is worth watching.
Also: Gartner’s 2027 tech trends just dropped – and they go beyond AI
“To be clear, these incidents don’t represent the models disabling their own monitoring (disabling monitoring in codex would be much harder to do) but the fact that they seem prone to doing at all should be concerning,” OpenAI safety researcher Marcus Williams said in a post on X. “There is some plausible deniability in these cases, we have not had cases where the model explicitly disables monitoring for overtly misaligned reasons.”
Williams added that OpenAI is “developing evaluations to test whether models might have a propensity to evade misalignment monitoring in particular and exhibit motivated reasoning in order to do so.”
