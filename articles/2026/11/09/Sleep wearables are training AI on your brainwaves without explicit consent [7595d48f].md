---
id: "7595d48fd8a6df79"
title: "Sleep wearables are training AI on your brainwaves without explicit consent"
url: "https://tomshardware.com/peripherals/wearable-tech/wearable-sleep-trackers-are-using-your-brainwaves-to-train-ai-models-without-explicit-user-consent-tens-of-millions-of-hours-of-eeg-data-harvested"
link: "https://tomshardware.com/peripherals/wearable-tech/wearable-sleep-trackers-are-using-your-brainwaves-to-train-ai-models-without-explicit-user-consent-tens-of-millions-of-hours-of-eeg-data-harvested"
source: "Tom's Hardware"
domain: "tomshardware.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T18:29:41Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["rndsignals"]
language: "en"
summary: "Wearable sleep trackers are using your brainwaves to train AI models without explicit user consent — tens of millions of hours of EEG data harvested\n\"We agree users should be explicitly informed\"\nYour sleep data might be doing double duty. While wearable headbands promise to help users understand their sleeping patterns, some of the companies behind them are also turning the electrical signals…"
tags: []
orgs: ["Google", "Meta"]
topics: ["models & research", "search & media", "health & science", "business & funding"]
content_source: "fulltext"
word_count: 1010
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50429502"
score: 25
comments: 1
community: "Hacker News"
---

# Sleep wearables are training AI on your brainwaves without explicit consent

Tom's Hardware · rndsignals · 2026-11-09

Wearable sleep trackers are using your brainwaves to train AI models without explicit user consent — tens of millions of hours of EEG data harvested
"We agree users should be explicitly informed"
Your sleep data might be doing double duty. While wearable headbands promise to help users understand their sleeping patterns, some of the companies behind them are also turning the electrical signals collected from their customers' brains into training material for artificial intelligence models. Science recently conducted an investigation alongside Pulitzer Center's AI Accountability Network and found that the customer neurology companies have accumulated tens of millions of hours of electroencephalography (EEG) recordings — a rather technical way of saying brain-wave data. As per the findings, several are using those recordings to develop so-called brain foundation models, despite initially failing to spell out that use in their privacy policies.
Interaxon, the Canadian firm behind the Muse sleep and meditation headband, is one of them. Its devices monitor electrical activity in the brain, alongside other physiological measurements, while users sleep. The recordings are processed into reports that help customers track their rest and identify changes in their sleeping patterns. But there is another use for that information. Interaxon has already trained an AI model using about 50,000 hours of EEG recording and says it removes identifying information, including names, email, and addresses, before using the data. “We aim to use as much of that eligible corpus as possible,” Nadia Kumentas, its Chief Marketing Officer, said.
That was not made particularly clear to customers, though. Prior to talking to Seince, Interaxon's privacy policy did not explicitly disclose that users' brain recordings could be used to train foundation models. The company has, however, updated the same with Kumentas acknowledging, "We agree users should be explicitly informed." For customers whose recordings had already been used, the classification came late, which likely exposes the company to potential lawsuits. Privacy, it seems, remains a major issue. As per Science, more than two-thirds of the companies studied explicitly allowed corporate transfers of data without user consent. That could be significant if a small neurotechnology firm is acquired, potentially putting its accumulated recordings in the hands of a new owner. Colorado and California, however, have amended their consumer privacy laws to cover neural data, although other states lag behind.
Interaxon isn’t the only company pushing this idea. Emotiv, another wearable EEG maker, is training its Large Brain model partly on recordings from customers using its high-end devices. It also updated its privacy policy following questions by Science, disclosing the use of de-identified neural data for model training subject to opt-in consent.
Notably, the idea behind these systems is particularly different from training a large language model. Instead of feeding AI an enormous amount of text, developers supply it with recordings of electrical activity in the brain. The model then learns recurring patterns that can be adapted to recognize different brain states or assist with specific research tasks. And there are already some interesting results. AI startup Piramidal has trained its model on more than 4 million hours of EEG data in partnership with Cleveland Clinic. The company developed a seizure-detection system that correctly identified nine out of 10 seizures in a pilot study after being fine-tuned on the clinic's recordings. That, however, doesn’t mean consumer headbands can suddenly read people's thoughts. Most wearable EEG devices use just one to six electrodes, considerably fewer than 19 to 25 typically found in clinical EEG systems. Also, their recordings are generally less comprehensive.
That said, the privacy implications of wearable brain technology aren't entirely new. In February, an engineer discovered he could access other people's brainwave recordings through a smart sleep mask he had purchased. He reportedly investigated the device after running into connection problems. By examining its Android application, he discovered hardcoded credentials that appeared to be shared across devices, which he later found were EEG readings belonging to other users.
The industry has also been gathering neural recordings on a considerable scale. Last December, we covered Coundit’s effort to collect 10,000 hours of neural data from thousands of patients. The San Francisco startup built its own headset system to capture brain activity alongside speech and text, with the aim of developing AI capable of translating signals into language. Meta has also been working on BrainQwerty, a non-invasive brain-computer interface that translates brain activity into keyboard inputs. Its second-generation system improved average word accuracy to 61% from 40% in the earlier version, although the technology remains a far cry from practical everyday use.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.
Newton Gitonga is a tech journalist covering gadgets, PC hardware, AI, data centers, and the wider tech industry. His interest in technology started early, taking apart things around the house to see how they worked, often to his dad’s frustration. His curiosity sometimes got the better of him, including a few failed attempts to fix laptops, one of them a gifted Dell XPS. He has previously written for Notebookcheck, ZyCrypto, CoinCentral, and Crypto News Flash.
- bigdragon The article said:Prior to talking to Seince, Interaxon's privacy policy did not explicitly disclose that users' brain recordings could be used to train foundation models. The company has, however, updated the same with Kumentas acknowledging, "We agree users should be explicitly informed." For customers whose recordings had already been used, the classification came late, which likely exposes the company to potential lawsuits. Privacy, it seems, remains a major issue. As per Science, more than two-thirds of the companies studied explicitly allowed corporate transfers of data without user consent.In other words, they'll put it in the terms and conditions after sale. You'll either accept them or have to return the product (if you can). I rarely see any way to opt out of this sort of data harvesting anymore. Companies will do everything they can besides compensating the people whose data they're taking. Reply
