---
id: "8ce62867b20076e5"
title: "LTX 2.5 running locally on a 48GB M5 Pro MacBook Pro in TensorSharp’s Video Studio"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9p6cp/ltx_25_running_locally_on_a_48gb_m5_pro_macbook"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9p6cp/ltx_25_running_locally_on_a_48gb_m5_pro_macbook"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T06:12:26Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["fuzhongkai"]
language: "en"
summary: "I maintain TensorSharp , an open-source local inference engine and agent runtime. I’ve added Video Studio to bring local video generation, an editable timeline, and an optional local LLM assistant into the same project. The attached demo runs in TensorAgent on macOS . The actual run Machine: MacBook Pro with an Apple M5 Pro chip and 48GB of memory. Model: LTX 2.5 Distilled, loaded locally.…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 416
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9p6cp/ltx_25_running_locally_on_a_48gb_m5_pro_macbook/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# LTX 2.5 running locally on a 48GB M5 Pro MacBook Pro in TensorSharp’s Video Studio

Reddit · fuzhongkai · 2026-10-19

I maintain TensorSharp , an open-source local inference engine and agent runtime. I’ve added Video Studio to bring local video generation, an editable timeline, and an optional local LLM assistant into the same project. The attached demo runs in TensorAgent on macOS . The actual run Machine: MacBook Pro with an Apple M5 Pro chip and 48GB of memory. Model: LTX 2.5 Distilled, loaded locally. Generation: Image-to-video at 1024 × 1024. Output: 145 frames at 24 fps, approximately 6.04 seconds, with audio enabled. Generation time: 13 minutes 15 seconds. The recording is sped up. The elapsed time is visible in the Jobs panel, and the 48GB figure is the machine’s installed memory. I start with an imported image and ask the character to smile and raise her hand toward her mouth. Once the clip is generated, I add it to the timeline, append the original image as a five-second ending, and render and play the resulting 11.04-second composition . What Video Studio adds Generate and edit in one project. Generated takes stay in the asset library alongside imported video, images, and audio. You can arrange them across multiple tracks, trim and split clips, adjust volume and fades, undo changes, and render an MP4 through FFmpeg. Projects autosave. Use different local video models. Studio connects to TensorSharp’s native pipelines for LTX 2.5 Distilled, MiniMax-H3, and supported Wan 2.1/2.2 checkpoints. First/last-frame conditioning, timed keyframes, and reference-image support depend on the loaded checkpoint. Continue from a clip’s last frame. Use that frame to condition the next generation, then add the new take after the previous one. This helps assemble longer sequences from short generations. Appearance and motion can still drift across segments, and generated audio does not automatically continue across the join. Ask a local LLM to help edit. Beyond what this recording demonstrates, a tool-capable local chat model can inspect the project, propose timeline edits, and plan shots. You review proposed edits before applying them, and they are undoable. The host currently has one active model slot, so switching between the text assistant and video generation is explicit. Generation uses TensorSharp’s native inference engine, and composition/export uses local FFmpeg. With the model weights and media tools installed, this workflow can run without a cloud account. Manual editing also works without a model loaded. GitHub: zhongkaifu/TensorSharp Setup and capability details: Video Studio guide If you’re generating video locally, what would help your workflow most: lower memory requirements, better continuity between shots, or easier management and editing of alternate takes?
