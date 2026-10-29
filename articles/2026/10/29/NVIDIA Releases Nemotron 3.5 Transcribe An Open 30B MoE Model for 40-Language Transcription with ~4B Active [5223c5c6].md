---
id: "5223c5c63e91fadb"
title: "NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language Transcription with ~4B Active Parameters"
url: "https://marktechpost.com/2026/10/28/nvidia-nemotron-3-5-transcribe-open-speech-llm"
link: "https://marktechpost.com/2026/10/28/nvidia-nemotron-3-5-transcribe-open-speech-llm"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T04:41:24Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA has released Nemotron 3.5 Transcribe , an open-weights speech LLM built for transcription. One model handles 40 languages and recordings up to 1 hour . A text instruction picks the output style for each request. Options include verbatim, written form, speaker-attributed, contextual and translated output. For developers, it can replace separate ASR, diarization and alignment tools. \n\n…"
tags: ["Agentic AI", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "New Releases", "Open Source"]
orgs: ["Nvidia", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "safety & ethics", "agents & coding"]
content_source: "summary"
word_count: 1746
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language Transcription with ~4B Active Parameters

MarkTechPost · Asif Razzaq · 2026-10-29

NVIDIA has released Nemotron 3.5 Transcribe , an open-weights speech LLM built for transcription. One model handles 40 languages and recordings up to 1 hour . A text instruction picks the output style for each request. Options include verbatim, written form, speaker-attributed, contextual and translated output. For developers, it can replace separate ASR, diarization and alignment tools. 

 TL;DR 

 Size: 34B total and about 4.3B active parameters; 65,536-token context; audio up to 1 hour. 

 Runs on: 1x H100 80 GB in BF16. FP8 (about 35 GB) and NVFP4 (about 21 GB) checkpoints exist; NVFP4 runs on an RTX 5090. GGUF files target NeMo-Speech.cpp. 

 Performance: Best open-weights model on the English and multilingual Open ASR Leaderboards; top commercial APIs still lead. 

 Best: 4.71% mean WER on the 9 public English Open ASR sets (next open model: 4.94%). 

 Worst: 34.95% cpCER on AliMeeting Mandarin far-field meetings. 

 Bottom line: Best thing: 1 open model covers transcripts, speaker labels, timestamps and translation. Worst thing: offline only, with weak Mandarin meeting accuracy. 

 What is Nemotron 3.5 Transcribe? 

 Nemotron 3.5 Transcribe is a speech-augmented language model (SALM) from NVIDIA that turns audio and instructions into text. An audio encoder feeds embeddings into an LLM decoder, which makes transcription promptable. NVIDIA’s technical research report argues there is no single correct transcript. Numbers, fillers and domain terms depend on who reads the output. NVIDIA positions the model as a transcription specialist, not a general-purpose assistant. 

 How does the architecture work? 

 It has three parts: 

 Parallel Expert Encoder: a trainable 0.6B Transformer ASR encoder runs beside a frozen Nemotron 3 Diarization model. The diarizer tracks up to 8 speakers. Its speaker activity is added to the ASR features every 80 ms. The LLM therefore sees who spoke when, without architecture changes. 

 LLM backbone: Nemotron 3.5 Lightning 30B-A3B , a hybrid Mamba-Transformer MoE. It has 52 layers: 23 Mamba-2, 23 MoE and only 6 attention layers. Each MoE layer routes to 6 of 128 experts plus 1 shared expert. Few attention layers keep the KV cache small for hour-long audio. 

 Add-ons: a shared multi-token prediction (MTP) layer drafts tokens for speculative decoding. A 50M-parameter CTC adapter aligns the finished transcript to audio for word timestamps. 

 The model name says 30B-A4B, but the checkpoint holds about 34B parameters. The extra weight comes from the 1.3B MTP module and the audio components. 

 Training used 1 supervised fine-tuning stage on 256 H100 GPUs for 28,500 steps. A short RL stage followed: 400 GSPO updates with a reward of 1 minus WER. The model saw about 1.72M unique hours of audio, or 6.5M hours with repeats. 

 How does it score on benchmarks? 

 All numbers below are self-reported by NVIDIA in the technical report . 

 English Open ASR (9 public sets): 4.71% mean WER. The next open model, Qwen3-ASR-1.7B , scores 4.94%. Seven commercial systems still lead, topped by OtterAI speech-v3.1 at 3.88%. 

 Multilingual Open ASR (7 languages): 4.62% mean WER, versus 6.49% for Qwen3-ASR-1.7B. ElevenLabs Scribe v2 reaches 3.56%. 

 Long-form ASR: 10.98% mean WER, versus 13.37% for Parakeet-TDT-0.6B-v3. 

 Multi-speaker, full sessions: 15.80% mean cpWER, versus 16.83% for DiCoW v3.3 with DiariZen. NVIDIA says it is the first SALM to beat cascaded systems here. 

 Contextual ASR: an entity list cuts named-entity WER on ContextASR-Bench from 12.21% to 2.20%. 

 Auto-play</button>
</div>
</div>

<div class="pane" id="p2">
<div class="seg">
<button class="chip on" data-b="en">English Open ASR</button>
<button class="chip" data-b="ml">Multilingual Open ASR</button>
<button class="chip" data-b="lf">Long-form</button>
</div>
<div id="nt35bars"></div>
<p class="note" id="nt35bn"></p>
</div>

<div class="pane" id="p3">
<p class="note" style="margin:0 0 10px!important">1 checkpoint, different instructions. Click a style to see the request pattern and output shape (illustrative, not a model sample).</p>
<div class="seg" id="nt35ps">
<button class="chip on" data-p="0">Verbatim</button>
<button class="chip" data-p="1">Written form</button>
<button class="chip" data-p="2">Context terms</button>
<button class="chip" data-p="3">Speakers</button>
<button class="chip" data-p="4">Translate</button>
</div>
<div class="out"><div class="lbl">Instruction</div><pre><code id="nt35pi"></code></pre></div>
<div class="out"><div class="lbl">Output shape</div><pre><code id="nt35po"></code></pre></div>
</div>

<div class="pane" id="p4">
<div class="grid2">
<div class="card on"><h4>BF16</h4><div class="big">67.5 GB</div><p>Reference weights · 1x H100 80 GB</p><div class="more">Ampere, Hopper and Blackwell. NVIDIA estimates about 410 RTFx on 1 H100 with MTP2 (batched English ASR).</div></div>
<div class="card"><h4>FP8</h4><div class="big">~35 GB</div><p>Ada Lovelace, Hopper, Blackwell</p><div class="more">Error rate 1.0% higher in relative terms on average. NVIDIA recommends it when non-English accuracy matters most.</div></div>
<div class="card"><h4>NVFP4</h4><div class="big">~21 GB</div><p>Blackwell only · runs on RTX 5090</p><div class="more">Error rate 3.6% higher in relative terms on average. Best when memory or throughput is the main constraint.</div></div>
<div class="card"><h4>NIM speed</h4><div class="big">2,238x</div><p>Real time on 1 RTX PRO 6000 Blackwell</p><div class="more">NVFP4 + DFlash2 in the Nemotron Transcribe NIM; 30 s clip in 0.13 s. These serving optimizations are not open source yet.</div></div>
</div>
<p class="note">Runtimes: vLLM 0.32.0 + NeMo Speech plugin, Hugging Face Transformers, SGLang-Omni 0.2.0, GGML (NeMo-Speech.cpp). License: OpenMDW-1.1.</p>
</div>

<div class="pane" id="p5">
<div class="row"><div class="ic up">+</div><div><b>Best open-weights ASR:</b> 4.71% English and 4.62% multilingual mean WER on the Open ASR Leaderboards.</div></div>
<div class="row"><div class="ic up">+</div><div><b>Meetings:</b> 15.80% mean cpWER on full sessions, ahead of DiCoW v3.3 + DiariZen at 16.83%.</div></div>
<div class="row"><div class="ic up">+</div><div><b>Context:</b> an entity list cuts named-entity WER on ContextASR-Bench from 12.21% to 2.20%.</div></div>
<div class="row"><div class="ic dn">!</div><div><b>Commercial gap:</b> OtterAI speech-v3.1 reaches 3.88% English WER; ElevenLabs Scribe v2 reaches 3.56% multilingual.</div></div>
<div class="row"><div class="ic dn">!</div><div><b>Mandarin meetings:</b> 32.91% cpCER on AISHELL-4 and 34.95% on AliMeeting.</div></div>
<div class="row"><div class="ic dn">!</div><div><b>Offline only:</b> not a streaming ASR service; release-day vLLM is roughly 2x slower than the NIM.</div></div>
</div>

<div class="ft"><span>Source: NVIDIA technical report and model card (self-reported), Oct 2026</span><span class="br">© Marktechpost</span></div>

<script>
(function(){
var R=document.getElementById('mtp-nt35');
function post(){try{parent.postMessage({mtpEmbed:'nt35',h:R.offsetHeight+40},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
R.querySelectorAll('.pane').forEach(function(x){x.classList.remove('on')});
t.classList.add('on');document.getElementById(t.dataset.t).classList.add('on');
if(t.dataset.t==='p2')drawBars(curB);setTimeout(post,60);setTimeout(post,500);});});
var S=[
'<strong>Audio in.</strong> The model takes 16 kHz single-channel audio, up to 1 hour per request. Encoders process independent 30 s chunks, so encoder compute grows linearly with length. Each second of audio becomes 12.5 LLM input positions.',
'<strong>Parallel Expert Encoder.</strong> A trainable 32-layer Transformer ASR encoder (0.6B) runs beside the frozen Nemotron 3 Diarization model (~100M, up to 8 speakers). Speaker activity is added to ASR features every 80 ms, so the LLM sees who spoke when.',
'<strong>Hybrid MoE LLM.</strong> Nemotron 3.5 Lightning 30B-A3B: 23 Mamba-2, 23 MoE and 6 attention layers. 128 experts, top-6 routing, 1 shared expert, ~3.5B active. A shared MTP layer drafts tokens for speculative decoding.',
'<strong>Text + timestamps.</strong> The LLM writes the transcript in the style the instruction asks for. A 50M-parameter CTC adapter then force-aligns words to audio, giving speaker-attributed word timestamps.'];
var cur=0,timer=null,nodes=R.querySelectorAll('.node'),D=document.getElementById('nt35d'),W=document.getElementById('nt35w');
function go(i){cur=(i+4)%4;nodes.forEach(function(n,k){n.classList.toggle('on',k===cur)});D.innerHTML=S[cur];W.style.width=((cur+1)*25)+'%';}
nodes.forEach(function(n){n.addEventListener('click',function(){stop();go(+n.dataset.s)})});
document.getElementById('nt35next').onclick=function(){stop();go(cur+1)};
document.getElementById('nt35prev').onclick=function(){stop();go(cur-1)};
var pb=document.getElementById('nt35play');
function stop(){if(timer){clearInterval(timer);timer=null;pb.textContent=' Auto-play'}}
pb.onclick=function(){if(timer){stop();return}pb.textContent='❚❚ Pause';timer=setInterval(function(){go(cur+1)},2200)};
go(0);
var B={
en:{d:[['Nemotron 3.5 Transcribe',4.71,1],['Qwen3-ASR-1.7B',4.94],['Canary-Qwen-2.5B',5.38],['Parakeet-TDT-0.6B-v3',5.58],['Whisper-large-v3',6.66]],m:8,n:'Mean WER (%) on the 9 public English Open ASR sets, lower is better. Baselines: leaderboard results of Oct 21, 2026, as listed in NVIDIA\'s report.'},
ml:{d:[['Nemotron 3.5 Transcribe',4.62,1],['Qwen3-ASR-1.7B',6.49],['Voxtral-Small-24B',6.52],['Whisper-large-v3',7.94]],m:9,n:'Mean WER (%) over 7 languages (de, fr, it, es, pt, nl, hi; Hindi uses OIWER), lower is better. Baselines: leaderboard results of Oct 2, 2026.'},
lf:{d:[['Nemotron 3.5 Transcribe',10.98,1],['Parakeet-TDT-0.6B-v3',13.37],['Whisper-large-v3',13.92],['Canary-Qwen-2.5B',14.08]],m:16,n:'Mean WER (%) on the long-form track (Earnings-21, Earnings-22, CORAAL), lower is better.'}};
var curB='en',BB=document.getElementById('nt35bars'),BN=document.getElementById('nt35bn');
function drawBars(k){curB=k;var b=B[k];BB.innerHTML=b.d.map(function(r){return '<div class="bar'+(r[2]?' me':'')+'"><div class="lb">'+r[0]+'</div><div class="tr"><div class="fl" data-w="'+(r[1]/b.m*100)+'"></div></div><div class="v">'+r[1].toFixed(2)+'%</div></div>'}).join('');BN.textContent=b.n;
setTimeout(function(){BB.querySelectorAll('.fl').forEach(function(f){f.style.width=f.dataset.w+'%'})},40);setTimeout(post,80);}
R.querySelectorAll('[data-b]').forEach(function(c){c.addEventListener('click',function(){R.querySelectorAll('[data-b]').forEach(function(x){x.classList.remove('on')});c.classList.add('on');drawBars(c.dataset.b)})});
drawBars('en');
var P=[
['Audio transcription. Language: as spoken.\nWording: verbatim, including fillers and repetitions.\nFormatting: punctuation and capitalization.\nOutput: transcript only.','So, uh, the the launch moved to\nnext Tuesday at three thirty.'],
['Audio transcription. Language: as spoken.\nWording: omit fillers and accidental repetitions.\nNumbers in their standard written form.','So, the launch moved to\nnext Tuesday at 3:30.'],
['Transcribe with punctuation and capitalization.\nContext terms: Nemotron, NVFP4, DFlash2.','We tested Nemotron in NVFP4\nwith the DFlash2 draft model.'],
['Transcribe this audio with punctuation and capitalization.\nPut speaker tags <spk:0> <spk:1> <spk:2> <spk:3>\non the transcription.\n(+ timestamps enabled in the request)','<spk:0> Can we ship on Friday?\n<spk:1> Yes, if QA signs off.\n\nwords: [{"word":"Can","start":0.42,"end":0.58,"speaker":"spk:0"}, ...]'],
['Please translate the given speech to German.','Der Start wurde auf nächsten\nDienstag um 15:30 Uhr verschoben.']];
var PI=document.getElementById('nt35pi'),PO=document.getElementById('nt35po'),tt=null;
function showP(i){PI.textContent=P[i][0];var s=P[i][1],k=0;PO.textContent='';if(tt)clearInterval(tt);tt=setInterval(function(){k+=2;PO.textContent=s.slice(0,k);if(k>=s.length){clearInterval(tt);post()}},16);setTimeout(post,60);}
R.querySelectorAll('[data-p]').forEach(function(c){c.addEventListener('click',function(){R.querySelectorAll('[data-p]').forEach(function(x){x.classList.remove('on')});c.classList.add('on');showP(+c.dataset.p)})});
showP(0);
R.querySelectorAll('.card').forEach(function(c){c.addEventListener('click',function(){R.querySelectorAll('.card').forEach(function(x){if(x!==c)x.classList.remove('on')});c.classList.toggle('on');setTimeout(post,380)})});
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</div>
</body></html>"> 
 (function(){var f=document.getElementById("mtp-nt35-frame");window.addEventListener("message",function(e){if(e.data&&e.data.mtpEmbed==="nt35"&&e.data.h){f.style.height=e.data.h+"px";}});})(); 
 -->

 How do you deploy Nemotron 3.5 Transcribe? 

 Weights ship in BF16 , FP8 , NVFP4 and GGUF . A DFlash2 draft model is optional. The OpenMDW-1.1 license allows commercial use. 

 Runtimes include vLLM 0.32.0 with the NeMo Speech plugin, Transformers and SGLang-Omni 0.2.0. vLLM exposes an OpenAI-compatible API. 

 NVIDIA model’s main speed comes from its Nemotron Transcribe NIM. With NVFP4 and DFlash2, 1 RTX PRO 6000 Blackwell Server Edition transcribes 2,238 seconds of audio per second. It returns a 30-second clip in 0.13 seconds. There is a catch: those serving optimizations are not open source yet. NVIDIA expects the release-day vLLM path to be roughly 2x slower. On 1 H100 in BF16 with MTP2, NVIDIA estimates about 410 RTFx. 

 For fine-tuning, NVIDIA tested 17 tasks. Each took about 0.5 to 2.3 GPU-hours on a single GB300. 

 How does it compare with other open ASR models? 

 Feature Nemotron 3.5 Transcribe Qwen3-ASR-1.7B Canary-Qwen-2.5B Whisper-large-v3 Parameters 34B total, ~4.3B active 1.7B 2.5B 1.55B Languages 40 30 + 22 Chinese dialects English only 99 (HF tag) Max audio per request 1 hour Not disclosed 40 s in training 30 s window, chunked long-form Speaker attribution Built in, up to 8 speakers Not listed Not listed Not listed Word timestamps Built in (CTC adapter) Via separate ForcedAligner-0.6B Not listed Yes, word-level License OpenMDW-1.1 Apache-2.0 CC-BY-4.0 Apache-2.0 English Open ASR, 9 public sets (mean WER, lower is better) 4.71% 4.94%* 5.38%* 6.66%* Open ASR mean WER on own model card (earlier leaderboard set) Not reported 5.76% 5.63% 7.44% Multilingual Open ASR, 7 languages (mean WER) 4.62% 6.49%* Not applicable (English only) 7.94%* Reference hardware 1x H100 80 GB (BF16) Not disclosed Tested on A6000, A100, RTX 5090 Not disclosed 

 *Competitor scores on the current 9-set leaderboard come from NVIDIA’s report, citing Hugging Face leaderboard results from October 2026. The leaderboard set changed since the competitors published their own cards, so the 2 WER rows are not interchangeable. 

 Key Takeaways 

 One open model handles transcripts, speakers, timestamps and translation across 40 languages. 

 4.71% English WER is the best open-weights score; commercial APIs still lead. 

 About 4.3B active parameters; BF16 fits 1 H100, NVFP4 fits an RTX 5090. 

 An entity list cuts named-entity WER from 12.21% to 2.20%. 

 Offline only; Mandarin meetings and code-switching remain weak spots. 

 Check out the technical report , model weights , project page and live demo . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language Transcription with ~4B Active Parameters appeared first on MarkTechPost .
