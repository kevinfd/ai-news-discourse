---
id: "5ce3cacfb8a62ae2"
title: "OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime"
url: "https://marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime"
link: "https://marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T14:16:53Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "OpenAI and Cisco have released Shirudo , an open-source Linux runtime for defending live systems. Shirudo is an eBPF runtime that lets AI agents write temporary “shields” against known exploits. Shields block the vulnerable behavior while legitimate requests keep flowing. Teams get time to test and ship the real patch. The engineering came from Isovalent at Cisco , the team behind Cilium and…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "New Releases", "Software Engineering", "Staff"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 1449
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime

MarkTechPost · Asif Razzaq · 2026-11-24

OpenAI and Cisco have released Shirudo , an open-source Linux runtime for defending live systems. Shirudo is an eBPF runtime that lets AI agents write temporary “shields” against known exploits. Shields block the vulnerable behavior while legitimate requests keep flowing. Teams get time to test and ship the real patch. The engineering came from Isovalent at Cisco , the team behind Cilium and Tetragon. 

 TL;DR 

 Size: Software runtime, not a model. Code is pre-release . 

 Runs on: Linux on x86-64, arm64 and riscv64, with TPM 2.0 and a patched bpf-next kernel. The quickstart VM example uses 4 CPUs and 4G RAM. 

 Performance: No overhead or latency numbers published. One controlled exploit test is disclosed. 

 Best: A Codex-generated shield blocked Java4Shell (CVSS 9.2) on running Elasticsearch 9.5.5, with no restart. 

 Worst: Targets need a bpf-next kernel plus 5 carried patches not yet in bpf-next. No TPM-less mode. 

 Bottom line: Best: signed, TPM-attested mitigations agents can write in code. 

 What problem does Shirudo solve? 

 Patching takes time. OpenAI team notes that testing and deploying a fix can take days or weeks. Blocking a whole Linux operation is risky, because exploits and normal requests often share it. Shirudo targets that patch window. 

 How does Shirudo work? 

 Shirudo uses eBPF, which runs small verified programs at hooks inside the Linux kernel. The name is Japanese for “shield.” Isovalent calls it a rewrite of Tetragon , its 2022 eBPF security platform. 

 The design splits work across 2 roles: 

 Operator machine: a one-shot CLI, not a daemon. It builds and signs shields, then pushes them to an OCI registry. Signing code never reaches a target . 

 Target node: no persistent Shirudo daemon. Its control plane is an eBPF program loaded at boot. It pulls packages and verifies signatures before loading them. 

 A shield can do 3 things. It can block the code path a bug needs, replace vulnerable code, or add detection visibility. The docs call these packages upatches : small BPF C programs shipped as signed artifacts. 

 There is deliberately no policy DSL. The Linux Plumbers talk by Daniel Borkmann and John Fastabend says agents work better with code directly. 

 What does the agent loop look like? 

 Isovalent describes 4 stages, with Codex as the control plane: 

 Discovery: find bugs or ingest external disclosures. 

 Mitigation: build an exploit reproducer, pick a hook, and iterate until the shield works. 

 Rollout: push signed shields, monitored against a security score and app health. 

 Monitoring: a hit count tracks exploitation attempts against shielded bugs. 

 Operators approve shields before enforcement. Teams can also observe a shield’s impact before it blocks anything. 

 How is trust enforced? 

 The kernel checks each loader’s signature against a .bpf keyring. The eBPF verifier then checks program safety. A TPM 2.0 records every load and unload, and signs attestation evidence. The test bundle uses an ML-DSA-87 signing key, a post-quantum algorithm. Registry traffic uses TLS 1.3 with hybrid post-quantum key exchange. 

 Back</button><button class="btn" id="mtpS-next">Next </button></div>
 <p class="note">Sources: Isovalent technical post and Shirudo quickstart docs.</p>
 </div>

 <div class="pane">
 <div class="glass">
 <div style="font-weight:800;font-size:16px">Java4Shell (CVE-2026-114938) · CVSS 4.0 score 9.2</div>
 <div style="font-size:13.5px;margin-top:4px">Heap corruption in OpenJDK's Base64 decoder. Target: Elasticsearch 9.5.5, kept running.</div>
 <div class="tl" id="mtpS-tl"></div>
 </div>
 <div style="margin-top:12px"><button class="btn" id="mtpS-x">Send exploit input</button><button class="btn alt" id="mtpS-ok">Send normal Base64</button></div>
 <pre id="mtpS-log"><span class="pulse">Base64 guard installed on java.util.Base64$Decoder.decode0 (classfile)</span></pre>
 <p class="note">Log lines paraphrase the Isovalent test log. This shield was Java bytecode (an in-application guard), not a kernel eBPF program.</p>
 </div>

 <div class="pane">
 <div class="grid" id="mtpS-req"></div>
 <p class="note">Tap a card for detail. Source: Shirudo system requirements and carried kernel patches pages.</p>
 </div>

 <div class="pane">
 <div class="ink" style="overflow-x:auto">
 <table>
 <tr><th></th><th>Shirudo</th><th>Tetragon</th><th>Falco</th><th>KubeArmor</th></tr>
 <tr><td class="s">License</td><td>BSD-2-Clause</td><td>Apache-2.0</td><td>Apache-2.0</td><td>Apache-2.0</td></tr>
 <tr><td class="s">Blocks live</td><td>Yes</td><td>Yes, in-kernel</td><td>Detect and alert (per docs)</td><td>Yes, via LSMs</td></tr>
 <tr><td class="s">Authoring</td><td>Code, no DSL</td><td>TracingPolicy resource</td><td>YAML rules</td><td>Policy specs</td></tr>
 <tr><td class="s">Replaces code</td><td>Yes</td><td>Not disclosed</td><td>Not disclosed</td><td>Not disclosed</td></tr>
 <tr><td class="s">TPM-attested loads</td><td>Required</td><td>Not disclosed</td><td>Not disclosed</td><td>Not disclosed</td></tr>
 <tr><td class="s">Status</td><td>Pre-release</td><td>Open-sourced 2022</td><td>CNCF graduated</td><td>CNCF sandbox</td></tr>
 </table>
 </div>
 </div>

 <div class="ft"><span>Sources: openai.com, isovalent.com, docs.shirudo.dev, calif.io</span><span class="m">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-shirudo');
var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
function send(){try{parent.postMessage({mtpShirudoH:R.offsetHeight+40},'*')}catch(e){}}
tabs.forEach(function(t){t.addEventListener('click',function(){tabs.forEach(function(x){x.classList.remove('on')});panes.forEach(function(x){x.classList.remove('on')});t.classList.add('on');panes[+t.dataset.p].classList.add('on');if(t.dataset.p==='2')grow();setTimeout(send,60);setTimeout(send,500)})});
var S=[
['OPERATOR','1. Build','A one-shot CLI compiles a shield from code. There is no persistent daemon and no policy DSL.'],
['OPERATOR','2. Sign','The build helper signs the package. Signing code lives only on the operator, so it never reaches a target. The test bundle uses an ML-DSA-87 key.'],
['REGISTRY','3. Push','Signed packages go to an OCI registry. Registry traffic uses TLS 1.3 with hybrid post-quantum key exchange.'],
['TARGET','4. Pull and verify','The target pulls the package. The kernel checks the loader signature against the .bpf keyring, then the eBPF verifier checks safety.'],
['TARGET','5. Attach','The shield attaches to the running kernel or workload with no restart. It can block a code path, replace code, or add visibility.'],
['TARGET','6. Attest','TPM 2.0 extends a measurement register for each load or unload and signs evidence the operator verifies. A hit count tracks exploit attempts.']];
var i=0,dots=R.querySelector('#mtpS-dots'),box=R.querySelector('#mtpS-step');
S.forEach(function(){var d=document.createElement('div');d.className='dot';dots.appendChild(d)});
function draw(){box.innerHTML='<span class="who">'+S[i][0]+'</span><h4>'+S[i][1]+'</h4><p>'+S[i][2]+'</p>';box.style.animation='none';box.offsetHeight;box.style.animation='mtpS-fade .4s ease';dots.querySelectorAll('.dot').forEach(function(d,k){d.classList.toggle('on',k<=i)});send()}
R.querySelector('#mtpS-next').onclick=function(){i=(i+1)%S.length;draw()};
R.querySelector('#mtpS-prev').onclick=function(){i=(i+S.length-1)%S.length;draw()};draw();
var T=[['Oct 24','Calif.io finds bug with Codex',100],['Nov 17','Oracle ships the fix',100],['Nov 18','Shield blocks exploit on live node',100],['Nov 23','Shirudo released',100]];
var tl=R.querySelector('#mtpS-tl');
T.forEach(function(r,k){tl.insertAdjacentHTML('beforeend','<div class="tlrow"><b>'+r[0]+'</b><div style="flex:1"><div class="bar" data-w="100"></div></div><span style="flex:1.3">'+r[1]+'</span></div>')});
function grow(){tl.querySelectorAll('.bar').forEach(function(b,k){b.style.width='0';setTimeout(function(){b.style.width=b.dataset.w+'%'},120+k*250)})}
var log=R.querySelector('#mtpS-log'),base='Base64 guard installed on java.util.Base64$Decoder.decode0 (classfile)\n';
R.querySelector('#mtpS-x').onclick=function(){log.textContent=base+'> input: 64 x "A" + "="\nWARN rejected candidate: length=65 padding=1 remainder=1 alphabet=standard\nOK exploit failed · Elasticsearch still running';send()};
R.querySelector('#mtpS-ok').onclick=function(){log.textContent=base+'> input: valid Base64 payload\nOK decoded normally · request served';send()};
var Q=[['bpf-next kernel','Needs the signed-loader ABI. The test kernel reports 7.4.0-rc1-bpf-next+. No fallback for older kernels.'],
['5 carried patches','TPM command LSM hook, security.bpf xattr reads, sleepable inode hooks, trusted d_parent, remote mm LSM check. None in bpf-next yet.'],
['TPM 2.0','Required through /dev/tpmrm0. There is no TPM-less mode.'],
['systemd 256+','Plus a dracut initrd and a unified kernel image booted via systemd-stub.'],
['Architectures','x86-64, arm64 and riscv64 per the docs. Test VMs run only on x86-64 and arm64.'],
['Operator toolchain','clang and LLVM 23 with the BPF target, OpenSSL 3.5 or newer. Any Linux kernel works on the operator.']];
var g=R.querySelector('#mtpS-req');
Q.forEach(function(q){var c=document.createElement('div');c.className='glass req';c.innerHTML='<div class="t">'+q[0]+' ＋</div><div class="d">'+q[1]+'</div>';c.onclick=function(){c.classList.toggle('open');setTimeout(send,400)};g.appendChild(c)});
window.addEventListener('load',send);window.addEventListener('resize',send);setTimeout(send,300);
})();
</script>
" style="width:100%;height:600px;border:0;display:block;background:transparent;" loading="lazy" scrolling="no"> 

window.addEventListener('message',function(e){if(e.data&&e.data.mtpShirudoH){var f=document.getElementById('mtp-shirudo-frame');if(f&&e.source===f.contentWindow){f.style.height=e.data.mtpShirudoH+'px';}}});

 How did Shirudo perform against Java4Shell? 

 Java4Shell (CVE-2026-114938) is a heap corruption bug in OpenJDK’s Base64 decoder. It scores 9.2 on CVSS 4.0. It affects OpenJDK 17.0.6 and newer on x86-64 CPUs with AVX-512 VBMI. Calif.io found it on October 24 using Codex. Oracle shipped a fix on November 17. 

 Codex generated a guard on java.util.Base64$Decoder.decode0 . It was attached to a running Elasticsearch 9.5.5 node. The exploit input was rejected and the service stayed up. That is the only disclosed test. No false-positive rate or overhead figure was published. 

 Source note: OpenAI frames shields as eBPF. The Isovalent post says this specific shield was Java bytecode. The Java agent docs call such upatches an in-application mitigation, not a kernel boundary. Those docs also describe startup-time loading only, while the demo attached at runtime. 

 What do you need to run Shirudo? 

 Requirements are strict. Per the system requirements page : 

 A bpf-next kernel with the signed-loader ABI. The test kernel reports 7.4.0-rc1-bpf-next+. 

 5 carried kernel patches , none in bpf-next yet. 

 TPM 2.0, systemd 256 or newer, and a unified kernel image. 

 Operator: clang and LLVM 23, plus OpenSSL 3.5 or newer. 

 There is no fallback for older kernels. Developers can try the VM quickstart or the Isovalent lab . 

 How does Shirudo compare with other eBPF security tools? 

 Metrics Shirudo Tetragon Falco KubeArmor Maintainer Cisco (Isovalent) + OpenAI Isovalent (Cisco) CNCF graduated, created by Sysdig CNCF Sandbox License BSD-2-Clause, BPF dual BSD/GPL Apache-2.0 Apache-2.0 Apache-2.0 Blocks in real time Yes Yes, in-kernel Detect and alert (per docs) Yes, via LSMs Authoring Code, no DSL TracingPolicy custom resource YAML rules Security policy specs Replaces vulnerable code Yes Not disclosed Not disclosed Not disclosed Signed + TPM-attested loads Yes, required Not disclosed Not disclosed Not disclosed Kernel needs Patched bpf-next Not disclosed Not disclosed Not disclosed Status Pre-release Open-sourced 2022 Graduated Sandbox 

 Key Takeaways 

 Shirudo lets AI agents write signed eBPF shields for live Linux systems. 

 A Codex-built guard blocked Java4Shell (CVSS 9.2) on running Elasticsearch. 

 Every load is signature-checked and recorded by TPM 2.0. 

 Targets need a patched bpf-next kernel today. 

 No overhead or false-positive data is published yet. 

 Check out the OpenAI announcement , Isovalent technical post , GitHub repo and docs . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime appeared first on MarkTechPost .
