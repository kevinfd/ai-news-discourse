---
id: "6fc8c039af460fdf"
title: "Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model"
url: "https://energy-based-reasoners.github.io"
link: "https://energy-based-reasoners.github.io"
source: "Lobsters"
domain: "energy-based-reasoners.github.io"
source_type: "community"
collector: "rss"
date: "2026-11-18T14:45:20Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["energy-based-reasoners.github.io via xyproto"]
language: "en"
summary: "Comments"
tags: ["ai"]
orgs: []
topics: ["chips & infrastructure", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 469
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50543989"
score: 312
comments: 55
community: "Hacker News"
---

# Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model

Lobsters · energy-based-reasoners.github.io via xyproto · 2026-11-18

1Duke University2UIUC3Harvard University
    
TL;DR – We introduce Energy-Based Reasoners (EBRs), reasoning models that learn an energy function over latent reasoning states and formulate looped updates as gradient descent on this energy. Its value scores candidate predictions without requiring an external verifier, while its gradient guides refinement and provides a natural signal for stopping. With only 1.8M parameters, EBRs achieve 99.9% accuracy on Sudoku-Extreme while using 345× less inference compute than the next-best model. On N-Queens and Graph Coloring, EBRs achieve state-of-the-art coverage while maintaining near-100% single-sample accuracy.
Looping is a powerful inductive bias for reasoning. By repeatedly iterating a recurrent block, looped models can scale their effective depth and enable multi-step reasoning in latent space. However, existing looped models are not inherently guided by an explicit measure of progress, making it difficult to determine when to stop looping and how to improve upon the current state. To enable this, we introduce Energy-Based Reasoners (EBRs), which learn an energy function over latent reasoning states and formulate looped updates as gradient descent on this energy. The energy scores latent states, while its gradient guides refinement and provides a signal for stopping. To train EBRs effectively, we further introduce exploration-based training to discover additional modes and to better shape the energy landscape over a broader set of states. Across four algorithmic reasoning benchmarks, EBRs match or outperform prior recurrent reasoning models, achieving 99.9% accuracy on Sudoku-Extreme while using 345× less inference compute than the next-best model and maintaining comparable training compute. On all multi-solution benchmarks, EBRs achieve state-of-the-art coverage of distinct valid solutions while maintaining near-100% single-sample accuracy. These results suggest that energy-based models are a promising approach for strong reasoning performance.
Existing looped reasoners update their latent state without any explicit assessment of it. An EBR learns an energy function that guides refinement, stopping and selection.
Score. The energy rates the compatibility between the reasoning state and the initial board . Lower means better compatibility.
Refine. The gradient turns the score into an improvement direction.
Stop. The state becomes stationary once the gradient is small, so the gradient acts as a stopping criterion.
Select. Among multiple candidate solutions, we pick the one with the lowest energy.
Running more descent steps refines each answer further, and running more trajectories gives the energy more candidates to choose the lowest-energy one from.
Each trajectory stops once its energy gradient falls below a threshold, so easy puzzles finish in a few steps and hard ones keep going.
EBR acts like stochastic gradient descent and can capture many different solutions. Coverage captures the share of each input's distinct valid solutions that 20 samples find.
@article{chen2026energy,
  title={Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model},
  author={Chen, William Xingxu and Gladstone, Alexi and Li, Zeyu Michael and Ji, Heng and Du, Yilun},
  journal={arXiv preprint arXiv:2611.08977},
  year={2026}
}
