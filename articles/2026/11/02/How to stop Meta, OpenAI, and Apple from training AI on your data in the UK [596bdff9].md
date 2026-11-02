---
id: "596bdff9e4a56a9e"
title: "How to stop Meta, OpenAI, and Apple from training AI on your data in the UK"
url: "https://hotminute.co.uk/2026/11/02/how-to-stop-meta-openai-and-apple-from-training-ai-on-your-data-in-the-uk"
link: "https://hotminute.co.uk/2026/11/02/how-to-stop-meta-openai-and-apple-from-training-ai-on-your-data-in-the-uk"
source: "HotMinute"
domain: "hotminute.co.uk"
source_type: "community"
collector: "reddit"
date: "2026-11-02T11:03:37Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["HotMinuteUK"]
language: "en"
summary: "How to stop Meta, OpenAI, and Apple from training AI on your data in the UK\nThe world’s largest AI companies, including Meta, OpenAI, and Apple, all offer UK users ways to keep their data out of AI training.\nThis comes after the Information Commissioner’s Office (ICO) published a report in October which notes that training foundation models involves processing personal data, so people have the…"
tags: ["r/artificial"]
orgs: ["Meta", "Apple", "OpenAI", "Anthropic", "UK"]
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 989
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xlu9ui/how_to_stop_meta_openai_and_apple_from_training/"
score: null
comments: null
community: "r/artificial"
---

# How to stop Meta, OpenAI, and Apple from training AI on your data in the UK

HotMinute · HotMinuteUK · 2026-11-02

How to stop Meta, OpenAI, and Apple from training AI on your data in the UK
The world’s largest AI companies, including Meta, OpenAI, and Apple, all offer UK users ways to keep their data out of AI training.
This comes after the Information Commissioner’s Office (ICO) published a report in October which notes that training foundation models involves processing personal data, so people have the right to submit requests to foundation model developers about that data.
These rights apply to both first-party data and third-party data, the regulator said.
“Personal data may be present not only in training datasets but also in the models themselves, which creates challenges for exercising data rights,” the ICO said.
“There are currently limited technical means of identifying whether, and to what extent, a specific person’s personal data is represented within a trained model. Nevertheless, developers must provide individuals with clear information about the use of this data and how they can exercise their rights, regarding both training data and trained models.”
The regulator noted that through its supervisory and policy work on foundation model development, it identified concerns about the accessibility and appropriateness of some developers’ mechanisms for enabling people to exercise their rights where their personal data has been used to train foundation models.
It added that in some cases, developers had not implemented clear and effective mechanisms to enable people to exercise rights such as access, erasure, and objection.
Meta
Meta has established dedicated mechanisms for both users and non-users, including:
- An objection process relating to the use of first-party personal data6 for AI training;
- A separate form for third-party data subjects to raise concerns about the use of their information.
Notably, Meta’s process asks third-party data subjects to provide the prompt that generated the relevant output and a screenshot of the output itself. This offers a practical way to address the difficult problem of transparency for third-party data contained in a model.
To find the form, users will need to open the Facebook or Instagram app and go to Settings > About > Privacy Policy, then tap the ‘Right to object’ link.
The form asks for the email address linked to the account. A box for explaining how the processing affects you is optional. Meta will then send an email to confirm it has received the objection.
It should be noted that the objection only applies to future training rounds. Meta keeps data it has already used to train its models.
OpenAI
By default, ChatGPT uses conversations with the user to train its models unless this is turned off by users.
To access the setting on the web, users need to click on their account menu, then Settings > Data controls, and turn off ‘Improve the model for everyone’.
It should be noted that OpenAI said that requests are assessed on a case-by-case basis and involve balancing an individual’s privacy rights against other important considerations, such as freedom of expression and the public interest.
Anthropic
Much like OpenAI, Anthropic gives users the option to contact them about the use of personal data for its Claude model but does not make a guarantee that it will stop using it.
“If we incidentally collect personal data in our training data, we do not link it to a specific individual. Models do not store text like a database, and they do not have access to or pull from the original training data once the models have been trained.
“As a result, there are limitations on our ability to identify information from our training data that relates to a specific individual in response to a rights request.”
Anthropic added that it does use techniques that can reduce the likelihood of data from our training data being reproduced by Claude.
” However, if you have a concern about your personal data being included in a response provided by Claude, you can contact us. To help us assess your request, please give us as much relevant detail as you can.
“This should include information such as your name, email address, screenshots or details of the response that shows your personal data, the prompt used, or the URLs referenced. We’ll consider the specific circumstances of your request in accordance with local legal requirements.”
Apple
Apple noted that it does not use any personal AI to train its foundational models, but does train it on public web pages that its Applebot crawler views.
Apple provided a dedicated process for people to object to the web-crawling and use of personal data contained on publicly accessible webpages for foundation model development. This can be done by:
Individuals can ask Apple to stop processing their publicly available data for AI training through its Apple Intelligence Privacy Inquiries form. The form lets people name specific web pages Apple should not use.
Website owners can also block AI training without dropping out of Siri and Spotlight results. This works by adding these two lines to the site’s robots.txt file:
- User-agent: Applebot-Extended
- Disallow: /
Moving forward
In terms of training data, the ICO said that developers must have clear, accessible and appropriate mechanisms for enabling and responding to requests from the people the information is about. This includes requests about third-party data.
The mechanisms available should enable people to easily understand their rights about their personal data. This includes:
- When you’ve used their information to train a model;
- How they can exercise their rights;
- What information they need when submitting a request.
In this case, developers should provide:
- Dedicated and clear routes for submitting requests;
- Information about any technical limitations that may affect the outcome of a request;
- The rationale for any decision to refuse a request.
The UK GDPR contains limited exemptions and circumstances in which a developer doesn’t have to comply with a request. For example, where they can demonstrate that they genuinely can’t identify the person the information is about.
