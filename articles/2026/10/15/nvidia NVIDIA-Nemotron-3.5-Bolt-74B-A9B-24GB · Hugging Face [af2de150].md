---
id: "af2de150ea4eafa2"
title: "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB · Hugging Face"
url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB"
link: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-15T15:04:12Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-LiLiCorr-GGUF NVIDIA Nemotron 3.5 Bolt 74B-A9B 24GB is a vision-language model (VLM) designed to run everyday agentic tasks locally, using a native 2-bit quantization to fit in 24GB of memory and run alongside other applications. It optimizes intelligence…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "OpenAI", "Google", "Hugging Face"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 3928
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6o31q/nvidianvidianemotron35bolt74ba9b24gb_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB · Hugging Face

Hugging Face · jacek2023 · 2026-10-15

Instructions to use nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB", trust_remote_code=True)
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
model = AutoModelForMultimodalLM.from_pretrained("nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB", trust_remote_code=True, device_map="auto")
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB",
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
	}' Use Docker docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
-  SGLang  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB",
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
        --model-path "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB",
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
-  Docker Model Runner  How to use nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB with Docker Model Runner: docker model run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
Description
NVIDIA Nemotron 3.5 Bolt 74B-A9B 24GB is a vision-language model (VLM) designed to run everyday agentic tasks locally, using a native 2-bit quantization to fit in 24GB of memory and run alongside other applications. It optimizes intelligence and speed per GB. It aims to achieve the optimal balance between speed and intelligence, being faster than most popular dense models while smarter than most popular MoE models with a similar memory footprint.
This model is ready for commercial or non‑commercial use.
Model Summary
Model Overview
Model Developer: NVIDIA Corporation
Model Dates: December 2025 - May 2026
Data Freshness:
- The post-training data has a cutoff date of May 2026.
What is Nemotron?
NVIDIA Nemotron™ is a family of open models with open weights, training data, and recipes, delivering leading efficiency and accuracy for building specialized AI agents.
Quick Start
This model requires the following vLLM version or newer. Please use this command.
docker run -it --name vllm --gpus all --ipc=host -p 8000:8000 \
  --entrypoint /bin/bash \
  vllm/vllm-openai:nightly-77154ca6116ae34cbfe314beef1016bde9b63989
pip install b12x
vllm download-kernels
wget https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB/resolve/main/ultra_v3_reasoning_parser.py
export VLLM_USE_V2_MODEL_RUNNER=1
vllm serve nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB \
  --trust-remote-code \
  --load-format auto \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --max-num-seqs 1 \
  --enable-chunked-prefill \
  --kv-cache-dtype fp8 \
  --linear-backend b12x \
  --moe-backend b12x \
  --attention-backend FLASHINFER \
  --mamba-backend flashinfer \
  --mamba-ssm-cache-dtype bfloat16 \
  --mamba-cache-dtype bfloat16 \
  --mamba-cache-mode align \
  --seed 42 \
  --allowed-local-media-path / \
  --limit-mm-per-prompt '{"video":1,"image":1}' \
  --video-pruning-rate 0.5 \
  --media-io-kwargs '{"video":{"fps":2,"num_frames":256}}' \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser-plugin ultra_v3_reasoning_parser.py \
  --reasoning-parser ultra_v3 \
  --speculative-config '{"method":"dflash","model":"nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-LiLiCorr","num_speculative_tokens":7,"rejection_sample_method":"standard","attention_backend":"FLASHINFER","draft_load_config":{"load_format":"auto"}}'
For more details on how to deploy and use the model — see the Quick Start Guide below!
License/Terms of Use
Governing Terms: Use of the models is governed by the OpenMDW License Agreement, version 1.1.
Benchmarks
*The reported MCP-Atlas score for Qwen3.6-35B-A3B-BF16 is 62.8; we measured 51.2 on the 500 public MCP-Atlas tasks.
Deployment Geography: Global
Use Case
Nemotron-3.5-Bolt-74B-A9B-24GB is optimized for use in local agent harnesses and general agentic tasks involving tool calling, web browsing, and terminal use. English and coding languages are the primary languages, with Spanish, French, German, Italian, and Japanese also being supported.
Release Date
Hugging Face 10/15/2026 via https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
Reference(s)
- NVIDIA Nemotron 3 model family on Hugging Face
- NVIDIA Nemotron 3.5 Bolt 74B A9B 24GB Technical Report
- NVIDIA Nemotron 3.5 Bolt 74B A9B 24GB Technical Blog
Model Architecture
- Architecture Type: Mamba2-Transformer Hybrid Mixture of Experts (MoE) with vision encoder
- Network Architecture: Nemotron Hybrid LatentMoE
  - Nemotron 3.5 Super LLM — hybrid Mamba-2 + MoE + Attention backbone
  - C-RADIO v4-H — vision encoder for image and video frames, connected to the backbone through an MLP projector
- Number of model parameters: 74B Total / 9B Active
Model Design
The model was compressed from Nemotron 3.5 Super VL 120B-A12B. The model supports up to 256K tokens of context. The prompt, visual inputs, conversation history, tool results, and generated response share this context window. Individual deployment recipes may use a smaller context window to accommodate the available GPU memory and concurrency.
Training Methodology
Stage 1: Compression
We compress the Nemotron 3.5 Super VL parent checkpoint (120B-A12B) to Nemotron 3.5 Bolt 74B-A9B 24GB using Star Elastic, a push-button, router-guided architecture search and end-to-end compression algorithm invented at NVIDIA.
A budget-conditioned router heterogeneously selects routed-expert counts and MoE intermediate widths across layers, while expert top-K is fixed at 9, down from 22 in the parent model. The router’s architecture search targets a deployment footprint below 24 GB at batch size 1 and 128K context. Its budget already accounts for subsequent quantization and the precision of weights and runtime states (such as 2-bit routed-expert weights and 16-bit SSM states, to name but two, with further details provided in the quantization section). The objective is to find the architecture with the lowest knowledge-distillation loss that satisfies this memory budget, jointly optimizing architecture and model weights through knowledge distillation and a model-size penalty.
Architecture search runs at 8K context, with the router converging during the first 8B tokens. Once the architecture is fixed, recovery continues at 8K to a total of 72B tokens, followed by 48B tokens at 128K context, for 120B tokens overall. Following Star Elastic’s schedule, this takes advantage of faster knowledge recovery at 8K rather than starting directly at 128K, before extending recovery to long contexts.
Stage 2: Vision Adaptor Training:
We constructed the Nemotron 3.5 Bolt 74B-A9B VL model by re-attaching the trained vision tower from the parent Super 3.5 VL model back to the compressed LLM. We then performed lightweight fine-tuning of only the vision-to-language projection layers (the vision adapter), using image-text datasets previously used to train the parent model’s vision adapter. Training used an image-only blend of approximately 6.6M samples per epoch. The blend comprised a general English mix of captioning, visual question answering, counting, and document datasets (~2M samples), CC3M images recaptioned by Qwen3-30B (~1.7M samples), and Chinese document OCR data (~2.5M samples). It also included PDF and table document data, along with datasets used to train NVCLIP OCR. No video or text-only data was used during vision adapter training.
Stage 3: Supervised Fine-Tuning
Post vision-adaptor training, the model is trained with vision heavy SFT training to recover vision capabilities further. Before moving to multi-turn agentic training, we applied checkpoint merging as it provided more well-rounded capabilities across text and vision capabilities. The model was further trained on agentic environments and RLHF, and a final checkpoint merging yielded the final BF16 checkpoint.
For vision, we used dataset blends targeting ScreenSpot Pro (~10.1B tokens) and WebArena (~9.5B tokens), supplemented with small amounts of MolmoWeb/WebVoyager browsing data, CharXiv chart data, HopChain multi-page document data, and BabyVision-targeted reasoning data. For text, we used a downsampled blend of Kimi-K3-generated synthetic datasets targeting the AIME, GPQA Diamond, Terminal Bench 2.1, SciCode, AA-LCR, APEX, and LMArena benchmarks. We also incorporated a very small proportion of GLM 5.2-generated trajectories targeting MCP-Atlas. During this stage, the LLM, vision-adaptor and the vision encoder were all trained.
Following the vision-heavy SFT stage, we performed model merge with the vision adaptor only trained checkpoint using SLERP interpolation. Vision adaptor training and SFT stage with vision heavy dataset is critical to recovering vision benchmarks, as compression was performed only on the text tower of the parent model with knowledge distillation applied to recover text only benchmarks during compression. There is little to no degradation in text accuracy.
Stage 4: Reinforcement Learning
The model was further trained with RLHF and several stages of E2E RL training to improve agentic capabilities and minimize task completion times for tool-heavy multi-turn workloads. During RLHF, we used the Nemotron 3 Ultra GenRM model which was also trained with a reasoning penalty for token efficiency.
For further training, we have used multiple agentic environments with full E2E GRPO to target MCP and SWE tasks. We use 32 prompts with 16 generations per prompt, giving a total of 512 batch size. For the Terminal environment, it was not used for RL training, but it has been used to generate on-policy rollouts to prevent regressions during quantization. Our MCP E2E RL environment includes a simulated MCP-server with tasks requiring multi-turn tool interactions to achieve the goals. Training on this environment improved MCP use capabilities and provided around 8 nominal point increase from ~48 to ~56 on 500 public task subset out of 1000 total tasks on the MCP-Atlas benchmark. The scoring mechanism for the MCP-Atlas benchmark uses a 0.75 threshold on coverage metric, i.e. the mean claim score (each task has multiple claims that are scored separately) and it provides a binary pass / fail score per task coverage in the end. We observed further RL training continued to provide improvement on coverage scores across tasks, but it did not translate to post-threshold based official score improvements. Whether longer RL training would have eventually provided improvements on the benchmark remains an open-question. SWE-RL E2E training also used some optimizations to improve efficiency in terms of generated tokens and tool-call efficiency. Training used 64 prompts with 16 generations per prompt, giving 1,024 trajectories per optimizer step, with a maximum total sequence length of 196,608 tokens. We used Adam at a learning rate of $3 \times 10^{-6}$. This training also led to accuracy and efficiency improvements on PinchBench as a generalization benefit with scores up-to 90.4 across 10-repeat average.
Stage 5: Quantization
We quantize the experts of the model to 2-bits to fit the network in RTX Spark's memory. We use quantization-aware-distillation (QAD) to recover the accuracy. Quantization was performed using Modelopt.To further reduce the size of the network with quantization to 24GB, we quantize all experts to IQ2-XXS, such that each parameter has 2.0625 bits per element (ggml-org). This includes both the routed and shared experts. Previous work on low-bit quantization such as ParetoQ (Liu et al., 2025) and Quest (Panferov et al., 2025) have shown that lower-bits for FC layers could be pareto-optimal, i.e., layers at twice the size in 2 bits are better than the original size in 4 bits. This is a major lever we use to create our for-size checkpoint. In low-batch size inference scenarios, the latency of the kernels also improve linear with the compression rate of the weights, leading to significant inference speed gains due to the low-bit quantization. We performed further mixed-precision to achieve our memory constraint without impacting the capabilities of the model. The model keeps some layers quantized to either NVFP4 (Mamba layers) or Q8_0 (Embedding and output layers).
Nemotron-3.5-Bolt-74B-A9B-24GB is a result of the above work.
Input
- Input Type(s): Image, Video, Text
- Input Format(s):
  - Image: Red, Green, Blue (RGB) (jpeg, png)
  - Video: mp4, up to 2 minutes. For 1080p videos, sample up to 1 FPS / 128 frames. For lower-resolution videos such as 720p, higher temporal sampling such as 2 FPS / 256 frames may be used.
  - Text: String
- Input Parameters:
  - Image: Two-Dimensional (2D)
  - Video: Three-Dimensional (3D)
  - Text: One-Dimensional (1D)
- Other Properties Related to Input: Maximum context length up to 256K tokens. Supported languages include English, French, Spanish, Italian, German, Japanese, Hindi, Korean, Brazilian Portuguese, and Chinese.
Output
- Output Type(s): Text
- Output Format: String
- Output Parameters: One-Dimensional (1D): Sequences
- Other Properties Related to Output: Maximum context length up to 256K tokens. Supports JSON output format, reasoning output with chain-of-thought, and tool calling.
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.
Software Integration
- Runtime Engine(s): vLLM
- Supported Hardware Microarchitecture Compatibility: NVIDIA Blackwell SM120 & SM121
- Supported Operating System(s): Linux
The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.
Model Version(s)
- Nemotron-3.5-Bolt-74B-A9B-24GB
Other variants and drafter models are availble.
Quick Start Guide
vLLM
export VLLM_USE_V2_MODEL_RUNNER=1
vllm serve nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB \
  --trust-remote-code \
  --load-format auto \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --max-num-seqs 1 \
  --enable-chunked-prefill \
  --kv-cache-dtype fp8 \
  --linear-backend b12x \
  --moe-backend b12x \
  --attention-backend FLASHINFER \
  --mamba-backend flashinfer \
  --mamba-ssm-cache-dtype bfloat16 \
  --mamba-cache-dtype bfloat16 \
  --mamba-cache-mode align \
  --seed 42 \
  --allowed-local-media-path / \
  --limit-mm-per-prompt '{"video":1,"image":1}' \
  --video-pruning-rate 0.5 \
  --media-io-kwargs '{"video":{"fps":2,"num_frames":256}}' \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser-plugin ultra_v3_reasoning_parser.py \
  --reasoning-parser ultra_v3 \
  --speculative-config '{"method":"dflash","model":"nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-LiLiCorr","num_speculative_tokens":7,"rejection_sample_method":"standard","attention_backend":"FLASHINFER","draft_load_config":{"load_format":"auto"}}'
API Client
Install the OpenAI-compatible client:
pip install openai
Text and reasoning
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
model = "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB"
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
Tool calling
The model requests a tool call; the application executes it and returns the result. This complete example uses a local inventory lookup.
import json
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
model = "nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB"
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
Dataset Overview
Parent Corpus
The parent NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 model card reports the following foundation and post-training corpus information. Foundation training size is separate from Bolt’s 80-billion-token compression training data described below.
Data Modality: Text, images, and video
Foundation Training Data Size: More than 20 trillion tokens
Foundation Data Collection Period: 2013 to December 2025
Data Collection Method: Hybrid: automated, manually collected, and synthetic
Labeling Method: Hybrid: automated, manually labeled, and synthetic
The foundation corpus contains curated and synthetic text covering English, 19 other spoken languages, and 43 programming languages. Sources include webpages, dialogue, articles, code, and other written materials across math, science, legal, finance, and general knowledge domains.
The post-training corpus includes reasoning, coding, tool use, instruction following, structured outputs, chat, safety, and long-context tasks, together with image and video understanding. Synthetic trajectories are filtered for structural correctness, repetition, and task validity.
Bolt Training
Data Modality: Image, Video, Text Training Data Size: 80 Billion Tokens Dataset partition: Training [100%], testing [0%], validation [0%] Time period for training data collection: 2013 to February 24, 2026 Time period for testing data collection: 2013 to February 24, 2026 Time period for validation data collection: 2013 to February 24, 2026 Data Collection Method by dataset: Hybrid: Automated, Manually-Collected, Synthetic Labeling Method by dataset: Hybrid: Automated, Manually-Labeled, Synthetic
Nemotron 3.5 Bolt 74B-A9B is a compressed version of the NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 model. The below describes the pre-training and post-training methodology used to develop the NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 model. Whereas Super VL had a training data size of more than 20T tokens, Nemotron 3.5 Bolt 74B-A9B has a training data size of 80B tokens.
The NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 language backbone is pre-trained on a large corpus of high-quality curated and synthetically-generated text data. Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including legal, math, science, finance, and more. We also include a small portion of question-answering, and alignment style data to improve model accuracy.
Multimodal training data was assembled from a diverse collection of image, video, and text datasets. Raw datasets were first converted into a standardized JSONL format with unified conversation-turn structure. Image and video datasets were paired with question-answer annotations, often regenerated or refined using large vision-language models to improve quality and consistency. Quality filtering was applied using model-based judges to remove low-quality, unsafe, or off-topic samples. Deduplication and CSAM scanning were performed across all image datasets. Data was then packed into fixed-length sequences for efficient training.
Multiple safety measures were implemented throughout the data pipeline. All image/text datasets underwent CSAM (Child Sexual Abuse Material) scanning, with results tracked per dataset. Content safety filtering was applied using two independent safety judge models to flag and remove samples containing harmful content including weapons references, criminal planning, sexual content involving minors, harassment, hate speech, profanity, threats, violence, or suicide-related content. Synthetic data generation pipelines included explicit quality and safety filtering stages.
The post-training corpus for NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 consists of high-quality curated and synthetically-generated data across text+image, text+video, and text-only samples, structured to support document reasoning, computer use, and long-horizon workflows. During post-training, we generate synthetic data by distilling trajectories, solutions, and translations from strong teacher models and agent systems, often grounded in real tasks or documents and aggressively filtered for quality. Across all pipelines we stack automated verification — compilers, numerical checks, language identification, model-based judges — to ensure our data is high quality.
For all domains, we apply a unified data filtering pipeline to ensure that only high-quality, license-compliant, and verifiable samples are used for post-training. We first discard malformed examples using structural checks (e.g., missing tool definitions when tool calls are present). We then aggressively filter reasoning traces exhibiting pathological repetition, such as repeated n-grams within a sliding window or across the entire trajectory, which we found to be a strong indicator of malformed or low-quality reasoning. Finally, based on internal audits of synthetically generated datasets, we observed that some teacher models occasionally produce reasoning traces and final responses that implicitly align with specific political entities or promote nationalistic narratives. To mitigate this, we apply targeted keyword- and regex-based filters and remove all trajectories matching such behavior.
Prior to training this model, NVIDIA implemented measures to respect EU text and data mining opt-outs by (1) respecting robots.txt instructions to the extent such signals reflect valid rights reservations, and (2) filtering datasets on any actionable metadata identifiers provided by rightsholders.
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
User-Sourced Data (Collected by Provider including Prompts)
No user-sourced data, including user inputs, prompts, or interactions with the AI model, was used to train this model. Data point counts, modality sizes, and provider services/products for this category are not applicable.
NVIDIA-Sourced Synthetic Datasets (Pre-Training)
NVIDIA-Sourced Synthetic Datasets (Post-Training)
Testing Datasets
Data Collection Method by dataset 
- Hybrid: Automated, Manually-Collected, Synthetic
Labeling Method by dataset 
- Hybrid: Automated, Manually-Labeled, Synthetic
Properties: This corpus comprises a mix of high-quality standard benchmarks and test suites for modern multimodal agentic AI. These benchmarks test model capabilities on tasks such as document and chart understanding, GUI grounding, video understanding, tool-calling, and instruction following.
Evaluation Datasets
Data Collection Method by dataset 
- Hybrid: Automated, Manually-Collected, Synthetic
Labeling Method by dataset 
- Hybrid: Automated, Manually-Labeled, Synthetic
Properties: This corpus comprises a mix of high-quality standard benchmarks and test suites for modern multimodal agentic AI. These benchmarks test model capabilities on tasks such as document and chart understanding, GUI grounding, video understanding, tool-calling, and instruction following.
Inference
- Acceleration Engine: PyTorch
- Test Hardware:
  - NVIDIA Hopper H100
  - NVIDIA Hopper H200
  - NVIDIA Blackwell GB200
  - NVIDIA Blackwell GeForce RTX 5090
  - NVIDIA DGX Spark
  - NVIDIA RTX Spark
Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the model output will not blur or maintain proportions of image subjects included.
We advise against circumvention of any provided safety guardrails contained in the Model without a substantially similar guardrail appropriate for your use case. For more details: Safety and Explainability Subcards.
For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here.
- Downloads last month
- 1,137
