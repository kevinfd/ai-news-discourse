---
id: "9bb7235c9cc6d40c"
title: "Hugging Face appears to be hosting a load of models that could be used for cyber attacks"
url: "https://transformernews.ai/p/hugging-face-appears-to-be-hosting"
link: "https://transformernews.ai/p/hugging-face-appears-to-be-hosting"
source: "Transformer"
domain: "transformernews.ai"
source_type: "newsletter"
collector: "rss"
date: "2026-11-11T18:00:36Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Chris Stokel-Walker"]
language: "en"
summary: "Credit: Shakeel Hashim for Transformer/Hugging Face It’s ironic, but not surprising: Hugging Face, the open source AI model hosting platform hacked by AI agents earlier this year , is home to thousands of models that could enable pretty much anyone to launch their own AI-powered cyberattacks. More than 6,500 models tagged as “abliterated,” uncensored or heretic — terms meaning that safety…"
tags: []
orgs: ["Hugging Face", "Anthropic", "Nvidia", "DeepSeek"]
topics: ["models & research", "safety & ethics", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 1336
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!IXSQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc25397-3c1b-47c4-87a2-72b45dfb96ca_1920x1080.png"
discussion_url: null
score: null
comments: null
community: null
---

# Hugging Face appears to be hosting a load of models that could be used for cyber attacks

Transformer · Chris Stokel-Walker · 2026-11-11

It’s ironic, but not surprising: Hugging Face, the open source AI model hosting platform hacked by AI agents earlier this year, is home to thousands of models that could enable pretty much anyone to launch their own AI-powered cyberattacks.
More than 6,500 models tagged as “abliterated,” uncensored or heretic — terms meaning that safety filters and guardrails have been removed from the models — were hosted on the platform in July, and many more remain. The continued existence of the models on Hugging Face points to an emerging challenge: How the platform is following its own content policy on uncensored models. That has become even more of an issue following its purchase by Nvidia.
“The open-weight models are getting almost as good as frontier models, and now frontier capability is available to anyone, regardless of intent, with no guardrails,” said CrowdStrike CEO George Kurtz at a conference in Barcelona this month. “That’s what we’re facing.” He later told Transformer that abliterated models were “certainly problematic.”
Hugging Face’s content policy explicitly prohibits models designed to disrupt systems, gain unauthorized access or generate malicious code. But stripping out a model’s safeguards doesn’t necessarily mean it was designed for those purposes. The question is where Hugging Face draws the line between an unrestricted tool and one expressly intended for cyberattacks.
“It’s a natural magnet for the bad guys,” said Alan Woodward, a cybersecurity expert at the University of Surrey, who reckons freely distributing such models creates obvious risks. Determined criminals could also remove safeguards themselves, but there’s a gap between that and making the models available for distribution without restriction on a mass scale. “It’s not altogether helpful that they’re available to one and all through Hugging Face, and that may be where there needs to be some conversations with the likes of Hugging Face.”
There are indications that Hugging Face does take action against some of these models. In early October, it took down a version of a GLM-5.3 model that was explicitly marketed as “abliterated for offensive cyber.” The model, developed by a creator using the username Audnai, is no longer available on the platform. The company did not respond to questions about why it removed one model explicitly branded as being for offensive cyberattacks and not others.
However, Audnai has several other models, including one updated in the last few days, that market themselves as “unrestricted” or “abliterated.” There’s another abliterated GLM-5.3 model, although users must accept conditions to access its files. Audnai claims the model refuses just 7.5% of harmful requests in their tests. Audnai also advertises an unrestricted version of Kimi K3.1.
They’re far from the only developer offering models on Hugging Face that specifically market themselves as for offensive cyberattacks, including versions of DeepSeek-4.1 and one described as a ‘CyberStrike-OffSec,’ or offensive security model. One GLM-5.3 derivative uploaded by dealignai describes itself as “built for offensive cybersecurity.” Its creators claim the model has been tested generating working keyloggers, ransomware and tools for brute-force attacks.
The dangers of these models being available to all and sundry aren’t hypothetical. In September, Anthropic found GLM-5.3 could successfully develop exploits for known browser vulnerabilities in 12% of attempts. That means roughly one in eight times, the AI model wrote code that could exploit potential issues in web browsers — the same kind of method used by hackers to get into victims’ machines. The researchers also found that removing its safety restrictions made it comply with all harmful requests in a separate set of tests.
But those who are providing the tools that can strip out guardrails from models point out that just because a model is abliterated, doesn’t mean it’s going to be used for nefarious purposes. “It turns a model into an answering machine,” says Philipp Emanuel Weidmann, the developer of Heretic, a tool that removes safety alignment — Weidmann calls it “censorship” — from mainstream AI models produced by large labs. “That’s it.”
Hugging Face’s confusion over whether abliterated models should or shouldn’t be allowed on its platform is echoed by the wider AI community.
“I honestly feel a bit torn,” says Andrew Arditi, an AI researcher who helped establish the scientific foundations for abliteration. In a 2024 paper, he and his colleagues discovered that a small part of an AI model’s internal machinery could determine whether it refused a request. Once removed, models became much more willing to answer questions they would otherwise refuse to address. And overcautious big tech companies have tended to draw the boundaries of what their models would address pretty tightly. “We certainly did not expect this methodology to explode as much as it has over the past couple years,” says Arditi.
Weidmann claims that most demand for abliteration comes from legitimate sources, not cybercriminals. He says he speaks to companies interested in using unrestricted models to conduct pharmaceutical and cybersecurity research. Even Switzerland’s Supreme Court has explored Heretic, he claims, after mainstream AI models refused to translate certain legal documents. Woodward agrees that there are legitimate uses for unrestricted models. AI safety guardrails can prevent cybersecurity professionals from investigating the same vulnerabilities that attackers exploit, making abliterated models potentially useful defensive tools.
Catherine Flick, a professor of ethics and games technology at the University of Staffordshire, is less convinced that the potential benefits of security-stripped models justify the risks. “I think most of the reasons why people would use this is to get around the things that have been very rightly refused.”
She argues that removing refusals can also expose weaknesses in models whose answers to dangerous questions have never been properly tested. She also worries that once these models are released, the ability to control their distribution is lost — meaning that they can be misused, even if the creators never intended them to do so.
The debate also encompasses a broader question around whether AI should replicate the closed-source norms of the past, or be more open to open-source sharing. Supporters say that open-source and open-weight models give people more accountability over how the AI models work, and free access to AI from the grasp of a handful of large AI labs. But critics say putting such powerful tools in the hands of everyone can be a gamble that could easily backfire. As CrowdStrike’s Kurtz points out, “the genie’s out of the bottle.”
“All these models are out there, and they’re really good,” Kurtz told Transformer. “Even if you put a stop to all, it wouldn’t change anything because they’re already out there.”
That’s a concern that has vexed the frontier AI labs, and caused them to campaign against the idea of open-weight models, which have their parameters publicly available to download and modify. AI developers can restrict access to their most powerful models, but when the underlying weights are publicly available, preventing users from modifying them becomes extraordinarily difficult, they argue. The extent to which that worry is legitimately felt is questioned by those involved in abliteration. “I personally assume that most of the so-called backlash isn’t organic at all and is attributable to influence operations by corporate entities,” says Weidmann. There is no evidence to show that is the case.
Arditi, the researcher and early identifier of the possibilities of abliteration, believes there must be something between the two extremes of AI models controlled entirely by their developers and models stripped of almost every restriction. But that solution has yet to emerge. “There really isn’t currently much ideation or discourse on what a middle path might look like.”
He suggests researchers should investigate ways of allowing businesses and individuals to customise their AI models without removing every safeguard against misuse. Thinking Machines, the AI lab set up by former OpenAI executive Mira Murati, has suggested a “safe path” to open weights in a blog post.
A change of approach from the frontier labs, which weakens some of the most stringent guardrails in place, is something Woodward also thinks is necessary. Abliterated models “only need to be a necessary evil if there’s no alternative,” he says.
