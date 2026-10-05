---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 28 items, 3 important content pieces were selected

---

**Technology News**
1. [vLLM v0.31.0: DeepSeek-V4.1-Flash optimizations and fast-restart mechanism](#item-tech-news-1) ⭐️ 8.0/10
2. [Sona: One Transformer Replaced Yandex Music&\#x27;s 15+ Stage Pipeline](#item-tech-news-2) ⭐️ 7.0/10
3. [Bloomberg Industry Research: US AI Lead Over China Narrows to 3%](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.31.0: DeepSeek-V4.1-Flash optimizations and fast-restart mechanism](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM v0.31.0 shipped on October 5, 2026 with 717 commits from 307 contributors \(96 new\), targeting production LLM inference operators. The release centers on DeepSeek-V4.1-Flash performance work — FlashMLA mega attention with the NVFP4 compressed KV cache as the SM100 default, DeepGEMM sparse MQA logits for the indexer, Mega-Gate fusing the gate GEMM with expert selection, MXFP8 quantization improvements, and Engram sharding — plus a new fast-restart mechanism via the \`vllm preload\` CLI that keeps post-quantized weights resident in GPU memory across engine restarts, and experimental CRIU-based \`vllm snapshot create/restore\` for fully initialized TP1 engines. Model Runner V2 gains draft-model speculative decoding and custom logits processors, large-scale serving adds MoonEP, DeepEPv2 with sequence parallelism, and a sharding-aware NCCL M2N weight-transfer backend for RL, and scheduling controls introduce \`--max-num-active-seqs\` and a reworked waiting queue that prioritizes requests already holding KV blocks. Breaking changes include gating per-request multimodal kwargs behind \`--trust-request-mm-kwargs\`, removing \`tokenizer\_mode=&quot;slow&quot;\`, renaming \`--enable-mamba-fine-grained-prefix-cache\` to \`--enable-mamba-shared-prefix-checkpoint\`, replacing \`quantization=&quot;fp8&quot;\` with the \`fp8\_per\_tensor\` shorthand, removing the AllSpark INT8 W8A16 backend, and enabling XPU graphs by default.

github · khluu · Oct 5, 06:44

**「Background」** vLLM is an open-source LLM inference engine widely used for production LLM deployments. Version 0.31.0 follows the v0.30.x series and introduces breaking changes including the removal of \`tokenizer\_mode=&quot;slow&quot;\`, renaming of \`--enable-mamba-fine-grained-prefix-cache\` to \`--enable-mamba-shared-prefix-checkpoint\`, and changes to online quantization APIs. Users upgrading from v0.30.x need to update their configurations accordingly.

**「Upgrade requires configuration migration」** Upgrading from v0.30.x requires configuration updates: \`tokenizer\_mode=&quot;slow&quot;\` is removed, \`--enable-mamba-fine-grained-prefix-cache\` is renamed to \`--enable-mamba-shared-prefix-checkpoint\`, online quantization via \`quantization=&quot;fp8&quot;\` must be replaced with \`fp8\_per\_tensor\`, the AllSpark INT8 W8A16 backend is removed, and \`--enforce-eager\` now also disables JIT kernel warmup. Additionally, per-request multimodal kwargs \(\`mm\_processor\_kwargs\`, \`media\_io\_kwargs\`\) are rejected by default unless \`--trust-request-mm-kwargs\` is explicitly set, a security hardening change that may break existing integrations relying on per-request multimodal configuration.

<details><summary>References</summary>
<ul>
<li>Releases · vllm-project/vllm - GitHub</li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#open-source`, `#performance-optimization`, `#deepseek`

---

<a id="item-tech-news-2"></a>
### [Sona: One Transformer Replaced Yandex Music&\#x27;s 15+ Stage Pipeline](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 7.0/10

Yandex Music&\#x27;s Sona, a single transformer using a novel History Compression technique, replaced their entire multi-stage recommendation pipeline \(15+ candidate generators, pre-ranker, and ranker\) in an A/B test on smart speakers. The model reads up to 8,192 events, splitting them into older \(6,144\) and recent \(2,048\) blocks that exchange information via cross-attention, with a 7-layer stack running only on recent events—roughly halving inference cost. In a 7-day A/B test with 15% of users per arm, Sona achieved +4.53% Active Users and +6.30% Total Listening Time over the production control \(both significant at p &lt; 0.01\). However, it hasn&\#x27;t shipped to full traffic yet, and catalog coverage is lower than the production stack.

reddit · r/MachineLearning · /u/SettingAccording8986 · Oct 5, 10:07

**「Background」** Traditional production recommendation systems use multi-stage pipelines with specialized models for candidate generation, pre-ranking, and ranking. Recent work from Meta and Netflix has shown that single end-to-end generative models can replace these cascades, but handling long user histories \(thousands of events\) remains computationally expensive due to quadratic attention costs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/meta-recsys/generative-recommenders">GitHub - meta-recsys/ generative -recommenders: Repository hosting...</a></li>
<li><a href="https://www.linkedin.com/posts/thiyagu-ganesan-32b6219_how-netflix-built-genpage-a-single-genai-activity-7484994802640650240-GPSp">Netflix Ditches Multi-Stage AI Pipeline for Single -Model... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#recommender-systems`, `#transformer-architecture`, `#production-ML`, `#generative-recommendation`, `#inference-optimization`

---

<a id="item-tech-news-3"></a>
### [Bloomberg Industry Research: US AI Lead Over China Narrows to 3%](https://www.bloomberg.com/news/articles/2026-10-04/us-lead-in-ai-over-china-narrows-after-deepseek-gains-bi-says) ⭐️ 7.0/10

Bloomberg Industry Research says the performance advantage of US AI companies over Chinese counterparts has shrunk to a historic low in recent months. After DeepSeek released V4.1 Flash in September 2026, leading Chinese models trailed US models by just 3% on benchmarks, down from roughly 9% in May and 15% at the start of the year. The report attributes China&\#x27;s progress to accumulated technical expertise and optimization for domestic hardware, and says the narrowing gap calls into question the effectiveness of US technology export restrictions. DeepSeek V4.1 Flash ranked sixth globally on LiveBench in September, but Chinese models still account for only 3 of the top 15.

telegram · zaihuapd · Oct 5, 07:32

**「Background」** Bloomberg Intelligence&\#x27;s 3% estimate followed a rapid narrowing during 2026: the report says Chinese top models trailed US models by about 15% at the start of the year and about 9% in May, before DeepSeek released V4.1 Flash in September. The report attributes the improvement to accumulated technical expertise and optimization for domestic hardware, and it says the gains raise questions about the effectiveness of US technology export restrictions.

**「Policy and Procurement Implications」** The narrowing from 15% to 3% provides concrete benchmark data that US export control policymakers can use to reassess whether current restrictions are achieving their stated goal of maintaining a meaningful performance gap. For organizations evaluating AI models, the 3% gap means Chinese models such as DeepSeek V4.1 Flash are now within practical reach for many workloads, though Chinese models still hold only 3 of the top 15 LiveBench spots, indicating the lead persists at the frontier. The data also validates the domestic-hardware substitution strategy—DeepSeek trained V3 on Huawei Ascend chips rather than Nvidia—that has been central to China&\#x27;s response to export controls.

<details><summary>References</summary>
<ul>
<li><a href="https://www.livemint.com/ai/deepseek-narrows-ai-gap-with-us-rivals-to-just-3-threatening-american-dominance-11791173222487.html">DeepSeek narrows AI gap with US rivals to just 3% ... - Mint</a></li>
<li><a href="https://awesomeagents.ai/news/china-70b-ai-chip-subsidy-self-sufficiency/">China Unveils $70B AI and Chip Subsidy to Counter US Controls</a></li>
<li><a href="https://www.techbrunch.co.za/chinas-ai-strategy-outpaces-americas-agi/">America’s AGI Obsession Is Outsmarted By China ’s Bold 6-Step...</a></li>
<li><a href="https://www.forbes.com/sites/ashishbhatia/2026/08/04/the-china-ai-thesis/">The China AI Thesis: : Why AI Is Now A US - China Duopoly, Not One...</a></li>

</ul>
</details>

**Tags**: `#AI benchmarks`, `#US-China tech competition`, `#DeepSeek`, `#export controls`, `#industry analysis`

---