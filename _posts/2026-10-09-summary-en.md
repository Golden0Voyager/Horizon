---
layout: default
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 41 items, 9 important content pieces were selected

---

**Technology News**
1. [ThinkingBox-Bench: 507 Stateful Workflows Reveal Agent Reliability Gaps](#item-tech-news-1) ⭐️ 7.0/10
2. [OpenAI bans Russian and Iranian AI influence operations, labels Russian as first Category 5](#item-tech-news-2) ⭐️ 7.0/10
3. [US Government Suspends Microsoft&\#x27;s H-1B and Green Card Eligibility Over Alleged Fraud](#item-tech-news-3) ⭐️ 7.0/10
4. [Anthropic Updates Claude Usage Policy with Expanded Abuse Prohibitions](#item-tech-news-4) ⭐️ 7.0/10
5. [Anthropic Launches Free Opt-In OSS Vulnerability Scanner](#item-tech-news-5) ⭐️ 7.0/10

**Financial News**
1. [After a yearslong slump, China&\#x27;s real estate market may be set for a turnaround](#item-finance-news-1) ⭐️ 7.0/10
2. [Huawei Pivots to Domestic-Chip Smartphones as EV Sales Slump](#item-finance-news-2) ⭐️ 7.0/10
3. [China Drafts Gig Worker Rights Regulation](#item-finance-news-3) ⭐️ 7.0/10
4. [OpenAI Annualized Revenue Reported at $50B, $20B Below Prior Estimates](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ThinkingBox-Bench: 507 Stateful Workflows Reveal Agent Reliability Gaps](https://www.reddit.com/r/MachineLearning/comments/1x17shf/thinkingbox_solving_an_agent_task_once_vs_solving/) ⭐️ 7.0/10

Microsoft researchers introduce ThinkingBox-Bench, a benchmark of 507 policy-conditioned business workflows across 5 domains \(retail, travel/hospitality, auto insurance, neobank IT, consulting IT/HR\), each run 20 times from an identical clean backend for 10,140 trials per model, graded against terminal database state and side effects rather than task completion. Three metrics—pass@1, pass@20, and all-20—reveal that discovery and repeatability rank models very differently: Kimi-K3 solves 93.89% of tasks at least once but only 13.41% on all 20 attempts, while Claude Opus 5 discovers fewer \(79.09%\) but repeats far more \(47.53%\). In a retrospective ablation over 121,680 valid trials across 12 models, 67.24% of failures terminated cleanly with no final tool error, meaning a completion-style proxy would have scored them as done; state checks found wrong field values in 77.61% of those clean failures, unintended extra effects in 43.30%, and missing required effects in 25.36%. The paper, code, dataset, and HF OpenEnv environment are publicly available.

reddit · r/MachineLearning · /u/tuhin\_k · Oct 9, 00:50

**「Background」** Agent evaluation has traditionally relied on single-run success rates and completion-style proxies—whether the agent finished the task—rather than verifying that the backend database reached the correct terminal state. This approach conflates task completion with correct outcomes and does not capture reliability across repeated attempts.

**「Impact」** For teams building or evaluating AI agents, single-run success rates may not reflect reliable performance: ranking by pass@20 and ranking by all-20 produce nearly reversed leaderboards, and most failures look clean to completion-style proxies. The benchmark is available on HF OpenEnv, allowing independent evaluation of any model against the 507 tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.19741">One Success Isn’t Reliability: Thinkingbox , a Sandbox and...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.19741">One Success Isn&#x27;t Reliability: Thinkingbox , a Sandbox and... | alphaXiv</a></li>
<li><a href="https://huggingface.co/papers/2608.19741">Paper page - One Success Isn&#x27;t Reliability: Thinkingbox , a Sandbox...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#benchmarking`, `#evaluation methodology`, `#stateful workflows`, `#reliability`

---

<a id="item-tech-news-2"></a>
### [OpenAI bans Russian and Iranian AI influence operations, labels Russian as first Category 5](https://openai.com/index/disrupting-ai-enabled-false-front-operations/) ⭐️ 7.0/10

OpenAI banned two state-linked AI influence operations that used ChatGPT: a Russian operation impersonating identities to run a Latin American research platform spreading false content about Ukraine, and an Iranian operation using seven fictitious journalist personas to submit articles and generate social media comments. The Russian operation was rated as OpenAI&\#x27;s first-ever Category 5 influence operation, while the Iranian operation received a Category 4 rating. Both campaigns combined traditional tactics with AI-generated content, and some material reached mainstream media.

telegram · zaihuapd · Oct 8, 15:52

**「OpenAI&\#x27;s Breakout Scale and False-Front Operations」** OpenAI has been tracking AI-enabled influence operations using a Breakout Scale that classifies campaigns by severity and reach, with Category 5 being the highest level. &\#x27;False front&\#x27; operations use fabricated identities—such as fake journalists or think tanks—to lend credibility to disinformation distributed through mainstream channels.

**「Impact」** The assignment of a Category 5 rating to the Russian operation marks the highest severity level OpenAI has ever assigned to an influence operation, providing a concrete benchmark for assessing the scale and sophistication of AI-enabled disinformation campaigns.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/disrupting-ai-enabled-false-front-operations/">Disrupting AI - enabled “ false front ” operations | OpenAI</a></li>
<li><a href="https://cellcog.ai/blog/openai-false-front-operations/">OpenAI &#x27;s False - Front Report: Its First Category 5 Takedown | CellCog</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#disinformation`, `#OpenAI`, `#state-sponsored influence`, `#AI misuse`

---

<a id="item-tech-news-3"></a>
### [US Government Suspends Microsoft&\#x27;s H-1B and Green Card Eligibility Over Alleged Fraud](https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea) ⭐️ 7.0/10

The Trump administration has suspended Microsoft&\#x27;s participation in the H-1B visa and green card programs, alleging fraud. Vice President Vance stated that Microsoft laid off 6,000 US employees last year while securing 6,300 H-1B visas and nearly 3,000 green cards, calling it the company that &\#x27;abused the system the most.&\#x27; Vance accused Microsoft of posting false job advertisements to prove it could not hire American workers, then replacing them with foreign labor. Microsoft has not yet responded to the allegations. Vance also named nine universities, including Harvard, Yale, and MIT, accusing them of abusing the J-1 visa program.

telegram · zaihuapd · Oct 9, 00:00

**「Background」** The PERM \(Permanent Labor Certification\) program is the U.S. Department of Labor&\#x27;s process through which employers sponsor foreign workers for permanent residency \(green cards\), typically after those workers have been on H-1B visas. The H-1B visa is a temporary work visa for high-skilled foreign professionals, and the J-1 visa is an exchange visitor program. Understanding these programs is essential to grasping the significance of Microsoft&\#x27;s suspension.

**「Immediate hiring disruption and precedent risk」** The suspension immediately prevents Microsoft and other affected tech firms from filing green card applications for their foreign workers, directly disrupting international talent recruitment pipelines. The administration&\#x27;s stated criteria—comparing domestic layoffs against visa volumes—could be applied to other large tech employers, creating compliance risk for companies with similar patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oann.com/newsroom/vance-microsoft-suspended-from-perm-green-card-sponsorship-program/">Vance : Microsoft suspended from PERM green card sponsorship...</a></li>
<li><a href="https://www.nytimes.com/2026/10/08/us/politics/microsoft-visas-green-cards.html">Trump Administration Suspends Microsoft From Green Card Program...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/oct/08/jd-vance-microsoft-visa-workers-green-card-suspension">Microsoft suspended from applying for green cards ... | The Guardian</a></li>
<li><a href="https://www.dw.com/en/us-suspends-microsoft-adobe-from-filing-for-green-cards/a-79605053">US suspends Microsoft , Adobe from filing for green cards</a></li>
<li><a href="https://www.foxbusiness.com/politics/vance-suspends-microsoft-others-from-foreign-workers-applying-green-cards-accuses-company-visa-abuse">Vance accuses Microsoft of abusing visa system... | Fox Business</a></li>

</ul>
</details>

**Tags**: `#immigration-policy`, `#microsoft`, `#h1b-visa`, `#tech-industry`, `#regulation`

---

<a id="item-tech-news-4"></a>
### [Anthropic Updates Claude Usage Policy with Expanded Abuse Prohibitions](https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude) ⭐️ 7.0/10

Anthropic has updated its Claude usage policy for the first time in over a year, adding prohibitions on sustained and unnecessary abuse, election interference, weapons development \(including software and hardware that enable weapons and armed drones\), surveillance, deceptive political propaganda, fake account amplification, voter deception, and high-risk health and financial uses. Terminating conversations remains the primary enforcement mechanism, and the restrictions apply only to extreme cases of repeated model abuse. The update affects developers and organizations using Claude, with the weapons ban notably expanding to cover enabling software and hardware as well as armed drones.

telegram · zaihuapd · Oct 9, 01:34

**「Background」** Anthropic’s Claude usage policy had not been revised since its last update in late 2025, setting the baseline for permissible model use. The October 8 2026 announcement marks the first substantive change in over a year, continuing Anthropic’s annual practice of updating the policy to reflect evolving model capabilities and user feedback.

**「Impact on Claude Users and Developers」** Developers and organizations using Claude must now review their applications against the expanded prohibitions on election interference, weapons development \(including software and hardware enabling weapons and armed drones\), surveillance, and deceptive political propaganda. The primary enforcement mechanism remains conversation termination, but it applies only to extreme cases of repeated abuse—ordinary frustration and criticism of the model are still permitted. This means teams building tools that could be repurposed for these prohibited uses need to assess compliance risk, though the policy does not ban the underlying capabilities outright.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/2026-usage-policy-update">2026 Usage Policy update \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/">Anthropic changes usage policy to ban model abuse and election ...</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1008100/anthropic-new-usage-policy-abuse-claude">Anthropic bans ‘abusive or cruel behavior’ toward Claude | The Verge</a></li>
<li><a href="https://www.anthropic.com/news/2026-usage-policy-update">2026 Usage Policy update \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI Policy`, `#Anthropic`, `#AI Governance`, `#Usage Restrictions`, `#Responsible AI`

---

<a id="item-tech-news-5"></a>
### [Anthropic Launches Free Opt-In OSS Vulnerability Scanner](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) ⭐️ 7.0/10

Anthropic launched OSS Scanner, a free, opt-in vulnerability scanning service for qualifying open-source projects, with core maintainers applying via GitHub pull request. Reports are generated by Claude and other models without manual review, including reproduction steps, vulnerability descriptions, and patch suggestions where possible, though Anthropic warns they may contain errors. Over six months, the service identified more than 29,000 candidate vulnerabilities, of which approximately 6,000 were manually reviewed by Anthropic. In early testing, 85 of 97 high or critical vulnerabilities met Anthropic&\#x27;s disclosure criteria.

telegram · zaihuapd · Oct 9, 02:00

**「From Project Glasswing to OSS Scanner」** OSS Scanner is the public-facing successor to Anthropic&\#x27;s internal Project Glasswing, an earlier initiative that used Claude to discover vulnerabilities in open-source code. The experience gained from Project Glasswing directly informed the design and deployment of the opt-in scanning service now available to eligible open-source projects.

**「Maintainer Triage Burden」** Qualifying open-source maintainers can submit a GitHub PR to opt in and receive AI-generated vulnerability reports with reproduction steps and patch suggestions, but these reports are not manually reviewed and may contain errors. The scale of findings—over 29,000 candidate vulnerabilities identified in six months—raises a triage concern for resource-limited projects: as AI makes vulnerability discovery cheaper and more accessible, the expertise needed to investigate and validate findings remains scarce.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source">An opt-in vulnerability -finding service for open - source software</a></li>
<li><a href="https://www.infosecurity-magazine.com/opinions/ai-vulnerabilities-open-source/">AI is Finding More Vulnerabilities But Open Source Needs More...</a></li>

</ul>
</details>

**Tags**: `#AI-security`, `#open-source`, `#vulnerability-scanning`, `#Anthropic`, `#LLM-applications`

---

## Financial News

<a id="item-finance-news-1"></a>
### [After a yearslong slump, China&\#x27;s real estate market may be set for a turnaround](https://www.cnbc.com/2026/10/08/chinas-real-estate-market-may-be-set-for-a-turnaround-sp-says.html) ⭐️ 7.0/10

S&amp;P Global Ratings forecasts China&\#x27;s residential real estate prices may bottom in Q3 2028, with major cities recovering sooner, citing new government policies to reduce supply and subsidize first-time buyers as key drivers of a potential turnaround.

rss · CNBC Finance · Oct 8, 09:27

**Tags**: `#china-real-estate`, `#housing-market`, `#policy-analysis`, `#s-and-p-global-ratings`, `#market-forecast`

---

<a id="item-finance-news-2"></a>
### [Huawei Pivots to Domestic-Chip Smartphones as EV Sales Slump](https://www.cnbc.com/2026/10/08/huawei-china-smartphone-ev-slow.html) ⭐️ 7.0/10

Huawei released the Mate 90 series on Oct. 1, 2026, built on its own &quot;LogicFolding&quot; chip, as its consumer business — which halved to about $34 billion in 2021 after U.S. sanctions and has since recovered to roughly $51 billion in 2025 \(39% of total revenue\) — doubles down on domestically-chipped phones. Meanwhile, Huawei-powered vehicle deliveries fell 29% year-on-year in September, marking a third consecutive monthly decline, against a backdrop of China&\#x27;s auto market contracting more than 20% over the first three quarters of 2026.

rss · CNBC Finance · Oct 8, 08:04

**「Background」** U.S. sanctions imposed in 2019 blocked Huawei&\#x27;s access to Google&\#x27;s Android operating system and TSMC-made semiconductors, causing its consumer business revenue to halve to about $34 billion in 2021 before recovering to roughly $51 billion in 2025. China&\#x27;s auto market is on track for its worst year since 2021, with sales down more than 20% over the first three quarters, and Huawei&\#x27;s EV business operates through partnerships with manufacturers like Chery and Seres rather than manufacturing vehicles itself.

**「Investor impact」** Shanghai-listed Seres Group, which manufactures Huawei&\#x27;s Aito EV line, has seen its shares fall more than 60% year-to-date as Huawei-powered vehicle deliveries dropped 29% year-on-year in September — a third consecutive monthly decline — while competitors BYD and Leapmotor posted double-digit growth.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/10/08/huawei-china-smartphone-ev-slow.html">Huawei doubles down on smartphones as EV sales slow</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Smartphones`, `#Electric Vehicles`, `#China Tech`, `#U.S. Sanctions`

---

<a id="item-finance-news-3"></a>
### [China Drafts Gig Worker Rights Regulation](https://mp.weixin.qq.com/s/saqkOXlhe0wX7qD83vdkRw) ⭐️ 7.0/10

China&\#x27;s Ministry of Human Resources and Social Security released a draft regulation on October 8, 2026, seeking public comment through November 8 on protecting gig economy workers&\#x27; rights, including ride-hailing drivers, delivery riders, and online streamers. The draft sets a floor that normal labor compensation must not fall below local minimum wage standards, requires appropriate rest after four hours of continuous work, prohibits punitive fines, and mandates that major decisions such as stopping dispatch or banning accounts be reviewed by a human rather than made automatically by algorithms.

telegram · zaihuapd · Oct 8, 09:23

**「Background」** &quot;New employment forms&quot; \(新就业形态\) refers to gig economy work such as ride-hailing, food delivery, and online streaming. This draft is a national-level regulation from China&\#x27;s Ministry of Human Resources and Social Security, the country&\#x27;s labor policy authority, and would cover tens of millions of workers in these roles.

**「Impact」** Gig‑economy workers such as ride‑hailing drivers, delivery riders and online streamers would gain minimum‑wage guarantees, mandatory rest after four hours of work and protection from automatic algorithmic penalties, while platform companies could face higher labor costs and compliance obligations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mohrss.gov.cn/">mohrss .gov.cn</a></li>
<li><a href="https://www.cqcb.com/news/64/2026-10-08/6233035.html">cqcb.com/news/64/ 2026 -10-08/6233035.html</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gig_economy">Gig economy - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#labor policy`, `#gig economy`, `#regulation`, `#worker rights`, `#China`

---

<a id="item-finance-news-4"></a>
### [OpenAI Annualized Revenue Reported at $50B, $20B Below Prior Estimates](https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1) ⭐️ 7.0/10

Financial Times reports that OpenAI&\#x27;s annualized revenue as of late September is approximately $50 billion, about $20 billion less than the previously reported $70 billion figure, largely because OpenAI excludes revenue from cloud partners such as AWS and Google Cloud—a methodology difference that may temper market optimism about AI demand growth.

telegram · zaihuapd · Oct 8, 17:22

**「Background」** The $70 billion figure was previously communicated to OpenAI&\#x27;s investors and widely reported, but the gap largely stems from differing calculation methods: Anthropic counts revenue from cloud partners like AWS and Google Cloud, while OpenAI excludes those sales.

**「Market Impact」** AI-focused investors and related equities may see tempered expectations for demand growth, as the $20 billion gap—largely an accounting-method difference rather than a restatement of booked results—could reduce confidence in the pace of AI revenue expansion.

<details><summary>References</summary>
<ul>
<li><a href="https://gangstaai.org/news/openai-revenue-50-billion-20-billion-below-projection-ai-stocks-sink">OpenAI Told Its Investors the Number Was $ 70 Billion . | Gangsta AI</a></li>
<li><a href="https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1">OpenAI annualised revenues $20bn less than previously signalled</a></li>
<li><a href="https://cryptobriefing.com/openai-revenue-run-rate-nears-50-billion/">OpenAI &#x27;s revenue run rate nears $ 50 billion , short of the numbers...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/msft-orcl-nvda-qqq-focus-190141481.html">MSFT, ORCL, NVDA, QQQ In Focus: OpenAI ’s Annualized Revenue ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI Industry Revenue`, `#Financial Reporting`, `#Cloud Partnerships`, `#Market Expectations`

---