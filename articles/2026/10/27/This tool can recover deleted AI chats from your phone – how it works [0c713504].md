---
id: "0c7135040eb2072d"
title: "This tool can recover deleted AI chats from your phone – how it works"
url: "https://zdnet.com/innovation/orisa-tool-recovers-deleted-local-ai-chats-android-phones"
link: "https://zdnet.com/innovation/orisa-tool-recovers-deleted-local-ai-chats-android-phones"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T16:55:54Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "This new tool proves it’s still best to limit the info you share with chatbots."
tags: ["Artificial Intelligence"]
orgs: []
topics: []
content_source: "fulltext"
word_count: 485
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/bluecubes3GettyImages-2279412518.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# This tool can recover deleted AI chats from your phone – how it works

ZDNet · Radhika Rajkumar · 2026-10-27

ZDNET’s key takeaways
- An experimental tool recovered deleted information from chats.
- It’s helpful for cybersecurity investigations.
- It also demonstrates limitations in perceived local AI security.
How the tool works
Many privacy-conscious AI users prefer to run assistants locally on their devices, because their data isn’t sent out to the cloud, where it could be vulnerable to prying eyes or data breaches. Instead, the chat session uses your device memory.
But, as it turns out, some information from those sessions can stick around in your phone’s working memory even if you’ve deleted the chats themselves. Georgia Tech researchers created ORISA, a tool that searches that memory for clues to deleted conversations. They designed a fake note-keeping AI assistant for their experiment using the ChatterUI Android app, gave it a set of 100 fictional pieces of information about a project, and then deleted that information.
More from ZDNET
Also: You can run local AI on your Android or iOS device
Using ORISA, the researchers then searched the device memory for remnants of that information that could be used as context to restart the session. ORISA found enough usable information to create a new working session with 26 fictional facts from the original set of 100. That’s more than the 14 the original assistant session had access to, “because the rest had fallen outside its active memory,” the researchers explained.
“It can help establish what information someone shared with an AI assistant and what assistance they received,” Ph.D. student Ken Xu, and lead author of the study, said of the experiment.
What it means for you
ORISA was developed to fill a cybersecurity gap. The researchers noted that a downside of local AI is its lack of “centralized logging and enforcement.” That means bad actors can fine-tune models for crimes, for example, and then make the evidence untraceable by deleting them after they’ve used them.
Until now, that reality has made it difficult for investigators using forensic memory techniques to recover useful evidence of that activity.
Also: Lenovo’s RTX Spark laptop passed my completely bonkers AI coding test
“ORISA leverages the batch tokens and key-value (KV) caches preserved in process memory to reconstruct token sequences and restore session-level attention states,” the researchers wrote.
That means a tool like this is most relevant to those trying to stop cybercrime rather than to those digging into your personal data. That said, if hackers recreate a technology like this or get their hands on a tool like ORISA itself, they could theoretically use it to gather deleted information from your chats and recreate your queries using that information as context. But ORISA’s efficacy also depends on time — the researchers noted that it’s harder to recover deleted information as time goes on, because your phone’s memory gets overwritten by newer activity.
Either way, our long-standing advice remains: Don’t share sensitive information with chatbots, even in a local session.
