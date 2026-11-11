---
id: "46e307363c086c72"
title: "Trending on huggingface:2D to 3D"
url: "https://huggingface.co/speridlabs/idol"
link: "https://huggingface.co/speridlabs/idol"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-10T18:17:48Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["R_Duncan"]
language: "en"
summary: "Has dependency on dinov3, is trending top model on hf since last week. Runs with 8GB vram. Enjoy!"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "Nvidia"]
topics: ["chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 501
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsub9f/trending_on_huggingface2d_to_3d/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Trending on huggingface:2D to 3D

Hugging Face · R_Duncan · 2026-11-10

Idol
A single image to a 3D Gaussian splat.
One picture of an object in, up to a million 3D Gaussians out, including the sides the picture never showed.
Idol turns one picture of an object into a 3D Gaussian splat. Give it a render, a generated image or a photo: it removes the background, frames the object and generates up to 1,048,576
Gaussians, written as a standard 3DGS .ply. It runs on consumer GPUs, using 7.2 GB of VRAM and can run in under 2 seconds.
Examples
Idol turns one picture of an object into a 3D Gaussian splat. Give it a render, a generated image or a photo: it removes the background, frames the object and generates up to 1,048,576 Gaussians, including the sides the picture never showed. It runs on consumer GPUs, using 7.2 GB of VRAM and can run in under 2 seconds.
Get started
1. Get access to the image encoders. Idol reads its input through two gated models on Hugging Face. Accept their
terms with your Hugging Face account, then log in once with hf auth login (or set HF_TOKEN):
- facebook/dinov3-vith16plus-pretrain-lvd1689m
- black-forest-labs/FLUX.2-dev (only its VAE is downloaded)
2. Install the code
git clone https://github.com/speridlabs/idol-sdk.git
cd idol-sdk
pip install -e .          # Python 3.10+, PyTorch 2.5+, an NVIDIA GPU with CUDA
There is no separate download step: on the first run, Idol's weights (about 3 GB, from this repository) and the two image encoders download automatically into the Hugging Face cache. If the encoders are not accessible yet, Idol stops before downloading anything and says what is missing.
3. Generate a 3D object
python -m idol.sample --image photo.jpg --mode real
python -m idol.sample --image renders/ --mode synthetic --out outputs
For each image this writes <name>.ply (open it in any Gaussian splat viewer), <name>_input.png (the image the
model saw, after background removal and cropping) and <name>_camera.json (the predicted camera of the input).
Pick the mode for your input. It sets how much room the crop leaves around the object:
From Python:
from idol import IdolPipeline
pipeline = IdolPipeline.from_pretrained("speridlabs/idol")
output = pipeline("photo.jpg", mode="real", seed=42, num_gaussians=1_048_576)
output.gaussian.save_ply("photo.ply")
Flags
Faster sampling is on by default on GPU (~1.7x, same output quality): the denoiser is compiled with torch.compile,
the guided and unguided passes run as one batch, and attention uses cuDNN with TF32 matmuls while sampling. The first
image in a process is slower while it compiles.
More details about the model
Benchmark
Idol, TripoSplat, TRELLIS and LGM, scored at the input view (PSNR, SSIM, LPIPS, IoU) and at seven new views (DINOv2, CLIP, sharpness distance). Mean scores, 1 × H100 per model. Bold is the best in each column.
* LGM has the highest PSNR despite visibly blurry results, because PSNR averages squared pixel error.
Across GPUs
One image to 262,144 Gaussians in 3.4 s. Request time at 50 steps: median over 8 images, with the same code and settings on every GPU, one GPU per machine.
Made with ❤️ by speridlabs.com
- Downloads last month
- 28,250
