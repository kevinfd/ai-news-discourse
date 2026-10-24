---
id: "92b34237ebd94dd6"
title: "NVIDIA Releases Nemotron 3.5 Bolt E4B 4GB: An Open Small Language Model for Local Voice Agents, Game Characters and Robots"
url: "https://marktechpost.com/2026/10/23/nvidia-nemotron-3-5-bolt-e4b-4gb"
link: "https://marktechpost.com/2026/10/23/nvidia-nemotron-3-5-bolt-e4b-4gb"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-24T03:56:29Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA has just released Nemotron 3.5 Bolt E4B 4GB , an open small language model for fast conversational agents. It targets voice assistants, game NPCs and robot interfaces running locally on RTX, Jetson and Spark hardware. The model is post-trained from Google’s Gemma 4 E4B using reinforcement learning only. For developers, this is agent behavior in about 4GB of VRAM. That leaves room for…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Enterprise AI", "For Devs", "Harness"]
orgs: ["Nvidia", "Google"]
topics: ["chips & infrastructure", "models & research", "agents & coding", "robotics & autonomy"]
content_source: "summary"
word_count: 1517
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Releases Nemotron 3.5 Bolt E4B 4GB: An Open Small Language Model for Local Voice Agents, Game Characters and Robots

MarkTechPost · Asif Razzaq · 2026-10-24

NVIDIA has just released Nemotron 3.5 Bolt E4B 4GB , an open small language model for fast conversational agents. It targets voice assistants, game NPCs and robot interfaces running locally on RTX, Jetson and Spark hardware. The model is post-trained from Google’s Gemma 4 E4B using reinforcement learning only. For developers, this is agent behavior in about 4GB of VRAM. That leaves room for speech and vision models. 

 TL;DR 

 Size: 8B total parameters , 4B effective, 64K context. 

 Runs on: GeForce RTX, Jetson, RTX Spark and DGX Spark. The Q4_K_M build used 3.1 to 4.3 GB VRAM on RTX in NVIDIA tests. 

 Performance: Top score on 15 of 21 benchmarks against Gemma 4 E4B, Qwen3.5-4B and Nemotron 3 Nano 4B (NVIDIA-measured). 

 Best: IHEval 84.8, versus 67.0 for Gemma 4 E4B and 60.6 for Qwen3.5-4B. 

 Worst: Tau2-Bench 55.1, about 20 points behind Qwen3.5-4B at 75.1. 

 What is Nemotron 3.5 Bolt E4B? 

 Nemotron 3.5 Bolt E4B is a small language model from NVIDIA that powers local conversational agents. It combines natural dialogue with multi-turn tool calling. NVIDIA lists 3 target workloads: device and voice assistants, interactive characters, and embedded or industrial agents. 

 The research report shows a Reachy Mini robot running on a Jetson Orin Nano 8GB. In that demo, Cosmos 3 Edge handles vision while Bolt handles speech replies and tool calls. NVIDIA team also calls Bolt the third-generation small model for NVIDIA ACE game characters . 

 Core features from the launch post : 

 Multi-turn tool use, with guidance for asynchronous tool calls. 

 A conversational_mode flag for short, speech-ready replies. 

 Configurable reasoning, plus a runtime thinking budget to cap latency. 

 64K context for history, tool definitions and application state. 

 How was Bolt E4B trained? 

 NVIDIA skipped supervised fine-tuning entirely. As per the research report , SFT improved tool calling but hurt Gemma’s conversational quality and verbosity. Instead, the research team used RLVR and RLHF through NeMo-RL and NeMo-Gym . 

 Every training sample ran in both reasoning and non-reasoning modes. Each batch kept a 2:1 ratio of non-reasoning to reasoning samples. Length penalties in the GenRM environment stopped answers from growing during training. The datasets and the full recipe are public. 

 For deployment, NVIDIA quantized the BF16 checkpoint to Q4_K_M with importance-matrix calibration. Calibration used about 1M tokens of RL rollouts. The release also ships a DFlash drafter for speculative decoding. On an RTX 5070, Bolt with DFlash reached 272.6 tokens/s. Gemma 4 E4B with its MTP drafter reached 225.9 tokens/s, so Bolt is 1.21x faster. 

 How does Nemotron 3.5 Bolt E4B perform on benchmarks? 

 NVIDIA grouped 21 benchmarks into 5 capability areas. All scores here are BF16, measured by NVIDIA in its own NeMo-Gym harness. Bolt led 15 of 21 rows in reasoning mode. 

 NVIDIA also reports roughly 40% higher average scores than Nemotron 3 Nano 4B. It claims up to 80% fewer output tokens in reasoning-enabled comparisons. Separately, Scale Labs ranked Bolt first among small models on MultiChallenge at 56.03%, per an X post . 

 </div>
 <div class="node">RLVR + RLHF</div><div class="arr"> </div>
 <div class="node">Verbosity control</div><div class="arr"> </div>
 <div class="node">Q4_K_M imatrix</div><div class="arr"> </div>
 <div class="node">DFlash drafter</div>
 </div>
 <div class="stepbox">
 <div class="stepn" id="mtp-sn">Step 1 of 5</div>
 <div class="stept" id="mtp-st"></div>
 <p class="stepd" id="mtp-sd"></p>
 </div>
 <div class="ctl">
 <button class="btn ghost" id="mtp-prev">Back</button>
 <div class="dots"><span class="dot on"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
 <button class="btn" id="mtp-next">Next</button>
 </div>
 </div>

 <div class="pane" data-p="2">
 <div class="chips" id="mtp-chips"></div>
 <div id="mtp-bars"></div>
 <div class="note">BF16 scores measured by NVIDIA in its NeMo-Gym harness. Vendor-reported scores may differ. Green value marks the best in each row.</div>
 </div>

 <div class="pane" data-p="3">
 <div class="devs" id="mtp-devs"></div>
 <div class="meters">
 <div class="meter"><div class="mv" id="mtp-vram">0</div><div class="mu">VRAM (GB)</div><div class="mbar"><div class="mfill" id="mtp-vb"></div></div></div>
 <div class="meter"><div class="mv" id="mtp-ttft">0</div><div class="mu">Time to first token (ms)</div><div class="mbar"><div class="mfill" id="mtp-tb"></div></div></div>
 <div class="meter"><div class="mv" id="mtp-tps">0</div><div class="mu">Generation (tokens/s)</div><div class="mbar"><div class="mfill" id="mtp-pb"></div></div></div>
 </div>
 <div class="verdict" id="mtp-verdict"></div>
 <div class="note">Q4_K_M, llama.cpp (CUDA), batch size 1, 3K input / 50 output tokens, no cached context. Source: NVIDIA.</div>
 </div>

 <div class="pane" data-p="4">
 <div class="two">
 <div class="col w"><h4>Where it wins</h4><ul>
 <li>IHEval 84.8 vs 67.0 (Gemma 4 E4B) and 60.6 (Qwen3.5-4B)</li>
 <li>MultiChallenge 53.1, top of the 4 models</li>
 <li>RelyToolBench 63.2 vs 43.3 for Qwen3.5-4B</li>
 <li>1.21x Gemma's MTP throughput with DFlash on RTX 5070</li>
 </ul></div>
 <div class="col l"><h4>Where it trails</h4><ul>
 <li>Tau2-Bench 55.1 vs 75.1 for Qwen3.5-4B</li>
 <li>RULER 64K 87.0 vs 95.1 for Qwen3.5-4B</li>
 <li>MMMU-Pro Vision 42.0 vs 47.6 for Gemma 4 E4B</li>
 <li>5,785 ms first token on Jetson Orin Nano at 3K input</li>
 </ul></div>
 </div>
 </div>

 <div class="ft"><span>Sources: <a href="https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/" target="_blank" rel="noopener">NVIDIA blog</a> · <a href="https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf" target="_blank" rel="noopener">Tech report</a> · <a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16" target="_blank" rel="noopener">Model card</a></span><span class="brand">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-bolt-e4b');
function post(){try{var h=R.offsetHeight+40;parent.postMessage({mtpEmbed:'bolt-e4b',height:h},'*');}catch(e){}}
var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
tabs.forEach(function(t){t.addEventListener('click',function(){var i=+t.dataset.t;tabs.forEach(function(x){x.classList.toggle('on',x===t)});panes.forEach(function(p){p.classList.toggle('on',+p.dataset.p===i)});if(i===2)drawBars();if(i===3)showDev(curDev);setTimeout(post,60);});});
R.querySelectorAll('.rv').forEach(function(b){b.addEventListener('click',function(){b.classList.toggle('open');setTimeout(post,380);});});
var steps=[
['Start from Gemma 4 E4B','Bolt begins as Google’s Gemma-4-E4B-it: 8B total parameters, 4B effective. NVIDIA keeps the backbone and changes behavior.'],
['RL-only post-training','RLVR and RLHF run in NeMo-RL and NeMo-Gym. Environments cover tool calling, instruction following, instruction hierarchy and structured outputs. SFT was dropped because it hurt conversational quality.'],
['Train both modes, control length','Every sample runs with reasoning on and off, at a 2:1 non-reasoning to reasoning ratio. Group-relative length penalties keep answers short. NVIDIA reports up to 80% fewer output tokens than peers.'],
['Quantize to Q4_K_M','The BF16 checkpoint is quantized with llama.cpp using importance-matrix calibration on about 1M tokens of RL rollouts. This build targets a ~4GB VRAM envelope.'],
['Speed up with DFlash','A parallel drafter proposes 7 tokens in one pass; Bolt verifies them. On RTX 5070 it reaches 272.6 tokens/s vs 225.9 for Gemma with MTP, a 1.21x gain.']];
var si=0,nodes=R.querySelectorAll('.node'),arrs=R.querySelectorAll('.arr'),dots=R.querySelectorAll('.dot');
function step(){document.getElementById('mtp-sn').textContent='Step '+(si+1)+' of 5';document.getElementById('mtp-st').textContent=steps[si][0];document.getElementById('mtp-sd').textContent=steps[si][1];
nodes.forEach(function(n,i){n.classList.toggle('on',i<=si)});arrs.forEach(function(a,i){a.classList.toggle('on',i<si)});dots.forEach(function(d,i){d.classList.toggle('on',i===si)});
document.getElementById('mtp-prev').disabled=si===0;document.getElementById('mtp-next').textContent=si===4?'Restart':'Next';setTimeout(post,60);}
document.getElementById('mtp-prev').addEventListener('click',function(){if(si>0){si--;step();}});
document.getElementById('mtp-next').addEventListener('click',function(){si=si===4?0:si+1;step();});
step();
var M=['Bolt E4B','Nemotron 3 Nano 4B','Qwen3.5-4B','Gemma 4 E4B'];
var B={'Conversation':[['MultiChallenge','consistency across turns',[53.1,35.3,51.8,42.1]],['RoleMRC','role identity adherence',[80.6,47.0,65.8,74.6]],['EQ-Bench v3','emotional intelligence',[39.4,19.3,32.9,41.1]]],
'Tool use':[['BFCL-v3','correct tools and arguments',[68.5,61.1,70.9,66.4]],['Tau2-Bench','multi-turn customer tasks',[55.1,29.2,75.1,38.5]],['When2Call-MT','call, clarify or abstain',[63.4,27.7,37.8,62.9]]],
'Instruction':[['IHEval','instruction hierarchy',[84.8,51.3,60.6,67.0]],['IFBench','precise output constraints',[63.8,60.1,58.9,42.8]],['StructEval-T','valid structured outputs',[80.4,63.5,76.0,79.3]]],
'Context':[['RULER 64K','retrieval and reasoning',[87.0,91.5,95.1,86.5]],['LongBench v2 (48K)','long prompts',[50.5,31.4,59.9,49.3]],['LongMemEval','recall across conversations',[72.1,25.2,66.8,70.9]]],
'Grounding':[['GaRAGe','facts from supplied sources',[42.6,25.2,24.7,34.7]],['RAGTruth','avoiding unsupported claims',[77.6,71.4,75.6,77.0]],['RelyToolBench','tool grounding',[63.2,41.2,43.3,61.6]]]};
var cat='Conversation',chips=document.getElementById('mtp-chips');
Object.keys(B).forEach(function(k){var c=document.createElement('button');c.className='chip'+(k===cat?' on':'');c.textContent=k;c.addEventListener('click',function(){cat=k;chips.querySelectorAll('.chip').forEach(function(x){x.classList.toggle('on',x===c)});drawBars();});chips.appendChild(c);});
function drawBars(){var box=document.getElementById('mtp-bars');box.innerHTML='';B[cat].forEach(function(b){var mx=Math.max.apply(null,b[2]);var d=document.createElement('div');d.className='bench';var h='<div class="bname">'+b[0]+' <span>'+b[1]+'</span></div>';
b[2].forEach(function(v,i){h+='<div class="row'+(i===0?' bolt':'')+(v===mx?' top':'')+'"><div class="m">'+M[i]+'</div><div class="track"><div class="fill" data-w="'+v+'"></div></div><div class="v">'+v.toFixed(1)+'</div></div>';});
d.innerHTML=h;box.appendChild(d);});requestAnimationFrame(function(){requestAnimationFrame(function(){box.querySelectorAll('.fill').forEach(function(f){f.style.width=f.dataset.w+'%';});});});setTimeout(post,60);}
var D=[['RTX 5070','12GB',3.5,548,133.4,'Fast enough for live voice turns, with VRAM left for speech models.'],['RTX Spark','32GB',3.1,930,67.0,'Lowest VRAM use in NVIDIA’s tests, under 1 second to first token.'],['Jetson AGX Orin','32GB',4.2,3687,24.0,'Workable for robots and kiosks; expect multi-second first replies at 3K input.'],['Jetson Orin Nano','8GB',4.2,5785,15.5,'Fits the 8GB board, but first-token latency is the bottleneck at 3K input.']];
var curDev=0,devs=document.getElementById('mtp-devs');
D.forEach(function(d,i){var b=document.createElement('button');b.className='dev'+(i===0?' on':'');b.innerHTML=d[0]+'<small>'+d[1]+'</small>';b.addEventListener('click',function(){curDev=i;devs.querySelectorAll('.dev').forEach(function(x){x.classList.toggle('on',x===b)});showDev(i);});devs.appendChild(b);});
function count(el,to,dec){var s=performance.now(),dur=700;function f(t){var p=Math.min(1,(t-s)/dur);p=1-Math.pow(1-p,3);var v=to*p;el.textContent=dec?v.toFixed(dec):Math.round(v).toLocaleString('en-US');if(p<1)requestAnimationFrame(f);}requestAnimationFrame(f);}
function showDev(i){var d=D[i];count(document.getElementById('mtp-vram'),d[2],1);count(document.getElementById('mtp-ttft'),d[3],0);count(document.getElementById('mtp-tps'),d[4],1);
document.getElementById('mtp-vb').style.width=(d[2]/6*100)+'%';document.getElementById('mtp-tb').style.width=(d[3]/6000*100)+'%';document.getElementById('mtp-pb').style.width=(d[4]/140*100)+'%';document.getElementById('mtp-verdict').textContent=d[5];setTimeout(post,60);}
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
"> 
 (function(){window.addEventListener("message",function(e){var d=e.data;if(d&&d.mtpEmbed==="bolt-e4b"&&d.height){var f=document.getElementById("mtp-bolt-e4b-frame");if(f&&e.source===f.contentWindow){f.style.height=d.height+"px";}}});})(); 

 Bolt does not win everywhere. Qwen3.5-4B leads on Tau2-Bench (75.1 vs 55.1) and RULER 64K (95.1 vs 87.0). It also leads LongBench v2 (59.9 vs 50.5) and BFCL-v3 (70.9 vs 68.5). Gemma 4 E4B keeps a narrow edge on EQ-Bench v3 (41.1 vs 39.4). 

 How does Bolt E4B compare with other small models? 

 Feature Nemotron 3.5 Bolt E4B Gemma 4 E4B Qwen3.5-4B Nemotron 3 Nano 4B Parameters 8B total, 4B effective 8B with embeddings, 4.5B effective 4B (language model) 3.97B Architecture Gemma 4 E4B, RL post-trained Dense with Per-Layer Embeddings Gated DeltaNet + attention hybrid Mamba-2 + Transformer hybrid Context 64K 128K 262K 262K License OpenMDW-1.1 Apache 2.0 Apache 2.0 NVIDIA Nemotron Open Model License Inputs Text (card); NIM also accepts image and audio Text, image, audio Text, image, video Text IHEval* 84.8 67.0 60.6 51.3 MultiChallenge* 53.1 42.1 51.8 35.3 Tau2-Bench* 55.1 38.5 75.1 29.2 RULER 64K* 87.0 86.5 95.1 91.5 Availability Open weights; free API on build.nvidia.com Open weights Open weights Open weights 

 *Benchmark rows are NVIDIA-measured BF16 scores from the Bolt launch post . Vendor-reported scores differ. 

 What hardware does it run on? 

 NVIDIA measured the Q4_K_M build with llama.cpp at batch size 1. The figures below use 3K input and 50 output tokens. 

 Device VRAM (GB) Time to first token (ms) Tokens/s RTX 5070 (12GB) 3.5 548 133.4 RTX Spark (32GB) 3.1 930 67.0 Jetson AGX Orin (32GB) 4.2 3,687 24.0 Jetson Orin Nano (8GB) 4.2 5,785 15.5 

 The ‘4GB’ label describes a target memory envelope, not the file size. The Q4_K_M GGUF on Hugging Face is 6.18 GB. 

 Bolt is available on Hugging Face , Ollama , LM Studio, Unsloth and Jetson AI Lab . It also ships as an NVIDIA NIM and through the In-Game Inferencing SDK . 

 Key Takeaways 

 Gemma 4 E4B, post-trained by NVIDIA with RL only, no SFT. 

 Leads 15 of 21 agent benchmarks in NVIDIA’s own harness. 

 IHEval 84.8 is the standout; Tau2-Bench 55.1 is the weak spot. 

 ‘4GB’ is the VRAM target; the GGUF file is 6.18 GB. 

 Open weights, data and recipes under OpenMDW-1.1. 

 Check out the technical report , GGUF model , BF16 model and training recipe . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post NVIDIA Releases Nemotron 3.5 Bolt E4B 4GB: An Open Small Language Model for Local Voice Agents, Game Characters and Robots appeared first on MarkTechPost .
