---
id: "7b3521fa7aad3318"
title: "Can You Entrust New Year's Card Design to AI? — Comparing ChatGPT and Gemini Using the Exact Same Prompt"
url: "https://note.com/moco_prompt_lab/n/na1003f6da119?hl=en"
link: "https://note.com/moco_prompt_lab/n/na1003f6da119?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-25T03:41:00Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["もこのプロンプト実験室"]
language: "en"
summary: "Both Are Great at Art. The Deciding Factor Was the \"Text\"Welcome to Moko's Prompt Lab; this time, we have a seasonal experiment. Can you rely entirely on image-generating AI to design a business New ..."
tags: []
orgs: ["OpenAI", "Google"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1023
paywalled: false
image: "http://www.bing.com/th?id=ONUT.NwVrXG8LJXaH5fJY0_nckw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Can You Entrust New Year's Card Design to AI? — Comparing ChatGPT and Gemini Using the Exact Same Prompt

note · もこのプロンプト実験室 · 2026-11-25

Can You Entrust New Year's Card Design to AI? — Comparing ChatGPT and Gemini Using the Exact Same Prompt
Introduction — Conclusion: Both Are Great at Art. The Deciding Factor Was the "Text"
Welcome to Moko's Prompt Lab; this time, we have a seasonal experiment. Can you rely entirely on image-generating AI to design a business New Year's card? I submitted the exact same prompt to ChatGPT and Gemini (both on free plans) and compared the results.
To give the conclusion first, the visual quality of both exceeded expectations. Both incorporated the sheep motif, warm colors, and vertical layout. Where they diverged was the text. One got every single specified character right, while the other had a one-character typo in the greeting message that remained even after asking for a correction. When it comes to business New Year's cards, a single wrong character renders them unusable. In that sense, regarding whether they can be "sent straight to print," the verdict is that it still takes an extra step.
Note that the subject used is a fictional renovation company created for this experiment. No real companies or addresses were used.
The Prompt — The Fictional Business "Sumai Kobo"
For the fictional business, I chose a community-rooted renovation company named "Sumai Kobo." For the address, I masked it as "1-2-3 ○○-cho, Tama-shi, Tokyo" to see whether the AI would arbitrarily replace it with a realistic-looking address. The phone number was 042-000-0000, clearly identifiable as fictional.
The prompt pasted into each AI was completely identical.
What I compared was text accuracy (Kingashinnen / company name / greeting message / address and phone number), the sheep motif and atmosphere, vertical orientation and margins, as well as responsiveness to revision requests and print-ready resolution. On top of that, I asked each AI once for the exact same correction ("Please make the sheep slightly larger and make the company name darker").
ChatGPT's Results — Every Single Text Item Was Accurate
ChatGPT's first piece had a classic composition: a white sheep in the center, Mount Fuji, the first sunrise of the year, plum blossoms, and pine trees. I zoomed in to check the text character by character, and everything—from "謹賀新年", "本年もよろしくお願いいたします", "2027年 元旦", and "すまい工房" down to the address and phone number—was exactly as specified, with zero typos. The address's "○○-cho" was also rendered with the placeholder characters intact.
When asked for a revision, the sheep became noticeably larger, and the company name became bolder and darker. The text did not break down either. However, its method of revision was the "complete redraw" type, altering parts I hadn't asked to change, such as adding extra rays of sunrise light in the background. It is worth knowing that it is not a partial edit of the same image.
The disappointing part was the resolution. The image was 1024×1536 pixels. The standard guideline for printing on a full postcard (100×148 mm) at 300 dpi is 1181×1748 pixels, falling a tier short. While sufficient for viewing on a screen, there is a chance it might turn out slightly soft in print.
Gemini's Results — Resolution Is Sufficient. But There Was a 1-Character Typo in the Greeting
Gemini's first piece featured a creative layout: a large sheep beside a Japanese-style house, complete with small props typical of a renovation company such as a hammer and lumber. It also had a distinct white margin border. The resolution was 1696×2528 pixels, surpassing the 300 dpi guideline for postcard printing.
However, the issue was the text. While "謹賀新年", "すまい工房", "2027年 元旦", the address, and the phone number were accurate, the greeting message came out as "お願いいいたします" (onegain itashimasu). It had an extra "い" (i) character. Additionally, the letters "TEL" were added to the phone number without being requested.
When asked for a revision, the sheep grew one size larger, and the company name became darker. This was a "retention-style" edit where the layout was largely preserved, making it more practical for real-world tasks than ChatGPT in that regard. However, the typo "お願いいいたします" remained unchanged even after the correction. Since the revision request this time was about the sheep and the company name, that was only natural, but it shows the risk of things going straight to print unless you scrutinize and verify the text right at generation.
What We Learned from the Comparison
Putting them side by side clearly revealed their distinct strengths.
- Text Accuracy: ChatGPT was accurate across all items. Gemini had a one-character typo in the greeting message.
- Resolution: ChatGPT came in at 1024×1536, slightly falling short of the benchmark. Gemini cleared the benchmark at 1696×2528.
- Revision approach: ChatGPT redraws the entire image (unrequested elements also change). Gemini maintains the layout.
- Common successes: Sheep motif, warm color palette, vertical orientation, margins, and not arbitrarily replacing masked characters in the address.
For this particular subject, ChatGPT was closer to being "ready to use as-is." The reason is simple: for New Year's cards, textual accuracy is the top priority. While you can find workarounds for resolution through printing methods, typos cannot be fixed once the cards are sent.
What We Learned
- When it comes purely to visual quality, image generation AIs are already at a practical level for New Year's cards. Both faithfully followed instructions regarding zodiac motifs and overall mood.
- Even so, you can't simply "generate and be done." At a bare minimum, you need to visually check the text character by character. Longer strings of text, such as greetings, are particularly risky.
- The approach to revisions differs by AI (full redraw vs. layout retention). For tasks requiring repeated fine-tuning, this difference becomes crucial.
- If you plan to print the cards, check the resolution beforehand as well. Even if it looks sharp on screen, it might fall short of the benchmark for full-bleed postcard printing.
- Next year is the Year of the Horse. Repeating this exact experiment next year with updated models will let us see how much textual typos have decreased. This test could easily become an annual tradition.
If there's an experiment you'd like to see tested next, please let us know in the comments.
