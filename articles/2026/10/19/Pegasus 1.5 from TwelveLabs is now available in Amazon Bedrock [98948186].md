---
id: "98948186cc0e34f7"
title: "Pegasus 1.5 from TwelveLabs is now available in Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/pegasus-1-5-from-twelvelabs-is-now-available-in-amazon-bedrock"
link: "https://aws.amazon.com/blogs/machine-learning/pegasus-1-5-from-twelvelabs-is-now-available-in-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-19T16:49:19Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Ron Tal"]
language: "en"
summary: "On Oct 9, 2026 we announced the availability of TwelveLabs’ Pegasus 1.5 on Amazon Bedrock . Pegasus 1.5 is a video language model that turns long-form video into structured, timestamped metadata. You describe the moments that matter to your workflow, and the model returns every matching segment as JSON. \n Video represents a significant and complex category of unstructured data, yet most of it…"
tags: ["Amazon Bedrock", "Announcements", "Foundational (100)"]
orgs: ["Amazon", "China"]
topics: ["models & research", "agents & coding", "jobs & society"]
content_source: "fulltext"
word_count: 1825
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Pegasus 1.5 from TwelveLabs is now available in Amazon Bedrock

AWS Machine Learning Blog · Ron Tal · 2026-10-19

Artificial Intelligence
Pegasus 1.5 from TwelveLabs is now available in Amazon Bedrock
On Oct 9, 2026 we announced the availability of TwelveLabs’ Pegasus 1.5 on Amazon Bedrock. Pegasus 1.5 is a video language model that turns long-form video into structured, timestamped metadata. You describe the moments that matter to your workflow, and the model returns every matching segment as JSON.
Video represents a significant and complex category of unstructured data, yet most of it remains unsearchable and underutilized. Extracting structured, actionable insights from that content has historically required labor-intensive manual review or fragmented toolchains.
With earlier versions of Pegasus, you can point the model at a clip, ask a question, and get an answer. Now, Pegasus 1.5 analyzes the entire video, finds every segment that matches user-defined criteria, and returns structured, timestamped metadata. It also introduces video segmentation, multimodal prompting with reference images, and on-the-fly processing.
With Pegasus 1.5 on Amazon Bedrock, you can analyze videos directly from an Amazon Simple Storage Service (Amazon S3) URI or a base64 string with no pre-indexing required, and your data remains within the AWS data boundary.
In this post, we cover what’s new in Pegasus 1.5, how the model is packaged on Amazon Bedrock, and how to send your first request. We then walk through video segmentation, structured JSON output, and multimodal prompting.
What’s new in Pegasus 1.5
Pegasus 1.5 has the following changes compared to previous versions:
- Time-based metadata generation. You define the segments, events, or domain-specific cues that matter to your workflow, such as editorial segments, sports plays, speaker changes, or brand appearances. Pegasus 1.5 returns every matching segment as JSON, with start and end times and the requested fields populated.
- Multimodal prompting. A segment definition can combine a text description with a visual reference. This makes it possible to locate a specific product, logo, or person, along with what they are doing on screen.
- On-the-fly processing. No ingestion pipeline or pre-indexing step is required. Videos are sent directly from Amazon S3 and results are returned in the response.
- Extended processing capacity. Pegasus 1.5 analyzes videos up to two hours long in a single request, up from one hour in Pegasus 1.2.
Pegasus 1.5 retains and enhances the core capabilities that made Pegasus 1.2 a powerful tool for video understanding, including:
- Video-to-text generation: Creates detailed textual descriptions based on video content.
- Granular visual comprehension: Analyzes objects, on-screen text, and numerical content within video frames.
- Temporal grounding: Accurately identifies timestamps of specific events within videos.
- Multimodal understanding: Combines visual, audio, and textual information for comprehensive analysis.
- Multilingual support: Full support for English, with partial support for Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish, Thai, and Vietnamese.
How Pegasus 1.5 works on Amazon Bedrock
Pegasus 1.5 takes a video and either a text prompt or a set of segment definitions, and returns text or JSON. You call it on the bedrock-runtime endpoint with the InvokeModel API, or with InvokeModelWithResponseStream when you want the response streamed as it’s generated.
Each request runs in one of two analysis modes, chosen with the analysisMode field:
You can point the model at video in two ways. An S3 location (s3Location) takes the object’s uri and the bucketOwner account ID, and suits long-form video. A base64 string (base64String) embeds the video in the request body, up to 25 MB, and suits short clips.
To track cost by application, create an application inference profile from the Pegasus 1.5 model, tag it, and call it by its Amazon Resource Name (ARN) in place of the model ID.
Getting started with Pegasus 1.5
The following section outlines how to get started with Pegasus 1.5.
Prerequisites
Before you begin, make sure you have:
- An active AWS account with Amazon Bedrock access.
- Python 3.10 or later, with the AWS SDK for Python (Boto3) installed.
- AWS Identity and Access Management (IAM) permissions for bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream.
- Model access enabled for TwelveLabs Pegasus 1.5 in the Amazon Bedrock console.
- Videos stored in an Amazon S3 bucket, or short clips you can send inline.
The following policy grants both invoke actions on Pegasus 1.5.
Boto3 signs requests with your usual AWS credentials. You can also authenticate with an Amazon Bedrock API key by setting it in the AWS_BEARER_TOKEN_BEDROCK environment variable. For production, prefer a short-term key generated from your IAM credentials with the aws-bedrock-token-generator package, because it expires automatically. Bearer-token authentication also requires the bedrock:CallWithBearerToken permission.
Send your first request
Install Boto3:
The following example analyzes a video stored in Amazon S3 in general mode. This example uses the global Cross Region Inference (CRIS) endpoint. To target the US geographic endpoint instead, replace “global.” with “us.” in the endpoint URL.
The response carries the answer in message, the token counts in input_tokens and output_tokens, and the reason generation ended in stopReason. A stopReason of length means the answer reached maxOutputTokens before it finished, so check it before you rely on the output:
Request fields for general mode:
For a short clip, you can send the video inline instead of from S3:
Note that the preceding example uses the optional includeMetering attribute. includeMetering: True makes Pegasus 1.5 add two billing-usage fields to the non-streaming response: outputTokenCount and inputVideoSecond (the analyzed video’s duration in seconds).
Stream the response
For interactive applications, InvokeModelWithResponseStream returns the answer in chunks as it’s generated. Each chunk carries the next piece of text in message:
Return structured JSON
In general mode, you can constrain the answer to a JSON Schema so downstream code can parse it directly. Set responseFormat.type to json_schema and put the schema under jsonSchema. The answer arrives in message as a JSON string:
Video segmentation: Turning video into structured data
Time-based metadata generation is where Pegasus 1.5 differs most from earlier versions. Instead of a prompt, you send one or more segment definitions, and the model returns every segment of the video that matches each one.
Set analysisMode to time_based_metadata and responseFormat.type to segment_definitions. The definitions take the place of inputPrompt, so leave that field out. Each definition has:
- id: a name for the definition, returned on every segment it matches.
- description: what a matching segment looks like.
- fields: the values to extract for each segment, each with a name, a type (string, boolean, number, integer, array, or timestamp), and a description.
The following example identifies each editorial section in a news broadcast and returns a title, summary, and key topics for each one:
The previous sample code when tested against a sports clip may produce an output like the following sample.
Each segment carries start_sec, end_sec, and the fields you defined. segmentTimeFormat controls how the times are written: seconds returns numbers you can do arithmetic on, while hh:mm:ss and hh:mm:ss.fff return readable timestamps as strings. The response also includes a definition_errors list, which is empty when every definition was processed.
A single request can include multiple segment definitions, for example one for editorial sections and another for on-screen brand appearances. Pegasus 1.5 returns the matches for all of them in one segments list, and tags each segment with _definition_id so you can tell them apart. The following example adds a second definition to the previous request and groups the results:
Because the schema is defined once, the same definitions can be applied across an entire video library, producing consistent metadata for every asset.
Multimodal prompting: Adding visual context to your queries
Pegasus 1.5 introduces multimodal prompting, so you can include reference images alongside your text prompts. This is useful when you want to ask the model about specific objects, people, or scenes that are easier to show than describe.
For example, you can provide a product image and ask the model to identify every moment where that product appears in a video. Or you can provide a reference image of a specific logo and ask the model to detect brand appearances and their timestamps. This capability enhances the precision of video analysis, and opens up use cases such as visual brand monitoring, product placement analysis, and image-guided content search.
Reference images attach differently depending on the mode. In general mode, put them in promptV2.mediaSources, alongside the question in promptV2.inputText. In segmentation mode (analysisMode: time_based_metadata), attach them to the mediaSources of each segment definition inside responseFormat.segmentDefinitions. A definition can then match a visual reference as well as a text description. Each image needs a name, a media_type of image, and exactly one source: either an inline base64String or an s3Location with uri and bucketOwner. A single request can carry up to 30 reference images.
A general-mode request asks the model about an object shown in a reference image. The following sample payload and response provide an example in general mode.
In segmentation mode, the reference image lives inside the definition, so Pegasus returns only the segments where that product appears. The following sample payload and response provide an example in segmentation mode.
Monitoring usage
Pegasus 1.5 publishes Amazon CloudWatch metrics in the AWS/Bedrock namespace under its model ID, including Invocations, OutputTokenCount, InvocationLatency, and InvocationClientErrors. Use them to track volume and latency. Pair them with application inference profiles when you need usage broken down by application.
Use cases
Pegasus 1.5 is designed for organizations that manage large volumes of long-form video:
- News and broadcast archives: Teams can define editorial segments, topics, and speaker changes once, then catalog years of footage that was previously searchable only by transcript keywords.
- Sports broadcasters and leagues: Detect plays, scoring events, and other key moments across full-length game footage, speeding up highlight production.
- Streaming applications: Scene-level metadata supports moment-based recommendations, contextual ad placement, and segment-level brand safety review.
In each case, people remain part of the workflow. Their work shifts from finding and tagging every moment by hand to reviewing and refining the metadata generated by the model.
Input requirements
Pegasus 1.5 supports the following video specifications:
- Duration: Up to 2 hours.
- File size: Up to 2 GB from Amazon S3, or up to 25 MB as a base64 string.
- Resolution: 360×360 to 5184×2160.
- Aspect ratio: Between 1:1 and 2.4:1, or their inverses.
- Formats: FFmpeg-supported formats.
Now available
TwelveLabs Pegasus 1.5 is available today on Amazon Bedrock in the US West (Oregon) AWS Region. Check the full Region list for future updates, and visit the Amazon Bedrock pricing page for pricing information. Pegasus 1.5 is billed through AWS Marketplace, so its charges appear on your AWS bill and in AWS Cost Explorer under TwelveLabs rather than Amazon Bedrock.
To get started:
- Visit the TwelveLabs models page on Amazon Bedrock to learn more about the model family.
- Review the Pegasus 1.5 model card for feature support, Region availability, and sample code.
- Send us feedback at AWS re:Post for Amazon Bedrock or through your usual AWS Support contacts.
We’re excited to see what you build with TwelveLabs Pegasus 1.5 in Amazon Bedrock.
