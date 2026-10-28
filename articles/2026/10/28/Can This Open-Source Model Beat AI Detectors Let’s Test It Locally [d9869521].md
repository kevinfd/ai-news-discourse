---
id: "d9869521c826dafa"
title: "Can This Open-Source Model Beat AI Detectors? Let’s Test It Locally"
url: "https://kdnuggets.com/can-this-open-source-model-beat-ai-detectors-lets-test-it-locally"
link: "https://kdnuggets.com/can-this-open-source-model-beat-ai-detectors-lets-test-it-locally"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-28T12:00:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Abid Ali Awan"]
language: "en"
summary: "Can a free, open-source AI humanizer beat paid tools? We tested a 12B model locally and compared the results against AI detectors to see if the hype is real."
tags: []
orgs: ["Nvidia", "Hugging Face", "Google"]
topics: ["models & research", "chips & infrastructure", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1335
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/awan_opensource_model_beat_ai_detectors_let_test_locally_7.png"
discussion_url: null
score: null
comments: null
community: null
---

# Can This Open-Source Model Beat AI Detectors? Let’s Test It Locally

KDnuggets · Abid Ali Awan · 2026-10-28

Can This Open-Source Model Beat AI Detectors? Let’s Test It Locally
Can a free, open-source AI humanizer beat paid tools? We tested a 12B model locally and compared the results against AI detectors to see if the hype is real.
You do not need to pay for an expensive subscription to rewrite AI-generated content anymore. Open-source models like Humanizer let you do it locally, without monthly fees, API costs, or sending your writing to a third-party service. The model is gaining attention in the open-source community, with more than 143,000 downloads and 2,100 likes reported on Hugging Face in early October 2026. Its developer also claims that 95% of 210 rewritten English drafts were classified as human-written by Originality.ai, although that result has not been independently verified.
In this tutorial, we will download the 12-billion-parameter Humanizer model, run it locally on a Linux machine using llama.cpp with NVIDIA CUDA support, and use it to rewrite AI-generated text. We will then test the results against popular AI detectors, including Originality.ai, GPTZero, and Copyleaks, to see whether this free, open-source alternative can actually deliver on its claims.
Understanding the Humanizer Model
Humanizer is an open-source, 12-billion-parameter model built on Google's Gemma 4 12B. Unlike general-purpose language models, it is specifically fine-tuned to rewrite AI-generated content into more natural, human-like writing while preserving the original meaning, facts, and important details.
The model was trained on 28,598 pairs of AI-generated drafts and real human-written text, collected from sources such as academic papers, government reports, emails, Reddit, and Hacker News. It first learned to transform AI-written drafts into human-like text through supervised fine-tuning. The developers then used Direct Preference Optimization with 3,918 preference pairs, followed by Group Relative Policy Optimization, where a large language model (LLM) judge evaluated rewrites for factual accuracy, unnecessary copying, and changes in meaning.
When you provide a draft, Humanizer rewrites the wording, adjusts sentence structure, removes repetitive AI-style phrasing, and varies sentence length while trying to keep the original information intact. Interestingly, the developers did not use AI detectors during training. Instead, they focused on improving writing quality and factual consistency.
According to the developer's evaluation, 95% of 210 English rewrites were classified as human-written by Originality.ai, while the quantized Q8_0 version achieved approximately 93%. These results are developer-reported, and the model can still introduce factual errors or perform differently across detectors.
You can also download the desktop application for Windows and macOS and run it offline without writing any code. For advanced users, Humanizer supports llama.cpp, Ollama, Transformers, MLX, and vLLM.
In this tutorial, we will run the Q8_0 model locally on Linux using llama.cpp with NVIDIA CUDA support.
1. Install llama-server with CUDA
First, we need to set up llama.cpp, an open-source inference engine that lets us run LLMs locally without relying on cloud APIs. We will use its llama-server component to serve Humanizer through a local HTTP API. Since our Linux machine already has NVIDIA CUDA installed, we can build llama.cpp with GPU acceleration to make text generation faster.
Clone the llama.cpp repository and build the server with CUDA support:
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release --target llama-server -j
Once the build is complete, verify the installation:
./build/bin/llama-server --version
Output:
built with GNU 13.3.0 for Linux x86_64
2. Download and Run Humanizer
Next, we will download the 8-bit quantized version of Humanizer from Hugging Face. Quantization reduces the model's memory requirements, making it easier to run on consumer GPUs without loading the full-precision weights. We will use the Q8_0 version, which offers a good balance between model quality and memory usage, and then launch it using llama-server.
Install the Hugging Face CLI:
pip install -U huggingface_hub
Download the model weights and prompt configuration:
hf download jialinyyzz/humanizer \
  humanizer-12b-Q8_0.gguf prompt_format.json \
  --local-dir ./humanizer-model
The Q8_0 model requires substantial GPU memory. If your GPU has less VRAM available, you can try the smaller humanizer-12b-Q6_K.gguf version instead.
Start the server:
./build/bin/llama-server \
  -m ./humanizer-model/humanizer-12b-Q8_0.gguf \
  -c 8192 \
  -np 1 \
  -ngl 99 \
  -fa on \
  -b 2048 \
  -ub 512 \
  -t 8 \
  --host 127.0.0.1 \
  --port 8910
Here, -ngl 99 offloads all model layers to the GPU, -c 8192 sets the context window, and -fa on enables Flash Attention. The server runs on port 8910 and is accessible only from the local machine.
Open another terminal and check whether the model is available:
curl -s http://127.0.0.1:8910/models
If the server returns the loaded model information, Humanizer is ready to accept requests.
3. Rewrite AI-Generated Text
Now that Humanizer is running locally, we can test it on AI-generated content. We will create a short article, send it to the model through the local API, and save the rewritten version to a text file. The model uses a specific prompt format to guide the rewriting process, so we will load the official configuration rather than writing our own instructions.
First, create a file called draft.txt and add an AI-generated article of around 200 words. For this experiment, we used an article about running AI models locally, which GPTZero flagged as 100% AI-generated, as shown in the screenshot below.
Next, create a Python file called humanize.py:
import json
import urllib.request
# Load prompt and article
pf = json.load(open("humanizer-model/prompt_format.json"))
draft = open("draft.txt").read().strip()
# Model settings
body = {
    "prompt": pf["instr"] + "\n\n" + draft + pf["sep"],
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 0,
    "min_p": 0,
    "repeat_penalty": 1.0,
    "n_predict": 2048,
    "seed": -1,
}
# Generate humanized text
req = urllib.request.Request(
    "http://127.0.0.1:8910/completion",
    json.dumps(body).encode(),
    {"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=600) as response:
    result = json.load(response)["content"].strip()
# Save output
with open("humanized.txt", "w") as f:
    f.write(result)
print(result)
The script loads the original draft, combines it with the model's recommended instructions, and sends it to the local llama-server. We use a temperature of 1.0 and a top_p of 0.95, following the developer's recommended generation settings. The rewritten text is then saved automatically.
Run the script:
python3 humanize.py
The rewritten article will appear in your terminal and will also be saved as humanized.txt.
We then tested the rewritten article using GPTZero, and the results were quite promising. The AI detection score dropped from 100% to 49%, while the human-written score increased to 51%. GPTZero was uncertain about the text but indicated that it would likely be considered human-written. This shows a noticeable improvement after running the article through Humanizer, although results may vary with different content and detectors.
Final Thoughts
After testing Humanizer on multiple AI-generated articles, I found the results to be quite hit or miss. Sometimes, the rewritten content was classified as human-written, while other times, detectors still flagged it as AI-generated. Based on my testing, it felt like a 50-50 chance of getting a good result.
I am not entirely sure why the results were so inconsistent. I followed the instructions from the official repository, used the recommended settings, and ran the model locally. Even then, I could not consistently reproduce the developer's reported results.
But there is another issue here: AI detectors are not always reliable. They can produce false positives, sometimes flagging text as AI-generated even when a human wrote every word. This makes it difficult to judge how effective a humanizer really is based on detector scores alone.
Overall, I can see why Humanizer is getting so much attention. You can download it, run it locally, and rewrite content without paying for expensive subscriptions or API calls. It is an interesting open-source alternative, even if the results are not always consistent. I would recommend trying it yourself, reviewing the rewritten text for accuracy, and not relying too heavily on AI detection scores.
 
Abid Ali Awan (@1abidaliawan) is a certified data scientist professional who loves building machine learning models. Currently, he is focusing on content creation and writing technical blogs on machine learning and data science technologies. Abid holds a Master's degree in technology management and a bachelor's degree in telecommunication engineering. His vision is to build an AI product using a graph neural network for students struggling with mental illness.
