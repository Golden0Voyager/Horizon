---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 42 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [Python 3.15 发布：PEP 810 显式懒加载与内置采样分析器](#item-tech-news-1) ⭐️ 9.0/10
2. [黑客利用丹佛斯控制器漏洞瘫痪欧洲超市冷柜](#item-tech-news-2) ⭐️ 7.0/10
3. [WiFi 7 路由器改造为 320 Msps 软件定义无线电接收器](#item-tech-news-3) ⭐️ 7.0/10
4. [Meta 发布 Muse Wonder 模型](#item-tech-news-4) ⭐️ 7.0/10
5. [Looped Diffusion Transformer：共享块在每步去噪中循环复用，采样时可调节循环深度](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic 称蒸馏防护使数据提取减少 90%–99%](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [克利夫兰联储主席哈马克暗示可能进一步加息](#item-finance-news-1) ⭐️ 7.0/10
2. [中欧就混动、电动汽车贸易达成共识](#item-finance-news-2) ⭐️ 7.0/10
3. [新能源汽车出口退税率由 13%下调至 9%](#item-finance-news-3) ⭐️ 7.0/10
4. [税务处罚新裁量基准 11 月施行，社保欠缴最高罚 3 倍](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Python 3.15 发布：PEP 810 显式懒加载与内置采样分析器](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 9.0/10

Python 3.15 正式发布，同时 Python 3.10 结束支持，跨版本维护者可以开始使用 3.11 引入的特性。本次发布由 3.14 与 3.15 发布经理 Hugo van Kemenade 编写 What&\#x27;s New 指南，重点包括 PEP 810 显式懒加载（\`lazy import json\`、\`lazy from pathlib import Path\`，符号首次使用时才真正导入模块）、PEP 798 推导式解包（\`\[\*L for L in lists\]\`、\`\{\*\*d for d in dicts\}\` 等语法，扩展自 2015 年 Python 3.5 的 PEP 448），以及标准库新增的采样分析器 Tachyon（\`profiling.sampling\`），原 \`cProfile\` 更名为 \`profiling.tracing\`。Simon Willison 指出懒加载直接解决了其 LLM CLI 工具因插件依赖（如 \`sentence\_transformers\`）导致的启动延迟问题；Miguel Grinberg 对 3.15.0rc3 的基准测试显示整体性能与 3.14 基本持平，仅实验性 JIT 在 Fibonacci 测试上带来 1.2 倍提升，这是其首次观察到 JIT 有实质性能收益。

rss · Simon Willison · 10月12日 18:15

**「背景」** Python 3.15 是继 3.14 之后的下一个主要版本，3.14 于前一年发布，相比 3.13 在多个类别上带来了显著的性能提升。新增的推导式解包语法（PEP 798）是对 PEP 448 的扩展，后者于 2015 年随 Python 3.5 引入。采样分析器此前需要借助 py-spy 等外部工具，Python 3.15 将该能力直接集成到标准库中，命名为 profiling.sampling。

**「对开发者的具体影响」** 维护跨版本 Python 软件的开发者必须停止支持 Python 3.10，并可将最低版本要求提升至 3.11，从而使用 3.11 引入的新特性。此外，PEP 810 的显式延迟导入（\`lazy import\`）直接解决了插件类工具因加载重型依赖（如 \`sentence\_transformers\`）导致的启动延迟问题，开发者可在插件文档中改用该语法替代手动延迟导入。标准库新增的 Tachyon 采样分析器（\`profiling.sampling\`）也意味着此前依赖 py-spy 等外部工具进行运行时性能分析的场景，现在可直接使用内置模块完成，无需额外安装。

**标签**: `#Python`, `#language-release`, `#PEP-810`, `#software-engineering`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [黑客利用丹佛斯控制器漏洞瘫痪欧洲超市冷柜](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 7.0/10

2026 年 10 月 12 日，黑客利用丹佛斯（Danfoss）制冷控制器的已知漏洞远程激活欧洲多家超市的自动除霜功能，导致法国 Intermarche 等连锁 150 余家门店冷柜停机，供应链和门店价格亦受波及。涉事控制器包括已停止支持的 SM800（2021 年 EOS）和 SC355（2016 年 EOS）等型号，服役年限达 15 至 20 年，Claroty Team82 此前已公开披露相关漏洞研究。丹佛斯官方营销材料曾主动推广将冷柜控制器接入互联网以实现远程诊断和能效管理，为攻击面提供了便利；2026 年 8 月美国多个军事基地冷冻设备也曾发生类似事件，社区推测两者可能关联。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**「背景」** 丹佛斯（Danfoss）AK‑SM 800A 系列冷藏控制器内嵌网页管理界面，曾被 Team 82 研究发现多个漏洞，其中包括可绕过身份验证的缺陷，攻击者可利用这些漏洞远程触发自动除霜功能。这些控制器在欧洲许多超市中已使用 15‑20 年，因成本考虑尚未更换，因而成为攻击目标。

**「影响」** 10 月 11 日至 12 日夜间，法国 Intermarché、E.Leclerc 和 Système U 等连锁的 150 余家门店的 Danfoss 联网制冷控制器被远程触发自动除霜，冷冻食品库存大面积损毁，配送与门店价格同步受冲击。零售商应立即排查仍在使用的 Danfoss 制冷控制器是否存在已知 CVE，并评估将联网制冷设备纳入 OT 安全审计的必要性。

**「社区讨论」** 评论者指出，超市因利润微薄无力承担安全审查和设备定期更换成本，导致已知漏洞长期存在。另有评论者以医院实验室设备为例，说明工业设备联网已成趋势——部分新设备需付费订阅才能运行，&quot;为何要把冷柜联网&quot;的质疑忽视了这一现实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers">Freeze the Controller , Defrost the Food: Uncovering Vulnerabilities in...</a></li>
<li><a href="https://www.linkedin.com/posts/claroty_team82-activity-7330549882962735105-h-MB">Danfoss fixes AK-SM8xxA Series cooler controllers vulnerability</a></li>
<li><a href="https://cybernews.com/security/danfoss-refrigeration-hack-france-supermarkets/">Refrigeration Cyberattack Hits French Supermarkets | Cybernews</a></li>
<li><a href="https://cybersecuritynews.com/supermarket-fridges-hacked/">Attackers Reportedly Hack Supermarket Fridges and Raise ...</a></li>
<li><a href="https://shattered.io/french-supermarket-fridge-cyberattack-2026/">French Supermarket Fridge Cyberattack Hits 150 Stores</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#IoT-security`, `#OT-vulnerabilities`, `#supply-chain`, `#retail-tech`

---

<a id="item-tech-news-3"></a>
### [WiFi 7 路由器改造为 320 Msps 软件定义无线电接收器](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 7.0/10

开源项目 w1700k-sdr 将 WiFi 7 路由器硬件改造为工作在 5 GHz 频段、采样率达 320 Msps 的软件定义无线电（SDR）接收器。该项目由开发者 h0m3us3r 发布在 GitHub 上，此前该开发者已将 ESP32 微控制器改造为 SDR（eSpDR 项目）。项目利用消费级 WiFi 7 路由器的射频前端和高速数据接口，实现了传统上需要专用硬件才能达到的采样率，大幅降低了高性能 SDR 的入门门槛。

hackernews · djfergus · 10月12日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**「背景」** 同一开发者 h0m3us3r 此前已发布 eSpDR 项目，将 ESP32-S3 微控制器改造为 80 Msps 的 SDR 接收器，通过原始基带 IQ 数据流传输至 Linux 主机。近期多个独立项目也陆续发现 ESP32 系列芯片具备隐藏的 SDR 能力，覆盖 2.2–2.7 GHz 及 4.8–6.0 GHz 频段，采样率最高可达 80 MS/s。本次 w1700k-sdr 项目将这一思路从微控制器扩展到 WiFi 7 路由器，采样率提升至 320 Msps，工作频段为 5 GHz。

**「降低高性能 SDR 入门门槛」** 该项目使业余无线电爱好者和研究者能够利用消费级 WiFi 7 路由器硬件获得 5 GHz 频段 320 Msps 采样率，相比商用 SDR 接收机大幅降低了高性能 SDR 的入门成本。社区成员还推测该方案可能兼容采用相同芯片组的 Banana Pi R4 等设备，但尚未得到官方确认。

**「社区讨论」** 社区讨论集中在硬件兼容性和实际应用场景上。有用户指出该项目使用的芯片组与 Banana Pi R4 相同，推测可在该设备上运行；另有用户提到该开发者此前已将 ESP32 改造为 SDR，期待更多消费级 WiFi 设备被改造为 SDR。还有用户讨论了该技术在服务监视器制造领域的潜在应用，认为结合 CNC 加工、廉价 PCB 和通用元件，可以大幅降低专业无线电设备的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/h0m3us3r/eSpDR">GitHub - h 0 m 3 us 3 r / eSpDR · GitHub</a></li>
<li><a href="https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/">Various Projects Independently Find Hidden SDR Capabilities in...</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_software-defined_radios">List of software-defined radios - Wikipedia</a></li>
<li><a href="https://signalens.com/compare/">Comparison - Signalens Ltd.</a></li>

</ul>
</details>

**标签**: `#SDR`, `#WiFi 7`, `#hardware-hacking`, `#open-source`, `#radio-engineering`

---

<a id="item-tech-news-4"></a>
### [Meta 发布 Muse Wonder 模型](https://research.meta.ai/blog/muse-wonder) ⭐️ 7.0/10

Meta 于 2026 年 10 月 12 日在 research.meta.ai 发布了 Muse Wonder，一款新的 AI 模型。由于源内容不可用，官方技术规格无法确认，但社区讨论（550 分，303 条评论）显示评价分化，涉及数据安全和实际性能两个主要关切。社区还将 Muse Wonder 与 8 月的 Muse Spark 1.2 和 9 月的 Muse 1.3 进行了对比。

hackernews · meetpateltech · 10月12日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=50059115)

**「背景」** Meta 的超级智能实验室在经历了约 14 个月的内部 AI 组织重组后，于 2026 年 10 月 12 日发布了 Muse Wonder 和 Muse Wonder Full，这是 Meta 首次推出前沿模型，也是其首次公开宣称模型性能可与行业前沿水平持平。

**「用户数据隐私泄露风险」** 社区成员报告在使用 Meta 账户登录 Muse Wonder 时，登录界面出现他人的个人资料和电子邮件，且账户设置页面无法访问，导致个人信息可能被他人看到并可能收到垃圾登录信息。这表明当前的登录流程存在数据暴露漏洞，用户应避免直接使用 Meta 账户登录或及时检查账户安全设置以防止隐私泄露。

**「社区讨论」** 用户 pmuse 报告在 Muse Code 站点登录时看到他人个人资料和邮箱，且无法访问账户设置来停用账户，疑似存在数据暴露漏洞；用户 jjcm 的独立 Image-to-HTML 测试显示 Muse Wonder 远逊于 Opus 5.5，更接近 Sonnet 或 Haiku 水平。另有用户 atleastoptimal 从战略角度认为，前沿 AI 领域有多家公司竞争比单一公司主导更有利于避免权力过度集中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://trendintech.com/meta-muse-wonder-ai-frontier-model-2026/">Meta Muse Wonder AI Model: Frontier Launch Explained [2026]</a></li>
<li><a href="https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/">Meta releases its first frontier model, Muse Wonder - TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI model release`, `#Meta AI`, `#multimodal models`, `#open source AI`, `#community benchmarks`

---

<a id="item-tech-news-5"></a>
### [Looped Diffusion Transformer：共享块在每步去噪中循环复用，采样时可调节循环深度](https://www.reddit.com/r/MachineLearning/comments/1x49d61/looped_diffusion_transformer_the_same_blocks_run/) ⭐️ 7.0/10

一篇研究论文（arXiv 2609.40305，9 月 30 日）提出了一种循环扩散 Transformer 架构：在每个去噪步骤内，将一组共享的 Transformer 块重复运行多次，而非通过扩大模型规模来提升质量。作者指出朴素的循环复用并不能可靠地带来收益，因此引入了对每个循环的深层监督（deep supervision）和自调制注意力（self-modulating attention）来修复这一问题。论文的核心主张是：一个 260M 参数的循环模型在多个基准上优于一个 6.5 倍大的模型，同时推理计算量减少 4.9 倍；在固定推理预算下，增加循环深度比增加去噪步数更有效。代码和权重以 MIT 协议开源（权重托管在 Hugging Face 的 sensenova 账号下）。发帖者在 M5 Pro 上进行了独立验证：PyTorch MPS、fp32、100 步 Euler、CFG 6.0、每个提示词一个种子，循环深度从 1 到 4 对比。模型在深度 4 下训练，README 称其他深度无需重新训练即可使用。验证结果显示，大部分质量变化发生在深度 3 之前，深度 3 和 4 在所有展示的提示词上结果非常接近。在该机器上，深度 1 每张图约 23–24 秒，深度 4 约 43–47 秒。不过，验证范围有限（仅 5 个提示词、单一种子），arXiv 编号 2609.40305 对应的日期（2026 年 9 月）在发布时点尚未到来，且效率主张均为作者自报，尚需更广泛的基准测试来确认。

reddit · r/MachineLearning · /u/Fit-Ant2238 · 10月12日 18:13

**「背景」** 扩散 Transformer（DiT）通常通过增加参数量和层数来提升生成质量，但推理计算成本随之线性增长。循环 Transformer 的概念可追溯至 2018 年的 Universal Transformers，其核心思想是复用同一组权重块多次以加深计算深度而不增加参数量。Looped-DiT 将这一思路引入扩散模型，在 MiniT2I（基于 MMDiT 的像素空间去噪器）基础上，通过在每个去噪步骤内多次运行共享 Transformer 块来扩展计算深度，并引入深度监督与自调制注意力机制以稳定循环特征更新。

**「对实践者的意义」** 对于从事扩散模型效率优化的研究者，该架构提供了一种在推理时按需调节计算量的新手段：循环深度可在采样时选择，类似于循环和递归深度语言模型中的迭代次数，从而在单张图像上实现计算与精度的权衡。然而，当前验证仅覆盖 5 个提示词和单一随机种子，且效率数据为作者自报，在更广泛的基准和多种子条件下确认之前，不宜将其视为已确立的范式转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.40305">[ 2609 . 40305 ] Looped Diffusion Transformer</a></li>
<li><a href="https://arxiv.org/html/2609.40305">Looped Diffusion Transformer</a></li>
<li><a href="https://github.com/asimfish/awesome_loop_transformer">Awesome Loop Transformer: Looped Transformers, Recurrent ...</a></li>

</ul>
</details>

**标签**: `#diffusion-transformers`, `#model-efficiency`, `#architecture-design`, `#open-source`, `#research-paper`

---

<a id="item-tech-news-6"></a>
### [Anthropic 称蒸馏防护使数据提取减少 90%–99%](https://www.anthropic.com/research/distillation-defenses) ⭐️ 7.0/10

Anthropic 于 10 月 12 日披露，其针对窃取 Claude 能力的模型蒸馏攻击所部署的新防护措施，初步证据显示已使被提取数据减少约 90% 至 99%。公司称已封禁数万相关账号，部分账号发起攻击后不到两小时即被封禁。具体措施包括限制推理内容跨会话、跨模型和跨账号流转，部署双阶段分类器并持续修补绕过手法，误报率低于 0.1%。Anthropic 同时提示，部分开发者需更新集成，且被拦截的请求仍可能产生费用。

telegram · zaihuapd · 10月13日 01:25

**「相关背景」** 模型蒸馏是一种通过向 AI 模型发送大量查询来提取其能力的攻击手法。Anthropic 此前已多次披露针对 Claude 的蒸馏攻击：2026 年 2 月指控三家中国 AI 公司蒸馏 Claude，同年 9 月又报告了一起新的协调性能力提取行动。此次发布的防护措施正是针对这些攻击的回应。

**「开发者需更新集成并关注计费变化」** 使用 Claude API 的部分开发者需更新集成以适配新的跨会话、跨模型和跨账号限制，且被拦截的请求仍可能产生费用，直接影响依赖 Claude 能力的下游应用的请求逻辑和成本预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/ai-industry-has-data-problem-anthropic-just-made-ignore-dimitrova-5uvce">Who, What, How stole data from Anthropic</a></li>
<li><a href="https://www.remio.ai/post/anthropic-distillation-report-alleges-a-new-campaign-to-copy-claude">Anthropic Distillation Report Alleges a New Campaign to Copy Claude</a></li>
<li><a href="https://www.anthropic.com/research/distillation-defenses">Strengthening our defenses against distillation attacks</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#model distillation`, `#LLM security`, `#Anthropic`, `#IP protection`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [克利夫兰联储主席哈马克暗示可能进一步加息](https://www.cnbc.com/2026/10/12/beth-hammack-fed-inflation-policy.html) ⭐️ 7.0/10

克利夫兰联储主席贝丝·哈马克（美联储货币政策委员会投票成员）表示，可能需要进一步加息以应对持续高企的通胀，并警告若通胀居高不下，&quot;通胀心态&quot;可能在经济中根深蒂固。

rss · CNBC Finance · 10月13日 02:58

**「背景」** 美联储上月投票加息，为三年来首次。8 月个人消费支出物价指数（PCE，美联储偏好的通胀衡量指标）同比上涨 3.4%（核心 3%），市场定价显示下次会议维持利率不变的概率为 78%，但 12 月加息的概率接近 88%。

**标签**: `#monetary policy`, `#Federal Reserve`, `#inflation`, `#interest rates`, `#economic outlook`

---

<a id="item-finance-news-2"></a>
### [中欧就混动、电动汽车贸易达成共识](https://www.mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_4d502e1d49fd4480b39a6cfd0d752038.html) ⭐️ 7.0/10

中国商务部表示，中欧在贸易投资磋商机制下就混动汽车和电动汽车贸易达成多项共识。混动汽车安排以 2025 年为基础向上调整，中方配额不低于欧方其他进口来源地；电动汽车方面，欧方将继续推进企业价格承诺及复审程序。

telegram · zaihuapd · 10月12日 06:19

**「背景」** 欧盟此前对中国电动汽车发起反补贴调查并加征关税，双方于 2025 年中同意探索以价格承诺机制替代关税的方案，即中国车企自愿承诺最低出口价格。此后中欧技术团队于 2025 年 11 月在北京进行了五轮磋商，此次共识是这一谈判进程的延续。

**「影响」** 中国车企对欧出口获得配额保障，出口空间得到一定确定性；欧盟本土车企则继续面临来自中国的竞争压力，价格承诺复审结果将影响双方企业的实际成本与定价策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anybolt.com/2026/">AnyBolt: 2026</a></li>
<li><a href="https://www.electric-cars-china.com/news/china-china-eu-electric-vehicle-tariff-negoti-82573124.html">China : China - EU Electric Vehicle Tariff Negotiations Reach Technical...</a></li>

</ul>
</details>

**标签**: `#China-EU trade`, `#automotive industry`, `#trade policy`, `#electric vehicles`, `#tariff quotas`

---

<a id="item-finance-news-3"></a>
### [新能源汽车出口退税率由 13%下调至 9%](https://www.news.cn/20261012/9709731f470b42f9a84825c2e4eb914b/c.html) ⭐️ 7.0/10

财政部与税务总局 10 月 12 日联合公告，自 2027 年 4 月 1 日起，新能源汽车增值税出口退税率由 13%下调至 9%（降幅 4 个百分点），同时取消电子烟设备等产品出口退税。公告明确，涉及消费税的产品继续适用消费税退（免）税政策，不作调整。退税率下调将直接增加新能源汽车出口企业的税负成本，对出口利润率和国际价格竞争力构成压力。

telegram · zaihuapd · 10月12日 11:00

**「背景」** 出口退税是政府将出口商品在国内生产环节已缴纳的增值税退还给企业的制度，以提升中国产品的国际竞争力。此次调整是财政部和税务总局对部分产品出口退税政策的整体调整之一，同期还取消了电子烟设备等产品出口退税。

**「影响」** 中国新能源汽车出口企业将直接受影响：退税率下调 4 个百分点意味着每辆出口车的增值税退税金额减少，压缩出口利润空间；2025 年中国新能源汽车出口量为 261.5 万辆，2026 年上半年已达 235.5 万辆，出口规模庞大，政策调整对行业盈利影响显著。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bydtoday.com/china-nev-exports-surge-120-percent-h1-2026-caam/">China NEV Export Tracker: Data, Markets and Definitions</a></li>

</ul>
</details>

**标签**: `#fiscal policy`, `#new energy vehicles`, `#export tax rebate`, `#China`, `#industry regulation`

---

<a id="item-finance-news-4"></a>
### [税务处罚新裁量基准 11 月施行，社保欠缴最高罚 3 倍](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5252754/content.html) ⭐️ 7.0/10

国家税务总局发布《全国税务行政处罚裁量基准（2026 年版）》，自 2026 年 11 月 1 日起施行，将用人单位逾期不缴或少缴社保费纳入处罚事项，按欠缴金额和占比分档，最高罚款为欠缴金额的 3 倍。处罚前提是经责令限期缴纳后逾期仍不缴纳，还需补缴欠费并按日加收万分之五滞纳金。

telegram · zaihuapd · 10月13日 02:45

**「背景」** 该基准依据《行政处罚法》《税收征收管理法》及《社会保险法》制定，旨在规范税务行政处罚裁量权行使、助力全国统一大市场建设。其中按日加收万分之五的滞纳金为既有规定，本次新增的是将用人单位社保欠缴纳入可处罚事项。

**「影响」** 用人单位在被责令限期缴纳后仍未补缴社保费的，将面临最高三倍欠缴金额的罚款及日万分之五的滞纳金。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://beijing.chinatax.gov.cn/bjswj/sszc/zxwj/202610/ce51fc8f3ba5410fa1af98f433d7cf79.shtml">国家税务总局关于发布《全国税务行政处罚裁量基准（2026年版）》的公...</a></li>
<li><a href="https://www.163.com/dy/article/L928LA6H0550AVKV.html">欠缴社保，最高罚3倍！2026年11月1日起施行|法律|缴费人|裁量权|正负...</a></li>

</ul>
</details>

**标签**: `#tax policy`, `#social security`, `#regulatory enforcement`, `#China`, `#employer compliance`

---