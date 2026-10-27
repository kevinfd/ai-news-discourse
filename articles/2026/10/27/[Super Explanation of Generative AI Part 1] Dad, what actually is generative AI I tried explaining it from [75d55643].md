---
id: "75d556435b205ca5"
title: "[Super Explanation of Generative AI Part 1] \"Dad, what actually is generative AI?\" I tried explaining it from the basics as if I were talking to my middle school son"
url: "https://note.com/honyaku_ai_30/n/n63b6a4825e5c?hl=en"
link: "https://note.com/honyaku_ai_30/n/n63b6a4825e5c?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-27T01:01:00Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["ほんやく"]
language: "en"
summary: "\"If you use generative AI, you can make your work more efficient.\"\"From now on, people who can master AI will...\"I've been seeing talk like that quite often lately.But what exactly is generative AI in ..."
tags: []
orgs: ["Google", "Amazon", "IBM"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 3032
paywalled: false
image: "http://www.bing.com/th?id=ONUT.xgP6cMq8ZGS45CAju5GmtQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# [Super Explanation of Generative AI Part 1] "Dad, what actually is generative AI?" I tried explaining it from the basics as if I were talking to my middle school son

note · ほんやく · 2026-10-27

[Super Explanation of Generative AI Part 1] "Dad, what actually is generative AI?" I tried explaining it from the basics as if I were talking to my middle school son
"If you use generative AI, you can make your work more efficient."
"From now on, people who can master AI will..."
I've been seeing talk like that quite often lately.
But what exactly is generative AI in the first place? How is it different from regular AI or search engines? I imagine there are some people who find it hard to ask about it now.
I also use AI for my work and side projects. However, using it and being able to explain it clearly to others are two different things.
So, starting with this post, I'm going to begin a series called "Super Explanation of Generative AI."
I have a middle school son, so this time I took on the role of a teacher and summarized the basics in a conversation format as if I were teaching him.
There are no difficult mathematical formulas here. I would be happy if there is even one point where you think, "So that's what it was."
Period 1: What does the "generative" in "generative AI" mean?
Son: Dad, you've been using AI all the time lately, but what is generative AI in the first place?
Dad: First of all, "generative" means "to create." Generative AI is AI that uses the characteristics it has learned from a vast amount of data to create things like text or images.
Son: Are AI and generative AI different things?
Dad: Rather than being completely separate, generative AI is part of the big family called AI.
AI stands for "Artificial Intelligence." It is used as a general term for technology that allows computers to perform tasks that humans consider intellectual, such as identifying, predicting, and handling language.
For example, there are AIs that identify whether an email is spam or predict product sales based on past data. Among those, generative AI is the kind that creates content like text or pictures.
Son: Is it the difference between answering "This is a photo of a cat" and "I will draw a picture of a cat"?
Dad: As an initial image, that's easy to understand. However, current services sometimes include both the ability to read photos and the ability to create text or pictures. They aren't necessarily divided into neat, separate apps.
Son: Then, generative AI isn't just the stuff you chat with.
Dad: That's right. Chatting is just one way to use it. There are also generative AIs that create images, audio, music, videos, and more.
Reference for basic definition: IBM"What is generative AI"
Period 2: Why can it answer so many different things?
Son: But how did it learn to write sentences? Did someone input all the answers?
Dad: It's not like a person registered every possible question and answer one by one. It's easier to understand if you separate the "learning phase" from the "usage phase."
In the "learning phase," we use a massive amount of examples like text and images to adjust the numerical values inside the computer. It learns the relationships and usage of words for text, and features like shapes and colors for images, in a way that can be calculated.
The mechanism created this way to generate answers is called a "model."
Son: Like a fashion model?
Dad: It's the same word, but it has a different meaning here. For now, you can just remember it as "the AI's calculation mechanism created through learning."
And in the "usage phase," we make requests to that trained model. Then, it uses the request and any provided materials as clues to create an answer.
Son: Is it like someone who has practiced cooking a lot being asked, "Make something using eggs today"?
Dad: That's a close analogy. It uses what it learned through practice and what it was just asked to do to create the output. However, that doesn't mean the AI is experiencing or understanding things the same way a person does.
Son: Does it study from scratch every time I talk to it?
Dad: In normal conversation, it doesn't relearn the entire model every time.
Using the content of a conversation as a clue in the moment is different from retraining the model. Depending on the service, there may be a memory function to save information, and sometimes conversations are used for later development or learning. That varies depending on the service and settings.
Just because it "seems to remember the current conversation" doesn't mean that "the AI used by people all over the world learned from my story on the spot."
References for terminology and mechanisms: AWS"What isGenerativeAI", Google Cloud"GenerativeAIGlossary"
Lesson 3: How are sentences created?
Son: I understand that it learns, but I find the part where it actually outputs sentences mysterious.
Dad: For representative AIs that create text, the basic principle is to predict "what is likely to come next, based on the text and instructions so far."
For example, suppose you ask it, "Tell me what to bring on a rainy day in one sentence."
"Today is"
"raining so"
"I will take"
"an umbrella"
It's like building the continuation little by little like this.
Son: Is it like predictive text on a smartphone?
Dad: It's similar as an introductory analogy. But it can use not just the continuation of short phrases, but also long requests and document content as clues. Since it also connects to explaining, translating, and programming, thinking it's exactly the same as predictive text is a bit too narrow.
In reality, it handles text by breaking it down into small units called "tokens." Sometimes these are whole words, and sometimes a single word is broken down further. The divisions in the diagram are just examples to make it easier to understand.
Son: Does it always choose the most likely word?
Dad: Not necessarily. There are differences in how candidates are chosen, so even with the same question, the phrasing can be different.
Also, additional training is performed to provide answers that are helpful for conversation. Hearing that it "predicts the next word" sounds simple, but that alone doesn't explain the entire mechanism.
Son: So, it doesn't have long answers already finished from the start, then.
Dad: Right. It's not a mechanism that retrieves a ready-made answer every time. However, sometimes expressions very similar to the text it learned appear. You can't say, "Because it was generated, it's definitely a text unlike anyone else's."
Reference for the prediction that forms the basis of text generation: Research paper "Better & Faster Large Language Models via Multi-token Prediction"
4th Period: How is it different from searching?
Son: But if it answers when you ask, isn't that the same as an internet search?
Dad: There is a difference in their basic roles.
Searching is finding information that already exists. Generation is assembling content according to a request.
If we use a library as an example, searching is "finding relevant books or pages." Generation is "drafting an explanation." It's easy to understand if you think about that difference.
Son: Then, are there things the AI hasn't checked on the net even if I ask it?
Dad: Yes, there are. This is important. Just because the AI gave an answer doesn't mean it checked the latest internet information every time.
On the other hand, there are services that use search functions to create answers based on the information found. So now, there are cases where "searching" and "generating" are connected on one screen.
Son: What about when I want to know today's news?
Dad: You want to see if it's an answer that actually verified the latest information. If there are sources attached, open those pages and check the date and content as well.
Even with answers using search results, it can sometimes misunderstand information or pick up only parts of it.
Reference for the mechanism combining search and generation: IBM"What is RAG (Retrieval-Augmented Generation)?"
5th Period: It's useful, so why does it make mistakes?
Son: It answers so thoroughly, but it can make mistakes too.
Dad: Yes. And it can make mistakes in very natural-sounding sentences.
It might introduce books that don't exist, mix up people's names or dates, or explain things as if they were written in the source material when they actually weren't.
This phenomenon of producing plausible but incorrect content is sometimes called a "hallucination."
Son: I wish it would just say "I don't know" if it doesn't know.
Dad: I agree. However, being able to create a natural-sounding answer and being able to verify that the content is factual are not the same thing.
Sometimes information is missing, the question is ambiguous, or the learned information is outdated. Just asking it "don't make mistakes" won't completely prevent them.
Son: So, should I doubt all of its answers?
Dad: Rather than treating everything with the same level of skepticism, I think it's easier to use if you are mindful of "areas where mistakes would be a problem."
If it's for fictional story title ideas, its free-thinking is useful. If it's for historical dates used in a school presentation, check them against textbooks or reliable sources. If it's for decisions involving money or health, don't rely solely on the AI's answer.
Son: So you can't judge it by whether it's written confidently or not.
Dad: Exactly. Separate the way it's phrased from the accuracy of the content. I think that's an important lesson for adults, too.
Reference for incorrect answers and the need for verification: AnthropicOfficial Help
6th Period: Specifically, what can I ask it to do?
Son: I understand the mechanism a little now. So, what is it useful for?
Dad: For example, things like this.
Son: How do you use it, Dad?
Dad: Organizing article ideas or drafting text. At work, I sometimes have it organize difficult instructions into explanations that are easier for me to understand.
For example, you give it a long text and ask it to "summarize the three most important points." That's summarization. However, you should check the original text to make sure no important conditions were left out.
Son: It seems like it could be used for studying, too.
Dad: You could think of ways to use it like asking, "I don't understand this explanation, so rephrase it using familiar examples," or "Don't give me the answer, just give me the first hint."
If you just accept the answer as a whole, you won't know if you've actually understood it. I think it's a good idea to try explaining it back in your own words after it has explained it to you.
Son: Can it make games, too?
Dad: It can help write programs. Code is basically a set of instructions written for a computer. However, the code it produces won't necessarily work, nor is it guaranteed to be safe. You will need to test and fix it.
Son: So it's not like it completes everything in one go.
Dad: Exactly. It's easier to think of it as a tool to help you come up with ideas or to assist you when you're stuck. What it can do also varies depending on the service or the features available.
7th Period: Are images created in the same way as text?
Son: I understand how it continues text, but do images have a "next word" too?
Dad: There isn't just one way to create images, so the exact same explanation as for text isn't enough.
One representative method is the "diffusion model." Simply put, it's a mechanism that gradually creates an image from grainy noise.
Son: Like something blurry gradually turning into a cat?
Dad: That's the right image. If you ask for "a white cat sleeping on a windowsill," it uses those words as clues to create an image with the characteristics of a cat and a windowsill.
However, it's not that a finished cat was hidden in the initial noise and it's just discovering it. It uses the features it has learned to give shape to the image.
Son: So it's not like it's searching the internet for cat ears and bodies and pasting them together.
Dad: As a basic explanation, it's different from cutting and pasting. However, it can sometimes resemble existing works, and it doesn't mean that anything you generate can be used freely.
Also, not all image generation uses diffusion models. For now, it's enough to remember that "the way text and images are created can be different."
Reference for how image generation works: IBM"What is a diffusion model"
8th Period: How should I ask it so that it understands me well?
Son: Do I have to learn difficult commands to use it?
Dad: At first, normal language is fine. We call requests and instructions to AI "prompts," but you don't have to think of them as special spells.
For example, if you ask a friend to "buy me something" versus "buy me some bread for lunch that costs under 500 yen," the information conveyed is different, right?
Son: With the first way of asking, they might buy me a snack.
Dad: Something similar happens with AI. The four things I try to keep in mind are these.
"For what purpose," "for whom," "using what materials," and "in what format."
Son: I want a concrete example.
Dad: For example, this is a fictional request for practice.
Son: With this, it's clear what you want it to create.
Dad: I also make sure to state the purpose first when I create work documents. If that isn't conveyed, even if the writing is excellent, the document might end up going in the wrong direction.
Son: What if I can't say everything properly from the start?
Dad: You can just fix it along the way. You can continue to ask things like "make it shorter," "this phrasing is difficult," or "include one example."
It's not a test where you have to make the perfect request in one go. You can clarify what you wanted while looking at the answers that come out.
Reference for ways of thinking about conveying clear instructions and background: Anthropic"Prompt Engineering Best Practices"
9th Hour: Before you use it, you must know at least this
Son: Then, if I put in all my school handouts and conversations with friends, will it teach me various things?
Dad: Before you put them in, let's think about that for a moment.
Names, addresses, face photos, and things friends told you in confidence are not information you should hand over lightly, right? If it's my work, customer manuscripts and company secrets are the same.
The storage and use of input information for learning differ depending on the service, contract, and settings. At work, you need to confirm the environment and rules approved by the company.
Son: If it's "not used for learning," does that mean it's not saved either?
Dad: Those are two separate things. Whether it's used for learning and whether history or other data is saved are things we should check separately.
If you're practicing for the first time, it's easier to use fictional content where individuals aren't identifiable, like the school festival example from earlier.
Son: What about having it do all my homework?
Dad: Following school rules comes first. Beyond that, I want to think about how to ask for help in a way that actually helps you learn.
Just saying "write the whole essay" doesn't show if you've become able to write it yourself. Asking "tell me the parts of my essay that are hard to understand" might lead to practice in rewriting.
The age requirements for minors and the conditions for parental consent vary by service, so let's check them together when you start using it.
Son: So, just because it's convenient doesn't mean I can give it anything or leave everything to it, right?
Dad: Exactly. I think just thinking a little about how you use it will change how you interact with it.
Finally: Rather than a "teacher who knows everything," it's about how you interact with it
Son: To summarize today's talk, generative AI is something that learns from many examples and creates text or pictures based on requests. But what it produces isn't always correct.
Dad: Yeah. You've got the important points down.
Son: So, I need to convey my requests clearly, look at the answers and correct them, and check the important parts.
Dad: I want to value that way of using it too, Dad.
Son: Then, what you need to use AI isn't knowing a lot of difficult words?
Dad: You don't need to know everything from the start. You can begin by just conveying "what you want to do" and "what you don't understand."
And don't pretend to understand things you don't. Being able to say, "I don't understand that part, so can you explain it again?" is a convenient thing about AI used in conversation.
In organizing this to explain it to my son, I felt that "the more familiar a word is, the harder it is to explain."
When using generative AI, you tend to want to talk about "how amazing it is that I could do this." But I feel that knowing "what it is in the first place" makes it easier to understand both its convenience and its limitations.
In this series, I would like to talk about AI that creates videos, AI that runs in-house or on local environments, and AI agents that handle multiple tasks in the same way.
By the way, these three are not neatly categorized side-by-side. They are different perspectives: "what to create," "where to run it," and "how to proceed with the work." I plan to unravel those points one by one in future installments.
I want to make this a series that is easy to read, both for those who felt they couldn't ask until now and for those who want to try using it from here on out.
Please let me know if there is anything about AI that you "actually don't quite understand." I would be happy if I could make it the theme of our next lesson.
