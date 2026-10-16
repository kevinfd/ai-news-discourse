---
id: "e6d4137ccba91a10"
title: "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B model family released (base, NVFP4, BF16, and LiLiCorr speculative decoding)"
url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16"
link: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-15T14:46:04Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jinnyjuice"]
language: "en"
summary: "Instructions to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.\n- Libraries\n-  Transformers How to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with Transformers: # Use a pipeline as a high-level helper\nfrom transformers import pipeline\npipe = pipeline(\"image-text-to-text\",…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "OpenAI", "Google"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 2969
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6nl8m/nvidianvidianemotron35supervl120ba12b_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B model family released (base, NVFP4, BF16, and LiLiCorr speculative decoding)

Hugging Face · jinnyjuice · 2026-10-15

Instructions to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16", trust_remote_code=True)
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForMultimodalLM
model = AutoModelForMultimodalLM.from_pretrained("nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16", trust_remote_code=True, device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}' Use Docker docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
-  SGLang  How to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16",
		"messages": [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": "Describe this image in one sentence."
					},
					{
						"type": "image_url",
						"image_url": {
							"url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
						}
					}
				]
			}
		]
	}'
-  Docker Model Runner  How to use nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 with Docker Model Runner: docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
Description
NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 is the full-precision release of NVIDIA Nemotron 3.5 Super VL, a vision-language model for reasoning, coding, tool use, document understanding, and video understanding. The BF16 weights support customization, domain adaptation, and full-precision evaluation. For optimized deployment, see the NVFP4 release.
The model combines interleaved Mamba-2, Mixture-of-Experts (MoE), and attention layers with a C-RADIO vision encoder and a vision-language connector. It has 120B total parameters and 12B active parameters and supports context lengths up to 1M tokens. Multi-Token Prediction (MTP) enables native speculative decoding.
This model is ready for commercial or non-commercial use.
Model Summary
Model Overview
Model Developer: NVIDIA Corporation
What is Nemotron?
NVIDIA Nemotron™ is a family of open models with open weights, training data, and recipes, delivering leading efficiency and accuracy for building specialized AI agents.
Quick Start
For efficient inference on DGX Spark or data center GPUs, see the NVFP4 card. The example below serves BF16 on 4× H100.
Nemotron 3.5 Super VL has configurable reasoning levels: off, on (medium), and on. Selecting on (medium) will reduce the number of tokens generated compared to on, but may impact accuracy. You can learn about the reasoning budget here!
Use Docker with NVIDIA GPU support and the vllm/vllm-openai:nightly-3f1bcfd82bb2e93fcd364fc7a5491718453a77e2 or (vllm/vllm-openai:v0.32.0) image. If the model requires authentication, set HF_TOKEN in your shell before launching the container.
export MODEL=nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
vllm serve $MODEL \
  --served-model-name nemotron-3.5-super-vl \
  --tensor-parallel-size 4 \
  --trust-remote-code \
  --gpu-memory-utilization=0.85 \
  --allowed-local-media-path=/ \
  --max-num-seqs=32 \
  --limit-mm-per-prompt '{"video": 1, "image": 1}' \
  --video-pruning-rate 0.5 \
  --media-io-kwargs '{"video": {"fps": 2, "num_frames": 256}}' \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser nemotron_v3 \
  --speculative_config.method mtp \
  --speculative_config.num_speculative_tokens 3
Wait for the server to finish loading the model and compiling kernels, then check the endpoint:
curl --fail http://localhost:8000/v1/models
All vLLM and SGLang examples use port 8000 and the API model name nemotron-3.5-super-vl. See the API Client for text, image, video, and tool-calling examples.
License/Terms of Use
Governing Download Terms: Use of this model is governed by the OpenMDW License Agreement, version 1.1.
Benchmarks
We evaluated our model on the following benchmarks:
We evaluated Nemotron 3.5 Super on a comprehensive suite of benchmarks spanning agentic capabilities, reasoning and knowledge, multimodal, conversational ability and instruction following, long-context understanding, and multilingual performance. All evaluation results for Nemotron 3.5 Super and baselines were collected via NeMo Gym. For reproducibility purposes, more details on the evaluation settings can be found in the NeMo Gym recipes folder and the corresponding reproducibility tutorial. The published recipes specify the benchmark-specific containers, prompts, inference parameters, parser configurations, and scoring settings used to produce the results.
There were a few benchmarks that were not yet onboarded in our open source tools, and for these we used either their official open source implementation or an internal scaffolding that we plan to open source in the future: BabyVision, CharXiv-RQ, MathVision, MMLongBench-Doc, OCR-Reasoning, OCRBench-v2, V*, Video-MME-v2.
Agentic Coding Benchmarks
Additional harness-level coding-agent results for SWE-Bench Pro and Terminal-Bench 2.1 are shown below.
Deployment Geography: Global
Use Case
This model is intended for developers who want to customize a post-trained vision-language model, adapt it to domain-specific data, develop quantized variants, or run full-precision inference and evaluation.
Release Date
Hugging Face - 10/15/2026 via Hugging Face
Reference(s)
Model Architecture
- Architecture Type: Mamba-2–Transformer hybrid Mixture of Experts (MoE) with Multi-Token Prediction (MTP)
- Network Architecture: Nemotron Hybrid MoE with 512 routed experts per MoE layer, a C-RADIO vision encoder, and a vision-language connector
- Number of Model Parameters: 120B total / 12B active
Model Design
The model combines sparse expert computation, attention, and Mamba-2 layers to support long-context processing. The vision encoder and connector turn visual inputs into representations processed by the language backbone. A shared MTP head predicts future tokens recursively for speculative decoding.
The model supports up to 1M tokens of context. The prompt, visual inputs, conversation history, tool results, and generated response share this context window. Individual deployment recipes may use a smaller context window to accommodate the available GPU memory and concurrency.
Training Methodology
Stage 1: Foundation and Multi-Token Prediction
The language backbone is initialized from Nemotron 3 Super Base. A shared MTP head is trained for 100B tokens while the backbone remains frozen, followed by 1T tokens of distillation from Nemotron 3 Ultra Base.
Stage 2: Continued Pre-Training and Mid-Training
The model undergoes 100B tokens of Indic continued pre-training, a 35B-token extension to 1M context, 67B tokens of software-engineering mid-training at 256K context, and a final 9B-token long-context recovery stage. Software-engineering data includes repositories, issue–pull-request pairs, commit diffs, build and CI logs, and agent trajectories.
Stage 3: Vision-Language Training
A C-RADIO vision encoder and connector extend the language backbone to visual inputs, including images, document pages, and video frames.
Stage 4: Supervised Fine-Tuning
A two-stage supervised fine-tuning pipeline jointly trains the language and vision components on vision, reasoning, code, tools, chat, safety, and long-context data. Training uses packed sequences of up to 524,288 tokens.
Stage 5: Reinforcement Learning and Distillation
Reinforcement learning with verifiable rewards, reinforcement learning from human feedback, and specialized teacher training improve reasoning, agentic, chat, and vision capabilities. Multi-teacher on-policy distillation consolidates these capabilities into a single model.
Stage 6: MTP Boosting
The MTP head is further trained against the frozen post-trained backbone to improve speculative-decoding acceptance.
Input
- Input Type(s): Text, images, and video
- Input Format(s): Text strings, images, and sampled video frames
  - Video: mp4, up to 2 minutes.
  - Image: Red, Green, Blue (RGB) (jpeg, png)
- Input Parameters: 
  - Video: Three-Dimensional (3D)
  - Image: Two-Dimensional (2D)
  - Text: One-Dimensional (1D)
- Other Properties Related to Input: Maximum context length up to 1M tokens. Documents can be supplied as page images with accompanying text.
Output
- Output Type(s): Text
- Output Format: String
- Output Parameters: One-dimensional sequences
- Other Properties Related to Output: Maximum context length up to 1M tokens.
Our AI models are designed and optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.
Software Integration
- Runtime Engine(s): vLLM; SGLang
- Hardware: 
  - NVIDIA Blackwell
  - NVIDIA Hopper
- Operating System(s): Linux
The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.
Model Version(s)
- v1.0 - GA
Quick Start Guide
Choose your deployment
Speculative Decoding
The serving examples enable the model's native MTP head. No separate drafter download is required for these vLLM and SGLang recipes. In vLLM, num_speculative_tokens controls draft length; in SGLang, the MTP recipe uses EAGLE with speculative-eagle-topk 1.
Performance depends on hardware, request length, and concurrency. To compare with standard decoding, remove the speculative configuration while keeping the model, workload, sampling parameters, and other server settings the same.
vLLM
Use vllm/vllm-openai:nightly-3f1bcfd82bb2e93fcd364fc7a5491718453a77e2 for these commands (or vllm/vllm-openai:v0.32.0). 
4× H100 (up to 1M Context Length)
Use this command if you need to serve the model with up to 1M context length.
vllm serve $MODEL \
  --served-model-name nemotron-3.5-super-vl \
  --tensor-parallel-size 4 \
  --trust-remote-code \
  --async-scheduling \
  --allowed-local-media-path=/ \
  --max-num-seqs 32 \
  --enable-mamba-shared-prefix-checkpoint \
  --limit-mm-per-prompt '{"video": 1, "image": 1}' \
  --video-pruning-rate 0.5 \
  --media-io-kwargs '{"video": {"fps": 2, "num_frames": 256}}' \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser nemotron_v3 \
  --speculative_config.method mtp \
  --speculative_config.num_speculative_tokens 5
2× GB200 (up to 1M Context Length)
Use this command if you need to serve the model with up to 1M context length.
vllm serve $MODEL \
  --served-model-name nemotron-3.5-super-vl \
  --tensor-parallel-size 2 \
  --trust-remote-code \
  --async-scheduling \
  --allowed-local-media-path=/ \
  --max-num-seqs 32 \
  --enable-mamba-shared-prefix-checkpoint \
  --limit-mm-per-prompt '{"video": 1, "image": 1}' \
  --video-pruning-rate 0.5 \
  --media-io-kwargs '{"video": {"fps": 2, "num_frames": 256}}' \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser nemotron_v3 \
  --speculative_config.method mtp \
  --speculative_config.num_speculative_tokens 5
For the multimodal examples, each request can contain one image and one video. The video configuration samples up to 256 frames at 2 FPS with a pruning rate of 0.5. For 1080p videos, use 1 FPS and up to 128 frames; 2 FPS and 256 frames can be used for lower-resolution video such as 720p. Start with short MP4 clips of one to two minutes.
SGLang
Use lmsysorg/sglang:v0.5.20. The example below runs on two GB200 GPUs.
docker run --rm --gpus all --ipc=host \
  -p 8000:8000 \
  -e HF_TOKEN \
  -v "$HOME/.cache/huggingface:/root/.cache/huggingface" \
  --entrypoint sglang lmsysorg/sglang:v0.5.20 \
  serve --model-path "$MODEL_CKPT" \
  --served-model-name nemotron-3.5-super-vl \
  --host 0.0.0.0 \
  --port 8000 \
  --trust-remote-code \
  --tp-size 2 \
  --reasoning-parser nemotron_3 \
  --tool-call-parser qwen3_coder \
  --mamba-ssm-dtype float16 \
  --enable-mamba-cache-stochastic-rounding \
  --mamba-cache-philox-rounds 5 \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 5 \
  --speculative-eagle-topk 1
API Client
Install the OpenAI-compatible client:
pip install openai
Text and reasoning
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
model = "nemotron-3.5-super-vl"
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Explain why binary search takes logarithmic time."}],
    temperature=1.0,
    top_p=0.95,
    max_tokens=16384,
    extra_body={"chat_template_kwargs": {"enable_thinking": True}},
)
choice = response.choices[0]
if choice.finish_reason == "length":
    raise RuntimeError("The response reached max_tokens; increase the output budget.")
print(choice.message.content)
Set enable_thinking to False to disable reasoning. For medium reasoning effort, use {"enable_thinking": True, "medium_effort": True}. Reasoning tokens and the final answer share the max_tokens budget.
Images
Use a multimodal server configuration. The example below sends a local image as a base64 data URL.
import base64
from pathlib import Path
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
image_bytes = Path("image.png").read_bytes()
image_url = "data:image/png;base64," + base64.b64encode(image_bytes).decode()
response = client.chat.completions.create(
    model="nemotron-3.5-super-vl",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Describe the image and any visible text."},
        {"type": "image_url", "image_url": {"url": image_url}},
    ]}],
    temperature=1.0,
    top_p=0.95,
    max_tokens=16384,
)
if response.choices[0].finish_reason == "length":
    raise RuntimeError("The response reached max_tokens; increase the output budget.")
print(response.choices[0].message.content)
Video with vLLM
Use a multimodal vLLM configuration with the video sampling settings above.
import base64
from pathlib import Path
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
video_bytes = Path("video.mp4").read_bytes()
video_url = "data:video/mp4;base64," + base64.b64encode(video_bytes).decode()
response = client.chat.completions.create(
    model="nemotron-3.5-super-vl",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Summarize the events in this video in order."},
        {"type": "video_url", "video_url": {"url": video_url}},
    ]}],
    temperature=1.0,
    top_p=0.95,
    max_tokens=16384,
)
if response.choices[0].finish_reason == "length":
    raise RuntimeError("The response reached max_tokens; increase the output budget.")
print(response.choices[0].message.content)
Tool calling
The model requests a tool call; the application executes it and returns the result. This complete example uses a local inventory lookup.
import json
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
model = "nemotron-3.5-super-vl"
inventory = {"keyboard": 12, "monitor": 5}
tools = [{"type": "function", "function": {
    "name": "get_inventory",
    "description": "Return the inventory count for a product.",
    "parameters": {
        "type": "object",
        "properties": {"product": {"type": "string", "enum": ["keyboard", "monitor"]}},
        "required": ["product"],
        "additionalProperties": False,
    },
}}]
messages = [{"role": "user", "content": "How many keyboards are in stock?"}]
def complete(history, tool_choice="auto"):
    response = client.chat.completions.create(
        model=model,
        messages=history,
        tools=tools,
        tool_choice=tool_choice,
        temperature=1.0,
        top_p=0.95,
        max_tokens=16384,
        extra_body={"chat_template_kwargs": {"enable_thinking": True}},
    )
    choice = response.choices[0]
    if choice.finish_reason == "length":
        raise RuntimeError("The response was truncated; increase max_tokens.")
    return choice.message
message = complete(messages)
messages.append(message.model_dump(exclude_none=True))
if not message.tool_calls:
    print(message.content)
else:
    for call in message.tool_calls:
        arguments = json.loads(call.function.arguments)
        if (call.function.name != "get_inventory"
                or not isinstance(arguments, dict)
                or set(arguments) != {"product"}
                or not isinstance(arguments["product"], str)
                or arguments["product"] not in inventory):
            raise ValueError("Invalid inventory tool call")
        product = arguments["product"]
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": json.dumps({"product": product, "count": inventory[product]}),
        })
    print(complete(messages, tool_choice="none").content)
Training, Testing, and Evaluation Datasets
Training
Data Modality: Text, images, and video
Foundation Training Data Size: More than 20 trillion tokens
Image Training Data Size: 1 Million to 1 Billion Images
Text Training Data Size: More than 10 Trillion Tokens
Video Training Data Size: 10,000 to 1 Million Hours
Foundation Data Collection Period: 2013 to December 2025
Data Collection Method: Hybrid: automated, manually-collected, and synthetic
Labeling Method: Hybrid: automated, manually-labeled, and synthetic
The foundation corpus contains curated and synthetic text covering English, 19 other spoken languages, and 43 programming languages. Sources include webpages, dialogue, articles, code, and other written materials across math, science, legal, finance, and general knowledge domains.
The post-training corpus includes reasoning, coding, tool use, instruction following, structured outputs, chat, safety, and long-context tasks, together with image and video understanding. Synthetic trajectories are filtered for structural correctness, repetition, and task validity.
For more information about the datasets used to train this model, please see the Public Summary of Training Content
Detailed dataset information
Base Pre-Training Corpus (Nemotron 3 Foundation)
The foundation of the model is trained on the Nemotron 3 corpus, comprising the following datasets from the Nemotron Pretraining Datasets collection:
Public Datasets
Crawled and Scraped from Online Sources by NVIDIA
The English Common Crawl data was downloaded from the Common Crawl Foundation (see their FAQ for details on their crawling) and includes the snapshots CC-MAIN-2013-20 through CC-MAIN-2025-13. The data was subsequently deduplicated and filtered in various ways used in the Nemotron-CC data pipeline. Additionally, we extracted data for fifteen languages from the following three Common Crawl snapshots: CC-MAIN-2024-51, CC-MAIN-2025-08, CC-MAIN-2025-18. The fifteen languages included were Arabic, Chinese, Danish, Dutch, French, German, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Swedish, and Thai. As we did not have reliable multilingual model-based quality classifiers available, we applied just heuristic filtering instead—similar to what we did for lower quality English data in the Nemotron-CC pipeline, but selectively removing some filters for some languages that did not work well. Deduplication was done in the same way as for Nemotron-CC.
The GitHub Crawl was collected using the GitHub REST API and the Amazon S3 API. Each crawl was operated in accordance with the rate limits set by its respective source, either GitHub or S3. We collect raw source code and subsequently remove any having a license which does not exist in our permissive-license set.
Private Non-publicly Accessible Datasets of Third Parties
Private Non-publicly Accessible Datasets by NVIDIA
NVIDIA-Sourced Synthetic Datasets (Pre-Training)
NVIDIA-Sourced Synthetic Datasets (Post-Training)
Language Distribution in Post-Training
For our post-training recipe, we focused on the following languages in addition to English: French, German, Italian, Japanese, Spanish, and Chinese. Those languages were represented in the form of multilingual reasoning and translation tasks.
Additional Training Data
Testing Datasets
Data Collection Method: Hybrid: automated, manually-collected, and synthetic
Labeling Method: Hybrid: automated, manually-labeled, and synthetic
Properties: Standard benchmarks and task-specific test suites covering reasoning, coding, tool use, instruction following, long context, and visual understanding.
Evaluation Datasets
Data Collection Method: Hybrid: automated, manually-collected, and synthetic
Labeling Method: Hybrid: automated, manually-labeled, and synthetic
Properties: Standard benchmarks and task-specific test suites covering reasoning, coding, tool use, instruction following, long context, and visual understanding.
Inference
- Acceleration Engine: PyTorch
- Test Hardware: 
  - NVIDIA Hopper
    - H100
    - H200
  - NVIDIA Grace Blackwell
    - GB200
    - GB300
  - NVIDIA Blackwell
    - B200
    - B300
The deployment examples above provide configurations for NVIDIA Hopper and Blackwell systems. Choose the precision, context length, and concurrency appropriate for the application and available memory.
Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
We advise against circumvention of any provided safety guardrails contained in the Model without a substantially similar guardrail appropriate for your use case. For more details: Safety and Explainability subcards. For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, and Privacy subcards.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here.
- Downloads last month
- 2,155
