---
id: "f44164034d1ab5d3"
title: "CoreWeave connects custom training loops to model serving"
url: "https://thenewstack.io/coreweave-forge-training-loops"
link: "https://thenewstack.io/coreweave-forge-training-loops"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T16:30:00Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Urvashi Chowdhary"]
language: "en"
summary: "Production traffic shows failures that benchmarks or pre-deployment evaluations can’t fully reveal. It tells you which edge cases matter and what users need. Turning that signal into the next model version requires an upfront decision: does the model need to change, or is the problem in retrieval, context, prompts, tools, or serving? \n\n Changing weights won’t fix a failure elsewhere in the…"
tags: ["AI Engineering", "AI Infrastructure", "AI Operations", "sponsor-coreweave", "sponsored-post-contributed"]
orgs: ["CoreWeave", "OpenAI", "Meta", "Nvidia"]
topics: ["models & research", "products & launches", "agents & coding", "chips & infrastructure"]
content_source: "summary"
word_count: 1264
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# CoreWeave connects custom training loops to model serving

The New Stack · Urvashi Chowdhary · 2026-11-17

Production traffic shows failures that benchmarks or pre-deployment evaluations can’t fully reveal. It tells you which edge cases matter and what users need. Turning that signal into the next model version requires an upfront decision: does the model need to change, or is the problem in retrieval, context, prompts, tools, or serving? 

 Changing weights won’t fix a failure elsewhere in the system. When the model is the right place to intervene, production evidence can improve both quality and economics. A smaller model might reproduce a more expensive model’s behavior; better examples might improve consistency; an outcome-based reward might suit the task. Refining a capable model can also avoid another migration to a new model generation. 

 Choose a technique from the failure mode 

 Model distillation fits when a stronger model already produces the desired behavior and you want a smaller, more economical model to reproduce it. Supervised fine-tuning (SFT) fits when high-quality examples can teach more consistent behavior. Reinforcement learning (RL) fits when you can reliably evaluate an outcome but cannot readily specify the ideal response in advance. 

 “Changing weights won’t fix a failure elsewhere in the system. When the model is the right place to intervene, production evidence can improve both quality and economics.” 

 You may use all three approaches over a model’s lifecycle. Choose from the evidence in your workload, even when that means using a technique that takes more setup. 

 Production traces have to become training data. Post-training needs compute and orchestration , and the resulting model has to be evaluated and returned to inference . That is the work of closing the loop . In RL, inference generates rollouts during training, and new weights must return to serving throughout the run. 

 At Fully Connected 2026 , we introduced CoreWeave Model Distillation , CoreWeave RL Rollouts on CoreWeave Inference, and a programmable training API. These workflows connect in CoreWeave Forge . The programmable API is in limited preview, with an official launch planned for later in 2026. 

 Keep the data fresh when the base model stays 

 CoreWeave Model Distillation provides a managed workflow. CoreWeave Agent Lens captures inference traffic as the application runs. The workflow turns it into training data, relabels weak outputs, tests base models and hyperparameters, deploys candidates to Serverless Inference , and compares them with the production model. 

 If the model already has the capabilities your task needs, fresh production data can improve its fit without changing the serving profile you know. Compare the new version against the model already running before you move traffic. 

 Method used this workflow to revisit a model it had already deployed. In 2024, it used OpenPipe to train Llama 3.1 8B to navigate bank interactive voice response (IVR) systems, using GPT-4o outputs. In August 2026, Method brought in fresh production data, relabeled it with GPT-5.6 Sol, and trained another version. The candidate won 57.5% of head-to-head evaluations against the deployed version. 

 The base model had not changed. Fresh production data and Model Distillation in Forge made another iteration possible sooner. The 57.5% result is the share of head-to-head evaluations the new version won. 

 Control the training recipe in Python 

 For teams that want to design their own learning process, the programmable training API for Serverless Training separates training logic from infrastructure operations. You write a Python loop; CoreWeave manages the compute and underlying training infrastructure. 

 Here’s one way to combine RL updates with periodic supervised updates on verified demonstrations. The example creates a learner and serving adapter, uses an Adam optimizer with a learning rate of 1e-5, and publishes updated weights to the sampler after each step. 

Python
learner = await training.create_learner(model=model, lora=lora)
sampler = await serving.create_adapter(name="sampler")
optimizer = AdamConfig(learning_rate=1e-5)

for step in range(num_steps):
 trajectories = await run_agent(sampler, tasks)
 update = learner.batch()
 update.forward_backward(
 build_rl_batch(trajectories), loss="importance_sampling"
 )
 update.optim_step(optimizer=optimizer)

 if (step + 1) % sft_interval == 0:
 update.forward_backward(next_demo_batch(), loss="cross_entropy")
 update.optim_step(optimizer=optimizer)

 update.publish_weights(to=sampler)
 await update.result()

await (await learner.save_state("final")).result()
await learner.close()

 The rollout and batch helpers are illustrative. Your agent logic, reward calculations, and data preparation belong in those helpers. The loop uses importance-sampling loss for RL and cross-entropy loss for demonstrations, then waits for the update result. It saves the final learner state and closes the learner. 

 You choose how often demonstrations enter the loop, how rewards are calculated, and how the recipe evolves. SFT, RL, and distillation share the training primitives, while the platform runs the distributed systems underneath. 

 Willow began with supervised learning, then added RL scorers to reduce filler words, improve readability, and remove self-corrected phrases. The scorers were combined into a reward function. Lawrence Liu, Willow’s chief technology officer and co-founder, reported better text styling, emoji handling, and responsiveness to commands than in the deployed model. 

 Remove checkpoint reload delays from RL 

 RL serving needs enough rollout generation, alignment with the policy being trained, and timely weight updates. The trainer, reward logic, and environment can stay where they are while CoreWeave Inference handles this part of the loop. 

 CoreWeave RL Rollouts is built on Nvidia Dynamo with vLLM support. When the trainer writes a checkpoint, the service hot-loads it into a live deployment while preserving in-flight requests and endpoint availability. It returns training metadata: token log probabilities (logprobs), token IDs, and expert routing for mixture-of-experts (MoE) models. 

 “When the trainer writes a checkpoint, the service hot-loads it into a live deployment while preserving in-flight requests and endpoint availability. Serving uses the trainer’s current policy weights, removing staleness and redeployment delays that would otherwise hold up the next batch of rollouts.” 

 Checkpoints can be full snapshots or incremental deltas, reducing synchronization after the first upload. Serving uses the trainer’s current policy weights, removing staleness and redeployment delays that would otherwise hold up the next batch of rollouts . 

 Measure quality and infrastructure separately 

 We validated the workflow with Nvidia and you.com by post-training Nvidia Nemotron 3.5 Lightning for web search. The run combined SFT and RL with you.com’s search tools inside the training loop. 

 BrowseComp accuracy increased from a 36.97% baseline to 45.45%, a reported 22.94% relative improvement. Average tool calls fell 30.24%. Separately, hot-loading checkpoints into a live deployment was approximately 15 times faster than traditional redeployment cycles. 

 Better search tooling, post-training refinement, and harness improvements worked together to improve accuracy and reduce tool calls. Hot-loading cut the time spent waiting for checkpoint synchronization. If you’re trying to make a smaller or more efficient model competitive with models an order of magnitude larger, that extra training time matters too. 

 Keep the model connected to its experiment 

 CoreWeave Forge connects production inference , training, and serving again. Model Distillation supplies a managed path. The programmable API lets researchers control the training loop without managing its infrastructure. RL Rollouts supports teams keeping their own trainer while using CoreWeave for rollout inference. 

 Models produced by serverless training return as tagged artifacts that can move into Serverless Inference without a separate registry handoff. Experiments remain logged beside them, keeping the run, model, and eventual deployment connected. 

 “Choose a failure you can reproduce, use it to guide the training method, and compare the candidate with the model serving users.” 

 Choose a failure you can reproduce, use it to guide the training method, and compare the candidate with the model serving users. Keep the production examples, evaluation, and resulting artifact together so your team can use them again. 

 The CoreWeave Forge blog and announcement press release provide context on the capabilities introduced at Fully Connected 2026. CoreWeave also plans further engineering explanations of Model Distillation, the programmable training API, and RL Rollouts. 
 The post CoreWeave connects custom training loops to model serving appeared first on The New Stack .
