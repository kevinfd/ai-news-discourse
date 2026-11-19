---
id: "641eff8edea36ad7"
title: "Show HN: Try Vibe Robotics! (IRL or MuJoCo SIM)"
url: "https://github.com/google-deepmind/robotics-antigravity-plugin"
link: "https://github.com/google-deepmind/robotics-antigravity-plugin"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-18T23:38:40Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["_sshahid_"]
language: "en"
summary: "Hey HN, I'm Salman, a research engineer at GDM Robotics on the team that built this robotics plugin. Whether you're a robotics founder, data company, making RL environments, or just getting FOMO seeing all the cool robotics demos on X, you can just plug in a robot and start prompting away. The plugin we've written up includes skills that steer the model toward following best practices. The…"
tags: []
orgs: ["Google"]
topics: ["robotics & autonomy", "models & research", "policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 643
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50553913"
score: 11
comments: 0
community: "Hacker News"
---

# Show HN: Try Vibe Robotics! (IRL or MuJoCo SIM)

GitHub · _sshahid_ · 2026-11-18

The Robotics plugin brings frontier spatial reasoning, multimodal perception, and code generation directly into the real-time robot loop. Your agent writes the controller, tests it in MuJoCo simulation, and runs the same code on a real robot arm. You can also work in simulation only, with no robot hardware. This makes closed-loop control, rapid hardware bring-up, and continuous robotics applications fast and affordable enough for everyday use.
An I2RT YAM Pro arm sorts cookies from a moving conveyor belt into two boxes.
- "Generate a pelican riding a bicycle simulation in MuJoCo."
- "Create a MuJoCo grocery sorting task using a LeRobot SO-101 arm. Scatter groceries of different shapes and sizes across a countertop, and have the robot sort them into designated bins without crushing fragile items or knocking anything over. Include randomized layouts. Show me some example successful trajectories."
- "Build a realistic coffee shop scene in MuJoCo with bimanual Franka Research 3 robot arms, espresso machine, cups, and serving counter. Program the robot to pick up an empty cup, place it beneath the coffee dispenser, and deliver the finished drink onto a tray. All object movements must be driven by contact from the robot."
- "In simulation, build my setup from these photos: one YAM Pro arm, a moving conveyor belt, two types of cookies, and two boxes. Use the YAM Pro arm to pick each cookie off the moving belt and place it in the matching box. Test it across several runs and show me a video."
- "Bring up my real SO-101 arm and use it to pick up the blue marker from the table. Record a video."
- "Bring up my real YAM arm and use it to wave hi. Record a video."
- "Bring up my real YAM arm and use it to place the pen several inches deep inside the tall box without touching the walls. Record a video."
Using with Google Antigravity
- Download and install the latest version of Google Antigravity from antigravity.google.
- Install the plugin directly from GitHub, or clone it into your local plugins directory: agy plugin install https://github.com/google-deepmind/robotics-antigravity-plugin Or copy the plugin manually and restart Google Antigravity: git clone https://github.com/google-deepmind/robotics-antigravity-plugin.git mkdir -p ~/.gemini/config/plugins cp -r robotics-antigravity-plugin/plugins/* ~/.gemini/config/plugins/
You can also install individual skills via npx:
npx skills add google-deepmind/robotics-antigravity-plugin
If you install the Robotics plugin from the Google Antigravity Marketplace,
the seven MuJoCo API skills (mujoco-python,
mujoco-spec-editing, mujoco-rendering, mujoco-accelerated,
mujoco-parity, mujoco-studio, and mujoco-gui) are already bundled.
If you install from this GitHub repository, install the MuJoCo skills from the canonical MuJoCo repository:
npx skills add google-deepmind/mujoco
The same skills also ship inside the mujoco Python package at
pathlib.Path(mujoco.__file__).parent / 'doc' / 'skills'.
For skills that call Gemini perception models, set GEMINI_API_KEY in your
environment before running.
Built a cool robot or MuJoCo simulation workflow? Post a link to your example repository, demo video, or prompt in GitHub Discussions.
robotics-antigravity-plugin/
├── plugins.json                 # Top-level plugin discovery manifest
└── plugins/
    └── robotics/                # Unified robotics plugin (perception, planning, control, sim2real, MuJoCo Studio, and robot bring-up)
See plugins/robotics/README.md for the plugin overview.
Warning
A moving robot can injure people and damage equipment. Stay next to the robot, keep the workspace clear, and keep a way to cut power within reach. You are responsible for the safe operation of your robot.
- Contributing: See CONTRIBUTING.md for our contribution policy, or open an issue for bug reports and feature requests.
- Security: Eligibility for the Google Open Source Software Vulnerability Rewards Program is determined by the Google Open Source Software Vulnerability Reward Program Rules.
You can find more about Gemini Robotics, including demos, at deepmind.google/models/gemini-robotics.
Copyright 2026 Google LLC. Licensed under the Apache License 2.0. Some skills download third-party software and robot models, or call third-party services such as the Gemini API, at run time. These are licensed by their owners under their own terms.
