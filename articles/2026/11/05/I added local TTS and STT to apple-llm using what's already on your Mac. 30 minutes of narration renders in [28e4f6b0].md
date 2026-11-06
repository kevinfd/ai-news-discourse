---
id: "28e4f6b0f1966306"
title: "I added local TTS and STT to apple-llm using what's already on your Mac. 30 minutes of narration renders in under 20 seconds on an M4 Air"
url: "https://reddit.com/r/LocalLLaMA/comments/1xoowb4/i_added_local_tts_and_stt_to_applellm_using_whats"
link: "https://reddit.com/r/LocalLLaMA/comments/1xoowb4/i_added_local_tts_and_stt_to_applellm_using_whats"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:37:08Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["light_2earth"]
language: "en"
summary: "I posted apple-llm here a while back: a Node and Python package that calls the LLMs Apple ships with macOS, with no API key. Version 0.3 adds the rest of what's already on your Mac, the system voices and Apple's speech recognition. There's nothing to sign up for, and your audio stays on the machine. The narrator in the video and every demo voice came from my Mac through the package. Nobody…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple", "OpenAI"]
topics: ["agents & coding"]
content_source: "post"
word_count: 442
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoowb4/i_added_local_tts_and_stt_to_applellm_using_whats/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I added local TTS and STT to apple-llm using what's already on your Mac. 30 minutes of narration renders in under 20 seconds on an M4 Air

Reddit · light_2earth · 2026-11-05

I posted apple-llm here a while back: a Node and Python package that calls the LLMs Apple ships with macOS, with no API key. Version 0.3 adds the rest of what's already on your Mac, the system voices and Apple's speech recognition. There's nothing to sign up for, and your audio stays on the machine. The narrator in the video and every demo voice came from my Mac through the package. Nobody recorded anything. npm install -g apple-llm # or: pip install apple-llm apple-llm speak "Hello there" --voice Samantha apple-llm speak --file book.txt -o book.m4a apple-llm transcribe meeting.mp4 -o meeting.srt apple-llm listen Or from code: from apple_llm import speak, transcribe speak("Hello there", voice="Samantha") text = transcribe("meeting.mp4").text The npm package's local server also answers /v1/audio/speech and /v1/audio/transcriptions , so an OpenAI client works once you change the base URL. Because speech now sits next to the LLMs, there's also a voice assistant example in about 20 lines: microphone to text, text to the on-device model, reply to speech, with none of it leaving the Mac. The docs are LLM-friendly too. llms.txt is a single plain-text guide covering setup, the local LLM, TTS, STT, both SDKs, the HTTP APIs and troubleshooting. Give that URL to your coding agent and ask it to wire apple-llm into your project. What I measured (M4 MacBook Air, macOS 27.2) 30 minutes of speech rendered to a file: 18 to 20 s, 11.3 MB M4A, about 50 MB of memory 60 minutes: 40 s, 22.5 MB 30 minutes transcribed: about 28 s, with a timestamp on every word if you ask for it 184 voices on my Mac, and 68 recognition languages, each downloaded the first time you use it What it can't do No Siri voices by name. Apple doesn't let apps choose them. The default voices on my Mac are basic quality. Better ones are a free download in System Settings. It won't detect the language from the audio. You name it, or it uses your system language. No MP3 or Opus output, and no WebM, Ogg or MKV input. 3 to 4% word error rate on clean synthetic speech. Real recordings will do worse, so test on yours. I wanted speech and the LLMs in one library with no dependencies, for both Node and Python. It needs macOS 26 or later on Apple Silicon, plus the Xcode Command Line Tools. MIT licensed. GitHub: https://github.com/jagdishpal02000/apple-llm Site: https://jagdishpal02000.github.io/apple-llm/ I've only run this on macOS 27.2, and I've tested the microphone with speech played through the speakers rather than a person talking. If you're on macOS 26, or you try listen in a noisy room, tell me what breaks.
