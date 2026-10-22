---
id: "bd65f691832a9ea1"
title: "AI is great with text and images but bad at audio and video. What other gaps stand between us and AGI?"
url: "https://reddit.com/r/singularity/comments/1xby0ar/ai_is_great_with_text_and_images_but_bad_at_audio"
link: "https://reddit.com/r/singularity/comments/1xby0ar/ai_is_great_with_text_and_images_but_bad_at_audio"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T20:10:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["coldrolledpotmetal"]
language: "en"
summary: "edit: This post is about understanding video and audio, not generating it. AI video and music generation is already impressive, but that's not what I'm talking about. I’ve been seeing a bunch of people on this sub say in the past month or so that AGI has already arrived with GPT Astra and Opus 5.5, but I think there are still a lot of relatively basic tasks that AI can’t do anywhere near a human…"
tags: ["r/singularity"]
orgs: ["Google"]
topics: ["safety & ethics", "agents & coding", "models & research"]
content_source: "post"
word_count: 479
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xby0ar/ai_is_great_with_text_and_images_but_bad_at_audio/"
score: null
comments: null
community: "r/singularity"
---

# AI is great with text and images but bad at audio and video. What other gaps stand between us and AGI?

Reddit · coldrolledpotmetal · 2026-10-21

edit: This post is about understanding video and audio, not generating it. AI video and music generation is already impressive, but that's not what I'm talking about. I’ve been seeing a bunch of people on this sub say in the past month or so that AGI has already arrived with GPT Astra and Opus 5.5, but I think there are still a lot of relatively basic tasks that AI can’t do anywhere near a human level. Sure, we’re seeing incredible advances in computer use, and AI has gotten quite good at math and programming. It’s great with static things like text, images, and code, but it struggles with anything that unfolds over time. That also breaks verification, the thing that drove the advances in agentic coding: a model that can’t properly perceive its output can’t check it. Audio is the clearest example. GPT-Live sounds great and understands you well, but the labs’ audio work has gone almost entirely into conversational speech, not general audio understanding. Ask a model to follow one voice in a noisy room, or tell you which instrument came in when, and it falls apart in ways a person with normal hearing never would. Speaker separation exists, but it gets brittle as soon as people talk over each other. Giving models tools like demucs or Python doesn’t fix this either, because they’re bottlenecked by the narrow models powering those tools. A model can write code that generates audio, but it can't listen to the result and reliably tell whether it sounds remotely like what was intended, much less whether or not it sounds good. Coding agents improved quickly because they can run the code and check the output. With audio, that feedback loop currently doesn't exist. Video has the same problem. By default, Gemini samples video at 1 frame per second, so it’s basically watching a slideshow, and anything that happens between frames doesn’t exist to it. Google’s new agentic video mode that lets the model zoom in on the parts it thinks matter is just a workaround for not perceiving time continuously. I know there’s a lot of debate around the definition of AGI, but something that can’t tell whether a song sounds right or follow a conversation in a crowded room doesn’t seem general to me yet. I’m sure these problems are solvable with more resources thrown at them, but until they’re solved, I don’t think we can call it AGI. TL;DR: Frontier AI is great at static things like text, images, and code, but it still struggles with anything that unfolds over time, like audio and video, largely because the labs haven’t put much effort there. Those gaps are why I’m hesitant to call what we have AGI. So, what else do y’all think AGI should be able to do that current AI still can’t, even when combining the capabilities of multiple models?
