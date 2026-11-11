---
id: "97c5f109dd6ca8ff"
title: "LLMs Play Zachtronics' TIS-100"
url: "https://tis-100.wincon.dev"
link: "https://tis-100.wincon.dev"
source: "Wincon"
domain: "tis-100.wincon.dev"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T00:37:05Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["fairestvalue"]
language: "en"
summary: "TIS-100 Bench: LLMs Push the Pareto Frontier in Programming Puzzle Games\nTwelve nodes. Two registers per node. Fifteen lines of code. In TIS-100, even multiplying two numbers is a small engineering project, and players have spent a decade optimizing these programs on a public community leaderboard. We gave 16 LLMs the game and its manual, withheld the leaderboard, and told them to keep…"
tags: []
orgs: ["OpenAI", "Google"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 2236
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50448340"
score: 80
comments: 18
community: "Hacker News"
---

# LLMs Play Zachtronics' TIS-100

Wincon · fairestvalue · 2026-11-11

TIS-100 Bench: LLMs Push the Pareto Frontier in Programming Puzzle Games
Twelve nodes. Two registers per node. Fifteen lines of code. In TIS-100, even multiplying two numbers is a small engineering project, and players have spent a decade optimizing these programs on a public community leaderboard. We gave 16 LLMs the game and its manual, withheld the leaderboard, and told them to keep improving.
Within days, players picked up the models’ programs and improved on most of them.
Each node is a tiny processor, and neighboring nodes have to wait for one another to exchange values. The game scores a working solution on cycles, nodes, and instructions, and you start wondering whether one more instruction could disappear. Lower is better, but improving one score can make another worse, so each puzzle has a frontier of tradeoffs instead of one best answer.
Leaderboard
We ran 16 LLMs, covering leading frontier and open-weight models. Every model attempted all 47 puzzles in the game, plus eight community tournament puzzles, in one scored attempt each (pass@1), with 10 to 45 minutes per puzzle, depending on difficulty, to find a working program and keep improving it.
Opus 5.5 and GPT-6 Astra lead, and the data doesn’t separate them. Both solved all 55 puzzles and both found new frontier points on 11. Opus 5.5 found more points, 72 to 32, while GPT-6 Astra has the higher record proximity, 78.0 to 77.2. Record proximity measures closeness to the community records, where 100 means matching them. The proximity gap’s 95% bootstrap interval includes zero, from −0.7 to +2.4 points. GPT-6 Astra also leads in all six tested hypervolume settings, which measure the space covered by each model’s tradeoffs.
Solving and optimizing are also different skills. Gemini 3.8 Flash solved 53 puzzles and found new points on 1; Fable 5.1 solved fewer, 52, and found new points on 5.
RL environments & traces are available upon request for research teams. Get in touch ↗
How it works: harness design
Every result here is a program we can run and test on fresh inputs, which makes a programming game a useful benchmark. Models get what a player can inspect, through text tools instead of a mouse and screenshots: the manual, visible test inputs, registers, and game feedback. They don’t get community code or exact records, only the game’s coarse score histograms.
- Read, edit, run
- Models read the puzzle and language reference, edit programs, and run them in the real game.
- Diagnostics
- Wrong outputs and deadlocks return mismatches, registers, and blocked ports, so the next edit can respond to evidence.
- Saved progress
- Every passing program joins the model’s own frontier and can be recovered with get_best, so a risky edit can’t lose an earlier result.
- Reminders
- If a model ends its turn early, a reminder asks it to keep testing, so quitting early doesn’t decide the score. Reminders contain no solution hints.
- A visible clock
- Models see time used against a 10-, 30-, or 45-minute limit. Setup doesn’t count; thinking and game calls do. Models can’t end an episode early.
- Run limits
- Game execution stops after roughly 1 second without state changes, 5 seconds without output, or 60 seconds overall, and returns diagnostics.
Why test 100,000 inputs? The game checks a small set of cases per run. Our headline count requires a fresh-game replay and 100,000 passing tests on the independent TIS-100-CXX simulator, providing stronger evidence that a program generalizes to new inputs.
One record up close
Undecimal Twin RounderSPEC44149538, one of the eight tournament puzzles, rounds an input to the nearest multiple of N on one output and of 11−N on the other. When we froze the leaderboard, the best community program took 2,694 cycles. Opus 5.5 passed its first program after 6.5 minutes, at 5,669 cycles. It went under the record 16 minutes in and finished at 1,918, which is 29% faster. That speed cost one more node and 28 more instructions than the old record.
The core of the program is a two-speed search. Instead of subtracting N one step at a time, nodes 5 and 6 subtract 4N until they overshoot, then add N back until the value turns positive. Each drives a small coprocessor, node 2 or node 7, by sending it jump offsets through a port, so the coprocessor works as a lookup table for 4N and N.
Loading puzzle trajectories…
Five models got under the old record in-game. The other two cycle records are GPT-6.1 Sol’s 3,460 on Intersection IdentifierSPEC64160260, against 3,872 (11% faster), and Gemini 4 Argon’s 188 on Error: 8SPEC79324720, against 198 (5% faster). All three are on tournament puzzles, none in the main game. Of the 133 new frontier points, 18 beat a community record outright. The other 115 are new tradeoffs: better balances between the three scores than any community solution.
What separates the models
Cost doesn’t track quality
GPT-6.1 Sol reaches 75.6 record proximity at an estimated $0.75 per puzzle. Opus 5.5 reaches 77.2 at $5.08, 7 times the cost for 2 more points. Fable 5.1 is the most expensive at $7.19 and scores 70.2.
Activity doesn’t explain quality either. GPT-6.1 Sol averages 136 game calls per puzzle at 75.6 record proximity; Gemini 4 Argon averages 41 at 76.2.
New points concentrate on hard puzzles
New frontier points appear on 14 hard puzzles, 4 medium puzzles, and no easy ones. Long-running puzzles are harder to solve but easier to improve: on puzzles with a cycle record of 200 or less, 88% of episodes pass and 4% find a new point. Above 500 cycles, 76% pass and 8% find one.
Speed is the hardest score
Every model is closest to the community on nodes and furthest on cycles. Across all 13, mean proximity is 72 for nodes, 56 for instructions, and 45 for cycles.
What the models built
We grouped all 55 puzzles by their main demand, then read the programs. Fifteen of the sixteen models solved all five routing puzzles, and none found a new frontier point there. The examples below show how different designs spend the same resources.
Multiplication: spend code to save cycles
Signal Multiplier43786 has no MUL. Gemini 4 Argon and GPT-6 Astra use JRO, a relative jump, to enter a block of repeated instructions at the right position. The jump selects how many copies of a value to send and add, saving the counter updates and branches of a multiplication loop.
Gemini 4 Argon’s fastest program uses two paths to multiply in parallel and a final node to interleave their outputs. It takes 436 cycles against GPT-6 Astra’s 523, about 17% faster, at a cost of two more nodes and 33 more instructions.
Window sums: distribute the history
Signal Window Filter60099 outputs the sums of the last three and last five inputs, so a solution has to remember history as well as add. Gemini 4 Argon’s four-node program uses SWP to rotate stored values and ADD/SUB to update running state. GPT-6.1 Sol spreads that delay and aggregation across seven nodes, passing intermediate values between them.
GPT-6.1 Sol’s program runs in 318 cycles with 26 instructions; Gemini 4 Argon’s takes 428 cycles with only 17. The difference is how much of the work runs in parallel, and how much communication and code that costs.
Indexed access from stacks
T31 Node EmulatorNEXUS.23.727.9 needs eight addressable storage slots, but the available memory nodes are stacks. These programs move values between stacks to reach the requested slot, then read or replace it. MiMo-V2.6-Pro uses counted transfer loops; Opus 5.5 uses JRO to pick among unrolled transfers, spending extra instructions to save cycles.
Memory isn’t one skill: MiMo-V2.6-Pro solves this emulator but fails Sequence Mode CalculatorNEXUS.09.904.9 and Signal Window Filter60099.
Each row is that model’s fastest saved program for the puzzle, picked for illustration. Not all are new frontier points.
God mode: what if the model could see the target?
The main benchmark hides the community’s scores. In a separate study on six puzzles, five models got:
- The target: exact community scores, showing which tradeoffs remain unbeaten.
- Diagnostics: cycle-by-cycle traces and profiles of where each node stalls.
- Edge cases: a fast simulator that runs 10,000 random tests and returns failures.
- More time: 30 minutes, plus extensions for progress, up to 60.
Every model improved: GPT-6 Astra from 82.8 to 91.8, GPT-6.1 Sol from 82.9 to 90.6, Opus 5.5 from 81.4 to 89.1, Grok 4.7 from 67.5 to 75.1, and Gemini 4 Argon from 83.5 to 87.9 in mean record proximity. Scores rose in 28 of the 30 model–puzzle pairs.
The diagnostics changed what models did next. On Signal Multiplexer22280, GPT-6.1 Sol’s first passing program took 294 cycles. Its profile showed node 2 working 86% of the time while nodes 1 and 3 spent 84% blocked waiting to write to it. GPT-6.1 Sol moved the branching out of node 2 and into those two neighbors. The next run took 204 cycles, 31% faster, at a cost of two more nodes and five more instructions.
Information, tools, and time all changed together, so this study can’t say which addition helped most. These runs are outside the main leaderboard and the headline count.
Puzzles: Signal Multiplexer, Sequence Generator, Signal Edge Detector, Interrupt Handler, Sequence Peak Detector, and Signal Error Corrector.
Co-discovery
We submitted selected programs to the leaderboard, and the community improved on them almost immediately. On Undecimal Twin RounderSPEC44149538, @LongingForRest took Opus 5.5’s 1,918-cycle program and cut it to 1,744 by the next day. The record is now credited to both: LongingForRest/opus-5-5.
Neither got there alone. The models found new tradeoffs quickly, and players read those programs, worked out why they worked, and took them further.
Mathematics is seeing the same shift. Terence Tao and colleagues used LLM-guided search across 67 problems and improved on the best known results in several. In “After Math,” Silvia De Toffoli and Eamon Duede argue that a result only becomes a solution once mathematicians can understand it, and that AI fits better as an assistant than a competitor. TIS-100 is a small, measurable version of that future: a model finds a better program, and people turn it into something they understand.
Pareto explorer
Choose a puzzle and model, then select a point to see its scores and the program that produced it. Every puzzle also has its own page with records and the best programs: all 55 puzzles.
The plot shows cycles and instructions; node counts can differ. New frontier points are judged on all three scores.
Download all 3,714 model Pareto points (CSV) · all 3,714 programs (ZIP), also on GitHub and Hugging Face. 186 rows are marked as new frontier points, which pool to 133 across models.
Methods
Expand
Suite. All 22 campaign puzzles, all 25 TIS-NET puzzles, and eight tournament puzzles from 2018: 19 easy (10 minutes), 17 medium (30), and 19 hard (45). Every model has one scored episode per puzzle. Time limits differ by difficulty, so difficulty and search time can’t be separated.
Scoring. Each model–puzzle pair contributes one selected attempt, with no best-of-attempts scoring, so solve rates are pass@1: a puzzle counts as solved when that one episode saved a program that replays in a fresh game. Unsolved puzzles stay in every average and score zero.
New frontier points. The reference is the community leaderboard as of October 15, 2026. Ties don’t count. Models found 154 candidate points on 23 puzzles. Our count pools and deduplicates them across models and keeps the 133 on 18 puzzles with fresh-game replay and 100,000 passing tests. Testing is strong evidence of correctness, not proof.
Record proximity. The community record divided by the model’s best score, averaged across the three scores and all puzzles, ×100. Each score can come from a different program.
Limits. One episode per pair compares the configurations as tested and doesn’t measure repeated-run variability. Spread between puzzles is variation across tasks. Public puzzles may overlap with training data. Mechanic groups are our own labels.
Programs. Every model Pareto point’s program is public under the MIT License, in TIS-100 save format and named like the community leaderboard’s files (<puzzle>.<cycles>-<nodes>-<instructions>.txt). They are mirrored as one file per program on GitHub and as a table on Hugging Face. Two points replay in the game but fail some random tests; they are included and never count as new frontier points.
Resources. Costs are estimated from recorded October 2026 API list prices, including cache discounts. Tokens accumulate across responses, so repeated input counts again, and tokenizers differ. Game calls count individual dispatched tools, including errors, and exclude the automatic final submission.
Cite
@misc{wincon2026tis100bench,
  title  = {TIS-100 Bench: LLMs Push the Pareto Frontier in Programming Puzzle Games},
  author = {{Wincon}},
  year   = {2026},
  month  = nov,
  url    = {https://tis-100.wincon.dev/},
  note   = {Benchmark snapshot 2026-11-03-v5}
}
Credits
Thanks to Zachtronics, the TIS-100 players, and the maintainers of the community leaderboard, TIS-100-CXX, and leaderboard bot. Their solutions and tools make this comparison possible. Thanks also to @12345ieee, @LongingForRest, @Hersmunch, @easone, @18111398, and everyone on the Zachtronics Discord who discussed the submissions and kept improving them.
TIS-100, SpaceChem, and Opus Magnum are trademarks of Zachtronics. Model names and logos are trademarks of their respective owners and appear only to identify the models tested. Wincon Research is not affiliated with or endorsed by Zachtronics or any model provider.
Have a question or want to share feedback? Get in touch ↗
