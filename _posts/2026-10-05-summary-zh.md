---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 28 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 性能优化与快速重启机制](#item-tech-news-1) ⭐️ 8.0/10
2. [Yandex Music 用单一 Transformer 替换 15+ 推荐组件](#item-tech-news-2) ⭐️ 7.0/10
3. [彭博行业研究：美国对华 AI 性能优势缩至 3%](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 性能优化与快速重启机制](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM v0.31.0 于 2026 年 10 月 5 日发布，面向 LLM 推理服务部署用户，包含 717 个提交、来自 307 位贡献者（96 位新贡献者）的改动，核心亮点是 DeepSeek-V4.1-Flash 在 SM100 上默认启用 FlashMLA mega attention 配合 NVFP4 压缩 KV 缓存，并新增 DeepGEMM 稀疏 MQA logits、Mega-Gate 融合、多个解码器边界融合算子、MXFP8 量化改进、Engram 分片增强、视觉塔编码器 CUDA 图和 SWA 有界重放。新增 \`vllm preload\` CLI 快速重启机制通过权重缓存守护进程在引擎重启间保持量化后权重驻留 GPU 显存，支持数据并行、MTP 草稿模型、\`/health\` 端点和就绪等待，实验性 CRIU 快照可恢复完全初始化的 TP1 引擎。Model Runner V2 新增草稿模型推测解码和自定义 logits 处理器，大规模服务方面新增 MoonEP 均衡 EP all2all 后端、prefill 上下文并行与数据并行组合、DeepEPv2 序列并行等，调度控制新增 \`--max-num-active-seqs\` 独立限制 RUNNING 准入和等待队列重排优先调度已持有 KV 块的请求。安全方面拒绝逐请求 \`mm\_processor\_kwargs\` 和 \`media\_io\_kwargs\`（除非设置 \`--trust-request-mm-kwargs\`），前缀缓存额外键按来源标记防止 LoRA 名称与 \`cache\_salt\` 冲突。

github · khluu · 10月5日 06:44

**「项目背景」** vLLM 是一个开源的大语言模型推理和服务引擎，被广泛用于生产环境中的 LLM 部署。v0.31.0 是该项目的重大版本更新，包含 717 个提交和 307 位贡献者的工作，重点优化了 DeepSeek-V4.1-Flash 的推理性能，并引入了快速重启机制和多项调度控制改进。

**「升级需处理多项破坏性变更」** vLLM v0.31.0 包含多项破坏性变更，直接升级可能导致现有部署中断：\`tokenizer\_mode=&quot;slow&quot;\` 已被移除，\`--enable-mamba-fine-grained-prefix-cache\` 重命名为 \`--enable-mamba-shared-prefix-checkpoint\`，通过 \`quantization=&quot;fp8&quot;\` 进行的在线量化被 \`fp8\_per\_tensor\` 简写替代，AllSpark INT8 W8A16 后端被移除，\`--enforce-eager\` 现在也会禁用 JIT kernel 预热，XPU 图默认启用且 \`VLLM\_XPU\_ENABLE\_XPU\_GRAPH\` 环境变量被移除。此外，安全策略收紧：逐请求的 \`mm\_processor\_kwargs\` 和 \`media\_io\_kwargs\` 现在默认被拒绝，除非显式设置 \`--trust-request-mm-kwargs\`。使用这些配置的生产环境需要在升级前逐项调整参数，否则服务将无法启动或行为改变。

<details><summary>参考链接</summary>
<ul>
<li>Releases · vllm-project/vllm - GitHub</li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#open-source`, `#performance-optimization`, `#deepseek`

---

<a id="item-tech-news-2"></a>
### [Yandex Music 用单一 Transformer 替换 15+ 推荐组件](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 7.0/10

Yandex Music 的 Sona 模型在 A/B 测试中用一个 Transformer 替换了原有的 15+ 候选生成器、预排序器和排序器组成的多阶段推荐管线。该模型采用「历史压缩」（History Compression）技术，将 8,192 个事件拆分为较早的 6,144 个和最近的 2,048 个，通过交叉注意力和一层全历史自注意力交换信息，随后仅对最近 2,048 个事件运行 7 层堆叠，推理成本约降低一半。在智能音箱场景的 7 天 A/B 测试中（每组 15% 用户），Sona 相比生产对照组 Active Users 提升 4.53%、Total Listening Time 提升 6.30%（p &lt; 0.01），但目录覆盖率低于生产管线，且尚未全量上线，长期 A/B 测试正在进行中。

reddit · r/MachineLearning · /u/SettingAccording8986 · 10月5日 10:07

**「背景」** 传统推荐系统通常采用多阶段流水线架构：多个候选生成器负责召回，预排序器和排序器依次筛选和打分。大语言模型展示了单一端到端模型可以替代原本分散在多个专用组件中的工作，这一思路已被引入生产环境——例如 Meta 和 Netflix 都已用单个生成式模型取代了多阶段推荐流水线。Sona 在此基础上提出了 History Compression 技术，将 8,192 条用户历史事件拆分为较旧的 6,144 条和最近的 2,048 条，通过交叉注意力和一层全历史自注意力交换信息，随后仅对最近 2,048 条运行 7 层堆叠，从而在保留大部分质量的同时将推理成本降低约一半。

**「对推荐系统工程师的影响」** Sona 提供了一个具体的生产级案例，表明单一端到端生成式模型可以在保留质量的同时替代多阶段管线并将推理成本减半。历史压缩技术为长上下文 Transformer 的推理优化提供了可复用的架构思路，但目录覆盖率下降的问题仍需解决，且该结果来自 Reddit 公告而非同行评审论文，置信度有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.11015">Sona Technical Report</a></li>
<li><a href="https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/">Yandex Introduces Sona : A Single Generative Recommender That...</a></li>
<li><a href="https://github.com/meta-recsys/generative-recommenders">GitHub - meta-recsys/ generative -recommenders: Repository hosting...</a></li>
<li><a href="https://www.linkedin.com/posts/thiyagu-ganesan-32b6219_how-netflix-built-genpage-a-single-genai-activity-7484994802640650240-GPSp">Netflix Ditches Multi-Stage AI Pipeline for Single -Model... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#recommender-systems`, `#transformer-architecture`, `#production-ML`, `#generative-recommendation`, `#inference-optimization`

---

<a id="item-tech-news-3"></a>
### [彭博行业研究：美国对华 AI 性能优势缩至 3%](https://www.bloomberg.com/news/articles/2026-10-04/us-lead-in-ai-over-china-narrows-after-deepseek-gains-bi-says) ⭐️ 7.0/10

彭博行业研究称，DeepSeek 于 2026 年 9 月发布 V4.1 Flash 后，中国头部模型在基准测试中仅落后美国模型 3%，较 5 月约 9% 和年初 15% 大幅收窄。该报告将中国 AI 的进步归因于技术积累及对国产硬件的优化，并指出这一趋势令美国技术出口限制的效果受到质疑。DeepSeek V4.1 Flash 在 LiveBench 全球排名第六，但中国模型在前 15 名中仍仅占 3 席。

telegram · zaihuapd · 10月5日 07:32

**「背景」** 美国对中国实施 AI 芯片出口管制，旨在限制中国获取先进计算硬件以延缓其 AI 发展。彭博行业研究持续追踪中美 AI 模型性能差距，此前数据显示年初差距约为 15%，5 月收窄至约 9%。报告指出，中国 AI 进步源于技术积累及对国产硬件的优化。

**「出口管制效果受质疑」** 彭博行业研究的数据直接质疑了美国对华 AI 芯片出口管制的实际效果：尽管中国公司被限制使用英伟达最新芯片，DeepSeek 等团队通过转向华为升腾等国产硬件并优化模型架构，将性能差距从年初的 15% 压缩至 3%。这一趋势意味着美国政策制定者需要重新评估现有管制措施的约束力，而全球 AI 开发者在模型选型时也需将中国模型纳入考量——DeepSeek V4.1 Flash 已进入 LiveBench 全球第六。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://awesomeagents.ai/news/china-70b-ai-chip-subsidy-self-sufficiency/">China Unveils $70B AI and Chip Subsidy to Counter US Controls</a></li>
<li><a href="https://www.techbrunch.co.za/chinas-ai-strategy-outpaces-americas-agi/">America’s AGI Obsession Is Outsmarted By China ’s Bold 6-Step...</a></li>

</ul>
</details>

**标签**: `#AI benchmarks`, `#US-China tech competition`, `#DeepSeek`, `#export controls`, `#industry analysis`

---