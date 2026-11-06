---
id: "b81f2f6635786d1a"
title: "Google Releases Gemini Omni 1.2 Flash: 15-Second AI Video at $0.07 per Second"
url: "https://marktechpost.com/2026/11/05/google-gemini-omni-1-2-flash-15-second-video"
link: "https://marktechpost.com/2026/11/05/google-gemini-omni-1-2-flash-15-second-video"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T22:58:21Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google has released Gemini Omni 1.2 Flash , the newest version of its video generation and editing model. Gemini Omni 1.2 Flash generates and edits clips up to 15 seconds natively. It also cuts the price by 30% compared with Omni 1.1 Flash. The model is generally available on Google Cloud and the Gemini API . For developers, the takeaways are longer clips, fewer re-renders and a lower bill per…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["Google", "Hugging Face", "ByteDance"]
topics: ["models & research", "agents & coding", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 879
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Releases Gemini Omni 1.2 Flash: 15-Second AI Video at $0.07 per Second

MarkTechPost · Asif Razzaq · 2026-11-05

Google has released Gemini Omni 1.2 Flash , the newest version of its video generation and editing model. Gemini Omni 1.2 Flash generates and edits clips up to 15 seconds natively. It also cuts the price by 30% compared with Omni 1.1 Flash. The model is generally available on Google Cloud and the Gemini API . For developers, the takeaways are longer clips, fewer re-renders and a lower bill per second. 

 TL;DR 

 Runs on: Google-hosted only (Gemini API, Google Cloud). No open weights, no local deployment. 

 Performance: Google reports better reference adherence and less drift. No 1.2 benchmark scores are published. 

 Best: Native 15-second clips at $0.07 per second of 720p video, about $1.05 per 15-second clip. 

 Worst: Google says fast sports action, rapid script changes and complex physics still need work. 

 What is Gemini Omni 1.2 Flash? 

 Gemini Omni 1.2 Flash is a multimodal video model from Google DeepMind. It takes text, images, short video clips and audio as input. It outputs video with audio. Google’s developer docs describe the Omni line as natively multimodal, with editing handled through the Interactions API. 

 What changed from Omni 1.1 Flash? 

 The launch lists 6 upgrades: 

 Longer clips: Generation and editing now reach 15 seconds, up from 10 seconds in Omni 1.1. 

 Duration control: You set length in 1-second steps from 3 to 15 seconds. 

 Reference adherence: You can combine character, product or style images with motion clips up to 3 seconds. 

 Consistency: Faces, garments, packaging text and brand colors hold across camera angles with less morphing. 

 Speech: Dialogue sounds more natural, with clearer lip-sync and distinct multi-speaker conditioning. 

 Camera control: FPV flythroughs, zoom-outs and orbits show fewer unwanted jump cuts. 

 How does the draft, edit, upscale workflow work? 

 Google frames cost control as a workflow, not just a price. You draft at 360p or 720p. You fix a detail with a follow-up edit instead of regenerating the whole clip. Then you upscale the best result to 1080p or 4K. 

 Multi-turn conversational editing now works across full 15-second clips. In practice, you can swap a product, background, lighting or aspect ratio turn by turn. The docs show this through a previous_interaction_id , so the prior video is not re-uploaded. 

 How much does Gemini Omni 1.2 Flash cost? 

 Google prices Omni 1.2 Flash at $0.07 per second of 720p video . Savings are similar at other resolutions . For context, the pricing page bills Omni 1.1 Flash at roughly $0.10 per second of 720p video. A full 15-second 720p clip on 1.2 works out to about $1.05. 

 Google Vids users can generate 15-second clips at no additional cost. Provisioned Throughput is available, and outputs carry a SynthID watermark. 

 How does it compare with other video models? 

 Feature Gemini Omni 1.2 Flash Gemini Omni 1.1 Flash Veo 3.1 Seedance 2.0 Developer Google DeepMind Google DeepMind Google ByteDance Parameters Not disclosed Not disclosed Not disclosed Not disclosed Max single clip 15 s 10 s 8 s 15 s Duration options 3 to 15 s, 1 s steps Not disclosed 4, 6 or 8 s 4 to 15 s Output resolution 360p, 720p; 1080p and 4K upscaled 360p, 720p; 1080p and 4K upscaled 720p, 1080p, 4K 480p, 720p native Native audio Yes Yes Yes Yes Multi-turn editing Yes, up to 15 s Yes Not listed Not disclosed 720p price $0.07/s About $0.10/s Not listed on source page Token-based, varies Weights Closed, API only Closed, API only Closed, API only Closed, API only 

&&
 -->

 How does it perform on benchmarks? 

 Google has not published benchmark scores for version 1.2. Its claims rest on side-by-side demos against Omni 1.1. The DeepMind model page reports human-rater results for the Omni Flash line, including 1,003 MovieGenBench prompts. In June, an earlier Omni Flash version took #1 on the Arena text-to-video board . Those rankings predate 1.2, so treat them as family context only. 

 Early partner feedback is positive but self-selected. According to Google’s release page, invideo’s VP of Engineering said the model sticks to the prompt and that physics and sound feel real. QuickFrame AI says 15 seconds at 1080p lets users build a full CTV ad in 1 generation. 

 Where can developers use it? 

 Gemini API: Prototype in Google AI Studio and build with the developer docs . 

 Google Cloud: Use the Agent Platform API with enterprise SLAs. 

 Google apps: Flow, Google Vids, Google Ads and the Gemini app (rolling out to AI Ultra). 

 Key Takeaways 

 Gemini Omni 1.2 Flash generates and edits native 15-second clips, up from 10. 

 Price drops 30% to $0.07 per second of 720p video. 

 Multi-turn editing now spans full 15-second clips without re-generation. 

 No benchmark scores for 1.2 are published yet. 

 Audio references remain allowlist-gated on Google Cloud. 

 Check out the launch post , the Google Cloud announcement and the developer docs .. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google Releases Gemini Omni 1.2 Flash: 15-Second AI Video at $0.07 per Second appeared first on MarkTechPost .
