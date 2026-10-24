---
id: "9134c26f4d1d4dac"
title: "Kyutai CADRE: Video Autoencoders That Cut World Model Lag Below 230 ms"
url: "https://marktechpost.com/2026/10/23/kyutai-cadre-video-autoencoders-interactive-world-models"
link: "https://marktechpost.com/2026/10/23/kyutai-cadre-video-autoencoders-interactive-world-models"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T23:26:53Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Kyutai has released CADRE , open causal diffusion representation autoencoders for interactive world models. The Kyutai CADRE video autoencoder targets one problem: action lag. Many world models borrow autoencoders from text-to-video generators. Those autoencoders pack many frames into one latent, so every action waits. Per the research paper , CADRE world models run at 20 fps on 1 H100 and react…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Staff"]
orgs: ["Nvidia", "Hugging Face"]
topics: ["models & research", "robotics & autonomy"]
content_source: "summary"
word_count: 1067
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Kyutai CADRE: Video Autoencoders That Cut World Model Lag Below 230 ms

MarkTechPost · Michal Sutter · 2026-10-23

Kyutai has released CADRE , open causal diffusion representation autoencoders for interactive world models. The Kyutai CADRE video autoencoder targets one problem: action lag. Many world models borrow autoencoders from text-to-video generators. Those autoencoders pack many frames into one latent, so every action waits. Per the research paper , CADRE world models run at 20 fps on 1 H100 and react within 230 ms. 

 TL;DR 

 Size: 7 autoencoders, each about 476M trained parameters plus a frozen 86M DINOv3 ViT-B/16 . The world model is 1.2B parameters. Video runs at 288×512, 20 fps. 

 Runs on: 1 H100 (bf16, batch 1). Quantized variants: Not disclosed. 

 Performance: CADRE forms most of the latency-quality frontier. It is as fast and better in 42 of 48 comparisons with MIRA, Wan 2.2, Cosmos and LTX-2. 

 Best: Driving FVD of 162.6 (CADRE-2×16×16, 1 step) against 599.7 for Wan 2.2. 

 Worst: Robot manipulation action following (ARR) of 0.45 for CADRE-2×32×32, against 0.85 for Wan 2.2. 

 What is CADRE? 

 CADRE is a family of video autoencoders from Kyutai built for action-conditioned world models. A world model generates in the autoencoder’s latent space. So the autoencoder’s compression sets both cost per frame and action delay. 

 Compression is written τ×s×s. τ is frames per latent, and s is the spatial factor. The research gives the latency as τ/f plus generation and decode time. At τ = 8 and 20 fps, the chunk alone adds 400 ms. Humans notice their own movement lagging beyond about 230 ms. 

 How does CADRE work? 

 The encoder reuses the MIRA recipe. A frozen DINOv3 extracts per-patch features from each frame. One trained 3D convolution then compresses them into a 64-channel latent. Only this bottleneck changes between the 7 members. 

 The decoder is a causal diffusion transformer with 24 blocks. It streams chunk by chunk. Progressive self-distillation teaches it to decode in 1 or 2 steps. This happens in a single training stage, without an adversarial loss. 

 The autoencoders train on 23 public video sources, about 76k hours. The mix spans web, robot, driving and game video. 

 How was CADRE evaluated? 

 Kyutai trained the same 1.2B causal diffusion transformer on each autoencoder. It used 4 environments: robot manipulation (ABC), human manipulation (EgoDex), driving (PhysicalAI AV) and indoor navigation (RealEstate10K). Each model sees 2 s of real video, then generates 4.8 s. 

 Scores cover image quality (FID), motion quality (FVD) and action following (ARR). ARR uses a frozen inverse dynamics probe. An ARR of 1 matches real video. 

 &&

 What do the benchmarks show? 

 On one H100, CADRE-2×32×32 reacts in 185 ms and sustains 23.4 fps with 1 decoding step. The Wan 2.2 autoencoder needs 317 ms, LTX-2 492 ms and Cosmos 605 ms. DC-AE is faster at 118 ms but frame-by-frame. 

 The gap is widest with a moving camera. In driving, Wan 2.2 FVD reaches 599.7 and LTX-2 913.3. In indoor navigation, LTX-2 ARR falls to 0.04. Against the retrained MIRA decoder, the 1-step diffusion decoder lowers FVD by 1.4 to 2.5×. 

 What are the 4 findings? 

 Decode by diffusion: at strong compression, perceptual regression blurs, while diffusion samples 1 sharp video. 

 Compress time in the autoencoder: patching inside the world model loses detail. At 8 frames, ARR drops from 0.72 to 0.56. 

 Camera motion decides compression: still cameras tolerate temporal compression. Moving cameras favor fewer frames and coarser spatial tokens. 

 Coarse tokens hurt motion first: in robot manipulation, 32× spatial compression multiplies FVD by 2.4 over 16×. FID barely moves. 

 Comparison: CADRE vs other video autoencoders 

 Feature CADRE-2×32×32 CADRE-2×16×16 MIRA recipe Wan 2.2 VAE Cosmos CV8x8x8 LTX-2 VAE Compression (τ×s×s) 2×32×32 2×16×16 2×32×32 4×16×16 8×8×8 8×32×32 ( paper ) Tokens per 16 frames 1152 4608 1152 2304 4608 288 Decoder Causal diffusion, 1 to 2 steps Causal diffusion, 1 to 2 steps Perceptual regression Causal Causal Non-causal, windowed Action latency, 1 H100 185 ms 216 ms 175 ms 317 ms 605 ms 492 ms Max fps, 1 H100 23.4 17.3 26.6 34.2 39.0 87.4 FVD, driving (lower is better) 171.3 162.6 311.6 599.7 452.5 913.3 FVD, robot manipulation 105.0 47.6 267.1 52.9 39.5 69.6 ARR, robot manipulation (higher is better) 0.45 0.73 0.39 0.85 0.78 0.25 Reconstruction PSNR (OpenVid-HD) 22.86 25.12 24.44 35.02 31.39 28.24 Weights license CC BY-NC 4.0 + DINOv3 License CC BY-NC 4.0 + DINOv3 License Not disclosed Apache 2.0 NVIDIA Open Model License LTX-2 Community License 

 Latency, fpsA, FVD, ARR and PSNR: CADRE paper , Tables 4, 6 and 7. CADRE uses 1 decoding step. All figures are self-reported by Kyutai. 

 Where does CADRE fall short? 

 CADRE does not win everywhere. In robot manipulation, Cosmos posts an FVD of 39.5 against 47.6 for the best 1-step CADRE. At the fast end, DC-AE beats CADRE-1×48×48 in manipulation. Wan 2.2 also reconstructs held-out video far better, at 35.02 dB PSNR. 

 Kyutai team argues reconstruction does not predict rollouts. Wan 2.2 ranks last on indoor rollout FVD. 

 Long latents leave visible seams between chunks. At τ = 8, boundary excess reaches 1.6 to 1.8 across environments. CADRE-4×24×24 is an outlier in navigation, with FVD 403 in driving. Each world model covers one environment at 288×512. Whether findings transfer to generalist models remains open. 

 How can developers use CADRE? 

 The code is MIT licensed. Weights on Hugging Face are CC BY-NC 4.0, so commercial use is excluded. The release covers 7 autoencoders, 4 longer-trained multi-resolution versions and 4 world models on CADRE-2×16×16. A live demo lets you drive them by keyboard. 

 Key Takeaways 

 7 open autoencoders, one bottleneck apart, isolate compression as the only variable. 

 World models on CADRE run at 20 fps on 1 H100, under 230 ms lag. 

 Driving FVD drops to 162.6, against 599.7 for Wan 2.2. 

 Still cameras favor temporal compression; moving cameras favor spatial compression. 

 Weights are non-commercial (CC BY-NC 4.0); code is MIT. 

 Check out the paper , the Kyutai blog , the GitHub repo and the model collection . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Kyutai CADRE: Video Autoencoders That Cut World Model Lag Below 230 ms appeared first on MarkTechPost .
