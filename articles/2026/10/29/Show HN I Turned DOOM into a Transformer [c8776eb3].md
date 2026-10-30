---
id: "c8776eb352e97b7b"
title: "Show HN: I Turned DOOM into a Transformer"
url: "https://github.com/mottopanikeiku/doomformer"
link: "https://github.com/mottopanikeiku/doomformer"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-29T23:25:46Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["falperc"]
language: "en"
summary: "Instead of trying to run DOOM on things, I have instead decided to use DOOM (many, many, many doom games actually) to create a transformer. For a lot of the math required I essentially had to use DOOM game mechanics and voodoo dolls (DOOM is turing complete btw) and exchange them with the actual operations, essentially creating an alternative to NumPy (a 65000x slower one). Thus, I am proud to…"
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 1262
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50297697"
score: 99
comments: 31
community: "Hacker News"
---

# Show HN: I Turned DOOM into a Transformer

GitHub · falperc · 2026-10-29

Neural networks computed by voodoo dolls inside DOOM maps.
Every value is read back and checked against NumPy. Tolerance 0.
Quick start · Walk a digit · The museum · How it works · What is checked · Films · Docs
pip install git+https://github.com/mottopanikeiku/doomformer   # Python 3.11+, Linux or macOS
doomformer hello             # 2 s: a small MLP, every value checked
doomformer draw --digit 7    # 15 s: the marine walks a 7 and the level reads it
doomformer doctor checks your setup. It builds ACC, the ACS compiler, if it is missing. That needs git, cmake and a
C compiler. On Fedora: sudo dnf install git cmake gcc gcc-c++ make.
Tip
No install needed for the Colab notebook. Draw a digit in your browser and DOOM reads it.
The marine holds FIRE and inks the floor. Then he presses READ.
1,355 voodoo dolls in the same map run an MNIST network. The winning digit's doll crosses a line. That line lights the digit on the display.
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
       ▄████████████████
       ████▀▀     ▀████▀
       ▀▀▀        ▄███▀
                  ████
                  ███
                  ███
                  ███
                 ████
                 ███▀
                 ████
                 ▀███
DOOM reads: 7  (right)   -- the winner's doll lit it on the 7-segment display
EXACT: all 248 values DOOM computed [...] equal the NumPy integer reference (tolerance 0)
READ pass: 273 game tics = 8 s of real-time DOOM at 35 tics/s, 3 s wall [...]
Python reads back 248 values and checks every one. With --digit, Python presses the keys for you. Without it, you
walk and draw yourself. Full output
Note
EXACT means DOOM got the same numbers as the integer network. It does not mean the digit is right.
The float model scores 97.58 %. The network also trained on the strokes the scripted marine walks. Details · Film
Tip
Play it without Python. Download museum.wad
(sha256) and the free
Freedoom IWAD. Then run gzdoom -iwad freedoom2.wad -file museum.wad.
Step on seven floor pads to light a digit. Press READ. 136 voodoo dolls run a tiny network and light the answer.
Press MUTATE and the level rewires one connection while it runs. The same 7 now reads as 1. You can watch it happen: one doll stops at its gate.
$ doomformer museum verify
7                        pads abc     w_7a +1  DOOM reads 7  scores [4, 6, 3, 5, 4, 3, 2, 7, 3, 4]  EXACT (148 values; 744 tics; [...])
7 after MUTATE           pads abc     w_7a -1  DOOM reads 1  scores [4, 6, 3, 5, 4, 3, 2, 5, 3, 4]  EXACT (148 values; 744 tics; [...])
7 after RESTORE          pads abc     w_7a +1  DOOM reads 7  scores [4, 6, 3, 5, 4, 3, 2, 7, 3, 4]  EXACT (148 values; 744 tics; [...])
A self-test version runs exactly in GZDoom, LZDoom, UZDoom and ZDoom 2.8.1. Details
Every part of a network becomes a part of the map:
One layer, from dolls to dolls:
flowchart LR
    A["input value<br/>= a crowd of dolls"] --> B["weight lines<br/>each crossing adds w"]
    B --> C["the sum<br/>= a light level or height"]
    C --> D["staircase of gates<br/>= the activation"]
    D --> E["next layer's dolls"]
    The engine has sharp edges, and the compiler works around them:
- A floor mover ignores a second request while it is still moving.
- A teleport cancels lines a doll crossed earlier in the same tic.
- Things far from a BSP node can land in the wrong room, so every map fits in 32,000 units.
doomformer facts checks these in about 10 s. Engine facts ·
Engine features it needs ·
Other ports
Computers in DOOM maps are not new. counter.wad counts with voodoo dolls, conway.wad runs Game of Life, and Danny Spencer's calculator adds numbers. New here: a compiler for neural networks, and an exact check on every value. Related work
Every run compares each value the map exposes with NumPy. That proves the inputs that ran, nothing more. So the repo also attacks its own check:
The MNIST map exposes 248 values. It does not expose its 903 staircase counts and 1,351 gate comparisons. Those are checked only through the sums they feed. Fuzzing and tests found four bugs in the compiler. All are fixed. Verification
Who computes what
ACS level scripts move gates, rewind the dolls, sense the world and copy results out. Two do more. df.Agent takes an
argmax in ACS. --opt 3 copies each layer's values into the next layer with a script.
Per demo
The maps need ZDoom (UDMF and ACS). This repo runs ViZDoom 1.3.2 with Freedoom assets.
Times are from a 16-core arm64 Linux machine. Every command
Some outputs are picked. DEMON CANYON, the name --nightmare writes, is one hand-picked sample. ask gets 94.7 % of
its training questions right, and 35.4 % of new wordings.
His brain is the level. The level senses the nearest demon. 1,345 voodoo dolls of the marine run his brain and pick an action. The level turns him and fires. Python only steps the clock and reads. 50 of 50 decisions are exact. Film · Code
Warning
He is not playable. One decision takes 22 s of game time, and the demons are frozen while he thinks. With the demons
awake (--live), he dies in 5.5 s without a kill. Live demons
All demos, numbers and picked seeds
Compile a network into a map. Let its outputs open doors, flash lights or shove the marine. This runs as pasted:
import numpy as np
import doomformer as df
# 2 inputs -> [a AND b, a OR b] -> 2 outputs, all integers
net = df.MLP(
    weights=[np.array([[1, 1], [1, 1]]), np.array([[1, 0], [0, 1]])],
    biases=[np.array([-1, 0]), np.array([0, 0])],
    thresholds=[np.array([1]), np.array([1])],
    signed_input=False,
)
with df.compile(net) as brain:
    for x in ([0, 0], [1, 0], [1, 1]):
        # computed by voodoo dolls; raises df.MismatchError on any difference from net.reference
        print(x, "->", brain(np.array(x)).tolist())
    brain.record([np.array([0, 1]), np.array([1, 1])], "dolls.gif")   # film the dolls doing it
df.MLP.from_torch converts a PyTorch model (example 02). The world and actions
hooks wire outputs to doors, lights and thrusts (example 03).
Guide · 12 examples · Show and tell
One map runs in one game, on one core. df.run_many spreads inputs over many games, or over a Ray cluster. A network
can also be split into tile maps, one per layer. Then Python copies values between them.
doomformer mnist --tiles --all --workers 6         # all 10,000 digits as tile maps, about 23 min
pip install "doomformer[ray]"
ray start --head                  # other machines: ray start --address=HEAD:6379
doomformer mnist --all --ray --record mnist.json   # all 10,000 digits, one map each, on a cluster
Budget one core and 1.3 GB of RAM per game. Scaling
Important
- Slow. A small MLP runs about 23,000 times slower than NumPy. Most of the time goes to idle conveyor belts. Speed
- Only the runs are checked. Inputs that never ran are not covered. Not covered
- Integer models. Attention is integer attention. No model has LayerNorm.
- ViZDoom first. Other DOOM engines ran only small maps.
- No reinforcement learning. The marine copies a scripted aimbot.
- Finite machines. Memory is bounded. Nothing here claims DOOM is Turing complete.
- Picked samples. Showcased seeds and names are picked. The list
Code and docs: MIT. Data keeps its own licence (THIRD_PARTY.md). The level-name lists come
from the Doom Wiki (CC BY-SA 4.0) and id Software's source (GPL-2.0). The 100 sample MNIST digits are CC BY-SA 3.0. The
fruit-fly circuits in models/fly come from the FlyWire connectome (CC BY-NC 4.0, non-commercial). Freedoom graphics
are BSD-licensed. DOOM is a trademark of id Software / ZeniMax. This project is not affiliated with them.
