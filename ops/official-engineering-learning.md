# Official Engineering Knowledge Learning Stream

Version: **v0.1**
Status: **Pilot**
Owner: `knowledge_learning`

> 这是一条官方工程知识学习流，不是新的 Research Problem，也不是 Research Runner 的第二个运行态。

## 1. 目的与边界

本流持续处理 OpenAI、Anthropic 等一线厂商公开的工程文章、技术指南和架构实践：

```text
Official source discovery
→ source verification
→ value / freshness / gap screening
→ reading recommendation
→ human-guided learning
→ optional knowledge card
→ optional research bridge
→ candidate cognitive correction
```

它回答“这项工程机制怎样工作、在哪些条件下有用、边界是什么、我是否真的理解”；Research Runner 回答“证据如何推进一个 Active Problem 的 Evidence Gap”。两条流可以互相链接，但不共享运行状态。

本流不：

- 创建正式 Research Problem、Hypothesis、Evidence、Judgment 或 Principle；
- 把厂商实现自动升级为通用架构原则；
- 把 AI 摘要当作人的理解；
- 把 Product Claim 当作 Product Fact 或企业结果；
- 为每篇发现的文章自动生成知识卡；
- 修改 `research/RESEARCH_STATE.yaml` 或 Research Runner 的 `next_action`。

## 2. 允许的来源与导航维度

第一阶段只收录可访问、可核验的官方来源：

- OpenAI 官方工程文章、官方开发者指南和官方业务技术指南；
- Anthropic 官方工程文章和官方开发者文档。

导航维度是检索和去重标签，不是八个新目录：

`Model / Reasoning → Prompt / Context → Tool Calling → Agent / Workflow → Skills → Harness / Runtime → Multi-Agent → Evaluation / Security`

发现时可使用官方站点的 sitemap、RSS、站内搜索或页面链接；队列中的 source URL 必须指向官方页面或官方文件。无法稳定核验标题、发布日期、版本或正文的资料只能进入 `NEEDS_REVIEW`，不得写成已核验来源。

## 3. 队列与状态机

唯一候选入口是 [`source-queue.md`](../learning/official-engineering/source-queue.md)。每个条目至少记录：

- Source ID、厂商、准确标题、官方 URL、发布日期 / 版本；
- 来源核验状态与最后核验时间；
- 导航维度、相对当前知识缺口的增量和阅读优先级；
- 可选的 Research Bridge 候选；
- 当前状态和下一步。

状态只能按下列路径前进，回退或归档时写明原因：

```text
DISCOVERED
→ AI_ANALYZED
→ SELECTED
→ READING
→ HUMAN_UNDERSTOOD
→ APPLIED
→ ARCHIVED
```

`NEEDS_REVIEW` 可从任何状态进入，用于来源、版本、解释或人类确认存在问题的条目。只有研究者明确完成理解确认后，才能进入 `HUMAN_UNDERSTOOD`；AI 不得代替确认。

`SELECTED` 表示人选择了要读的条目。AI 可以给推荐和排序，但“推荐”不等于 `SELECTED`。没有实质增量的条目可以从 `AI_ANALYZED` 直接 `ARCHIVED`，不要制造阅读债务。

## 4. 轻量 A–F 学习协议

官方工程资料沿用论文 Part A–E 的纪律，但缩短为适合工程文章的六步。每次只做足以支持下一步的工作。

### Part A｜Source Understanding

恢复作者的原始问题、背景、技术机制、案例、明确结论和未解决问题。保留原始术语和必要短引，区分作者描述与我们的解释。

### Part B｜Mechanism Reconstruction

回答：为什么需要？怎样工作？解决什么问题？与相邻机制有什么区别？说明依赖的模型能力、系统边界和失败方式。

### Part C｜Architecture Variables

提取有效条件、失败条件、替代方案、成本和维护变量，并标注哪些判断可能只适用于当前模型能力阶段。不得把厂商的命名直接当成稳定架构层。

### Part D｜Enterprise Translation

只在有帮助时映射到 `Business Application / Workflow / Agent / Context / Harness / Runtime / Action / Governance`。不为完成表格而强行关联全部主题；企业映射必须标记为 `RESEARCH_INFERENCE`。

### Part E｜Human Takeaways

通过简短解释、概念比较、反例问题或虚构案例应用确认理解。研究者自己写出 2–5 个掌握的机制、适用边界、旧认识变化和仍不确定之处，才可将状态改为 `HUMAN_UNDERSTOOD`。

### Part F｜Research Bridge

只有资料对现有 Problem 产生实质增量时才执行：关联已有 Problem，说明支持 / 挑战 / 收窄什么假设，提出待验证问题，并建议是否交给原 Research Runner。该步骤只产生候选链接或候选问题，不自动写入 Evidence Ledger、Hypothesis、JUDGMENTS、PRINCIPLES 或正式 Problem。

## 5. 五种内容必须分开

知识卡或学习记录中使用以下标签，不能互相改写：

| 标签 | 含义 |
|---|---|
| `SOURCE_CLAIM` | 作者明确提出的观点；可引用或准确转述 |
| `SOURCE_MECHANISM` | 原文描述的工程机制、接口、流程或限制 |
| `AI_EXPLANATION` | AI 为帮助理解而写的解释、类比或整理 |
| `RESEARCH_INFERENCE` | 映射到企业架构或现有研究的推论 |
| `HUMAN_TAKEAWAY` | 研究者确认后留下的个人理解和边界 |

厂商的性能、客户效果、路线图和“最佳实践”先标为 `SOURCE_CLAIM` / `Product Claim`，除非有独立公开证据，不写成通用结论。

## 6. 知识卡晋级规则

`learning/official-engineering/notes/` 只保存经过选择、具有复用价值的知识卡。知识卡不是发现日志：

1. `DISCOVERED` / `AI_ANALYZED` 只停留在队列；
2. 人选择阅读后才进入 `SELECTED` / `READING`；
3. AI 可协助起草解释，但不自动创建已完成知识卡；
4. 研究者完成 Part E 并明确确认后，才创建或更新卡片并设为 `HUMAN_UNDERSTOOD`；
5. 相同机制优先引用或更新既有卡片；
6. `APPLIED` 只表示研究者在公开、合成或实际允许的场景中使用并记录了边界，不表示企业结果已被证明。

卡片字段模板见 [`notes/README.md`](../learning/official-engineering/notes/README.md)。

## 7. 自动发现任务的写入边界

Codex Automation 可以：

- 检查允许的官方来源是否有新资料；
- 核验标题、URL、日期、版本和页面可读性；
- 按主题和已有条目去重；
- 评估阅读优先级并生成简短推荐；
- 更新 `learning/official-engineering/source-queue.md`；
- 在队列中提出候选 Research Bridge。

Codex Automation 只能写入上述 source queue（必要时修正同一条目的来源核验字段）。它不得写入 `research/`、`NOW.md`、`JUDGMENTS.md`、`PRINCIPLES.md`、正式 Problem / Hypothesis 文件或知识卡正文，也不得标记 `HUMAN_UNDERSTOOD`、`APPLIED`，不得修改 Research Runner 运行态。任何越界建议只能作为队列中的 `candidate` 文本，等待人工审核。

## 8. 验收与停止条件

每次自动发现任务结束检查：

1. 每个新增条目都来自允许的官方来源，并有准确标题、URL、日期 / 版本或明确 `NEEDS_REVIEW`；
2. 没有重复条目、批量摘要或无阅读价值的堆积；
3. 推荐说明包含“为什么现在值得读、相对已有知识新增什么、何时停止”；
4. `SOURCE_CLAIM`、`SOURCE_MECHANISM`、`AI_EXPLANATION`、`RESEARCH_INFERENCE` 没有混写；
5. 没有自动创建知识卡或声称用户已理解；
6. 没有写入 Research Runner 或正式研究状态；
7. 有效修改只限 source queue，并通过 `git diff --check`、仓库一致性检查和 PR 人工审核。

没有新增高价值资料时记录 `NO_MATERIAL_UPDATE`，不创建空 PR。

## 9. Codex Automation 任务提示词

将以下提示词作为独立于 Research Runner v0.4 的定期任务使用。调度频率由用户在 Codex Automations 中选择；任务每次都从最新 `origin/main` 的独立分支开始，并通过 PR 等待人工审核。

```text
你运行的是 Official Engineering Knowledge Learning Stream v0.1，不是 Research Runner。

先读取 AGENTS.md、REPOSITORY_STATE.yaml、context/CURRENT.md、context/TOPIC_INDEX.md，再读取 ops/official-engineering-learning.md 和 learning/official-engineering/source-queue.md。只检查 OpenAI 官方工程文章 / 开发者指南和 Anthropic 官方工程文章 / 开发者文档。核验标题、官方 URL、发布日期或版本、页面正文可读性和最近更新时间；无法核验的条目标为 NEEDS_REVIEW，不凭记忆补全。

按 Model / Reasoning、Prompt / Context、Tool Calling、Agent / Workflow、Skills、Harness / Runtime、Multi-Agent、Evaluation / Security 去重和排序。对每个候选写一句中文推荐：为什么现在值得读、相对已有队列新增什么、建议何时停止。把新资料和状态变化只写入 learning/official-engineering/source-queue.md。保留 SOURCE_CLAIM、SOURCE_MECHANISM、AI_EXPLANATION、RESEARCH_INFERENCE 的边界。

只能使用 DISCOVERED、AI_ANALYZED、NEEDS_REVIEW、ARCHIVED 等自动可判定状态。不得把任何条目标为 SELECTED、READING、HUMAN_UNDERSTOOD 或 APPLIED；不得创建或批量生成 notes 知识卡；不得修改 research/、NOW.md、JUDGMENTS.md、PRINCIPLES.md、Problem / Hypothesis、research/RESEARCH_STATE.yaml 或任何 Research Runner 状态。若发现与现有研究的可能关联，只写 candidate Research Bridge，不写 Evidence Ledger。

若没有高价值新增或需要人工选择，记录 NO_MATERIAL_UPDATE 并不制造空 PR。完成后运行 git diff --check 和 python3 scripts/check_repository_state.py，报告 Changed Files、候选数、NEEDS_REVIEW 数、Research Bridge 候选、检查结果、branch、commit、PR 和 merge status。不要自动合并。
```
