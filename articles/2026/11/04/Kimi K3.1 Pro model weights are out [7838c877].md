---
id: "7838c87736f9082f"
title: "Kimi K3.1 Pro model weights are out"
url: "https://huggingface.co/moonshotai/Kimi-K3.1-Pro"
link: "https://huggingface.co/moonshotai/Kimi-K3.1-Pro"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "hackernews"
date: "2026-11-04T15:30:30Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["abrarthought"]
language: "en"
summary: "Instructions to use moonshotai/Kimi-K3.1-Pro with libraries, inference providers, notebooks, and local apps. Follow these links to get started.\n- Libraries\n-  Transformers How to use moonshotai/Kimi-K3.1-Pro with Transformers: # Use a pipeline as a high-level helper\nfrom transformers import pipeline\npipe = pipeline(\"image-text-to-text\", model=\"moonshotai/Kimi-K3.1-Pro\", trust_remote_code=True) #…"
tags: []
orgs: ["DeepSeek", "Anthropic", "OpenAI", "Google"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 1857
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50366999"
score: 563
comments: 162
community: "Hacker News"
---

# Kimi K3.1 Pro model weights are out

Hugging Face · abrarthought · 2026-11-04

Instructions to use moonshotai/Kimi-K3.1-Pro with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use moonshotai/Kimi-K3.1-Pro with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("image-text-to-text", model="moonshotai/Kimi-K3.1-Pro", trust_remote_code=True) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("moonshotai/Kimi-K3.1-Pro", trust_remote_code=True, device_map="auto")
- Inference
- HuggingChat
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use moonshotai/Kimi-K3.1-Pro with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "moonshotai/Kimi-K3.1-Pro"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "moonshotai/Kimi-K3.1-Pro",
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
	}' Use Docker docker model run hf.co/moonshotai/Kimi-K3.1-Pro
-  SGLang  How to use moonshotai/Kimi-K3.1-Pro with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "moonshotai/Kimi-K3.1-Pro" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "moonshotai/Kimi-K3.1-Pro",
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
        --model-path "moonshotai/Kimi-K3.1-Pro" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "moonshotai/Kimi-K3.1-Pro",
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
-  Docker Model Runner  How to use moonshotai/Kimi-K3.1-Pro with Docker Model Runner: docker model run hf.co/moonshotai/Kimi-K3.1-Pro
📰 Tech Blog | 🚀 API Quickstart
1. Model Introduction
Kimi K3.1 Pro is an open-weight, natively multimodal agentic model, and our most capable 3T-class model to date. Post-trained from Kimi K3 with large-scale joint reinforcement learning across hundreds of downstream domains, it is the first model in the K3.1 series. With a 1-million-token context window, Kimi K3.1 Pro delivers substantial improvements in coding, 3D creation, financial research, factual accuracy, and other agentic capabilities.
2. Model Summary
* Compared with Kimi K3, we replace the full-attention Gated MLA layers with Gated DeepSeek Sparse Attention (Gated DSA) layers for more efficient long-context modeling.
3. Evaluation Results
Unless otherwise specified, all Kimi K3.1 Pro results use reasoning effort max, temperature = 1.0, and top-p = 0.95. A dash (—) means that the source table does not report a score. Higher scores are better except where the benchmark name explicitly states lower is better; Elo scores and other benchmark-specific metrics are not directly comparable with accuracy or pass-rate scores.
Evaluation Footnotes
Coding benchmarks
- Terminal-Bench 4.0. Kimi K3.1 Pro is evaluated with the Claude Code harness. The DeepSeek-V4.1-Flash-1017 score is taken from its release blog. All remaining scores are the maximum values reported in model blog posts or on the official Terminal-Bench leaderboard.
- Terminal-Bench-Science 0.1. Kimi K3.1 Pro is evaluated with Claude Code. Internal evaluation of DeepSeek-V4.1-Flash-1017 yields 9.3; the table instead reports 15.7 for the older DeepSeek-V4.1-Flash from the official leaderboard. All remaining scores are from the Terminal-Bench-Science leaderboard.
- SWE-Marathon v1.1. Kimi K3.1 Pro and DeepSeek-V4.1-Flash-1017 are evaluated with Claude Code. Other scores are from the official leaderboard.
- ProgramBench. The table reports binary scores: a task receives 1 if its ProgramBench score is at least 95%, and 0 otherwise. K3.1 Pro is evaluated with Claude Code. DeepSeek and GLM scores are taken from the DeepSeek release blog; remaining scores are from Vals AI.
- DeepSWE v1.1. K3.1 Pro is evaluated with Claude Code. Other scores come from the respective technical reports for GPT-6 Astra, Claude Opus 5.5, Claude Fable 5.1, DeepSeek-V4.1-Flash-1017, and GLM-5.3.
- PostTrainBench. K3.1 Pro and DeepSeek-V4.1-Flash-1017 are evaluated internally on v1.2 with Claude Code and H20 GPUs rather than H100 GPUs. For stable evaluation, all judge models use DeepSeek-V4.1-Flash-1017 at maximum effort, which best matched the official GPT-5.6-Terra (xhigh) judge in testing. Other scores are from the official leaderboard.
- Kimi Code Bench 2.0 and Kimi Code Bench 3.0 Long-horizon. These are internal benchmarks. K3.1 Pro is evaluated with Claude Code; all other models use their maximum-effort setting. Proprietary-model testing may involve fallback behavior.
- BenchCAD. Open models are evaluated on 1,000-case subsets randomly sampled from the 17,900-case Vision2Code dataset at maximum reasoning effort. With-tools results use Claude Code; without-tools results use single-shot generation with official prompts and scoring. Claude scores are from the Opus 5.5 System Card, and GPT-6 Astra's with-tools score is from its official report. GPT-6 Astra has no reported without-tools score.
Agentic benchmarks
- BioMysteryBench. Uses the official v11 release, with Kimi K3 as judge. K3.1 Pro uses Kimi Code; GLM-5.3 and DeepSeek-V4.1-Flash-1017 use Claude Code; GPT-6 Astra uses Codex. Claude scores are from official system cards.
- Agents' Last Exam. Uses the official v1.1 release, comprising 122 tasks, including 86 CLI tasks. Runs that bypass stated requirements receive zero. DeepSeek and Kimi are evaluated with Claude Code and Kimi Code, respectively; other results are from the official benchmark website.
- OfficeQA Pro and OfficeQA Pro v2. GPT-6 Astra uses Codex; other models use Claude Code. Each task provides the complete PDF corpus as page images without machine-readable text. External-model trajectories that retrieve reference answers online receive zero for those tasks.
- Frontier Finance. Evaluated with the official Finance Agent v2 harness.
- HANDBOOK.md. Evaluated with the official OpenHands-based harness, using tasks from the benchmark's early open-source v1 release.
- Harvey Legal Agent. Evaluated on 1,251 public tasks with Artificial Analysis's Stirrup harness. The reported score is the all-pass rate: the percentage of tasks passing every rubric criterion.
- OSWorld V2.1. Kimi models use the Kimi Agent harness in the official OSWorld v2 repository. GPT-6 Astra's score is taken from Muse Wonder's technical report.
- DECK-Arena and Design Bench. DECK-Arena evaluates presentation generation on real-world queries; Design Bench covers graphic design through direct and reference-image few-shot prompting. Both evaluate python-pptx, pptxjs, and Kimi's in-house DSL in a harness with integrated search and image generation. The automated grader is calibrated on more than 10,000 human judgments.
- BrowseComp. Uses context compaction triggered at 200K tokens and a 500-step maximum. If the limit is reached, the agent is forced to answer before judging. All runs use temperature = 1.0 and top-p = 1.0.
- GDPval-AA v2.1, AA-Briefcase v1.1, and AutomationBench-AA. Scores are cited from Artificial Analysis. APEX-Agents. Scores are cited from the official leaderboard.
- Tool-augmented multimodal evaluations. GDP.pdf w/ python, ZeroBench w/ python, and ChartoGraphy w/ python are averaged over five runs; other multimodal benchmarks with Python are averaged over four. For GDP.pdf w/ python, each original PDF is sent to a sandbox for IPython processing. Responses are graded against each rubric criterion using Gemini-3.5-Flash at medium reasoning effort and the official judging prompt. The reported score is the task-macro mean rubric pass rate.
Reasoning, knowledge, and multimodal benchmarks
- GDP.pdf. Each PDF is provided as page images resized to a longest edge of 1,152 pixels, interleaved with Docling-extracted text in page order. Responses are graded against each rubric criterion using Gemini-3.5-Flash Medium and the official judging prompt. The table reports the strict pass rate among fully scored responses. GLM-5.3 Max and DeepSeek-V4.1-Flash-1017 Max scores are cited from Artificial Analysis.
- HLE-Full and HLE-Diamond. The full evaluation sets contain 2,500 and 1,000 questions, respectively. For scores marked *, accuracy is reported on the text-only subset.
- Run counts. GDP.pdf, ZeroBench, and ChartoGraphy are averaged over five runs; other multimodal benchmarks are averaged over four.
- MMMU-Pro. Evaluated using the official protocol, preserving the original input order and prepending images to the text input.
- PerceptionBench. An in-house benchmark focused on atomic visual perception capabilities.
- Kimi Hallucination Benchmark. Evaluates factual accuracy on an internal set of challenging, de-identified prompts drawn from practical work tasks. The table reports claim-level hallucination rates assessed by fact-checking agents.
Cybersecurity benchmarks
- ExploitBench. K3.1 Pro is evaluated with the official harness under a 300-turn budget. The table reports the pass@5 maximum-capability score: for each environment, the best of five seeds is scored by capability flags reached out of 16; arbitrary code execution counts as all 16 capabilities. Comparison scores are from OpenAI, Anthropic, and GLM-5.3.
- ExploitGym. K3.1 Pro is evaluated with Kimi Code under a six-hour wall-clock budget per task. GPT-6 Astra, Claude, and GLM comparison scores are taken from their respective official reports, with Claude results using the same six-hour budget.
- xdev-bench-hard. K3.1 Pro is evaluated with Kimi Code; GLM-5.3 and DeepSeek-V4.1-Flash-1017 use Claude Code. The internal benchmark contains expert-curated, source-code-based vulnerability discovery and exploitation tasks. The final model is evaluated at pass@3 over a random subset of runs, without hard timeouts or output-token limits.
4. Deployment and Availability
You can access Kimi K3.1 Pro's API on https://platform.kimi.ai by selecting kimi-k3.1-pro, and we provide OpenAI/Anthropic-compatible API for you.
Currently, Kimi K3.1 Pro is recommended to run on the following inference engines:
5. Model Usage
The thinking effort of Kimi K3.1 Pro is configured with the top-level reasoning_effort request field, which supports "low", "high", and "max" (default "max").
For multi-turn conversations and tool calls, Kimi K3.1 Pro requires the complete assistant message returned by the API to be passed back to messages as-is — including reasoning_content and tool_calls, not just content:
import openai
def chat_with_preserved_thinking(client: openai.OpenAI, model_name: str):
    messages = [
        {
            "role": "user",
            "content": "Tell me three random numbers."
        },
        {
            "role": "assistant",
            "reasoning_content": "I'll start by listing five numbers: 473, 921, 235, 215, 222, and I'll tell you the first three.",
            "content": "473, 921, 235"
        },
        {
            "role": "user",
            "content": "What are the other two numbers you have in mind?"
        }
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        max_tokens=4096,
        reasoning_effort="max",
    )
    # the assistant should mention 215 and 222 that appear in the prior reasoning content
    print(f"response: {response.choices[0].message.reasoning}")
    return response.choices[0].message.content
For full guides and examples (vision input, structured output, partial mode, tool choice, dynamic tool loading, context caching), see the Kimi K3.1 Pro Quickstart and Thinking Effort.
6. License
Kimi K3.1 Pro is released under the Kimi K3.1 Pro License.
7. Contact Us
If you have any questions, please reach out at support@moonshot.ai.
- Downloads last month
- 11,658
Model tree for moonshotai/Kimi-K3.1-Pro
Spaces using moonshotai/Kimi-K3.1-Pro 4
Evaluation results
- Idavidrein/gpqa · Diamond View evaluation results leaderboard
- harborframework/terminal-bench · Terminalbench 4 View evaluation results leaderboard
- datacurve/deep-swe · Deep Swe View evaluation results leaderboard
- mercor/apex-agents · Apex Agents View evaluation results leaderboard
- harborframework/terminal-bench-science · Terminalbenchscience 0 1 View evaluation results leaderboard
- agents-last-exam/agents-last-exam leaderboard
- Overall Pass Rate View evaluation results
- Ale Cli Pass Rate View evaluation results
