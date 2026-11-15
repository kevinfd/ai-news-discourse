---
id: "c91a7de9e7aaec62"
title: "Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls"
url: "https://marktechpost.com/2026/11/15/bland-tofu-1-full-duplex-speech-to-speech-model"
link: "https://marktechpost.com/2026/11/15/bland-tofu-1-full-duplex-speech-to-speech-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-15T10:06:21Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Bland, the San Francisco voice-AI company, has released Tofu-1 , a full-duplex speech-to-speech model in research preview. The Tofu-1 speech-to-speech model targets calls from moving cars, hospital rooms and weak-signal lines. It listens while it speaks and reasons while it talks. For phone-agent teams, one model now handles audio in and audio out, with no transcript between. You can check the…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff"]
orgs: ["OpenAI", "Nvidia", "Hugging Face"]
topics: ["models & research", "products & launches", "agents & coding", "health & science"]
content_source: "summary"
word_count: 680
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls

MarkTechPost · Michal Sutter · 2026-11-15

Bland, the San Francisco voice-AI company, has released Tofu-1 , a full-duplex speech-to-speech model in research preview. The Tofu-1 speech-to-speech model targets calls from moving cars, hospital rooms and weak-signal lines. It listens while it speaks and reasons while it talks. For phone-agent teams, one model now handles audio in and audio out, with no transcript between. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 What is Tofu-1? 

 Tofu-1 is a full-duplex speech-to-speech model from Bland that hears, reasons and replies in audio during phone calls. It is the first release in a planned family of Bland speech-to-speech models. 

 How does Tofu-1 differ from a cascade voice agent? 

 Most voice agents are cascades. They turn speech into text, pass it to a language model, then turn the reply back into speech. Tofu-1 listens to the audio directly , so tone, hesitation and background sound stay available to the model. Bland has not published the internal architecture. 

 Audio understanding 

 Bland lists 3 audio skills on its product page: 

 Speaker tracking: tells speakers apart and works out who each one is addressing. 

 Noise separation: separates voices from a crying child, a TV, highway traffic, a hospital intercom or keypad tones. 

 Paralinguistics: hears hesitation, frustration and urgency. 

 Full duplex and thinking while talking 

 Callers can interrupt or correct Tofu-1 mid-sentence. While it works on a request, it keeps the conversation moving. It reports the result only when the work is done. It never claims a task is finished early. 

 Scene generation 

 Because Tofu-1 models the sound of a call, it can also produce one. That includes a second speaker, the room around them and line noise. 

 What is Bland’s ‘TV Test’? 

 The TV Test asks one question: can the model follow the caller while ignoring speech from another scene? TV audio is often louder than the caller. Bland marks its TV Test walkthrough as illustrative, not recorded model output. 

 How does Tofu-1 compare with other full-duplex models? 

 Feature Bland Tofu-1 OpenAI GPT-Live-1 NVIDIA NemotronLabs VoiceChat 11B Block Dessa Type Full-duplex speech-to-speech Full-duplex voice model Full-duplex speech-to-speech Full-duplex speech-to-speech Parameters Not disclosed Not disclosed 11B Not disclosed Weights Closed Closed Open (OpenMDW 1.1) Not released Training data Millions of hours of real conversation Not disclosed ~550k hours audio plus text Human speech only, no text Hardware Bland-hosted OpenAI-hosted A100, H100, H200, B100, B200, RTX-6000 MacBook Pro M4 Max or better Turn-taking latency Not disclosed 0.798 s (FDB v1) 448 ms (FDB) Not disclosed Tool use Keeps talking while it works Delegates to backend model Live tool calling, 82.5% tool selection (FDB v3) Not disclosed Access Enterprise research preview API and ChatGPT Hugging Face checkpoint, NVIDIA container Research preview for safety researchers 

 Competitor figures come from each vendor’s own page. FDB results use different benchmark versions and are not directly comparable. 

 How can teams access Tofu-1? 

 Research preview access is open to a limited number of enterprises. Bland names banking, healthcare, insurance and government as target sectors. The sign-up form asks for monthly call volume, from under 1,000 to 50,000+. 

 Key Takeaways 

 Tofu-1 is Bland’s first full-duplex speech-to-speech model, built for noisy calls. 

 It hears audio directly: speakers, background noise and caller emotion. 

 The only number is self-reported: over 92% could not spot it in screenings. 

 No size, latency, pricing or benchmarks yet; rivals publish latency and tool-use scores. 

 Access is a closed enterprise preview, with Bland citing January availability. 

 Check out the Tofu-1 product page , the launch post on X and the research preview sign-up . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls appeared first on MarkTechPost .
