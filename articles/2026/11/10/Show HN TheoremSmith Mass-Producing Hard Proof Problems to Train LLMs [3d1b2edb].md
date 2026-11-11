---
id: "3d1b2edb7f68f71f"
title: "Show HN: TheoremSmith: Mass-Producing Hard Proof Problems to Train LLMs"
url: "https://charleshuang.me/2026/09/27/theoremsmith"
link: "https://charleshuang.me/2026/09/27/theoremsmith"
source: "charleshuang.me"
domain: "charleshuang.me"
source_type: "community"
collector: "hackernews"
date: "2026-11-10T18:33:17Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["charles6huang"]
language: "en"
summary: "Making models better at formal verification will help push the boundaries of math research and significantly reduce the number of bugs in our code. Recently, training models on RL environments (tasks paired with verifiers that reward correct solutions) has driven big gains in model performance, and proofs are unusually easy to verify. Here we introduce TheoremSmith, a pipeline for generating…"
tags: []
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1799
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50444276"
score: 10
comments: 0
community: "Hacker News"
---

# Show HN: TheoremSmith: Mass-Producing Hard Proof Problems to Train LLMs

charleshuang.me · charles6huang · 2026-11-10

TheoremSmith: Mass-Producing Hard Proof Problems to Train LLMs
Table of Contents
TL;DR: Making models better at formal verification will help push the boundaries of math research and significantly reduce the number of bugs in our code. Recently, training models on RL environments (tasks paired with verifiers that reward correct solutions) has driven big gains in model performance, and proofs are unusually easy to verify. Here we introduce TheoremSmith, a pipeline for generating synthetic formal verification environments. It reliably creates multi-hour, frontier-difficulty tasks and can scale throughput effectively.
Why Improve Formal Verification?
Math research: In the past few months, we’ve seen a wave of AI-assisted math breakthroughs. Just in September, 10,000 agents derived a possible solution to the Navier–Stokes problem, and we also got a formalization of Fermat’s Last Theorem. These were possible because LLMs can brute-force countless proof strategies, work that would take humans years.
Verifying code: Software outages have increased 50% in the past two years. AI code generation has played a large part in this. Industry QA and testing standards cannot keep up with the rise of agentic coding. Formal verification allows us to mathematically prove the correctness of a program, significantly reducing (but not eliminating!) the number of bugs in code. Historically, formal methods have been too expensive to use for most systems; for example, the seL4 project reported a verification cost of $362 per source line of code. As a result, formal methods were usually only used for small and very risk-averse codebases, such as cryptographic libraries and microkernels. But with AI, these economics have flipped (about $0.10 per line of code). Formal verification is finally starting to become cheap enough for mainstream viability.
There are two halves to formal verification:
- Defining a specification. A specification is a statement about some behaviour. Here, it’s a mathematical statement that we wish to prove, like 2 + 2 = 4. Creating a specification is difficult and subjective because we must translate from natural language into formal logic—and sometimes we don’t even get natural language! Verifying a codebase often involves making tricky assumptions about what users “want.” The Boeing 737 MAX crashes are an example of the consequences of making a wrong assumption. So verifying whether a spec is faithful to the original intent demands great taste and is incredibly hard to do programmatically.
- Proving said specification. We can take some specification and construct a proof for why it is true. Checking that this proof establishes the specification is much easier. Proof assistants like Lean were built for this!
Verifiable Domains Are Low-Hanging
Recent efforts to post-train models with RL environments have led to considerable performance gains. For example, GLM 5.3 improved coding benchmark performance by 50% through post-training alone, using synthetically generated RL environments instead of human-generated ones.
Much of the effort involved in creating a good RL environment boils down to creating a good verifier. We need to accurately reward a model’s good work—and punish bad work and cheating—for models to learn effectively. Some domains are much easier to make verifiers for than others. It’s hard to put into words what makes a good painting, but we can easily determine whether a solution to a math problem is correct. Formal proofs are extremely easy to check. Tools like Lean and Rocq (formerly Coq) can tell us whether a proof (solution) is correct. Even though proof generation is highly verifiable, models are still subpar. VeriSoftBench, which tests how well agents complete subsets of real Lean repos, maxes out at a measly ~40%.
How can we make models better at writing proofs? How can we do this in a way that reflects real-world use cases, with huge, complex codebases and projects? To do this, we need to train models on tasks that mimic the real world.
Here we introduce TheoremSmith, our method for automatically creating exactly these kinds of difficult tasks.
Sowing Seeds
Here is how TheoremSmith creates tasks using existing Lean projects.
In Lean, proofs usually depend on smaller proven facts called lemmas (similar to functions in a programming language). Those lemmas can depend on other lemmas, so real Lean projects form long and complex chains of dependencies. If we represent a real Lean project as a directed acyclic graph (DAG), with each proof connected to its dependencies, we have a set of top-level theorems that are not dependencies of any other proof. These are the main results the project proves.
To create a seed task, we identify all of the top-level theorems that aren’t used by any other proofs. We then recursively remove the dependencies for each top-level theorem. A model will have to re-derive them from scratch later.
A small complication: A dependency can appear in a theorem’s statement (what we wish to prove) or only in its proof. If it appears only in the proof, we blank the dependency entirely, both the dependency’s statement and its proof. If it appears in the statement, we can’t blank the dependency. Then our agent would have to fill in our theorem statement, and it could rewrite it to be trivially true. Instead, we keep the dependency’s statement in the task and blank only the dependency’s proof.
Verifying the Agents
How do we know if an agent has actually written a correct proof for our statements? We could use Lean to check if the proof satisfies the specification, but there are many ways for an agent to cheat on the task. What if the agent sneakily changes the spec to something trivial? Agents could also inject code to break the environment or use new axioms that make their proof true when it isn’t, among other things.
To prevent reward hacking (when a model cheats on a task), we use Lean Comparator. Comparator checks our statement against an untrusted, AI-generated proof and safely determines whether it proves the statement. In a TheoremSmith task, agents must fill out an answer file for each proof they are tasked to complete. After the agents have finished all their proofs, we use Comparator to check whether the proofs satisfy our original task statements.
How does Comparator work?
Comparator takes a Challenge file containing the statement to prove and an AI-generated, untrusted solution file.
- Compile the solution inside a sandbox in case of malicious code injected by the AI.
- Compare the original statement with the statement in the compiled solution, checking whether they match.
- Use the Lean kernel to check whether the solution satisfies the validated statement.
- Check whether the solution uses any extra axioms (facts assumed to be true without proof).
Synthesis
For models to do real work using formal verification, we need them to get better at working for longer and handling much larger, more complex projects. One of the largest struggles in proving Fermat’s Last Theorem was collaboration between the many agents needed to tackle such a large proof. For agents to get better at solving long and complex problems, we need to create training data that’s equally long and complex.
We synthesize new, longer-horizon tasks from the seed tasks we have previously generated. We created a pipeline to do this, taking inspiration from Recursive Synthesis for Long-Horizon Terminal Tasks. We create new tasks using these steps:
- Identify the root theorems of the project as before.
- Synthesize new theorems that depend on the previous roots.
- Compile and check whether the new roots are correct.
- Rinse and repeat.
The Factory
How can we reliably automate the creation of these tasks at scale? Agents commonly make mistakes when one-shotting task creation. We need to ensure that our tasks are high quality and cannot be reward hacked.
Here is a simplified explanation of our task creation pipeline. We divided it into four phases. At the end of each phase, we run LLM and deterministic checks, and retry if they fail. In our experience, this noticeably improves task quality and consistency.
- Sourcing. An agent searches for open-source Lean projects to use as seeds.
    
  - Checks:
        
    - The project has a permissive license.
    - It compiles.
    - It is large and complex enough to produce hard tasks.
- Task creation. Run seed creation and task synthesis as described above.
    
  - Checks:
        
    - Submitting the original proofs as a solution must pass (an oracle run).
    - The task fails a blank solution (a no-op run).
- Solve rollouts. A model attempts to solve each task, and an agent analyzes the trajectories (chat logs and tool calls from the run).
    
  - Checks:
        
    - The task must be difficult.
    - Failures are from difficulty and not because of issues with the task.
- Adversarial and reward-hacking rollouts. A model is given knowledge about its environment and the verifier and purposefully tries to reward hack the task.
    
  - Checks:
        
    - Every hack attempt must fail Comparator.
    - Hacks that succeed trigger a fix to the task, and the adversarial rollout is re-run.
The pipeline has been fully open-sourced here.
For a more detailed walkthrough on task generation, see Automating RL environment creation.
Results
TheoremSmith generated hundreds of tasks with 30+ minute horizons for frontier models. Tasks consistently passed our internal QA.
Limitations
- There’s no direct evidence showing that TheoremSmith’s synthetically generated tasks lead to real-world increases in models’ proof abilities. Synthetically generated tasks may not follow the same patterns as real projects, and training on these may not help models solve real math problems.
- The source projects here skew towards math. We’d also like models to get better at verifying code.
- The seed projects are public, so models may have seen the original proofs during pretraining.
- The LLM-based checks in the pipeline are imperfect. They might let through tasks which are impossible or reward hackable.
Future Work
Some directions we’d like to explore:
- Train models on TheoremSmith tasks and measure whether improvements transfer to real-world formal-verification tasks.
- To improve models’ software verification skills, TheoremSmith should be adapted to other verification tools like Isabelle, Dafny, and Verus.
- OpenAI’s proposed solution to the Navier–Stokes problem used swarms of thousands of agents working concurrently. How can we adapt TheoremSmith to assist in training these kinds of scenarios? Can we create training environments that use multi-agent swarms and elicit new advances in agent collaboration? Multi-agent RL environments are not yet widely used. Formal verification may be a good place to experiment with them because credit assignment is simple. Each lemma an agent proves can be checked independently and assigned credit.
- Codebases are often refactored or updated after being formally verified. This requires refactoring the proofs as well, which is difficult and time-consuming. We think this problem will only become more common as proving codebase correctness becomes more mainstream. Pipelines similar to TheoremSmith could be used to create training data to train and evaluate proof refactoring.
