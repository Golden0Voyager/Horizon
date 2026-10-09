---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 41 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [ThinkingBox-Bench：507 个有状态工作流揭示 Agent 可靠性差距](#item-tech-news-1) ⭐️ 7.0/10
2. [OpenAI 首次将俄伊 AI 影响行动列为最高等级并予以封禁](#item-tech-news-2) ⭐️ 7.0/10
3. [美政府以欺诈为由暂停微软绿卡申请资格](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic 一年多来首次更新 Claude 使用政策](#item-tech-news-4) ⭐️ 7.0/10
5. [Anthropic 推出开源漏洞扫描服务 OSS Scanner](#item-tech-news-5) ⭐️ 7.0/10

**财经新闻**
1. [After a yearslong slump, China&\#x27;s real estate market may be set for a turnaround](#item-finance-news-1) ⭐️ 7.0/10
2. [华为押注国产芯片手机，电动车业务连续三月下滑](#item-finance-news-2) ⭐️ 7.0/10
3. [人社部就新就业形态劳动者权益保障办法征求意见](#item-finance-news-3) ⭐️ 7.0/10
4. [OpenAI 年化收入较此前报道少 200 亿美元](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [ThinkingBox-Bench：507 个有状态工作流揭示 Agent 可靠性差距](https://www.reddit.com/r/MachineLearning/comments/1x17shf/thinkingbox_solving_an_agent_task_once_vs_solving/) ⭐️ 7.0/10

微软研究人员发布 ThinkingBox-Bench，一个包含 507 个跨 5 个领域（零售、旅行/酒店、汽车保险、新银行内部 IT、咨询 IT/HR）的有状态业务工作流基准，每个任务在 20 次独立尝试中执行（每模型 10,140 次试验），并对照终端数据库状态与副作用而非仅任务完成度进行评分。核心发现是 pass@1、pass@20 与 all-20 三个指标会给出几乎相反的排行榜：Kimi-K3 覆盖最广（93.89% 至少一次解决），但仅 13.41% 在 20 次中全部成功；Claude Opus 5 发现较少（79.09%）但重复性高得多（47.53%）。在 121,680 次有效试验的回顾性消融中，79,853 次失败里有 67.24% 仍然&quot;干净地&quot;终止并调用了状态变更工具，因此基于完成度的代理指标会误判为成功。论文、代码、数据集已在 Hugging Face OpenEnv 公开，但原始评估轨迹未发布。

reddit · r/MachineLearning · /u/tuhin\_k · 10月9日 00:50

**「背景」** 过去的 AI 代理评估往往只看单次运行是否完成任务，假设任务完成即意味着后端数据库达到了正确状态，而未检查实际的状态变化或副作用。这种做法在涉及多步骤、有状态的业务工作流时可能高估代理的可靠性，因为代理可能在看似成功的轨迹中留下错误的字段值、额外或遗漏的效果。ThinkingBox‑Bench 正是为了弥补这一评估空白而设计的。

**「对评估实践的影响」** 对构建或评估 AI Agent 的团队而言，仅报告单次成功率或&quot;任务完成&quot;代理指标会严重高估可靠性；在 ThinkingBox-Bench 上，67.24% 的失败案例在状态检查前看起来完全正常，因此需要在评估流程中加入终端状态与副作用校验，而非依赖完成度信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.19741">One Success Isn’t Reliability: Thinkingbox , a Sandbox and...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.19741">One Success Isn&#x27;t Reliability: Thinkingbox , a Sandbox and... | alphaXiv</a></li>
<li><a href="https://huggingface.co/papers/2608.19741">Paper page - One Success Isn&#x27;t Reliability: Thinkingbox , a Sandbox...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmarking`, `#evaluation methodology`, `#stateful workflows`, `#reliability`

---

<a id="item-tech-news-2"></a>
### [OpenAI 首次将俄伊 AI 影响行动列为最高等级并予以封禁](https://openai.com/index/disrupting-ai-enabled-false-front-operations/) ⭐️ 7.0/10

OpenAI 宣布封禁两个利用 ChatGPT 的国家关联影响行动：俄罗斯行动被评为其首次出现的第 5 类（最高等级），伊朗行动为第 4 类。俄罗斯行动通过冒用身份控制拉美一个“研究平台”，传播损害乌克兰声誉并影响当地政治的虚假内容；伊朗行动以 7 个“记者”人设向全球中小网络媒体投稿并批量生成社交媒体评论，产出近 100 篇署名文章。两起行动均结合传统手段与 AI，部分内容已进入主流媒体。

telegram · zaihuapd · 10月8日 15:52

**「背景」** OpenAI 此前已建立&quot;影响行动突破量表&quot;（Breakout Scale）来对利用 AI 进行虚假信息传播的行动进行分级，并持续追踪相关案例。此次俄罗斯行动被评为第 5 类，是该量表启用以来首次出现该级别分类。

**「影响」** 封禁导致相关账号被停用、生成的虚假内容被移除，切断了这些行动进一步传播的渠道，并标志着 OpenAI 在检测和处置国家级 AI 错误信息方面的阈值提升，可能促使平台加强对类似滥用的监测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/disrupting-ai-enabled-false-front-operations/">Disrupting AI - enabled “ false front ” operations | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#disinformation`, `#OpenAI`, `#state-sponsored influence`, `#AI misuse`

---

<a id="item-tech-news-3"></a>
### [美政府以欺诈为由暂停微软绿卡申请资格](https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea) ⭐️ 7.0/10

特朗普政府宣布暂停微软参与 H-1B 签证及绿卡申请项目，指控其存在欺诈行为。副总统万斯在发布会上称，微软去年裁员 6000 名美国员工，却获得 6300 份 H-1B 签证和近 3000 张绿卡，是&quot;利用该系统最多的公司&quot;。万斯指责微软先发布虚假招聘广告、证明招不到美国工人，再以外籍劳工替换美国员工；微软尚未回应。此外，万斯还点名哈佛、耶鲁、MIT 等九所大学，称其涉嫌滥用 J-1 签证项目。

telegram · zaihuapd · 10月9日 00:00

**「H-1B 与 PERM 签证项目背景」** 美国 H-1B 签证项目允许雇主为高技能外籍员工申请工作签证，PERM（Program Electronic Review Management）程序则是外籍员工通过 H-1B 签证申请绿卡的关键步骤。J-1 签证面向交流访问者。此次暂停意味着微软无法再为持有 H-1B 签证的外籍员工提交绿卡申请。

**「对科技企业与高校的影响」** 微软和 Adobe 等科技公司已被禁止为其外籍员工提交绿卡申请，直接中断了这些企业为国际人才提供长期居留担保的能力。万斯同时点名哈佛、耶鲁、MIT 等九所大学涉嫌滥用 J-1 签证项目，这些高校的留学生签证通道也可能面临审查。微软目前尚未对此作出回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oann.com/newsroom/vance-microsoft-suspended-from-perm-green-card-sponsorship-program/">Vance : Microsoft suspended from PERM green card sponsorship...</a></li>
<li><a href="https://www.dw.com/en/us-suspends-microsoft-adobe-from-filing-for-green-cards/a-79605053">US suspends Microsoft , Adobe from filing for green cards</a></li>
<li><a href="https://www.foxbusiness.com/politics/vance-suspends-microsoft-others-from-foreign-workers-applying-green-cards-accuses-company-visa-abuse">Vance accuses Microsoft of abusing visa system... | Fox Business</a></li>

</ul>
</details>

**标签**: `#immigration-policy`, `#microsoft`, `#h1b-visa`, `#tech-industry`, `#regulation`

---

<a id="item-tech-news-4"></a>
### [Anthropic 一年多来首次更新 Claude 使用政策](https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude) ⭐️ 7.0/10

Anthropic 一年多来首次更新 Claude 使用政策，新增禁止对 Claude 持续且无必要的滥用行为，并将选举干预、武器研发、监控以及健康与金融用途等高风险滥用情形纳入禁止范围。新规还明确禁止欺骗性政治宣传、用假账户放大内容及选民欺骗等行为；武器禁令扩展至使武器运转的软硬件和武装无人机等。执行手段仍以终止对话为主，且仅适用于反复滥用模型的极端情况。

telegram · zaihuapd · 10月9日 01:34

**「背景」** Anthropic 通常每年根据模型能力演进和客户反馈更新使用政策，此次是超过一年来的首次更新。新增条款针对选举干预、武器研发（含使武器运转的软硬件及武装无人机）、监控及欺骗性政治宣传等此前未明确禁止的高风险场景。

**「影响」** 开发者和组织若继续将 Claude 用于选举干扰、武器研发（包括使武器运作的软硬件）、监控或欺骗性政治宣传，将面临账户被终止的风险；因此需要及时审查并调整现有集成，确保不涉及禁止场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/">Anthropic changes usage policy to ban model abuse and election ...</a></li>
<li><a href="https://www.anthropic.com/news/2026-usage-policy-update">2026 Usage Policy update \ Anthropic</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude">Anthropic bans ‘abusive or cruel behavior’ toward Claude | The Verge</a></li>
<li><a href="https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/">Anthropic changes usage policy to ban model abuse and election ...</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude">Anthropic bans ‘abusive or cruel behavior’ toward Claude | The Verge</a></li>

</ul>
</details>

**标签**: `#AI Policy`, `#Anthropic`, `#AI Governance`, `#Usage Restrictions`, `#Responsible AI`

---

<a id="item-tech-news-5"></a>
### [Anthropic 推出开源漏洞扫描服务 OSS Scanner](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) ⭐️ 7.0/10

Anthropic 推出名为 OSS Scanner 的免费、自愿接入漏洞扫描服务，面向符合条件的开源项目，报告由 Claude 等模型自动生成，未经人工审核，包含漏洞复现步骤、漏洞说明及可能的补丁建议，但可能存在错误。Anthropic 称过去半年发现逾 2.9 万个候选漏洞，人工审查约 6,000 个；早期测试的 97 个高危或严重漏洞中，85 个符合其披露流程要求。符合条件项目的核心维护者可通过提交 GitHub PR 申请接入。

telegram · zaihuapd · 10月9日 02:00

**「背景」** 在推出 OSS Scanner 之前，Anthropic 曾在内部项目 Glasswing 中使用 Claude 模型进行漏洞挖掘，积累了 AI 辅助安全扫描的经验。这一经验为后来面向开源社区的免费自愿接入扫描服务奠定了技术基础。

**「维护者需自行验证 AI 生成的漏洞报告」** 符合条件的开源项目核心维护者可通过提交 GitHub PR 申请接入该服务，获得由 Claude 生成的漏洞报告，包含复现步骤和补丁建议。但报告未经人工审核且可能存在错误，维护者需自行验证。考虑到 Anthropic 半年内已发现逾 2.9 万个候选漏洞，而开源项目通常资源有限，大量 AI 生成的漏洞报告可能给维护者带来额外的审查负担——正如 Infosecurity Magazine 所指出的，发现漏洞的技术正变得更廉价易得，但调查漏洞所需的专业能力并未同步增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source">An opt-in vulnerability -finding service for open - source software</a></li>
<li><a href="https://www.infosecurity-magazine.com/opinions/ai-vulnerabilities-open-source/">AI is Finding More Vulnerabilities But Open Source Needs More...</a></li>

</ul>
</details>

**标签**: `#AI-security`, `#open-source`, `#vulnerability-scanning`, `#Anthropic`, `#LLM-applications`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [After a yearslong slump, China&\#x27;s real estate market may be set for a turnaround](https://www.cnbc.com/2026/10/08/chinas-real-estate-market-may-be-set-for-a-turnaround-sp-says.html) ⭐️ 7.0/10

S&amp;P Global Ratings forecasts China&\#x27;s residential real estate prices may bottom in Q3 2028, with major cities recovering sooner, citing new government policies to reduce supply and subsidize first-time buyers as key drivers of a potential turnaround.

rss · CNBC Finance · 10月8日 09:27

**标签**: `#china-real-estate`, `#housing-market`, `#policy-analysis`, `#s-and-p-global-ratings`, `#market-forecast`

---

<a id="item-finance-news-2"></a>
### [华为押注国产芯片手机，电动车业务连续三月下滑](https://www.cnbc.com/2026/10/08/huawei-china-smartphone-ev-slow.html) ⭐️ 7.0/10

华为于 10 月 1 日发布首款搭载自研&quot;逻辑折叠&quot;芯片的 Mate 90 系列手机，消费者业务营收从 2021 年制裁后低谷的约 340 亿美元回升至 2025 年的约 510 亿美元（占总营收 39%）。与此同时，华为赋能的电动车 9 月交付量同比下降 29%，连续第三个月下滑，而中国汽车市场前三季度销量降幅超 20%。

rss · CNBC Finance · 10月8日 08:04

**「背景」** 2019 年美国制裁切断了华为对谷歌安卓系统和台积电芯片的获取渠道，使其从全球智能手机出货量第一的位置跌落，消费者业务营收一度腰斩至约 340 亿美元（2021 年）。与此同时，中国汽车市场正经历 2021 年以来最差的年份，前三季度总销量同比下降超过 20%，新能源汽车销量下降 13%。

**标签**: `#Huawei`, `#Smartphones`, `#Electric Vehicles`, `#China Tech`, `#U.S. Sanctions`

---

<a id="item-finance-news-3"></a>
### [人社部就新就业形态劳动者权益保障办法征求意见](https://mp.weixin.qq.com/s/saqkOXlhe0wX7qD83vdkRw) ⭐️ 7.0/10

2026 年 10 月 8 日，人力资源社会保障部发布《新就业形态劳动者权益保障办法（征求意见稿）》，即日起至 11 月 8 日公开征求意见。办法提出正常劳动报酬不得低于当地最低工资标准、连续工作 4 小时应保障适当休息、停止派单和封禁账号等重大决定不得由算法自动作出须经人工审核，并明确不得滥用罚款等惩罚性措施，覆盖网约车司机、外卖骑手、网络主播等群体。

telegram · zaihuapd · 10月8日 09:23

**「背景」** 新就业形态劳动者指网约车司机、外卖骑手、网络主播等依托平台工作的群体，此前长期处于传统劳动关系与灵活就业之间的监管空白地带。人社部此次以全国性征求意见稿形式，首次系统性地为这一群体设定最低工资、休息保障和算法决策限制等底线规则，覆盖数以千万计的从业者。

**「影响」** 该办法若最终出台，将直接影响网约车司机、外卖骑手、网络主播等新就业形态劳动者及其所属平台企业——平台须确保正常劳动报酬不低于当地最低工资标准、连续工作 4 小时保障休息，且停止派单、封禁账号等重大决定须经人工审核而非算法自动作出。但当前仍处于征求意见阶段（10 月 8 日至 11 月 8 日），最终条款可能调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.ce.cn/xwzx/gnsz/gdxw/202610/t20261009_3250349.shtml">ce.cn/xwzx/gnsz/gdxw/202610/t20261009_3250349.shtml</a></li>
<li><a href="https://www.cqcb.com/news/64/2026-10-08/6233035.html">cqcb.com/news/64/ 2026 -10-08/6233035.html</a></li>

</ul>
</details>

**标签**: `#labor policy`, `#gig economy`, `#regulation`, `#worker rights`, `#China`

---

<a id="item-finance-news-4"></a>
### [OpenAI 年化收入较此前报道少 200 亿美元](https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1) ⭐️ 7.0/10

据《金融时报》报道，投资者获得的财务文件显示，OpenAI 截至 9 月底的年化收入约为 500 亿美元，比此前广泛流传的 700 亿美元少约 200 亿美元。差异主要源于计算口径不同——Anthropic 将通过 AWS、谷歌云等云合作伙伴销售的收入计入，而 OpenAI 未计入；OpenAI 拒绝置评。

telegram · zaihuapd · 10月8日 17:22

**「背景」** 此前广泛流传的 700 亿美元年化收入数字，与本次投资者文件中披露的约 500 亿美元之间的差异，主要源于计算口径不同：Anthropic 将通过 AWS、谷歌云等云合作伙伴销售的收入计入年化收入，而 OpenAI 未计入这部分。

**「影响」** 投资者对 AI 需求增长速度的乐观预期可能因此降温，尤其是关注微软、甲骨文、英伟达等 AI 相关股票的投资者，因为 200 亿美元的差距（尽管部分源于会计口径差异）可能改变市场对 AI 商业化进度的判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gangstaai.org/news/openai-revenue-50-billion-20-billion-below-projection-ai-stocks-sink">OpenAI Told Its Investors the Number Was $ 70 Billion . | Gangsta AI</a></li>
<li><a href="https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1">OpenAI annualised revenues $20bn less than previously signalled</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/msft-orcl-nvda-qqq-focus-190141481.html">MSFT, ORCL, NVDA, QQQ In Focus: OpenAI ’s Annualized Revenue ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI Industry Revenue`, `#Financial Reporting`, `#Cloud Partnerships`, `#Market Expectations`

---