---
id: "83d109159117bc7a"
title: "Edge0 Releases Audio8-TTS-Realistic, a 0.6B Voice Cloning TTS Model"
url: "https://marktechpost.com/2026/10/29/edge0-audio8-tts-realistic-0-6b-voice-cloning"
link: "https://marktechpost.com/2026/10/29/edge0-audio8-tts-realistic-0-6b-voice-cloning"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-30T05:02:52Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Edge0 has released Audio8-TTS-Realistic , an open-weight text-to-speech model for zero-shot voice cloning. Audio8-TTS-Realistic is a 0.6B-parameter model that clones a voice from 1 reference clip and transcript. It supports 23 languages, 12 more than its predecessor. The weights and code ship under Apache 2.0 . For developers, the catch is competitive multilingual accuracy at a size that is…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Generative AI", "Harness", "Language Model", "New Releases"]
orgs: ["China", "Apple", "OpenAI", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "products & launches", "agents & coding"]
content_source: "summary"
word_count: 1403
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Edge0 Releases Audio8-TTS-Realistic, a 0.6B Voice Cloning TTS Model

MarkTechPost · Asif Razzaq · 2026-10-30

Edge0 has released Audio8-TTS-Realistic , an open-weight text-to-speech model for zero-shot voice cloning. Audio8-TTS-Realistic is a 0.6B-parameter model that clones a voice from 1 reference clip and transcript. It supports 23 languages, 12 more than its predecessor. The weights and code ship under Apache 2.0 . For developers, the catch is competitive multilingual accuracy at a size that is cheap to fine-tune and serve. 

 TL;DR 

 Size: 601M main-model parameters (codec excluded); up to 2,048 packed text/audio positions of context. 

 Runs on: a CUDA GPU is recommended; smoke-tested on NVIDIA H20 in BF16. The paper reports 1.1 to 1.2 GiB peak memory on an Apple M2 CPU (INT4 ONNX). No Realistic ONNX export is public yet. 

 Performance: ahead of larger open models on CV3, behind 4B-class models on MiniMax. 

 Best: 4.86% average CV3 error across 9 languages, versus 7.73% for Qwen3-TTS-1.7B. 

 Worst: 48.57% WER on Thai (CV3) and 31.35% CER on Cantonese (MiniMax). 

 What is Audio8-TTS-Realistic? 

 It is the second 0.6B release in Edge0’s Audio8 TTS family. It builds on Audio8-TTS-Preview-0.6b and keeps the same Transformers inference interface. The repository bundles the checkpoint, a 44.1 kHz neural audio codec, tokenizer, processor and custom code. It can also generate speech without a reference voice. 

 New languages are Arabic, Finnish, Hindi, Indonesian, Malay, Norwegian, Portuguese, Russian, Swedish, Thai, Turkish and Vietnamese. 

 How does the architecture work? 

 The model uses a dual-autoregressive (DualAR) design inspired by Fish Audio S2 Pro . According to the technical research report , the slow branch is built on Qwen2.5 0.5B. It has 24 layers at width 896 and runs at about 21.5 frames per second. Each step predicts text tokens plus the first audio codebook. 

 A shallow 4-layer fast branch then predicts the remaining 9 codebooks in parallel. Sequential compute therefore happens only at the frame level. 

 How does Edge0 train for realism? 

 The team argues that word error rate (WER) and speaker similarity (SIM) miss rhythm, pauses and timing. A model can score well on both and still sound synthetic. 

 Training runs in 3 stages: 

 Multilingual supervised fine-tuning (SFT). 

 GRPO with a combined reward: 0.7 weight on WER, 0.3 on SIM. 

 GRPO guided by a learned realism critic. 

 The critic scores each output against a matched human recording of the same sentence. It was trained on a quality ladder built from 6 open-source TTS systems. These were ranked in a private blind listening study, with human recordings at the top. Synthetic pause compression adds finer rungs to the ladder. 

 An identity-erasure loss stops the critic from rewarding generator fingerprints. The critic head has about 3M parameters on top of a frozen WavLM-large encoder. A duration penalty also kicks in beyond 1.35x the reference length. This blocks the policy from gaming the critic with slower speech. 

 The final stage used only Chinese and English prompts. It still improved both aggregate metrics on the 13 lower-resource languages. Their error fell from 22.53% to 20.77%, and SIM rose from 0.637 to 0.679. 

 Step through</button>
 </div>
 <div id="a8-stage"></div>
 <p class="note">The realism stage used only Chinese and English prompts, yet improved both metrics on the 13 additional languages. Source: technical report, Table 1.</p>
 </div>

 <div class="pn" data-p="bench">
 <div class="ctrl">
 <button class="btn on" data-b="cv3">CV3 (9 langs)</button>
 <button class="btn" data-b="mm">MiniMax (24 langs)</button>
 <button class="btn" data-b="seed">Seed-TTS EN/ZH</button>
 </div>
 <div id="a8-bench"></div>
 <p class="note" id="a8-bnote"></p>
 </div>

 <div class="pn" data-p="lang">
 <div class="ctrl">
 <button class="btn on" data-l="az">A to Z</button>
 <button class="btn" data-l="best">Best first</button>
 <button class="btn" data-l="worst">Worst first</button>
 </div>
 <div class="lg" id="a8-lang"></div>
 <p class="note">CV3 error rate per language (CER for Chinese, Japanese, Korean; WER otherwise). 500 items each. Shorter bar is better.</p>
 </div>

 <div class="pn" data-p="run">
 <p><b>Transformers</b> (PyTorch 2.5+, Transformers 4.57+, CUDA GPU recommended):</p>
<pre><code>model_id = "Edge0/Audio8-TTS-Realistic-0.6b"
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModel.from_pretrained(model_id, trust_remote_code=True)</code></pre>
 <p><b>Serving:</b> SGLang Omni adapter with paged attention, dynamic batching and an OpenAI-compatible <code>/v1/audio/speech</code> API. Throughput and streaming were not benchmarked by Edge0.</p>
 <p><b>CPU:</b> the paper reports 1.1 to 1.2 GiB peak on an Apple M2 with INT4 ONNX. The repo states no Realistic ONNX export is available yet.</p>
 </div>

 <div class="ft"><span>Numbers self-reported by Edge0; competitor figures from their own sources or Boson AI's evaluation.</span><a href="https://www.marktechpost.com" target="_blank" rel="noopener">© Marktechpost</a></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-a8tts');
function rs(){try{parent.postMessage({mtpEmbedHeight:R.offsetHeight+40,id:'mtp-a8tts'},'*')}catch(e){}}
function $$(s){return Array.prototype.slice.call(R.querySelectorAll(s))}
$$('.tab').forEach(function(t){t.onclick=function(){
 $$('.tab').forEach(function(x){x.setAttribute('aria-selected',x===t?'true':'false')});
 $$('.pn').forEach(function(p){p.classList.toggle('on',p.getAttribute('data-p')===t.getAttribute('data-t'))});
 if(t.getAttribute('data-t')==='bench')bench(curB);
 if(t.getAttribute('data-t')==='train')stage(curG);
 if(t.getAttribute('data-t')==='lang')lang(curL);
 setTimeout(rs,60);};});
/* architecture */
var D=['A reference clip and its exact transcript condition the model. The model can also generate speech without a reference.',
'The slow branch is built on Qwen2.5 0.5B. Once per audio frame it predicts text tokens plus the first of 10 codebooks.',
'A 4-layer fast branch reads the slow hidden state and predicts the remaining 9 codebooks in parallel, adding no extra sequential steps.',
'The bundled codec turns 10 codebooks of 4,096 entries per frame back into a 44.1 kHz waveform. It is excluded from the 0.6B count.'];
var det=R.querySelector('#a8-detail');det.textContent=D[0];
$$('.blk').forEach(function(b){b.onclick=b.onmouseenter=function(){$$('.blk').forEach(function(x){x.classList.toggle('on',x===b)});det.textContent=D[+b.getAttribute('data-d')]};});
var F=R.querySelector('#a8-frames'),N=16,html='';
for(var i=0;i<N;i++){html+='<div class="fr">';for(var c=0;c<10;c++)html+='<div class="cb"></div>';html+='</div>'}
F.innerHTML=html;var fr=$$('.fr'),k=0;
setInterval(function(){var col=fr[k%N].children;
 if(k%N===0)fr.forEach(function(f){Array.prototype.forEach.call(f.children,function(x){x.className='cb'})});
 col[0].className='cb s';setTimeout(function(){for(var c=1;c<10;c++)col[c].className='cb f'},180);k++;},420);
/* training */
var G=[[5.41,0.639,22.36,0.638],[5.01,0.643,22.53,0.637],[4.86,0.661,20.77,0.679]],curG=0;
var LB=['CV3 error % (9 langs)','CV3 SIM','Extra 13 langs error %','Extra 13 langs SIM'],MX=[25,1,25,1];
function stage(g){curG=g;$$('.stp').forEach(function(s){s.classList.toggle('on',+s.getAttribute('data-s')<=g)});
 $$('[data-g]').forEach(function(b){b.classList.toggle('on',+b.getAttribute('data-g')===g)});
 var h='';for(var i=0;i<4;i++){h+='<div class="mrow"><span class="lab">'+LB[i]+'</span><div class="trk"><div class="bar me" data-w="'+(G[g][i]/MX[i]*100)+'"></div></div><span class="val">'+(i%2?G[g][i].toFixed(3):G[g][i].toFixed(2)+'%')+(g?'<br><small style="color:#9a9a9f">'+((G[g][i]-G[0][i])>0?'+':'')+(G[g][i]-G[0][i]).toFixed(i%2?3:2)+' vs SFT</small>':'')+'</span></div>'}
 var el=R.querySelector('#a8-stage');el.innerHTML=h;grow(el);setTimeout(rs,60);}
$$('[data-g]').forEach(function(b){b.onclick=function(){stopP();stage(+b.getAttribute('data-g'))}});
var P=null;function stopP(){if(P){clearInterval(P);P=null;R.querySelector('#a8-play').textContent=' Step through'}}
R.querySelector('#a8-play').onclick=function(){if(P){stopP();return}var g=0;stage(0);this.textContent='■ Stop';P=setInterval(function(){g++;if(g>2){stopP();return}stage(g)},1500)};
function grow(el){requestAnimationFrame(function(){requestAnimationFrame(function(){Array.prototype.forEach.call(el.querySelectorAll('[data-w]'),function(b){b.style.width=b.getAttribute('data-w')+'%'})})})}
/* benchmarks */
var B={cv3:{max:9,rows:[['Higgs TTS 3 (~4B)',4.41],['Audio8-Realistic (0.6B)',4.86,1],['VoxCPM2 (2B)',5.35],['CosyVoice3 (1.5B)',6.89],['Qwen3-TTS (1.7B)',7.73]],n:'CV3 macro-average error, excluding hard subsets. Higgs and Qwen3-TTS figures from Boson AI evaluation; VoxCPM2 and CosyVoice3 from the VoxCPM repo.'},
mm:{max:30,rows:[['Higgs TTS 3 (~4B)',2.74],['Audio8-Realistic (0.6B)',5.89,1],['Qwen3-TTS (1.7B)',27.41]],n:'MiniMax 24-language average, including languages outside each model\u0027s supported list. Qwen3-TTS supports 10 of the 24.'},
seed:{max:2,rows:[['Qwen3-TTS (1.7B)',1.01],['Higgs TTS 3 (~4B)',1.11],['Audio8-Realistic (0.6B)',1.25,1],['VoxCPM2 (2B)',1.41],['CosyVoice3 (1.5B)',1.67]],n:'Average of Seed-TTS English WER and Chinese CER, excluding hard Chinese. Lower is better.'}},curB='cv3';
function bench(k){curB=k;$$('[data-b]').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-b')===k)});
 var d=B[k],h='';d.rows.forEach(function(r){h+='<div class="mrow"><span class="lab"'+(r[2]?' style="color:#fff!important;font-weight:700"':'')+'>'+r[0]+'</span><div class="trk"><div class="bar'+(r[2]?' me':'')+'" data-w="'+(r[1]/d.max*100)+'"'+(r[2]?'':' style="background:#55555b!important"')+'></div></div><span class="val">'+r[1].toFixed(2)+'%</span></div>'});
 var el=R.querySelector('#a8-bench');el.innerHTML=h;R.querySelector('#a8-bnote').textContent=d.n;grow(el);setTimeout(rs,60);}
$$('[data-b]').forEach(function(b){b.onclick=function(){bench(b.getAttribute('data-b'))}});
/* languages */
var L=[['Chinese',1.81],['English',2.91],['Japanese',7.51],['Korean',4.80],['German',3.20],['French',7.94],['Spanish',3.39],['Italian',4.93],['Russian',7.26],['Arabic',21.10],['Finnish',32.28],['Hindi',21.71],['Indonesian',13.74],['Malay',17.80],['Dutch',10.87],['Norwegian',17.96],['Polish',19.23],['Portuguese',6.87],['Swedish',19.25],['Thai',48.57],['Turkish',12.57],['Vietnamese',28.11]],curL='az';
function col(v){return v<8?'#f5f5f4':v<20?'#a1a1a6':'#5c5c62'}
function lang(m){curL=m;$$('[data-l]').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-l')===m)});
 var a=L.slice();if(m==='az')a.sort(function(x,y){return x[0]<y[0]?-1:1});if(m==='best')a.sort(function(x,y){return x[1]-y[1]});if(m==='worst')a.sort(function(x,y){return y[1]-x[1]});
 var h='';a.forEach(function(r){h+='<div class="lc"><div class="t"><span>'+r[0]+'</span><em>'+r[1].toFixed(2)+'%</em></div><div class="mini"><i data-w="'+(r[1]/50*100)+'" style="background:'+col(r[1])+'"></i></div></div>'});
 var el=R.querySelector('#a8-lang');el.innerHTML=h;grow(el);setTimeout(rs,60);}
$$('[data-l]').forEach(function(b){b.onclick=function(){lang(b.getAttribute('data-l'))}});
window.addEventListener('load',rs);window.addEventListener('resize',rs);setTimeout(rs,300);rs();
})();
</script>
"> 
 window.addEventListener("message",function(e){if(e.data&&e.data.id==="mtp-a8tts"&&e.data.mtpEmbedHeight){var f=document.getElementById("mtp-a8tts-frame");if(f)f.style.height=e.data.mtpEmbedHeight+"px";}}); 

 How does it perform on benchmarks? 

 All numbers below are self-reported error rates, where lower is better. 

 Seed-TTS (English/Chinese): 1.25% average error, SIM 0.704. 

 CV3 (9 languages): 4.86% average error, SIM 0.661. 

 MiniMax (24 languages): 5.89% average error, SIM 0.754. 

 On CV3, Audio8 beats VoxCPM2 (5.35%), CosyVoice3-1.5B (6.89%) and Qwen3-TTS-1.7B (7.73%). On MiniMax, Qwen3-TTS-1.7B scores 27.41%, but it officially supports only 10 of the 24 test languages. 

 Larger models still lead elsewhere. Higgs TTS 3 reports 4.41% on CV3 and 2.74% on MiniMax. Qwen3-TTS-1.7B averages 1.01% on Seed-TTS. Edge0 itself calls its table a reference comparison, since evaluation pipelines and text normalization differ. 

 How does it compare with other open TTS models? 

 Feature Audio8-TTS-Realistic Qwen3-TTS-12Hz-1.7B-Base VoxCPM2 Higgs TTS 3 Size 0.6B (excl. codec) 1.7B 2B ~4B backbone License Apache 2.0 Apache 2.0 Apache 2.0 Research and non-commercial Languages 23 10 30 100+ Output sample rate 44.1 kHz Not disclosed 48 kHz 24 kHz Seed-TTS EN WER 1.46% 1.24% 1.84% Not disclosed Seed-TTS ZH CER 1.03% 0.77% 0.97% Not disclosed CV3 avg error (9 langs) 4.86% 7.73% (Boson AI eval) 5.35% 4.41% MiniMax avg error (24 langs) 5.89% 27.41% (Boson AI eval) Not disclosed 2.74% Hardware noted CUDA GPU; INT4 M2 CPU in paper GPU, FlashAttention 2 ~8 GB VRAM 1x H100 serving tests 

 VoxCPM2’s CV3 average is computed from its per-language table. 

 How do you deploy it? 

 Install PyTorch 2.5+ and Transformers 4.57+, then load with trust_remote_code=True . Voice cloning needs a clean reference clip and its exact transcript. The GitHub repo adds a CLI, batching and supervised fine-tuning scripts. 

 For GPU serving, an SGLang Omni adapter provides paged attention, dynamic batching and an OpenAI-compatible /v1/audio/speech API. Edge0 notes throughput and streaming were not benchmarked. A free Playground runs on Hugging Face ZeroGPU. 

 Key Takeaways 

 601M parameters, 23 languages, Apache 2.0 weights. 

 A learned realism critic drives the final GRPO stage. 

 4.86% CV3 error beats Qwen3-TTS-1.7B and VoxCPM2. 

 4B-class Higgs TTS 3 still leads on CV3 and MiniMax. 

 Lower-resource languages remain weak, with Thai near 49% WER. 

 Check out the Paper , Model Weights , Repo and Samples . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Edge0 Releases Audio8-TTS-Realistic, a 0.6B Voice Cloning TTS Model appeared first on MarkTechPost .
