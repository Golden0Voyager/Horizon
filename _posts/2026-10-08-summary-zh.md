---
layout: default
title: "Horizon Summary: 2026-10-08 (ZH)"
date: 2026-10-08
lang: zh
---

> 从 45 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [Claude Haiku 5.5 发布：可配置思考等级与分层定价](#item-tech-news-1) ⭐️ 8.0/10
2. [GPT-6 发布：系统卡记录安全回退与 UI 争议](#item-tech-news-2) ⭐️ 8.0/10
3. [Chrome 重新上线 JPEG XL 支持](#item-tech-news-3) ⭐️ 7.0/10
4. [God of War on PSP, recompiled to WebAssembly and running in the browser](#item-tech-news-4) ⭐️ 7.0/10
5. [谷歌与 Unity 合作推出自然语言 AI 游戏平台](#item-tech-news-5) ⭐️ 7.0/10
6. [Common Sense Media 称 ChatGPT for Teens 对儿童构成不可接受风险](#item-tech-news-6) ⭐️ 7.0/10
7. [谷歌向全球用户开放 SynthID AI 内容检测工具](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [美联储会议纪要显示官员预期年内再加息，但未明确时点](#item-finance-news-1) ⭐️ 8.0/10
2. [IMF 总裁：AI 既是增长希望也是通胀隐患](#item-finance-news-2) ⭐️ 8.0/10
3. [美股屡创新高，美国税收却难跟上](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude Haiku 5.5 发布：可配置思考等级与分层定价](https://www.anthropic.com/claude-haiku-5-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Haiku 5.5，引入可配置思考等级（low 到 max），允许开发者在质量、速度和成本之间灵活权衡。定价采用分层结构：输入在 10 万 token 以内为 $0.10/MTok，超出后为 $0.50/MTok；输出在 10 万 token 以内为 $0.50/MTok，超出后为 $2.50/MTok。此外，Anthropic 宣布为 Max 和 Team 订阅用户推出月度 API 额度（Max 5x 用户 $100/月，Max 20x 用户 $200/月，Team 订阅用户最高 $500 共享）。

hackernews · sfkgtbor · 10月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49996437)

**「背景」** Claude Haiku 是 Anthropic 的轻量级模型系列，前代 Haiku 4.5 主要面向低延迟、低成本的推理场景。此次发布的 Haiku 5.5 引入了可配置的 thinking 等级（low 到 max），让开发者在质量、速度和成本之间做权衡；同时定价采用 100k token 分档结构，100k 以内输入 $0.10/MTok、输出 $0.50/MTok，超过 100k 则升至 $0.50 输入和 $2.50 输出。此外，Anthropic 本周起向 Max 和 Team 订阅者发放月度 API 额度（Max 5x 为 $100、Max 20x 为 $200、Team 最高 $500 池化），这是订阅体系与 Claude Platform 计费首次打通。

**「影响」** 开发者在使用 Claude Haiku 5.5 时会遇到输入或输出超过 100 k tokens 时费用突然跳升（输入从 0.10 USD/MTok 跳至 0.50 USD/MTok，输出从 0.50 USD/MTok 跳至 2.50 USD/MTok），而可配置的思考级别（low‑max）则让他们在延迟、成本和质量之间进行权衡；与此同时，Max 和 Team 订阅用户每月获得固定额度的 API 积分（Max 5× 用户 100 USD，Max 20× 用户 200 USD，Team 用户最高 500 USD），这部分需抵消部分使用成本。

**「社区讨论」** simonw 用骑自行车的海鸥测试了不同思考等级，发现 low 等级会出错，而 medium 及以上均正确；max 耗时 5 分 9 秒、花费 3.38 美分，low 仅 7 秒、0.09 美分。minimaxir 批评 10 万 token 的分界点过低，对 Agent 场景不友好。chriddyp 的 DataAnalyticsBench 基准测试显示 Haiku 5.5 比 Haiku 4.5 便宜 9 倍且评分高 2 个等级，是完成考试最快的模型。charlesabarnes 认为月度 API 额度对订阅用户是重大利好，但担心这是为了缓解用户对定价上涨的不满。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/anthropic-claude-haiku-5-5-price-cut-2026/">Claude Haiku 5.5 Slashes Price 75% to $0.10/M [2026]</a></li>
<li><a href="https://www.datacamp.com/blog/claude-haiku-5-5">Claude Haiku 5.5: Features, Benchmarks, and Pricing</a></li>
<li><a href="https://artificialanalysis.ai/models/claude-haiku-5-5">Claude Haiku 5 . 5 (max) - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://benchlm.ai/compare/claude-haiku-5-5-vs-claude-sonnet-5-5">Claude Haiku 5 . 5 vs Claude Sonnet 5 . 5 : Benchmarks &amp; Cost</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-haiku-5.5">Claude Haiku 5 . 5 - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI models`, `#Anthropic`, `#LLM pricing`, `#model release`, `#thinking levels`

---

<a id="item-tech-news-2"></a>
### [GPT-6 发布：系统卡记录安全回退与 UI 争议](https://openai.com/index/gpt-6-for-everyone/) ⭐️ 8.0/10

OpenAI 发布了 GPT-6，并推出面向所有人的「智能 UI」。根据系统卡，与 GPT-5.6 相比，GPT-6 Sol（十月版）在标准自残评估上出现统计显著回退，GPT-6 Luna（十月版）在标准自残、血腥和性内容评估上均出现统计显著回退，极端主义视觉评估也有回退。该发布在 Hacker News 上获得 510 分、268 条评论，社区围绕 UI 设计选择、安全回退以及相对 GPT-5.6 的能力改进展开讨论。

hackernews · joshuawright11 · 10月7日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49996425)

**「背景」** GPT-5.6 于 2026 年 7 月 9 日发布，包含 Luna、Terra 和 Sol 三个变体，其中 Sol 于 9 月 10 日获得预览。GPT-6 是 OpenAI 的下一个主要版本，同样提供 Sol 和 Luna 变体，但系统卡将 10 月发布的新版本与仍在 Codex 和 ChatGPT Work 中使用的 9 月版本区分开来。GPT-6 在 ChatGPT 中整合了 Astra 的安全改进。

**「安全回退要求重新评估部署」** 系统卡明确记录 GPT-6 Sol 在标准自残评估上出现统计显著回退，GPT-6 Luna 在自残、血腥和性内容评估上均出现统计显著回退，Sol 在极端主义视觉评估上也有回退。对于在内容审核或消费者产品中部署这些模型的开发者，尽管 ZDNET 报道 Sol 准确率翻倍且成本减半、Luna 以更低成本匹配上一代高级模型性能，仍需重新评估安全基线，不能仅凭成本效益直接替换 GPT-5.6。

**「社区讨论」** 部分用户批评新 UI 设计，认为过多的空白和清单式布局显得居高临下，「像被当作小孩对待」；另有用户担忧 OpenAI 将工作功能与聊天合并的趋势，认为这与 Codex 高度相似，希望此类设计不会渗透到实际工作场景中。还有用户分享了与 GPT 交互的经验，认为逐句来回对话比阅读完整长文更有效，但指出模型有时会重复粘贴相同内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deploymentsafety.openai.com/gpt-6-october">GPT-6 Sol and GPT-6 Luna: October 2026 update - OpenAI Deployment ...</a></li>
<li><a href="https://cdn.openai.com/pdf/gpt-6-october.pdf">PDF GPT-6 Sol and GPT-6 Luna: October 2026 update - cdn.openai.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://openai.com/research/index/release/">OpenAI Research | Release</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI&#x27;s GPT - 6 Sol doubles its accuracy rate - for half the cost - ZDNET</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#OpenAI`, `#GPT-6`, `#Safety Evaluations`, `#Major Release`

---

<a id="item-tech-news-3"></a>
### [Chrome 重新上线 JPEG XL 支持](https://developer.chrome.com/blog/jpeg-xl-in-chrome) ⭐️ 7.0/10

Chrome 正在发布 JPEG XL 图像格式支持，这是在 Chrome 110 中移除该功能后的重大反转。Firefox 也计划在 10 月的稳定版中加入 JPEG XL 支持，若按计划推进，该格式将从仅 Safari 支持扩展到主流浏览器覆盖。需要注意的是，JPEG XL 在 CPU 受限环境下可能表现不佳，且与 AVIF 在某些场景（如高压缩率有损压缩）下存在性能差异。

hackernews · AshleysBrain · 10月7日 11:25 · [社区讨论](https://news.ycombinator.com/item?id=49991227)

**「背景」** JPEG XL 是由 Google 主导开发的现代图像格式，支持有损与无损压缩、HDR、动画等功能，被视为 WebP 的潜在替代方案。Chrome 曾在 Chrome 110 版本中移除了 JPEG XL 支持，此次重新加入标志着 Google 对该格式态度的转变。与此同时，Firefox 也计划在稳定版中加入 JPEG XL 支持，两大主流浏览器的支持将显著提升该格式在 Web 端的可用性。

**「对 Web 开发者的影响」** Chrome 155 与 Firefox 157 相继原生支持 JPEG XL 后，主流浏览器覆盖率显著提升，Web 开发者可将 JPEG XL 作为跨浏览器可用的现代图像格式，获得更好的压缩率和 HDR 支持。不过，社区讨论指出在 CPU 受限场景下 JPEG XL 解码可能带来性能压力，开发者需根据实际场景权衡选择。

**「社区讨论」** 社区对 Chrome 重新支持 JPEG XL 表示欢迎，认为此前 Chrome 不支持是该格式推广的主要障碍。关于 JPEG XL 与 AVIF 的对比，有观点认为 AVIF 在高压缩率有损压缩场景下略有优势，但 JPEG XL 的通用性更强；也有开发者表达了对图像格式碎片化的担忧，希望最终能统一为一种格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.neowin.net/news/google-chrome-155-brings-support-for-jpeg-xl-jxl/">Google Chrome 155 brings support for JPEG XL (.jxl) - Neowin</a></li>
<li><a href="https://www.techspot.com/downloads/19-mozilla-firefox.html">Mozilla Firefox Download Free - 157.0 | TechSpot</a></li>

</ul>
</details>

**标签**: `#image-formats`, `#web-development`, `#chrome`, `#jpeg-xl`, `#browser-standards`

---

<a id="item-tech-news-4"></a>
### [God of War on PSP, recompiled to WebAssembly and running in the browser](https://github.com/snuri00/psp-web-recomp) ⭐️ 7.0/10

A project recompiles PSP&\#x27;s God of War from MIPS machine code through C++ to WebAssembly, enabling it to run in the browser via a reimplementation of the PSP OS and graphics chip with WebGL2 rendering.

hackernews · sn001 · 10月7日 11:27 · [社区讨论](https://news.ycombinator.com/item?id=49991243)

**标签**: `#WebAssembly`, `#binary-translation`, `#game-emulation`, `#systems-programming`, `#open-source`

---

<a id="item-tech-news-5"></a>
### [谷歌与 Unity 合作推出自然语言 AI 游戏平台](https://blog.google/innovation-and-ai/technology/ai/playground-experimental-gaming-platform/) ⭐️ 7.0/10

谷歌与 Unity 宣布达成战略合作，共同推出面向互动娱乐的 AI 游戏平台，将谷歌的 AI 能力与 Unity 的 3D 游戏引擎结合。该平台允许创作者仅通过自然语言提示词生成、调试并实时体验可玩游戏，无需编写代码。双方还计划于年内推出深度整合工具“Unity Spark”，用于构建高精度 3D 场景与交互玩法。目前该消息来自谷歌官方博客的发布公告，尚未披露底层 AI 架构细节，也未说明 Unity Spark 的具体发布时间与可用性。

telegram · zaihuapd · 10月7日 13:10

**「背景」** Unity 是全球主流的 3D 游戏引擎，其官方披露每月约有 30 亿人游玩由 Unity 制作的游戏，但其中几乎没有人自己开发过游戏，因此 Unity 将“让游戏创作大众化”视为其创立使命。此次合作正是基于这一背景：谷歌提供 AI 能力与数十亿用户的产品生态，Unity 提供游戏引擎与开发经验，双方共同推出名为 Playground 的 AI 游戏平台，用户可用自然语言提示词生成可在浏览器中运行的游戏，目前在美国面向 18 岁及以上用户开放。

**「对游戏创作者的影响」** 该平台允许创作者无需编写代码，仅通过自然语言提示词即可生成、调试并实时体验可玩游戏，将游戏开发的技术门槛大幅降低。双方计划于年内推出的深度整合工具“Unity Spark”将进一步支持高精度 3D 场景与交互玩法的高效构建，使非专业开发者也能参与游戏创作。截至公告时，该平台与 Unity Spark 均处于计划阶段，尚未正式上线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/google-unity-ai-gaming-platform-playground-unity-spark-100726">Google and Unity launch AI game creation platform Playground</a></li>
<li><a href="https://investors.unity.com/news/news-details/2026/Google-and-Unity-Partner-on-New-AI-Gaming-Platform-for-the-Next-Era-of-Interactive-Entertainment/default.aspx">Unity Technologies - Google and Unity Partner on New AI ...</a></li>
<li><a href="https://www.gaming.net/google-launches-playground-ai-game-platform-with-unity-spark-to-follow/">Google Launches Playground AI Game Platform With Unity Spark ...</a></li>
<li><a href="https://investors.unity.com/news/news-details/2026/Google-and-Unity-Partner-on-New-AI-Gaming-Platform-for-the-Next-Era-of-Interactive-Entertainment/default.aspx">Unity Technologies - Google and Unity Partner on New AI Gaming Platform ...</a></li>
<li><a href="https://unity.com/news/google-and-unity-partner-on-new-ai-gaming-platform-for-the-next-era-of-interactive-entertainment">Google and Unity Partner on New AI Gaming Platform for the Next Era of ...</a></li>
<li><a href="https://www.straitstimes.com/world/google-unity-launch-platform-to-create-video-games-from-prompts">Google and Unity launch AI game creation platform | The Straits Times</a></li>

</ul>
</details>

**标签**: `#AI`, `#game development`, `#Google`, `#Unity`, `#natural language generation`

---

<a id="item-tech-news-6"></a>
### [Common Sense Media 称 ChatGPT for Teens 对儿童构成不可接受风险](https://www.bloomberg.com/news/articles/2026-10-07/chatgpt-for-teens-is-not-safe-for-kids-common-sense-media-report-says) ⭐️ 7.0/10

Common Sense Media 于 2026 年 10 月 7 日发布报告，指出面向 13‑17 岁用户的 ChatGPT for Teens 在涉及自杀、自残、饮食失调等危机对话时，常未及时或未通知家长，也未可靠建议求助，因而给出“不可接受风险”评级并呼吁 OpenAI 暂停推广。OpenAI 回应称该评估未能准确反映其防护机制的实际运作，可能是在家长控制功能上线前进行的测试，已请求对方重新测试；评估机构则坚持结论，认为家长提醒在危机场景下不可靠。该报告为独立第三方评估，而 OpenAI 的回应为供应商对方法论的异议，尚未有独立复测结果。

telegram · zaihuapd · 10月7日 14:20

**「背景」** Common Sense Media 是一家评估儿童与青少年媒体及科技产品的非营利组织，其青年人工智能安全研究所（Youth AI Safety Institute）专门负责 AI 安全评估。ChatGPT for Teens 是 OpenAI 面向 13 至 17 岁用户推出的青少年版产品，内置家长控制与危机干预机制。

**「对家长与部署方的实际影响」** Common Sense Media 的评估发现，ChatGPT for Teens 在涉及自杀、自残、饮食失调等危机对话时，家长提醒功能不可靠，且未稳定建议用户寻求专业帮助。这意味着 13 至 17 岁用户的家长不能仅依赖该产品的内置家长通知机制来应对孩子的心理健康危机。同时，OpenAI 反驳称测试可能发生在家长控制功能上线之前，双方对评估方法的分歧尚未解决，因此该产品的安全边界仍处于争议状态。对于考虑在青少年群体中部署或推广 ChatGPT for Teens 的学校、机构或政策制定者而言，这一争议意味着在独立验证完成前，不宜将其作为危机干预的可靠工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cryptopolitan.com/chatgpt-teens-parent-alerts-common-sense/">ChatGPT for Teens alerted parents late or never, Common Sense finds</a></li>
<li><a href="https://qz.com/common-sense-media-chatgpt-teens-unacceptable-risk-100726">Common Sense Media rates ChatGPT for Teens an unacceptable ...</a></li>
<li><a href="https://www.remio.ai/post/chatgpt-teen-safety-keeps-teens-talking-when-it-should-hand-off">ChatGPT Teen Safety Keeps Teens Talking When It Should Hand Off</a></li>
<li><a href="https://www.dailysabah.com/business/tech/chatgpt-for-teens-deemed-unacceptable-risk-to-children">ChatGPT for Teens deemed ‘unacceptable risk’ to children | Daily Sabah</a></li>
<li><a href="https://techcrunch.com/2026/10/07/chatgpt-for-teens-keeps-teens-talking-even-during-mental-health-crises/">ChatGPT for Teens keeps teens talking, even during... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#child protection`, `#OpenAI`, `#responsible AI`, `#AI ethics`

---

<a id="item-tech-news-7"></a>
### [谷歌向全球用户开放 SynthID AI 内容检测工具](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/) ⭐️ 7.0/10

谷歌宣布向全球用户开放 SynthID Detector，用户可上传图片、视频或音频，检测其中是否包含谷歌开发的 SynthID 数字水印，从而判断内容是否由 AI 生成。SynthID 水印不会影响内容正常使用，但能够被专门的检测系统识别。谷歌表示，自 2023 年推出 SynthID 以来，已为超过 1800 亿张图片和视频以及约 24 万年的音频内容添加水印。目前该技术已获得 OpenAI、英伟达等企业支持，苹果也计划加入。谷歌称，希望通过扩大 SynthID 应用，帮助用户更方便地识别 AI 生成内容，并推动 AI 内容溯源标准的发展。

telegram · zaihuapd · 10月7日 17:37

**「背景」** SynthID 是谷歌 DeepMind 在 2023 年推出的用于在 AI 生成的图像、视频和音频中嵌入不可感知数字水印的技术。谷歌于 2026 年 10 月 7 日向全球用户开放 SynthID Detector，使任何人可上传媒体检测其中是否包含来自谷歌、OpenAI、英伟达及 Kakao 等合作伙伴的水印。

**「用户获得免费检测工具，但覆盖范围有限」** 用户现在可以通过 SynthID Detector 免费上传图片、视频或音频来检测是否包含 SynthID 数字水印，这是此前未公开提供的能力。但该工具仅能识别 SynthID 水印，无法检测其他 AI 生成内容；行业分析指出，SynthID 水印与 C2PA 加密清单代表不同的威胁模型，两者各有局限，均无法完整解决 AI 内容认证问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unite.ai/google-opens-synthid-detector-globally-with-partner-ai-content-checks/">Google Opens SynthID Detector Globally With Partner AI Content...</a></li>
<li><a href="https://copilot-autogent.github.io/ai-security-blog/blog/content-provenance-c2pa-synthid/">Content Provenance at Scale: What C2PA and SynthID Actually ...</a></li>

</ul>
</details>

**标签**: `#AI content detection`, `#digital watermarking`, `#content provenance`, `#Google DeepMind`, `#AI ethics`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美联储会议纪要显示官员预期年内再加息，但未明确时点](https://www.cnbc.com/2026/10/07/fed-officials-see-another-hike-coming-but-no-sign-as-to-when-minutes-show.html) ⭐️ 8.0/10

美联储周三公布的会议纪要显示，18 位提交预测的联邦公开市场委员会官员中有 16 位认为年底前需要再加息一次，以应对已持续超过五年高于 2%目标的通胀，但纪要未给出具体时点。美联储下一次利率决定在 10 月 28 日，随后是 12 月 9 日；8 月核心 PCE 通胀率为 3%、整体为 3.4%，虽仍远高于 2%目标，但低于预期。

rss · CNBC Finance · 10月7日 18:42

**「背景」** 美联储于 2026 年 9 月将联邦基金利率上调 25 个基点至 3.75%-4.00%，为 2023 年以来首次加息。新任主席沃什自 5 月就任后多次强调通胀风险，而美国核心 PCE 通胀率仍维持在 3%左右，远超 2%的目标水平。

**「影响」** 10 年期美债收益率 10 月 7 日升至 5.365%，为 2002 年 4 月以来最高，推高房贷和企业贷款等信用敏感行业的融资成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalreserve.gov/aboutthefed/bios/board/warsh.htm">Federal Reserve Board - Kevin Warsh, Chairman</a></li>
<li><a href="https://tradingeconomics.com/united-states/interest-rate">United States Fed Funds Interest Rate</a></li>
<li><a href="https://wisevoter.com/world/us/2026/10/07/treasury-yields-hit-highest-level-since-2002">Treasury Yields Hit Highest Level Since 2002 - Wisevoter</a></li>

</ul>
</details>

**标签**: `#monetary policy`, `#Federal Reserve`, `#inflation`, `#interest rates`, `#Treasury yields`

---

<a id="item-finance-news-2"></a>
### [IMF 总裁：AI 既是增长希望也是通胀隐患](https://www.cnbc.com/2026/10/07/economy-inflation-ai-trade-imf-iran-hormuz-trump-.html) ⭐️ 8.0/10

IMF 总裁格奥尔基耶娃在新加坡表示，AI 若发展得当每年可为全球增长贡献约 0.5 个百分点，相当于增加一个东盟体量的经济体。但她警告，AI 收益高度集中且推高通胀，全球公共债务正逼近 GDP 的 100%，中东冲突已将油价推至每桶 100 美元以上，多重压力叠加令全球经济前景承压。

rss · CNBC Finance · 10月7日 06:16

**「背景」** 格奥尔基耶娃在 IMF 与世界银行年会前夕发表此观点，指出当前全球经济同时面临海湾战争带来的负面能源供给冲击和 AI 投资热潮带来的正面需求冲击，两者叠加效果在全球分布极不均衡。

**「潜在影响」** 她警告，若 AI 企业盈利不及预期，超大规模云服务商的高杠杆和全球对美国股票的大量持仓可能将失望情绪放大为广泛的市场冲击，建议各国货币政策保持审慎偏鹰立场。

**标签**: `#IMF`, `#AI economics`, `#global debt`, `#energy markets`, `#financial stability`

---

<a id="item-finance-news-3"></a>
### [美股屡创新高，美国税收却难跟上](https://wallstreetcn.com/member/articles/3783090) ⭐️ 7.0/10

10 月 6 日标普 500 指数再创历史高位，美国家庭未实现资本利得超 30 万亿美元，但 2026 财年联邦赤字预计达 2.1 万亿美元，全部资本利得实际税率仅约 3%。

telegram · zaihuapd · 10月7日 07:06

**「背景」** 美国现行税制仅对已实现资本利得（资产实际卖出时的收益）征税，未实现利得（账面浮盈）无需缴税，这是市场财富增长与税收收入脱节的核心机制。国会预算办公室（CBO）预计 2026 财年联邦赤字约为 2.1 万亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bankingnews.gr/diethni/articles/895883/crash-us-deficit-exceeds-2-trillion-borrowing-6-billion-every-day">Crash: US deficit exceeds $ 2 trillion – Borrowing $6 billion every day!</a></li>
<li><a href="https://weneedacpa.com/2026/05/unrealized-capital-gains-tax-2026/">Will Congress Tax Unrealized Capital Gains in 2026?</a></li>

</ul>
</details>

**标签**: `#US fiscal policy`, `#capital gains tax`, `#wealth inequality`, `#stock market performance`, `#federal deficit`

---