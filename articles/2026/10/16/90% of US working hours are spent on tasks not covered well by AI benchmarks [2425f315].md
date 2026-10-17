---
id: "2425f3153984e15e"
title: "90% of US working hours are spent on tasks not covered well by AI benchmarks"
url: "https://mercor.com/research/labor-index/benchmark-map"
link: "https://mercor.com/research/labor-index/benchmark-map"
source: "Mercor"
domain: "mercor.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-16T17:08:38Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["speckx"]
language: "en"
summary: "of the US economy\nAI benchmarks have multiplied in recent years, but coverage of economically valuable work remains limited. To measure this, we compiled relevant benchmarks to measure their coverage of American jobs. This Benchmark Map is our first step toward building a comprehensive, continuously updated resource for understanding AI capabilities across the economy.\n- of 923 occupations…"
tags: []
orgs: []
topics: ["models & research", "jobs & society", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 1747
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50121179"
score: 521
comments: 442
community: "Hacker News"
---

# 90% of US working hours are spent on tasks not covered well by AI benchmarks

Mercor · speckx · 2026-10-16

of the US economy
AI benchmarks have multiplied in recent years, but coverage of economically valuable work remains limited. To measure this, we compiled relevant benchmarks to measure their coverage of American jobs. This Benchmark Map is our first step toward building a comprehensive, continuously updated resource for understanding AI capabilities across the economy.
- of 923 occupations covered
- 208
- of 18,797 tasks covered
- 924
- benchmarks in the index
- 29
Each tile represents one of the 923 O*NET occupations making up the US labor force, grouped into 22 job families. Occupations are shaded according to the share of their tasks which are represented in our initial list of AI benchmarks. A single benchmark prompt can be mapped to multiple O*NET tasks.
click a family to open it
Coverage by
Covered with at least
- Benchmark Index
- No coverage
In our data set: only 208 of 923 occupations have a task with at least 5 benchmark prompts, and 6 of 22 job families have no such occupations.
Our findings suggest that 90% of American working hours are spent on tasks with little or no coverage from existing benchmarks. This makes it very hard to know how good AI models are at the work Americans actually do.
The coverage of existing benchmarks is not random, either. Our map suggests that the AI community is focusing on the largest labor markets first:
For example, benchmarks in our initial list heavily cover AI-exposed lawyers’ tasks, but barely cover any of the O*NET tasks of similarly AI-exposed legal secretaries or court clerks. The long tail of smaller, middle-income knowledge work jobs appears undercovered.
As we build out our coverage of model capabilities across the economy, we hope to both surface and help fill more gaps in our understanding of what models can do.
To break down the economy into sectors, occupations, and tasks, we used the US Department of Labor’s O*NET taxonomy. O*NET divides the US workforce into 923 occupations; for each occupation, O*NET attempts to provide a comprehensive list of “tasks” which make up the occupation, totaling 18,797 tasks across all occupations.
To measure benchmark coverage, we start with a list of 29 benchmarks selected for their quality and economic relevance. (The full list and selection criteria are in the Benchmark Index tab). In selecting benchmarks for this list, we prioritized:
- Public Availability. Included benchmarks have at least 25 publicly available tasks. We also include Mercor’s APEX benchmarks, where we have access to held-out benchmark prompts and are therefore able to map them to O*NET tasks.
- Agentic Tasks. Included benchmarks ask models to perform agentic tasks, rather than answering questions or advising the user on how to complete a task.
- Economic Realism. Benchmark tasks resemble tasks which humans (or agents) are frequently asked to do in real-world enterprises. Economically valuable tasks are prioritized over academically complex ones.
- Economic Diversity. We capped the number of included benchmarks per job family, in significant part to account for the massive overrepresentation of software engineering and research tasks in popular benchmarks.
- Balanced Difficulty. Benchmarks are not yet saturated by frontier models.
Following work by Wang et al., we then ask an LLM judge to tag each benchmark prompt with as many O*NET tasks as it thinks correspond to that prompt. We validate our LLM tagging with human expert tags on Mercor’s APEX benchmarks, a subset of this list of 29. On the Benchmark Map, an O*NET task counts as “covered” if our LLM judge has mapped it to at least 5 prompts from our 29 benchmarks.
To estimate the total share of working hours Americans spend on tasks covered by benchmarks on this list, we combine our coverage estimates with Hatgis-Kessell et al.’s LLM-derived estimates of the working time share of each O*NET task.
A more detailed account of our methodology can be found in the Methodology tab.
Our estimates of total economic coverage, and of patterns in coverage, all come from the initial list of 29 benchmarks we chose. This is not a complete or perfectly representative sample of the broader universe of unsaturated, public, agentic economic benchmarks. Any incomplete list will necessarily bias down estimates of economic coverage, and it is difficult to bound that bias. We want to stress, therefore, that these results are provisional. We will update them as we expand the initial benchmark list.
We also capped the number of included benchmarks in each job family in order to maximize breadth of coverage. We think this makes our estimate of economy-wide benchmark coverage more accurate, at the cost of biasing down our estimates of coverage in the most-benchmarked job families (e.g. software engineering).
By selecting for unsaturated benchmarks, we risk understating benchmark coverage on O*NET tasks which are easier for LLMs to complete. On the other hand, including saturated benchmarks would risk overstating benchmark coverage if saturation is downstream of lower task realism. The latter claim seems likely, given that benchmarks often overstate LLM performance in real-world deployments. We think that the bias from including saturated benchmarks would be greater than the bias from excluding them, but neither option is ideal.
Finally, while we outline our benchmark selection criteria in the Benchmark Index tab, several criteria (like “Economic Realism”) are difficult to formalize and introduce some subjectivity in our choices.
The benchmarks in our index have relatively deep and narrow coverage of the overall economy. They disproportionately focus on the economic tasks most exposed to AI automation (as measured by Eloundou et al.), with O*NET tasks rated as “exposed” about 6x more likely to be represented on benchmarks than tasks rated “unexposed”. This makes sense: benchmarks are designed to measure AI progress, and AI progress is most plausible on the most AI-exposed tasks. This explains why benchmarks are full of tasks in Software Engineering and Financial Analysis while sparse on tasks in Truck Driving and Gas Plant Operation.
But even after controlling for AI-exposure, O*NET tasks from occupations with larger wage bills are significantly overrepresented among benchmark prompts:
After controlling for occupation and AI-exposure score, O*NET “task importance” is another predictor of benchmark coverage. In particular, O*NET tasks come with domain expert estimates of the importance of the task for its occupation on a scale of 1-5. We find that the tasks scored most important are about 6–10x more likely to be represented on benchmarks than those scored least important:
The plots above suggest a reasonable allocation of the relatively limited resources devoted to high-quality, economically relevant benchmarks so far; it’s natural to prioritize making benchmarks which cover the most important and AI-exposed tasks in the occupations with the largest wage bills. But barring a significant increase in the number and diversity of such benchmarks, these patterns will result in significant blind spots in our view of economically valuable model capabilities.
Measuring model capabilities by job occupation is essential – for enterprises deciding which models fit their needs, for policymakers forecasting the economic impact of AI, and for Americans thinking about their careers. Unfortunately, this is a hard problem to solve.
We could just try averaging model performance on all benchmark prompts relevant to a given job. But as our Benchmark Map suggests, benchmarks cover some economic tasks much more intensively than others. A simple average would give too much weight to frequently benchmarked tasks.
O*NET offers a way to potentially reduce this bias. If we average model performance on occupation-relevant benchmark prompts weighted by O*NET classification, so that each O*NET task is equally weighted in our occupation average, we get a step closer to a number that represents real economic performance.
As a first step, we try this approach on Mercor’s APEX benchmarks for four occupations: investment banking, law, accounting, and software engineering. We compare O*NET-weighted scores to simple averages of model performance on tasks related to each occupation. The resulting weighted and unweighted scores are generally quite similar:
In this case, at least, O*NET weighting changes very little. Model performance on APEX prompts is similar across the O*NET tasks included in the weighted scores above, which limits the value of reweighting. However, less than ⅓ of the O*NET tasks relevant to the 4 occupations above have enough APEX coverage to be included in our weighted scores. We are hopeful that applying O*NET weighting to a much larger set of benchmarks will result in high-quality occupation-specific model scores, and are working toward that goal.
However, even if we incorporate tasks from dozens of benchmarks, several obstacles remain:
- 01 How do we navigate low statistical power? The sheer breadth of work done in the US economy means that for any O*NET occupation and task, we have relatively few benchmark items. This means that our estimates are inherently underpowered, and just one or two low-quality items can severely bias our scores.
- 02 How do we account for the varying difficulty and fidelity of tasks? Some benchmark items are highly saturated, whereas others are still unsolved. This is partly a function of time (as older benchmarks were designed for less performant models and simpler environments) and partly a function of quality (some benchmark items are simplistically graded, have minor mistakes, or can be reward hacked). We do not yet have an explicit way of weighting by quality.
- 03 Can evals that primarily measure AI automation generalize to augmentation? In the real world, AI models are still primarily used by humans, rather than automating entire job functions end-to-end. Therefore, measuring the real-world occupation capabilities of a model should ideally include measuring how much the model augments human productivity. We have completed some early work in this direction, but finding a methodology that scales remains elusive.
- 04 Can every O*NET occupation and task be measured with benchmarks? Knowledge-based work is well-suited to measurement through benchmarks because it is largely done on digital machines, like laptops and phones. Dingel and Neiman estimate that only 37% of US jobs could feasibly be done entirely from home, suggesting that ~63% of jobs involve some tasks with a physical-world component which would be hard to incorporate into current benchmarks. For now, this may not be a meaningful oversight – with the rapid development of robotics capabilities, we anticipate a significant need for physical task benchmarks.
We are actively working on these problems; if you are too, please reach out!
We are indebted to Wang et al. for the O*NET tagging methodology, and thank Nathan Lambert for feedback on a draft of this work.
