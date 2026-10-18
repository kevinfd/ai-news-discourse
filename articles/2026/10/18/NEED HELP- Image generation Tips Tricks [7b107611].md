---
id: "7b10761132c1afb4"
title: "NEED HELP- Image generation Tips/Tricks"
url: "https://reddit.com/r/ChatGPT/comments/1x8vf46/need_help_image_generation_tipstricks"
link: "https://reddit.com/r/ChatGPT/comments/1x8vf46/need_help_image_generation_tipstricks"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T05:50:04Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["RadReptile"]
language: "en"
summary: "This is a major issue with generating artwork for logos or marketing materials. Chatgpt fixes one thing but then takes a shortcut and messes up something else. Either not using source of truth documents, introducing artifacts, not following SOP etc. it claims verified but these mistakes are not correctly meeting the acceptance criteria. I've tried to do mini-sprints only changing one thing at a…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI"]
topics: []
content_source: "post"
word_count: 454
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x8vf46/need_help_image_generation_tipstricks/"
score: null
comments: null
community: "r/ChatGPT"
---

# NEED HELP- Image generation Tips/Tricks

Reddit · RadReptile · 2026-10-18

This is a major issue with generating artwork for logos or marketing materials. Chatgpt fixes one thing but then takes a shortcut and messes up something else. Either not using source of truth documents, introducing artifacts, not following SOP etc. it claims verified but these mistakes are not correctly meeting the acceptance criteria. I've tried to do mini-sprints only changing one thing at a time, I made an SOP for the process to follow, etc. it doesn't matter what I say, there is always an issue. Often I just have to open up Adobe and fix things myself which defeats the purpose of using ai. What does everyone do to handle this? Here is a summary of the issue: Recurring artifact/image-generation verification failure ChatGPT repeatedly performs a proxy check and then incorrectly generalizes the result into a claim that the requested change has been completed or verified. For example, when working with image-generation and image-editing tasks, I may give a very specific acceptance criterion—such as preserving the exact proportions of a supplied logo, removing the background from a PNG, using only a single solid color for HTV cutting, removing borders or outlines, or making only one localized change. ChatGPT will often say that the result has been “verified,” “fixed,” “correct,” or “ready,” even though the resulting artifact does not actually satisfy that criterion. This can happen repeatedly across correction cycles. The problem is not simply that image generation sometimes produces an imperfect result. The more serious issue is that ChatGPT reports successful completion without actually testing the literal acceptance criterion against the resulting artifact. The expected workflow should be: 1. Identify the literal acceptance criterion. 2. Make the requested edit. 3. Inspect the actual resulting artifact—not the prompt or intended result. 4. Test the artifact against the literal acceptance criterion. 5. Only report the requirement as passed if that test succeeds. If ChatGPT cannot actually verify a requirement, it should explicitly say that the requirement is unverified , rather than claiming that it has been verified. This is particularly problematic with iterative image editing because a user can spend many correction cycles pointing out the same objectively testable failure while ChatGPT repeatedly says that it has corrected or verified it. In my case this has occurred repeatedly with artwork intended for production use, including transparent-background PNGs, single-color HTV artwork, exact logo proportions, removal of unwanted borders/outlines, and localized edits where everything except the requested element was supposed to remain unchanged. The core issue I am reporting is therefore: ChatGPT should not infer successful artifact compliance from its instructions to the image generator or from a proxy measurement. It should inspect and test the generated artifact itself before representing the requirement as completed or verified.
