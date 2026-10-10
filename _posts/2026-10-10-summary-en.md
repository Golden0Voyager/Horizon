---
layout: default
title: "Horizon Summary: 2026-10-10 (EN)"
date: 2026-10-10
lang: en
---

> From 43 items, 5 important content pieces were selected

---

**Technology News**
1. [Cloudflare Acquires Deno in Acquihire, Ending Independent Runtime Development](#item-tech-news-1) ⭐️ 7.0/10
2. [Typesafe AI Raises $870M at $7.5B Valuation for Decision-Model Product Jev](#item-tech-news-2) ⭐️ 7.0/10
3. [JetBrains Releases Mellum2.1, an Open-Source Coding Model for Local Agents](#item-tech-news-3) ⭐️ 7.0/10

**Technology Blog**
1. [Software&\#x27;s Centaur Age May Last Decades](#item-tech-blog-1) ⭐️ 4.0/10

**Financial News**
1. [Apple Cuts iPhone 18 Pro Orders by 15%, Shares Dip in Pre-Market](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Cloudflare Acquires Deno in Acquihire, Ending Independent Runtime Development](https://deno.com/blog/cloudflare) ⭐️ 7.0/10

Cloudflare has acquired Deno in an acquihire, ending independent development of the JavaScript/TypeScript runtime created by Ryan Dahl. The company will support the Deno runtime for one more year with monthly releases containing bug fixes and security updates, after which development will cease. Deno will remain open source, and Cloudflare welcomes others to continue its development.

hackernews · ilreb · Oct 9, 13:03 · [Discussion](https://news.ycombinator.com/item?id=50019911)

**「Deno&\#x27;s Origins and Cloudflare&\#x27;s Existing Runtime」** Deno was created by Ryan Dahl, the original author of Node.js, as a modern JavaScript/TypeScript runtime with a built-in security model, establishing itself as a notable alternative to Node.js over roughly eight years of development. Cloudflare, which already operates its own JavaScript runtime called workerd for its serverless Workers platform, is acquiring Deno in an acquihire that will end independent development after one year of maintenance-only support, with the project remaining open source.

**「One-Year Migration Window for Deno Developers」** Developers relying on the Deno runtime have a defined one-year window—through monthly releases containing only bug fixes and security updates—before Cloudflare ends development of the runtime entirely. Projects built on Deno-specific features such as its built-in security model, TypeScript-first tooling, or the Deno Deploy platform must plan migration to Node.js, Bun, or Cloudflare Workers within that period, since no new features will ship after the maintenance window closes. The runtime remains open source, so a community fork is theoretically possible, but Cloudflare has not committed to supporting or endorsing any successor project, leaving the long-term path for Deno-dependent codebases uncertain.

**「Community Discussion」** Commenters expressed sadness about the end of Deno&\#x27;s independent development, with some noting they had anticipated the outcome after Deno shifted priorities toward npm compatibility. One commenter suggested the headline &\#x27;Deno development effectively shut down via a Cloudflare acquihire&\#x27; better captures the situation, while another noted the broader pattern of developer tooling acquisitions across the industry.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/deno-joins-cloudflare/">Deno is joining Cloudflare | Cloudflare Blog</a></li>
<li><a href="https://www.explainx.ai/blog/deno-joins-cloudflare-celld-workerd-runtime-sunset-2026">Deno Joins Cloudflare: Runtime Sunset in 1 Year - explainx.ai</a></li>

</ul>
</details>

**Tags**: `#JavaScript`, `#Deno`, `#Cloudflare`, `#Runtime`, `#Acquisition`

---

<a id="item-tech-news-2"></a>
### [Typesafe AI Raises $870M at $7.5B Valuation for Decision-Model Product Jev](https://typesafe.ai/blog/series-ai) ⭐️ 7.0/10

Typesafe AI announced an $870M funding round at a $7.5B valuation for its decision-model product Jev, which the company describes as enabling AI systems to make structured decisions. The round was announced on October 9, 2026, via the company&\#x27;s blog, with no independent benchmarks or third-party verification of Jev&\#x27;s performance included in the announcement. The funding positions Typesafe AI as a major player in the decision-model space, though community members noted that competing products from OpenAI, Microsoft, and open-source contributors emerged within days of Jev&\#x27;s release.

hackernews · tosh · Oct 9, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50023450)

**「Jev&\#x27;s Launch Context」** Jev is a decision-model AI product launched by TypeSafe AI in September 2026, designed to make decisions rather than generate text. The launch post garnered nearly 40 million views. Three days after launch, a developer from Kerala claimed to have built a similar system a year earlier.

**「Competitive Pressure from Microsoft&\#x27;s Decision-1」** Microsoft&\#x27;s Decision-1 model, released around the same time as Typesafe AI&\#x27;s funding announcement, is available in Microsoft Foundry and claims top performance in latency and quality on structured decision tasks, outperforming both LLMs and other decision models. Combined with OpenAI&\#x27;s Decisions API and a growing number of open-source alternatives that appeared within days of Jev&\#x27;s release, developers and organizations evaluating decision-model capabilities now have multiple established alternatives. Microsoft&\#x27;s speed and benchmark claims remain unverified independently, but the rapid proliferation of competing options raises questions about whether Typesafe AI&\#x27;s $7.5B valuation reflects a durable competitive advantage or a rapidly commoditizing market.

**「Community Discussion」** Community members debated whether the $7.5B valuation is justified given that competitors reportedly emerged within days of Jev&\#x27;s release. One commenter noted that OpenAI&\#x27;s Decisions API and Microsoft&\#x27;s Decision-1 model appeared shortly after, while another argued that Typesafe AI&\#x27;s engineering team and marketing execution may still position it favorably on the latency-quality-cost curve despite lacking a technical moat.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=3q_MQg2CRt4">System 1: The Race to Build AI That Decides ( Jev , Laya...) - YouTube</a></li>
<li><a href="https://commandline.microsoft.com/microsoft-decision-1-model-foundry/">Microsoft-Decision-1: Our model for fast decision-making</a></li>
<li><a href="https://windowsreport.com/microsoft-decision-1-ai-model-is-here-with-35x-faster-performance-than-gpt-6-sol/">Microsoft-Decision-1 AI Model Is Here With 35x Faster ...</a></li>
<li><a href="https://windowsforum.com/news/microsoft-decision-1-in-foundry-fast-ai-classification-model-benchmarks-and-pricing-caveats.447797/">Microsoft Decision-1 in Foundry: Fast AI Classification Model ...</a></li>

</ul>
</details>

**Tags**: `#AI funding`, `#startup valuation`, `#competitive landscape`, `#decision models`, `#industry analysis`

---

<a id="item-tech-news-3"></a>
### [JetBrains Releases Mellum2.1, an Open-Source Coding Model for Local Agents](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 7.0/10

JetBrains released Mellum2.1, a 12B-parameter mixture-of-experts coding model with 2.5B active parameters, licensed under Apache 2.0 and available on Hugging Face. The model was trained with reinforcement learning in real environments and is designed for local coding agents that can explore codebases, edit files, and check their own modifications. The announcement is a vendor claim; the source provides no independent benchmarks or comparative evaluation.

telegram · zaihuapd · Oct 9, 07:30

**「Mellum2 Predecessor」** JetBrains first released Mellum2 on June 1, 2026, as a 12B-parameter mixture-of-experts model optimized for low-latency text-and-code workloads, extending the original Mellum code-completion model to broader natural language and software engineering tasks \(tool-2-2\). Mellum2.1 keeps the same architecture and parameter counts but adds reinforcement learning training in real environments, enabling the model to explore codebases, edit files, and verify changes for use in local coding agents \(tool-2-1\).

**「Impact」** Developers can immediately download Mellum2.1 from Hugging Face and deploy it for local coding agents under the permissive Apache 2.0 license, with no commercial restrictions. The 2.5B active parameters \(out of 12B total\) design targets efficient local inference, making it practical for teams that want to run agentic coding workflows—exploring codebases, editing files, and verifying changes—without relying on cloud API costs. However, the release announcement does not include benchmark results or comparative evaluations against existing open-source coding models such as Qwen 2.5 Coder or DeepSeek Coder, so developers should validate performance on their own workloads before adopting it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/">JetBrains Releases Mellum2.1: A 12B MoE Open Model for Coding ...</a></li>
<li><a href="https://huggingface.co/blog/JetBrains/mellum2-launch">Introducing Mellum2: A 12B Mixture-of-Experts Model by JetBrains</a></li>
<li><a href="https://insiderllm.com/guides/codellama-vs-deepseek-coder-vs-qwen-coder/">CodeLlama vs DeepSeek Coder vs Qwen Coder : Best... | InsiderLLM</a></li>
<li><a href="https://webscraft.org/blog/yaku-model-ollama-vibrati-u-2026-porivnyannya-llama-qwen-deepseek-i-mistral?lang=en">Top 10 Ollama Models 2026 : Llama, Qwen , DeepSeek , Mistral</a></li>

</ul>
</details>

**Tags**: `#open-source-model`, `#coding-agent`, `#mixture-of-experts`, `#JetBrains`, `#AI-for-Software-Engineering`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Software&\#x27;s Centaur Age May Last Decades](https://seangoedecke.com/softwares-centaur-age-may-last-decades/) ⭐️ 4.0/10

rss · Sean Goedecke · Oct 10, 00:00

**「Background」** Sean Goedecke argues that human-AI &quot;centaur&quot; partnerships—engineers working alongside coding agents—are currently the most effective mode of software development and will likely persist for at least a decade.

**「Solution」** He traces the centaur age from GitHub Copilot \(2022\) through chat interfaces and coding agents \(Cursor&\#x27;s agent mode in 2024, Claude Code in early 2025\) to current unsupervised agents \(post-Claude Opus 4.5, November 2025\), noting that agent output now needs human review mainly for alignment issues rather than bugs. Drawing on historical analogies—chess&\#x27;s centaur age lasted roughly twenty years, while the knitting-frame centaur age endured two hundred—he presents six competing arguments about whether software&\#x27;s centaur age will be shorter or longer than chess&\#x27;s, then concedes &quot;we have no real idea.&quot; His practical advice: don&\#x27;t quit software engineering, lean into the partnership, think about what value humans can still add \(shifting from technical expertise in 2023 to alignment today\), and avoid panicking about worst-case scenarios. The argument rests on historical analogy and honest uncertainty rather than technical evidence or benchmarks.

**「Takeaway」** Goedecke&\#x27;s core thesis is that the centaur age will likely last at least a decade—long enough for engineers to make serious plans or finish their careers—because chess, the most recent comparable centaur age, lasted twenty years and was attacked by the same AI forces now targeting software.

**Tags**: `#AI-assisted development`, `#software engineering career`, `#human-AI collaboration`, `#opinion essay`, `#automation`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Apple Cuts iPhone 18 Pro Orders by 15%, Shares Dip in Pre-Market](https://www.forbes.com/sites/siladityaray/2026/10/09/apple-shares-dip-after-report-says-its-cutting-iphone-18-pro-component-orders/) ⭐️ 7.0/10

Apple reportedly reduced component orders for the iPhone 18 Pro and Pro Max by at least 15% this month amid weaker-than-expected demand, triggering a more than 1.6% pre-market stock decline on Friday.

telegram · zaihuapd · Oct 9, 13:31

**「Background」** The iPhone 18 Pro and Pro Max launched on September 9, 2026, starting at $1,199 and $1,299 respectively — a $100 price increase over the models they replaced. Apple also skipped a standard iPhone 18 this year, deferring it to early 2027, and is set to release its first foldable, the iPhone Duo, on October 23.

<details><summary>References</summary>
<ul>
<li><a href="https://eazypc.in/iphone-duo-apple-price-hike-2026-india/">IPhone Duo Costs ₹2.99 Lakh: 2026 Apple Price Hike</a></li>
<li><a href="https://www.macrumors.com/2026/10/09/apple-cuts-iphone-18-pro-orders-price-demand/">Apple Reportedly Cuts iPhone 18 Pro Orders After Price Hike...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#iPhone 18 Pro`, `#Supply Chain`, `#Consumer Demand`, `#Stock Market`

---