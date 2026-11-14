---
id: "8905b192b2378237"
title: "This AI finds patterns in visual brain activity and turns them into pictures"
url: "https://livescience.com/technology/artificial-intelligence/this-ai-finds-patterns-in-visual-brain-activity-and-turns-them-into-pictures?amp%3Butm_campaign=dhfacebook&amp%3Butm_content=app.dashsocial.com%2Flive-science%2Flibrary%2Fmedia%2F746552371&amp%3Butm_medium=social"
link: "https://livescience.com/technology/artificial-intelligence/this-ai-finds-patterns-in-visual-brain-activity-and-turns-them-into-pictures?amp%3Butm_campaign=dhfacebook&amp%3Butm_content=app.dashsocial.com%2Flive-science%2Flibrary%2Fmedia%2F746552371&amp%3Butm_medium=social"
source: "Live Science"
domain: "livescience.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T20:29:33Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Fcking_Chuck"]
language: "en"
summary: "\"An artificial intelligence (AI) tool can use brain scans to recreate the images people looked at with eerie accuracy. The system, called Brain-IT, uses data from functional magnetic resonance imaging (fMRI) to measure activity in the visual cortex, the part of the brain that processes visual input. A computer model then predicts both the broad layout of an image and high-level information about…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research", "health & science"]
content_source: "fulltext"
word_count: 1162
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xvissf/this_ai_finds_patterns_in_visual_brain_activity/"
score: null
comments: null
community: "r/artificial"
---

# This AI finds patterns in visual brain activity and turns them into pictures

Live Science · Fcking_Chuck · 2026-11-13

This AI finds patterns in visual brain activity and turns them into pictures
A new AI model, called Brain-IT, can transform brain scans into images and reverse the process, turning images into what they'd look like as brain activity.
An artificial intelligence (AI) tool can use brain scans to recreate the images people looked at with eerie accuracy.
The system, called Brain-IT, uses data from functional magnetic resonance imaging (fMRI) to measure activity in the visual cortex, the part of the brain that processes visual input. A computer model then predicts both the broad layout of an image and high-level information about its content. It then passes those predictions to an AI image generator, researchers explained in a study uploaded to the preprint database arXiv. The research was presented at the ICLR 2026 conference, held April 23-25, and publicized by its authors in September.
Brain-IT builds on an approach called the Universal Brain Encoder. That model begins with an image and then predicts the fMRI response that would be expected in individual "voxels" — small 3D units — in a brain scan.
"The key idea is that every voxel, a tiny cube of brain tissue, gets its own learned vector that captures what it cares about in images," said study first author Roman Beliy, a doctoral candidate in the Department of Computer Science and Applied Mathematics at the Weizmann Institute of Science in Israel.
Some voxels may be tuned to relatively simple elements of an image, such as edges, textures or locations. Others might be responding to higher-level abstract categories, like faces, bodies or scenes.
Peering inside your mind
Traditional image-to-fMRI systems have generally been custom trained for each participant and dataset. The Universal Brain Encoder is more flexible. It learns from data from multiple people and can transfer information across participants, datasets or different MRI systems with varying magnetic-field strengths, according to the study.
A voxel can determine which parts of an image are relevant to it based on its learned profile, essentially saying, "I recognize edges. Which parts of this image are edges?"
Get the world’s most fascinating discoveries delivered straight to your inbox.
The Universal Brain Encoder starts with an image and predicts brain activity; Brain-IT starts with measured brain activity and reconstructs the image the person saw. In other words,it asks "based on this brain activity, what was the subject looking at?". It sorts thousands of tiny brain-scan measurements from the visual cortex into 128 groups based on the kinds of visual information they tend to carry.
The system then lets those groups share clues with one another, allowing it to combine, for example, information about a scene's shape, color and possible objects, to build a more complete picture of the image, Beliy explained.
The decoder produces two types of visual predictions. One captures semantic information — the features associated with what is likely in a scene; for an image of a dog standing in grass, for instance, this would include things like the features of a dog and an outdoor, grassy setting. The other captures structural information, like the broad visual layout or how forms are arranged.
In the above example, this would be aspects like the outline of the dog or where it was positioned in the frame. The structural prediction gives the generator a starting point for the image, rather than beginning from pure noise, while the semantic info guides an image generator that removes the remaining static until the image emerges.
Although the new tool can recreate what people see, it can't reproduce memories or imagined scenes.
"We're not reading people's thoughts," study co-author Michal Irani, a computer scientist at the Weizmann Institute of Science, told Live Science. "The images we do manage to recover from fMRI require people's cooperation and full intended collaboration."
How scientists tested the model
Brain-IT's synthetic images were compared with the images that participants saw. Brain-IT surpassed prior leading methods on standard objective reconstruction metrics and produced more faithful results, the study authors wrote. The system shined when limited fMRI data from a new participant was available, with just one hour of data from a new participant producing results as accurately as earlier approaches that had been trained on 40 hours of recordings.
A high-scoring or realistic-looking output should not be mistaken for a perfect copy of what someone saw, however.
In the final stage of processing, the system uses an off-the-shelf diffusion generator trained on massive numbers of images. Models like this generate plausible images and can smooth textures, sharpen facial features or fill in missing details.
Beliy said this "beautification" can make reconstructions more polished and convincing and introduce details that don't necessarily come from the brain data itself. In other words, the scan constrains the generated picture, but the AI model supplies some of its realism from learned patterns in photographs.
Why this is not memory decoding
While the new system produces impressive results for seen images, it can't be used to reconstruct an imagined or remembered image.
"Brain-IT relies on how the brain processes a seen image," Irani said. "Information flows from the eyes to the primary visual cortex and onward through a series of visual areas that recognize objects and scenes."
In a controlled experiment, researchers also know precisely which image was shown, giving the model a target during training and evaluation. In contrast, memories and imagined images do not offer the same clean reference. They can be vague and shaped by brain networks involved in memory and thought, with only partial and weaker reactivation of visual regions, Irani said. One limitation that would prevent this technology from being widely deployed is that the only way to get reliable results is from fMRI scanning, which is cumbersome and expensive. The team is currently experimenting with using easier-to-collect electroencephalogram (EEG) data, which is obtained via electrodes on the head, but that work is in the very preliminary stages, according to Irani.
The new system could help brain researchers better understand which visual information is represented in different brain regions, how those regions interact and how individuals’ patterns differ. Such tools could eventually reveal differences in visual processing that could help clinicians spot neurological, neurodevelopmental and psychiatric conditions.
"There are numerous useful medical applications which we are currently striving toward," Irani said. "These include using our brain encoder/decoder to detect and analyze brain disorders such as MS, PTSD, autism and psychiatric disorders."
Beliy, R., Zalcher, A., Kogman, J., Wasserman, N., & Irani, M. (2025, October 29). Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer. arXiv.org. https://arxiv.org/abs/2510.25976
Alan is a freelance tech and entertainment journalist who specializes in computers, laptops, and video games. He's previously written for sites like PC Gamer, GamesRadar, and Rolling Stone. If you need advice on tech, or help finding the best tech deals, Alan is your man.
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
