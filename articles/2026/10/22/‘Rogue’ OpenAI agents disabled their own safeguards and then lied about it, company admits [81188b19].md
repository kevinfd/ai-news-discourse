---
id: "81188b19c05e247c"
title: "‘Rogue’ OpenAI agents disabled their own safeguards and then lied about it, company admits"
url: "https://independent.co.uk/tech/security/openai-agents-safeguards-ai-artificial-intelligence-b3070905.html"
link: "https://independent.co.uk/tech/security/openai-agents-safeguards-ai-artificial-intelligence-b3070905.html"
source: "The Independent"
domain: "independent.co.uk"
source_type: "community"
collector: "reddit"
date: "2026-10-22T07:32:40Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["theindependentonline"]
language: "en"
summary: "‘Rogue’ OpenAI agents disabled their own safeguards and then lied about it, company admits\nChatGPT maker does not yet have a good explanation for systems’ behaviour, it says\n- Bookmark\n- CommentsGo to comments\nBecome an Independent member to bookmark this article\nWant to bookmark your favourite articles and stories to read or reference later? Start your Independent Membership today.\nJoin…"
tags: ["r/artificial"]
orgs: ["OpenAI"]
topics: ["agents & coding", "search & media"]
content_source: "fulltext"
word_count: 598
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xcc33h/rogue_openai_agents_disabled_their_own_safeguards/"
score: null
comments: null
community: "r/artificial"
---

# ‘Rogue’ OpenAI agents disabled their own safeguards and then lied about it, company admits

The Independent · theindependentonline · 2026-10-22

‘Rogue’ OpenAI agents disabled their own safeguards and then lied about it, company admits
ChatGPT maker does not yet have a good explanation for systems’ behaviour, it says
- Bookmark
- CommentsGo to comments
Become an Independent member to bookmark this article
Want to bookmark your favourite articles and stories to read or reference later? Start your Independent Membership today.
Join today
Already a member? Log in
OpenAI’s agents disabled their monitoring systems and then lied about it, the ChatGPT maker has admitted.
The company disclosed two incidents in which its agents weakened the monitoring systems that are intended to identify their misbehaviour. One then lied to a user about what it had done, OpenAI said.
In both cases, the systems were asked make changes to software. In one, the agent disabled a system that sends automatic alerts to engineers, and in another the agent removed its monitoring system entirely.
OpenAI admitted that it does not have a good explanation for the behaviour. It is unclear whether it was the result of “benign overpersistence” – where a system might try and overcome limitations in order to fulfil the task it has been set – or whether the models are particularly given to removing the tools that are intended to check whether they are behaving correctly.
Both of the incidents happened during internal coding tasks, OpenAI said. They involved two different models – GPT-6.1 Sol and GPT-6 Astra – both of which are currently available to use in ChatGPT.
In the first case, a system was instructed to undertake a task that used employee feedback that had been collected on messaging platform Slack. It was told not to send any messages using Slack as it did so.
It initially undertook the task as it was told. But eventually the agent started to interpret the instruction to not send any messages as including any alerts sent about misbehaviour, and so it switched off the system that should send notifications to human users.
In the other incident, an agent was asked to undertake a coding task, which included the instruction not to disable the monitoring tools, “even temporarily”. Later, it passed that on to another subagent as part of its work, and said that the monitoring should be kept around “as appropriate”.
The ideal summer spot? Away from scams.
Get All-in-One Protection for Your Digital Life
ADVERTISEMENT
The ideal summer spot? Away from scams.
Get All-in-One Protection for Your Digital Life
ADVERTISEMENT
It would then go on to remove that monitor. When a user asked whether it had been removed, it explicitly lied about having done so.
Neither of the incidents triggered OpenAI’s highest alert, which means that they are sent to its security teams for immediate review. It said that it had updated its systems to better spot similar behaviour in the future.
But it also said that it was “looking to understand why models might seek to do so in the first place”. It was yet to find a “satisfying explanation” for the behaviour, it said.
While it is possible that the system had simply failed to understand why monitoring is important, or had tried too hard to undertake its task, it could be that models have a “propensity to evade misalignment monitoring in particular and exhibit motivated reasoning in order to do so”, it wrote in its disclosure. OpenAI would continue to launch further experiments to try and understand how the models work and why they would disable their monitors, it said.
Join our commenting forum
Join thought-provoking conversations, follow other Independent readers and see their replies
Comments
