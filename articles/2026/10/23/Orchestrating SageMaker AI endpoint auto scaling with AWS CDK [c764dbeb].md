---
id: "c764dbeb21a3918f"
title: "Orchestrating SageMaker AI endpoint auto scaling with AWS CDK"
url: "https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk"
link: "https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-23T16:30:10Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Lauren Eterno"]
language: "en"
summary: "Updating the Amazon Sagemaker AI real-time endpoint configuration (changing the instance type, instance count, or environment variables) causes deployments through AWS CloudFormation or the AWS Cloud Development Kit (AWS CDK) to fail. SageMaker AI requires you to deregister the scalable target before updating the endpoint, but when you deregister it, CloudFormation can’t track the AWS…"
tags: ["Advanced (300)", "Amazon SageMaker AI", "Technical How-to"]
orgs: ["Amazon"]
topics: ["products & launches", "policy & regulation", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1480
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Orchestrating SageMaker AI endpoint auto scaling with AWS CDK

AWS Machine Learning Blog · Lauren Eterno · 2026-10-23

Artificial Intelligence
Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
Updating the Amazon Sagemaker AI real-time endpoint configuration (changing the instance type, instance count, or environment variables) causes deployments through AWS CloudFormation or the AWS Cloud Development Kit (AWS CDK) to fail. SageMaker AI requires you to deregister the scalable target before updating the endpoint, but when you deregister it, CloudFormation can’t track the AWS Application Auto Scaling resources.
In this post, we show you how to use a reusable CDK construct with AWS CloudFormation custom resources to orchestrate deregister and register auto scaling automatically during endpoint updates. You can update your endpoint configuration and auto scaling parameters in a single deployment without manual intervention.
Why this problem occurs
When you deploy a SageMaker AI endpoint with native CloudFormation auto scaling resources, then change the endpoint configuration and redeploy, several failure modes emerge. The specific failure depends on what you change and how you work around the issue.
Changing the endpoint configuration with auto scaling registered
CloudFormation tries to update the endpoint while the scalable target is still registered. SageMaker AI rejects the update with the following error:
SageMaker AI blocks the endpoint update before CloudFormation reaches the auto scaling resources.
Manually deregistering auto scaling, then changing only the endpoint configuration
If you deregister the scalable target through the AWS Command Line Interface (AWS CLI) and redeploy with only an endpoint configuration change, the deployment succeeds. However, CloudFormation doesn’t register auto scaling even though it is in the CloudFormation template. Because the auto scaling parameters in the CloudFormation template haven’t changed, CloudFormation doesn’t register the scalable target or re-apply the scaling policy. The endpoint is now running without auto scaling, and there is no error to indicate anything went wrong.
Manually deregistering auto scaling, then changing auto scaling parameters
If you deregister the scalable target through the AWS CLI and redeploy with auto scaling parameter changes, CloudFormation tries to update the ScalableTarget resource that no longer exists:
This failure is notable because the rollback also fails (UPDATE_ROLLBACK_FAILED), leaving the stack in a broken state that requires manual intervention in the CloudFormation console to recover.
Solution overview
You can use this CDK construct to replace the native AWS::ApplicationAutoScaling::ScalableTarget and AWS::ApplicationAutoScaling::ScalingPolicy CloudFormation resources with three custom resources. These custom resources deregister and register auto scaling around the endpoint update with explicit dependency ordering, enforced by node.add_dependency calls in CDK. The full sequence is:
- Deregister (custom resource): Removes the scalable target before the endpoint update begins. On first deploy, no scalable target exists yet, so the handler handles the error gracefully and continues.
- Endpoint update (CDK-managed): CDK updates the endpoint resource normally, swapping to the new endpoint configuration.
- Register Scalable Target (custom resource): Waits for the endpoint to reach InService status, then registers the scalable target.
- Attach Scaling Policy (custom resource): Waits for the scalable target to be queryable, then applies the target tracking policy.
Register Scalable Target and Attach Scaling Policy use the CDK provider’s asynchronous completion pattern. Each custom resource has an on_event handler that returns immediately and an is_complete handler. The provider’s waiter re-invokes the is_complete handler on an interval (every 30 seconds) until its readiness check passes. The provider’s total_timeout (1 hour for Register Scalable Target, 15 minutes for Attach Scaling Policy) bounds the wait, so it isn’t limited by the timeout of any single Lambda invocation.
A ConfigHash property on each custom resource forces CloudFormation to re-invoke the Lambda functions whenever a configuration value changes. The endpoint configuration and auto scaling parameters are defined together because a single ConfigHash drives the auto scaling orchestration.
While the construct defines three custom resources, the deployed stack contains more than three Lambda functions. Each custom resource is backed by a CDK cr.Provider, and the provider framework generates its own helper Lambda functions. A synchronous provider (Deregister) adds one framework function. An asynchronous provider (Register Scalable Target and Attach Scaling Policy) adds three (onEvent, isComplete, and onTimeout) plus an AWS Step Functions state machine that drives the waiter. As a result, the deployed stack contains three custom resources, two Step Functions state machines, and twelve Lambda functions. Five of the resources hold the construct’s own handler code (one for Deregister, and an on_event and is_complete pair for each asynchronous resource), with the remaining seven generated by the provider framework. You don’t write or maintain the framework-generated functions, but they are present in the stack and worth accounting for when you review the deployed resources.
Walkthrough
In this walkthrough, you deploy a SageMaker AI endpoint with auto scaling using the provided example stack, then verify that configuration updates work correctly.
The walkthrough includes the following steps:
- Clone the repository and install dependencies.
- Configure your endpoint and auto scaling settings.
- Deploy and verify.
- Test an update.
The source code is available in the linked GitHub repository.
Prerequisites
For this walkthrough, you need the following:
- An AWS account with permissions for Amazon SageMaker AI, AWS Lambda, AWS Identity and Access Management (IAM), Application Auto Scaling, and Amazon CloudWatch.
- AWS CDK v2 installed.
- Python 3.12 or later.
- uv for Python dependency management.
- A SageMaker AI model artifact in Amazon Simple Storage Service (Amazon S3) and a container image in Amazon Elastic Container Registry (Amazon ECR), or a SageMaker AI built-in algorithm container.
Clone the repository and install dependencies
- Clone the repository:
- Install dependencies:
Configure your endpoint and auto scaling settings
The endpoint and auto scaling settings are defined together in config/config.yaml because a single config_hash drives the auto scaling orchestration. A change to either section triggers the full sequence.
Edit config/config.yaml with your values:
The endpoint parameters map to the SageMaker AI CreateModel and CreateEndpointConfig APIs. The auto scaling parameters map to the Application Auto Scaling RegisterScalableTarget and PutScalingPolicy APIs.
Deploy and verify
- Bootstrap your AWS environment if you haven’t already:
- Deploy the stack:
CloudFormation creates the SageMaker AI model, endpoint configuration, and endpoint, then runs the three custom resources in sequence to register auto scaling.
- Verify that the deployment registered the scalable target:
- Verify that the deployment applied the scaling policy:
Test an update
Change a value in config/config.yaml, for example, update the instance type from ml.m5.large to ml.m5.xlarge, and redeploy:
After the deployment completes, verify that auto scaling is still registered and has the updated values:
Integrating with an existing stack
Use the example stack if you’re starting fresh or want a reference implementation. Use the construct directly if you already have a CDK stack with SageMaker AI resources.
To integrate with an existing stack, copy the sagemaker_autoscaling/constructs/ directory into your project and add the construct alongside your endpoint resources:
How the construct works
This section walks through the key implementation details of SagemakerAutoscalingConstruct.
Deregister
The Deregister custom resource calls deregister_scalable_target before the endpoint update. It handles ObjectNotFoundException for first deployments where no scalable target exists:
The dependency is established in CDK:
Register Scalable Target
Even though CloudFormation treats the endpoint resource as complete once the update is accepted, the scalable target can only be registered after the endpoint reaches InService. Rather than block a single Lambda invocation on that wait, Register Scalable Target uses the provider’s asynchronous completion pattern. The on_event handler returns immediately, and the provider’s waiter re-invokes the is_complete handler on query_interval until the endpoint is InService. The provider’s total_timeout (1 hour) bounds the wait, not the timeout of any single Lambda invocation:
On stack deletion, the on_event handler deregisters the scalable target to clean up.
Attach Scaling Policy
There is a brief window after RegisterScalableTarget returns where the target isn’t yet queryable. Attach Scaling Policy uses the same asynchronous completion pattern: the on_event handler returns immediately, and the is_complete handler reports completion only once the scalable target is queryable, at which point it applies the policy. The provider’s total_timeout (15 minutes) bounds the wait:
On stack deletion, the on_event handler deletes the scaling policy to clean up.
Cleaning up
To avoid incurring future charges, delete the resources:
This removes the SageMaker AI endpoint, endpoint configuration, model, Lambda functions, IAM roles, Amazon CloudWatch alarms created by the target tracking scaling policy, and deregisters the scalable target.
Conclusion
In this post, we showed you how to use a reusable CDK construct to deregister and register auto scaling automatically to orchestrate SageMaker AI endpoint updates. The construct uses three CloudFormation custom resources with explicit dependency ordering and a ConfigHash property to keep auto scaling intact across deployments.
To get started, clone the sample-sagemaker-endpoint-autoscaling repository and follow the setup instructions. The repository includes an example stack you can deploy directly, or you can integrate the construct into your existing CDK stack.
For more information about Application Auto Scaling for SageMaker AI, see Automatically scale Amazon SageMaker AI models. For more information about CloudFormation custom resources, see Custom resources in the AWS CloudFormation User Guide.
