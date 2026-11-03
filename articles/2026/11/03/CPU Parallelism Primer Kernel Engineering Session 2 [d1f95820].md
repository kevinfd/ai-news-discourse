---
id: "d1f95820118cf15d"
title: "CPU Parallelism Primer | Kernel Engineering | Session 2"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xmq7q6/cpu_parallelism_primer_kernel_engineering_session"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xmq7q6/cpu_parallelism_primer_kernel_engineering_session"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T11:11:21Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Winter_Mistake_3185"]
language: "en"
summary: "Session 2 of my free GPU kernel engineering series covers CPU parallelism, with no GPU code. The idea is that most GPU performance ideas are CPU ideas turned up, so here are the parts I found most useful on their own. A single accumulator is a dependency chain. In `sum += a[i] * b[i]` every add waits on the previous one, so the loop uses a fraction of the core. Independent ops needed in flight…"
tags: ["r/ArtificialInteligence"]
orgs: ["Intel"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 326
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xmq7q6/cpu_parallelism_primer_kernel_engineering_session/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# CPU Parallelism Primer | Kernel Engineering | Session 2

Reddit · Winter_Mistake_3185 · 2026-11-03

Session 2 of my free GPU kernel engineering series covers CPU parallelism, with no GPU code. The idea is that most GPU performance ideas are CPU ideas turned up, so here are the parts I found most useful on their own. A single accumulator is a dependency chain. In `sum += a[i] * b[i]` every add waits on the previous one, so the loop uses a fraction of the core. Independent ops needed in flight is about latency x throughput, and four accumulators give four independent chains with the same arithmetic. Measure this with an in-cache array and -fno-tree-vectorize, or you'll be timing two effects at once. The compiler won't fix it for you. FP addition isn't associative, so it must keep your order unless you allow otherwise (-ffast-math, or `#pragma omp simd reduction(+:sum)` per loop). The same non-determinism appears in GPU reductions. Branch cost is predictability. The sorted-vs-random loop showed a [X]x gap at -O0 on my machine ([CPU], GCC [version]) and mostly vanished at -O2, because the compiler removed the branch. Check what it generated before blaming the hardware. Threads: Amdahl says 90% parallel on 8 cores gives about 4.7x, not 8. Per-thread partials in one small array cause false sharing, because they land on one 64-byte cache line that bounces between cores. Padding fixed it for me ([X]x faster at [N] threads), though the gap depends on whether threads sit on separate physical cores. A dot product is memory-bound. It does 2 FLOPs per 8 bytes, so at [BW] GB/s it caps near [Y] GFLOP/s no matter how much SIMD or threading you add. Hiding memory latency needs latency x bandwidth bytes in flight, which is the GPU's reason for running thousands of threads. Video: https://youtu.be/_xE1_2FFTC0 Caveats: numbers are from one machine, intrinsics assume AVX2, and the latency/throughput figures are typical Intel values. Is anything wrong or oversimplified, especially the false-sharing explanation? And which CPU lessons transferred best to GPU work for you?
