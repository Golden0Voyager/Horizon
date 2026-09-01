---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 18 items, 7 important content pieces were selected

---

1. [Google Removes MV2 Extensions from Chrome Web Store, Including uBlock Origin](#item-1) ⭐️ 8.0/10
2. [Introducing wrapture](#item-2) ⭐️ 7.0/10
3. [Sliding-Window Attention with Sinks Outperforms Linear Attention on Long-Context Reasoning](#item-3) ⭐️ 7.0/10
4. [Repurposing Security Cameras for Automatic Bird Identification with BirdNet-Go](#item-4) ⭐️ 6.0/10
5. [Curated Reference Site Documents ChatGPT Work Tools and Browser Control Skill](#item-5) ⭐️ 6.0/10
6. [SynthFin-AML v10.0 Exposes Temporal Leakage in GNNs on Dynamic Financial Graphs](#item-6) ⭐️ 6.0/10
7. [Entropic Scree: Mutual-Information Diagnostic for Dirty High-Dimensional Data](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google Removes MV2 Extensions from Chrome Web Store, Including uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has officially removed all Manifest V2 extensions from the Chrome Web Store, including the widely-used uBlock Origin ad blocker, completing its long-planned transition to Manifest V3. This means Chrome users can no longer install these extensions through official channels. This affects millions of Chrome users who rely on MV2 extensions for ad blocking, privacy protection, and other functionality, raising serious concerns about Google's unilateral control over the browser ecosystem and web safety. The move has prompted widespread calls for users to switch to Firefox, where uBlock Origin continues to work with full capabilities. uBlock Origin is one of the most popular and effective ad blockers available, and its MV2 version offered more powerful filtering capabilities than what MV3 permits. The transition to MV3 restricts how extensions can filter network traffic, which significantly limits the effectiveness of content blockers on Chrome.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Manifest V2 and V3 are different versions of the Chrome extension platform API. MV2 has been the standard for years, while MV3 introduces new restrictions on how extensions can filter and modify network traffic, which Google claims improves security and performance. Google announced the MV2 deprecation plan years ago, giving developers time to migrate, but many popular extensions like uBlock Origin could not be fully recreated under MV3's limitations.

**Discussion**: Community sentiment is overwhelmingly negative toward Google's decision, with users expressing frustration over Google's monopoly power and the safety implications of losing effective ad blocking. Many commenters strongly recommend switching to Firefox, noting that uBlock Origin works best there, and some share personal stories about ad blocking being critical for protecting elderly family members from malicious ads and scamware.

**Tags**: `#Chrome`, `#Browser Extensions`, `#Ad Blocking`, `#Privacy`, `#Web Standards`

---

<a id="item-2"></a>
## [Introducing wrapture](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Graham Dumpleton introduces Wrapture, a Python library that extends monkeypatching concepts from wrapt to enable simultaneous function tracing and value overriding, serving as both a unittest.mock alternative and a code observation tool.

rss · Simon Willison · Aug 31, 23:59

**Tags**: `#Python`, `#Testing`, `#Tracing`, `#Monkeypatching`, `#Tooling`

---

<a id="item-3"></a>
## [Sliding-Window Attention with Sinks Outperforms Linear Attention on Long-Context Reasoning](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 7.0/10

A new arXiv preprint by Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron, and Emy Gervais claims that Sliding Window Attention (SWA) with sinks achieves 2 to 10 times higher performance than post-trained linear attention models on long-context reasoning benchmarks, without requiring any post-training. The authors argue that the linear attention research direction has been benchmarked against the wrong baselines and recommend switching to SWA instead. If validated, this finding could redirect significant compute resources away from expensive post-training linear attention pipelines toward simpler, faster sliding-window approaches, fundamentally reshaping the efficient attention research landscape. The claim challenges the assumption that linear attention requires extensive post-training to be competitive, suggesting the field may have been optimizing against an unfair comparison. The paper only evaluates on two benchmarks—Needle-in-a-Haystack and BABILong—limiting the breadth of evidence for the 2-10x performance gap claim. The authors concede that linear attention may have shown some promise but likely requires training from scratch or extensive post-training to even match SWA, which runs fast and holds memory low without additional training.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**Background**: Standard Transformer attention has quadratic computational cost relative to sequence length, making long-context processing expensive. Sliding Window Attention (SWA) limits each token's attention to a local window, reducing cost to linear; attention sinks are retained early tokens that stabilize generation when older tokens are evicted from the window. Linear attention mechanisms replace the softmax kernel with a kernel function to achieve linear complexity, but often require post-training to restore performance. Needle-in-a-Haystack tests a model's ability to retrieve specific information buried in long contexts, while BABILong evaluates long-context reasoning capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28444v1">Sliding - window beats linear attention</a></li>
<li><a href="https://runinfra.ai/glossary/attention-sinks">Attention sinks : what it is and why it moves cost | RunInfra</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-attention-mechanisms">Linear Attention Mechanisms</a></li>

</ul>
</details>

**Tags**: `#attention mechanisms`, `#long-context LLMs`, `#efficient transformers`, `#sliding window attention`, `#linear attention`

---

<a id="item-4"></a>
## [Repurposing Security Cameras for Automatic Bird Identification with BirdNet-Go](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 6.0/10

A hobbyist repurposed existing security camera audio feeds by connecting them to BirdNet-Go, an open-source AI-powered soundscape analyzer, to create an automatic bird identification system that runs 24/7 on local hardware. The project demonstrates how RTSP audio streams from cameras like Unifi and Aqara can be ingested by BirdNet-Go for real-time bird species classification. This project illustrates how edge-AI tools like BirdNet-Go can be creatively applied to existing IoT hardware, lowering the barrier to entry for citizen science and backyard bird monitoring without requiring specialized equipment. It also highlights the growing ecosystem of open-source wildlife monitoring tools that run locally without cloud dependencies. BirdNet-Go expects 48kHz audio samples, which some consumer cameras cannot provide (e.g., Aqara cameras are limited to 16kHz), and outdoor microphones without windshields suffer from significant wind noise. Community members shared workarounds including adding external microphones to Raspberry Pi setups and building portable BirdNet-Pi units with e-ink displays for field use.

hackernews · speckx · Aug 31, 16:47 · [Discussion](https://news.ycombinator.com/item?id=49511856)

**Background**: BirdNet-Go is an open-source, self-hosted real-time soundscape analyzer that uses multi-model local AI inference to identify birds, bats, and other wildlife from audio input. It can ingest soundcard input or network audio streams such as RTSP feeds and presents detections through a web UI, running 24/7 on hardware as small as a Raspberry Pi. Edge AI refers to deploying AI models on local devices rather than in the cloud, enabling real-time processing without internet connectivity.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/birdnet-go: Self-hosted realtime soundscape analyser for birds, bats and other wildlife. Multi-model local AI inference, runs 24/7 on a Raspberry Pi. · GitHub</a></li>
<li><a href="https://www.ibm.com/think/topics/edge-ai">What Is Edge AI? | IBM</a></li>

</ul>
</details>

**Discussion**: Community members shared their own implementations, with one user successfully connecting BirdNet-Go to a Unifi doorbell camera via RTSP and planning to add an e-ink display for visual bird identification. Others discussed hardware challenges such as wind noise from unprotected microphones and insufficient sampling rates, recommending external microphones paired with Raspberry Pi as a more reliable alternative. Several users also highlighted complementary tools like Cornell University's Merlin Bird ID app and shared portable BirdNet-Pi builds with e-ink displays for hiking and travel.

**Tags**: `#bird-identification`, `#edge-AI`, `#IoT`, `#open-source-tools`, `#hardware-hacking`

---

<a id="item-5"></a>
## [Curated Reference Site Documents ChatGPT Work Tools and Browser Control Skill](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 6.0/10

Simon Willison published a curated reference site at codex-tool-reference.simonw.chatgpt.site documenting tools and skills for ChatGPT Work, notably featuring a browser control skill that enables AI agents to interact with web pages via Playwright. The skill instructs ChatGPT Work to launch a Playwright instance through its Node.js REPL and retrieve full browser usage documentation programmatically. This reference site provides a practical resource for developers exploring ChatGPT Work's tool ecosystem, and the browser control skill represents a novel approach to AI-agent browser interaction that could enable autonomous web task automation. It demonstrates how LLM-powered agents can leverage existing browser automation libraries like Playwright to perform real-world web operations. The browser control skill works by running `nodeRepl.write(await browser.documentation())` to retrieve detailed browser usage instructions, effectively bootstrapping the agent's understanding of browser capabilities at runtime. Community members noted that some work tools can slow things down and waste tokens, and questioned how this differs from Codex if Codex can already perform similar tasks.

hackernews · ijidak · Aug 31, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49510000)

**Background**: ChatGPT Work is OpenAI's workspace environment that extends ChatGPT with tool-use capabilities, allowing AI agents to execute code, run commands, and interact with external systems. Playwright is an open-source browser automation library developed by Microsoft that supports Chromium, Firefox, and WebKit, commonly used for end-to-end testing and web scraping. AI agents are autonomous programs that can pursue goals, use tools, and take actions with some level of independence, often driven by large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Browser_automation">Browser automation</a></li>

</ul>
</details>

**Discussion**: Simon Willison highlighted the browser control skill as the most interesting feature, explaining how it bootstraps browser instructions via Playwright's Node.js REPL. Some commenters raised practical concerns about token consumption and performance overhead from certain tools, while others questioned the distinction between this reference and Codex itself. A meta-commentary emerged about AI-generated websites sharing a uniform visual style reminiscent of the Bootstrap era.

**Tags**: `#ChatGPT`, `#AI Agents`, `#Browser Automation`, `#Tool Use`, `#Simon Willison`

---

<a id="item-6"></a>
## [SynthFin-AML v10.0 Exposes Temporal Leakage in GNNs on Dynamic Financial Graphs](https://www.reddit.com/r/MachineLearning/comments/1w3imxy/your_gnn_is_probably_just_an_overcomplicated_mlp/) ⭐️ 6.0/10

The authors identified widespread temporal leakage in standard GNN baselines for anti-money laundering on dynamic graphs and released SynthFin-AML v10.0 (100k nodes, 1.2M edges) with a 3-snapshot architecture that enforces strict causal boundaries. They also fixed tabular distribution leakage by ensuring fraud and retail transaction amounts share the same lognormal distribution, then benchmarked GraphSAGE (0.881 PR-AUC) against LightGBM (0.848 PR-AUC) on the strict temporal split. Temporal leakage has been a known but under-addressed problem in temporal graph learning, and this release provides a rigorous, reproducible benchmark that prevents models from cheating by seeing future edges. The finding that GraphSAGE only marginally outperforms LightGBM on clean data challenges the assumption that GNN overhead always pays off for tabular financial data. The 3-snapshot architecture physically disjointes temporal windows: Train Graph (edges ≤ Day 7), Val Graph (edges ≤ Day 8), Test Graph (edges ≤ Day 10), bounding the GNN receptive field to the true causal horizon. The authors engineered 11 point-in-time graph features (including Weighted PageRank and neighbor volume aggregates) for the tree model and submitted the benchmark upstream to PyTorch Geometric via PR #10774.

reddit · r/MachineLearning · /u/Glabmayt2075 · Aug 31, 16:21

**Background**: Graph Neural Networks (GNNs) propagate information across graph edges, but on dynamic graphs where edges appear over time, standard transductive random splits can allow the model to see future edges during training—a problem known as temporal leakage. The temporal graph learning community (e.g., TGN, DyGNN literature) has discussed time-aware splitting, but many anti-money laundering benchmarks still use improper splits that inflate model performance. Additionally, synthetic AML datasets often suffer from tabular leakage, where fraudulent transaction amounts have statistically different distributions from normal transactions, making fraud trivially separable.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/valiyevoktay-cmd/synthfin-aml-">GitHub - valiyevoktay-cmd/synthfin-aml-: A graph-native Anti ...</a></li>
<li><a href="https://agihunt.info/en/p/1a058aaf31d9df7cce291ca15d1">SynthFin-AML benchmark exposes temporal leakage… · AGI Hunt</a></li>
<li><a href="https://kumo.ai/pyg/concepts/data-leakage/">Data Leakage in Graph ML: When Future Information Contaminates Training | Kumo.ai | Kumo.ai</a></li>

</ul>
</details>

**Tags**: `#Graph Neural Networks`, `#Temporal Graph Learning`, `#Anti-Money Laundering`, `#Dataset Release`, `#Evaluation Methodology`

---

<a id="item-7"></a>
## [Entropic Scree: Mutual-Information Diagnostic for Dirty High-Dimensional Data](https://www.reddit.com/r/MachineLearning/comments/1w3br9c/how_to_assess_if_there_is_a_strong_signal_in_your/) ⭐️ 6.0/10

A new tabular data diagnostic tool called Entropic Scree has been announced, using transformed mutual information metrics to estimate signal volume, signal-to-noise ratio (SNR), intrinsic rank, and linear sufficiency in dirty high-dimensional datasets. The tool is currently available as an R function, with Python and R packages planned for release soon. This addresses a critical practitioner pain point: determining whether noisy, real-world high-dimensional data contains enough signal to support reliable modeling, without relying on the strict parametric or distance-based assumptions of traditional PCA. By using an information-theoretic approach, it broadens applicability to datasets where linear variance decomposition may fail. Entropic Scree is explicitly described as a diagnostic oracle rather than a linear projection matrix, meaning users should not project raw data onto extracted eigenvectors via standard dot products. It also identifies decoupled sub-networks of variables and serves as a practical diagnostic for the 'From Garbage to Gold' framework, which explores when uncurated, error-prone data can still yield accurate prediction models.

reddit · r/MachineLearning · /u/Chocolate_Milk_Son · Aug 31, 12:02

**Background**: Mutual information is an information-theoretic measure that quantifies the statistical dependency between variables without assuming linearity or specific distance metrics. Traditional PCA relies on linear variance and Euclidean distance assumptions, which may not hold for messy real-world data with non-linear relationships. The intrinsic rank of a dataset refers to the minimum number of dimensions needed to capture its essential structure, a concept central to dimensionality reduction. The 'From Garbage to Gold' framework proposes that even uncurated, error-prone data can be used directly for accurate prediction under certain conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tjleestjohn/Entropic-Scree">GitHub - tjleestjohn/Entropic-Scree: A non-parametric ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mutual_information">Mutual information - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#data-quality`, `#mutual-information`, `#dimensionality-reduction`, `#diagnostic-tools`, `#tabular-data`

---