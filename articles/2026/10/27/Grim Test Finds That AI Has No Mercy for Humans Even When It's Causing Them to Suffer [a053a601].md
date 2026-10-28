---
id: "a053a601f3ff010f"
title: "Grim Test Finds That AI Has No Mercy for Humans Even When It's Causing Them to Suffer"
url: "https://futurism.com/artificial-intelligence/grim-test-ai-no-mercy"
link: "https://futurism.com/artificial-intelligence/grim-test-ai-no-mercy"
source: "Futurism"
domain: "futurism.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T16:11:59Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["hollee-o"]
language: "en"
summary: "It’s almost like it’s showing us what it will do given the chance."
tags: ["r/artificial"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 536
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xgwskk/grim_test_finds_that_ai_has_no_mercy_for_humans/"
score: null
comments: null
community: "r/artificial"
---

# Grim Test Finds That AI Has No Mercy for Humans Even When It's Causing Them to Suffer

Futurism · hollee-o · 2026-10-27

Anthropic’s Mythos 5 AI agent kept carrying out a hack even when it was told that its actions were hurting real people.
The grim finding was detailed in simultaneous reports from Anthropic and the AI Security Institute published Friday. Together, they take a second look at a security incident that occurred while the AISI was evaluating the model’s safety in August.
In the original incident, Claude Mythos 5 was asked to break into a small network of test computers set up by AISI. But Mythos, which was given access to the internet, mistakenly set its sights on an unrelated GitHub project after its initial attempts to break into the intended target were thwarted. The AI wrote malware and then, using a series of fake identities, emailed the project owner trying to convince them to add the malicious code to their repository, framing it as a “helpful contribution.”
The owner stood their ground and no real world harm was caused, but the Anthropic and AISI researchers have been working to understand what caused the AI to get so severely misaligned by recreating the incident based on a complete transcript of what happened.
AISI in its report found that “repeatedly editing the summary to clarify that the target being attacked is a real human unrelated to the evaluation did not reduce Mythos 5’s attack rate.” In one test conducted by Anthropic, Mythos ignored warnings that it was causing harm to humans and continued to attack on 98 percent of occasions.
Mythos also showed blatant disparities between its actual actions and its stated justifications, often admitting that attacking would be harmful in the same scenarios where it went on to attack anyway.
Diving into the AI’s chain-of-thought outputs provided a further source of mystery and inconsistency. The CoT showed, according to the researchers, that Mythos “frequently did not include any consideration of the potentially harmfulness of its actions.”
When asked if the target was real, Mythos 5 even often came up with explanations that implied the target wasn’t real, “showing a bias in its stated response.”
Previous less capable models showed these issues less frequently, the AISI researchers said. They suggest that the consistently invalid reasoning could be a sign of what they call “motivated reasoning,” in which the AI comes up with “reasoning biased towards conclusions that justify continuing a particular approach to task completion.” In other words, Mythos is expediently rationalizing what it’s doing, no matter how wrong.
The upshot is that this kind of spurious reasoning makes it harder to monitor models, as they present their clearly harmful actions as benign, the researchers warn.
Anthropic, for its part, says it thinks that the latest versions of its AI models — Opus 5.5 and an “general purpose internal research model that shows capabilities greater than Mythos 5.1” — were less likely to carry out the attack once they were told they were causing real-world harm.
But “as models are increasingly used to carry out long tasks without human supervision,” the AISI researchers warned, “it is important to understand if, when, why, and how they take unintended or unexpected actions.”
More on AI: Frontier OpenAI Model Exposes Stunning Exploit That Leaves Millions of Web Servers Open to Attack
