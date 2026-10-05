---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 24 items, 2 important content pieces were selected

---

**Technology News**
1. [Top ARC-ΑGI-3 scores on Kaggle just went from 7% to 56% \[N\]](#item-tech-news-1) ⭐️ 7.0/10
2. [Google Releases VeriHarness Self-Verification Framework for Long-Horizon Tasks](#item-tech-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Top ARC-ΑGI-3 scores on Kaggle just went from 7% to 56% (N)](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 7.0/10

A Reddit post claims top ARC-AGI-3 scores on Kaggle surged from 7% to 56% in 30 days using small local models, potentially surpassing average human performance on a benchmark designed to highlight human reasoning superiority.

reddit · r/MachineLearning · /u/we\_are\_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/)

**Tags**: `#ARC-AGI`, `#AI benchmarks`, `#abstract reasoning`, `#Kaggle competition`, `#AI progress`

---

<a id="item-tech-news-2"></a>
### [Google Releases VeriHarness Self-Verification Framework for Long-Horizon Tasks](https://arxiv.org/abs/2610.00972v1) ⭐️ 7.0/10

Google&\#x27;s research team has published VeriHarness, a self-verification framework in which the same model that generates candidate outputs also verifies them on long-horizon tasks, using evidence-driven checking for divergent claims and active challenging for consensus claims before selecting, revising, or rebuilding the final result. On five long-horizon task benchmarks across two models, the authors report achieving the highest selection scores, with evidence-driven revision improving Gemini 3.5 Flash by 6.2 points and Claude Opus 4.8 by 6.4 points over single generation. The framework and approximately 26,000 rollouts have been released on GitHub. These are self-reported results from a single research paper, not independently measured benchmarks.

telegram · zaihuapd · Oct 4, 13:32

**「Background」** Long-horizon tasks involve multi-step reasoning and execution where errors compound across steps, making single-pass LLM generation unreliable. Self-verification—where a model checks its own outputs—has emerged as a training-free approach to improve reliability, but prior methods typically relied on simple majority voting or single-model consistency checks. The paper describes VeriHarness as the first agentic verification harness for long-horizon tasks, designed to be training-free and plug-and-play across benchmarks and models.

**「Open Dataset Reduces Research Barriers」** The release of approximately 26,000 rollouts—generated at a cost exceeding $100,000—along with open-source code and dataset at veriharness.com, provides researchers working on agentic verification with a ready-made resource that eliminates the need to independently produce comparable-scale rollout data. Teams evaluating or extending self-verification methods for long-horizon tasks can now build directly on this dataset rather than incurring the same computational expense.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long - Horizon Tasks</a></li>
<li><a href="https://arxiv.org/html/2610.00972v1">VeriHarness : Scaling Agentic Verification for Long-Horizon Tasks</a></li>

</ul>
</details>

**Tags**: `#AI verification`, `#self-consistency`, `#long-horizon tasks`, `#LLM evaluation`, `#Google research`

---