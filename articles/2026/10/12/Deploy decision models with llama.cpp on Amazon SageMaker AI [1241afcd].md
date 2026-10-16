---
id: "1241afcd37b68e81"
title: "Deploy decision models with llama.cpp on Amazon SageMaker AI"
url: "https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai"
link: "https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-12T15:51:46Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Jyothirmai Kottu"]
language: "en"
summary: "Applications that route requests, select agent actions, or assign policy outcomes often need scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrastructure. \n This post continues a series on specialized AWS Deep Learning Containers (DLCs) for…"
tags: ["Advanced (300)", "Amazon SageMaker AI", "Technical How-to"]
orgs: ["Amazon", "OpenAI", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 1614
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Deploy decision models with llama.cpp on Amazon SageMaker AI

AWS Machine Learning Blog · Jyothirmai Kottu · 2026-10-12

Artificial Intelligence
Deploy decision models with llama.cpp on Amazon SageMaker AI
Applications that route requests, select agent actions, or assign policy outcomes often need scores over a fixed set of choices instead of free-form text. Deploying these decision models with llama.cpp on Amazon SageMaker AI gives you a managed path for serving quantized models on CPU or GPU infrastructure.
This post continues a series on specialized AWS Deep Learning Containers (DLCs) for generative AI inference. Previous posts cover WhisperX, vLLM-Omni – Part 1, and vLLM-Omni – Part 2.
In this post, you first use the AWS DLC for llama.cpp to serve OpenAI-compatible chat completions through SageMaker AI InvokeEndpoint. You then extend the same runtime with SemIf, formerly OpenJev, which returns probabilities over declared options without decoding an answer token. The accompanying code sample includes CPU and GPU deployment options.
Solution overview
Figure 1 shows two deployment paths from the same packaged model. The text-generation path uses the AWS DLC for llama.cpp and returns generated responses through the OpenAI-compatible API. The structured-decision path builds a child image that replaces the default server with a SemIf adapter and returns probabilities for declared options.
For the standard path, package the model as model.tar.gz in Amazon Simple Storage Service (Amazon S3) and reference the published DLC image directly. The container finds the first .gguf file under /opt/ml/model, maps POST /invocations to llama-server at /v1/chat/completions, and passes SM_LLAMA_CPP_* environment variables to llama.cpp arguments.
The llama-server HTTP API doesn’t expose the final-position logits and state operations that SemIf uses. The structured-decision path therefore uses AWS CodeBuild to build a child image and store it in Amazon Elastic Container Registry (Amazon ECR). The child image keeps the DLC’s compiled CPU or CUDA libraries while replacing its entry point with a SageMaker-compatible adapter.
Understand the input and output schemas
The AWS DLC for llama.cpp accepts the OpenAI Chat Completions schema. Send a messages array with role and content, plus generation controls such as max_tokens and stream:
The response uses the OpenAI-compatible choices array. Read generated text from choices[0].message.content.
SemIf uses a constrained decision schema instead of chat messages. The request contains a caller-defined ID, unstructured state, a question, and an ordered list of allowed options:
The response returns option_ids, probabilities, and raw option_logits in the same order, along with prompt, timing, and pinned model metadata. With stable option IDs, your application can apply thresholds, fallbacks, and policy checks without parsing generated prose.
SemIf belongs to a broader class of decision models that score application-defined outcomes from unstructured state. Other implementations include Jev, TypeSafe’s decision model and /v1/systemone API; Kev, a model server designed for TypeSafe API compatibility; and Strands Decider 2B, a purpose-built model for agent workflows with calibrated outputs.
Choose the right decision workflows
Use this pattern when your application defines the allowed choices at request time and needs a model to interpret unstructured context. Examples include routing a case to a queue, extracting one value from a known set, assigning an incident priority, checking a policy outcome, or selecting an agent action. Keep authorization and deterministic business rules outside the model, and validate model probabilities before treating them as operational confidence.
Use the standard SageMaker AI text-generation path when you need OpenAI-compatible chat completions through InvokeEndpoint. The SageMaker AI image maps POST /invocations to the llama-server /v1/chat/completions endpoint. Build a child image only when your application needs behavior that this interface doesn’t provide, such as SemIf’s direct logits and state access.
Removing answer-token generation doesn’t remove model inference. The model still processes the complete state, question, and option descriptions before SemIf reads the final logits. Keep prompts focused, and evaluate the selected model with labeled decisions from your application before production use.
Tune for your latency and quality targets
The following benchmark applies to the SemIf extension, not the text-generation endpoint. Model size, quantization, prompt length, runtime, and CPU thread count affect each decision. To quantify these trade-offs, we sent the same 231 public JevBench tasks serially to one CPU endpoint and one GPU endpoint.
Compared with the CPU configuration, the GPU endpoint was 4.9 times faster at p50 and 32.2 times faster at p95. The sample uses the SageMaker AI instance pools feature to list compatible GPU instance types in priority order, so SageMaker can select an alternative when the first preference isn’t available. The pool ordered g6e, g6, g5, then g4dn. SageMaker selected ml.g6e.xlarge, and startup logs confirmed that llama.cpp offloaded all 34 model layers to an NVIDIA L40S. The CPU and GPU images used different llama.cpp builds and produced different predictions on six hard tasks. Treat the one-answer accuracy difference as runtime variation, not evidence that GPU offload improves model quality.
Smaller models reduced median latency, but the 2B and 0.8B candidates achieved 66.7 percent and 58.4 percent accuracy. The sample therefore keeps the 4B Q4_K_M model as its quality-first default. These measurements include network latency and aren’t service guarantees.
Benchmark the complete model and infrastructure configuration against your own decisions. Use CPU for background, offline, or low-throughput workloads that aren’t latency-sensitive and can tolerate seconds of response time. Use GPU for interactive decisions, long prompts, or workloads with tight tail-latency targets. Keep state and option descriptions concise, group decisions that share the same state into one request, and scale endpoint instances for concurrency. Shared-state scoring reuses the common prompt prefix, while the adapter returns retryable HTTP 503 responses instead of allowing an unbounded queue around its stateful llama.cpp context.
Prerequisites
You need:
- An AWS account and an S3 bucket in your deployment AWS Region.
- Python 3.10 or later, Git, and the AWS Command Line Interface (AWS CLI).
- A purpose-specific CodeBuild service role for the optional SemIf extension.
- An AWS Identity and Access Management (IAM) role that SageMaker AI can assume.
- Permissions for SageMaker AI, Amazon ECR, Amazon S3, CodeBuild, IAM pass-role actions, and Amazon CloudWatch Logs.
- Quota for a compatible x86 CPU or NVIDIA GPU SageMaker real-time endpoint.
The text-generation example uses the CPU DLC and a fixed CPU instance. The SemIf extension keeps CPU as the default for workloads that aren’t latency-sensitive and offers an optional CUDA image with ordered instance pools. Review SageMaker AI pricing before creating an endpoint.
Deploy a decision model and extend it with SemIf
Use the following procedure to deploy the standard text-generation endpoint, then build the optional SemIf extension for structured decisions on CPU or GPU.
- Clone the code sample and install its dependencies.
- Set the deployment values for your account.
- Package the pinned GGUF model and tokenizer with CodeBuild.
         
         Wait for the returned build ID to reach SUCCEEDED. The build records the source revisions and checksums in model-manifest.json and stops if the GGUF checksum differs from the validated value.
- Deploy the GGUF model with the AWS DLC for llama.cpp.
         Resolve a digest-pinned server-sagemaker-cpu-v1 image from the AWS DLC for llama.cpp documentation, then create the SageMaker AI model, endpoint configuration, and endpoint:
Select a server-sagemaker-cpu-v1 or server-sagemaker-cuda-v1 image rather than the corresponding EC2 image. The SageMaker AI images implement the /ping and /invocations container contract and map invocation payloads to chat completions.
This walkthrough supplies the GGUF model through the SageMaker AI model artifact in Amazon S3. As an alternative, you can configure SM_LLAMA_CPP_HF_REPO and SM_LLAMA_CPP_HF_FILE to download a GGUF file from Hugging Face when the endpoint has network egress.
You don’t need a Dockerfile or an ECR repository for this path. Wait for the endpoint to enter InService, then send an OpenAI-compatible chat request:
- Build the optional SemIf child image and resolve its immutable digest.
         For CPU: For GPU, build the CUDA child image instead: After the build succeeds, construct the immutable image URI: The deployment script rejects mutable image tags.
- Deploy the SemIf endpoint.
         The CPU configuration uses a fixed instance type: Wait for the returned endpoint name to enter InService. This path sets n_gpu_layers=0. The adapter serializes scoring around one stateful llama.cpp context, so scale out with endpoint instances after measuring your workload rather than assuming parallel scoring inside one container.
For the GPU image, provide ordered instance pools and request full model offload: Instance pools are ordered placement fallbacks, not inference load balancing. SageMaker selects one available type for the variant. Endpoint creation can take longer while SageMaker AI works through the pool. Check the startup logs for the selected GPU and a message confirming that all model layers were offloaded.
- Invoke the SemIf endpoint with the example decision.
         The request declares stable IDs for each allowed option: The response preserves the option order and includes conditional probabilities, raw logits, token and prompt metadata, and the pinned model identity: Apply application-level thresholds and fallbacks. Don’t use a model decision as a substitute for authorization.
Clean up
Delete the SageMaker AI endpoint, endpoint configuration, and model:
The script deletes only those explicitly named SageMaker AI resources. Delete the CodeBuild projects, ECR repository, model and source objects in Amazon S3, logs, and purpose-specific IAM roles when you no longer need them.
Conclusion
The AWS DLC for llama.cpp gives you a managed foundation for serving decision models on SageMaker AI across CPU and GPU instances. It can load GGUF models from SageMaker AI model artifacts or a configured Hugging Face repository, then serve OpenAI-compatible chat completions through InvokeEndpoint without requiring a custom container. When your application needs direct logits and model state operations, you can extend the DLC with a SemIf adapter. Choose CPU for workloads that aren’t latency-sensitive, and choose GPU when prompt prefill and tail latency affect the application experience.
Review the code sample, AWS DLC for llama.cpp documentation, and SageMaker AI custom inference container contract to adapt the deployment for your workload.
