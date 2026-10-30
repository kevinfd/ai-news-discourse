---
id: "aa702b033bfda9cd"
title: "Lend and borrow resources across teams with AWS Batch’s quota management for SageMaker Training jobs"
url: "https://aws.amazon.com/blogs/machine-learning/lend-and-borrow-resources-across-teams-with-aws-batchs-quota-management-for-sagemaker-training-jobs"
link: "https://aws.amazon.com/blogs/machine-learning/lend-and-borrow-resources-across-teams-with-aws-batchs-quota-management-for-sagemaker-training-jobs"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-29T16:58:57Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Michelle Goodstein"]
language: "en"
summary: "With the launch of AWS Batch support for Amazon SageMaker Training jobs, customers gained a new fully managed way to queue, schedule, and retry machine learning (ML) training workloads without building their own infrastructure. Instead, they use the queuing and scheduling features of AWS Batch. As organizations scale their artificial intelligence and machine learning (AI/ML) operations and…"
tags: ["Advanced (300)", "Amazon SageMaker AI", "AWS Batch", "Technical How-to"]
orgs: ["Amazon"]
topics: ["jobs & society", "business & funding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1501
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Lend and borrow resources across teams with AWS Batch’s quota management for SageMaker Training jobs

AWS Machine Learning Blog · Michelle Goodstein · 2026-10-29

Artificial Intelligence
Lend and borrow resources across teams with AWS Batch’s quota management for SageMaker Training jobs
With the launch of AWS Batch support for Amazon SageMaker Training jobs, customers gained a new fully managed way to queue, schedule, and retry machine learning (ML) training workloads without building their own infrastructure. Instead, they use the queuing and scheduling features of AWS Batch. As organizations scale their artificial intelligence and machine learning (AI/ML) operations and onboard more teams, coordinating access to shared graphics processing unit (GPU) capacity can introduce additional communication, coordination, and configuration overhead for administrators. This overhead includes setting up separate queues, adjusting capacity limits, and carefully orchestrating the right workloads to get the right resources at the right time. A core value proposition of AWS Batch is helping customers increase utilization of their compute, and as training environments grow, so does the opportunity to do more with existing capacity.
Working backward from customers managing multi-team training environments, we heard a consistent request: give us a way to define allocations per team or project, share idle capacity automatically, and run our highest-priority workloads first. This request led us to build quota management, a new scheduling capability for AWS Batch. Administrators can use it to divide compute capacity into quota shares, organized by team, project, or workload. Each quota share uses configurable resource-sharing strategies that maximize GPU utilization while honoring each team’s allocation when it matters most.
This post shows how quota management works, including how to configure quota shares with lending and borrowing strategies, set up in-share preemption for priority workloads, and get started using the SageMaker Python SDK.
Quota shares and preemption
Administrators can allocate and share constrained GPU resources by defining a quota share for separate entities, such as individual teams or projects. Each quota share includes compute quotas (capacity limits) and resource-sharing strategies for idle compute. These strategies determine whether idle compute is reserved until jobs arrive (RESERVE), lent to other quota shares that have work available (LEND), or both lent when idle and borrowed when the share has work that might benefit (LEND_AND_BORROW).
A quota share operates as a virtual queue nested hierarchically within an associated job queue. When scheduling jobs for a job queue, AWS Batch prioritizes quota shares that are under their capacity limits as it iterates through the associated quota shares. If jobs arrive in a quota share that has lent out its capacity, AWS Batch performs cross-share preemption. This reclaims resources for the lending quota share, so administrators don’t need to track down the jobs borrowing capacity and terminate them on their own. If jobs arrive in a quota share that is at or above its capacity limit, AWS Batch checks whether there’s available capacity to borrow from another quota share. If so, workloads can run using otherwise-idle capacity.
You can turn on priority-based in-share preemption when you configure a quota share. Where cross-share preemption reclaims lent capacity as jobs arrive in a lending quota share, in-share preemption preempts lower priority jobs that are in the SCHEDULED, STARTING, or RUNNING state. This allows higher priority jobs at the front of the queue to start running sooner.
Prerequisites
Before you proceed with this example, you must have an AWS account with permissions to create and manage AWS Batch resources. For this example, see the sample IAM permissions needed to invoke AWS Batch and SageMaker APIs.
The example uses the SageMaker Python SDK v3. Complete the setup required to install a compatible version of the SageMaker Python SDK:
Configuring quota management resources
Using the new quota management capabilities requires creating a Scheduling Policy that contains a quotaSharePolicy, a Service Environment that specifies its capacity limits in terms of specific instances, and a SageMaker Training job queue that is connected to both. After that, you can associate quota shares to a job queue. The user guide has AWS Command Line Interface (AWS CLI) and console examples for configuring quota management resources and quota shares. An end-to-end example of quota management integrated with the aws_batch module in the SageMaker Python SDK v3 is contained in a sample notebook. In this example, we step through code snippets that summarize the key components, and use the helper functions from the notebook to create a Scheduling Policy, Service Environment, Job Queue, and three Quota Shares.
The three quota shares configured here represent three different projects. Each has the same capacity limit set: a single ml.g5.xlarge instance. The QS1 quota share represents background jobs. For this project, you want to run the most important background job first and borrow as much spare capacity as is available. Within this quota share, no jobs are urgent, and preemptions are acceptable because all jobs use checkpointing. This quota share uses the LEND_AND_BORROW resource-sharing strategy and has in-share preemption turned on. Higher priority jobs within the same quota share can then preempt running jobs that are lower priority.
QS2 represents medium priority workloads. Teams choosing this configuration would prefer to wait for capacity to become available rather than endure additional preemptions. Those preemptions come from borrowed capacity being reclaimed or from in-share preemptions because of higher priority job submission. This is appropriate for shorter jobs, or when most submitted jobs have similar priorities. The quota share still benefits from job priority being taken into consideration at job dispatch. Submitted jobs trigger AWS Batch to reclaim any lent capacity needed to run the jobs.
QS3 represents workloads that need to start as quickly as possible with minimal interruptions. It’s configured to reserve capacity and neither lends nor borrows to other quota shares. It doesn’t experience cross-share preemptions, because its workloads don’t exceed their capacity limits. By also turning off in-share preemption, workloads submitted to this quota share are not preempted by AWS Batch as long as the capacity limit is unchanged.
These quota share configurations are inputs to the create_quota_management_resources function in the sample notebook, which also configures the corresponding Scheduling Policy, Service Environment, and Job Queue with the constant names chosen.
Submit SageMaker Training jobs to QS1
The aws_batch module within the SageMaker Python SDK has been extended to allow programmatic submission of SageMaker Training jobs to a quota-management-enabled AWS Batch job queue. To demonstrate these new capabilities, we use a Hello World ModelTrainer that’s submitted to the job queue. The following code snippet identifies an image URI to use based on the Region and instance type selected.
We use this image URI within a basic hello world model trainer example:
To use the job queue within the SageMaker Python SDK, provide the queue name to the TrainingQueue constructor within the aws_batch module.
We can then submit three jobs to QS1, our background jobs quota share. The first job submitted has the highest priority, followed by the medium priority job, and then the lowest priority job. As nothing is currently running in QS1 or QS2, two instances’ worth of jobs should start, corresponding to the first and second jobs submitted (as they had the highest relative priority). Note that because this is only a hello world training job, it doesn’t require data, but typically a ModelTrainer requires data to perform training.
Submitting jobs to QS2 triggers cross-share preemption to reclaim lent capacity
The team that owns QS2 might discover they have work to perform and submit a job to QS2. Doing so triggers a preemption of capacity back from QS1, which is currently borrowing that capacity (QS3’s capacity isn’t configured to be borrowed). This is a cross-share preemption.
Updating job priorities in QS1 triggers in-share preemption to run highest priority jobs
If a scientist realizes that the qs1_job_low job in QS1, which is still RUNNABLE, needs to begin running now because of changing priorities, they can use the new UpdateServiceJob API to increase the priority of an already submitted job in QS1. Because there’s no available capacity to borrow, this kicks off an in-share preemption, so that the job currently running is preempted and qs1_job_low can begin.
(Optional) Clean up created resources
To clean up the resources created in this post, run the following code:
Conclusion
In this post, we covered quota management, a new scheduling capability in AWS Batch, and how to use it with SageMaker Training jobs and get started setting up quota shares for your own projects. For more details, see the AWS Batch quota management user guide.
AWS Batch with quota management can help your organization increase compute utilization and more effectively prioritize your teams and workloads, freeing up time for your infrastructure admins and ML scientists. By implementing quota management, your teams can focus on their workloads and reduce time spent managing and coordinating infrastructure. This capability is especially powerful with Amazon SageMaker AI training plans, so that your organization can reserve capacity in the quantity you need, during the time you need it. By using AWS Batch with SageMaker AI, you can make full use of the training plan. We encourage you to try out this new capability so it can make a meaningful impact in your operations.
