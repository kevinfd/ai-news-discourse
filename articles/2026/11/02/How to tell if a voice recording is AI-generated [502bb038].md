---
id: "502bb03862e6e9b0"
title: "How to tell if a voice recording is AI-generated"
url: "https://scientificamerican.com/article/how-to-tell-if-a-voice-recording-is-ai-generated"
link: "https://scientificamerican.com/article/how-to-tell-if-a-voice-recording-is-ai-generated"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-02T14:15:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["scientificamerican"]
language: "en"
summary: "I can clone my voice in seconds—but there are tricks to help tell real speech from AI"
tags: ["r/artificial"]
orgs: ["Google"]
topics: ["models & research", "search & media", "business & funding"]
content_source: "fulltext"
word_count: 854
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xm9hsx/how_to_tell_if_a_voice_recording_is_aigenerated/"
score: null
comments: null
community: "r/artificial"
---

# How to tell if a voice recording is AI-generated

Scientific American · scientificamerican · 2026-11-02

I’ve long been intrigued by the technology needed to virtually clone my own voice. Just three years ago this effort involved multiple hours of recorded speech and a host of specialized tools to create a quick quote that sounded even remotely like me. Now I can do it with just a few seconds of audio and a couple of clicks—and it takes an expert to recognize that it’s fake.
Why would I do this? I have a background in acoustic analysis, and as the technology has advanced, I’ve been curious to test it and track any tells that reveal the clone as a fake. So last week I again cloned my voice, this time using a free, open-source tool. If that sounds easy, it’s because it is, says Sarah Barrington, a doctoral candidate at the University of California, Berkeley, who studies artificial intelligence voice cloning. At most, a cloning service might ask the user to affirm their right to copy a voice.
“There are platforms online that will advertise as few as three seconds’ worth of someone’s voice to create a clone,” Barrington says. Voice cloning, she explains, went, “kind of overnight, from quite technical to immediately consumer-accessible.” In a demonstration in her lectures, for example, Barrington clones her own voice from a YouTube clip in a mere 90 seconds.
On supporting science journalism
This level of accessibility has drawn the attention of scammers. Reuters reported in September that someone posing as a lawyer and using a cloned voice persuaded a large Italian private bank to wire around €95 million (about $105 million) abroad.
Our ears are, in general, bad at distinguishing between real and cloned voices. Barrington and her colleagues conducted a study where they played real and cloned voices of 220 different speakers to more than 600 listeners. About half of these listeners were asked to flag voices they thought were artificially generated, and they did so successfully 60 percent of the time. In a separate test, when the other half of listeners heard a clone and a real speaker side by side, they judged them to be the same person about 80 percent of the time.
In the past, cloned voices could be discerned based on breaths, pauses and disfluencies such as “ums.” Essentially, the voices were too polished—too unnatural. This is no longer the case. Ums, ahs, breaths and other inflections are now added intentionally to better mask the clone. Researchers are instead training AI models to detect clones based on measurements associated with the sound wave itself, a process involving something called audio forensics.
By zooming in on the waveform of my own voice far enough, I can see each tiny vibration of my own vocal folds as a repetitive bump in signal. Tiny variations in the length of those cycles, known as jitter, and the height of their peaks, known as shimmer, are some of the many features that can be weighed together by a detection model to tell if a voice is AI-generated.
Even the best detectors have blind spots, however. AI models can be tuned to detect the signatures of one cloning company’s tools or perhaps a few, but that ability “often does not transfer well to other providers,” Barrington says. For example, spectral analysis, which visualizes the change in audio frequencies over time, can reveal quirks of particular cloning tools, but there is no single measure that works across all of them.
“You would expect to immediately see giveaways,” Barrington says. “That is absolutely not the case.” In other words, no single measurement can show that a recording is fake. You need a suite of tools. (To further complicate things, a phone call minimizes or degrades much of a voice’s key forensic detail, making clones even harder to spot.)
In my own testing, I compared two dozen sentences that I had spoken and the clone’s versions of the same sentences. Sentences recorded with a heater humming in the background showed that the clone’s jitter was statistically indistinguishable from mine, though its shimmer was steadier. In a quiet room, however, the clone came out measurably cleaner, with less noise under the tone in all 12 sentences, even after a simulated phone call.
For now, one of the most promising ways to distinguish AI-cloned voices from real ones may be embedded in the cloning technology itself. Some companies that make AI audio tools, such as Google, hide an inaudible watermark in the created audio. This watermark makes small changes throughout the sound that are too faint to hear but can be read by a detector later—and these changes go with the audio file wherever it is shared.
These watermarks are powerful, but they are not foolproof; someone might alter a recording enough to erase such a mark. And even when they are available, they may not be required: watermarks are optional on some open-source programs that offer them. Still, Barrington says that, like a locked door, a good watermark can “keep out 99 [percent] of the bad cases.” And for the rest—our audio forensics techniques will have to keep evolving as fast as the cloning tools are.
