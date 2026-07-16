---
layout: default
title: "Horizon Summary: 2026-07-16 (EN)"
date: 2026-07-16
lang: en
---

> From 18 items, 10 important content pieces were selected

---

1. [Thinking Machines Launches Open-Weights Multimodal Model Inkling with Audio Support](#item-1) ⭐️ 8.0/10
2. [Stripe and Advent Jointly Offer to Acquire PayPal](#item-2) ⭐️ 8.0/10
3. [Running Gemma 4 26B on Legacy CPU Without GPU](#item-3) ⭐️ 8.0/10
4. [Firefox Runs Entirely in WebAssembly: Technical Demo](#item-4) ⭐️ 8.0/10
5. [Claude's web_fetch Vulnerability Enables Data Exfiltration](#item-5) ⭐️ 8.0/10
6. [xAI Open Sources Grok Build, Sparking Privacy and Trust Debate](#item-6) ⭐️ 7.0/10
7. [Telegram Data Center Infrastructure: Security Concerns and Technical Debt Revealed](#item-7) ⭐️ 7.0/10
8. [Seeking Critiques of JEPA and World Models in Robot Learning](#item-8) ⭐️ 7.0/10
9. [Mechanistic Interpretability: Disentangling Convolutional Neurons via Hadamard Product](#item-9) ⭐️ 6.0/10
10. [Does Edge Against Closing Lines Transfer to Earlier Sports Bets?](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Thinking Machines Launches Open-Weights Multimodal Model Inkling with Audio Support](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines released Inkling, an open-weight multimodal model with 975B parameters (41B active) and a 1M-token context window, natively supporting text, image, and audio inputs. It was trained on 45 trillion tokens of multimodal data and offers local deployment via tools like llama.cpp and Unsloth. As one of the largest open-weight models with audio capabilities, Inkling enables enterprises to customize frontier-level AI for specific tasks while retaining data privacy. Its release intensifies the US-China AI competition by offering a viable alternative to Chinese models like DeepSeek. Inkling uses a Mixture-of-Experts architecture and integrates with Thinking Machines' Tinker platform for fine-tuning. While not the strongest overall model, its multimodal efficiency and open-weight accessibility make it ideal for customization. The company employs an 'open base + proprietary fine-tuning' business model.

hackernews · vimarsh6739 · Jul 15, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48924912)

**Background**: Open-weight models release trained parameters but not full source code, differing from fully open-source AI. Thinking Machines, founded by ex-OpenAI CTO Mira Murati in 2025, raised $2B at a $12B valuation. Inkling's 1M-context window and audio support address gaps in existing open models, which often lack multimodal integration or long-context capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://huggingface.co/blog/thinkingmachines-inkling">Welcome Inkling by Thinking Machines</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thinking_Machines_Lab">Thinking Machines Lab - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Users praised Inkling's audio capabilities and local deployment options, with some comparing it favorably to Chinese models like DeepSeek. Discussions highlighted its strategic role in the US AI ecosystem and the complexity of modern model development. Critics noted it's not the strongest model but valued its customization potential.

**Tags**: `#Open Source AI`, `#Multimodal Models`, `#Thinking Machines`, `#LLM`, `#AI Strategy`

---

<a id="item-2"></a>
## [Stripe and Advent Jointly Offer to Acquire PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 8.0/10

Stripe and investment firm Advent have reportedly submitted a joint offer to acquire PayPal for more than $53 billion. This potential merger would consolidate major players in the digital payments space under one umbrella. This deal could significantly reshape the fintech landscape, raising concerns about market consolidation and potential antitrust scrutiny due to the combined market share. It may impact transaction fees and service policies for merchants and consumers relying on these platforms. The proposed acquisition value exceeds $53 billion, and the combined entity would include brands like Venmo and Braintree. Antitrust regulators may require divestitures, such as unwinding Venmo or Braintree, to approve the deal.

hackernews · rvz · Jul 15, 03:32 · [Discussion](https://news.ycombinator.com/item?id=48915953)

**Background**: PayPal is a long-standing digital payments company, while Stripe is a major provider of online payment processing for internet businesses. Advent is a private equity firm known for large-scale investments. Mergers of this scale often face regulatory hurdles to prevent monopolistic practices.

**Discussion**: Community members expressed concern over potential fee increases and reduced competition, noting that Stripe and Braintree are direct competitors. Some users highlighted risks regarding account flagging and policy restrictions, particularly for industries like cannabis or adult services. Others pointed out that antitrust approval would be difficult due to high market concentration metrics like the Herfindahl-Hirschman Index.

**Tags**: `#Fintech`, `#Payments`, `#M&A`, `#Antitrust`, `#Stripe`

---

<a id="item-3"></a>
## [Running Gemma 4 26B on Legacy CPU Without GPU](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

A technical demonstration shows Gemma 4 26B running at 5 tokens per second on a 13-year-old Xeon CPU without any GPU, proving large language models can operate on legacy hardware. This benchmark challenges the assumption that modern LLMs require expensive GPU hardware, opening possibilities for local inference on older systems and sparking debate about cost-efficiency between local and cloud inference. The demonstration achieves 5 tokens per second on a 13-year-old Xeon processor with no GPU acceleration, while community members report varying speeds from 7-12 tokens per second on similar hardware depending on configuration.

hackernews · neomindryan · Jul 15, 15:34 · [Discussion](https://news.ycombinator.com/item?id=48922434)

**Background**: Large language models like Gemma 4 26B typically require substantial computational resources, with most deployments relying on modern GPUs for efficient inference. CPU-only inference has historically been considered impractical for large models due to memory bandwidth and computational limitations. The Gemma series is Google's open-weight model family, with 26B referring to 26 billion parameters.

**Discussion**: Community members debate the cost-efficiency of local versus cloud inference, with some calculating that cloud providers offer cheaper per-token costs despite slower local speeds. Others share their own benchmarks showing higher speeds on similar hardware and predict continued improvements in model efficiency, with one user forecasting >200B MoE models on consumer hardware by mid-2027.

**Tags**: `#LLM`, `#Local Inference`, `#Hardware Optimization`, `#Cost Analysis`, `#Gemma`

---

<a id="item-4"></a>
## [Firefox Runs Entirely in WebAssembly: Technical Demo](https://developer.puter.com/labs/firefox-wasm/) ⭐️ 8.0/10

The entire Firefox browser engine, including Gecko and SpiderMonkey, has been compiled to WebAssembly and runs within a canvas element, featuring end-to-end encryption via the WISP protocol and experimental JIT optimizations. This breakthrough demonstrates WebAssembly's potential to host complex applications like full browsers, which could revolutionize secure environments such as locked-down TV operating systems or air-gapped systems. The project required over 25,000 tokens for debugging and JIT research, uses a novel WASM-to-JS JIT compiler, and necessitates a Firefox flag for WASM extensions. A more RAM-efficient alternative, browser.js, is also available.

hackernews · coolelectronics · Jul 15, 21:00 · [Discussion](https://news.ycombinator.com/item?id=48926939)

**Background**: WebAssembly (WASM) is a binary instruction format enabling near-native performance in browsers. Gecko is Firefox's rendering engine, while SpiderMonkey is its JavaScript engine. The WISP protocol proxies TCP/UDP over WebSockets for secure communication.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpiderMonkey_(Javascript_engine)">SpiderMonkey (Javascript engine)</a></li>

</ul>
</details>

**Discussion**: Users highlighted practical use cases like bypassing ad-blocker restrictions on locked-down TV OSes (e.g., VIDAA), questioned the $25k cost for a 'fun experiment,' and raised technical concerns about WASM extension dependencies and polyfill limitations.

**Tags**: `#WebAssembly`, `#Firefox`, `#Browser Engineering`, `#JIT Compilation`, `#Security`

---

<a id="item-5"></a>
## [Claude's web_fetch Vulnerability Enables Data Exfiltration](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Security researcher Ayush Paul discovered a loophole in Claude's web_fetch tool that bypasses existing safeguards, allowing attackers to exfiltrate user data through nested links in fetched web pages. The attack successfully extracted sensitive information like user names and locations. This vulnerability undermines trust in AI tool security, demonstrating how even well-designed safeguards can be circumvented. It highlights risks in AI systems with access to private data and external tools, impacting user privacy and industry safety standards. The attack exploited web_fetch's ability to follow links within previously fetched pages, using a honeypot site with nested URLs to extract data. Anthropic patched the issue by restricting web_fetch to only user-provided or search-result URLs.

rss · Simon Willison · Jul 15, 14:21

**Background**: The 'lethal trifecta' refers to AI systems combining private data access, untrusted external content, and outbound actions—creating exfiltration risks. Claude's web_fetch tool was designed to mitigate this by only allowing navigation to user-entered or search-result URLs, but the loophole bypassed this restriction.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>
<li><a href="https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Docs</a></li>
<li><a href="https://arxiv.org/pdf/2604.05432">Your LLM Agent Can Leak Your Data: Data Exfiltration via ...</a></li>

</ul>
</details>

**Discussion**: Hacker News discussions emphasized concerns about AI security flaws and the effectiveness of current safeguards. Users debated whether tool-use restrictions alone can prevent sophisticated attacks, with some advocating for stricter isolation between data access and external actions.

**Tags**: `#AI Security`, `#Claude`, `#Data Exfiltration`, `#Simon Willison`, `#Tool Use`

---

<a id="item-6"></a>
## [xAI Open Sources Grok Build, Sparking Privacy and Trust Debate](https://github.com/xai-org/grok-build) ⭐️ 7.0/10

xAI has announced the open sourcing of Grok Build, making the codebase publicly available on GitHub. This move comes amid ongoing scrutiny over the company's data handling practices and previous privacy controversies. This open-source release could significantly impact the AI development ecosystem by providing developers with access to xAI's tooling, but it also raises questions about whether transparency can rebuild trust after data privacy concerns. The decision may influence how other AI companies approach open-source strategies. The community response has focused less on technical novelty and more on corporate trustworthiness, with users questioning xAI's motives and demanding independent verification of data deletion claims. Some developers are recommending alternative platforms like pi.dev over Grok Build.

hackernews · skp1995 · Jul 15, 20:24 · [Discussion](https://news.ycombinator.com/item?id=48926590)

**Background**: xAI is an artificial intelligence company founded by Elon Musk, known for developing the Grok AI assistant. Open sourcing refers to making software source code publicly available for anyone to view, modify, and distribute. In the AI industry, open-source releases are often seen as ways to build community trust and accelerate development, though they can also be strategic moves to improve reputation after controversies.

**Discussion**: Community sentiment is largely skeptical, with users viewing the open-source move as a tactical reputation repair rather than genuine transparency. Key concerns include the lack of independent certification for data deletion claims and questions about xAI's motives given their market position. Some commenters recommend alternative platforms, while others demand third-party verification before trusting the company again.

**Tags**: `#AI`, `#Open Source`, `#xAI`, `#Data Privacy`, `#Industry News`

---

<a id="item-7"></a>
## [Telegram Data Center Infrastructure: Security Concerns and Technical Debt Revealed](https://dev.moe/en/3025) ⭐️ 7.0/10

A Hacker News discussion analyzed Telegram's data center infrastructure, revealing regional distribution patterns, significant technical debt in custom code, and alarming security concerns about potential FSB involvement in infrastructure management. This matters because it exposes potential security vulnerabilities in a widely-used messaging platform, raises questions about data sovereignty and surveillance risks, and highlights architectural decisions that create maintenance burdens and single points of failure. Community members noted that DC2 serves Russian and Ukrainian users, DC5 frequently experiences downtime affecting Chinese users, and DC3's status remains unclear—possibly deprecated or reserved for special data flows. The infrastructure reportedly uses extensive custom code requiring developers to learn proprietary systems.

hackernews · theanonymousone · Jul 15, 13:22 · [Discussion](https://news.ycombinator.com/item?id=48920475)

**Background**: Telegram is a cloud-based instant messaging platform known for its distributed architecture with multiple data centers (DCs) worldwide. Each data center handles specific geographic regions or user populations, and the platform's infrastructure design has been a subject of technical discussion due to its custom-built systems rather than standard distributed database solutions.

**Discussion**: The community discussion revealed serious security concerns, with one user citing investigations showing Telegram's infrastructure is managed by someone who also manages FSB infrastructure without employee knowledge. Others criticized the technical debt and custom code complexity, while some noted regional service patterns and questioned whether certain data centers serve special purposes.

**Tags**: `#Telegram`, `#Infrastructure`, `#Security`, `#Distributed Systems`, `#Hacker News`

---

<a id="item-8"></a>
## [Seeking Critiques of JEPA and World Models in Robot Learning](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 7.0/10

A researcher is requesting critical analysis and potential downsides of Yann LeCun's JEPA and world model approaches for robot learning, highlighting concerns about their overhyped claims compared to other AI paradigms. This debate is significant as JEPA and world models represent a potential paradigm shift in AI research, challenging dominant approaches like LLMs and reinforcement learning, which could reshape future robotics and AI development. The researcher notes LeCun's dismissive stance toward LLMs and RL while promoting JEPA as the 'only next big thing,' prompting scrutiny of its technical limitations and practical viability in real-world robotics applications.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · Jul 15, 17:34

**Background**: JEPA (Joint Embedding Predictive Architecture) is Yann LeCun's proposed framework for building predictive models that learn representations by predicting future states in latent space. World models aim to simulate environments for planning, contrasting with LLMs' text-centric approaches and RL's trial-and-error learning.

**Tags**: `#JEPA`, `#World Models`, `#Robot Learning`, `#AI Research`, `#Yann LeCun`

---

<a id="item-9"></a>
## [Mechanistic Interpretability: Disentangling Convolutional Neurons via Hadamard Product](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 6.0/10

An independent researcher introduced a novel method using the Hadamard product to analyze individual 1x1 convolutional neurons in InceptionV1, revealing monosemantic feature clusters (e.g., cars, cats) and dependent neuron activation patterns where low-value clusters (e.g., letters) share firing concepts with balanced positive/negative weights. This work advances mechanistic interpretability for convolutional networks, which are less studied than transformers, potentially improving transparency in CNN-based AI systems and informing how gradient descent organizes features in noisy activation ranges. The method clusters Hadamard products of receptive fields and neuron weights to identify monosemantic patterns, but findings remain preliminary without peer review. The discovery of dependent neurons firing on shared concepts with balanced weights suggests deliberate gradient descent behavior.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability studies neural networks by reverse-engineering their internal structures. The Hadamard product is an element-wise matrix multiplication used here to isolate neuron-specific feature detection. Monosemantic features refer to neurons activating for single concepts (e.g., 'cats'), while dependent neurons exhibit coordinated firing patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>
<li><a href="https://www.neelnanda.io/mechanistic-interpretability/glossary">A Comprehensive Mechanistic Interpretability Explainer & Glossary — Neel Nanda</a></li>

</ul>
</details>

**Tags**: `#mechanistic-interpretability`, `#neural-networks`, `#convolutional-neurons`, `#feature-analysis`, `#inceptionv1`

---

<a id="item-10"></a>
## [Does Edge Against Closing Lines Transfer to Earlier Sports Bets?](https://www.reddit.com/r/MachineLearning/comments/1ux1n0v/if_your_model_finds_edge_against_closing_lines/) ⭐️ 6.0/10

A sports prediction modeler on Reddit is questioning whether consistent edge found against closing lines in backtesting transfers to live predictions made 12-24 hours before events when line movement features are incomplete. This paradox represents a genuine challenge for ML practitioners in sports betting and forecasting domains, as it questions the validity of backtesting methodologies when feature availability differs between training and inference phases. The modeler's strongest feature is line movement from opening to closing implied probability, but at prediction time this feature is incomplete since the market hasn't fully moved yet, creating a tension between backtest performance and real-world applicability.

reddit · r/MachineLearning · /u/MrProbability101 · Jul 15, 10:11

**Background**: Closing Line Value (CLV) measures the difference between the odds you bet at and the final closing line, serving as the gold standard for measuring betting skill. Implied probability converts betting odds into win percentages, while sharp money refers to bets placed by professional winning bettors that sportsbooks track closely. Closing lines are considered nearly impossible to beat because they aggregate all available information including sharp money and injury news.

<details><summary>References</summary>
<ul>
<li><a href="https://pricearb.com/glossary/clv">CLV - Closing Line Value - Sports Betting Glossary | PriceArb</a></li>
<li><a href="https://oddsindex.com/guides/implied-probability-calculator">Implied Probability Calculator: Odds to Percentage | OddsIndex</a></li>
<li><a href="https://www.bettingpros.com/articles/what-is-sharp-money-how-to-follow-where-the-pros-bet/">What Is Sharp Money? How to Follow Where the Pros Bet | BettingPros</a></li>

</ul>
</details>

**Tags**: `#sports-betting`, `#prediction-models`, `#market-efficiency`, `#feature-engineering`, `#backtesting`

---