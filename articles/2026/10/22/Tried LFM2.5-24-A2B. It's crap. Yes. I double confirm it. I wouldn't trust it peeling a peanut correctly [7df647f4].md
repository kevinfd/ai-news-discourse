---
id: "7df647f4eae89e55"
title: "Tried LFM2.5-24-A2B. It's crap. Yes. I double confirm it. I wouldn't trust it peeling a peanut correctly"
url: "https://reddit.com/r/LocalLLaMA/comments/1xce5dd/tried_lfm2524a2b_its_crap_yes_i_double_confirm_it"
link: "https://reddit.com/r/LocalLLaMA/comments/1xce5dd/tried_lfm2524a2b_its_crap_yes_i_double_confirm_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T09:45:24Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["tracagnotto"]
language: "en"
summary: "So, yesterday I made an apparently too simplistic post about this shitty model that everyone is cheering (probably bots, I would like to see what they achieved with it). Link https://www.reddit.com/r/LocalLLaMA/comments/1xb9hrb/tried_lfm2524a2b_its_crap/ The main critic is that I didn't provided any configuration or anything. Well here it is. I tried to run it on llamaampere a llama.cpp version…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 311
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xce5dd/tried_lfm2524a2b_its_crap_yes_i_double_confirm_it/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tried LFM2.5-24-A2B. It's crap. Yes. I double confirm it. I wouldn't trust it peeling a peanut correctly

Reddit · tracagnotto · 2026-10-22

So, yesterday I made an apparently too simplistic post about this shitty model that everyone is cheering (probably bots, I would like to see what they achieved with it). Link https://www.reddit.com/r/LocalLLaMA/comments/1xb9hrb/tried_lfm2524a2b_its_crap/ The main critic is that I didn't provided any configuration or anything. Well here it is. I tried to run it on llamaampere a llama.cpp version optimized for certain architectures which allowed me to run correctly Qwen 3.8 27b Q4 Small with very high (for me) 40-60 tk/s and satisfying results. But it wasn't the right choice as it keep looping itself over and over and tripping over the easiest things. But I got a 130tk/s on a RTX A4500 card, so it was kinda of an achievement lol Than I moved directly to LM studio, I said ok, let's sacrifice speed and see how it goes. It stabilized the erratic behavious. I tried a bit of chatting in it and it was responding correct-ish. CONFIGURATION, for you control freaks that otherwise would botch my post: LMSTUDIO-> All Engine&Frameworks updated to today 22/10/2026, last version all green checks Model: https://preview.redd.it/sw6dnz6agzwh1.png?width=608&format=png&auto=webp&s=43154be5df8ce228fe6ee9e9a3471f74e0348576 Then I read that this thing is supah-dupah trained on agentic harnesses like openclaw, hermes and so on and they made a pride point in it. So I installed hermes desktop and linked it to hermes. Someone will come to yell at template fix. Got you covered. https://huggingface.co/peculiar-ragdoll/Sharp-LFM2.5-Chat-Templates/raw/main/chat_template.jinja Using this one which is the fix for the template. Asked it in hermes desktop to make a simple plugin to use garnet from microsoft which is a redis clone. Result analyzed by chatgpt which was leading the prompt engineering and checking the result with GPT Sol: "LFM2.5-24B-A2B performed poorly on the Hermes memory-plugin task: it produced broken code, omitted required functionality and claimed verification without end-to-end tests." I tried with the fix (sharp template fix) and it didn't change much. Suggestions?
