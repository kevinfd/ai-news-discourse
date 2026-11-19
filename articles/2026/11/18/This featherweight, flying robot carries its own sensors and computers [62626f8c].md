---
id: "62626f8cbcfd5bbe"
title: "This featherweight, flying robot carries its own sensors and computers"
url: "https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118"
link: "https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118"
source: "MIT News"
domain: "news.mit.edu"
source_type: "research"
collector: "rss"
date: "2026-11-18T19:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Adam Zewe | MIT News"]
language: "en"
summary: "Over the past decade, MIT researchers have developed aerial microrobots with bumblebee-like speed, agility, and durability, for tasks like precision agriculture or search-and-rescue. But these featherweight microrobots couldn’t carry the electronics needed for navigation, forcing them to remain connected to a motion-capture system in the lab. Now, the researchers have designed a flapping-wing…"
tags: ["Research", "Robotics", "Drones", "Electronics", "Bioinspiration", "Artificial intelligence", "Sensors", "Machine learning", "Research Laboratory of Electronics", "Laboratory for Information and Decision Systems (LIDS)", "Electrical engineering and computer science (EECS)", "Aeronautical and astronautical engineering"]
orgs: []
topics: ["robotics & autonomy", "models & research", "health & science", "search & media"]
content_source: "fulltext"
word_count: 1073
paywalled: false
image: "https://news.mit.edu/sites/default/files/styles/news_article__cover_image__original/public/images/202611/MIT-Onboard-Microbot-A1-press.jpg?itok=-TluzTJd"
discussion_url: null
score: null
comments: null
community: null
---

# This featherweight, flying robot carries its own sensors and computers

MIT News · Adam Zewe | MIT News · 2026-11-18

Over the past decade, MIT researchers have developed aerial microrobots with bumblebee-like speed, agility, and durability, for tasks like precision agriculture or search-and-rescue. But these featherweight microrobots couldn’t carry the electronics needed for navigation, forcing them to remain connected to a motion-capture system in the lab.
Now, the researchers have designed a flapping-wing microrobot with onboard sensors and computation, which can follow a complex trajectory and land precisely on a sunflower outside the lab’s motion capture environment.
While the robot is still connected to an offboard power source, this demonstration highlights the potential of aerial microrobots to be used for precision agriculture in the future.
For instance, flying microrobots could weave through a field of almond trees or blueberry bushes to carefully pollinate delicate blossoms in regions where natural pollinator populations have been decimated by habitat loss. They could also hover near plants without causing damage, monitoring crop health and spotting pests before they become widespread.
To enable onboard sensing and computation, the researchers developed a method to expand the artificial muscles that power the robot’s wings, increasing the net payload so the tiny robot could carry the necessary electronics.
They also designed a sensor suite that can rapidly estimate the robot’s position and orientation without relying on an offboard motion capture system, and a miniature electronics package to securely hold the tiny computational components on the nimble vehicle.
“This is a really important milestone for the research community. This is the first demonstration of an aerial microrobot that is sensory and compute autonomous. There are many situations, like pollination or industrial surveillance, where you can’t use a larger robot. Small-scale robots are uniquely positioned for these types of tasks, and if this thread of technology becomes successful in the future, it could be very promising,” says Kevin Chen, an associate professor in the Department of Electrical Engineering and Computer Science (EECS), head of the Soft and Micro Robotics Laboratory within the Research Laboratory of Electronics (RLE), and co-corresponding author of a paper on the robot.
He is joined on the paper by co-lead authors and MIT graduate students Yi-Hsuan (Nemo) Hsiao, Quang Phuc Kieu, and Zhongtao Guan; co-corresponding authors Jonathan P. How, a Ford Professor of Aeronautics and Astronautics and a principal investigator in the Laboratory for Information and Decision Systems (LIDS) and the Aerospace Controls Laboratory (ACL) at MIT; Elizabeth Farrell Helbling, an assistant professor at Cornell University; and others at MIT. The research appears today in Science Robotics.
Increasing the payload
The MIT researchers previously developed a swift, agile aerial microrobot with four wings, each powered by a set of soft actuators, or artificial muscles, that flap the wings rapidly so the bot can perform detailed maneuvers.
The robot, roughly the same size and shape as a microcassette, weighs less than a paperclip.
To bring this tiny robot closer to real-world applications, the researchers need it to carry the additional weight from electronics for onboard sensing and computation, while still being fast, maneuverable, and robust to collisions.
In this research, they developed a method to scale up the artificial muscles without hampering the robot’s performance. They carefully tuned the radius and length of the soft actuators, increasing their size by 50 percent while boosting the robot’s net lift forces by 46 percent.
“It is very difficult to scale up the actuators without causing the output power of the system to go down, which reduces the lift forces. We tuned the geometry of the robot very precisely so lift proportionally increases with the additional actuator weight,” Chen explains.
They were able to achieve a lift-to-weight ratio of 1.9, giving the robot more than enough lift force to carry the onboard electronics package they developed, which weighs only 244 milligrams.
The tiny electronics package contains the sensors, and microcontroller needed for onboard sensing and computation.
The researchers incorporated an inertial measurement unit to estimate attitude, an optical flow sensor to estimate lateral flight speed and position, and a time-of-flight sensor to measure height.
But without the precision of the attached motion capture system, the robot does not know its absolute position, causing it to drift off course.
Speedy sensing
To overcome this challenge, the team designed a sensing algorithm to calculate the robot orientation, angular velocity, and position extremely quickly, simplifying the calculations to reduce the computational cost.
They found that estimating position continuously at a faster rate yielded higher performance than a more accurate, slower estimation.
“We spent a lot of time optimizing the selection of the sensors and position estimators so the robot would have very low drift. Our robot can now fly with positional accuracy that is comparable to flying with offboard cameras,” says Hsiao.
They integrated the sensors and computing components into a tiny electronics package, which they attached to a fiberglass substrate so it wouldn’t be thrown off by vibrations of the robot.
“When you are talking about a computer which is that small, everything must be thought through carefully. There are so many factors to consider; it must do both perception and control, while fitting onto the robot and running fast enough that the vehicle will remain stable during flight,” How says.
They tested the offboard computation capabilities of the aerial microrobot through a series of flight demonstrations, including hovering at different heights and following point-to-point trajectories. The robot maneuvered quickly and precisely, with positional errors of only a few centimeters.
In addition, they demonstrated the robot’s potential for artificial pollination by using a joystick to send high-level position setpoints, guiding the aerial vehicle around several plants before carefully landing on a sunflower.
“This is quite difficult to do, even if you do have a motion-capture system,” Hsiao says.
The researchers analyzed the vehicle’s power expenditures and found the electronics only consume about 6 percent of the total power, with the rest fueling the robot’s artificial muscles and wings.
They identified ways to further reduce power consumption from the electronics. This would allow for the addition of more components, like a camera that would enable the robot to recognize objects.
The researchers are now working toward two goals: putting a camera onboard for autonomous object recognition and obstacle avoidance; and integrating power electronics and batteries onto the tiny robot, which would enable untethered flight in an outdoor environment.
This research was funded by the U.S. National Science Foundation (NSF), U.S. Office of Naval Research, U.S. Air Force Office of Scientific Research, MathWorks, and a Zakhartchenko Fellowship.
