---
id: "e504c61a39ac2d49"
title: "Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture"
url: "https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture"
link: "https://aws.amazon.com/blogs/machine-learning/build-a-model-improvement-flywheel-with-amazon-sagemaker-hyperpod-data-capture"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-13T18:01:15Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Shantanu Tripathi"]
language: "en"
summary: "Foundation models deployed on Amazon SageMaker HyperPod meet inputs that no pre-curated dataset covers: domain-specific jargon, unexpected formats, new products, and changing user behavior. Without a record of production inference data, teams can’t detect drift, find failure patterns, or use real interactions to improve the model. \n Amazon SageMaker HyperPod now provides Data Capture, a built-in…"
tags: ["Amazon SageMaker HyperPod", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "policy & regulation"]
content_source: "fulltext"
word_count: 3219
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture

AWS Machine Learning Blog · Shantanu Tripathi · 2026-11-13

Artificial Intelligence
Build a model improvement flywheel with Amazon SageMaker HyperPod Data Capture
Foundation models deployed on Amazon SageMaker HyperPod meet inputs that no pre-curated dataset covers: domain-specific jargon, unexpected formats, new products, and changing user behavior. Without a record of production inference data, teams can’t detect drift, find failure patterns, or use real interactions to improve the model.
Amazon SageMaker HyperPod now provides Data Capture, a built-in capability that records live inference inputs and outputs to Amazon Simple Storage Service (Amazon S3) at three independent tiers, with minimal latency impact and zero impact on model availability.
In this post, we walk through one complete example on a single SageMaker HyperPod cluster. A home-appliance support router captures its production traffic, Amazon Athena queries surface a new-product blind spot, a SQL policy labels the captured records, and a fine-tune on that data teaches the router the new product. We measure accuracy before and after, on data that could not have existed before the model was deployed. The inference operator serves the model on one node, and the training operator runs the fine-tuning on another.
We use synthetic data for the walkthrough. The scripts, manifests, SQL, synthetic datasets, and expected outputs are available in the accompanying GitHub repository.
Three-tier Data Capture architecture
HyperPod Data Capture provides three independent tiers, each at a different point in the request path. You can turn on any combination in the same dataCapture block.
Tiers 1 and 3 both store full payloads, so enabling both stores every record twice. Use Tier 1 for compliance and Model Monitor, Tier 2 when you only need traffic metadata, and Tier 3 when you intend to use the payloads. This post uses Tier 3 only. Because Tier 3 records complete payloads, which can include names, addresses, and order numbers, protect that data before it becomes training data. Use sampling, AWS Key Management Service (AWS KMS) encryption (kmsKeyId), S3 lifecycle rules, and personally identifiable information (PII) redaction (for example, with Amazon Comprehend).
Prerequisites
- A SageMaker HyperPod cluster orchestrated by Amazon Elastic Kubernetes Service (Amazon EKS), with the inference operator installed (Setting up your HyperPod clusters for model deployment) and the training operator EKS add-on amazon-sagemaker-hyperpod-training-operator installed (Installing the training operator).
- Two available NVIDIA GPUs, one for serving and one for training. We used an ml.g6e.8xlarge for serving and an ml.g6e.xlarge for training (one 48 GB NVIDIA L40S each). The serving pod holds its GPU for the life of the endpoint, so with only one GPU the training pod stays Pending.
- kubectl configured for the cluster.
- An S3 bucket in the same Region.
Confirm both operators are installed. The command returns two rows:
Solution overview
The following diagram shows the five steps of the walkthrough on one SageMaker HyperPod cluster: capture every request and response to Amazon S3, analyze the captures with Athena, label them with a SQL policy, fine-tune with the training operator on a second GPU, and redeploy side by side with capture still on.
The inference operator adds three sidecars to the model pod. Every request that passes through the NGINX proxy is copied to an OpenTelemetry collector, batched, and written to S3 through a Mountpoint-S3 volume. Athena reads those files in place. The training operator runs the fine-tune as a HyperPodPyTorchJob on a second GPU, and the new model is served by a second endpoint that also has capture on.
Step 0: Set your variables
Every later step reads these. Edit the first block, then paste the whole thing:
Step 1: Stage the base model in S3
We use Qwen2.5-3B-Instruct because it is small enough to fine-tune in about a minute and fits on a single L40S.
Step 2: IAM permissions
Four identities need access. For the policy statements, see Data capture for inference on HyperPod.
- The Mountpoint-S3 CSI driver role. Tier 3 capture writes through a Mountpoint-S3 volume, and the driver authenticates as its own IAM roles for service accounts (IRSA) role, not as the pod’s service account. It needs s3:PutObject, s3:AbortMultipartUpload, and s3:DeleteObject on your capture bucket, plus kms:Decrypt, kms:GenerateDataKey, and kms:DescribeKey if you set kmsKeyId. If this is missing, the endpoint stays healthy and requests succeed, but no captures appear. See Mountpoint for Amazon S3 CSI driver.
- The inference operator execution role. It needs s3:PutObject on your capture bucket, plus kms:Decrypt and kms:GenerateDataKey if you set kmsKeyId. The capture files themselves are written through the CSI driver role, so when no captures appear, check that role first.
- The training pod’s service account ($TRAIN_SA). Read access to the base model and training data, and write access for the merged model, through EKS Pod Identity.
- Athena. Read access to the capture prefix, plus a query-results location.
Enabling Data Capture
The next three steps deploy the router with Tier 3 capture on, check that the pod runs the capture sidecars, and confirm that records reach Amazon S3.
Step 3: Deploy the model with Tier 3 capture enabled
This is the whole feature: the dataCapture.modelPod.enabled: true block. Everything else is an ordinary vLLM deployment.
The preceding modelPod block sets 100% sampling and captures both input and output, which are the defaults. To tune it, add any of these optional fields under modelPod:
Step 4: Wait for the pod
A capture-enabled pod runs four containers: the model, sidecar-reverse-proxy (NGINX), otel-collector, and s3-uploader. The model container and the pod’s app label are both named after modelName.
In our run, the pod was ready about five minutes after kubectl apply, most of it spent downloading the weights.
Step 5: Send a request and confirm captures land in S3
Send an inference request through the capture proxy on port 8081, then, after the flush interval, list the capture prefix. The model itself listens on port 8000. Requests sent there bypass the proxy and are not captured.
You see one or more .jsonl objects under {s3Uri}/{uniqueID}/pod/{variant}/{YYYY}/{MM}/{DD}/{HH}/. The uniqueID is generated per endpoint. Each line is one inference in the SageMaker data-capture format shown next.
The captured record format
The request and response bodies are stored base64-encoded, as the encoding field shows, so reading them back requires base64-decoding and then parsing JSON:
Decoded, endpointInput.data is the request body the client sent and endpointOutput.data is the response the model returned.
The scenario: A support-ticket router meets a product launch
The deployed model is a support-ticket router for a home-appliance retailer. It uses vLLM guided JSON decoding to classify each ticket into one of six categories: ProductFridge, ProductWasher, ProductOven, ProductDishwasher, ProductMicrowave, or the catch-all Other. Guided decoding means it can only return a valid object with one of those labels:
After the model was deployed, the retailer launched its own line of air conditioners, the Arctis series (Arctis 9K, 12K, Mini, and so on). The router has no category for them. It can’t say “this is new.” It can only pick the closest label it knows. Unless every request and response is recorded, the evidence disappears the moment the response is returned.
The synthetic traffic
We generated two synthetic datasets:
- Production traffic: 900 tickets, replayed in order through the capture proxy over 15 minutes, using the router’s original six-label prompt. The first 400 come before the launch and mention no air conditioners. In the remaining 500, the share of Arctis tickets ramps from 15% to 55%.
- Evaluation set: 280 labeled tickets, 40 per category, including the new ProductAC. It is held out by content: it uses symptoms, sentence templates, and Arctis model names that never appear in the traffic.
Each production request looks like this (system prompt abbreviated):
To replay the traffic, clone the accompanying repository, generate the datasets, and send them through the capture proxy. scripts/pod.sh runs the client inside the model container, so no load balancer or DNS is needed. The client prints the three timestamps that the Athena steps use: RUN_START, LAUNCH_TS (the first post-launch ticket), and RUN_END.
Export the three values that your run printed, and wait one flush interval:
Surfacing the problem with Amazon Athena
Offline benchmarks still look unchanged after the launch, because they are frozen in the past. The shift is visible only in the captured production traffic. This section shows how a data scientist finds it with Athena, without provisioning any infrastructure.
Step 6: Set your variables and configure an Athena helper function
Step 7: Declare the captures to Athena (two layers)
The first layer is the envelope. An external table describes the outer JSON of each record, and partition projection over year/month/day/hour maps the hourly S3 prefixes to partitions without a crawler or ADD PARTITION. The data fields are declared as plain strings, because they are base64 text.
The second layer is a view that decodes each record once. from_utf8(from_base64(...)) turns the payloads back into JSON. Without it, every extraction returns NULL. The ticket is the user message (messages[1], because messages[0] is the system prompt). The model’s answer is a JSON string inside the response JSON, so it needs a second extraction.
Two notes on the view:
- Always filter on partitions. Athena reads raw JSON, so a query without a partition filter scans every object you have ever captured. The view filters to one day, and the time bound limits it to our traffic run: the same prefix also holds the request from Step 5.
- messages[1] assumes one system message followed by one user message. Captured traffic is whatever clients actually sent, so adjust the extraction for multi-turn or few-shot requests.
Step 8: Is the category mix changing?
(Output is tab-separated. We aligned it here for readability. Our run compressed “weeks” into 15 minutes. In production, bucket by date_trunc('day', ts) or 'week' instead.)
The following chart plots the per-minute share of tickets routed to Other as bars, and the cumulative share as a line, with the launch marked.
Before the launch, Other stays under 7% per minute. It jumps to 15% in the launch minute and keeps climbing, reaching 47–65% in the last three minutes. The cumulative line in the chart only reaches 22.6%, because it averages the post-launch tickets with all the traffic from before the launch. That is why the per-minute rate, not the cumulative share, is what you would put behind an alarm.
Split at the launch, the whole category mix looks like this:
Other went from 4.8% of tickets before the launch (19 of 400) to 36.8% after it (184 of 500), and became the largest category.
Step 9: What is inside the Other bucket?
The Other bucket isn’t a mix of unrelated tickets. It’s dominated by one product name, arctis, and the vocabulary of a cooling appliance, which points to a new category the router has no label for.
Step 10: How big is it, and does the model’s confidence flag it?
Search the whole traffic stream for the new product, not just the Other bucket:
There are 178 air-conditioner tickets, 19.8% of all traffic. None of them appeared before the launch. They fall into two groups:
- 164 went to Other. Under the six-label schema, that is the correct answer: Other exists for exactly this case. The router isn’t broken. The taxonomy is missing a category, so these tickets reach a generic queue instead of the team that supports the product.
- 14 went to ProductFridge. These are true misroutes: a refrigerator team is now getting air-conditioner tickets.
Now test the model’s confidence on these known misroutes:
Of the 14 misrouted tickets, 10 reported a confidence of 0.9 or higher. A labeling rule such as “keep predictions with confidence >= 0.9” would have kept 71% of the known-wrong labels. That’s because confidence is a field we asked the model to write, not a calibrated probability. If you need a real uncertainty signal, request token logprobs from vLLM and read the probability at the category token instead of the model’s self-report. Budget for the extra payload size, because the logprobs are captured with every response.
From diagnosis to labeled training data
A data scientist doesn’t hand-label hundreds of tickets. Instead, they write the Athena finding down as a labeling policy: a SQL view that assigns a corrected label to every captured record. We relabel the misrouted air-conditioner tickets to the new class.
Step 11: The labeling policy
The doubled backslashes (\\b) are shell escaping inside the double-quoted string. Athena receives \b, a regular-expression word boundary.
Check what the policy produced:
This heuristic works because the new category is clear-cut (keyword-identifiable). For ambiguous tickets or overlapping categories, the NULL rows would route to Ground Truth for human labeling.
Step 12: Build the training file
Export the labeled view and convert it to chat-format JSONL. The allowed category set now includes ProductAC, the same seven-label prompt clients will send after the redeploy. Save this as build_training_file.py:
Fine-tuning on captured data with the HyperPod training operator
We fine-tune on the same cluster that serves the model, using the HyperPod training operator on the second GPU. The first endpoint keeps serving throughout.
Step 13: The training script
The script downloads the base model and training data from S3 and trains a low-rank adaptation (LoRA) adapter. The loss is computed only on the assistant turn, so the model learns to produce the label rather than repeat the prompt. The script then merges the adapter back into the base weights, so vLLM can serve the result unchanged, and uploads the merged model to S3. The job mounts the script into the training pod from a ConfigMap.
Step 14: Submit a HyperPodPyTorchJob
- logMonitoringConfiguration is the training operator’s distinguishing feature. If no loss line appears within 20 minutes of start, or the log goes quiet for 10 minutes mid-run while the process is still alive, the operator restarts the job instead of letting it burn GPU hours.
- The job installs three Python packages when it starts. The training node needs outbound internet access, for example through a NAT gateway, and so does pulling the vllm/vllm-openai image from Docker Hub. On a cluster without internet egress, bake the packages into a custom image in Amazon Elastic Container Registry (Amazon ECR) and drop the pip install.
An excerpt of the job log:
Training took 60 seconds on one L40S. LoRA at rank 16 trains about 29.9 million parameters, under 1% of the 3.1-billion-parameter model. The average training loss was 0.0123, and the per-step loss reached 0.0 within the first epoch, which shows the model memorizes 900 templated examples readily. On real data, hold out a validation split and stop early. Here we rely on the held-out evaluation set.
Step 15: Deploy the fine-tuned model side by side, with capture still on
Instead of editing the running endpoint, deploy the new model as a second endpoint from the same manifest, onto the GPU the training job just released. The first endpoint keeps serving until you cut clients over, so the redeploy causes no downtime, and rolling back means pointing clients back at the first endpoint.
The new endpoint writes captures under its own uniqueID. Because ENDPOINT_NAME is now appliance-router-v2, rerunning the CAPTURE_LOCATION lookup from Step 6 finds that prefix, so you can point a second Athena table at it for the next round of analysis. When you move clients over, update the endpoint, the label set, and the guided-JSON enum in the same release.
Measuring the lift
We ran the same 280 held-out tickets against the fine-tuned endpoint:
Fine-tuning taught the router the new category and caused no regression on the five established classes. It also fixed five Other errors that existed before the launch which the launched router sent to ProductFridge.
Because our evaluation set comes from the same generator as the training data, we also wrote 24 probe tickets by hand, in styles the generator never produces. The fine-tuned model scored 20/24:
It routes all eight air-conditioner probes correctly, but it learned two shortcuts: “cooling” means air conditioner, and any mention of Arctis means ProductAC, including stock and price-match questions. Both come from the training data: the labeling policy sent every Arctis ticket to ProductAC, and the captured traffic contained no pre-sales questions. With capture on for the new endpoint, those tickets are exactly what the next round of capture collects.
How much latency does capture add?
We measured this directly: the same 400 routing requests, sent from inside the pod either to port 8000 (no capture) or to port 8081 (through the capture proxy). We ran three rounds at 8 concurrent requests, plus one serial round:
Rows at concurrency 8 are the average of three rounds. Round-to-round variation (±1 ms at p50) was larger than the difference between the two paths.
Other uses for captured data
After inference data lands in S3, the same records feed many workflows:
- Improve the model: Use supervised fine-tuning (shown here), distill a large model’s outputs into a smaller model, or build preference pairs for direct preference optimization (DPO).
- Understand the model: Run Athena analytics (shown here), build golden regression sets from real prompts, set drift alarms, discover emerging intents, and detect malformed outputs and refusals.
- Operate and govern: Route ambiguous samples to Ground Truth for labeling, keep audit trails (Tier 1 is recommended), replay the exact input behind an incident, and analyze traffic and payloads for cost attribution.
Cost considerations
Two costs scale with usage:
- S3. Our records averaged about 2.3 KB each (3,955 records in 9.0 MB). Longer prompts and responses cost proportionally more. The uploader wrote one object per flush interval per pod, about 1,440 PUTs per pod per day at 60 seconds.
- Athena charges by data scanned, so always filter on the partition columns, and convert the raw JSON to Parquet with a CREATE TABLE AS SELECT (CTAS) query for repeated analysis.
For current prices, see Amazon S3 pricing and Amazon Athena pricing.
Clean up
To avoid incurring unnecessary charges, clean up the resources created in this walkthrough:
Conclusion
In this post, we showed how you can use SageMaker HyperPod Data Capture to record live inference data and turn it into training data. With capture available at three independent tiers, you can:
- Collect real-world training data with no measurable impact on serving latency.
- Query inference patterns at scale with Amazon Athena, with no infrastructure to manage.
- Turn an Athena diagnosis into a reproducible SQL labeling policy.
- Fine-tune on captured production data and measure a hard before/after lift.
- Integrate with the HyperPod training operator and SageMaker Ground Truth for the rest of the loop.
We ran one full turn of the loop on a home-appliance support router. Captured traffic revealed a new-product blind spot, and a SQL labeling policy turned those captures into training data. A 60-second LoRA fine-tune with the HyperPod training operator ran on the same cluster that served the model. It took the new category from 0% to full recall without a regression on any existing category. None of that training data existed before the model was deployed.
Data Capture is available today on SageMaker HyperPod clusters with the inference operator. To get started, add the dataCapture section to your InferenceEndpointConfig or JumpStartModel resource and deploy. To close the loop on the same cluster, add the amazon-sagemaker-hyperpod-training-operator EKS add-on. The complete code for this walkthrough is in the accompanying GitHub repository.
For more information, see the SageMaker HyperPod inference documentation and the HyperPod training operator documentation.
