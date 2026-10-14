---
id: "64950daaf518492b"
title: "OpenAI, Google pushing new AI models easily tricked into making nudes, researchers say"
url: "https://arstechnica.com/tech-policy/2026/10/openai-google-pushing-new-ai-models-easily-tricked-into-making-nudes-researchers-say"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T11:00:30Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Ashley Belanger"]
language: "en"
summary: "Safety researchers continue to warn that a large volume of AI-generated explicit content is spreading unchecked, while regulators do little to meaningfully stop it. \n This non-consensual content is commonly shared in text and direct messages or stored in private clouds where it’s less likely to be detected or reported, a Google co-authored study of Internet users across the United States,…"
tags: ["AI", "Features", "Policy", "ai csam", "AI safety", "ai safety testing", "google", "image generators", "ncii", "openai"]
orgs: ["Google", "OpenAI", "Anthropic", "Hugging Face"]
topics: ["safety & ethics", "policy & regulation"]
content_source: "fulltext"
word_count: 305
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/10/white-circle-red-team-1152x648.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI, Google pushing new AI models easily tricked into making nudes, researchers say

Ars Technica · Ashley Belanger · 2026-10-14

Safety researchers continue to warn that a large volume of AI-generated explicit content is spreading unchecked, while regulators do little to meaningfully stop it.
This non-consensual content is commonly shared in text and direct messages or stored in private clouds where it’s less likely to be detected or reported, a Google co-authored study of Internet users across the United States, Australia, and the United Kingdom found this July. That’s why the “most critical intervention point” remains at the source: the harmful AI tools used to make the fake sexual images, Google researchers concluded.
Yet red-teaming in recent months suggests that as some of the leading AI image generators from Google and OpenAI become more capable, they may be getting worse at blocking explicit outputs.
Raising the red flag are researchers at White Circle, a public benefit corporation backed by senior leaders and researchers from Anthropic, DeepMind, Hugging Face, and OpenAI. It was founded after CEO Denis Shilov posted one of the most famous universal jailbreaks of leading models in October 2024. Bent on breaking models to conduct thorough safety testing, White Circle helps companies detect and deter threats when implementing advanced AI systems that may not always behave as expected.
Testing how well text-to-image models block banned content categories is a key research direction for White Circle, and Shilov thinks their latest findings are “horrifying” enough to share with the public.
Simple to bypass
In a little-noticed preprint published last month, White Circle researchers exposed flaws in the guardrails of DALL·E 3, Google’s Nano Banana 2, and GPT-Image-2. In a press release, they explained that “using just off-the-shelf tools, available online for anyone to download, and by sending API calls, White Circle was able to use the novel attack method to bypass the safety filters” and generate explicit content about 13 percent of the time.
