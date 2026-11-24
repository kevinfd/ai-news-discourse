---
id: "7aac9125c7b194c5"
title: "Google's Gemini API can now read Word, Excel, and more directly. Introducing the 'slicing' feature that lets you specify and pay only for the pages or cells you need | What ..."
url: "https://note.com/adhd_bakusoku/n/n59717d64c0f1?hl=en"
link: "https://note.com/adhd_bakusoku/n/n59717d64c0f1?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-24T04:32:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["メンサ会員のAi活用塾"]
language: "en"
summary: "Out of a 100-page document, you only really need it to read a few pages. Such situations are common in work. Google announced new features for the Gemini API in its official blog dated November 23, 2026."
tags: []
orgs: ["Google", "Amazon", "OpenAI", "Microsoft"]
topics: ["agents & coding", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 1148
paywalled: false
image: "/th?id=ONUT.KA7vhUf27y4iPD348aq2-g&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Google's Gemini API can now read Word, Excel, and more directly. Introducing the 'slicing' feature that lets you specify and pay only for the pages or cells you need | What ...

note · メンサ会員のAi活用塾 · 2026-11-24

Google's Gemini API can now read Word, Excel, and more directly. Introducing the 'slicing' feature that lets you specify and pay only for the pages or cells you need | What companies building systems to have AI read documents should know
Out of a 100-page document, you only really need it to read a few pages. Such situations are common in work. Google announced new features for the Gemini API in its official blog dated November 23, 2026. The Gemini API is a gateway for developers to call Gemini from other applications. It is now possible to pass Word, PowerPoint, Excel, and other files directly. Furthermore, you can specify only the necessary pages or cells to be read. When you specify slicing, the charges for the file are calculated based only on the selected parts.
What happened
- Announcement (dated November 23). Announced by a Google DeepMind representative on the official Google blog. → https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/
- Newly supported files. Microsoft Office (Word, PowerPoint, Excel) and OpenDocument. OpenDocument is a format used by free office software and others. You can also pass PDFs, audio, and video directly.
- Specifying 'slicing'. You can select the parts of the file you want it to read. Google calls this 'file slicing'.
- Documents/Slides: Page range, image quality (low, medium, high), and either 'text' or 'page images' (both are also possible).
- Spreadsheets: Sheet (tab), cell range, and combinations of 'values', 'formulas', and 'visuals'.
- Video: Time range, frames per second, image quality, and either 'transcription', 'frames', or 'audio'.
- Audio: Time range.
- Pricing mechanism. When slicing is specified, the file is counted and billed only for the selected parts. This is written in the developer documentation. → https://aistudio.google.com/docs/document-processing
- Available models. The official blog states that it is available for all Gemini 4 models. It is announced that it is already available in Google AI Studio and the Gemini API.
- Limits remain the same. Up to 50MB per file, up to 1,000 pages for PDFs, and up to 2,000 pages for Office files, etc. For spreadsheets, it is up to 50,000 cells per sheet. Even if you slice, the limits apply to the entire file.
Reference: Alphabet (Google's parent company) stock price chart (at the time of writing)
Explanation
1. You can stop 'reading the whole thing before searching'. Until now, large files had to be read in their entirety or split manually beforehand. With this update, once you upload to the Files API (the feature for storing files), you can slice different parts from the same file multiple times.
2. You can 'take a quick look, then get details only where needed'. Google recommends using the cheap 'text-only' mode to read the whole thing first. Then, view only the pages with tables or graphs in high image quality. Tokens are the units used to count charges. According to the documentation, when reading pages as images with Gemini 4 and 3, it costs approximately 280 tokens for low, 560 for medium, and 1,120 for high quality per page.
3. This is also a change for AI agents (AI that thinks through steps and performs tasks on its own). Previously, you had to run tools on your end to split files or convert them into images. Now, Google handles that task. Agents can specify on their own, 'Next, I want to see page 3.'
4. The beneficiaries are companies that want to automate document-heavy tasks (our account's perspective). These are companies building systems to have AI read estimates, meeting recordings, monthly summary tables, and so on. However, this is a developer-focused feature. It is not about changes to the standard Gemini app interface.
How to use it for work and how to try it today
Even if you are not a developer, you can use this to organize your needs before requesting a system (our account's view).
- List the 'documents you want the AI to read'. Select the documents you read repeatedly every month. Decide which pages or sheets are truly necessary.
- Talk to the person handling development about 'slicing'. Have them confirm whether the design is set up to read everything.
- Developers should run the examples in the documentation. Compare reading a small Word file as text only versus reading just one page in high resolution.
Example of a request to get help organizing documents (a prompt = instructions for AI). You can paste this into a ChatGPT or Gemini chat.
私は小さな会社の事務担当です。毎月、AIに読ませたい資料があります。
下に資料の名前と中身を書きます。
それぞれについて、AIに読ませるべきページ・シート・時間の範囲と、
「文字だけで足りる部分」「図や表を画像で見せたい部分」を分けて表にしてください。
専門用語は使わないでください。
（資料の例）
・月次の売上集計（Excel、12シート）
・営業会議の録画（60分）
・取引先からの提案書（PowerPoint、40枚）
Example of what a developer might ask an AI.
Gemini APIの「file slicing（ファイルの切り出し）」を使って、
社内のWord・Excelファイルを読む小さなプログラムを作りたいです。
Googleの公式ドキュメントに書かれた項目（start_page、end_page、content_layers など）だけを使い、
・Word：まず文字だけで全ページを読み、目的のページを探す。見つけたページだけ高い画質の画像で読む
・Excel：対象のシートとセルの範囲を指定し、値と数式を読む。グラフが必要なときだけ見た目も読む
という流れのPythonのコードを書いてください。
公式ドキュメントで確認できない項目は使わず、「要確認」と書いてください。
If you want to learn how to integrate AI into your own systems via API as in the example above, reading a book from cover to cover is the fastest way (our account's view). → Search for 'Generative AI API' books on Amazon
For those who want to learn starting from how to use Gemini in daily life, an introductory book is a good reference (our account's view). → Search for 'Gemini usage' books on Amazon
Points to note
- It is a developer-focused feature. It is something specified in programs using the Gemini API, not about the standard Gemini app.
- Pricing and free usage limits are not mentioned in the announcement. You should check the Google pricing page before using it.
- If you specify nothing, it reads everything. According to the documentation, for Gemini 4, documents are read as page images, and spreadsheets are read for all sheet values, formulas, and sheet names.
- There is no mention of availability by region. You should check if it is available in Japan via your own Google AI Studio.
- Be careful with confidential documents. You should first confirm whether company policy allows sharing the document with external services.
- In the API release notes, this feature is listed under the November 18th entry. This article is based on the official Google blog and developer documentation (confirmed November 24th).
Source:
- Google 'Introducing file slicing controls in the Gemini API' (November 23, 2026) https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/
- Gemini API "Document understanding" https://aistudio.google.com/docs/document-processing
- Gemini API "Release notes" https://aistudio.google.com/docs/changelog
Recommended articles to read together
- Gemini's new model "Neon". What makes the "fast and smart" AI available in the 2,900 yen/month Pro plan different? 3 things to try first for work https://note.com/adhd_bakusoku/n/ndc7c4c723a75
- Google announces "Gemini Decisions API," a new API that lets AI perform only "judgments." Judge up to 1,000 questions at once with yes/no or multiple-choice options https://note.com/adhd_bakusoku/n/n6c7cac975a9e
- Can you search the web while reading a PDF? Acrobat's AI Assistant now supports web search https://note.com/adhd_bakusoku/n/n1ec1908f5181
I summarize news and usage tips for using AI at work every day. Follow me to get the next article delivered to you.
*Some links in this article are affiliate links. As an Amazon Associate, this account earns income from qualifying purchases.
