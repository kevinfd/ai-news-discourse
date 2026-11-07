---
id: "2769f47996b69e00"
title: "Implementing GPT-2 in CSS"
url: "https://shubhampatil.dev/blog/gpt2-css"
link: "https://shubhampatil.dev/blog/gpt2-css"
source: "shubhampatil.dev"
domain: "shubhampatil.dev"
source_type: "community"
collector: "hackernews"
date: "2026-11-07T01:01:10Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["zapt02"]
language: "en"
summary: "Implementing GPT-2 Entirely In CSS\nA journey through the Wild West of web trickery.\nTL;DR: I got GPT-2 running a webpage, using only CSS (and interestingly, a bunch of variable font files).\nThe model contains ~124M parameters and inferences at around 15 s/tok (on a good day). You can try it out here!\nWhy?\nThis adventure started as usual, when I saw a tweet on my timeline:\nCMake is an…"
tags: []
orgs: ["OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 9842
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50400576"
score: 17
comments: 2
community: "Hacker News"
---

# Implementing GPT-2 in CSS

shubhampatil.dev · zapt02 · 2026-11-07

Implementing GPT-2 Entirely In CSS
A journey through the Wild West of web trickery.
TL;DR: I got GPT-2 running a webpage, using only CSS (and interestingly, a bunch of variable font files).
The model contains ~124M parameters and inferences at around 15 s/tok (on a good day). You can try it out here!
Why?
This adventure started as usual, when I saw a tweet on my timeline:
CMake is an almost-programming-language. Taking this category and stretching it to the farthest end: what's the most absurd "programming" language? CSS.
The only real constraint I imposed on myself here was that I couldn't use any JavaScript/WASM for inference, or any other language for that matter (I did use Python to write our stylesheets ahead of time, which isn't cheating since none of it runs when you open the page).
Below is a rough overview of how we're able to take what you type and calculate the words that come after it, without a turing-complete language in sight:
Getting to this point took hundreds of experiments, and hours of trial-and-error, but I'd like to walk you through how we produce a singular token, with the various tricks involved with CSS math and variable fonts for matrix multiplication.
Math in CSS
The first question I had was, can CSS even perform the arithmetic (and non-linearities) needed for a neural network, much less a transformer?
Turns out that modern CSS gets quite close to turing-completeness, and has some really interesting bells and whistles. I was already roughly familiar with calc(), which lets us add, subtract, multiply and divide numbers in our stylesheet, and CSS also lets us define variables and reference them like so:
:root   { --a: 0.5; --b: 2; }
.neuron { --out: calc(var(--a) * var(--b)); }   /* 1 */
That calc() is already a multiplication that the browser works out for us, which means that we could, at least in theory, write down any weighted sum in a neural network as one long calc() expression.
To test this, I built a tiny transformer with 7 characters in its vocabulary and random weights, since all I cared about at this point was whether it could spit out a token at all.
CSS doesn't have any primitives for arrays, so I had to write each weight straight into our stylesheet (ok, I had a Python script write them). A single number in a query vector looked something like this:
--generation-0-q-2-0: calc(
    0 /* bias */
  + (var(--generation-0-ln1-2-value-0)) * -0.01020212
  + (var(--generation-0-ln1-2-value-1)) * -0.03555801
  /* … through value-11 */
);
The rest of this tiny model was fairly trivial. For LayerNorm we can find the mean with calc() and let pow() and sqrt() cover the rest, and for the softmax in attention we can subtract the largest score with max() before raising each one with exp().
After I implemented our softmax, though, the page showed all 7 characters after each step, as if our model hadn't predicted a particular next token at all.
When I went through our variables one by one, I found that only the first 265 of the 4,509 in our stylesheet ever got a value. Huh, odd.
Variables in CSS
Intuitively, you'd think that our variables are storing values in memory and retrieving them when necessary. WRONG!
When you write var(--variable-name), the browser's style engine is actually copying over whatever expression that variable corresponds to, and if that expression has variables nested inside it, it recursively unrolls those as well:
Never once is a number registered in this process, isn't that peculiar? After a while, you get a huge chain of operations, just far too much for our page to handle.
Thankfully, CSS has a way around this, which is registering each variable with the @property at-rule. Once a variable has a declared type, the browser works it out once and keeps the actual number:
@property --variable-name {
  syntax: "<number>";
  inherits: true;
  initial-value: 0;
}
:root {
  --variable-name: calc(2 * 3);   /* stored as the number 6, not the text "calc(2 * 3)" */
}
Once I registered every variable this way, our expressions were finally being calculated properly.
When I opened the page again, it showed exactly one character at each step. My prompt " ab" gave me "cde", which was same thing my Python script predicted.
Six gigabytes of CSS
To put this in context, I had intended to scale from this dummy transformer, which only had 1,435 parameters, to GPT-2 small, which has around 124 million parameters.
Currently, each multiply-and-add has each term written out explicitly in our stylesheet, and estimating that each one lies between 25 bytes and 50 bytes, I predicted that our stylesheet would sit anywhere between 3 and 6 GB. And, all of that was only to generate a single token.
Yeah, that's not loading on a webpage. You can start to see how this current approach wasn't going to work at scale.
It was around here that the project inevitably drifted for some time. I had attempted various compression techniques but they didn't seem significant enough, and RAM usage crashed the browser entirely.
At one point or another in this period, I ended up reading a really cool deep dive into how fonts work (i.e. the OpenType specification), and one specific paragraph on variable fonts stuck out to me:
This sounded oddly like a dot-product? Similar to what we were doing in our stylesheet by hand. Was it possible that the browser's font rendering engine could carry out our matrix multiplications for us?
A bit on variable fonts
You've probably played around with font weight before (bold, light, etc.). In the past, type designers had to meticulously sculpt every single weight in a sequence (light, medium, bold, ultrabold), and if you wanted something in between, you were at the mercy of the type designer.
Someone then had an incredible idea: what if we drew the extremes (light and bold), and defined how each glyph smoothly moves between them?
Imagine a dial, where if you turned it to the left, the font got lighter. And if you turned it to the right, the font got bolder. This dial we're turning is formally called an axis, which we can set from CSS like so:
font-variation-settings: "wght" 700;
A font is really just a bunch of tables that tell the browser how to draw its glyphs. One of them, hmtx, stores each glyph's advance width, which is how far the browser moves to the right after drawing it.
Variable fonts add another table called HVAR, where we can say how much that width changes for each unit we turn an axis (these amounts are called deltas). When drawing our glyph, the browser multiplies each delta by its axis value, sums them all up, and tacks on the default width from hmtx:
Look at that second part again. That's a dot product!
Suppose glyph A starts out 580 units wide, and its width grows by 60 for each unit of an axis we'll call X1, shrinks by 80 for each unit of X2, and grows by 40 for each unit of X3. If we set our three axes to 0.5, 1 and 0.3, the browser works out:
Now say we add a second glyph B, which starts out 600 units wide and has its own deltas of 40, -25 and 70 for the same three axes, which comes out to \(600 + 20 - 25 + 21 = 616\).
If we stack the deltas of both glyphs on top of each other, they start to look like a matrix, with one row per glyph, and our axis settings represent the vector we're multiplying it by:
Below are those two glyphs, with each number shown in the font table that it's stored in, hmtx or HVAR:
It becomes quite clear how this is analogous to the thousands of matrix multiplications done in an actual transformer. Our input vector can be thought of as the font's axis settings, and each row in our weight matrix is just the deltas on one glyph, which the browser's text shaper (HarfBuzz, in Chromium's case) multiplies out for us whenever it lays out text on the page. Each resulting glyph's width then comes out as its row's dot product with our input vector.
This might just work.
Testing it out
To test this out, I put a random 64x64 matrix into a font with 64 axes and 64 glyphs. It compiled to just around 8.9 KB (around 2 bytes for each number, rather than 25-50), and when I compared the glyph widths against Python, the maximum error was only 0.24 font units! I was quite ecstatic to have finally found an avenue after banging my head on the wall for a while.
I got started, and took the weight matrices from GPT-2 and started putting them into a bunch of fonts.
Let's take the first matrix in each of GPT-2's blocks, which turns the 768-dimensional vector coming into the block into a query, a key and a value (768 numbers each, so 2,304 in total). As a font, this meant one axis for each of the 768 numbers coming in, and one glyph for each of the 2,304 rows of the matrix.
While the browser totally accepted 2,304 glyphs in one font, shoving 768 axes in one remained far too difficult. Chromium simply stopped loading fonts with more than 256 axes, so I had to split each of GPT-2's 768-wide inputs across 3 fonts.
Each of those 3 fonts got 256 of our inputs as its axes, which meant each of its glyphs could only work out a third of its row (a partial sum).
To add each of the thirds back together, we can just let the browser lay out text like it normally would.
If we put one glyph from each font side by side on a line, with no gaps between them, the line comes out exactly as wide as all three glyphs added together, which is our whole dot product:
We can then pass our 768 numbers in as axis settings, straight from our CSS variables. Our axes only go from -1 to 1, so each number first gets divided by a fixed number a bit bigger than the largest value I saw ahead of time, and we multiply that number back in once we've read the answer. A font just ignores any axis it doesn't have, so all three fonts can share one long list, with each one picking out its own 256:
.qkv {
  font-family: b0qkvS0, b0qkvS1, b0qkvS2;            /* block 0's first matrix, in 3 fonts */
  font-variation-settings:
    "A000" var(--in-0),   …, "A255" var(--in-255),   /* the first font's axes */
    "B000" var(--in-256), …, "B255" var(--in-511),   /* the second font's */
    "C000" var(--in-512), …, "C255" var(--in-767);   /* the third font's */
}
The deltas within our font file also can't contain decimals, so I stored each weight as a whole number, along with a scaling factor for each row that we multiplied back in our stylesheet.
A weight stored with more bit-precision ends up becoming a bigger whole number (therefore a bigger delta). Since each one of our glyphs can only be around 65,535 units wide (and has to start out wide enough such that it never goes negative), more bit-precise weights took up quite a bit more room.
I experimented with 8-bit integers, but quickly realized they yielded me far too much rounding error (about twice as much as 9-bit, across all 12 blocks). Using 10-bit integers got me glyphs as wide as 88,732 font units, way above 65,535, so I stuck with 9-bit integers.
Reading glyph widths back
Each matrix multiplication now left a row of glyphs on our page, where each glyph's width was one number of the output vector. Unfortunately, there wasn't a simple way to read back the width of an element using CSS.
My first attempt to read back glyph widths used a container query. If we mark a box as a container, any element inside it can use a unit called cqi, which is 1% of that box's width (meaning 100cqi is the whole width of the box).
I copied a glyph's width onto one of these boxes with anchor-size(), and a child inside that box could then turn the width into a number, like so:
.box    { container-type: inline-size; width: anchor-size(--glyph-0 width); }
.reader { --w: calc(100cqi / 1px); }   /* the glyph's width, as a number */
Unfortunately, cqi only ever measures the closest container above the reader, and a CSS variable only gets passed down from an element to its children, and not over to the element next to it.
LayerNorm, for example, needs all 768 numbers of a vector on one element to work out their mean. To get them there, box 1 had to hold reader 1, which held box 2, which held reader 2, and so on, with each reader passing down everything read above it.
This meant that each value we wanted on one element added another level of nesting. A single block needed thousands of values read back (2,304 from its first matrix alone), and Chromium stops nesting elements after 512 levels, so this wasn't going to work at all.
I needed some way to read a box's width without nesting anything, and the only thing I knew of in CSS that could write a number into a variable by itself was an animation. If we animate a variable from 0 to 1, it holds how far along the animation is at any given moment.
That progress usually depended on time, but it occurred to me that if I could get an animation to move forward based on how wide something is, I'd be able to read that width directly from an animation's progress.
An immediate one that jumps to mind is scroll-driven animations. You've probably seen these animations, usually a bar at the top of a page that grows as you scroll down.
The interesting one for us is a view timeline, where an animation's progress depends on how far an element has travelled through the visible window of a scroll box, from 0 when it's just about to come in on the right to 1 once it has fully left on the left.
Say our scroll box is \(V\) wide and our glyph is \(w\) wide. The entire trip of that glyph, from just off the right edge to fully gone on the left, is \(V + w\) long, and if we place our glyph with its left edge touching the left side of the scroll box, the browser treats it as having already come \(V\) of that trip:
Say our scroll box is 300 px wide and our glyph is 100 px wide. The glyph has moved 300 px of a 400 px trip, so the browser reports a progress of 0.75, and \(300 / 0.75 - 300\) hands us our 100 px back. Below, a wider glyph gives a smaller progress:
Since we can predetermine the width of our scroll box \(V\), all we need is the progress \(p\) as a number. If we run an animation whose keyframes go from --p: 0 to --p: 1 and tie it to our glyph's timeline, --p ends up equal to the progress, and a property called timeline-scope lets an element anywhere under a shared parent read that timeline, without being nested inside the scroll box at all:
@property --p { syntax: "<number>"; inherits: true; initial-value: 0; }
@keyframes read { from { --p: 0 } to { --p: 1 } }
.glyph  { view-timeline: --t0 inline; }       /* sits in a 65536px-wide scroll box */
.parent { timeline-scope: --t0; }             /* shares --t0 with the reader */
.reader {
  animation: read 1s linear both;
  animation-timeline: --t0;
  --w: calc(65536 / var(--p) - 65536);        /* the glyph's width, in px */
}
"Would it actually perform at scale?" was my primary question right now. I had been in this position far too many times to feel hopeful.
It did, mostly. In my experience, the time taken to read back values increased quadratically with the number of animation timelines on a singular element, so I had to split our 768 width reads across 3 separate elements (my best guess here is that Chromium checks every running animation against the others on the same element).
A font as a tokenizer
Now came the grand (yet inevitable) question: how do you let people type in a prompt?
The primary way to get values out of an <input type="text"> is through JavaScript, which was out of the question. There's also contenteditable, which lets the viewer of a webpage edit an element's content, and I knew that we could write a <style> tag directly in our HTML. That's when it occurred to me: what if we could apply contenteditable on a style element?
<style class="editor" contenteditable="plaintext-only">.prompt-source {
  --draft-prompt: "Once upon a time"; /* edit this */
}</style>
I tried something like this out, and miraculously, it worked! I could type whatever I wanted between those quotes, and the browser read it as part of our stylesheet.
This was also when I hit another roadblock. CSS has no reliable way to split a string up according to a set of rules, and I spent the next few days wondering what else could work with text, until I came back around to fonts.
GPT-2's tokenizer uses BPE, or byte-pair encoding, which is a long list of rules that say "hey, if a B comes after A, classify that as the token AB". Each of these is called a merge, and GPT-2 has around 50,000 of them, each with a rank that decides which ones happen first.
Fonts have something extremely similar, called ligatures. If you've ever used a fancy font in an IDE, you may be familiar with how typing => gets turned into a single arrow. 
The font table that holds these rules (GSUB) runs them in order, so we can quite literally copy GPT-2's merges into our font, like so:
feature rlig {
  lookup mergeBatch0 {
    sub g220 g83 by g256;   # "Ġ" + "t" → "Ġt", rank 0
  } mergeBatch0;
  …                         # 2,782 lookups in total
} rlig;
A ::before with content: var(--draft-prompt) puts our prompt on the page as text in this font. Once the browser has applied the merges, each token in our prompt is one glyph on the line, and I made each token's glyph exactly as wide as its ID plus one (zero is reserved for "there's no token here").
To read one token at a time, I added a font feature for each position in the prompt that shrinks the other tokens on the line down to zero width, and then a container query reader like the one from earlier turns the one glyph left into an ID (one value on its own only needs one level of nesting, so that's fine here).
I inputted "Once upon a time" on the page and got met with the following token IDs: [7454, 2402, 257, 640], which were the same IDs that GPT-2's tokenizer gave me (our fonts only trip up on things like newlines, double spaces and non-ASCII characters).
Our embedding table, too?
A token ID on its own wasn't useful to the model, since we needed to input the 768-dimensional embedding vector that our ID points to in GPT-2's embedding table (a big table with one row of 768 numbers for each of its 50,257 tokens). CSS has no arrays, so I wondered if we could get a font to do this lookup for us too.
The plan was to make a font with 768 glyphs, one for each dimension in the vector, whose widths would come out as the embedding of whichever token we were on.
However, a delta could only scale along with an axis value, while here we needed all 768 widths to jump to a whole different set of numbers whenever the token changed.
Font Regions
A cool trick I had found while browsing through the OpenType documentation was the concept of a region. We can give a delta a region, which is a small range on one or more axes. Inside that range, the strength applied to a delta rises to 1 at its peak, and fades back to 0 towards either edge. Outside this range, the delta does nothing at all.
So a really tiny region acts like a light switch on our delta (the delta only turns on when an axis lands on one exact value).
A font can hold lots of these regions, and each region gets its own delta on every glyph.
Whenever the browser draws a glyph, it works out each region's strength from our axis settings, multiplies it by that region's delta, and adds all of these onto the glyph's default width.
This meant that I could give each token its own tiny region, and set that region's 768 deltas to the token's embedding (times 4,096, since deltas have to be whole numbers). When we point our axes at one token's region, its strength is 1 and its deltas get added onto our 768 glyph widths, while every other region has a strength of 0 and stays off.
Chromium stores axis values as 14-bit numbers, so we could only fit around \(2^{14} = 16,384\) regions on one axis, nowhere near 50,257. No worries however, since a region can live on two axes at once. The browser works out the region's strength on each axis separately, and then multiplies the two together.
If our first axis lands inside the region (a strength of 1) and our second one lands outside it (a strength of 0), the region's strength comes out as 1 × 0 = 0, and it stays off, only turning on when both axes land inside their respective regions.
I defined two axes, GRUP and LOCL, and split them into 197 and 256 ranges, so that each token ID gets its own pair:
We can then set both axes straight from the token ID like so:
.embedding {
  --token: 5575;                                 /* " Mont" */
  font-variation-settings:
    "GRUP" round(down, var(--token) / 256, 1),   /* 21 */
    "LOCL" mod(var(--token), 256);               /* 199 */
}
Each glyph starts out 20,000 units wide. The first number in the embedding for the token " Mont" is 0.0364, which makes its region's delta on the first glyph 0.0364 × 4,096 = 149. With only that region turned on, the first glyph comes out 20,149 units wide.
Below, each dot is one token's region. Clicking one turns it on, and only that region's deltas get added to the glyph widths:
We can then read our 768 widths back with view timelines, take away the 20,000 and divide by 4,096, and our first transformer block can finally start working.
Attention, and memory
Each block is mostly calc() math and font multiplications, but attention was a bit of a headache. Our fonts could only hold weights that were fixed ahead of time, which was fine for the matrices that made a token's query (Q) and key (K), since those never change.
Attention then scores how much our token should look at each token before it, by multiplying our token's query by each earlier token's key. Neither of those are fixed, since they both depend on the prompt that was typed.
In our fonts, the only numbers we could set from CSS were the axis values, and every delta was frozen when I built the font file. This meant that a glyph's width could be a query times a weight, but not a query times a key (since the key was also a dynamic value).
The easiest way around this, I found, was to use font regions again. Remember how each token's region in our embedding font sat on two axes, and the browser multiplied the strengths on both? In the embedding font, each of those strengths was always either 0 or 1, but the strength on an axis can be anything in between.
Say we make one region across two axes called Q000 and K000, where the strength on each axis rises from 0 at an axis value of 0 up to 1 at an axis value of 1. If we set Q000 to 0.5 and K000 to 0.4, the strengths on the two axes are just 0.5 and 0.4, which makes the region's strength 0.5 × 0.4 = 0.2. From there, the browser multiplies that by a fixed delta (we used 468) and adds it onto our glyph width:
GPT-2 splits its attention into 12 heads, and each head compares 64 of the numbers in a query against the same 64 in each key, which makes one attention score \(q_1 k_1 + q_2 k_2 + \dots + q_{64} k_{64}\).
We can define a region like this for each of those 64 pairs (Q000 with K000, Q001 with K001, and so on), all on the same glyph. The browser then adds each region's product, times its delta of 468, onto that one glyph's advance width, and in total our glyph grows by 468 times \(q_1 k_1 + q_2 k_2 + \dots + q_{64} k_{64}\), which gives us an attention score.
A product can also come out negative (each pair actually gets one region for each mix of signs, with a delta of +468 or -468), which is why our glyph starts out 29,984 units wide (64 × 468 and a little extra), such that even if all 64 products came out at -1, its width wouldn't drop below zero:
Below are 4 of 64 dimensions with their Q and K axes:
We can then read each score back with a view timeline, like every other width on our page.
Now, we still needed the \(K\) and \(V\) pairs from previous tokens to be sitting somewhere on the page. Suppose we're on the 4th token of our text. Token 3's key was worked out back when we were on token 3, from token 3's own input, so why couldn't it just stay on the page?
The thing is, our page only has one set of elements for working a token through the model, and each token reuses them when its turn comes (there would be far too many elements otherwise).
A rule like --k: calc(var(--x) * 2) on those elements gets worked out again whenever --x changes, and CSS doesn't keep the old calculated result anywhere. This meant that once we move on to token 4 and --x held token 4's input, the key gets calculated again from that new value, and token 3's key is simply gone.
You might think we could just have a variable keep its own old value, by defining it in terms of itself:
.cache {
  --k-3: var(--k-3);   /* "keep whatever --k-3 was" */
}
But to work out --k-3, the browser first needs --k-3. It treats this as a cycle and throws --k-3 out entirely.
So, I was left wondering, how could I give our stylesheet some form of storage?
Transitions?
I started messing with transitions (an example of this you've seen is when a button fades its color over 200ms instead of directly changing to its new one). With a transition-delay, a button's old color can simply sit there until its delay is up, even though a rule asking the browser to render a new color is already registered.
Now, what happens when that delay is really, really long?
I tried a delay of 86,400 seconds (24 hours), and since nobody is going to leave the page open for a full day, the old value could just stick around there for good. I could finally store a number!
Our cache keeps one spot for each position in our text, where spot 1 holds the key and value of the first token, spot 2 holds the second, and so on. Each spot is just its own pair of variables (--k-3 and --v-3 for spot 3).
Each of these variables holds a whole key or value vector, written as a string of axis settings like "K000" 0.4, "K001" -0.1, … (we'll see why in a bit). We can then register them as properties and then list all of them in transition-property with our day-long delay, such that each spot can hold on to whatever value it had:
@property --k-1 { syntax: "*"; inherits: false; initial-value: "K000" 0; }
.kv-cache {
  transition-property: --k-1, --v-1, --k-2, --v-2, …;   /* all cached keys and values */
  transition-duration: 1ms;
  transition-delay: 86400s;
  transition-timing-function: steps(1, end);
  transition-behavior: allow-discrete;   /* swap the value, don't blend it */
}
To illustrate this clearer, here's a slider that sets the same number on two properties. Here, only --held has a day-long transition delay on it:
Writing into a spot works the other way around, where we take it off that list. Say we're working on the token in position 3. We can write a rule that only applies while we're on position 3 (the --position: 3 in the container parameters), where we list every spot in transition-property except spot 3, and set spot 3's variables to the key and value we just calculated. Since spot 3 doesn't have a transition on it anymore, it changes right away:
@container style(--position: 3) {
  .kv-cache {
    transition-property: --k-1, --v-1, --k-2, --v-2, --k-4, --v-4, …;   /* every spot but 3 */
    --k-3: var(--k-now);
    --v-3: var(--v-now);
  }
}
Once we move on to position 4, this container-rule stops applying and spot 3 goes back onto our list. From then on, any change to spot 3's value becomes a transition that waits a whole day before doing anything. This way, spot 3 keeps token 3's key and value, while the rule for position 4 writes token 4's into spot 4.
Dealing with KV caches
This is why we stored each key as a string of axis settings. When a new token comes along, we can put its query and a stored key side by side in one font-variation-settings, and let our dot-product font from earlier score them:
.score-3 { font-variation-settings: var(--k-3), var(--q-now); }   /* "K000" 0.4, …, "Q000" 0.5, … */
Our cached values remain as strings of axis settings however, and our stylesheet can't multiply strings together.
That became a problem at the last step of attention. After the softmax, each past token \(j\) has an attention weight \(p_j\), a number from 0 to 1 for how much our token looks at it, and a value vector \(\mathbf{v}_j\) sitting in its cache spot. Attention's output is each value vector multiplied by its token's attention weight, summed:
To multiply them, I used one more font. Each attention head is assigned a font with 64 glyphs, one for each number in a value vector. If we put a cached value vector on its axes, each glyph's width represents one of its numbers.
Each glyph starts out at a base width of 12,320.768 px (wide enough that it can't turn negative), and then adds 12,288 px times the value it holds. A value of 0 leaves it at its base width, a value of 1 adds 12,288 px, and a value of -1 takes 12,288 px away.
To scale that glyph by \(p_j\), its token's attention weight, we can use calc-size(), a CSS function that lets us set a box's width with a formula, where size stands for the width that box would naturally have (in our case, the glyph's width):
/* head 0, spot 3: one value glyph, drawn at 1024px */
.fvs-v-0-3 {
  font-family: FvsValue0;
  font-variation-settings: var(--fr-v-3-0);   /* the value vector in spot 3 */
  width: calc-size(max-content,
         calc(12320.768px + (size - 12320.768px) * var(--fw-0-3)));
  flex: none;
}
Here, size - 12320.768px is just the part our value added on top of the base width. We multiply only that part by token 3's attention weight --fw-0-3, and then add the base width back.
Now we need to add these scaled glyphs all up, since attention's output is the sum of each past token's value vector \(\mathbf{v}_j\) multiplied by its attention weight \(p_j\). To do that, we can use the browser's layout again, just like with our three fonts from earlier. If we line up one of these glyphs for each past token in a single row with no gaps, the row is as wide as all of them added together.
That width also includes one base width for each glyph, but since we know how many glyphs are in the row, we can take those bases away afterwards and divide by 12,288 to get our sum back.
Each of the 64 numbers in a value vector gets its own row, so let's follow just the first one. Say we have three past tokens whose first numbers are 1, 0 and -1, with attention weights of 1.000, 0.407 and 0.183 (we hold off on dividing them by their total of 1.590, the last step of the softmax, until the very end). Our row then comes out as:
Here is an example of that row, with one glyph for each past token in our sequence:
Inventing order, again
GPT-2 has 12 transformer blocks that have to run one after the other, and my first thought was to ignore the sequential ordering entirely. I wrote all 12 blocks out as one big connected set of variables, with each block reading straight from the one above it, and let the browser figure out the rest.
Our page finished in around 8.4 seconds, which looked great until I compared the 768 numbers coming out of the last block against a regular run of GPT-2 on my GPU. They were off by 10.36 on average (as a root-mean-square error). Not great.
When I instead ran each block on its own page, with a Python script carrying our 768 numbers from one page to the next, that error dropped to somewhere between 0.045 and 0.074, and we got the correct next token back (a comma)!
Why?
Each block reads its inputs back from the block above it with view timelines, and there was one thing about view timelines that I hadn't really thought about.
The browser draws our page in frames (many times a second), and in each frame it works out styles first, then layout (where everything goes and how wide it is), and then paints it.
A view timeline's progress depends on where things ended up in layout, so the browser can only work it out once layout is done, which means our CSS only gets to see a new width on the next frame.
This meant that when block 1's widths changed, block 2 spent at least a frame calculating its values with whatever block 1 had shown it the frame before, and block 3 then built on top of that:
Given enough frames, every block did end up with the right numbers, like in the last row above. However, nothing on the page told a block to wait for the one above it to settle, so whatever read the last block's output had no way of knowing when it was finally right, and could grab numbers that were built on old inputs. I needed a way to control this order myself.
On a much smaller model, I had already ordered things by nesting each step inside the one before it (a child's styles are only worked out after its parent's), and hiding the next step with content-visibility: hidden until the one above it had finished.
Setting content-visibility: hidden on an element told the browser to skip everything inside it, so nothing in there gets styled or laid out, and it couldn't calculate anything with half-finished inputs. A container query could then switch it back on once the step above it set --done to 1:
.step-2 { content-visibility: hidden; }
@container step-1 style(--done: 1) {
  .step-2 { content-visibility: visible; }   /* step 1 is done, so step 2 can run */
}
At GPT-2's size, however, just the 12 blocks stacked inside each other came out to 182,269 elements, only for a single token, which probably wasn't going to load at all.
Luckily, the elements on our page weren't holding any weights themselves.
Our weight matrices all sat in font files, and the few numbers that weren't in a font (like the numbers each block's LayerNorm scales and shifts its output by) were typed straight into the calc() expressions in our stylesheet. This meant that if we could change which fonts and constants a box was pointing at, the very same box could act as block 0, then block 1, and so on.
CSS already has a way to switch a whole group of rules on and off based on a variable, called a container style query. If we write @container style(--layer: 3), the rules inside it only apply when some parent element has --layer set to 3, so we can write one set of rules for each of our blocks, like so:
@container corestate style(--layer: 3) {
  .shared-qkv { font-family: b3qkvS0, b3qkvS1, b3qkvS2; }   /* block 3's weight fonts */
  .shared-fc  { font-family: b3fcS0, b3fcS1, b3fcS2; }
  /* … block 3's LayerNorm constants … */
}
From here on, I'll call each run of our shared boxes through one block a pass. One token goes through 12 "passes" (one for each block), and a variable called --pass counts them as we go. It keeps counting across tokens, so the block number is --layer: mod(var(--pass) - 1, 12), where pass 1 is block 0 and pass 13 is block 0 again for the next token.
Moving from one pass to the next on the same boxes turned out to be tricky. The obvious way to do it looks something like this:
/* once pass 4's output is on the page, start pass 5 */
@container style(--output-pass: 4) {
  .controller { --pass: 5; }
}
Say pass 4 has just finished. Here's what happens next:
1. Pass 4's output is on the page, so our rule matches and sets --pass to 5.
2. Pass 5 runs on the very same elements, so it overwrites pass 4's output with its own half-finished numbers.
3. CSS works out each value again from whatever is currently on the page, so our rule sees that pass 4's output isn't there anymore, stops matching with its container-rule, and --pass changes back to 4.
4. Pass 4 runs again, its output lands on the page, and we're back at step 1.
I needed a value that changed once and then stayed frozen, regardless of what our CSS did after, and I couldn't find anything in CSS (I looked for a while) that behaved like that.
I bumbled around outside of CSS for a bit (I'm not a CSS-purist by any means, sue me) and ended up taking a look at SVGs.
Turns out that SVGs have their own (much older) animation system called SMIL, which we can use inside our HTML. One of its elements, <set>, changes an attribute when some other element finishes an animation, and if we add fill="freeze", our attribute's changed value remains the same for as long as the page is open.
Whenever a step is done, our stylesheet runs a tiny 1ms animation on an empty SVG element, and SMIL listens for it to end like so:
/* the head has picked a winner for token 3 */
@keyframes native-handshake { from { opacity: .99 } to { opacity: 1 } }
body:has(#run:checked) #token-3-ready { animation: native-handshake 1ms both; }<g id="token-3-ready"></g>
<g id="token-3-captured">
  <set attributeName="class" to="done"
       begin="token-3-ready.animationend+0.001s" fill="freeze"/>
</g>
The opacity change itself doesn't matter here, as we only care that the animation ends.
SMIL then gives #token-3-captured the class done, which no CSS rule of ours can change. Then, a body:has(#token-3-captured.done) rule can let the next step begin (reloading a page is the only way to clear a frozen <set>, so each step gets a new pair of <set> elements).
Another thing that could potentially go wrong was that since each pass runs on the same boxes, a step could read a number left over from an earlier pass and happily compute with it.
Fortunately, we could get around this by painting another width on the page. Alongside its outputs, each step draws an extra box whose width represents the pass number it's working on (16,384 px, plus 1,024 px for each pass):
<i class="pass-reader" style="width: calc(16384px + var(--pass) * 1024px)"></i>
Suppose we're on pass 5, and our attention step needs the query, key and value that the step before it calculated. Along with those, it reads back that step's pass-number box. Since the box and the outputs beside it get laid out together, a box that indicates a pass number of 5 means the outputs next to it are from pass 5 too.
If the box still says 4, the outputs contains values left over from pass 4, and the attention step stays hidden with content-visibility: hidden until the box catches up:
Argmaxxing
After the twelfth block, one more font multiplication scores our vector against all 50,257 words in the vocabulary, and each word ends up as a box whose width is its score.
If we read each score back, we'd need 50,257 view timelines running at once, which would be quite resource-heavy. All I really needed was for the browser to find the biggest score for me.
It turns out that browsers already have a way to make a box as wide as the widest child inside it, called width: max-content. Unfortunately, it only tells us what the biggest score is, instead of which word that score belonged to.
At this point, each scored word is sitting on the page, with its score equal to its width on the page. First, we can split those boxes into 197 groups of 256 words, and give each group's box width: max-content. This rule makes each group grow to fit its best (aka widest) score.
We can then copy those 197 resulting widths into more max-content boxes with anchor-size(), 16 at a time, and do it again on those, until a single box at the end is as wide as the best score on the whole page.
Next, we can check each box against that best score. Each box takes its own score, subtracts the winning score, adds 1 px, and clamps the result between 0 and 1 px:
If the box is the winner, \(s - s_{\max}\) is 0 and we get exactly 1 px. If it isn't, it's at least 4 px behind (before comparing anything, I rounded each score to a multiple of 4 px), so we get -3 px or less, which the clamp turns into 0.
We do this twice. First, each of the 197 groups checks its best score against the winner and multiplies its 0-or-1 by \((197 - \text{group}) \times 4\) px, which counts down so that even group 0 has some width. Only the winning group's box has any width now, so one more max-content box is exactly as wide as it, and a reader works out the group number as \(197 - \text{width} / 4\) and stores it in --head-group-index.
Then we draw 256 fresh boxes, one for each of the words in that winning group. This time, each word does the same check with its own score, which gives each word its own 0-or-1, with only the winning word getting a 1.
Each box then multiplies its 0-or-1 by a width that depends on its place, which is just its position in the group (from 0 to 255). Like with the groups, if that width were the place itself, a winner at place 0 would come out 0 px wide, exactly like all of the losers.
Instead, each word uses \(256 - \text{place}\), so the first word in a group gets 256 px and the last one gets 1 px, which means any possible winner has some width.
Counting down helps with ties too. If two words tie for the best score, both of their boxes get some width, and max-content picks the wider one, which is the earlier word, the same one a normal argmax would pick.
We put those 256 boxes in one more max-content box, which makes it exactly as wide as the winner's box, \(256 - \text{place}\), and measure it with a container query. Taking that width away from 256 then gives us the winner's place back:
.head-result { --winner: calc(var(--head-group-index) * 256 + 256 - round(nearest, 100cqi / 1px, 1)); }
Let's say the token " Mont" wins. It sits in group 21 at place 199, so its box is the only one in that group with any width, at \(256 - 199 = 57\) px. Our rule measures those 57 px, and works out \(21 \times 256 + 256 - 57 = 5575\), which is the same ID we fed into our embedding font earlier.
This is an illustrated example with 8 words instead of 256:
To display the word, we can use a counter style (this is what decides whether a list is numbered "1, 2, 3" or "i, ii, iii") with each word in the vocabulary as a symbol:
@counter-style gpt2-vocabulary {
  system: fixed -1;                      /* the first symbol is number −1 */
  symbols: "" "!" "\"" "#" … " Once" …;   /* "" at −1, then words 0 … 50,256 */
}
.visible-output::after {
  counter-reset: token1 var(--display-token-1);   /* e.g. 7454 */
  content: counter(token1, gpt2-vocabulary);      /* prints "Once" */
}
The winning ID also has to become the next token's input, which means it has to make its way back to the embedding font at the start of our model.
Since a CSS variable only gets passed down from an element to its children, and our output head is nested deep inside the model, the head can't supply its ID straight to the embedding font. Instead, we can represent the token ID as a width again.
The page draws a box that starts out 65,536 px wide and gets 8 px wider for each ID, inside a hidden scroll box that's 524,288 px wide. A reader on the outermost element of our model, which every other part (the embedding font included) is nested inside, then can decode that box's width with our view-timeline method from earlier and passes the ID down from there.
Hello?
Once the reused block and the output head were in place, I gave it the prompt "Hello", clicked Run, and waited.
After about five and a half minutes, it printed "Hello, I'm sorry, but I'm", at around 40.7 seconds for each token.
All 8 tokens matched what the original GPT-2 picks in full floating-point precision! I then pushed it to 32 tokens, and got this back:
"Hello, I'm sorry, but I'm not sure if you're aware of this. I'm not sure if you're aware of this. I'm not sure"
It was quite slow, but for the first time I had GPT-2 small in all its 124M parameter glory, directly running on our webpage!
Where does a token go?
Now that I had a page that could generate text, I spent a good while making its individual pieces run faster on their own, but a full run of the model barely got any faster. To see where each token's time actually went, I recorded a log of the browser generating 8 tokens.
Since our fonts multiply numbers while the browser is shaping text (i.e. working out which glyphs to draw and how wide each one is), all of our matrix math landed under text shaping, which only took up 5% of a token's time to process.
More than half of each token (55.6%) went to style recalculation. Whenever something about an element changes, the browser has to work out that element's styles again.
While our weights all lived in fonts, everything around them was a bunch of CSS variables (LayerNorm, softmax, adding each block's output back on, and turning every width we read back into a number). Style recalculation is when the browser actually goes through all of those calc() expressions.
The rest of the time went into drawing frames, and our page needed a lot of them for each token.
Since our view timelines only moved forward once a frame, and each block had several sets of widths to read back one after another (its query, key and value, then its attention scores, and so on), each block took 4 frames to process. Changing --pass, through our SVG trick from earlier, cost another three frames on top of that. That got us to 7 frames for each of our 12 blocks, and one more for picking the word at the end, which added up to 85 frames being rendered for a single token.
This gave me two things to cut: the 85 frames, and the style recalculations on elements that didn't require them.
One of these was the set of variables that kept track of which pass we were on (like --pass) and whether it was done. These sat near the top of our model, with around 20,000 elements nested underneath them.
A variable registered with inherits: true gets passed down to every element under the one that sets it. Each time one of these changed, the browser redid the styles of all 20,000 or so elements, even though only a handful of them actually read it.
If we registered them with inherits: false instead, we could set them directly on just the few elements that read them, and only those got their styles redone. This brought us from 40.2 s a token (what a fresh rebuild of the page came in at) down to 32.8.
Remember our SVG trick from earlier? We were using it at the end of every pass just to bump --pass up by one, which made us wait about three frames each time.
Then, I realized that the last step of each pass already drew a little box with its pass number in it, right next to the numbers it saved. If that box said 4, pass 4 is done, and we didn't actually need the SVG to tell us that.
So I put one more element above the one that holds --pass, which reads that box with a view timeline and sets --pass to whatever it reads plus 1. With the SVG gone, we went from 85 frames spent on a token down to around 47.
Our attention scores didn't need to rely on frames at all. CSS has a unit, ch, which is the width of the "0" glyph in the current font. If we made our dot-product glyph the font's "0", then 1ch represents our attention score, and we could use it right away without a view timeline.
That, along with a handful of smaller fixes, brought our best runs to 15.3 s a token on our 8-token benchmark, down from 40.7 when it first worked. Not bad!
Scrollbars suck
By this point I could type a prompt into the page, tick a box and watch GPT-2 continue it one word at a time. I typed "Shubham was" into the box, and our page slowly printed out "...a member of the U.S. House ofEARTH".
EARTH?
When I ran the same prompt through my Python script, it gave me "House of Representatives", and since the first 13 tokens from our page matched it, something had gone wrong at the 14th token.
It turns out, the cause of this was a scrollbar on the page!
At some point, I'd set "Show scroll bars" to "Always" in my Mac's System Settings, which draws a classic 15 px scrollbar inside any element with overflow: scroll. That included the hidden 524,288 px scroll box we use to send the winning ID back to the embedding font, where the reader on our model's outermost element decodes the width of the ID's box.
This meant that our scroll box was really only 524,273 px wide, while our calc() was dividing by 524,288, so each width we decoded came out a tiny bit too large:
This predicted error grows along with our width, which is already growing with the ID we have.
To convert a width back into a token ID, our reader subtracts 65,536 px and divides by 8. A width that's slightly off gives us something like 17,132.3 instead of a whole number, which our reader just rounds to the nearest ID.
Since IDs sit 8 px apart, a width that's off by less than 4 px (halfway to the next ID) still rounds down to its correct one. Once our error surpasses 4 px, it rounds up to the next ID instead. With our 15 px scrollbar, this becomes the case for every ID from 9283 onward.
The box for " Representatives" (ID 17132) came out to about 202,600 px wide, so it was well past that point:
ID 17133 happens to be "EAR", and our model, quite reasonably, took "EAR" as its input and continued it with "TH". House of EARTH!
None of my tests had caught this, since they either ran the browser without a window or hid scrollbars, and the largest ID in my "Hello" test (7926) was only off by 3.7 px, just under the line.
Thankfully, fixing this only took a single line:
.feedback-scroller { scrollbar-width: none; }
Sampling without random()
Always picking the most likely next-token got repetitive quite quickly, as we saw earlier with a prompt of "Hello".
I wanted to implement proper sampling, where each word gets picked with the probability that our softmax assigned it.
The obvious tool here would be the new CSS random() function, which the browser happily parses and then returns 0 for, every single time (thanks Chrome).
After looking around for a while, I ended up using something called the Gumbel-max trick. We add a random number (some noise) to each word's score, and then pick the highest one, just like before:
Here \(s_i\) is word \(i\)'s score and \(g_i\) is its noise, while the temperature \(T\) scales that noise, so a higher \(T\) shuffles the words more.
Say four words have scores of 3, 2.5, 2 and 1. On each draw, we give every word its own random number on top of its score, and the biggest total wins.
The word with a score of 3 wins most of these draws, but now and again the word with a score of 2.5 gets a large enough noise value to overtake it. A word with score 1 needs a greater amount of noise to become larger than the other two values, which rarely happens.
Below, each click of "Draw" gives every word a new random number:
If our noise comes from the curve above, a spread of random numbers called the Gumbel distribution, each word ends up on top exactly as often as its softmax probability.
I then realized that our output head was already picking the widest box, so we could just make each word's box wider by its noise!
I generated a table of Gumbel noise ahead of time, with one number for each of the 50,257 words in each of 64 columns, and stored it in one more font with one glyph for each word. We can then give each word's box one extra glyph from this font, which means each box's width is equal to its word's score plus the noise that it's assigned
A SEED axis then picks which column the noise comes from (with one tiny region for each column, like the token regions in our embedding font), and a TEMP axis scales it. With TEMP at 0, our noise glyphs all come out the same width, and we get back the same word we'd have picked without them. Below are four of those boxes, each with its noise glyph:
How do we get a seed without random(), though?
I ended up implementing a clock animation that keeps counting a number up from 0 to 64 and starting over, just under once a second, and clicking "Run" on the page pauses the animation wherever it happens to be:
@keyframes clock { from { --clock: 0 } to { --clock: 64 } }
body {
  animation: clock .97s linear infinite;
  --seed: calc(mod(round(down, var(--clock), 1), 64) + 1);   /* 1 … 64 */
}
body:has(#run:checked) { animation-play-state: paused; }
Whatever number the clock is paused on when you click Run becomes the seed. The first new word reads the noise column right after it, the next word the column after that, and so on.
There was one last thing bugging me, which was that the tab sat completely blank for 34 seconds after loading.
Turns out that while a stylesheet in the <head> is loading, the browser goes ahead and lays out the body using its own default styles.
Our body holds 84,592 <i> elements, filled with characters from far-off corners of Unicode that only our own fonts can draw, and each time the browser came across one, it asked the operating system whether any installed font could draw it. With around 300,000 distinct characters on our page, this layout took up 30.8 seconds!
A <link> placed inside the body stops the browser from reading any more HTML until its stylesheet has loaded, so I just moved it out of the <head> and below our controls, and now the browser wouldn't touch our model until all our styles were loaded in. The page now showed "Ready" after 2.2 seconds, down from 34.
Did it work?
Typing "Shubham was" with greedy decoding matched a normal run of GPT-2 small on all 35 tokens. Sampling matched as well, both for "Hello" and for "Once upon a time" at two different seeds and temperatures, token for token.
Is it fast? No, not even close (as you can probably tell).
A token takes around 15 seconds at the start of a run, and that grows to around 50 seconds by the last one as our context fills up, which put a 4-token prompt plus 32 new tokens at a little over 17 minutes. It's also quite hungry for memory, using around 2 GB once the tab has loaded and up to around 6 GB while it's generating.
But hey, there's no JavaScript anywhere on the page.
Try it
You'll need desktop Chrome or Edge 139 or newer and around 16 GB of RAM, and the first visit downloads around 250 MB, most of which is fonts. The page takes a minute or two to load before it says "Ready", and then you can type up to 4 tokens between the quotes and tick Run.
If your laptop is plugged in, 32 new tokens should take somewhere around 15-20 minutes, and quite a bit longer on battery.
You can try it here: gpt2css.shubhampatil.dev
The source is on GitHub: ShubhamPatilsd/gpt2-in-css
If you have any idea how to make it faster (or questions on why some of this works the way it does), please do contact me.
