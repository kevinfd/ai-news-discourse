---
id: "1a5058e6eb20b5d2"
title: "Why Does Voice AI Still Struggle With Kenyans’ Speech?"
url: "https://spectrum.ieee.org/swahili-speech-recognition"
link: "https://spectrum.ieee.org/swahili-speech-recognition"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T12:00:03Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Faustine Ngila"]
language: "en"
summary: "When people read prepared text aloud, AI can transcribe Swahili with remarkably few errors, and Swahili speech recognition looks close to solved. A March 2026 preprint by a team including a Harvard University researcher reports a 3.24 percent word error rate on recordings from Mozilla’s Common Voice collection of volunteer-recorded speech. But Kenyans rarely talk like Common Voice volunteers.…"
tags: ["Natural-language-processing", "Speech-recognition", "Kenya", "Speech-recognition-technology", "Africa"]
orgs: ["Google", "OpenAI", "Anthropic", "Apple"]
topics: ["business & funding", "models & research"]
content_source: "fulltext"
word_count: 1123
paywalled: false
image: "https://spectrum.ieee.org/media-library/three-college-students-posing-together-in-front-of-a-whiteboard-covered-in-writing-from-various-sheng-dialects.jpg?id=68751313&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Why Does Voice AI Still Struggle With Kenyans’ Speech?

IEEE Spectrum · Faustine Ngila · 2026-11-24

When people read prepared text aloud, AI can transcribe Swahili with remarkably few errors, and Swahili speech recognition looks close to solved. A March 2026 preprint by a team including a Harvard University researcher reports a 3.24 percent word error rate on recordings from Mozilla’s Common Voice collection of volunteer-recorded speech.
But Kenyans rarely talk like Common Voice volunteers. They switch between Swahili and English mid-sentence, drop in Sheng slang that changes by neighborhood, speak with accents shaped by their first languages, and contend with public transport noise on low-end handsets.
Another 2026 preprint, which covers 20 African languages, argues that this kind of spontaneous, noisy, overlapping audio exposes a generalization gap that scaling laws built on the English language have not closed.
Voice has become a main interface for many Kenyans, as WhatsApp voice notes and chatbot voice prompts gain popularity in a country that ranks first globally on AI usage. But if an AI model cannot parse everyday speech, it quietly excludes the people it was meant to serve.
“My iPhone’s Siri is unable to follow my voice command in Sheng or Swahili,” says Loise Lionah, a beautician in Nairobi. “ChatGPT tries to understand but gets the meaning wrong. The case is similar with Gemini and Claude.”
Swahili Dialects and Sheng Challenge Voice AI
Swahili, also called Kiswahili, is one of Kenya’s two official languages, alongside English. A Bantu language of the East African coast, Swahili is spoken by more than 200 million people across 14 African countries. Tanzania is regarded as the home of standard Swahili. Yet Catherine Mangare, an AI and computing lecturer at Tanzania’s Sokoine University of Agriculture and a Ph.D. candidate at Okayama University in Japan, says even there, the standard is only the baseline. “Standard Kiswahili is a useful starting point,” she says, “but Tanzanian speech varies by region and setting.”
Sheng, spoken and understood by about 60 percent of Kenyans, adds another layer. The Swahili variant, which emerged among Nairobi’s urban youth many decades ago, follows Swahili grammar but borrows from English, Kenyan mother tongues, and even Hindi, Spanish, and American slang, and it has no standard spelling. Linguists label it a language in constant flux: For example, the Sheng word for “girl” fluctuates according to generation, location, and social media trends.
“Sheng itself is highly broken down per region,” says Tehillah Kachila, founder and CEO of Nairobi-based Zabibu Technika, a startup that builds the Fikra family of Swahili AI models. Kachila says the most recent Sheng dataset dates back to 2019—a major reason, he argues, why prominent voice AI systems struggle to respond accurately to Sheng prompts.
Lilian Wanzare, shown leading a voice-data collection workshop, develops speech datasets for Kenyan languages to help AI systems understand a wider range of speakers.Maseno Centre for Applied AI
Building Speech Data Sets for African Languages
The supply of recorded Swahili speech is growing. The African Next Voices project, supported by a US $2.2 million Gates Foundation grant, has recorded 9,000 hours across 18 languages. Lilian Wanzare, who leads the project’s Kenyan component at Maseno University’s Centre for Applied AI, puts its Kenyan output at roughly 3,000 hours of transcribed speech. Google’s WAXAL corpus, launched in February 2026, adds more than 11,000 hours across 21 African languages, Swahili included.
But hours are not the same as coverage. Gilbert Korir, co-founder and CEO of the Nairobi-based Swahili speech AI startup MsingiAI, says a large dataset can hide limited variation in speakers and recording conditions. The scarcest material is the conversational speech that mixes languages.
That’s why Cynthia Amol, a natural language processing researcher at Maseno University, says her team records unscripted speech. “Unscripted collection helps us capture more nuance and everyday word use, including natural code-switching.”
Why Swahili Trips Up Speech Models
Swahili is agglutinative, meaning words are built from stacked parts. “A single word can carry the negation, subject, tense, object, and action,” Wanzare says. “For example, the word ‘hajafika’ means ‘he has not arrived.’” The same root therefore shows up in many forms, giving models more variation to learn.
Spelling is a second trap. Speech-recognition models learn from recordings paired with written transcripts, so inconsistent spelling can complicate training. And human transcribers often spell borrowed words, Sheng terms, and dialect variants inconsistently; for example, “kompyuta” (the Swahili word for computer) can also appear as “compyuta” or “kompiuta.” In a paper on phonemic transcription for Swahili co-authored by Wanzare, the team addresses a related challenge by developing a pronunciation dictionary that maps written words to speech sounds using a consistent set of symbols.
Mixing languages adds another challenge. “In everyday conversations in Tanzania, people often mix Kiswahili and English, known as Swanglish,” says Okayama University’s Mangare. “A voice system trained mostly on recordings in a single language gets little practice with those switches.” The switch can even fall inside one word, as in “nita-check,” which pairs the Swahili prefix for “I will” with an English verb. In Swahili, Mangare says, “missing even a small part of a verb can change who did something or when.”
Accents add another layer. Mangare notes that someone might say “Kirimanjalo” for Kilimanjaro, or “nchanga” for “mchanga” (the Swahili word for soil). A listener familiar with the accent may understand right away, she says, while a voice system trained mostly on standard pronunciation may miss the word or place name.
And then there’s Sheng. “Sheng is quite dynamic,” Wanzare says. “Words are formed and ‘die’ on a daily basis, which makes data curation for it quite challenging.” Her team’s PolitiKweli dataset, built from social-media text that switches languages, captures the language at one moment in time. “Datasets in Sheng must be living documents that can be updated as the language evolves,” she says. Her group has not yet worked extensively on spoken Sheng.
A member of MsingiAI’s team demonstrates a call with its Nia Voice Agent, which the company has piloted with farmers in western Kenya.MsingiAI
Testing Voice AI Beyond the Benchmarks
Background noise adds to the overall challenge. “Noisy code-switched speech is harder than monolingual speech, because the model has to handle both the noise and the switch between languages at the same time,” Wanzare says. And Korir cautions that suppressing noise can strip out useful speech.
Model performance metrics can also miss what users care about. “A transcript can be mostly correct but get a farmer’s location or a payment amount wrong,” Korir says. Wanzare adds that a single overall benchmark score can hide how models perform across dialects, subject areas, genders, and ages.
For developers building voice AI for Kenya, the priorities are clear: collect conversational speech, treat spelling and dialect as engineering problems, evaluate by task and not by one score, and test under the conditions people actually encounter.
