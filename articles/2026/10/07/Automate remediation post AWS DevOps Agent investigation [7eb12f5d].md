---
id: "7eb12f5d530ed4a6"
title: "Automate remediation post AWS DevOps Agent investigation"
url: "https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-07T15:46:49Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Michele Scarimbolo"]
language: "en"
summary: "Reducing the time between incident detection, investigation, and remediation is a critical priority for organizations running production workloads on AWS. When an issue arises, on-call engineers often need to quickly diagnose the problem across application components, identify the root cause, and apply the fix, often in the middle of the night. \n AWS DevOps Agent , an AI powered agent that…"
tags: ["Advanced (300)", "DevOps", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2044
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Automate remediation post AWS DevOps Agent investigation

AWS Machine Learning Blog · Michele Scarimbolo · 2026-10-07

Artificial Intelligence
Automate remediation post AWS DevOps Agent investigation
Reducing the time between incident detection, investigation, and remediation is a critical priority for organizations running production workloads on AWS. When an issue arises, on-call engineers often need to quickly diagnose the problem across application components, identify the root cause, and apply the fix, often in the middle of the night.
AWS DevOps Agent, an AI powered agent that autonomously triages incidents all day based on correlated metrics, logs, and application topology, addresses the first part of this priority by providing root cause analysis (RCA) and recommended actions for resolution. However, to retain control and help prevent unintended changes, organizations typically keep their observability agents, including AWS DevOps Agent, in an observe-and-report mode, where the agent diagnoses issues but doesn’t modify production resources directly. In this post, we demonstrate how to use AWS Lambda Durable Functions, a capability of AWS Lambda, Amazon EventBridge, and Amazon Bedrock to create an automated remediation workflow that complements AWS DevOps Agent to complete the issue resolution step. This workflow transforms investigation summaries into pre-validated fixes ready for single approval action, helping you reduce mean time to resolution (MTTR) and free your on-call engineers from repetitive diagnostic work.
Solution overview
With AWS Lambda Durable Functions, you can build resilient multi-step applications and AI workflows that can run for up to one year without requiring you to manage additional infrastructure or write custom state management and error handling code. These functions automatically checkpoint progress, suspend execution during long-running tasks, and recover from failures while maintaining reliable progress despite interruptions.
The following diagram illustrates the solution architecture.
The workflow consists of the following steps:
- AWS DevOps Agent completes an incident investigation and emits an event containing symptoms, findings, and root cause analysis.
- Amazon EventBridge receives the investigation completion event and triggers the devops-agent-trigger function with the investigation content.
- The Lambda function packages the investigation summary and invokes the devops-agent-remediation-durable durable function.
- The durable function sends the investigation context to Amazon Bedrock, which analyzes the findings and looks for applicable remediations.
- Amazon Bedrock identifies and lists the available remediation tools from a curated allowlist of approved Lambda functions: devops-agent-lambda-tool.
- Amazon Bedrock proposes specific remediation actions based on the investigation findings and the available tools.
- For read-only actions, the durable function runs the remediation tools autonomously. For infrastructure changes, the workflow suspends and waits for human approval before proceeding.
- After approval, the durable function applies the remediation actions to the infrastructure using the selected tools.
The durable function runs as an agentic loop, iteratively calling Amazon Bedrock, executing approved tools, and feeding results back into the conversation until the remediation is complete. To keep automated actions safe and auditable, the orchestrator enforces a curated allowlist of remediation tools. Each tool is a purpose-built Lambda function that performs a specific, well-scoped action, such as reading a Lambda function configuration or updating an AWS Identity and Access Management (IAM) policy statement. Amazon Bedrock can only select and invoke tools from this approved set, which keeps the scope of automated actions controlled. The workflow further distinguishes between read-only operations and mutating operations. Read-only tools run autonomously without human intervention. Mutating actions that would modify infrastructure state cause the durable function to suspend execution and wait for human approval. This is where AWS Lambda Durable Functions provide a key advantage. The function checkpoints its progress and pauses for minutes, hours, or even days without consuming compute resources, then resumes exactly where it left off after it receives the approval signal. By the time the on-call engineer engages, the system has already gathered relevant configurations, correlated the root cause with available remediation actions, and prepared a set of pre-validated changes ready for one-click approval. The current implementation uses an approve or reject signal. Because the callback accepts an arbitrary JSON payload, you can extend the approval to carry parameter overrides or reviewer observations. These can be fed back into the Bedrock conversation to refine the proposed remediation before execution.
In the following sections, we walk through the implementation details, including the Amazon EventBridge rule configuration and the durable function orchestration logic. We then deploy the solution using the AWS Cloud Development Kit (AWS CDK).
Prerequisites
Before deploying this solution, verify that you have the following prerequisites:
- The AWS Command Line Interface (AWS CLI) installed and configured.
- Python 3.14 or later.
- The AWS CDK installed.
- An active AWS DevOps Agent space.
- (Optional) Kiro with the Agent Toolkit for AWS. The Agent Toolkit gives Kiro secure access to AWS APIs through a managed MCP Server with IAM-based access controls. If you use Kiro, the incident simulation, deployment, and cleanup steps in this post can be completed with natural language prompts instead of running CLI commands manually. To set it up, add the AWS MCP Server to ~/.kiro/settings/mcp.json (setup instructions). The repository includes a Kiro rules and agents file that gives Kiro the project context, deployment sequence, and safety conventions automatically.
Simulate the incident
To demonstrate the end-to-end workflow, we simulate a common scenario: a Lambda function that exceeds its configured timeout. This gives AWS DevOps Agent a real incident to investigate and sets the remediation workflow in motion.
To keep the focus on the remediation solution itself, the steps to create and invoke this test function are kept in the repository. It includes a ready-to-use devops-agent-timeout function and step-by-step instructions to deploy it, invoke it, and confirm the timeout error in Amazon CloudWatch Logs. For the full walkthrough, see the “Simulate the incident” section of the README.
After the function is deployed and has produced at least one timeout error, you’re ready to start an investigation with AWS DevOps Agent.
Deploy the solution using the AWS CDK
Complete the following steps to deploy the remaining solution resources:
Kiro: If you have Kiro with the Agent Toolkit for AWS configured (see Prerequisites), open the cloned repository in Kiro and ask: “Set up the Python environment and deploy the CDK stack. Show me what resources will be created before deploying.” Kiro reads the project rules from the repository, sets up the virtual environment, installs dependencies, and shows you the planned resources before deploying. It confirms each infrastructure change before executing, following the same human-in-the-loop pattern that the remediation solution itself uses. To deploy manually, follow these steps.
- Clone the AWS CDK code hosted on GitHub:
- Navigate to the directory sample-automate-remediation-post-devops-agent-investigation:
- Bootstrap the AWS CDK. This is required the first time you use the AWS CDK in a specific AWS environment (a combination of an AWS account and AWS Region).
- Deploy the stack:
The AWS CDK automatically provisions and configures the following resources:
- Three Lambda functions: 
         
  - devops-agent-trigger.
  - devops-agent-remediation-durable.
  - devops-agent-lambda-tool.
- Amazon EventBridge rule.
The AWS CDK automatically handles the IAM permissions using least-privilege principles and AWS security best practices. For example, Amazon EventBridge is granted lambda:InvokeFunction permissions for the devops-agent-trigger function. The stack grants the aidevops:ListJournalRecords permission to the devops-agent-trigger function so it can fetch investigation summaries from the AWS DevOps Agent journal. It also grants the bedrock:InvokeModel permission to the devops-agent-remediation-durable function so it can invoke Amazon Bedrock.
Validate the solution
With the remediation stack deployed and the devops-agent-timeout function failing with timeout errors, we can now walk through the end-to-end workflow.
Start an investigation with AWS DevOps Agent
Open the AWS DevOps Agent console, navigate to your agent space, and ask: “What is happening with the devops-agent-timeout function?”
The investigation starts and takes a few minutes to complete. During this time, AWS DevOps Agent autonomously correlates CloudWatch metrics, logs, and the function’s configuration to determine the root cause.
After the investigation completes, AWS DevOps Agent presents the root cause analysis, identifying that the function timeout is insufficient for the workload.
Verify the trigger Lambda execution
The investigation completion emits an Investigation Completed event to Amazon EventBridge.
The rule triggers the devops-agent-trigger Lambda function, which fetches the investigation summary from the AWS DevOps Agent journal. In the /aws/lambda/devops-agent-trigger CloudWatch log group, you can see the parsed summary that is sent to the devops-agent-remediation-durable durable function, including symptoms, root causes, contributing causes, and investigation gaps.
Monitor the durable function execution
Navigate to the Lambda console, open the devops-agent-remediation-durable function, and choose the Durable executions tab. Choose the new execution to inspect its checkpointed steps.
The durable orchestrator begins its agentic loop by sending the investigation context to Amazon Bedrock. In the first Bedrock call, the model analyzes the investigation summary and determines that it needs to inspect the current function configuration before proposing a fix. It selects the lambda_get_function_configuration tool from the allowlist. Because this is a read-only operation, it runs autonomously without requiring human approval. The step result shows the current configuration of the devops-agent-timeout function, confirming a timeout value of 3 seconds.
Amazon Bedrock proposes the remediation
With the current configuration confirmed, Amazon Bedrock proceeds to the next iteration. It reasons that the 3-second timeout is the root cause of the failures and proposes increasing it to 30 seconds. The Amazon Bedrock response contains both the reasoning and the tool call:
Because lambda_update_function_configuration is a mutating action, the durable function suspends execution and waits for human approval.
Figure 8: cloudwatch logs output of lambda durable function for approval request
Important: The investigation_summary sent to Amazon Bedrock, and the remediation it proposes, are AI-generated and should always be reviewed before approval. The human approval gate is the security control: the approver must inspect the full tool parameters (for example, the exact FunctionName and Timeout in a lambda_update_function_configuration call) and confirm the change is correct.
Using the AWS CLI:
Using the AWS Console:
Navigate to the durable execution, select the pending callback, and choose Send success to confirm:
In the input field, enter {'approved': true} and confirm.
Verify the fix
After approval, the durable function resumes, invokes the tool Lambda to update the configuration, and Amazon Bedrock confirms the remediation is complete. The updated devops-agent-timeout function now shows the new timeout value:
The final step output (bedrock-call-4) confirms the successful remediation:
This entire cycle, from incident detection to automated fix, required only a single approval action from the engineer. The system handled diagnosis, configuration retrieval, remediation proposal, and execution autonomously.
Clean up
Clean up the resources you created by completing the following steps:
Kiro: If you use Kiro with the Agent Toolkit for AWS, ask: “Clean up all resources from the DevOps Agent remediation demo: destroy the CDK stack, delete the devops-agent-timeout test function, its IAM role, and its CloudWatch log group.” Kiro removes resources in the correct order, confirming each destructive action before proceeding. To clean up manually, follow these steps.
- Delete the AWS CDK resources:
- Manually delete the devops-agent-timeout function that simulates the incident:
- Manually delete the IAM role and the CloudWatch log group of the devops-agent-timeout function:
Conclusion
This post demonstrated how you can automate issue remediation by using Lambda Durable Functions, Amazon EventBridge, and Bedrock in conjunction with the DevOps Agent. The solution picks up where AWS DevOps Agent leaves off, transforming investigation summaries into actionable remediation steps that run with human-in-the-loop approval. This approach reduces mean time to resolution because, by the time the on-call engineer engages, the system has already diagnosed the issue, gathered current configurations, and prepared a ready-to-approve fix. Safety remains central to the design: the allowlist restricts Amazon Bedrock to only invoke pre-approved tools, and the human approval gate helps prevent unintended changes from reaching production without explicit authorization. The architecture is also inherently extensible. Adding new remediation capabilities requires only configuration updates to the tool registry, not code changes to the orchestrator. And because AWS Lambda Durable Functions suspend without consuming compute resources during the approval wait, the solution remains cost-efficient even when approval cycles span hours or days.
To get started using this solution, download the complete AWS CDK template from the GitHub repository, and follow the steps in this post to deploy the solution in your environment.
We would love to hear from you. Share your experience implementing this solution, ask questions, or suggest improvements in the comments. You can also join the AWS Community Builders program to connect with other builders and share your serverless architecture patterns.
