---
id: "7c60087412687908"
title: "Claude just found a CRISPR-like DNA pattern, but even Anthropic's scientists aren't sure what it does"
url: "https://scientificamerican.com/article/claude-just-found-a-crispr-like-dna-pattern-but-even-anthropics-scientists-arent-sure-what-it-does"
link: "https://scientificamerican.com/article/claude-just-found-a-crispr-like-dna-pattern-but-even-anthropics-scientists-arent-sure-what-it-does"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T10:00:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Adam Kovac"]
language: "en"
summary: "The large language model took less than a day to identify the curious stretch of DNA"
tags: []
orgs: ["Anthropic"]
topics: ["health & science", "models & research", "chips & infrastructure", "search & media"]
content_source: "fulltext"
word_count: 1772
paywalled: false
image: "http://www.bing.com/th?id=ONUT.LmoiSNZ4iappeU-V7pdVIw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Claude just found a CRISPR-like DNA pattern, but even Anthropic's scientists aren't sure what it does

Scientific American · Adam Kovac · 2026-10-14

Artificial intelligence companies have been making waves in mathematics, but they are also turning their attention to other sciences, too—including molecular biology.
Late last month, Anthropic claimed it had discovered a curious stretch of DNA in a virus called a bacteriophage that repeats over and over again. This is a similar feature to that of CRISPR, the basis of the powerful gene-editing tool CRISPR-Cas9.
The newly discovered DNA repeats sit next to a gene for a reverse transcriptase enzyme, a type of enzyme that copies RNA into DNA—a hint that this discovery may have some useful properties. But Eric Kauderer-Abrams, Anthropic’s head of life sciences, and Nicholas Perry, a researcher at the company, are clear: it’s still unknown exactly what this enzyme and the neighboring repeating pattern of DNA actually do.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
Claude, Kauderer-Abrams says, displayed intuition and persistence similar to that of a real biologist in the lab, showing “exactly the type of logic that the really talented computational biologists that we work with would go after.”
But much more work is needed to understand what this region of the genome does, and Claude is no replacement for biologists, the scientists say. “What this internal domain does, we’re still not sure,” Kauderer-Abrams adds.
Scientific American spoke to Kauderer-Abrams and Perry to find out how they got Anthropic’s AI model Claude on the hunt for these interesting bits of DNA in the first place and how it found this stretch of DNA.
[An edited transcript of the interview follows.]
When you decided to use Claude to search for patterns in DNA, what did you hope to find?
KAUDERER-ABRAMS: Our efforts in the life sciences are organized around two goals. The first is to dramatically accelerate the pace of basic science, and the second is to accelerate curing disease and extending health span. The first scientific problem that we decided to directly pursue ourselves was trying to find and systematize and scale up the process of finding useful new things that already exist in nature and turning them into tools that that have utility in science and medicine. We were inspired from how many great discoveries that went on to revolutionize science and medicine came about from looking around in nature and finding these odd things—PCR [polymerase chain reaction] tests, for example, or CRISPR. We believe that, with [an] AI agent collaborating in every step of the process, we would be able to increase the rate of making these sorts of discoveries.
I want to clarify one important thing: citing this amazing lineage of discoveries, we are by no means claiming that what Claude has discovered here is of that status. This was the first discovery in our lab that Claude made on its own, and we’re excited by it. But we’re very early; it’s the very beginning.
We know that it has these interesting properties that may be suggestive of having some potential as a tool, but we have no idea what its function is yet, and we’re at the very beginning of the research.
What training data and prompts made this possible for Claude?
KAUDERER-ABRAMS: Great question. We do a lot of work on each of those two things. On the training data, we have been putting a tremendous amount of energy into training Claude in biology—in the hardcore scientific tasks like bioinformatics and structural biology and organic chemistry and some of the softer things ... related to trying to have research taste and some level of strategic decision-making for things on the drug development side.
As for what prompts we use, in this case, we gave Claude a fairly generic prompt to go looking for particular patterns in DNA sequences that are associated with reverse transcriptase enzymes. We’ve run these sorts of searches through other families [of DNA polymerases], but it was a fairly generic prompt. Obviously, it’s not a prompt that an amateur biologist would have written.
What we asked Claude explicitly for in this prompt was to go and look for accessory proteins that might be hitching a ride along with these reverse transcriptase genes. And what Claude found was actually not that but this array of repeats in noncoding RNA. That’s what triggered Claude, realizing that that this might be a more interesting system that’s worth paying attention to.
Can you tell me about the DNA in which it found these patterns?
PERRY: One of the other things that Claude noticed was that these array of associated reverse transcriptases seem to be isolated to jumbo phages, which have very large genomes for bacteriophage. We have not seen this occur anywhere else, whether that’s other viruses or bacteria or humans. But in biology, the number one rule is to expect the unexpected. These genes have the ability to spread really widely in ways that you don’t expect. That’s another kind of beauty of this field: [it] is that there’s always something new to find, even with something like this. It’s completely possible that there are relatives or similar systems elsewhere.
Finding reverse transcriptases is something that’s been possible long before Claude. Is AI necessary to do this work, especially given how energy intensive large language models (LLMs) can be?
PERRY: The best thing that I can say about this is that the number of tokens and the compute time to do this analysis are actually fairly little. It’s actually affordable to the types of labs that are interested in doing this type of research. And as a comparison point, the time it would take for a human scientist to do the equivalent analysis that Claude did is on the weeks-to-months scale, and Claude was able to produce this analysis in a day.
The hardest part about doing biology is designing and performing all of the experiments that you need to actually prove what a biological system does, and so shrinking this up-front time of just finding something interesting to work on has really tremendous value for scientific efficiency. Even if there was a compute cost up front, you’re saving lots of human labor costs and effort.
Why use an LLM versus other kinds of machine learning?
KAUDERER-ABRAMS: There’s a distinction between general reasoning models, like LLMs, and the specialized AI biofoundation models like protein language models and protein structure prediction. We see these as today playing mostly complementary roles, in that you have the specialized tools that have been trained to do one thing, and you can’t interface them with them in natural language, but they’re very good at that one thing. The general reasoning models play a different role in that they can actually do all of the steps of the research process, including deciding which specialized tool models to call and in what context to use them.
Now that it’s been identified, where does the research go next?
KAUDERER-ABRAMS: There are two parts to this. The first is the research associated with this particular enzyme system, and the second is the research program that we’re running, generally, that extends far beyond this one enzyme system.
The first point, that’s exactly why we were excited to release this work so early.... [We want to open it up to the community and see what everyone can do with it. We’re excited for whoever is interested in participating to figure out what its function is, and I’ll stress that’s the important part. Finding these things is not quite a dime a dozen because [it’s] not every day that you find something with this set of properties. But the really impactful part is understanding the function and developing it into a tool. We’ll certainly be participating in that as well.
Then, separately, there are all sorts of other research projects that we’re starting. This is one shape of [a] research project of systematizing and scaling up searching for useful new tools in large databases and DNA sequences. But there are other kind of adjacent research projects that we’re just getting started, that all use the theme of seeing “How can we infuse AI into every step of the research process and use that to scale it up?”
As you mentioned, it’s one thing to identify interesting parts of DNA, but it’s another to turn that into something useful. How would Claude help close that gap?
KAUDERER-ABRAMS: We see Claude accelerating the process of turning a naturally occurring discovery into a tool by accelerating all of the cycle times of what’s happening in a research process.
When you look at Claude helping to draft the experimental protocols and analyze the data and debug things when you’re working in the lab, I think that that’s been one of the striking things. I think it’s obvious to people that AI is useful in computational work. What’s less obvious to people is that if you come to our lab, you’ll see Nick and our scientists that are at the bench, literally walking around with their computers, talking to Claude as they’re running the protocols.
How are you safeguarding against hallucinations?
KAUDERER-ABRAMS: That’s absolutely an important concern. And as a whole company, we’ve been putting a tremendous amount of technical effort into reducing hallucinations. As a whole field, we’ve made a lot of progress over the past few years. Beyond that, we have rigorous evaluations that we run that measure the reproducibility and Claude's capabilities in all these different areas.
But there’s no substitute, at the end of the day, for the human biologist. You have to use your judgment, and the model will sometimes say things that are incorrect, and that is part of what it means to be skilled at using AI is to recognize that that's the case and incorporate that awareness into how you work.
What applications do you think these sequences might have in the future?
KAUDERER-ABRAMS: It's really too early for us to speculate about the applications. I think I can say it is fairly uncommon to find this set of properties all together where you have some sort of base enzyme that already interacts with nucleic acids and you have a repeat array that is found up front with a certain structure that, in some ways, is reminiscent of the arrays that you find with CRISPR, and then you have an accessory protein. There’s certainly many of these systems that have been found in nature, but a good number of them have gone on to be developed into useful tools.
