---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 24 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Top ARC-ΑGI-3 scores on Kaggle just went from 7% to 56% \[N\]](#item-tech-news-1) ⭐️ 7.0/10
2. [Google 发布 VeriHarness 长程任务自验证框架](#item-tech-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Top ARC-ΑGI-3 scores on Kaggle just went from 7% to 56% (N)](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 7.0/10

A Reddit post claims top ARC-AGI-3 scores on Kaggle surged from 7% to 56% in 30 days using small local models, potentially surpassing average human performance on a benchmark designed to highlight human reasoning superiority.

reddit · r/MachineLearning · /u/we\_are\_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/)

**标签**: `#ARC-AGI`, `#AI benchmarks`, `#abstract reasoning`, `#Kaggle competition`, `#AI progress`

---

<a id="item-tech-news-2"></a>
### [Google 发布 VeriHarness 长程任务自验证框架](https://arxiv.org/abs/2610.00972v1) ⭐️ 7.0/10

Google 研究团队发布 VeriHarness，一个让同一模型既生成又验证长程任务输出的框架。对分歧主张核查环境证据，对共识主张主动挑战，再据此选择、修订或重建最终结果。在 5 个长程任务基准、2 个模型上取得最高选择分，证据驱动修订后较单次生成平均提升 Gemini 3.5 Flash 6.2 分、Claude Opus 4.8 6.4 分，并公开约 2.6 万条 rollouts。

telegram · zaihuapd · 10月4日 13:32

**「背景」** 长程任务（long-horizon tasks）指需要多步推理或操作的复杂任务，单次生成难以保证正确性。LLM 自验证领域已有基于多次采样一致性投票的方法，但缺乏针对长程任务的系统化验证框架。VeriHarness 提出&quot;证据绑定的 Harness-of-Harness&quot;模式，用同一模型对分歧主张核查环境证据、对共识主张主动挑战，实现免训练、即插即用的验证框架。

**「影响」** 公开约 2.6 万条 rollouts（生产成本超过 10 万美元）为智能体验证研究提供了大规模数据集，GitHub 仓库的开放使开发者可直接复用该自验证框架，在长程任务中实现较单次生成 6 分以上的性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long - Horizon Tasks</a></li>
<li><a href="https://github.com/SKZL-AI/veriharness">GitHub - SKZL-AI/ veriharness : An evidence-bound...</a></li>
<li><a href="https://arxiv.org/html/2610.00972v1">VeriHarness : Scaling Agentic Verification for Long-Horizon Tasks</a></li>

</ul>
</details>

**标签**: `#AI verification`, `#self-consistency`, `#long-horizon tasks`, `#LLM evaluation`, `#Google research`

---