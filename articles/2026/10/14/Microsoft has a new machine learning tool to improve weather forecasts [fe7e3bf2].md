---
id: "fe7e3bf246c62145"
title: "Microsoft has a new machine learning tool to improve weather forecasts"
url: "https://theverge.com/science/1011127/ai-weather-forecast-microsoft"
source: "The Verge"
domain: "theverge.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T16:05:21Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Justine Calma"]
language: "en"
summary: "Old-school physics-based weather forecasting and even new AI models typically become less reliable beyond two weeks, a problem Microsoft claims to have solved using machine learning. \n Researchers with the company say they've found a new, cost-effective way to make more accurate weather forecasts two to six weeks in advance - allowing farmers and emergency responders to plan ahead with greater…"
tags: ["AI", "Environment", "Microsoft", "Science", "Tech"]
orgs: ["Microsoft", "Google", "Nvidia"]
topics: ["models & research", "safety & ethics", "chips & infrastructure", "health & science"]
content_source: "fulltext"
word_count: 711
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft has a new machine learning tool to improve weather forecasts

The Verge · Justine Calma · 2026-10-14

Old-school physics-based weather forecasting and even new AI models typically become less reliable beyond two weeks, a problem Microsoft claims to have solved using machine learning.
Microsoft has a new machine learning tool to improve weather forecasts
New open-source software could make AI-enhanced weather forecasting more affordable.
Researchers with the company say they’ve found a new, cost-effective way to make more accurate weather forecasts two to six weeks in advance — allowing farmers and emergency responders to plan ahead with greater certainty. The findings were published today in the journal Nature, and the tool is now open-source software.
Microsoft joins Google, Nvidia, and other companies developing AI tools for weather forecasting. Instead of creating a new standalone weather model, Microsoft’s latest research in this realm uses machine learning to correct bias in existing models. It’s a more accessible way for resource-strapped weather agencies to improve accuracy using AI, the researchers hope.
It’s a more accessible way for resource-strapped weather agencies to improve accuracy using AI
While physics-based modeling is a resource-intensive endeavor running on supercomputers and generative AI depends on powerful GPUs, Microsoft Research New England senior principal researcher Lester Mackey says the new tool can run just on CPUs. “I have a lot of hope both for the increased resource efficiency of weather forecasting and the extended reliability of forecasts, especially for extreme weather,” Mackey tells The Verge.
Physics-based and AI-based models run into similar problems when they start predicting the weather two weeks or more in advance. Traditional models attempt to simulate the complex physics of Earth’s atmosphere, while AI models look for patterns in historical data to make forecasts. In both approaches, models rely on approximations to fill data gaps, whether from regions with sparse weather stations or complex atmospheric phenomena that scientists are still working to understand. The ways in which these models make up for those gaps in data can become a type of systematic bias. The resulting errors compound when making forecasts further ahead in time, making these predictions less precise.
Microsoft calls its method Probabilistic Bias Correction (PBC). The tool uses machine learning to identify systematic bias in a model and make corrections. One example Mackey gives is to correct for changes in climate. Greenhouse gas emissions from fossil fuels are heating up the planet, but a weather model might make predictions based on historical records that can bias it toward colder temperatures than the world is actually experiencing today.
The researchers found that PBC improved the accuracy of a leading physics-based weather model by the European Centre for Medium-Range Weather Forecasts (ECMWF) for 98 percent of precipitation and 92 percent of temperature targets. The machine learning framework also doubled the accuracy of ECMWF’s new AI forecasting system in the study’s analysis. Before the paper was published, the ECMWF had already awarded the authors’ research on PBC in its AI Weather Quest competition.
The new paper on PBC published by researchers at Microsoft, MIT, ECMWF, and other institutions “is a good example of new ideas being developed for the benefit and consideration of the community,” Matthew Chantry, ECMWF’s strategic lead for machine learning, said in an emailed comment to The Verge.
“As always, turning ideas into reality [in] an operational process is a most challenging step,” Chantry added.
The amount of compute and infrastructure needed for weather forecasting has often left technological advances out of reach for many agencies in economically developing countries. The paper’s authors, however, think PBC can be different. “One of the things that’s really exciting to me about models like PBC is how lightweight they are, how easy to train, that scientists without huge pools of resources can work on trying to configure [these] models and make them perform better in specific localities,” says Genevieve Flaspohler, one of the authors of the paper.
Flaspohler worked on PBC as an intern at Microsoft with Mackey, and now she’s the executive director of the nonprofit Rhiza Research, which is working with the Kenya Meteorological Service Authority — with funding from the Gates Foundation — to see whether AI can help get more accurate early warnings out to people. PBC is one of the methods they’re testing ahead of what’s expected to be a more extreme rainy season during a record-breaking El Niño.
