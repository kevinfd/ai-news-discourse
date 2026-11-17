---
id: "885f4bf8cabd27ff"
title: "How did you start, how do you end up now ?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xy34ed/how_did_you_start_how_do_you_end_up_now"
link: "https://reddit.com/r/LocalLLaMA/comments/1xy34ed/how_did_you_start_how_do_you_end_up_now"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T22:19:48Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["revennest"]
language: "en"
summary: "Here is my timeline Text Generation Ollama but quite have bad experience with it. LM studio which still feel half-bake at that time. Msty which easy to use like plug and play but not much I could do custom (or I just don't know at that time). Oobabooga Text Generation-Webui this is the one that make me stick to AI, easy to use and deep custom; I like its function feature that take prompt as…"
tags: ["r/LocalLLaMA"]
orgs: ["Meta", "Stability AI", "China"]
topics: ["products & launches", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 621
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xy34ed/how_did_you_start_how_do_you_end_up_now/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# How did you start, how do you end up now ?

Reddit · revennest · 2026-11-16

Here is my timeline Text Generation Ollama but quite have bad experience with it. LM studio which still feel half-bake at that time. Msty which easy to use like plug and play but not much I could do custom (or I just don't know at that time). Oobabooga Text Generation-Webui this is the one that make me stick to AI, easy to use and deep custom; I like its function feature that take prompt as method/processed then input value in other prompt and then it just output an outcome, no chat history. I run 1 - 4 with my mini pc with i5 6400T, 24GB DDR4 with onboard gpu... Llama 3.1 8B generate so slow at that time like 1 tok/s but I really enjoy using it with that very limited and the roleplay start from here, just my mini pc and Oobabooga Text Generation-Webui . Also some missing thing I forgot at that time, I even mess around with windows WSL then docker for Open WebUI and SearXNG . I finally can help but want it more so arise old gen pc, at that time DDR3 and thing relate to it is very cheap so I brought Xeon E3-1270 V2 with a Chinese mainboard and 32 GB DDR3 while I cancel the sell order of my GTX 1080 Ti. SillyTavern and KoboldCPP I found SillyTavern first but it has quite a trouble with Oobabooga Text Generation-Webui so I follow their guideline and try KoboldCPP which quite harder than Oobabooga Text Generation-Webui for me as KoboldCPP at that time still act like a zip that need to extract (in temp folder) every time I use so I copy from its temp folder, it could run but loss UI, only command-line left so I start to write a bat file to run it like this. pushd %~dp0 uv run kobold\koboldcpp.py ^ --config kobold_default_setting.kcpps ^ --model %gguf%%model%.gguf ^ --usecublas %cublas% "0" "mmq" ^ --contextsize %length% ^ --gpulayers %layer% ^ --quantkv %level% popd Llamafile As I don't want to extract KoboldCPP on every update, I found Llamafile , it quite easy for me to switch as the bat file I create for KoboldCPP just need a little change to work with this one, anyway it also lead me to the real on. Llama.CPP I found it on the right time as Llama.CPP just start to has their own WebUI and its speed is the real thing, at that time still not has router mode so my bat file has its Llama.CPP version. Image Generation A single Youtube video from ChameleonAi name Stable Diffusion Models Explained Once and for All (1.5, 2, XL, Cascade, 3) lead me to this rabbit hole. stable-diffusion-webui-Forge aka Forge , Thank to ChameleonAi that lead me to CivitAI which after read a guideline I have 2 choices which this or ComfyUI , as my AI user interface root from Oobabooga Text Generation-Webui so I choose this instead. reForge as Forge no longer update so I move on. Classic Forge same problem as reForge no longer update as a new model, Anima unable to run on reForge so I'm move on again. Audio Generation I try to do it via Llama.CPP but could not make it work so I wait for more update; While waiting, I finally give a chance for unsloth studio which quite disappoint for me in term of performance so I dig to the one that called via unsloth studio . Audio.CPP I try it before but at that time it still CLI only and I'm unsuccessful to make it work, but now it's also come their WebUI so another rabbit hole for me to fall. This is my AI journey up until now, how about your ?
