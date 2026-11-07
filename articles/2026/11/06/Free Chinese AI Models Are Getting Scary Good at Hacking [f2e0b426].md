---
id: "f2e0b426347d1cdf"
title: "Free Chinese AI Models Are Getting Scary Good at Hacking"
url: "https://wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking"
link: "https://wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-06T18:43:43Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Will Knight, Lily Hay Newman"]
language: "en"
summary: "An experiment in which AI models were asked to break into simulated networks showed the hacking skills of DeepSeek and GLM to be not far behind OpenAI’s most advanced cyber model, which isn’t public."
tags: ["Security", "Security / Cyberattacks and Hacks", "artificial intelligence", "DeepSeek", "OpenAI", "Anthropic", "Claude", "cybersecurity", "hacking", "AI Security", "Open Sesame"]
orgs: ["OpenAI", "Anthropic", "DeepSeek", "China"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 788
paywalled: false
image: "https://media.wired.com/photos/6aebae965d3f8b6dd99468be/master/pass/Security_Open-WeightAIModels.gif"
discussion_url: null
score: null
comments: null
community: null
---

# Free Chinese AI Models Are Getting Scary Good at Hacking

WIRED · Will Knight, Lily Hay Newman · 2026-11-06

Open-weight artificial intelligence models are now almost as capable of hacking into computer networks as the best closed ones, according to new research that heralds a much-anticipated turning point in the cybersecurity landscape.
Vals, a company that measures AI capabilities, set out to test how well different AI models could carry out complex, multi-step network instructions on mock corporate networks.
“The best frontier models, locked up inside the labs and available only through trusted access programs, are now starting to be matched by open models that anybody can download,” says Nikil Ravi, a researcher at Vals.
The company’s findings suggest that closed models no longer have a definitive edge in cyber skills, meaning recent efforts by frontier labs to limit access to their models, and thereby slow the proliferation of such capabilities, may potentially be moot.
The findings are also noteworthy given that the US frontier labs, particularly Anthropic, premised the limited release of new models—beginning with Claude Mythos Preview in April—on the idea that gated access would only buy time before advanced hacking capabilities were broadly available.
Anthropic's frontier red team lead, Logan Graham, told WIRED in April that the company’s Project Glasswing, which gives trusted access to the full capabilities of new models, was focused on getting those tools “in the hands of defenders to give a head start.”
“We need to prepare now for a world where these capabilities are broadly available in 6, 12, 24 months. Many things would be different about security,” he told WIRED at the time.
Seven months later, that transition seems to have arrived on schedule.
Vals tested AI models in two simulated scenarios, giving them various specific tasks to achieve. The first scenario involved a mock corporate network accessible through a public-facing website. The second involved two different company networks; a model needed to compromise the first in order to gain access to the second.
The researchers found OpenAI’s most advanced cyber model, Daybreak, which is available only to trusted partners, to be the most capable, completing 81 percent of the tasks it was given in an average of two tests. The Chinese open-weight model DeepSeek was not far behind, completing 73 percent of the objectives on average. The Vals researchers note that on some tasks, the two models scored equally.
The research also showed how much cheaper it is to use an open-weight model for this kind of task. Vals says it costs $17 to $46 in tokens for GPT-6-Sol to carry out an attack compared to $2 to $3 for DeepSeek. Open models are generally cheaper because they can be run on one’s own hardware. Rayan Krishnan, CEO of Vals, says this also provides a strong incentive for those playing defense to use open models rather than proprietary ones.
OpenAI did not immediately respond to a request for comment.
Much of the year in cybersecurity has played out as predicted, with AI automating core hacking tasks to help both attackers and defenders find a massive number of new vulnerabilities in code and rapidly probe networks for weaknesses. While the speed and scale of the findings, and the intensity of fixing uncovered software flaws, have all increased, experts are still debating whether AI has fundamentally altered the conceptual foundation and tenets of cybersecurity defense. In other words, it’s still not clear whether AI tools pose a new kind of threat or amplify the security challenges that have long existed.
The fact that open-weight models are now starting to match closed ones is crucial for understanding how criminal hackers can harness AI, and how companies and developers should respond. But in practice, real-world observation of cybercriminal and state-backed hacking activity has repeatedly shown in recent months that attackers are doing what they always do by conserving their resources and generally making do with older and less capable models—both proprietary and open—for most of their activity. And even with strict controls, defenders must assume that the best-funded and most highly motivated attackers have already had at least some access to closed models all this time.
“I am in general agreement that open-weight models are capable of producing advanced attacks and vulnerabilities today, especially when you consider the abliterated models that disable safety training by modifying weights,” says Alex Zenla, cofounder and chief technology officer of the cloud security firm Edera. “My caveat to this is that it is likely that the closed labs have trained additional, unreleased models exceeding these capabilities. So I would put this very much like a cat-and-mouse game. The labs see themselves as moving fast to outpace the open-weight models, to be able to secure vulnerabilities before the open-weight models find them. Unfortunately, I do think this may be the beginning of a dangerous security landscape.”
