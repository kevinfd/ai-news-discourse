---
id: "5ce7944026f130c8"
title: "Huggingface - WOW.. 2 ZeroGPU Spaces for all free accounts?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xqvhua/huggingface_wow_2_zerogpu_spaces_for_all_free"
link: "https://reddit.com/r/LocalLLaMA/comments/1xqvhua/huggingface_wow_2_zerogpu_spaces_for_all_free"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T10:34:10Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Fine_League311"]
language: "en"
summary: "I logged into my Hugging Face account today because one of my old scripts got blocked. The Space was paused with the \"content policy\" message. Okay, fair, it happens. 🤷cause this art of scipts are now ilegal! Then I wanted to make a new Space and saw: Docker = Paid. Great. My old Spaces still run, but new ones? Looked dead. BUT then I looked closer at the create page: Gradio is selectable and…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "Nvidia"]
topics: ["chips & infrastructure", "policy & regulation", "jobs & society"]
content_source: "post"
word_count: 347
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xqvhua/huggingface_wow_2_zerogpu_spaces_for_all_free/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Huggingface - WOW.. 2 ZeroGPU Spaces for all free accounts?

Reddit · Fine_League311 · 2026-11-08

I logged into my Hugging Face account today because one of my old scripts got blocked. The Space was paused with the "content policy" message. Okay, fair, it happens. 🤷cause this art of scipts are now ilegal! Then I wanted to make a new Space and saw: Docker = Paid. Great. My old Spaces still run, but new ones? Looked dead. BUT then I looked closer at the create page: Gradio is selectable and ZeroGPU is marked "Free"! I cancelled PRO last month, so I was like... wait, what? I looked it up. According to the HF docs, a free personal account in good standing (verified email, older than 30 days) can host up to 2 ZeroGPU Spaces for free. My account is pretty old, so it just works. Just Cool! What I found out: ZeroGPU is Gradio only . No Docker, no Streamlit, no own server. Quota is about 5 min GPU per day (older pages say 3.5, the docs now say 5). It resets 24h after your first use. That is a RTX Pro 6000 Blackwell , so for testing and small demos 5 minutes is actually fine. Orgs don't get it. It only works in my personal account, orgs need a Team/Enterprise plan. That's why it didn't show up there. Not every free account sees it. There is a forum thread where someone with a valid free account gets "Paid" anyway, so maybe it's a rollout thing. YMMV. CPU Basic seems gone for new Spaces, only Static is free and unlimited. Also news: Nvidia announced it will buy Hugging Face. I don't know if this has anything to do with the changes, I found nothing saying so. The CPU thing came before the announcement. Now I'm building a small reel maker (SDXL images on ZeroGPU, video assembly on CPU so it costs no GPU time). Will report if it works. 😄 Sources: Official docs: huggingface.co/docs/hub/en/spaces-zerogpu Forum thread (free account still shows Paid): discuss.huggingface.co/t/free-account-31-days-old-email-verified-0-spaces-not-offered-zerogpu-gradio-sdk-gated-as-paid/190930 S ummary: Free personal account = 2 ZeroGPU Gradio Spaces, about 5 min GPU/day (150min/month). Orgs and Docker still need paid.
