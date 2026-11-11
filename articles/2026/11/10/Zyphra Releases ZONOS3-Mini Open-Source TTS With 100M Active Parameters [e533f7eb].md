---
id: "e533f7eb1ec855e5"
title: "Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters"
url: "https://marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts"
link: "https://marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T15:42:55Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Zyphra has released ZONOS3-Mini , an open-source text-to-speech model built for real-time use on local devices. The ZONOS3-Mini text-to-speech model is a sparse Mixture of Experts (MoE) with 800M total and 100M active parameters. It supports zero-shot voice cloning and word-level delivery control. Weights ship under Apache 2.0. For AI devs, size is the key point. It runs in a browser tab, on a…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning"]
orgs: ["Nvidia", "Apple"]
topics: ["models & research", "chips & infrastructure", "safety & ethics"]
content_source: "summary"
word_count: 1677
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters

MarkTechPost · Asif Razzaq · 2026-11-10

Zyphra has released ZONOS3-Mini , an open-source text-to-speech model built for real-time use on local devices. The ZONOS3-Mini text-to-speech model is a sparse Mixture of Experts (MoE) with 800M total and 100M active parameters. It supports zero-shot voice cloning and word-level delivery control. Weights ship under Apache 2.0. For AI devs, size is the key point. It runs in a browser tab, on a laptop or on a server GPU. 

 TL;DR 

 Size: 800M total parameters, about 100M active per token (64 experts, top-2 routing); 32,768-position context; up to 10 minutes of audio per generation. 

 Runs on: NVIDIA GPUs via SGLang-Omni, Apple Silicon via MLX, CPU/CUDA/Metal/Vulkan via ggml, and phones or laptops via WebGPU in the browser. 

 Performance: Ranks first among open models on Zyphra’s ZTTS2-Eval Capability Index (self-reported). 

 Best: 80 ms median time to first audio on one H100 at 8 concurrent requests, and 457 seconds of audio per second peak throughput. 

 Worst: Under 570 ms time to first audio in the browser on a Pixel 9, versus under 150 ms on an M3 MacBook Air. 

 Bottom line: Best: frontier-level open TTS quality at 100M active parameters. Worst: every benchmark is run by Zyphra itself, and reference-clip cloning scores far lower than embedding mode. 

 What is ZONOS3-Mini? 

 ZONOS3-Mini is a compact zero-shot voice-cloning TTS model from Zyphra that runs in real time on-device. Zyphra trained it on 112 NVIDIA H100s in 2.5 days. It follows ZONOS2 , which used 8B parameters and an 86 Hz codec. That size limited where ZONOS2 could be deployed. 

 How does the ZONOS3-Mini architecture work? 

 Zyphra changed 3 layers of the stack : 

 A new codec : Zyphra trained Zyphra Audio Codec 1 (ZAC-1) to replace the Descript Audio Codec. ZAC-1 runs at 15 Hz with 10 codebooks of 4,096 entries: 1 semantic and 9 acoustic. Zyphra reports a 10x word error rate reduction versus a DAC-trained model under similar data constraints. A causal iSTFT head renders each frame to 44.1 kHz audio as soon as it is generated. 

 A hybrid MoE backbone : The model card lists 11 layers with model dimension 1,024. Sequence mixing follows a 3:1 ratio: 9 Gated DeltaNet layers and 2 global attention layers. Zyphra also adds latent MoE, Q balancing and attention residuals. 

 A new speaker encoder : Voice representation moves from the Qwen3-TTS speaker encoder to MECT-B2. The model accepts a raw reference clip of up to 60 seconds, or a single 192-dimensional speaker embedding. Post-training used DPO, then GRPO, to improve robustness. 

 How does word-level voice control work? 

 Identity controls cover age, gender, accent and voice texture through speaker embedding vectors and accent task vectors. Delivery controls cover pace, emotion, projection and liveliness through activation steering. Learned alignment heads let steering apply to specific words during streaming. A separate edit model, based on a VoiceCraft recipe, can modify sentences after generation. 

 Step through</button><button class="btn gh" id="rst">Reset</button></div>
 </div>

 <div class="pn" id="p2">
 <div class="det"><strong>64 experts, top-2 routing.</strong> Each token activates 2 experts, so about 100M of the 800M parameters do work per step. That is why the model fits real-time budgets on laptops and phones.</div>
 <div class="moe" id="moe"></div>
 <div class="cap" id="moecap">Routing token 1 …</div>
 <div class="ctl"><button class="btn" id="route"> Route tokens</button></div>
 <div class="note">ZONOS2 used 8B parameters on an 86 Hz codec. ZONOS3-Mini cuts both: 800M total, 15 Hz frames.</div>
 </div>

 <div class="pn" id="p3">
 <div class="grp">Identity (speaker embedding + accent vectors)</div>
 <div class="chips" data-g="id">
 <button class="chip on" data-d="Neutral base voice. No identity steering applied.">Neutral</button>
 <button class="chip" data-d="Age steering, e.g. age −1.5 targets a young adult and +1.5 an older adult.">Age</button>
 <button class="chip" data-d="Gender presentation steering, e.g. gender −1.5 for a masculine target.">Gender</button>
 <button class="chip" data-d="Accent task vectors, e.g. british 1.5 or australian 1.5, keeping the speaker recognizable.">Accent</button>
 <button class="chip" data-d="Texture steering: soft, raspy, bright or deep (e.g. raspy +5).">Texture</button>
 </div>
 <div class="grp">Delivery (activation steering, word-level)</div>
 <div class="chips" data-g="dl">
 <button class="chip on" data-w="-1" data-d="Whole line delivered neutrally.">Neutral</button>
 <button class="chip" data-w="0" data-d="Whisper +4 applied only to the span “I didn’t say”, via learned alignment heads.">Whisper opening</button>
 <button class="chip" data-w="1" data-d="Whisper +4 applied only to “she took the keys”.">Whisper ending</button>
 <button class="chip" data-w="-1" data-d="Emotion axes such as happy, angry or scared (e.g. scared +8).">Emotion</button>
 <button class="chip" data-w="-1" data-d="Pace −2 to +2 changes speed while keeping every word intelligible.">Pace</button>
 <button class="chip" data-w="-1" data-d="Projection −3 (intimate) to +3 (calling across a room).">Projection</button>
 </div>
 <div class="sent"><span class="w" data-s="0">I</span> <span class="w" data-s="0">didn’t</span> <span class="w" data-s="0">say</span> <span class="w" data-s="1">she</span> <span class="w" data-s="1">took</span> <span class="w" data-s="1">the</span> <span class="w" data-s="1">keys.</span></div>
 <div class="det" id="cdet">Neutral base voice. No identity steering applied.</div>
 <div class="note">Settings shown are examples from Zyphra’s published control demos. A VoiceCraft-style edit model can also change words after generation.</div>
 </div>

 <div class="pn" id="p4">
 <div class="seg" id="seg">
 <button class="chip on" data-m="ci">Capability Index ↑</button>
 <button class="chip" data-m="wer">Clean WER ↓</button>
 <button class="chip" data-m="sim">Speaker similarity ↑</button>
 <button class="chip" data-m="ut">MSR-UTMOS ↑</button>
 </div>
 <div id="bars"></div>
 <div class="note" id="bnote"></div>
 <div class="note">Source: Zyphra ZTTS2-Eval explorer, all-language set, ZONOS3-Mini in speaker-embedding mode. Self-reported by Zyphra.</div>
 </div>

 <div class="pn" id="p5">
 <div class="grid" id="dgrid">
 <div class="dc on" data-c="b"><b>Browser · WebGPU</b><p>Runs on your own GPU, no install. &lt;570 ms TTFA on a Pixel 9, &lt;150 ms on an M3 MacBook Air.</p></div>
 <div class="dc" data-c="s"><b>NVIDIA · SGLang-Omni</b><p>OpenAI-compatible /v1/audio/speech with streaming. 80 ms TTFA on 1 H100 at 8 concurrent.</p></div>
 <div class="dc" data-c="n"><b>Native · MLX / ggml</b><p>MLX for Apple Silicon; C++/ggml server and CLI for CPU, CUDA, Metal or Vulkan.</p></div>
 <div class="dc" data-c="c"><b>Hosted · Zyphra Cloud</b><p>Managed API served on NVIDIA H200s.</p></div>
 </div>
 <pre id="code"></pre>
 </div>

 <div class="ft"><span>Sources: zyphra.com · huggingface.co/Zyphra · ZTTS2-Eval</span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('z3m');
function $(s){return R.querySelector(s)} function $$(s){return R.querySelectorAll(s)}
function rs(){try{parent.postMessage({type:'z3m-h',h:R.offsetHeight+40},'*')}catch(e){}}
$$('.tab').forEach(function(t){t.onclick=function(){$$('.tab').forEach(function(x){x.classList.remove('on')});$$('.pn').forEach(function(x){x.classList.remove('on')});t.classList.add('on');$('#'+t.dataset.t).classList.add('on');if(t.dataset.t==='p4')draw(cur);rs()}});
var D=['<strong>Text.</strong> Input is NeMo-normalized (9 languages) and tokenized with an 8,192-entry SuperBPE vocabulary.','<strong>Speaker.</strong> Either a raw reference clip (up to 60 s, encoded into a token prefix) or a single 192-d MECT-B2 speaker embedding.','<strong>Hybrid MoE backbone.</strong> 11 layers: 9 Gated DeltaNet + 2 global attention, latent MoE with 64 experts and top-2 routing. Context: 32,768 positions.','<strong>ZAC-1 codes.</strong> Zyphra Audio Codec 1 at 15 Hz: 1 semantic + 9 acoustic codebooks of 4,096 entries each.','<strong>Causal iSTFT head.</strong> Each frame renders to 44.1 kHz audio as soon as it is complete, so streaming starts early.'];
var si=0,tm=null;
function setS(i){si=i;$$('#pipe .st').forEach(function(x){x.classList.toggle('on',+x.dataset.i===i)});$('#det').innerHTML=D[i];}
$$('#pipe .st').forEach(function(x){x.onclick=function(){setS(+x.dataset.i)}});
var F=$('#frames');for(var k=0;k<30;k++){var d=document.createElement('div');d.className='fr';F.appendChild(d)}
function frames(){var fs=F.children,j=0;var iv=setInterval(function(){if(j>=fs.length){clearInterval(iv);return}fs[j].classList.add('live');fs[j].style.height=(25+Math.round(Math.abs(Math.sin(j*1.7))*75))+'%';j++},70)}
$('#play').onclick=function(){clearInterval(tm);setS(0);[].forEach.call(F.children,function(f){f.classList.remove('live');f.style.height='20%'});var n=0;tm=setInterval(function(){n++;if(n>4){clearInterval(tm);return}setS(n);if(n===4)frames()},1100)};
$('#rst').onclick=function(){clearInterval(tm);setS(0);[].forEach.call(F.children,function(f){f.classList.remove('live');f.style.height='20%'})};
setS(0);
var M=$('#moe');for(var e=0;e<64;e++){var x=document.createElement('div');x.className='ex';M.appendChild(x)}
$('#route').onclick=function(){var t=0;var iv=setInterval(function(){[].forEach.call(M.children,function(c){c.classList.remove('hit')});if(t>=8){clearInterval(iv);$('#moecap').textContent='8 tokens routed · 2 of 64 experts active per token';return}var a=Math.floor(Math.random()*64),b=(a+1+Math.floor(Math.random()*63))%64;M.children[a].classList.add('hit');M.children[b].classList.add('hit');t++;$('#moecap').textContent='Routing token '+t+' → experts '+a+' and '+b},450)};
$$('#p3 .chips').forEach(function(g){g.querySelectorAll('.chip').forEach(function(c){c.onclick=function(){g.querySelectorAll('.chip').forEach(function(x){x.classList.remove('on')});c.classList.add('on');$('#cdet').textContent=c.dataset.d;if(g.dataset.g==='dl'){var w=c.dataset.w;$$('#p3 .w').forEach(function(s){s.classList.toggle('wh',w!=='-1'&&s.dataset.s===w)})}}})});
var B={ci:{n:'Capability Index',v:[66.2,61.7,60.2,37.7],max:70,note:'Item-response-theory index over 420 items. Reference-clip mode scores 44.7.'},wer:{n:'Clean WER',v:[7.79,11.06,11.01,25.55],max:28,note:'Lower is better. Clean read speech, 35 languages.'},sim:{n:'Speaker similarity',v:[83.4,81.2,82.9,69.6],max:90,note:'Higher is better. Clean set.'},ut:{n:'MSR-UTMOS',v:[3.07,3.16,3.04,3.54],max:4,note:'Higher is better. ZONOS3-Mini trails Fish S2 Pro and Qwen3-TTS 1.7B here.'}};
var NM=['ZONOS3-Mini','Fish S2 Pro','MOSS-TTS v1.5','Qwen3-TTS 1.7B'],cur='ci';
function draw(m){cur=m;var b=B[m],h='';for(var i=0;i<4;i++){h+='<div class="row"><span class="nm">'+NM[i]+'</span><div class="trk"><div class="bar'+(i===0?' me':'')+'" data-w="'+(b.v[i]/b.max*100)+'"></div></div><span class="val">'+b.v[i]+'</span></div>'}$('#bars').innerHTML=h;$('#bnote').textContent=b.note;setTimeout(function(){$$('#bars .bar').forEach(function(x){x.style.width=x.dataset.w+'%'})},40)}
$$('#seg .chip').forEach(function(c){c.onclick=function(){$$('#seg .chip').forEach(function(x){x.classList.remove('on')});c.classList.add('on');draw(c.dataset.m)}});
draw('ci');
var C={b:'Open zyphra.com/zonos3mini/localplayground\n# First visit downloads and caches the model.\n# Needs a browser with WebGPU support.',s:'sgl-omni serve --model-path Zyphra/ZONOS3-Mini --port 8000\n\ncurl -X POST http://localhost:8000/v1/audio/speech \\\n -H "Content-Type: application/json" \\\n -d \'{"input": "Hello from ZONOS3-Mini!"}\' --output output.wav',n:'# github.com/Zyphra/ZONOS3-Mini\nservers/mlx # Apple Silicon\nservers/ggml # CPU, CUDA, Metal or Vulkan, no Python at runtime\nservers/web # in-browser WebGPU build',c:'cloud.zyphra.com/models/zyphra/ZONOS3-Mini\n# Hosted on NVIDIA H200s'};
function code(k){$('#code').textContent=C[k];$$('#dgrid .dc').forEach(function(x){x.classList.toggle('on',x.dataset.c===k)});rs()}
$$('#dgrid .dc').forEach(function(x){x.onclick=function(){code(x.dataset.c)}});code('b');
window.addEventListener('load',rs);window.addEventListener('resize',rs);setTimeout(rs,300);
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(e){if(e.data&&e.data.type==='z3m-h'){var f=document.getElementById('z3m-frame');if(f&&e.source===f.contentWindow){f.style.height=e.data.h+'px';}}});

 How does ZONOS3-Mini perform on benchmarks? 

 Zyphra evaluated the model on its new ZTTS2-Eval benchmark. It covers 35 languages of clean read speech and 20 languages of in-the-wild recordings. A Capability Index uses item response theory over 420 items. 

 ZONOS3-Mini in speaker-embedding mode scores 66.2 on that index. Fish Audio S2 Pro scores 61.7 and MOSS-TTS v1.5 scores 60.2. On the clean set, ZONOS3-Mini posts 7.79 WER and 83.4 speaker similarity. 

 There are caveats. Zyphra built and ran the benchmark. Reference-clip mode scores only 44.7 on the index. Its clean-set MSR-UTMOS quality score of 3.07 trails Fish S2 Pro (3.16) and Qwen3-TTS 1.7B (3.54). 

 ZONOS3-Mini vs other open-source TTS models 

 Metrics ZONOS3-Mini Fish Audio S2 Pro MOSS-TTS v1.5 Qwen3-TTS 1.7B Total params 800M 5B (4B Slow AR + 400M Fast AR) 8B 1.7B Active params ~100M (MoE) Not disclosed Not disclosed Not disclosed License Apache 2.0 Fish Audio Research License (commercial use needs separate license) Apache 2.0 Apache 2.0 Codec frame rate 15 Hz ~21 Hz Not disclosed 12.5 FPS Languages No official list (evaluated on 35) 80+ 31 10 Official browser runtime Yes, WebGPU Not disclosed Not disclosed Not disclosed Reported latency 80 ms TTFA, 1 H100, 8 concurrent ~100 ms TTFA, 1 H200 Not disclosed 97 ms end-to-end ZTTS2 Capability Index* 66.2 61.7 60.2 37.7 Clean WER* (lower is better) 7.79 11.06 11.01 25.55 Clean speaker similarity* 83.4 81.2 82.9 69.6 Clean MSR-UTMOS* 3.07 3.16 3.04 3.54 

 *From Zyphra’s ZTTS2-Eval explorer , all-language set. ZONOS3-Mini in speaker-embedding mode. Run by Zyphra, not independently verified. Latency figures use different GPUs and are not directly comparable. 

 How can developers deploy ZONOS3-Mini? 

 There are 4 official paths, per the GitHub repository : 

 Browser: The WebGPU playground runs fully on your GPU, with no install or server. 

 NVIDIA servers: SGLang-Omni serves an OpenAI-compatible /v1/audio/speech endpoint with streaming. 

 Native: An MLX server for Apple Silicon, and a C++/ggml server and CLI for CPU, CUDA, Metal or Vulkan. 

 Hosted: Zyphra Cloud , served on NVIDIA H200s. 

 Key Takeaways 

 ZONOS3-Mini is an 800M-parameter MoE TTS model with ~100M active parameters. 

 Apache 2.0 weights; runs in-browser via WebGPU, plus MLX, ggml and SGLang. 

 Tops Zyphra’s open-model Capability Index at 66.2, ahead of Fish S2 Pro. 

 80 ms time to first audio on one H100; under 570 ms on a Pixel 9 browser. 

 All benchmarks are self-reported; reference-clip cloning scores much lower. 

 Check out the blog post , model weights , GitHub repo and ZTTS2-Eval benchmark . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters appeared first on MarkTechPost .
