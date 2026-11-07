---
id: "6c4e02fb692bfe08"
title: "Oc-e-Non-v1: A language model that gets to the f*cking point"
url: "https://huggingface.co/p-e-w/Oc-e-Non-v1"
link: "https://huggingface.co/p-e-w/Oc-e-Non-v1"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-06T15:23:37Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["-p-e-w-"]
language: "en"
summary: "Richard I of England was called \"Oc-e-Non\" ( Yes and No in Occitan) by some of contemporaries, supposedly because he used few words. Wouldn't it be nice if LLMs followed his shining example? Oc-e-Non-v1 is a tersified version of Qwen3-4B-Instruct-2507. It reduces Qwen's mean response length by 50%.   Output examples   \"What is 1+1?\" GPT-5.6 Terra (reasoning off):     1 + 1 = 2 😊️ Oc-e-Non-v1:…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Alibaba", "Google", "Hugging Face"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1239
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpfhpm/ocenonv1_a_language_model_that_gets_to_the_fcking/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Oc-e-Non-v1: A language model that gets to the f*cking point

Hugging Face · -p-e-w- · 2026-11-06

Instructions to use p-e-w/Oc-e-Non-v1 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use p-e-w/Oc-e-Non-v1 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="p-e-w/Oc-e-Non-v1")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("p-e-w/Oc-e-Non-v1")
model = AutoModelForCausalLM.from_pretrained("p-e-w/Oc-e-Non-v1", device_map="auto")
messages = [
    {"role": "user", "content": "Who are you?"},
]
inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use p-e-w/Oc-e-Non-v1 with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "p-e-w/Oc-e-Non-v1"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "p-e-w/Oc-e-Non-v1",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/p-e-w/Oc-e-Non-v1
-  SGLang  How to use p-e-w/Oc-e-Non-v1 with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "p-e-w/Oc-e-Non-v1" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "p-e-w/Oc-e-Non-v1",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
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
        --model-path "p-e-w/Oc-e-Non-v1" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "p-e-w/Oc-e-Non-v1",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use p-e-w/Oc-e-Non-v1 with Docker Model Runner: docker model run hf.co/p-e-w/Oc-e-Non-v1
Oc-e-Non-v1: A language model that gets to the fucking point
Oc-e-Non-v1 is a tersified version of Qwen/Qwen3-4B-Instruct-2507, made using Heretic v2.1.0.dev0. It reduces Qwen's mean response length by 50%.
You can produce similar models yourself using Heretic's config.terse.toml configuration file.
Richard I of England, called "Oc-e-Non" (Yes and No in Occitan) by some contemporaries,
supposedly because he used few words. (Image from Wikimedia Commons, CC-BY-SA)
Output examples
"What is 1+1?"
GPT-5.6 Terra (reasoning off): 1 + 1 = 2 😊️
Oc-e-Non-v1: 2
"Are dogs mammals?"
GPT-5.6 Terra (reasoning off): Yes. Dogs are mammals: they have hair, are warm-blooded, and mothers nurse their young with milk.
Oc-e-Non-v1: Yes
"Write a Python function that checks if a string contains only capital letters."
GPT-5.6 Terra (reasoning off):
You can use Python's built-in isupper() method to check whether a string contains only capital letters.
def is_only_uppercase(s):
    return s.isupper()
Example usage:
print(is_only_uppercase("HELLO"))  # True
print(is_only_uppercase("Hello"))  # False
print(is_only_uppercase("PYTHON")) # True
print(is_only_uppercase("hello123")) # False
Note: isupper() returns True if the string contains at least one uppercase letter and no lowercase letters. Numbers and special characters are allowed.
Oc-e-Non-v1:
def contains_only_uppercase(s):
    return s.isupper()
Arbitrary-Rank Ablation (ARA) parameters
Performance
Qwen3-4B-Instruct-2507
Highlights
We introduce the updated version of the Qwen3-4B non-thinking mode, named Qwen3-4B-Instruct-2507, featuring the following key enhancements:
- Significant improvements in general capabilities, including instruction following, logical reasoning, text comprehension, mathematics, science, coding and tool usage.
- Substantial gains in long-tail knowledge coverage across multiple languages.
- Markedly better alignment with user preferences in subjective and open-ended tasks, enabling more helpful responses and higher-quality text generation.
- Enhanced capabilities in 256K long-context understanding.
Model Overview
Qwen3-4B-Instruct-2507 has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Number of Parameters: 4.0B
- Number of Paramaters (Non-Embedding): 3.6B
- Number of Layers: 36
- Number of Attention Heads (GQA): 32 for Q and 8 for KV
- Context Length: 262,144 natively.
NOTE: This model supports only non-thinking mode and does not generate <think></think> blocks in its output. Meanwhile, specifying enable_thinking=False is no longer required.
For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our blog, GitHub, and Documentation.
Performance
*: For reproducibility, we report the win rates evaluated by GPT-4.1.
Quickstart
The code of Qwen3 has been in the latest Hugging Face transformers and we advise you to use the latest version of transformers.
With transformers<4.51.0, you will encounter the following error:
KeyError: 'qwen3'
The following contains a code snippet illustrating how to use the model generate content based on given inputs.
from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "Qwen/Qwen3-4B-Instruct-2507"
# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=16384
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 
content = tokenizer.decode(output_ids, skip_special_tokens=True)
print("content:", content)
For deployment, you can use sglang>=0.4.6.post1 or vllm>=0.8.5 or to create an OpenAI-compatible API endpoint:
- SGLang:python -m sglang.launch_server --model-path Qwen/Qwen3-4B-Instruct-2507 --context-length 262144
- vLLM:vllm serve Qwen/Qwen3-4B-Instruct-2507 --max-model-len 262144
Note: If you encounter out-of-memory (OOM) issues, consider reducing the context length to a shorter value, such as 32,768.
For local use, applications such as Ollama, LMStudio, MLX-LM, llama.cpp, and KTransformers have also supported Qwen3.
Agentic Use
Qwen3 excels in tool calling capabilities. We recommend using Qwen-Agent to make the best use of agentic ability of Qwen3. Qwen-Agent encapsulates tool-calling templates and tool-calling parsers internally, greatly reducing coding complexity.
To define the available tools, you can use the MCP configuration file, use the integrated tool of Qwen-Agent, or integrate other tools by yourself.
from qwen_agent.agents import Assistant
# Define LLM
llm_cfg = {
    'model': 'Qwen3-4B-Instruct-2507',
    # Use a custom endpoint compatible with OpenAI API:
    'model_server': 'http://localhost:8000/v1',  # api_base
    'api_key': 'EMPTY',
}
# Define Tools
tools = [
    {'mcpServers': {  # You can specify the MCP configuration file
            'time': {
                'command': 'uvx',
                'args': ['mcp-server-time', '--local-timezone=Asia/Shanghai']
            },
            "fetch": {
                "command": "uvx",
                "args": ["mcp-server-fetch"]
            }
        }
    },
  'code_interpreter',  # Built-in tools
]
# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)
# Streaming generation
messages = [{'role': 'user', 'content': 'https://qwenlm.github.io/blog/ Introduce the latest developments of Qwen'}]
for responses in bot.run(messages=messages):
    pass
print(responses)
Best Practices
To achieve optimal performance, we recommend the following settings:
- Sampling Parameters: 
  - We suggest using Temperature=0.7, TopP=0.8, TopK=20, and MinP=0.
  - For supported frameworks, you can adjust the presence_penalty parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.
- Adequate Output Length: We recommend using an output length of 16,384 tokens for most queries, which is adequate for instruct models.
- Standardize Output Format: We recommend using prompts to standardize model outputs when benchmarking. 
  - Math Problems: Include "Please reason step by step, and put your final answer within \boxed{}." in the prompt.
  - Multiple-Choice Questions: Add the following JSON structure to the prompt to standardize responses: "Please show your choice in the answer field with only the choice letter, e.g., "answer": "C"."
Citation
If you find our work helpful, feel free to give us a cite.
@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}
- Downloads last month
- 760
