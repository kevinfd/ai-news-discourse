---
id: "74d0b7787940bc8e"
title: "AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents"
url: "https://marktechpost.com/2026/11/12/aws-emulator-local-aws-api-emulator-ai-agents"
link: "https://marktechpost.com/2026/11/12/aws-emulator-local-aws-api-emulator-ai-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T17:26:08Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "AWS has released AWS Emulator , a local emulator of the AWS APIs. You run it on a laptop, a dev server or in CI. The AWS CLI and SDKs talk to it instead of AWS. No AWS account is needed, and there is no service fee . The unusual part: autonomous agents wrote and reviewed all of its code . For developers and coding agents, AWS Emulator gives a fast, free test loop against AWS-shaped APIs. \n\n…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Artificial Intelligence", "Context Engineering", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source"]
orgs: ["Amazon", "Hugging Face"]
topics: ["agents & coding", "products & launches", "robotics & autonomy"]
content_source: "summary"
word_count: 939
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents

MarkTechPost · Asif Razzaq · 2026-11-12

AWS has released AWS Emulator , a local emulator of the AWS APIs. You run it on a laptop, a dev server or in CI. The AWS CLI and SDKs talk to it instead of AWS. No AWS account is needed, and there is no service fee . The unusual part: autonomous agents wrote and reviewed all of its code . For developers and coding agents, AWS Emulator gives a fast, free test loop against AWS-shaped APIs. 

 TL;DR 

 Size: Built from 438 AWS API models , covering 200+ services . One Rust crate per service. 

 Runs on: Linux x86_64/aarch64 (RPM or Debian), or Docker on macOS/Windows with a 2 GiB memory limit. Source builds need 100 GB of free disk. 

 Performance: Passes 24,243 of 42,857 scored fidelity tests (56.6%) in release v1.0.322 . 

 Best: AWS KMS at 93.9% (291 of 310 tests); Amazon SQS at 89.8%. 

 Worst: AWS CloudFormation at 15.8% (414 of 2,612 tests). 

 What is AWS Emulator? 

 AWS Emulator is a headless local program from AWS that serves an AWS API endpoint. You point the CLI or an SDK at it with environment variables. Your code does not change. Resources live in memory and vanish when it stops. 

 The docs show a DynamoDB example. A CreateTable call with a 2-character name fails with the same ValidationException text AWS returns. 

 How did AI agents build AWS Emulator? 

 The project began with a prompt to Kiro . It returned a passable Amazon SQS emulator in about 15 minutes. AWS then split the work across 3 teams of agents: 

 Test writers derive scenarios from the public Smithy API models and verify each against real AWS. 

 Issue finders replay those tests against the emulator and file failures. 

 Fixers take 1 issue each and submit a patch. 

 Every patch passes a merge gate covering build, code review, security and fidelity. Several security agents run adversarial reviews . Matthew Goldberg reports hundreds of concurrent agents fixing thousands of issues a day. The release pipeline runs on AWS Developer Tools, with CodeCommit as the agents’ repository. Code reaches GitHub last. 

&&&

 How accurate is AWS Emulator? 

 AWS publishes a scores.json file with each release. We tallied the v1.0.322 file , scored on November 11, 2026. 

 Overall: 24,243 of 42,857 scored tests pass (56.6%); 80 were skipped. 

 Step level: 49,810 of 68,007 individual steps pass (73.2%). 

 Cross-service workflows: 2,752 of 6,569 pass (41.9%). 

 Core services: S3 79.1%, DynamoDB 77.3%, SNS 73.9%, Lambda 46.4%, EC2 41.5%. 

 Per the fidelity docs , control-plane APIs match AWS best. Data-plane, CloudFormation, Terraform and CDK support varies by service. Unimplemented operations return HTTP 501 NotImplemented . The tests live in aws-emulator-evaluation-suite , including failing ones. 

 How do you run AWS Emulator? 

 There are 4 paths, per the README : 

 Linux: install the RPM or Debian package and run aws-emulator . 

 macOS/Windows: build a container from AWS’s Dockerfile , capped at 2 GiB memory. 

 Rust embedded mode: add it as a dev-dependency for 1 isolated instance per test. 

 Coding agents: aws agent-toolkit add-skill --skill-name aws-emulator , with AWS CLI 2.35.0 or later. 

 A source build serves HTTPS on 127.0.0.1:9297 with a self-signed certificate. It needs a Rust toolchain, a C compiler and at least 100 GB of disk. Embedded mode carries the same build cost on the first cargo test . 

 How does it compare with LocalStack, Moto and Floci? 

 Feature AWS Emulator LocalStack Moto Floci License CC0 1.0 ( vendor/ Apache 2.0) Commercial plans Apache-2.0 MIT Price Free Hobby $0 (non-commercial); Base $39; Ultimate $89 per license/month (annual) Free Free Service coverage 200+ services, 438 API models 30+ / 55+ / 110+ by plan Not disclosed in README Not totaled in README Vendor token needed No Yes (auth token) No Not disclosed Default endpoint HTTPS 127.0.0.1:9297 Port 4566 Port 5000 Port 4566 In-process test mode Rust dev-dependency Not disclosed Python @mock_aws decorator Not disclosed Footprint 2 GiB Docker limit in AWS guide Not disclosed Not disclosed ~13 MiB idle, ~24 ms start (self-reported) Published fidelity scores Yes, per release Not disclosed Not disclosed Not disclosed 

 What are AWS Emulator’s limitations? 

 AWS lists them plainly : 

 No IAM evaluation. Identity and resource policies are not evaluated like AWS. Do not use it for security tests. 

 1 Region, 1 account. It accepts any IDs but does not isolate resources by them. 

 Verified in us-west-2 only , with global services checked in us-east-1. 

 In-memory and short-lived. It is not tested for long runs or load tests. Use --idle-timeout to stop it. 

 Telemetry is on by default. Turn it off with --telemetry off , EMULATOR_TELEMETRY=off , config.toml or the embedded API. 

 The release pace is fast. Versions v1.0.265 to v1.0.322 shipped between November 8 and 11. 

 Key Takeaways 

 AWS Emulator is a free, CC0 local copy of 200+ AWS services. 

 Agents wrote all the code; humans built the tests and merge gates. 

 It passes 56.6% of 42,857 published fidelity tests at launch. 

 SQS, KMS and S3 are strong; CloudFormation and IoT lag. 

 Use it for fast local and CI loops, not security or load testing. 

 Check out the GitHub repo , the user guide , the fidelity tests and the engineering post . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents appeared first on MarkTechPost .
