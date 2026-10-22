---
id: "c57547ebeeca777e"
title: "llama: create new fused op for QSA mask by am17an · Pull Request #30640 · ggml-org/llama.cpp"
url: "https://github.com/ggml-org/llama.cpp/pull/30640"
link: "https://github.com/ggml-org/llama.cpp/pull/30640"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T19:34:04Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["jacek2023"]
language: "en"
summary: "it's time to update your llama.cpp for another speedup (sparse attention models)"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Anthropic", "Microsoft"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1580
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbx12a/llama_create_new_fused_op_for_qsa_mask_by_am17an/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# llama: create new fused op for QSA mask by am17an · Pull Request #30640 · ggml-org/llama.cpp

GitHub · jacek2023 · 2026-10-21

Repository navigation
llama: create new fused op for QSA mask - #30640
Merged
Merged
Conversation
      
          
am17an
        changed the title
llama: create new fused op for QSA scoring
llama: create new fused op for QSA mask
      Oct 16, 2026 
    
      
          
github-actions
Bot
            added
      
  model
  Model specific 
      
  testing
  Everything test related 
      
  ggml
  changes relating to the ggml tensor library for machine learning 
      
  CUDA
  Related to the CUDA backend 
  labels
      Oct 16, 2026 
    
ee0d2cc    to
    8a86212      
    Compare
  
          
        
  
    Contributor
        
    
The harness sentinels were left uninitialized, so leftover memory could read as NaN and fail the NaN check.
8a86212    to
    2961d5e      
    Compare
  
          
    
  francisab 
      added a commit
        to francisab/llama.cpp
      that referenced
      this pull request
    
      Oct 21, 2026 
    
    
      
  
    
      Assisted-by: GitHub Copilot
              ServeurpersoCom
                self-requested a review
          October 21, 2026 11:22           
        
              
                    ggerganov
    
              
              reviewed
              
                  
                    Oct 21, 2026 
                  
              
              
            
              
                    ggerganov
    
              
              reviewed
              
                  
                    Oct 21, 2026 
                  
              
              
            
The k-pool mask op only covered the pooled QSA selection of qwen4exp
and glm5-next, while the DSA models and the DeepSeek V4 CSA build the
same top-k mask by hand with fill, set_rows and add.
ggml_top_k_mask(mask, top_k, score, blocks, extra) keeps the mask
cells of the live picks and the extra cells, and sets the rest to
-inf. Every row tensor is 4D in the layout of top_k, and the mask is
broadcast to those rows, so a selection can also be made per head.
score, blocks and extra are optional: without score every pick is
live, without blocks a pick is a cell, and extra holds the cells a
row keeps without a pick.
llm_graph_context::build_fused_top_k_mask views the row tensors in
the layout of kq_mask and registers the fused node. The k-pool
models, the DSA attention of build_attn and the DeepSeek V4 CSA mask
use it when the probe enables the op, and keep their current path on
backends without it.
        
  
    Contributor
        
    
55672a5    to
    2961d5e      
    Compare
  
          
        
  
    Contributor
        
  Author
    
        
  
    Contributor
        
  Author
    
        
  
  Member
        
    
    
  voidstackloop 
      added a commit
        to voidstackloop/llama.cpp
      that referenced
      this pull request
    
      Oct 21, 2026 
    
    
      
  
    
      Resolve the conflict with d454a20 (llama: create new fused op for QSA mask,
ggml-org#30640) in ggml-cuda.cu: master added GGML_OP_TOP_K_MASK where this branch
added GGML_OP_CUSTOM (the mailbox ops) to the compute dispatch and to
supports_op. Keep both cases.
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    
  PowerfulGhost 
      pushed a commit
        to PowerfulGhost/llama.cpp
      that referenced
      this pull request
    
      Oct 22, 2026 
    
    
      
  
    
      Refs:        upstream@c7fc50941 (245 commits, 730 files, +68887/-28225)
             冻结基线 f2cc728 -> c7fc509（"opencl: add F32-to-I32 ARGMAX (ggml-org#30897)"）
Knob:        本 merge 不新增开关。10 个手段的开关名与默认值（全部"默认开"）：
             T1  repack 组  : --repack 0（llama-bench）/ -nr|--no-repack（cli,server）；
                              子项 GFX906_MMV_FUSION_OFF=1、GFX906_Q8_MULTI_OFF=1、
                              GFX906_XQ_CACHE_OFF=1、GFX906_Q8_SHAPE_MMV=w、
                              GFX906_DOWN_REDUCE=0、GFX906_REPACK_THREADS=1
             T2  AllReduce : GGML_ENABLE_CUSTOM_AR=0（ENABLE 型：未设=开）
             T3  HC 链     : GFX906_HC_UP_PRE_OFF=1、GFX906_HC_POST_NORM_OFF=1
             T4  F32 家族  : GFX906_F32=0（主开关）；GFX906_F32_MULTI_OFF=1；
                              模式选择器 GFX906_F32_ROWS=0 / GFX906_F32_NC=0 / GFX906_F32_MULTI=0
             T5  SMA 融合  : GFX906_SMA_FUSION_OFF=1
             T6  conv-step : GFX906_CONV_STEP_OFF=1
             T7  GDN gather: GFX906_GDN_GATHER_OFF=1
             T8  MoE rank  : GFX906_TOPK_MOE_RANK_OFF=1
             T9  elem 链   : GFX906_ELEM_CHAIN=0
             T10 QSA ldxtk : GGML_LIDX_TOPK=0（模式选择器：0/off/false/no=plain 路径、
                              2=强制融合、未设=自动阈值）
Measured:    口径 = 8×MI50(gfx906) / -sm layer / -ngl 99 -fa on -ctk f16 -ctv f16
             （experiment-2026-10-22/p2-upstream-verify/RESULTS.md，20 个测量容器）
             · 确定性：6 prompt 贪心 32 tok 的 filtered/gen-only md5 跨两个独立容器全同
             · OFF 路径 vs 纯上游：6 prompt md5 + PPL b1/b8 **bit-identical**
             · PRE vs POST：merge 比合并前快 tg128 +4.30% / pp4096 +2.75% / pp16384 +2.05%
             · 手段仍生效：tg128 ON 46.640 vs 全 OFF 35.703 t/s（+30.6%）
             · 长上下文：pp32768 ON 2500.39 vs OFF 1999.32 t/s（+25.1%）
             · 算子级：LIDX.* 30/30、TOP_K_MASK 24/24、受上游影响的 5 个 op 1962/1962，FAIL=0
             本 commit（B1 + meta 登记）落地后重测（experiment-2026-10-22/p4-merge-fixes）：
             6 prompt 的 filtered/gen-only md5 与 PPL b1/b8 与上表**逐字节相同**；
             tg128 ON 46.614 vs 全 OFF 35.636 t/s（+30.8%）；算子级 30/30 + 24/24 + 1962/1962 不变。
Correctness: p2 §2（确定性）/ §3（OFF 路径 bit-identical）/ §7（算子级 0 FAIL）三项 PASS，
             p4 复测结论相同（逐字节相同）。
             注：test-backend-ops **全套**里的 TOPK_MOE(n_expert_groups>0) 与
             ADD_<unary>_MUL 的 FAIL 是**上游既有**问题（测试数据走 random_device，逐次不同），
             与本 merge / 本修复无关（p2 与 p4 的失败集合逐次不同但族相同）。
Conflicts:   5 个文件（git merge-tree 干跑预测 = 实际）
  1) ggml/src/ggml-cuda/common.cuh
     解法：union。上游把 streams/cublas 句柄数组的初始化从 `= { { nullptr } }` 改成 `= {}`，
     并把 new_pool_for_device 改成收 ctx 引用；我们加的是 repack_xq 缓存结构体 /
     q8_emit_producer / cur_cgraph / gfx906_env_on。上游的 `= {}` 保留
     （那 4 个成员都是**默认成员初始化器**，元素类型是指针 / size_t，
      `= { { nullptr } }` 与 `= {}` **逐元素等价** —— 只是写法变了，语义没变），
     我们的 4 个成员原样保留。
  2) ggml/src/ggml-cuda/gated_delta_net.cu（T7）
     解法：union。上游新增 gated-delta-net-mma.cu/cuh + ggml_cuda_gdn_mma_args_from_tensor()
     与一个 MMA 快速路径（select_gdn_mma_path）；我们加的是 GDN gather 消除
     （state_rows/state_row_stride 贯穿 kernel -> launch -> impl -> 对外签名）。
     两边都留。另加一条**正确性护栏**：MMA 路径只从 dst->src[5] 读 state，
     gather 被我们消掉时该 tensor 从未被写，故 MMA 入口加 `if (state_rows == nullptr)`；
     gfx906 (CDNA2) 上 select_gdn_mma_path 本来就返回 ar（要求 RDNA3.5 + n_tokens>=2048），
     即该护栏在本平台上零影响，只堵住 RDNA3.5 上的潜在错算。
  3) ggml/src/ggml-cuda/ggml-cuda.cu（T1/T2/T4/T5/T6/T7/T9 的 hook + T10 的派发）
     解法：union。GGML_OP_* 派发表里 ours 的 LIDX_TOPK_CHUNK/LIDX_TOPK_MERGE 两 case
     与上游的 TOP_K_MASK 一 case 并列；supports_op 同样并列。
     hook 归属（逐块核对，见 experiment-2026-10-22/p1-upstream-merge/RESULTS.md §3）：
       - include 区（行 35-37）：gfx906-tp-allreduce.cuh / gfx906-repack/repack.cuh /
         gfx906-hc-up-pre.cuh / gfx906-f32.cuh —— 全部保留
       - 行 784-790  ggml_backend_cuda_context 析构里的 repack_xq 缓存回收（T1）
       - 行 1047/1074/1313-1320/1349-1464  T2 自定义 AllReduce（tp_custom_ar_init /
         tp_custom_ar_prepare / tp_custom_ar_launch_rank / tp_custom_ar_destroy）
       - 行 2033/2080/2178/2264  T1 repack 的 mul_mat / mul_mat_vec_f / mul_mat_vec_q /
         mul_mat_id 四个派发点
       - 行 2770/2773  T10 的 LIDX_TOPK_CHUNK / LIDX_TOPK_MERGE 派发
       - 行 4032-4145  T1 q8-multi 计划 + T4 f32 计划（f32m_build_plan）
       - 行 4147-4243  T3 hc_post_norm 匹配器 + q8x 失效逻辑
       - 行 4253-4258  T6 conv-step 入口（ggml_cuda_try_conv_step_fusion）
       - 行 4262-4320  T1 q8-multi 调试 + T1 down_reduce 融合
       - 行 4337-4350  T7 GDN cache 融合（ggml_cuda_try_gdn_cache_fusion，
                  调用点加 cgraph 参数 -> gather 消除生效）
       - 行 4852-4884  T1 up/gate GLU 融合
       - 行 5104-5147  T5 SIGMOID->MUL->ADD 融合
       - 行 5152-5165  T3 ② hc_post_norm 融合入口
       - 行 5167-5196  T3 ① hc_up_pre 融合入口
       - 行 5234-5259  T9 elementwise 链融合（保持"最后跑"的位置）
       - 行 5265      cuda_ctx->graph_gen++（T1 的 q8_1 激活缓存代际）
       - 行 5463-5473  T6/T7 的 gather 跳过 + cur_cgraph 赋值
       - 行 5498-5505  T4 的 f32 分组 mat-vec 派发
       - 行 5518      ggml_cuda_try_fuse 入口（T5/T6/T7/T9 的总入口）
  4) ggml/src/ggml.c（T10 的 op 注册）
     解法：union + **修一处我们自己的漏**。
     枚举：上游在 DSV4_HC_POST 之后加了 GGML_OP_TOP_K_MASK，我们在 LIGHTNING_INDEXER 之后
     加了 GGML_OP_LIDX_TOPK_CHUNK / GGML_OP_LIDX_TOPK_MERGE —— 合并后 104 个 op。
     字符串表：上游的 "TOP_K_MASK" 同时进了 GGML_OP_NAME 和 GGML_OP_SYMBOL；**我们只进了
     GGML_OP_NAME，没进 GGML_OP_SYMBOL**（0bc314cf9 里 GGML_OP_SYMBOL 只有 101 条而数组长度
     是 103 ⇒ LIDX 两个 op 的符号是 nullptr，ggml_graph_print 会打印 (null)）。
     本次补上 "ldxtk_topk_chunk(q, k, weights, mask)" / "ldxtk_topk_merge(partial)"，
     两处 static_assert 改成 104，并用脚本逐下标核对 enum / NAME / SYMBOL 三表对齐。
  5) tests/test-backend-ops.cpp（T10 的测试）
     解法：union。test_ldxtk（我们的）与 test_top_k_mask（上游的）两个 test_case 类都保留，
     各自的 initialize_tensors 也都保留；两边的 test_cases.emplace_back 注册都在。
Merged-fix:  上游 d454a20 "llama: create new fused op for QSA mask (ggml-org#30640)" 的新 op
             GGML_OP_TOP_K_MASK 与我们的 T10 有语义冲突，已加最小护栏：
             src/models/qwen4exp.cpp 的 `if (cparams.fused_top_k_mask)` 改成
             `if (cparams.fused_top_k_mask && !use_ldxtk)`。
             原因：上游的 fused op 用"每个 pool 的分数"（score[n_pool, n_tokens]）来丢掉
             死 pick；我们的 ldxtk 路径不产生这个张量（score == nullptr），而上游的 op
             语义是"没有 score ⇒ 每个 pick 都是活的" ⇒ 死 slot（索引 -1，被 clamp 到 pool 0）
             会把 pool 0 错误地 unmask。
             ⇒ **两种失败模式，缺一不可**：
               (a) decode（n_tokens == 1）：reshape 的元素数恰好相等 ⇒ 不崩，但死 slot 被当成
                   活的 pick ⇒ **静默数值错**（pool 0 被错误 unmask）；
               (b) prefill（n_tokens > 1）：上游 op 里 rows(top_k) 要把 ldxtk 路径的 1-D
                   top_k（n_top_pool*n_tokens 个元素）reshape 成
                   [n_top_pool*n_tokens, n_tokens, 1, 1]，元素数差 n_tokens 倍 ⇒
                   ggml.c:3723 的 `GGML_ASSERT(ggml_nelements(a) == ggml_nelements(b))`
                   **硬 abort**（进程直接挂掉，不是静默错值）。
             ⇒ 护栏双重必要：prefill 是硬崩，decode 是静默错。
             护栏只影响 ldxtk 路径（auto 阈值 n_pool_max * n_ubatch >= 2^28，或
             GGML_LIDX_TOPK=2），不改动 T10 的阈值/开关。
             另加 ggml/src/ggml-cuda/topk-moe.cu 的 `config.n_groups > 0` 守卫：
             上游新加了"专家分组"掩码（在 kernel 内把组外专家置 -inf），
             我们的 T8 rank kernel 直接对原始 logits 排序、看不到那个掩码，必须让路。
             （我们的模型 n_expert_groups = 0，本平台上该路径本就不触发。）
             另修两处**协议 / 后端登记**（只动常量、断言与登记，不改任何数值路径）：
             ① ggml/include/ggml-rpc.h：op 计数护栏失配 —— 断言写着 GGML_OP_COUNT == 102
                而合并后实际是 104 ⇒ 该头文件在 -DGGML_RPC=ON 下**编译不过**
                （T10 加 2 个 op 时没动这个文件；上游为自己的 +1 op 把它改成 102 并把
                RPC_PROTO_PATCH_VERSION 0->1，merge 保留了上游的值）。
                现改为 static_assert(GGML_OP_COUNT == 104) 且 RPC_PROTO_PATCH_VERSION 1->2
                （patch 1 = 上游的 +1 op，patch 2 = 我们的 +2 个 LIDX op）。
                已核：全树其它 GGML_OP_COUNT 引用无硬编码计数（ggml.c 两处已是 104；
                ggml-backend-meta.cpp / ggml-openvino.cpp / test-backend-ops.cpp 都是按
                GGML_OP_COUNT 循环），ggml-rpc.cpp 里也没有 op 表长度常量。
             ② ggml/src/ggml-backend-meta.cpp：meta 后端（-sm tensor 用）的 op switch 里
                上游登记了 GGML_OP_TOP_K_MASK，我们两个 LIDX op 没登记 ⇒ 落到 default 分支的
                `GGML_ABORT("ggml op not implemented: %s")`（**硬崩，不是安全回退**）。
                现显式登记：输入全部已复制（MIRRORED）时各卡算同一份结果（与单卡一致）；
                输入被切分时显式报错并给出规避方式（-sm layer 或 GGML_LIDX_TOPK=0），
                绝不静默算错。默认构建（GGML_RPC=OFF / -sm layer）行为不变。
Census:      手段符号普查（0bc314cf9 -> 本 merge 的最终树）**没有任何一项变少**：
             gfx906-repack/ 10->10、gfx906_env_on 19->19、gfx906-tp-allreduce 4->4、
             tp_custom_ar_init 4->4、GGML_ENABLE_CUSTOM_AR 3->3、gfx906-f32 7->7、
             ggml_cuda_f32_env_on 9->9、GFX906_F32_MULTI_OFF 2->2、
             ggml_cuda_op_sigmoid_mul_add 3->3、GFX906_SMA_FUSION_OFF 2->2、
             GFX906_CONV_STEP_OFF 2->2、GFX906_GDN_GATHER_OFF 2->2、
             GFX906_TOPK_MOE_RANK_OFF 2->2、gfx906-hc-up-pre 4->4、
             GFX906_HC_UP_PRE_OFF 5->5、GFX906_HC_POST_NORM_OFF 3->3、
             GFX906_ELEM_CHAIN 8->8、GGML_LIDX_TOPK 4->5、ldxtk 92->101、
             LIDX_TOPK 25->30、ggml_ldxtk 12->12、LIDX_TOPK_CHUNK 13->15、
             LIDX_TOPK_MERGE 8->10、ggml_cuda_try_fuse 9->9、state_rows 36->38
             （+ 新增上游符号 TOP_K_MASK / ggml_top_k_mask / GGML_OP_TOP_K_MASK；
               GGML_OP_TOP_K_MASK 0->9、GGML_OP_LIDX_TOPK_CHUNK 12->14、
               GGML_OP_LIDX_TOPK_MERGE 7->9 —— 后三项含本 commit 在
               ggml-backend-meta.cpp 里新增的 case 标签与注释）。
             数字由 experiment-2026-10-22/p3-merge-review/census.py 整树 binary-safe 复算
             （日志：experiment-2026-10-22/p4-merge-fixes/logs/census-pre-vs-merge-vs-final.txt）。
Build:       JOBS=6 bash harness/build-tree.sh wt/upmerge builds/upmerge
             llama-bench llama-cli llama-perplexity test-backend-ops
             → 0 error；编译段 warning 与 p22 基线（build-14）逐条相同：5 条
             -Wpass-failed（gfx906-repack/repack-kernels.cuh:946 occupancy）+ 2 条
             "N warnings generated"；配置段 2 条环境级 warning（ccache / cpp-httplib）。
             参照构建：builds/upstream-c7fc（wt/upstream-c7fc @ c7fc509，同口径），
             0 error、编译段 0 warning。
             另：JOBS=6 EXTRA_CMAKE="-DGGML_RPC=ON" bash harness/build-tree.sh \
             wt/upmerge builds/upmerge-rpc-check ggml-rpc llama-cli llama-bench
             → 394/394 步、0 error，libggml-rpc.so / llama-cli / llama-bench 全部产出
             （B1 的 static_assert 只有这条配置才会被编译到）；warning 5 条，
             与 p22 基线（build-14）同族同位置（repack-kernels.cuh:946 的
             -Wpass-failed occupancy），无新增。
             本 commit 落地（B1 + meta 登记）后增量重建：27/27 步、0 error、
             编译段 0 warning（只重编 ggml-backend-meta.cpp.o 一个文件），
             数值相关二进制（libggml-hip.so / libllama.so / llama-cli /
             llama-perplexity / llama-bench / test-backend-ops）md5 与修前**完全相同**，
             只有 libggml-base.so 变了 ⇒ 数值不变是结构上必然。
             证据：experiment-2026-10-22/p4-merge-fixes/logs/build-upmerge*.log
Review:      bash harness/acceptance.sh    # 套容器（父 agent 串行跑，GPU 归父 agent）
Card:        knowledge/01-techniques/*.md（T1–T10，本轮未改；数值结论待父 agent 重测）
Report:      experiment-2026-10-22/p1-upstream-merge/RESULTS.md
             experiment-2026-10-22/p2-upstream-verify/RESULTS.md   （merge 臂 GPU 全套验证）
             experiment-2026-10-22/p3-merge-review/RESULTS.md      （独立复核）
             experiment-2026-10-22/p4-merge-fixes/RESULTS.md       （B1/meta/msg 修复与复测）
    
    
  
      
        
      
      
    6 tasks
  
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
