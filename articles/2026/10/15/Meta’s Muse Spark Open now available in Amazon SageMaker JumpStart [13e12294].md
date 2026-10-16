---
id: "13e122947fcaa3ff"
title: "Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart"
url: "https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart"
link: "https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-15T17:43:35Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Aris Tsakpinis"]
language: "en"
summary: "Muse Spark Open, Meta’s coding-optimized open-weight model, is now available in Amazon SageMaker JumpStart , the machine learning (ML) hub of Amazon SageMaker AI . The model was trained on real developer workflows, such as multi-file refactors and long debugging sessions, and it supports a context window of 1 million tokens. You can deploy it to a SageMaker AI endpoint in your own AWS account in…"
tags: ["Amazon SageMaker AI", "Amazon SageMaker JumpStart", "Announcements", "Intermediate (200)"]
orgs: ["Amazon", "Meta", "Nvidia"]
topics: ["models & research", "agents & coding", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1642
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart

AWS Machine Learning Blog · Aris Tsakpinis · 2026-10-15

Artificial Intelligence
Meta’s Muse Spark Open now available in Amazon SageMaker JumpStart
Muse Spark Open, Meta’s coding-optimized open-weight model, is now available in Amazon SageMaker JumpStart, the machine learning (ML) hub of Amazon SageMaker AI. The model was trained on real developer workflows, such as multi-file refactors and long debugging sessions, and it supports a context window of 1 million tokens. You can deploy it to a SageMaker AI endpoint in your own AWS account in a few steps, without managing the serving infrastructure yourself. SageMaker JumpStart offers two variants: BF16 (Muse-Spark-Open-816B-A42B) and NVFP4 quantized (Muse-Spark-Open-816B-A42B-NVFP4).
In this post, we introduce Muse Spark Open and show you how to deploy the model with Amazon SageMaker Studio and the SageMaker Python SDK, send it a first inference request, and clean up.
Overview of Muse Spark Open
Meta describes Muse Spark Open as a coding-optimized model trained for agentic coding workflows, with a focus on first-attempt accuracy, tool calling, and understanding of large codebases. It’s a reasoning model, and it accepts text, images, documents, audio, and audio-video as input and returns text.
Muse Spark Open uses a mixture-of-experts (MoE) architecture with 816 billion total parameters, of which 42 billion are active for each token. The model holds the capacity of a very large network, while the compute it spends on each token is closer to that of a much smaller dense model. Meta releases the weights under the Muse Model License, which includes the Muse Spark Usage Policy.
The following table summarizes the model.
Built for long-running coding agents
Meta trained Muse Spark Open on the way developers work in real repositories: code generation, debugging, multi-file refactors, and tasks that run for a long time. With the 1 million-token context window, the model can take in a whole project, including its dependencies, legacy code, and thousands of files. You don’t need to split a task into smaller pieces to fit the context.
Meta also designed Muse Spark Open as an agentic model from the start. Meta says the model plans, acts, observes the result, and corrects itself over long horizons, rather than making single tool calls. As a reasoning model, it works through a task before it acts, and the SageMaker AI endpoint returns that reasoning alongside the answer, so you can follow what an agent is doing and why. Meta trained the model to browse the web, coordinate subagents for work that can be split up, and operate computers across desktop, mobile, and browser environments. These are capabilities of the model. On SageMaker AI, your application or agent framework provides the tools, browser, and computer-use environment that the model calls. Beyond code, Meta reports that Muse Spark Open reasons across images, documents, audio, and video.
Two properties of the model shape how you serve it. First, sparse activation keeps per-token compute low, but serving still requires enough GPU memory to hold all 816 billion parameters, so the instance choice comes down to memory capacity. Second, the NVFP4 variant stores weights in NVIDIA’s 4-bit floating point format, which needs roughly a quarter of the memory of the BF16 weights. On SageMaker AI, that difference decides the instance: the NVFP4 variant runs on ml.p5e.48xlarge, and the BF16 variant runs on ml.p6-b300.48xlarge. That makes NVFP4 the variant to try first when you size for cost. Evaluate it on your own workloads to confirm the quality fits your use case.
With open weights on SageMaker AI, you also control the deployment. The endpoint runs in your AWS account, so your source code and prompts are processed on infrastructure that you configure and control. You can attach the endpoint to your own Amazon Virtual Private Cloud (Amazon VPC), encrypt its storage volume with a key from AWS Key Management Service (AWS KMS), and turn on network isolation for the container. You also choose the instance type and scaling limits, and you pin the model version, so the model only changes when you redeploy.
Use cases
You can use Muse Spark Open for a wide range of applications. Meta’s focus on coding and agentic workflows suits it to the following use cases:
- Coding assistants over private repositories: Answer questions about large codebases, refactor them, and debug them with the full project in context, while the code is processed on an endpoint in your account.
- Long-running coding agents: Run agents that plan a change, edit across multiple files, run tests in your own sandbox, and correct course based on the results.
- Multimodal engineering workflows: Turn screenshots, design documents, or a recorded bug report with audio and video into a reproduction plan or a draft fix.
Getting started with SageMaker JumpStart
You can deploy Muse Spark Open from SageMaker Studio or with the SageMaker Python SDK. Each path creates a real-time SageMaker AI endpoint in your account.
Prerequisites
Before you start, make sure that you have the following:
- An AWS account with permissions to create SageMaker AI models and endpoints.
- An AWS Identity and Access Management (IAM) execution role for SageMaker AI. For this walkthrough, the AmazonSageMakerFullAccess managed policy is sufficient. For production, scope the role to the actions and resources that your deployment needs. For details, refer to How to use SageMaker AI execution roles.
- A SageMaker AI domain with access to SageMaker Studio, for the Studio path. For setup instructions, refer to Use quick setup for Amazon SageMaker AI.
- Service quota for the endpoint instance type: ml.p5e.48xlarge for endpoint usage for the NVFP4 variant, or ml.p6-b300.48xlarge for endpoint usage for the BF16 variant. To raise a quota, refer to Requesting a quota increase.
- For the SDK path: Python 3.10 or later and SageMaker Python SDK v3 (pip install --upgrade sagemaker).
- An AWS Region where Muse Spark Open is available in SageMaker JumpStart. At launch, Muse Spark Open is available in US East (N. Virginia) and US East (Ohio). To check availability in other Regions, open SageMaker JumpStart in your Region.
The instances that host Muse Spark Open are multi-GPU instances, and you pay for an endpoint for as long as it runs, whether or not it serves requests. Delete the endpoint when you finish, as described in the clean-up section of this post. For rates, refer to Amazon SageMaker AI pricing.
Deploy using SageMaker Studio
The SageMaker Studio path suits a first evaluation: you find the model, review its license, and deploy it from one model detail card.
To find Muse Spark Open in SageMaker JumpStart
- Open SageMaker Studio.
- In the navigation pane, choose JumpStart.
- In the search box, enter Muse Spark Open.
- Choose Muse-Spark-Open-816B-A42B for the BF16 variant or Muse-Spark-Open-816B-A42B-NVFP4 for the NVFP4 variant to open its model detail card.
Figure 1 shows the model detail card, which lists the model description, license, and the Deploy option.
To deploy the model
- On the model detail card, choose Deploy.
- Muse Spark Open is a gated model, so SageMaker Studio shows its end-user license agreement (EULA). Review the agreement and accept it to continue.
- For Endpoint name, keep the generated name or enter your own.
- For Instance type, select ml.p5e.48xlarge for NVFP4 or ml.p6-b300.48xlarge for BF16. SageMaker Studio lists only the instance types that the model supports.
- For Initial instance count, enter 1.
- (Optional) Under Advanced options, select a VPC and an AWS KMS key, or turn on network isolation.
- Choose Deploy.
Figure 2 shows the deployment settings for the NVFP4 variant.
Deployment typically takes 15–20 minutes while SageMaker AI provisions the instance and loads the weights. When the endpoint status changes to InService, the endpoint is ready for requests, as shown in Figure 3.
Deploy using the SageMaker Python SDK
SageMaker JumpStart identifies each variant by a model ID:
- BF16: meta-vlm-muse-spark-open-816b-a42b.
- NVFP4: meta-vlm-muse-spark-open-816b-a42b-nvfp4.
The following code deploys the NVFP4 variant with SageMaker Python SDK v3. You can run it in a SageMaker Studio notebook, which uses your domain’s execution role. In any other Python environment with AWS credentials, pass your SageMaker AI execution role with the role_arn parameter. Muse Spark Open is a gated model, so you must set accept_eula=True to deploy it. To pin a specific model version, add model_version to JumpStartConfig.
Run inference
When the endpoint is in service, send it a request with the invoke method. The endpoint accepts an OpenAI-compatible chat payload with a messages list and returns a chat completion. The final answer is in message.content, the model’s reasoning is in message.reasoning_content, and usage.reasoning_tokens reports how many tokens the reasoning used. Because Muse Spark Open is a reasoning model, leave enough room in max_tokens for its reasoning and the final answer.
The endpoint also supports streaming. To receive tokens as they’re generated, add "stream": true to the request body and call endpoint.invoke_with_response_stream instead of invoke.
Clean up
To stop incurring charges, delete the endpoint when you no longer need it. If you deployed with the SDK, delete the model, the endpoint, and the endpoint configuration:
If you deployed from SageMaker Studio, delete the endpoint in the SageMaker AI console: choose Inference, then Endpoints, select the endpoint, and choose Actions, Delete.
Conclusion
In this post, we showed how to deploy Muse Spark Open, Meta’s coding-optimized open-weight model, from SageMaker JumpStart to an endpoint in your own AWS account. You used SageMaker Studio or the SageMaker Python SDK and sent the model a first inference request. Benchmark both variants on your own repositories before you choose an instance for production.
To get started, search for Muse Spark Open in SageMaker JumpStart in SageMaker Studio. For more deployment options, such as inference components and optimized deployment configurations, refer to JumpStart foundation model usage in the Amazon SageMaker AI Developer Guide. Before you deploy, review the Muse Model License, which SageMaker JumpStart shows when you deploy the model. For help planning a production deployment, contact AWS.
