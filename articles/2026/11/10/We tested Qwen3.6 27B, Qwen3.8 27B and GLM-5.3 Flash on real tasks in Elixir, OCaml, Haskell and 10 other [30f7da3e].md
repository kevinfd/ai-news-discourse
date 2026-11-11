---
id: "30f7da3e1e7537ab"
title: "We tested Qwen3.6 27B, Qwen3.8 27B and GLM-5.3 Flash on real tasks in Elixir, OCaml, Haskell and 10 other less common languages"
url: "https://longtail-swe.com"
link: "https://longtail-swe.com"
source: "longtail-swe.com"
domain: "longtail-swe.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T14:48:25Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Fabulous_Pollution10"]
language: "en"
summary: "Hi! My team and I built a benchmark of 202 real GitHub tasks in 13 languages that rarely show up in coding benchmarks: Elixir, OCaml, Haskell, Clojure, Kotlin, Swift, Julia, R and others. I think a lot of people do local development in these languages too. We didn’t have a huge compute budget, so I specifically added Qwen3.6 27B and Qwen3.8 27B to compare them. Qwen3.8 solves 43% of the tasks,…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "DeepSeek"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 650
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsorsx/we_tested_qwen36_27b_qwen38_27b_and_glm53_flash/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# We tested Qwen3.6 27B, Qwen3.8 27B and GLM-5.3 Flash on real tasks in Elixir, OCaml, Haskell and 10 other less common languages

longtail-swe.com · Fabulous_Pollution10 · 2026-11-10

LongTail-SWE
Can coding agents fix real issues in languages missing from standard benchmarks?
Vladimir Dobrovolskii · Ibragim Badertdinov · Alexander Golubev
Nebius
About the benchmark
LongTail-SWE evaluates coding agents on 202 real-world software engineering tasks across 13 underrepresented programming languages. Each task comes from a GitHub issue and a corresponding pull request, with an executable environment and tests. We review and repair task descriptions and tests to make evaluation more reliable.
Leaderboard
Nine model configurations, all in the same SWE-agent-like scaffold, three attempts per task. Pass@1 is the mean over all attempts, ± run-level SEM. Pass@3 counts tasks solved at least once. All-3 counts tasks solved every time. Tokens and steps are means per attempt. Qwen 3.8 27B was also used for difficulty selection.
By language
Pass@1 (%) by language, averaged over three attempts per task. N is the number of tasks.
How tasks are built
Merged pull requests linked to a single issue, from 13 languages. 2,640 are clear or repairable and pass screening.
An agent installs the project, runs and audits the tests. Each task gets its own Docker image.
A solver attempts the task. Three judges review it. A repairer fixes the tests and the description.
Tasks solved by Qwen 3.8 27B in all three runs are generally dropped. After validation, 35 tasks are excluded.
FAQ
How do I evaluate my model?
Each task ships as a Docker image with dependencies installed, and the tasks are also available in Harbor format. Run your agent on each task, then score the patch with the evaluator from the repository. An attempt counts as solved only if all fail-to-pass and pass-to-pass tests pass. We report three attempts per task; the agent prompts are in the repository.
How do you know the judges are right?
Two engineers independently reviewed 65 tasks from different pipeline stages and agreed on a label for each: 51 had defects and 14 did not. The three-judge protocol identified 49 of the 51 defective tasks (96.1% recall, 87.5% precision). It also flagged 7 of the 14 acceptable tasks for repair.
What does repair change?
Tests and an appended addendum to the description. The reference patch and initially audited issue text stay fixed during repair. The initial audit may redact implementation hints. Repair removes checks that reject valid alternative solutions and adds checks for requirements the tests missed. On 63 tasks whose description did not change, the same Opus 5.5 patches score 29.1% Pass@1 on the original tests and 67.2% on the repaired ones.
What about contamination?
Repositories in the collection were required to have been updated on or after January 1, 2026. This does not mean that every issue or pull request was created after that date. Tasks come from public issues and pull requests, so overlap with training data cannot be ruled out, and model training cutoffs are often undisclosed.
Are there plans to release data like this for training?
LongTail-SWE is an evaluation benchmark, with an easier companion set of 296 tasks. We are working on a larger release for training. In the meantime, see the SWE-rebench V2.1 RL tasks on Harbor and the SWE-rebench V2 dataset for training and evaluation. The repository provides task data, prompts and scripts for building environments and scoring patches.
Why these 13 languages?
Each language has an active open-source ecosystem with little or no coverage in current issue-resolution benchmarks. Together, they cover functional, JVM, BEAM, scientific and mobile stacks.
How does it relate to SWE-rebench?
LongTail-SWE builds on the SWE-rebench V2 pipeline. It adds screening for repairable candidates, an install-and-audit agent and the solver, judge and repairer loop.
Citation
@misc{dobrovolskii2026longtailswe,
  title         = {Longtail-SWE: High-Quality SWE Tasks for
                   Underrepresented Languages},
  author        = {Dobrovolskii, Vladimir and Badertdinov, Ibragim
                   and Golubev, Alexander},
  year          = {2026},
  eprint        = {2611.10304},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SE},
  url           = {https://arxiv.org/abs/2611.10304}
}
      From the team behind SWE-rebench, Nebius · Code MIT · Data CC BY 4.0
