---
id: "f6b29b4e2ab3b1b9"
title: "Show HN: Yogurt – Free, private, open-source alternative to Granola"
url: "https://github.com/FrigadeHQ/yogurt"
link: "https://github.com/FrigadeHQ/yogurt"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T15:33:06Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["brownrout"]
language: "en"
summary: "Hey HN, I’m Eric and I want to share an OSS project that I’ve been building in my free time. Yogurt is a free, MIT licensed desktop app that uses on-device AI models to transcribe, summarize, and chat with your meetings. Here's a quick demo video: https://www.youtube.com/watch?v=BFfbXAwRq98 Similar to Granola, Yogurt runs in the background and does not join your calls. But unlike Granola, Yogurt…"
tags: []
orgs: ["Apple", "Microsoft"]
topics: ["models & research", "products & launches", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 978
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50454625"
score: 259
comments: 97
community: "Hacker News"
---

# Show HN: Yogurt – Free, private, open-source alternative to Granola

GitHub · brownrout · 2026-11-11

Private AI meeting notes. Free and open source.
Download for Mac · Windows · Linux
Yogurt records your calls without adding a bot to the meeting.
  macOS 14.4+ (Apple Silicon) · Windows 10 2004+ (x64) · Ubuntu 22.04+ or similar (x64 AppImage) · 8 GB memory
yogurt.so · Help · Build and run locally · MIT license
Made by Frigade.
- Live transcripts. Yogurt records calls and turns speech into text as you talk.
- Meeting summaries. Yogurt writes up the conversation and any notes you add.
- Private by default. Your audio, transcripts and AI processing stay on your computer.
- Free and open source. You can use Yogurt without an account.
- Who said what. Yogurt names speakers from Zoom, Teams and Meet on Mac only.
- Languages. Multi-language mode transcribes 99 languages.
- Recording reminders. Yogurt offers to record when a supported call starts.
- Answers with sources. Yogurt answers questions across meetings and links to the source.
- Folders and search. You can find meetings by folder, title, notes or transcript.
- Copy and export. You can copy notes or transcripts, or save both as Markdown.
- Local MCP server. Your chosen assistant app can read your notes when you allow access.
- Automatic stop. Yogurt stops recording when the call ends.
yogurt-demo.mp4
- Record. Start recording your microphone and call audio; you can add your own notes.
- Transcribe. Yogurt uses whisper.cpp and, on supported Macs, Apple SpeechAnalyzer.
- Summarize and ask. A local open-weight model runs through llama.cpp.
Meeting data stays local; Yogurt goes online for model downloads and update checks.
Where your meetings, recordings, settings and models are stored
- Mac uses ~/Library/Application Support/Yogurt.
- Windows uses %APPDATA%\Yogurt.
- Linux uses ~/.config/Yogurt, or $XDG_CONFIG_HOME/Yogurt if set.
What kind of computer do I need?
A Mac with Apple silicon and macOS 14.4 or newer, a 64-bit PC with Windows 10 (version 2004) or newer, or a 64-bit Linux computer with Ubuntu 22.04 or newer. Each needs at least 8 GB of memory. If your computer is too slow, Yogurt tells you during setup. Calendar and speaker names from calls are Mac only for now.
Windows says “Windows protected your PC.” What do I do?
Click More info, then Run anyway. Windows shows this for new apps that aren’t signed with a Microsoft certificate yet. Yogurt is open source, so anyone can check what it does.
Does Yogurt join my meetings?
No. Yogurt records your microphone and the sound playing on your computer. No bot joins the call, so let the other people on the call know you’re recording.
Are recordings saved?
Yes. Your recordings, transcripts, and notes are saved locally on your computer.
Is Yogurt free?
Yes. Yogurt is free and open source under the MIT license. No account is needed.
Does Yogurt work offline?
Yes. After a one-time download of the AI models, transcription and summaries run locally on your computer.
How much does setup download?
It depends on your computer. Yogurt downloads a smaller notes model first, about 5 GB, then the best one your computer can run well, which can be 14 GB or more. Recording works once setup finishes, and notes and questions work offline once the notes model is in.
How do I connect my assistant app?
In Settings → AI apps, turn on access, copy the helper command, and add it as a local MCP server in your assistant app. Access is off by default. The app can read your meetings, notes and transcripts, but cannot change them. It may send what it reads to its own online model. Turn access off in Yogurt to stop further reads.
Can other apps read my notes through MCP?
Access is off until you enable it in Settings → AI apps. Apps get read-only access to meetings, notes and transcripts. Mac and Linux use a socket in your profile folder with 0600 permissions, so only your user account can open it. Windows uses a named pipe with a new random name each launch, stored only in your profile folder. There is no per-app token, so any app running under your account can read while access is on. Settings shows connected apps by their self-reported names.
Which AI models does Yogurt use?
Transcription uses Whisper through whisper.cpp, with large-v3-turbo or a smaller model depending on your computer. On supported Macs, Apple SpeechAnalyzer supplies live words while Whisper produces the saved transcript. Summaries and answers use a local open-weight model from the Gemma 4, gpt-oss or Qwen3 families, chosen for your hardware and run through llama.cpp. The app uses Electron and needs no account.
Which languages does Yogurt support?
Pick Multi-language in Settings → Language → Spoken language to transcribe 99 languages. You can also switch from the English menu in a note’s footer before or during recording. English only is the default. Summaries follow the meeting’s main language; answers follow your question’s language. Settings also offers 32 app languages.
Which call apps does Yogurt work with?
You can record calls in any app because Yogurt captures your microphone and system audio. Call detection covers Zoom, Teams and Meet. On Mac, Yogurt can also read their speaker names with Accessibility permission, when the call app shows who is speaking.
How does Yogurt know a call has started?
It checks which apps are using your microphone. For browser calls, it also checks the tab title or a nearby calendar event with a call link. This triggers an offer to record; recording starts only when you choose to.
How do I connect my calendar?
On Mac, allow Calendar access in Settings. Yogurt reads the calendars already on your computer and lets you choose which ones to show. You do not sign into a calendar account in Yogurt.
See Build and run locally for setup, tests and installer builds.
MIT · Copyright 2026 Frigade.
