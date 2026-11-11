---
id: "467c96aac5c6385e"
title: "adventists-ai/Sophon-Realtime-v1 · Hugging Face"
url: "https://huggingface.co/adventists-ai/Sophon-Realtime-v1"
link: "https://huggingface.co/adventists-ai/Sophon-Realtime-v1"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-10T14:20:01Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["pmttyji"]
language: "en"
summary: "An open full-duplex voice model family that hears your tone and speaks with one. Adventists AI · Apache-2.0 · Recommended: Tag · Flash · Try it online · GitHub Talking to it feels like a phone call with a person: it listens the whole time you talk, picks up as soon as you stop, and stops the moment you cut in. It hears how you say things (hesitation, emphasis, sarcasm, laughter, sighs) and…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Google", "xAI", "DeepSeek", "Hugging Face", "China"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1219
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xso32l/adventistsaisophonrealtimev1_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# adventists-ai/Sophon-Realtime-v1 · Hugging Face

Hugging Face · pmttyji · 2026-11-10

Sophon-Realtime v1
An open full-duplex voice model family that hears your tone and speaks with one. Adventists AI · Apache-2.0 · Recommended: Tag · Flash · Try it online · GitHub
Talking to it feels like a phone call with a person: it listens the whole time you talk, picks up as soon as you stop, and stops the moment you cut in. It hears how you say things (hesitation, emphasis, sarcasm, laughter, sighs) and answers with tone of its own: it laughs, sighs and clears its throat when the conversation calls for it.
This is the home page of the Sophon-Realtime v1 family. Three builds share one brain (the same 32B model listens, decides when to take the turn and writes the reply); they differ only in how the reply becomes sound. Start with Tag.
Three builds: which one?
Pick Tag if you want the voice to act; pick Flash if users per GPU matter most; pick E2E for the fastest first audio with a voice that still laughs and sighs. Tag and Flash share the same APIs, so you can switch later; E2E runs on its own engine.
Highlights
- VoiceBench 82.8 and Big Bench Audio 81.8%: the strongest brain among open full-duplex models. #1 among open full-duplex models on both; level with GPT-4o-mini-Audio on VoiceBench. All three builds share this brain.
- Paralinguistic understanding 48.6, #1 overall: it hears your tone. Ahead of Gemini 3.8 Flash (46.9) and Qwen3-Omni (44.6) on LISTEN, StressTest and MSPB. Its ears are DuplexJev, our open speech-decision model.
- NVV-SuperBench 0.86 (Chinese) and 0.80 (English) with the Tag build: it speaks with tone. The model decides when to laugh, sigh, breathe or clear its throat, and the voice performs it instead of reading the tag aloud.
- Fast: first audio in about 0.25 s with E2E and 0.31 s with Flash. It drafts its reply while you talk; when you cut in, it stops and answers your new question.
- Full-Duplex-Bench v3 tool calling: Pass@1 48%, ahead of Grok (43%), with a 100% response rate: it gets work done. Live mode is compatible with the OpenAI GPT-Live interface and lets it work with a larger backend model. Every reply comes with an auditable transcript.
- One 80 GB GPU for every build, one command. Tag and Flash are served by vLLM-Omni; up to 16 (Tag, E2E) or 40 (Flash) concurrent users per GPU. Apache-2.0 code and weights, free for commercial use.
Quick start (Tag)
Quickest:
pip install "sophon-realtime[trt]"   # Python 3.12, Linux, CUDA 13; keep [trt]: without TensorRT the voice is ~3x slower under load
sophon-realtime serve           # downloads the Tag weights (~42 GB) on first run, then serves on port 8000
Or use the one-command scripts (isolated environment):
git clone https://github.com/adventists-ai/sophon-realtime && cd sophon-realtime/tag
bash install.sh                 # venv + vLLM-Omni + plugin, and downloads the Tag weights (~42 GB)
GPU=0 PORT=8000 bash start.sh   # first start 15–20 min, later 5–8 min
python client_example.py --wav my_question.wav --lang en --voice ryan_en
- APIs: ws://HOST:8000/v1/realtime (full duplex: turn-taking, barge-in, back-channels) and POST /v1/chat/completions (audio in, text + audio out).
- Flash works the same way; see the Flash page. To just try it, talk to it in the ModelScope Studio.
Live mode: a drop-in for OpenAI GPT-Live
live/ in the GitHub repository is a gateway that speaks the OpenAI GPT-Live protocol in front of a Tag or Flash engine: GPT-Live clients switch by changing the URL and key. Sophon keeps the voice; when a request needs a lookup or an action it says a short "Let me check that", hands the task to your backend and speaks the result in its own words. A larger model can also run the back office: with DeepSeek V4 Pro, Big Bench Audio rises from 81.2 to about 83.
To start it, run one more command next to a Tag or Flash engine started with the one-command scripts:
cd sophon-realtime/live && BUILD=tag PORT=8000 LIVE_PORT=8780 bash start_live.sh   # GPT-Live clients: ws://HOST:8780/v1/live/sessions
Benchmark details
Conversation: VoiceBench (official evaluators, gpt-4o-mini judge)
AlpacaEval uses the 199-question standard subset. Other scores come from the VoiceBench leaderboard and from Table 3 of the NemotronLabs VoiceChat paper (arXiv:2609.21967); the MiniCPM-o 4.5 score there is from an independent evaluation.
Spoken reasoning: Big Bench Audio
1,000 spoken reasoning questions, graded on what the model actually says.
Sophon: self-run, with spoken answers transcribed and judged by gpt-4.1. Others: Artificial Analysis leaderboard.
Tool calling: Full-Duplex-Bench v3
Disfluent real human speech with multi-step tool calls. 100 tasks, judged by GPT-4o.
Sophon: best of several runs. Others: official Full-Duplex-Bench v3 results.
Hearing tone: paralinguistic understanding
Sophon-Realtime listens with DuplexJev. These benchmarks test emotion, sarcasm, stress and intonation.
Speaking with tone: NVV-SuperBench
Checks whether the laughs, coughs, sighs and breaths a reply calls for actually show up in the audio. Official scripts, 50 items per category, judged by Gemini 3 Flash; higher F1 is better.
All three builds speak the same tagged reply texts; only the voice differs.
How it works
- Listens continuously. At each pause, the same model decides in a single token whether you've finished, are still talking, are back-channeling or are thinking.
- Drafts early, speaks on time. A reply is drafted from your first pause and released the moment the model decides it's its turn. If you keep talking, the draft is dropped before you hear it.
- Writes how to say it, not just what. The brain marks where to laugh, sigh, breathe, cough or stress a word; All three builds perform these marks and never read them aloud.
- Text half a step ahead, voice in step. Text and voice stream together, so every reply has a transcript for audits, tools and larger backend models.
- Remembers what you actually heard. History keeps the real audio of both sides. When you interrupt, only the part you heard is kept.
- E2E: speech as continuous vectors. In the E2E build a compact talker (about 350M parameters) reads the tagged reply while it is still being written and generates continuous voice vectors directly, with no speech tokens in between; a 2-step decoder turns them into sound. First audio comes in about 0.25 s on one GPU. See the E2E page.
Fine-tuning
Fine-tune the thinker's LLM backbone with LoRA in ms-swift to change persona, tone, domain knowledge and tool use. The audio encoder and the voice stay as released, and turn-taking is not affected. Training continues the bundled tag LoRA (adapters/tag), so laughter, coughs and other sound tags are kept. One 80 GB GPU is enough.
pip install "ms-swift>=4.6"
git clone https://github.com/adventists-ai/sophon-realtime && cd sophon-realtime/finetune
modelscope download --model AdventistsAI/Sophon-Realtime-v1 --include 'base/*' 'adapters/*' --local_dir Sophon-Realtime-v1
python -m sophon_swift.adapters to-swift Sophon-Realtime-v1/adapters/tag tag_swift
swift sft --custom_register_path sophon_swift/swift_register.py \
  --model Sophon-Realtime-v1 --adapters tag_swift --tuner_type lora \
  --dataset my_data.jsonl --learning_rate 5e-5 --num_train_epochs 2 \
  --gradient_accumulation_steps 8 --gradient_checkpointing true --output_dir output
Data format, multi-turn and tool calls, export, serving and regression checks: see finetune/ in the GitHub repository.
Files
This repository is the home page of the v1 family. The thinker base (base/) and tag-writing LoRA (adapters/) used for fine-tuning, and the first E2E preview weights, are in the ModelScope repository. To deploy, use the weights on the Tag, Flash or E2E page.
License
Code and weights are released under Apache-2.0. Third-party components keep their own licences; see NOTICE.
Contact
Business enquiries: jiejin@adventists.ai
