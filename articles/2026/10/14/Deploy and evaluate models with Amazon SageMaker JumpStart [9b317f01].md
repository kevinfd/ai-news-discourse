---
id: "9b317f01752ab263"
title: "Deploy and evaluate models with Amazon SageMaker JumpStart"
url: "https://aws.amazon.com/blogs/machine-learning/deploy-and-evaluate-models-with-amazon-sagemaker-jumpstart"
link: "https://aws.amazon.com/blogs/machine-learning/deploy-and-evaluate-models-with-amazon-sagemaker-jumpstart"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-14T13:14:36Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Vamsi Goparaju"]
language: "en"
summary: "Choosing the right model for a specific application requires a practical way to test it with representative inputs. Amazon SageMaker JumpStart provides access to a broad catalog of already pretrained models. In this post, we show how to deploy an available model from SageMaker JumpStart, run a lightweight and repeatable performance test using the SageMaker Python SDK, and delete the endpoint…"
tags: ["Amazon SageMaker JumpStart", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon", "Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 461
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Deploy and evaluate models with Amazon SageMaker JumpStart

AWS Machine Learning Blog · Vamsi Goparaju · 2026-10-14

Artificial Intelligence
Deploy and evaluate models with Amazon SageMaker JumpStart
Choosing the right model for a specific application requires a practical way to test it with representative inputs. Amazon SageMaker JumpStart provides access to a broad catalog of already pretrained models. In this post, we show how to deploy an available model from SageMaker JumpStart, run a lightweight and repeatable performance test using the SageMaker Python SDK, and delete the endpoint when testing is complete. For supported models and available capacity, this workflow provides a repeatable evaluation path, although deployment time varies by model, instance type, quota, and AWS Region.
In 2026, SageMaker JumpStart introduced two improvements that simplify model discovery and deployment. In the Model Hub section of the Amazon SageMaker AI console, you can browse the SageMaker JumpStart catalog, view sample notebooks, and open them directly in SageMaker Studio. Pre-configured endpoint deployment options provide named configurations optimized for priorities such as low cost, low latency, or general-purpose workloads across a range of generative AI models, including Neuron-optimized configurations. Additionally, you can now go from Hugging Face model discovery to SageMaker AI deployment in a single click using the new deep link integration.
Solution overview
Our approach uses a reusable Python script that performs three steps:
- Discover and deploy a model from SageMaker JumpStart.
- Run model-specific sample prompts and measure latency, approximate output length, and single-request generation rate.
- Clean up the endpoint.
This pattern works for many compatible SageMaker JumpStart models, although payload formats, required instance types, end-user license agreement (EULA) requirements, and response schemas may require model-specific adjustments.
Prerequisites
- An AWS account with SageMaker AI permissions.
- Python 3+ with SageMaker Python SDK v3 installed (pip install "sagemaker>=3,<4").
- Sufficient GPU instance quota for the model you want to test or request a quota increase.
Step 1.a: Discover available models
UI path to find models in SageMaker JumpStart:
Code path using SageMaker Python SDK:
Or search by model name:
Step 1.b: Deploy the model
UI path to deploy models from SageMaker JumpStart:
Code path using SageMaker Python SDK:
Step 2: Run sample prompts and measure performance
Result:
Step 3: Cleanup
Conclusion
This pattern works for many available SageMaker JumpStart models, but the payload format, required instance type, EULA, and response parsing may require model-specific adjustments. By using consistent test prompts and measuring latency, throughput, and output quality across models, you can compare options and select the right fit for your workload.
Try this approach with different models from Amazon SageMaker JumpStart to find the right balance of quality, speed, and cost for your applications.
References
- SageMaker Python SDK Documentation
- Benchmark and Optimize SageMaker JumpStart Deployment (blog post)
- From Hugging Face to SageMaker Studio in One Click (blog post)
- Amazon SageMaker JumpStart
