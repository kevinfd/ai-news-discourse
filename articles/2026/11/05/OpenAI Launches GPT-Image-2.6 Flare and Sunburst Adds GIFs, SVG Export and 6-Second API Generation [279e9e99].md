---
id: "279e9e999639b209"
title: "OpenAI Launches GPT-Image-2.6 Flare and Sunburst: Adds GIFs, SVG Export and 6-Second API Generation"
url: "https://marktechpost.com/2026/11/04/openai-gpt-image-2-6-flare-sunburst"
link: "https://marktechpost.com/2026/11/04/openai-gpt-image-2-6-flare-sunburst"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T07:03:17Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "OpenAI just shipped Images 2.6 across ChatGPT, Codex and the API. For developers, the core release is GPT-Image-2.6, shipped as two API models: Flare and Sunburst. OpenAI team states that Images 2.6 generates images 50% faster than before. The update also adds GIF output, SVG export, markup-guided edits and a new complexity parameter. \n\n TL;DR \n\n Size: Closed weights, token-billed image API. \n\n…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["OpenAI", "Google", "Hugging Face"]
topics: ["products & launches", "models & research", "agents & coding"]
content_source: "summary"
word_count: 880
paywalled: false
image: "https://www.marktechpost.com/wp-content/uploads/2026/11/Static_01_animate-gifs-scaled.png"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI Launches GPT-Image-2.6 Flare and Sunburst: Adds GIFs, SVG Export and 6-Second API Generation

MarkTechPost · Asif Razzaq · 2026-11-05

OpenAI just shipped Images 2.6 across ChatGPT, Codex and the API. For developers, the core release is GPT-Image-2.6, shipped as two API models: Flare and Sunburst. OpenAI team states that Images 2.6 generates images 50% faster than before. The update also adds GIF output, SVG export, markup-guided edits and a new complexity parameter. 

 TL;DR 

 Size: Closed weights, token-billed image API. 

 Runs on: OpenAI-hosted only (ChatGPT, Codex, API). 

 Performance: 50% faster image generation than the previous release, per OpenAI. 

 Best: Flare can return an image in as little as 6 seconds at low quality. 

 Worst: No benchmark scores and no per-image cost table published for 2.6. 

 image source: openai 

 What is GPT-Image-2.6? 

 GPT-Image-2.6 is OpenAI’s image generation and editing model family for the API. It accepts text and image inputs and returns images. GPT-Image-2.6 Flare is built for fast iteration and interactive workflows. GPT-Image-2.6 Sunburst is built for detailed compositions and editing. 

 OpenAI states that Flare can generate images in as little as 6 seconds when quality is set to low. Sunburst targets higher quality and stronger consistency across edits at medium or high quality. 

 What changed in ChatGPT Images 2.6? 

 ChatGPT users can now turn a prompt or a photo into an animated GIF. They can adjust animation speed, edit individual frames and share the result. Users can also save and tag reference images of people, pets and characters. Those references can be reused later without uploading them again. 

 Usage keeps climbing. OpenAI says people now generate more than 4B images per week across ChatGPT and the API. That is up from more than 3B per week 8 weeks earlier, at the Images 2.5 launch. On average, that is over 500M images per day. 

 How does the new complexity parameter work? 

 The complexity field sets how much the model plans before it renders. The image generation guide lists 3 levels: low, medium and high. If you omit it, both models use high. 

 Low suits focused edits, such as changing a background or a sign. High helps with dense text, complex layouts and relationships between objects. OpenAI warns that higher complexity can add latency and introduce unwanted changes. Adjusting complexity has no separate fee. It is separate from quality , which controls rendering detail and fidelity. 

&&

 Markup edits, SVG and GIF output in the API 

 Image markup lets you mark up the exact region you want changed. The launch post says markup is coming to the API. The guide already lists markup-guided edits as supported for both models. It also lists SVG output and animated GIF output through the Image API. 

 SVG matters for icons, diagrams and UI assets that must scale without blur. GIF output removes a separate animation step for social and product teams. 

 How much does GPT-Image-2.6 cost? 

 Pricing is token-based and identical for Flare and Sunburst, per the model pages : 

 Text input: $5.00 per 1M tokens ($1.25 cached) 

 Image input: $8.00 per 1M tokens ($2.00 cached) 

 Image output: $30.00 per 1M tokens 

 How does GPT-Image-2.6 compare with Nano Banana 2.1 and FLUX 3 Image? 

 Feature GPT-Image-2.6 Flare / Sunburst GPT-Image-2.5 Flare / Sunburst Google Nano Banana 2.1 BFL FLUX 3 Image Released Nov 4, 2026 Sep 8, 2026 Oct 2026 Oct 1, 2026 Parameters Not disclosed Not disclosed Not disclosed Not disclosed (Klein: 5.6B ) Weights Closed Closed Closed Closed (Klein open, FLUX Kommunity License) Planning control complexity: low / medium / high Not disclosed Thinking: minimal / medium / high Bounding boxes in prompt Max reference images Not disclosed Not disclosed 14 10 Max output Not disclosed Not disclosed 4K 4K (about 16 MP) GIF output Yes Not disclosed Not disclosed Not disclosed SVG output Yes Not disclosed Not disclosed Not disclosed Pricing $8 / $30 per 1M image in / out $8 / $30 per 1M image in / out $0.0336 per 1K image $0.048 per 1K image Speed claim Flare: 6 s minimum at low quality Flare: up to 50% lower latency vs GPT-Image-2 Not disclosed Not disclosed 

 Google and BFL publish per-image prices. Nano Banana 2.1 starts at $0.0336 per 1K image and reaches $0.113 at 4K. FLUX 3 Image starts at $0.048 per 1K image and reaches $0.607 at 4K. Its open-weight sibling, FLUX 3 Image Klein, runs on consumer GPUs down to an RTX 3090. OpenAI’s edge is native GIF and SVG output. Its gap is transparency on per-image cost and quality. 

 Key Takeaways 

 Flare returns images in as little as 6 seconds at low quality. 

 Sunburst targets detail and edit consistency at medium or high quality. 

 New complexity parameter (low, medium, high; default high) costs nothing extra. 

 Token prices match GPT-Image-2.5: $30 per 1M image output tokens. 

 Check out the launch post , the Flare model card , the Sunburst model card and the image generation guide . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post OpenAI Launches GPT-Image-2.6 Flare and Sunburst: Adds GIFs, SVG Export and 6-Second API Generation appeared first on MarkTechPost .
