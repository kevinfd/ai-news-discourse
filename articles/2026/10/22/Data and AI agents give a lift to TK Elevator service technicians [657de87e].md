---
id: "657de87e70512b3c"
title: "Data and AI agents give a lift to TK Elevator service technicians"
url: "https://news.microsoft.com/source/emea/features/data-and-ai-agents-give-a-lift-to-tk-elevator-service-technicians"
link: "https://news.microsoft.com/source/emea/features/data-and-ai-agents-give-a-lift-to-tk-elevator-service-technicians"
source: "Microsoft Source"
domain: "news.microsoft.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-22T13:58:15Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["sbaynes"]
language: "en"
summary: "Tags: \n\n AI Customers \n\n The post Data and AI agents give a lift to TK Elevator service technicians appeared first on Source ."
tags: ["Digital Transformation", "AI", "Customers"]
orgs: ["Microsoft", "OpenAI"]
topics: ["agents & coding", "business & funding", "jobs & society", "search & media"]
content_source: "fulltext"
word_count: 1648
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Data and AI agents give a lift to TK Elevator service technicians

Microsoft Source · sbaynes · 2026-10-22

Data and AI agents give a lift to TK Elevator service technicians						 
					
									
DÜSSELDORF, Germany — Torben Teichmann, a service technician for TK Elevator, arrives at an office building. To do maintenance on an elevator, he dons his hard hat, safety glasses and gloves and takes out the tools he needs to access the parts of the elevator the public rarely sees.
In the past, Teichmann might have needed to manually find information: ask around to find the elevator, track down the notebook containing handwritten service notes and search through hundreds of pages of technical manuals. He might have discovered he needed other tools, requiring trips back to his car. Once the work was complete, he wrote up his notes, usually in his car, “and it’s not so comfortable to write there.”
Today, however, an agentic AI app, created with Microsoft Foundry and Azure OpenAI in Foundry Models, briefs Teichmann through his phone or tablet about the elevator before he even enters the building. He knows which tools to take with him. He knows which elevator, on which floor, and what the issue is — whether it’s regular maintenance or a service call for a problematic door, for example. On his phone, he can search digital manuals or the previous service history of the elevator.
							   “I love AI. It’s really easy. (…) I’m the boss at the job site and the AI is my buddy that gives advice.” 
						   
Torben Teichmann, a service technician for TK Elevator. Photo by Max Brunnert for Microsoft.
Afterward, another AI voice agent asks him questions about the work he has performed, which he can explain in his own words. The debriefing agent records Teichmann’s answers without requiring any writing or typing. It asks follow-up questions if more detail is needed.
The exchange works in both directions. The assistant draws on information collected from earlier visits, while Teichmann’s spoken debrief adds his experience to the record for colleagues who may service the equipment later. In the end, his debriefing notes are essential. Not just for him but for future generations of technicians. As TKE has 25,000 highly qualified service technicians globally, there are significant learnings from other parts of the world Teichmann can draw upon. In turn, his learnings will help colleagues across Germany and in other parts of the world.
“I love AI,” Teichmann says. “It’s really easy. The best is it’s information I need now,” he adds, pointing his finger to emphasize the urgency. “I’m the boss at the job site and the AI is my buddy that gives advice.”
The agents draw on a digital foundation TKE has developed over the past decade by connecting elevators and escalators to the secure cloud and bringing together the connected-equipment data, service information and technical documentation using Microsoft Azure.
Keeping people moving
Based in Düsseldorf, TK Elevator (TKE) manufactures, installs and services elevators and escalators, called “units” in industry parlance. Once purchased, those units are the property of the building owner. TKE has service contracts to maintain them, much the way an individual buys a car and takes it to the dealer for annual checkups. Units can last for decades, so maintenance plays an important role at TKE, whose 25,000 service technicians care for 1.4 million units globally.
The work is largely invisible when everything is running. But when an elevator breaks down, it quickly affects how people move through their day. TKE says its units carry 1.5 billion passengers a day.
“Our equipment is infrastructure critical,” says Christian Fongern, CEO of TKE Germany. “Imagine in an airport, in a hospital or in an office, an elevator or escalator is not working. This has tremendous impact on the people in that building. Our utmost target is to keep the elevators running. Uptime is our mission critical statement here, and service is the heart of our business.”
Most of the work is regular maintenance; not every service call involves a mechanical failure. Everyday use can also cause problems. For example, physical force applied to elevator doors or buttons, chewing gum deposited under an escalator handrail, all manner of small items (keys, coins, baby pacifiers) falling through the gap by the elevator door. Birds and mice manage to enter and make a mess. Dirt tracked in by so many shoes is one of the biggest problems, clogging the door rails or blocking a sensor. Whether the visit is planned or not, AI agents are intended to make the work easier by helping technicians find relevant information more quickly.
						Making the most of IoT 
					
TKE began digitally connecting elevators and escalators around a decade ago, using sensors and digital controllers to collect information about how the equipment was operating. From the start, it brought that information together in a central data platform using Microsoft Azure, Azure IoT and Azure Databricks and built it out further in partnership with Microsoft Industry Solutions Engineering, now called Microsoft Frontier Company.
Creating a common data environment was particularly important as TKE added different types of equipment through acquisitions. That meant servicing units made by other manufacturers, as well as introducing its digital-native EOX and HELIX elevators. More recently, generative AI has started to allow the company to draw on information that does not sit neatly in operational systems, including technical documents and technicians’ service notes.
“Everything we did before was on structured data,” says Christian Jung, head of digital data and AI foundation at TK Elevator. “It was either IoT data or enterprise data sitting in systems already. But we were not able to leverage data from unstructured sources.”
Sensor readings can show what an elevator is doing. But much of the knowledge needed to diagnose a problem may be elsewhere: in a technical manual, a previous technician’s notes or a description of what happened during an earlier visit. Generative AI allows TKE to extract, search and draw connections across these sources.
“We were able to give technical guidance to technicians on how to fix a problem,” Jung says.
For example, the same models of elevators or escalators in different buildings may get very different usage and service history — useful information when it’s time to maintain or repair a unit. Other context — the location of the unit, the business hours, the specific floor having a problem — can save a service technician significant time and frustration. It’s all the kind of information that generative AI can process easily but that was difficult to gather and share before.
						Getting real insights from data 
					
Collecting the data was only the first step. TKE created nine digital operations centers, or DOCs, where data analysts and technical specialists look for patterns that could help technicians identify emerging problems or prioritize maintenance.
Tobias Lüsebrink heads digital transformation for TKE Germany and works at the DOC in Berlin, where data analysts and technical elevator experts work closely to interpret data and find patterns. In addition to their desktop computers, big screens on the DOC’s walls let the team observe different situations in the field in real time so they can react quickly.
The DOCs track the status of the connected units, events recorded, error codes, etc. They use machine learning to calculate “health scores” for the connected units to help prioritize maintenance work. Should they spot breakdowns, they look for any patterns. “They’re using several sources of information, bringing them together and comparing these over time and across similar equipment,” Lüsebrink says. If they spot patterns, they send out recommendations to the service technicians.
An elevator door might open and close several times before the lift moves, then appear to work normally for days. To a passenger, it may seem like a momentary glitch. Data from the connected unit can reveal whether the behavior is recurring.
Thanks to IoT, the DOC “will see this kind of abnormal operation,” Lüsebrink says. “It’s not really a breakdown, but it’s pointing in a direction that something is not normal and it might lead to a breakdown if we don’t do something.”
							   Sharing experience for continuous learning 
						   
The DOC can flag the recurring behavior and share relevant information, including which floor has the affected door. The technician then inspects the equipment and uses their training and judgment to determine what action is needed.
The information also flows back from the field. A technician may find that the initial signal does not reflect the problem they encounter on site, or that several different faults could produce similar symptoms. Their debriefing notes help TKE refine future troubleshooting and identify new patterns.
“We use the feedback of our technicians in the field to do more precise troubleshooting or even prevent breakdowns,” Lüsebrink says.
Other technicians can also benefit, particularly those who are newer to the job. An experienced technician may recognize clues from the sound and feel of the ride, but that judgment can take years to develop, Lüsebrink says. Technology can’t capture all their expertise, but it can offer relevant suggestions based on the shared notes of the worldwide technician team. Lüsebrink adds that younger technicians expect to use digital tools.
							   “We have good documents, but the knowledge is in the brain of my colleagues,” says Teichmann, who has been a service technician for 12 years. “I can transfer my knowledge over the application to my colleagues, and the application provides it when they need this kind of information.” 
						   
Torben Teichmann, a service technician for TK Elevator, at work in Düsseldorf, Germany. Photo by Max Brunnert for Microsoft.
Teichmann puts the elevator back in service and dictates his conclusions to the debriefing agent. “You see how important it is to get it back to work quickly, even if it’s routine maintenance,” he says. AI agents can relieve some of the frustration of his job — finding the right elevator, bringing the right tools, taking notes — but as long as coins fall and shoes are dirty, he will have elevators to fix.
