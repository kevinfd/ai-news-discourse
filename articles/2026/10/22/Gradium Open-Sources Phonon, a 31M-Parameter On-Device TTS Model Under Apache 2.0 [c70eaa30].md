---
id: "c70eaa30e06d0fdc"
title: "Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache 2.0"
url: "https://marktechpost.com/2026/10/22/gradium-phonon-31m-on-device-tts"
link: "https://marktechpost.com/2026/10/22/gradium-phonon-31m-on-device-tts"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T16:56:12Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Gradium has open-sourced Phonon , a family of small text-to-speech models built to run on the device. The Gradium Phonon on-device TTS model comes in 31M and 40M sizes. The English Phonon 31m ships under Apache 2.0 and fits in a 64.5 MB file. Developers get natural speech with no cloud call, no GPU and no per-character bill. \n\n TL;DR \n\n Size: 31M parameters (excluding the audio tokenizer), 64.5…"
tags: ["Agentic AI", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "New Releases", "Open Source", "Staff", "Technology", "TTS"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 1508
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache 2.0

MarkTechPost · Asif Razzaq · 2026-10-22

Gradium has open-sourced Phonon , a family of small text-to-speech models built to run on the device. The Gradium Phonon on-device TTS model comes in 31M and 40M sizes. The English Phonon 31m ships under Apache 2.0 and fits in a 64.5 MB file. Developers get natural speech with no cloud call, no GPU and no per-character bill. 

 TL;DR 

 Size: 31M parameters (excluding the audio tokenizer), 64.5 MB q8 GGUF, 24 kHz mono output. Phonon 40m: 40M, 74.6 MB. 

 Runs on: CPUs, phones, Raspberry Pi 5, browsers (WASM, WebGPU) and NVIDIA GPUs. No GPU required. 

 Performance: top English Elo among open models Gradium tested; about 7 ms to first audio on CPU. 

 Best: 1.70% WER on a 500-sentence hard set, versus 3.50% for Kokoro (Gradium’s eval). 

 Worst: 0.51% Seed-TTS LLM WER, behind Kokoro (0.45%) and Magpie (0.46%). 

 What is Gradium Phonon? 

 Phonon is an open-weight TTS family from Gradium , a Paris voice AI company spun out of Kyutai. It generates speech locally on phones, laptops, boards and browsers. 

 The family has three models : 

 Phonon 31m: English only, 37 built-in voices, Apache 2.0. 

 Phonon 40m: 1 model per language (English, French, German, Spanish, Portuguese), CC BY-NC 4.0. 

 Phonon 40m multilingual: all 5 languages in 1 model, 102 voices, CC BY-NC 4.0. 

 How does Phonon work? 

 Phonon uses a causal transformer backbone. Its prefix combines text and speaker embeddings. A SentencePiece tokenizer with a 4,000-token vocabulary reads raw text, with no phoneme conversion. 

 The backbone generates 1 latent vector per 80 ms frame. A flow-matching head turns that vector plus noise into an audio embedding in a single step. A smaller variant of Kyutai’s Mimi decoder then outputs 24 kHz PCM audio. A separate end-of-speech head decides when to stop. 

 Phonon 31m uses 6 transformer layers, width 512 and 8 attention heads. Phonon 40m uses 9 layers at the same width. Both are distilled from a larger Phonon teacher. Training ran on an NVIDIA H100 cluster with NCCL and CUDA Graphs. 

 The work builds on Kyutai’s Continuous Audio Language Models research and Pocket TTS. 

 </span>
 <div class="st"><span class="n">STEP 2</span><b>SentencePiece</b></div><span class="arr"> </span>
 <div class="st"><span class="n">STEP 3</span><b>Causal transformer</b></div><span class="arr"> </span>
 <div class="st"><span class="n">STEP 4</span><b>Flow-matching head</b></div><span class="arr"> </span>
 <div class="st"><span class="n">STEP 5</span><b>Mimi decoder</b></div>
 </div>
 <div class="detail" id="how-d"></div>
 <div class="frames" id="frames"></div>
 <div class="ctl">
 <button class="btn ghost" id="prev"> Back</button>
 <button class="btn" id="next">Next step </button>
 <button class="btn ghost" id="play">Stream frames</button>
 <span class="cap">Each bar is 1 latent frame = 80 ms of 24 kHz audio</span>
 </div>
 </div>

 <div class="panel" id="p-bench">
 <div class="seg" id="bseg">
 <button class="on" data-b="wer">Hard-set WER (lower is better)</button>
 <button data-b="elo">English Elo (higher is better)</button>
 <button data-b="seed">Seed-TTS WER</button>
 </div>
 <div id="bars"></div>
 <div class="note" id="bnote"></div>
 </div>

 <div class="panel" id="p-speed">
 <div class="hw" id="hw"></div>
 <div class="gauge">
 <div class="gc"><div class="k">Time to first audio</div><div class="val" id="g1">6.9 ms</div><div class="src" id="g1s"></div></div>
 <div class="gc"><div class="k">Speed vs real time</div><div class="val" id="g2">29.9x</div><div class="src" id="g2s"></div></div>
 </div>
 <div class="note">Gradium blog rows are Phonon 31m; partner and press-release rows do not name the variant. Higher "x real time" means more seconds of audio per second of compute. Measured by Gradium and launch partners.</div>
 </div>

 <div class="panel" id="p-trade">
 <div class="to">
 <div class="tc p"><h4>Where Phonon 31m leads</h4><ul>
 <li>1.70% hard-set WER vs 3.50% for Kokoro</li>
 <li>6.9 ms to first audio on a MacBook Air M5 CPU</li>
 <li>3.7x real time on a Raspberry Pi 5</li>
 <li>Apache 2.0 weights, tokenizer and voices</li></ul></div>
 <div class="tc c"><h4>Where it falls short</h4><ul>
 <li>0.51% Seed-TTS WER, behind Kokoro at 0.45%</li>
 <li>English only at 31M; 40m models are CC BY-NC</li>
 <li>Prosody resets between sentences on long text</li>
 <li>All benchmarks are run by Gradium</li></ul></div>
 </div>
 </div>

 <div class="ft"><span>Sources: gradium.ai/blog, huggingface.co/gradium · self-reported numbers</span><span class="brand">Built by Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-phonon');
function send(){try{parent.postMessage({mtpFrameHeight:R.offsetHeight+40,id:'mtp-phonon'},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
 R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 R.querySelectorAll('.panel').forEach(function(p){p.classList.remove('on')});
 R.querySelector('#p-'+t.dataset.t).classList.add('on');
 if(t.dataset.t==='bench')drawBars(cur);
 setTimeout(send,60);});});
R.querySelectorAll('.mc').forEach(function(c){c.addEventListener('click',function(){
 R.querySelectorAll('.mc').forEach(function(x){x.classList.remove('on')});c.classList.add('on');
 document.getElementById('fam-d').textContent=c.dataset.d;setTimeout(send,30);});});
var steps=['Input text plus a speaker embedding. The voice can be built-in, cloned or designed in Gradium Studio, then run locally.',
'Raw text becomes tokens from a 4,000-token SentencePiece vocabulary. No phoneme conversion, so new languages are easier to add.',
'A causal transformer (6 layers, width 512, 8 heads in 31m) generates 1 latent vector per 80 ms frame, autoregressively.',
'A flow-matching head turns each latent plus noise into a continuous audio embedding in a single step. An end-of-speech head decides when to stop.',
'A smaller variant of Kyutai\'s Mimi decoder converts embeddings into 24 kHz PCM audio, streamed while generation continues.'];
var si=0,sts=R.querySelectorAll('.st');
function setStep(i){si=(i+5)%5;sts.forEach(function(s,k){s.classList.toggle('on',k===si)});document.getElementById('how-d').textContent=steps[si];}
setStep(0);
document.getElementById('next').onclick=function(){setStep(si+1)};
document.getElementById('prev').onclick=function(){setStep(si-1)};
var F=document.getElementById('frames');for(var i=0;i<24;i++){var d=document.createElement('div');d.className='fr';F.appendChild(d);}
var tm=null;document.getElementById('play').onclick=function(){
 var fr=F.children,k=0;clearInterval(tm);setStep(2);
 for(var j=0;j<fr.length;j++){fr[j].classList.remove('live');fr[j].style.height='20%';}
 tm=setInterval(function(){if(k>=fr.length){clearInterval(tm);setStep(4);return;}
 fr[k].classList.add('live');fr[k].style.height=(30+Math.round(Math.abs(Math.sin(k*1.3))*65))+'%';
 if(k===8)setStep(3);k++;},110);};
var B={wer:{max:9,u:'%',rows:[['Phonon 31m',1.70,1],['Phonon 40m multi',2.11,1],['Phonon 40m',2.22,1],['Kokoro',3.50],['Kitten TTS',7.40],['NeuTTS Nano',8.71]],
 n:'500 hard English sentences (phone numbers, emails, postal codes). Magpie scored 27.51%, off this scale. The Hugging Face card lists 1.5% for Phonon 31m; the blog lists 1.70%.'},
 elo:{max:2150,min:1900,u:'',rows:[['Phonon 40m',2117,1],['Phonon 31m',2098,1],['Phonon 40m multi',2097,1],['Pocket TTS 100m',2056],['Kokoro',2043],['NeuTTS',2034],['Magpie',1939]],
 n:'Blind pairwise listening tests, US English: 468 raters, 8,290 votes. Bars start at 1900 Elo.'},
 seed:{max:0.7,u:'%',rows:[['Phonon 40m',0.45,1],['Kokoro',0.45],['Magpie',0.46],['Phonon 40m multi',0.48,1],['Phonon 31m',0.51,1],['NeuTTS',0.62]],
 n:'Seed-TTS English evaluation sentences, LLM-assisted WER. Here Phonon 31m trails Kokoro and Magpie.'}};
var cur='wer';
function drawBars(k){cur=k;var b=B[k],h='';b.rows.forEach(function(r){h+='<div class="bar'+(r[2]?' me':'')+'"><span class="lb">'+r[0]+'</span><div class="tr"><div class="fl" data-w="'+(((r[1]-(b.min||0))/(b.max-(b.min||0)))*100).toFixed(1)+'"></div></div><span class="v">'+(k==='elo'?r[1]:r[1].toFixed(2)+b.u)+'</span></div>'});
 document.getElementById('bars').innerHTML=h;document.getElementById('bnote').textContent=b.n;
 setTimeout(function(){R.querySelectorAll('#bars .fl').forEach(function(f){f.style.width=f.dataset.w+'%'})},40);setTimeout(send,80);}
R.querySelectorAll('#bseg button').forEach(function(x){x.onclick=function(){R.querySelectorAll('#bseg button').forEach(function(y){y.classList.remove('on')});x.classList.add('on');drawBars(x.dataset.b);}});
drawBars('wer');
var H=[['MacBook Air M5 CPU','4 threads, no KleidiAI','6.9 ms','29.9x','Gradium blog'],
['M5 + KleidiAI + Accelerate','4 threads','5.4 ms','46.7x','Gradium blog'],
['Raspberry Pi 5','CPU','38 ms','3.7x','Gradium blog'],
['Snapdragon 8 Elite Gen 5','Oryon CPU','7.5 ms','24x','Gradium with Qualcomm'],
['Arm CPU + KleidiAI','Arm-measured','28 ms','15x','Measured by Arm'],
['NVIDIA L40S','CUDA backend','5 ms','Not disclosed','Gradium press release']];
var hw=document.getElementById('hw'),hh='';H.forEach(function(r,i){hh+='<div class="hwc'+(i?'':' on')+'" data-i="'+i+'"><b>'+r[0]+'</b><small>'+r[1]+'</small></div>'});hw.innerHTML=hh;
function count(el,txt){var m=txt.match(/[\d.]+/);if(!m){el.textContent=txt;return;}var end=parseFloat(m[0]),dec=(m[0].split('.')[1]||'').length,suf=txt.slice(m.index+m[0].length),t0=null;
 function f(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/600,1);el.textContent=(end*p).toFixed(dec)+suf;if(p<1)requestAnimationFrame(f);}requestAnimationFrame(f);}
function pick(i){var r=H[i];R.querySelectorAll('.hwc').forEach(function(c){c.classList.toggle('on',+c.dataset.i===i)});
 count(document.getElementById('g1'),r[2]);count(document.getElementById('g2'),r[3]);
 document.getElementById('g1s').textContent=r[4];document.getElementById('g2s').textContent=r[4];}
R.querySelectorAll('.hwc').forEach(function(c){c.onclick=function(){pick(+c.dataset.i)}});
pick(0);
window.addEventListener('load',send);window.addEventListener('resize',send);setTimeout(send,300);
})();
</script>
</body>
</html>
" style="width:100%;height:600px;border:0;display:block;background:transparent;" loading="lazy" scrolling="no"> 

window.addEventListener('message',function(e){if(e.data&&e.data.id==='mtp-phonon'&&e.data.mtpFrameHeight){var f=document.getElementById('mtp-phonon-frame');if(f)f.style.height=e.data.mtpFrameHeight+'px';}});

 How does Phonon perform on benchmarks? 

 Gradium ran blind pairwise listening tests with 1,189 raters and 17,270 votes. In US English, Phonon 40m scored 2117 Elo and Phonon 31m scored 2098. Kokoro scored 2043, NeuTTS 2034 and Magpie 1939. 

 Accuracy was tested on a public hard-sentence set . It holds 500 sentences per language, full of phone numbers, emails and postal codes. Phonon 31m scored 1.70% WER against 3.50% for Kokoro and 8.71% for NeuTTS Nano. 

 Built-in text normalization drives much of that gap. 

 On the easier Seed-TTS set, the gap closes. Phonon 31m scored 0.51% LLM WER, while Kokoro scored 0.45%. 

 How fast is Phonon on a CPU? 

 On a MacBook Air M5 CPU with 4 threads, Phonon 31m reaches first audio in 6.9 ms. It runs 29.9x faster than real time. Kokoro takes 517 ms, because it does not stream. With Arm KleidiAI and Apple Accelerate, Phonon 31m reaches 46.7x real time. 

 On a Raspberry Pi 5, Phonon 31m starts in 38 ms and runs 3.7x faster than real time. Gradium says Kokoro needs 7 seconds to start there. 

 On Snapdragon 8 Elite Gen 5, Phonon starts in 7.5 ms at 24x real time. On an NVIDIA L40S, CUDA reaches first speech in 5 ms. An AMD EPYC 7413 CPU takes 43 ms, per the press release . 

 Comparison: Phonon vs Kokoro, NeuTTS Nano and Kitten TTS 

 Feature Phonon 31m Phonon 40m multilingual Kokoro-82M NeuTTS Nano Kitten TTS v0.8 Developer Gradium Gradium hexgrad Neuphonic KittenML Parameters 31M (excl. tokenizer) 40M 82M ~228.7M total, ~116.8M active 15M / 40M / 80M Weights 64.5 MB (q8) 74.6 MB (q8) Not disclosed Not disclosed 25 to 80 MB Languages English EN, FR, DE, ES, PT 8 (v1.0) English (collection adds ES, FR, DE) English License Apache 2.0 CC BY-NC 4.0 Apache 2.0 NeuTTS Open License 1.0 Apache 2.0 Hard-set WER, EN (Gradium eval) 1.70% 2.11% 3.50% 8.71% 7.40% (variant not disclosed) English Elo (Gradium eval) 2098 2097 2043 2034 Not tested Seed-TTS LLM WER, EN (Gradium eval) 0.51% 0.48% 0.45% 0.62% Not tested First audio, M5 CPU, 4 threads 6.9 ms 8.8 ms (40m arch) 517 ms Not disclosed Not disclosed 

 Benchmark rows come from Gradium’s blog and model card . Size, language and license rows come from each model’s own card. 

 How can developers deploy Phonon? 

 The runtime is MIT or Apache-2.0 licensed. It covers Rust, Python ( pip install ptts ), Swift, C, C++ and the browser via phonon-tts . It also ships an OpenAI-compatible server and a WebSocket server. 

 Phonon loads in Transformers, MLX-Audio, Ollama and LM Studio. Voice cloning and voice design run in Gradium Studio, then the voice runs locally. 

 Key Takeaways 

 Phonon 31m is a 31M, 64.5 MB English TTS model under Apache 2.0. 

 It reports 1.70% WER on hard text, against 3.50% for Kokoro. 

 First audio arrives in 6.9 ms on a MacBook Air M5 CPU. 

 It runs 3.7x faster than real time on a Raspberry Pi 5. 

 Multilingual 40m models exist, but under a non-commercial license. 

 Check out the technical blog , model card , GitHub runtime and hard-sentence dataset . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache 2.0 appeared first on MarkTechPost .
