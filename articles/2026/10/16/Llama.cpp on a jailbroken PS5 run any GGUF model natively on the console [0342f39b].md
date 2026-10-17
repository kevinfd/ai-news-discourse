---
id: "0342f39befa10261"
title: "Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console"
url: "https://github.com/cobanov/PS5LM"
link: "https://github.com/cobanov/PS5LM"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-16T18:32:35Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Anon84"]
language: "en"
summary: "Your PS5 runs the language model. Every device on your network uses it.\nllama.cpp on the console's GPU, with OpenAI and Anthropic APIs and a screen made for the TV.\nGet the app · Website · Get started · Issues\nNew: decision models, powered by Ollaya. PS5LM now runs Jev-like\ndecision models (d1, Clef, OpenJev and more) on the GPU and answers the same /v1/systemone\nAPI as Ollaya: typed decisions…"
tags: []
orgs: ["Anthropic", "OpenAI", "Meta", "Hugging Face", "Alibaba"]
topics: ["models & research", "products & launches", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 780
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50122431"
score: 302
comments: 75
community: "Hacker News"
---

# Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console

GitHub · Anon84 · 2026-10-16

Your PS5 runs the language model. Every device on your network uses it.
llama.cpp on the console's GPU, with OpenAI and Anthropic APIs and a screen made for the TV.
Get the app · Website · Get started · Issues
New: decision models, powered by Ollaya. PS5LM now runs Jev-like
decision models (d1, Clef, OpenJev and more) on the GPU and answers the same /v1/systemone
API as Ollaya: typed decisions with calibrated probabilities, in a fraction of a second.
PS5LM is for anyone with a jailbroken PS5 who wants a private model server at home. It loads a GGUF model onto the console's GPU and serves it to your laptop, your phone and your coding tools. It needs no PC while it runs, no cloud and no account.
  
Qwen 3.5 9B answering requests from a laptop on a PS5 Slim. Click for the video.
  
  
  
  
  
  
  
Home, Models, Console, API and Settings on the TV.
- It runs on the GPU. llama.cpp's Vulkan backend on the console's RDNA 2 GPU, with 11.4 GB of the shared memory for the model and its context. Every architecture and quantization llama.cpp knows comes along.
- It answers your network. OpenAI's /v1/chat/completions, Anthropic's /v1/messages (Claude Code
works against it) and a chat page in any browser. Point a client at http://<console>:8081 and use
any model name: the loaded one answers.
- It decides, too. Load a decision model and the console answers TypeSafe's /v1/systemone:
choice, score and yes-or-no questions about text and images, the API Ollaya serves on a PC.
- It shows its work. Every request streams across the TV as a chat: which device asked, what it asked, and the reply as it is written. Square sends a demo and Triangle opens a keyboard, so the console can be tried from the couch.
- It watches the console. A Console page charts temperature, power, GPU and CPU load over the last two minutes or the last hour, beside a table of every reading.
- It picks what fits. The planner reads each GGUF and gives it the longest context and best cache that fit the memory free. A Suggested list holds models measured on the console, and the app downloads from Hugging Face by itself, to internal storage, the M.2 drive or a USB drive.
- It reads images. Models with an image projector (Gemma 4, MiniCPM-V, d1) take pictures in chat and in decisions.
Ollaya runs open decision models on a PC the way Ollama runs language models. PS5LM brings the same idea to the console: a decision model reads a state and answers typed questions in one forward pass, with no text generated.
curl http://<console>:8081/v1/systemone -H 'Content-Type: application/json' -d '{
  "state": "I was charged twice this month. Refund me or I cancel.",
  "questions": {
    "intent": {"type": "choice", "instructions": "What does the customer want?",
               "criteria": {"refund": null, "information": null, "cancel": null}},
    "angry":  {"type": "noul", "instructions": "Is the customer angry?"}
  }
}'
The Suggested list has d1 Omni 600M, d1 3B and Clef Flash. Any GGUF that carries llama.cpp's decision metadata loads the same way, and the app labels it a decision model.
You need a PS5 on firmware 7.00 to 13.60, jailbroken, with these payloads loaded:
- Download ps5lm-app-vX.Y.Z.zip from the latest release and unzip it.
- Copy the PPSA99575 folder to /data/homebrew over FTP. ShadowMountPlus adds PS5LM to the
home screen.
- Open PS5LM, go to Models > Suggested and get a model. Or copy a .gguf to /data/PS5LM/models, or to PS5LM/models on a USB drive.
- Load it. Once Home says Ready, open http://<console>:8081 in a browser, or point your OpenAI or
Anthropic client at it.
To update, copy the new folder over the old one. Settings, models and downloads stay in
/data/PS5LM. Using it from coding tools (opencode, Codex, Claude Code) is in
docs/CLI.md.
C++ on ps5-homebrew-ui, llama.cpp with ggml-vulkan on PS5_Vulkan's RADV, built on Linux.
Building · Console notes · Porting · Research · Models that fit · Roadmap · Changelog · The original payload
- abhi245y, who built the native GPU app this one grew from (PS5LM Plus).
- llama.cpp and ggml, which do the actual work.
- Mihawk-99 for PS5_Vulkan and RADV on the PS5, and
PS5CEMU-HAR for the driver patches in patches/mesa.
- BlackBearReloaded for ps5-homebrew-ui, ps5-opengl and ps5-homebrew-dev-protocol, and John Törnblom for the SDK.
- Marice for ps5-exporter, which the app carries.
- Manrope (OFL) for the type, and PocketVibe for the interface sounds.
GPL-3.0-or-later, see LICENSE. llama.cpp keeps its MIT licence, Manrope its OFL. No Sony SDK files, keys, firmware or model weights are in this repository.
PS5LM is not affiliated with Sony Interactive Entertainment. "PlayStation" and "PS5" are trademarks of Sony Interactive Entertainment.
