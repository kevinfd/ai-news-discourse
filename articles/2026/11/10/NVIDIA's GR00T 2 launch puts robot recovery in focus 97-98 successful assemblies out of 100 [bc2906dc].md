---
id: "bc2906dc666e35af"
title: "NVIDIA's GR00T 2 launch puts robot recovery in focus: 97-98 successful assemblies out of 100"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xsfhj5/nvidias_gr00t_2_launch_puts_robot_recovery_in"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xsfhj5/nvidias_gr00t_2_launch_puts_robot_recovery_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T06:12:09Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "NVIDIA introduced GR00T 2 at CoRL on November 9, a robot model that predicts future video and actions together. One result in the release deserves attention beyond the dexterity demos: a reasoning agent helped a robot recover from failed steps during long assembly runs. In NVIDIA's reported experiments, a YAM robot assembled a toy plane, a toy tractor and a Hot Wheels car in 98, 97 and 97 of 100…"
tags: ["r/ArtificialInteligence"]
orgs: ["Nvidia"]
topics: ["robotics & autonomy", "chips & infrastructure", "models & research", "agents & coding"]
content_source: "post"
word_count: 292
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xsfhj5/nvidias_gr00t_2_launch_puts_robot_recovery_in/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# NVIDIA's GR00T 2 launch puts robot recovery in focus: 97-98 successful assemblies out of 100

Reddit · shoumikgoswami · 2026-11-10

NVIDIA introduced GR00T 2 at CoRL on November 9, a robot model that predicts future video and actions together. One result in the release deserves attention beyond the dexterity demos: a reasoning agent helped a robot recover from failed steps during long assembly runs. In NVIDIA's reported experiments, a YAM robot assembled a toy plane, a toy tractor and a Hot Wheels car in 98, 97 and 97 of 100 trials respectively. The same post-trained policy without the agent succeeded in 71-84 of 100 trials, depending on the toy. Each trial began with the parts dumped onto the table in a cluttered layout absent from the post-training data. The recovery mechanism matters. The agent watches camera images and robot state, calls GR00T 2 for manipulation, and uses separate code-based skills when a part drops or progress stalls. It then hands control back. Some recovery skills were developed in simulation and transferred to the robot. This is a result for that combined system, not evidence that the base model alone became nearly infallible. My take: the interesting product direction is a robot that can finish despite an imperfect attempt, rather than one that needs every movement to go right. A dropped part can turn a polished demo into an operator call-out; recovering from it is part of the job, not a cosmetic extra. There is still a big boundary around the claim. These are NVIDIA's experiments on three toy-assembly tasks, not a measured reliability rate for arbitrary factory work. The reported successes also don't tell us the labor cost of building recovery skills or the economics of deployment. I'd want those costs alongside the completion rate before treating this as a business case. Launch: https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/ Detailed results and recovery setup: https://research.nvidia.com/labs/gear/gr00t-2/ ("Agentic Control")
