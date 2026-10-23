---
id: "cfb229afe325758d"
title: "Microsoft’s new voice AI can start working out what you want before you finish speaking"
url: "https://thenewstack.io/microsoft-streaming-speech-models"
link: "https://thenewstack.io/microsoft-streaming-speech-models"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T12:00:00Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Adrian Bridgwater"]
language: "en"
summary: "“I think you said, ‘representative.’” It’s the fastest way to bypass automated speech recognition chatbots that fail to route human callers to the service they need. Achieving a human handoff to a living, breathing representative still feels like a badge of honor. \n\n Microsoft wants to change that dynamic. \n\n Naomi Moneypenny , senior director of product development at Microsoft Foundry Models…"
tags: ["AI Agents", "AI Engineering", "AI Models"]
orgs: ["Microsoft", "Google", "Amazon"]
topics: ["agents & coding", "models & research", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1002
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft’s new voice AI can start working out what you want before you finish speaking

The New Stack · Adrian Bridgwater · 2026-10-23

Microsoft’s new voice AI can start working out what you want before you finish speaking
“I think you said, ‘representative.’” It’s the fastest way to bypass automated speech recognition chatbots that fail to route human callers to the service they need. Achieving a human handoff to a living, breathing representative still feels like a badge of honor.
Microsoft wants to change that dynamic.
Naomi Moneypenny, senior director of product development at Microsoft Foundry Models division, blogged on October 1 to introduce three new Microsoft AI (MAI) models in Microsoft Foundry, Redmond’s app and agent model catalog and platform.
“A voice agent has to do more than hear a request and produce a reply. It has to keep the interaction moving while it listens, reasons, uses tools, and speaks. A delay at either end can turn a conversation into a series of awkward pauses,” writes Moneypenny.
Available now in Microsoft Foundry, the latest voice-centric models include MAI-Transcribe-2-Streaming, which turns live speech into text as it is spoken; MAI-Voice-2.1, an expressive multilingual text-to-speech model; and MAI-Voice-2.1-Flash, optimized for responsive, high-volume voice applications.
Partials drive incremental speech recognition
Instead of waiting for a person to finish speaking before returning text, the technology (which has automatic language detection) produces its first hypotheses (known as partials, associated with the field of incremental speech recognition) within the “low hundreds of milliseconds” of receiving audio. The model then refines the partials as more context arrives, before committing to a stable transcript once an utterance ends.
“A live transcription experience can surface words almost as quickly as they are spoken.”
“That distinction matters when an application needs to act while someone is speaking. A customer-service agent can begin identifying a caller’s request before the sentence is complete. A voice assistant can start reasoning or preparing a tool call sooner. A live transcription experience can surface words almost as quickly as they are spoken,” writes Moneypenny.
MAI-Voice-2.1-Flash is proposed as “a natural fit” for live support agents, voice assistants, and other applications that generate spoken responses. Moneypenny suggests developers can choose MAI-Voice-2.1 when “expressive fidelity” is the priority, or Flash when they need to balance natural speech with responsiveness and cost at scale.
Moneypenny is bullish about the benchmarks thus far. Her post noted that MAI-Transcribe-2-Streaming “debuts at #1 for accuracy” on both partial and final transcripts on the benchmark-based Artificial Analysis leaderboard.
Time for voice to speak up?
All said and done then (pun intended), does this mean that across the spectrum of human-machine input methods, voice is now ready for wider use and adoption? CEO of voice-agent platform company Phonely, Will Bodewes, tells The New Stack he sees these developments positively.
“Voice AI is ready for prime time, if Microsoft’s entry into the market is any indication,” Bodewes says.
Microsoft is hardly new to speech, though: Azure Speech has been on the market for years, and it ships the new MAI models. “For an AI developer, that’s an opportunity to build on that momentum, so expect more players to follow suit. But the model is only the beginning. Voice agents need to learn from every call and measurably improve over time. For companies to see real results, their voice AI must be ready for prime time in theory and in practice.”
“In the early days, a speech request to a hosted model could sit behind a thousand others for 30 seconds, which, on a phone call, is a hang-up.”
From an infrastructure-operations perspective, there’s a clear advancement here. Bodewes, whose company builds its own voice-agent LLM, notes that in the early days (and he means back from the mid 2010s onwards in the initial cloud-based speech API era, such as the Google Cloud Speech-to-Text API, Azure Speech Services, Amazon Transcribe, etc.) a speech request to a hosted model could sit behind a thousand others for 30 seconds, which, on a phone call, is a hang-up.
“We built routing infrastructure just to find the least-loaded endpoints. Owning the model meant owning the queue, and that’s how we got to 120-millisecond responses,” explains Bodewes. “Every sentence you add to a prompt adds another chance of failure. So we enforce the critical steps in code. If an agent needs a name, email, and date of birth before it issues a refund, the codebase guarantees it. Leaving that to the LLM is how you ship incidents.”
The front end (speech) isn’t the hard part
Phonely machine learning researcher Amit Kiran Rege tells The New Stack he agrees the developments are positive, but warns of deeper nuances (speech pun intended, again) in the wider rollout.
“Microsoft shipped the two ends of the voice agent pipeline, speech in and speech out, which tells you it’s betting on a cascade effect for contact centers, the same as we did. But in our work, we found the ends aren’t the hard part. The hard part is the silence in the middle where the model is deciding whether a caller is done or taking a breath before the next word,” explains Rege.
What surprised Phonely when scaling this type of service to millions of calls is that speeding up the data pipeline makes the agent interrupt callers more.
“Microsoft shipped the two ends of the voice agent pipeline, speech in and speech out … But in our work, we found the ends aren’t the hard part.”
“Two-thirds of the time our agent decided to jump in too early, and nobody heard it, because the caller resumed before the first syllable and we canceled the reply. Cut your latency in half, and those become audible interruptions. Thus, the lesson is that latency and turn-taking have to improve together,” cautions Rege.
Talking our way into future interfaces
Microsoft’s position on these technologies states that developers can embrace these same models and toolsets to build customer-service agents, multilingual assistants that recognize a spoken language and reply in a consistent voice, what it defines as “interactive learning experiences that move between languages, speakers, and conversational exercises” and live captions and voice-driven interfaces.
