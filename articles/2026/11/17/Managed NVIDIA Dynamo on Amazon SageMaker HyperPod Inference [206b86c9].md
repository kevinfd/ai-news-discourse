---
id: "206b86c970ea91d6"
title: "Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference"
url: "https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference"
link: "https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-17T23:33:26Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Vinay Arora"]
language: "en"
summary: "Serving large language models (LLMs) efficiently requires sufficient GPU memory and careful coordination of prompt processing and token generation. GLM-5.3’s FP8 weights, for example, exceed the 640 GB of GPU memory on a single ml.p5.48xlarge instance, before accounting for KV cache and runtime overhead. Long prompts can also slow token generation when both share the same GPUs. \n Amazon…"
tags: ["Advanced (300)", "Amazon SageMaker HyperPod", "Announcements"]
orgs: ["Amazon", "Nvidia", "OpenAI"]
topics: ["chips & infrastructure", "jobs & society", "models & research", "health & science"]
content_source: "fulltext"
word_count: 1391
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference

AWS Machine Learning Blog · Vinay Arora · 2026-11-17

Artificial Intelligence
Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference
Serving large language models (LLMs) efficiently requires sufficient GPU memory and careful coordination of prompt processing and token generation. GLM-5.3’s FP8 weights, for example, exceed the 640 GB of GPU memory on a single ml.p5.48xlarge instance, before accounting for KV cache and runtime overhead. Long prompts can also slow token generation when both share the same GPUs.
Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo, combining Dynamo’s distributed inference capabilities with the infrastructure management of HyperPod to address these challenges. Dynamo is an open source distributed inference framework that supports multi-node deployment, disaggregated prefill and decode, and KV-aware routing with engines such as vLLM, SGLang, and TensorRT-LLM. HyperPod supports these deployments with high-performance Elastic Fabric Adapter (EFA) networking, coordinated GPU scheduling, and node health monitoring and recovery. In this post, we illustrate multi-node and disaggregated serving through a deployment example, share benchmark results, and outline best practices for optimizing inference on HyperPod.
How the integration works
The HyperPod Inference add-on installs the Dynamo custom resource definitions and these serving and scheduling components:
- HyperPod Inference Operator manages endpoint deployment through an InferenceEndpointConfig (IEC) custom resource. Its dynamoSpec section supplies the Dynamo configuration.
- Dynamo operator manages resources defined in a DynamoGraphDeployment (DGD), including the frontend, model workers, replica counts, and resource requirements.
- Grove coordinates related groups of pods, including multi-node workers, and their scaling relationships.
- Kubernetes AI (KAI) Scheduler places pods on GPU resources, using gang scheduling to schedule the pods required for a multi-node worker together.
AWS Deep Learning Containers (DLCs) provide the Dynamo runtime, while the add-on manages integrated component versions. To adopt a supported Dynamo release, update the add-on.
Deployment architecture
The following diagram shows the deployment paths, serving components, and infrastructure management for disaggregated inference on SageMaker HyperPod. The Dynamo frontend routes requests to prefill workers, which process prompts, and decode workers, which generate tokens. These separate pools allow independent scaling and tuning. Both pools load the full model weights, and KV cache transfers between them over EFA.
Dynamo also supports aggregated serving, where prefill and decode run in the same worker. In either topology, workers can run on one instance or span multiple instances using tensor and pipeline parallelism. Dynamo’s KV-aware router considers reusable prefix KV cache and active worker load in both topologies. Prefix reuse can reduce prompt recomputation and improve time to first token, while load awareness helps avoid overloading workers. For more details on the Dynamo architecture, see the Dynamo Knowledge Base overview.
HyperPod provides node, GPU, and EFA health monitoring and manages node replacement, while the orchestration components recreate affected workers. Deployments configured through InferenceEndpointConfig with dynamoSpec support invocation through SageMaker endpoints.
Two ways to configure your deployment
Whether you are new to HyperPod, new to Dynamo, or both, the add-on offers two deployment paths to fit your workflow:
Bring-your-own DynamoGraphDeployment (DGD) lets existing Dynamo users continue using upstream documentation, recipes, and manifests, with the Dynamo operator managing the deployment. To bring an existing DGD to HyperPod, use a supported container image and configure storage, networking, and pod placement for your cluster.
InferenceEndpointConfig with dynamoSpec lets existing HyperPod Inference users deploy a new Dynamo endpoint using the same configuration format and OpenAI-compatible interface they already know. For the inference engine, you can choose vLLM, SGLang, or TensorRT-LLM, with vLLM used by default. The operator also supplies defaults for KV-aware routing and replica counts.
Both paths support single-instance and multi-node deployments. In either case, HyperPod manages node health and replacement. The table summarizes the responsibilities for each path.
Deployment example: GLM-5.3
The following excerpts use the InferenceEndpointConfig (IEC) deployment path with vLLM on ml.p5.48xlarge instances. Dynamo-specific settings belong under spec.dynamoSpec. Model source and endpoint settings are included in the complete manifest.
Multi-node aggregated serving
This configuration runs one model-worker replica across two instances (16 GPUs), with two frontend replicas for request handling. Setting dynamoSpec.frontend.routingMode to kv-aware turns on KV-aware routing.
Here, spec.replicas controls the number of model-worker replicas, while frontend.replicas controls the number of frontend replicas.
Multi-node disaggregated serving
Replace aggregation under spec.dynamoSpec with the following disaggregation block, keeping the preceding frontend configuration. Replica counts are set separately for prefill and decode. This example runs one prefill replica and two decode replicas, each spanning two instances, for a total of six instances.
Apply the deployment
Apply the complete manifest with kubectl apply. The HyperPod Inference Operator makes the configured model weights available to the workers and generates the DGD. Grove and KAI Scheduler coordinate placement so that the pods required for each multi-node worker are scheduled together.
After the SageMaker endpoint is ready and configured for chat completions, clients can send an OpenAI-compatible request payload through the SageMaker Runtime API:
Benchmarks
We benchmarked Dynamo on SageMaker HyperPod across two models to compare serving configurations.
Disaggregated prefill and decode for Qwen3-235B
We used AIPerf to compare aggregated and disaggregated serving for Qwen3-235B-A22B-FP8 using Dynamo with TensorRT-LLM on two p5en.48xlarge instances (16 H200 GPUs). Requests contained 4,000 input tokens and 200 output tokens. We retained measured points that met two targets: P90 time to first token below one second, and median generation speed of at least 50 tokens per second per user. Among these points, disaggregated serving achieved 2.05× the highest aggregated throughput: 207 versus 101 output tokens per second per GPU, at concurrency 80 and 32, respectively.
Multi-node aggregated serving for Qwen3.5-397B
Dynamo supports multi-node serving in both aggregated and disaggregated modes for models that exceed a single instance’s GPU memory. To evaluate a worker spanning nodes, we used AIPerf to benchmark multi-node aggregated serving for Qwen3.5-397B-A17B-FP8 with Dynamo and vLLM, using TP4 × PP2 and eight active H200 GPUs. This model fits on one instance, so in practice you would not split it. It serves here as a controlled baseline. We compared eight GPUs on one p5en.48xlarge against four GPUs on each of two instances, using the same model, parallelism, and workload configuration. With an agentic workload featuring high prefix reuse at concurrency 32, the two-node configuration delivered 126.4 output tokens per second per GPU, retaining 99.1 percent of single-node throughput. This shows that Dynamo on SageMaker HyperPod can serve a model that needs more than one instance across nodes. The node boundary itself does not become a significant throughput penalty.
Best practices for optimized inference
NVIDIA Dynamo provides recipes and tools to help you select a serving configuration, benchmark performance, and tune your deployment on SageMaker HyperPod.
- Start with a matching recipe – Choose a Dynamo recipe for your model, inference engine, and GPU type. Account for model weights, KV cache, and runtime memory when sizing workers. For supported configurations, AISimulate can help compare aggregated and disaggregated serving, choose parallelism, and size prefill and decode worker pools before testing on GPUs.
- Verify communication before benchmarking – For deployments spanning instances, confirm that communication uses the intended EFA transport, including KV-cache transfers between prefill and decode workers. See the Dynamo EFA guide.
- Benchmark representative traffic – Replay your traffic with AIPerf, or use a generated agentic trace with representative prompt lengths, output lengths, and prefix reuse. Sweep concurrency for each configuration, retain points meeting your SLAs, and choose based on cost and latency priorities.
- Tune from measured bottlenecks – Adjust topology and worker allocation before engine settings, changing one variable at a time. Follow the performance tuning guide, or use Dynamo optimization agent skills to assist with benchmarking and tuning. Validate each candidate on your target HyperPod deployment.
Conclusion
NVIDIA Dynamo on SageMaker HyperPod Inference simplifies deploying and operating large models with multi-node serving, disaggregated prefill and decode, and KV-aware routing. The managed add-on installs the serving components, and configuration defaults simplify endpoint setup. HyperPod manages model weights, auto-scales clusters based on GPU and inference metrics, monitors node health, and replaces failed nodes. Together, these capabilities reduce undifferentiated infrastructure work so teams can focus on their models and applications. Get started with the setup instructions and complete deployment examples in the linked repository.
Acknowledgements
The authors would like to thank Eliuth Triana, Felipe Garcia, Sanjana Checker, Junyuan Yang, Jiahong Liu, Anish Maddipoti, Jacob Kern and Abdullahi Olaoye from NVIDIA for their contributions to this post. We also would like to thank Can Sun, Ophelia Yang, Aryaman Kothari, David Oh, and Ayush Kumar from AWS for their contributions.
