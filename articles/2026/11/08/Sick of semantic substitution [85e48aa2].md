---
id: "85e48aa2f524f53b"
title: "Sick of semantic substitution"
url: "https://reddit.com/r/ClaudeAI/comments/1xqp2l0/sick_of_semantic_substitution"
link: "https://reddit.com/r/ClaudeAI/comments/1xqp2l0/sick_of_semantic_substitution"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T03:49:58Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["DarkSkyKnight"]
language: "en"
summary: "It is an extreme productivity drain to have these models substitute settled vocabulary with random synonyms, particularly when working on math or code. No, Claude, you cannot just substitute \"morph the routine\" with \"reshape the routine\" because only Morph is in the code while reshape could literally be anything. This semantic substitution makes it extremely tedious to understand its work and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "policy & regulation", "agents & coding"]
content_source: "post"
word_count: 551
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqp2l0/sick_of_semantic_substitution/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Sick of semantic substitution

Reddit · DarkSkyKnight · 2026-11-08

It is an extreme productivity drain to have these models substitute settled vocabulary with random synonyms, particularly when working on math or code. No, Claude, you cannot just substitute "morph the routine" with "reshape the routine" because only Morph is in the code while reshape could literally be anything. This semantic substitution makes it extremely tedious to understand its work and output and, moreover, occasionally cause it to write a wrong plan that gets interpreted in a different way by the next agent picking up the plan. I almost suspect that this is a result of needing to satisfy watermarking regulation. Now, I'm not saying that watermarking itself caused this. I am instead hypothesizing that as part of a project to satisfy regulation, Anthropic created more semantic substitution in their models. Now, as for why I have this hypothesis: https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/ For example, if the LLM distribution is very low entropy, meaning it almost always returns the exact same response to the given prompt, then Tournament sampling cannot choose tokens that score more highly under the g functions. In short, like other generative watermarks 2 , Tournament sampling performs better when there is more entropy in the LLM distribution, and is less effective when there is less entropy. In Supplementary Information section H , we provide a theoretical analysis describing the watermarking strength of a layer of Tournament sampling as a function of a certain kind of entropy; similar analyses have been done for other generative watermarks 23 – 25 . The entropy of the LLM distribution itself depends on several factors, including the model—for example, larger or more advanced models tend to be more certain and thus lower entropy 21 , and reinforcement learning from human feedback can reduce entropy (also known as ‘mode collapse’) 26 . As for the conspiracy theory that I have, I suspect that Anthropic deliberately increased the entropy of the models in situations that naturally have low entropy in order to increase the statistical power of the watermark test. In situations that naturally have low entropy, there is typically only one very probable answer for the next token. What would increasing entropy look like? Well, we would deliberately shift the probability distributions to increase uncertainty: 0.999 -> 0.996 "concat" 0.0007 -> 0.0027 "concatenate" 0.0002 -> 0.0009 "controller" This increases the ability for watermarking to detect LLM-generated output, because there is now more variation to actually meaningfully detect the difference due to different starting seeds. But this means semantic substitution becomes more frequent . Going from a 0.1% probability of a nonsensical swap to a 0.4% is huge! Now consider this at scale, when Claude tries to explain what it has done. This occurs even if watermarking has no detectable output on quality ... because that is CONDITIONAL on them not changing the model itself. But they could easily have made the model produce higher entropy in order to make the watermarking work well even on outputs with low word counts or output with naturally low entropy... Who knows. Of course, the annoying semantic substitution could be due to a different reason, but regardless, prose is still the worst part of Claude models and has been since Opus 4.7. It is extremely unpleasant to work using Claude and they have seemingly made little progress on this issue.
