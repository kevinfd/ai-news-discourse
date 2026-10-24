---
id: "95364ce770790d21"
title: "Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide"
url: "https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide"
link: "https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-23T17:48:54Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Daniel Quang"]
language: "en"
summary: "Most fine-tuning teaches a model to produce a better answer to a single prompt. Agentic tasks are different. An agent that files an expense report or triages a support ticket takes a sequence of actions, and each step depends on what came before. There’s rarely one correct sequence to imitate, and the only reliable feedback is whether the whole sequence succeeded. Supervised fine-tuning has no…"
tags: ["Amazon SageMaker AI", "Expert (400)", "Technical How-to"]
orgs: ["Amazon", "OpenAI"]
topics: ["models & research", "agents & coding", "policy & regulation", "business & funding"]
content_source: "fulltext"
word_count: 3327
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide

AWS Machine Learning Blog · Daniel Quang · 2026-10-23

Artificial Intelligence
Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide
Most fine-tuning teaches a model to produce a better answer to a single prompt. Agentic tasks are different. An agent that files an expense report or triages a support ticket takes a sequence of actions, and each step depends on what came before. There’s rarely one correct sequence to imitate, and the only reliable feedback is whether the whole sequence succeeded. Supervised fine-tuning has no labels for that, and single-turn reinforcement learning cannot credit a decision made three steps before the outcome.
Multi-Turn Reinforcement Learning (MTRL) on Amazon SageMaker AI trains models on exactly that signal. SageMaker AI sends prompts to an agent you host on Amazon Bedrock AgentCore, or on your own infrastructure, such as Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Compute Cloud (Amazon EC2), or AWS Fargate, through an AWS Lambda forwarder. The example here uses AgentCore. The agent calls the policy model being trained, acts in your environment over as many turns as the task needs, and reports one reward when the episode ends. You don’t specify the right trajectory, only how to score the result.
This post uses Wordle, a game in which a player has six tries to guess a hidden five-letter word, as the example. After each guess, every letter turns green if it is in the right position, yellow if it’s in the word but in a different position, and gray if it isn’t in the word. The game suits MTRL because the rules are few, each guess depends on the feedback from the last, and the outcome is scored objectively. Wordle is a teaching example, and frontier models already play it well. In practice, you would use MTRL to make a small, low-cost model good at a multi-step task specific to your business, such as an internal workflow that public models were never trained on. The same pipeline applies to that setting.
In our run, MTRL took gpt-oss-20b from a 61 to an 84 percent solve rate on held-out words at its default reasoning effort, and from 15 to 69 percent at the low effort it trained at, for about $339 in training tokens. In this post, we walk through the pipeline end-to-end: deploying the agent and reward to AgentCore, preparing the dataset, training, monitoring in MLflow, and evaluating at serving settings. We also share the reward-design mistakes and training failures we hit. Your datasets, agent, and trained model stay in your AWS account and are not used to train the base models. All code is in the accompanying aws-samples repository.
Solution overview
The system has two halves. SageMaker AI owns the training job and the policy model. AgentCore hosts the agent, the Wordle environment, and the reward function. The following diagram shows how they connect.
For every rollout, the MTRL service invokes the AgentCore runtime, a capability of Amazon Bedrock AgentCore, with one training row, which holds one secret word. A Strands agent in the runtime calls the policy model through the SageMaker Job Runtime’s OpenAI-compatible endpoint. The model plays up to six guesses through one tool, guess_word, and after each guess the environment returns per-letter feedback and a summary of what is known. When the game ends, the agent returns one reward. Group Relative Policy Optimization (GRPO) uses the spread of rewards across several rollouts of the same word to update a Low-Rank Adaptation (LoRA) adapter on the policy model.
Three design points matter for what follows:
- The agent and reward live in one place. A single Python file deployed to AgentCore holds the environment, the tool, and the scoring function.
- The dataset carries only the secret word. The word lists bundled with the agent are built from the open-source SCOWL word lists and are used only for scoring.
- The reward is outcome-dominant. A solve pays 1.05–1.55 depending on speed, a loss pays -0.5, and never making a valid guess pays -1.5. A small shaping term rewards good strategy within each tier.
Supported models and AWS Regions
MTRL is serverless: you pick a base model and the service provisions the training and sampling infrastructure. At the time of writing, it supports the following base models, each trained with a LoRA adapter:
We chose GPT-OSS-20B because it has the lowest per-token price of the four and its reasoning effort is controllable per request. See the MTRL documentation for the current list.
Pricing
You don’t choose instances or size a cluster. You pay per million tokens in three dimensions, priced by base model:
- Prefill: input tokens the policy model processes. These accumulate in a multi-turn task, because every turn re-reads the history.
- Sample: tokens the policy model generates, including reasoning tokens.
- Train: tokens processed in the backward pass that updates the LoRA adapter.
The 100-step run consumed 491.6 million prefill, 159.7 million sample, and 643.3 million train tokens across 105,486 rollouts in 12 hours 40 minutes. At GPT-OSS-20B list prices in the US East (N. Virginia) Region (us-east-1) at the time of writing, that is about $339:
The train dimension dominates and scales with trajectory length, so shorter games and less verbose reasoning cut the bill. The AgentCore runtime bills separately for the vCPU and memory the agent uses. For this run, that was about $79, from the runtime’s Amazon CloudWatch usage metrics at us-east-1 list prices. DescribeJob reports the token counts under BillableTokenUsage. See Amazon SageMaker AI pricing for current rates.
Prerequisites
To follow this walkthrough, you need the following. See also the MTRL prerequisites.
- Python 3.10 or later, uv, Node 20 or later, and the AgentCore CLI (npm install -g @aws/agentcore). See Get started with Amazon Bedrock AgentCore for installation and the IAM permissions the CLI needs.
- botocore 1.43.37 or later, on the machine that launches the job. This is the first version that includes the AgentRFT CreateJob operation.
- Two AWS Identity and Access Management (IAM) roles, described in Step 1.
- An Amazon Simple Storage Service (Amazon S3) bucket in the same Region as the agent. The training job must also run in that Region, because CreateJob rejects a cross-Region runtime ARN.
Step 1: Create the IAM roles
MTRL uses two roles, and one of them has a trust policy that the general SageMaker AI documentation doesn’t mention.
Agent runtime role. agentcore deploy creates this role for you. It trusts bedrock-agentcore.amazonaws.com and needs the AmazonSageMakerJobRuntimeAccess managed policy, which lets the agent call the policy model and report rewards. The CDK stack in the sample repository attaches this policy automatically.
Training job role. You create this one. It must trust job.sagemaker.amazonaws.com with both sts:AssumeRole and sts:TagSession, and it needs the AmazonSageMakerJobFullAccess managed policy.
Note: The trust principal is job.sagemaker.amazonaws.com, not sagemaker.amazonaws.com. With the generic principal, CreateJob fails with “Could not assume role,” and the message names the correct principal only after retries.
Step 2: Deploy the agent to Amazon Bedrock AgentCore
Clone the sample repository, set your account and Region in Wordle/agentcore/aws-targets.json, and deploy:
The CLI builds the agent’s dependencies for the runtime’s Linux ARM64 platform, creates the execution role with AmazonSageMakerJobRuntimeAccess attached, and deploys through AWS CloudFormation. We recommend it over uploading a code package on the console, where it’s common to get the roughly 700 MB of compiled dependencies or the policy attachment wrong. Note the runtime ARN in the output for the training job.
The runtime reads two environment variables from agentcore.json. REASONING_EFFORT=low sets reasoning_effort on every request to the policy model. In our evaluation jobs, low effort used 63 to 83 percent fewer sample tokens per game than medium. REASONING_PROMPT_HINT=true also adds “Reasoning: low” to the system prompt, which is how gpt-oss reads the setting in its Harmony chat format. Neither variable gives the model any hint about the secret word.
The agent is one file, main.py. Simplified, its entrypoint looks like the following. For your own task, you change the task parsing, the tools, and the reward:
Important: The sagemaker_rft_handler decorator does not start an HTTP server by itself. Wrap it with BedrockAgentCoreApp and @app.entrypoint, with the entrypoint decorator outermost. Without this, every invocation times out after 30 seconds.
Step 3: Verify the runtime
Before spending GPU time, confirm the whole chain works with a payload shaped like the one the training service sends. The repository includes one as Wordle/payload.json:
The fake job ARN is expected to fail, and the way it fails is the proof. Put your own account ID into it first: for a job ARN in another account, the service returns a 403 before it checks whether the job exists, which looks like a broken IAM setup. From the Wordle directory, run:
In the runtime’s Amazon CloudWatch logs, you see the agent parse the prompt, authenticate to the Job Runtime endpoint, and receive a 400 error reading “Could not find job.” That failure confirms that parsing, authentication, and error reporting work. The command itself prints {“reward”: -1.5}, because the agent never reached the policy model. A 403 reading “not authorized to access this resource” means the job ARN still names another account. A 30-second timeout instead means the HTTP server is not starting (see the Important note in Step 2).
Step 4: Prepare the dataset
The MTRL dataset has no target responses, transcripts, or labels. Each row is one task for the agent to attempt. Here are the first three rows of the training file:
The service reads the prompt column (or the first column) and passes the string to your agent verbatim, without parsing it. We made the string a small JSON object with three fields:
- prompt: the instruction the agent shows the policy model, identical on every row.
- answer: the secret word. Only the environment and the reward function use it. The policy model never sees it.
- id: a row ID for tracing a rollout in the logs back to its source row.
The sample repository’s make_dataset.py draws 640 training words (five full batches of 128) and 128 validation words from the answer list with no overlap, so the validation solve rate measures generalization. The service also accepts Apache Parquet, JSON arrays, and CSV. Upload both files to Amazon S3:
Because the service never inspects the prompt string, a production task can pack a full message list, tool configuration, or reward specification into it. See the MTRL documentation for examples, including how to protect sensitive content in the string.
Step 5: Launch the training job
The launcher uses the MultiTurnRLTrainer class from the sagemaker-train SDK. Point it at the runtime ARN from Step 2, the role from Step 1, the datasets from Step 4, and an MLflow app for metrics. The MLflow app is required, so if you don’t have one, create it first with aws sagemaker create-mlflow-app:
The launcher overrides three hyperparameters and leaves every other one at the gpt-oss-20b default. It sets sampling_max_tokens to 8192, the service maximum, because at the default of 4096 gpt-oss often ran out of tokens while reasoning, before its first tool call. It sets max_epochs to 20 and max_steps to 100: 640 rows at the default global_batch_size of 128 is 5 steps per epoch, and with the default group_size of 8, each step plays 1,024 games. The job moves through Starting, Downloading, and Pending before reaching Training. After it’s training, your AgentCore runtime begins receiving rollout invocations.
Important: Don’t redeploy the agent while a job is running. Redeploying restarts the runtime, in-flight rollouts see no sampling requests, and the service fails the entire job.
Step 6: Monitor training in MLflow
The service logs reward, token, and turn statistics at every step and runs validation every val_every steps. The metric to watch is val/reward/pass_at_1, the fraction of held-out words solved. Every solve scores at least 1.01, so it clears the service’s success_threshold of 1.0 and pass@1 counts it. The following chart is built from this run’s MLflow history:
Training reward climbs to about +0.57 within 15 steps and holds there. Validation reward stays lower, mostly because of temperature 1.0 versus 0 rather than overfitting (see Step 7). The validation solve rate jumps from 2 to 31 percent in the first 10 steps, then moves between 35 and 48 percent. With 128 words, those swings are mostly noise. We did not test whether more steps help at serving settings.
The runtime’s OpenTelemetry traces in CloudWatch record every model turn and tool call. Here is one game the trained model played during an evaluation job (medium effort, temperature 1.0), with the reasoning trimmed. The secret word was PASTE:
A trained-model rollout from the AgentCore runtime traces. The model keeps green letters in place, never reuses a gray letter, and uses each yellow letter to rule out positions, though nothing in the training data showed it how.
Step 7: Evaluate the trained model at serving settings
When the job completes, its page in SageMaker AI Studio shows the status and the model package group that holds the trained model. DescribeJob, with JobCategory set to AgentRFT, returns the output model package ARN and the billable token counts.
An evaluation job (JobCategory set to AgentRFTEvaluation) plays your evaluation prompts through the same AgentCore runtime and reward, on the base model or the trained package, and logs eval/reward/pass_at_1 to MLflow. Unlike training validation, you can set the temperature. The repository’s launcher runs evaluations back to back, because the default quota allows one evaluation job at a time (you can request an increase):
Each 128-word evaluation took four to seven minutes. Reasoning effort comes from the agent’s environment variables, so to change it you edit REASONING_EFFORT, redeploy, and evaluate. We evaluated both models at low and medium effort and at temperature 0 and 1.0:
The gray segment of each bar is the base model and the blue segment is the gain from training. The low-effort, temperature-0 pair is the training job’s validation at steps 0 and 100. The medium-effort, temperature-1.0 trained result is the mean of two runs (80 and 88 percent).
At temperature 0, both models often end the game without a solve, at either effort. With sampling on, medium effort adds 15 points for the trained model and 46 for the base model. The adapter adds 14–54 points in every setting, so what training taught transfers across settings.
The training job’s own validation curve in MLflow told a different story: it peaked at 48 percent at step 90 and ended at 37 percent, scored at temperature 0. The hyperparameters reference recommends temperature 0 for evaluation because greedy decoding makes curves deterministic and comparable across runs. We report temperature 1.0 because that’s how we serve the model. At medium effort and temperature 1.0, the trained model solves 84 percent of held-out words, up from 61 percent for the base model.
Tip: Evaluate at the settings you will serve at. The training curve says this adapter ends at 37 percent. At serving settings it solves 84 percent. The evaluation jobs that show this cost about $1.20 in tokens and took about an hour.
Step 8: Clean up
Training and evaluation jobs stop billing when they complete, but the AgentCore runtime, its IAM role, the MLflow app, and the S3 objects persist. From the project directory:
Because agentcore remove all rewrites the files under agentcore/, run git checkout -- agentcore/ if you want to redeploy later. Deleting the AgentCore-Wordle-default CloudFormation stack removes the same resources and leaves the files alone. The training job role and the model packages are not billed.
Deep dive: Designing the reward
Our reward needed one revision, and the mistake is a common one.
The first design summed the per-guess scoring from the wordle-lora-rl project over the whole game. That scoring works there because each guess is an independent training sample. Summed into one reward per game, it produced two inversions we found only by reading traces:
- A lost game paid positive reward. Six turns of bonuses added up to about +0.49.
- Solving on turn 1 scored below solving on turn 3. A first-guess solve earned +0.99 and a third-guess solve earned +1.61, because the extra turns collected more bonuses.
The fix separates a dominant outcome term from a small, bounded shaping term:
The outcome term is set entirely by how the game ended:
The shaping term is that per-guess scoring, summed over the game:
- Penalties for contradicting a known green, yellow, or gray letter, for repeating a guess, and for words outside the dictionary.
- An entropy bonus for a strong opening word.
- Bonuses for trying new letters and for shrinking the set of remaining possibilities.
The sum is clipped to [-1, 1] and scaled by 0.04 for a solve and 0.15 for a loss, so it separates games with the same outcome but never moves a game into another tier. With typical shaping values:
A faster solve now always beats a slower one, every solve beats every loss, and never playing is the worst outcome. Our first fix used a single weight of 0.15, which let a guess-3 solve with full shaping (+1.45) outscore a guess-2 solve with the minimum (+1.25). Adjacent guess counts are 0.1 apart, so a smaller solve weight of 0.04 removes the overlap, and the worst solve (+1.01) still clears the 1.0 success threshold. Shaping still matters because GRPO learns from reward variance within a group, so two lost games that differ in clue consistency still teach the model something. As the SageMaker AI documentation advises, start with an outcome-based reward, add shaping sparingly, and check the reward on real trajectories.
Deep dive: What went wrong, in the order you will hit it
Each of these cost at least one training run.
- Bearer tokens under concurrency. Minting a token with a fresh botocore session per call starved the credential provider at 32 concurrent rollouts, and caching tokens for an hour returned 403 errors as credentials rotated. The fix is one self-refreshing session, a short cache, and a re-sign on 403.
- A rollout that never reaches the policy model fails the whole job. When every model call in a rollout failed authentication, the service ended the job with “No sampling requests were received.” Returning an error status fails it too, so always return a reward. A game where the model is sampled but never makes a valid guess is fine: it scores -1.5, and the 100-step run had 51 of them in about 105,000 rollouts.
- Tool calls drift into plain text. At too high a learning rate, the model wrote tool calls as text, every rollout got the same floor reward, and the gradient vanished. The agent now recovers guesses from raw text with a small formatting penalty.
- The plateau. Training reward stopped rising after about step 15 and validation stopped improving after about step 30, though at temperature 0 validation understates the model (Step 7). A curriculum that seeds games with prior guesses, or more rollouts per word than the default group_size of 8, is what we would try next.
Conclusion
MTRL on SageMaker AI trains a model on the outcome of a whole episode. That fits agentic tasks, where the right trajectory is unknown and only the result can be scored. We used a single episode-level reward. When intermediate steps can be scored too, MTRL also accepts one reward per turn through the UpdateReward API. In this post, an open-weight 20B model reached an 84 percent solve rate at serving settings, up from 61 percent, for about $339 in training tokens and about $79 in AgentCore runtime usage. The 37 percent the training curve reports is an artifact of how the training job scores validation, so evaluate at the settings you will serve at.
The same pipeline applies to internal procedures, tools, and workflows that public models were never trained on.
To get started, clone the sample repository, follow the preceding steps, and run the smoke test in Step 3 before committing GPU time. For the underlying APIs, see the SageMaker AI MTRL documentation.
