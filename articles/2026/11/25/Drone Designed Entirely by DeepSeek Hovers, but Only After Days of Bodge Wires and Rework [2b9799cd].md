---
id: "2b9799cd735fb916"
title: "Drone Designed Entirely by DeepSeek Hovers, but Only After Days of Bodge Wires and Rework"
url: "https://circuitdigest.com/news/drone-designed-entirely-by-deepseek-hovers-but-only-after-days-of-bodge-wires-and-rework"
link: "https://circuitdigest.com/news/drone-designed-entirely-by-deepseek-hovers-but-only-after-days-of-bodge-wires-and-rework"
source: "Circuit Digest"
domain: "circuitdigest.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-25T16:00:00Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["Aswinth Raj"]
language: "en"
summary: "Social feeds are full of clips claiming an AI designed a complex circuit board in ten minutes. The two engineers behind nktbuilds decided to test that claim the hard way in their video Can DeepSeek ..."
tags: []
orgs: ["DeepSeek"]
topics: ["robotics & autonomy", "models & research", "search & media"]
content_source: "fulltext"
word_count: 520
paywalled: false
image: "http://www.bing.com/th?id=ONUT.MyHSop1UXItlwA-JftORlg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Drone Designed Entirely by DeepSeek Hovers, but Only After Days of Bodge Wires and Rework

Circuit Digest · Aswinth Raj · 2026-11-25

Social feeds are full of clips claiming an AI designed a complex circuit board in ten minutes. The two engineers behind nktbuilds decided to test that claim the hard way in their video Can DeepSeek One-Shot a Working Drone?. They gave an open-source model one prompt, let it pick parts, draw footprints, lay out the PCB and write the flight firmware, then sent the files straight to the factory with no human review at all.
One prompt and one hard rule
To stop the model from simply copying one of the many open ESP32 drones, they forced it onto a chip with no reference drone to copy: a Raytac module built on Nordic's nRF54L15, which has Bluetooth LE but no Wi-Fi. The prompt asked for an all-in-one mini drone where the PCB is the frame, coreless brushed motors driven by PWM through MOSFETs, an addressable RGB LED and no charging circuit, as small as possible. The only intervention during the run was forcing all parts onto one side of the board to keep assembly cheap. The schematic came back as overlapping labels and spaghetti wires, and the layout was full of right-angle traces.
What went wrong on the bench
The good news was that the boards had no shorts and the power rails were correct. Then the debugger refused to see the MCU. The model had mirrored the module footprint, reversing every pin, the classic mistake of reading a bottom-view drawing as a top view. Daniel spent about four hours cutting traces and hand-wiring the signals back. Next, the IMU would not answer, because the nRF54L15 only allows its fast SPI on dedicated pins and the model had wired all six SPI lines to the wrong GPIO bank. Even after rerouting them, SPI still failed, so the team switched the IMU to I2C and tacked on the pull-up resistors the design had left out. Motors and propellers needed glue to stay on. At the nominal 3.7 V it could not lift itself. It finally hovered when fed about 5 V from a bench supply, and at 6.5 V it flipped over, partly because the IMU sits off the centre of gravity.
Our take: this is the most useful kind of AI hardware test, because it shows how errors compound. A model that gets 95 percent of symbols, footprints and routing right still leaves a board that needs days of rework. The team also ran the same prompt through two frontier models: one tool produced cleaner routing but hallucinated pins on the MCU footprint, and the other looked correct on screen but has not been built yet. For a drone where humans did the design, see the ESP-Fly, one of the smallest ESP32 drones.
Image credit: nktbuilds, frame from the YouTube video, cropped and resized.
About the author: Aswinth Raj is an electronics engineer and the editor of CircuitDigest, where he has published more than 150 hands-on projects and tutorials across Arduino, PIC, ESP32, Raspberry Pi and EV battery systems. He selects the stories on this page for what engineers and makers can actually learn or build from. Connect on LinkedIn
