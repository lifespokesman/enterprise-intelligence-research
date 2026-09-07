# NOW｜当前研究驾驶舱

> 这个文件只服务于“快速恢复研究状态”。无论中断多久，重新开始时先读这里。

## 1. 我现在研究什么

当前主问题：

**当 AI 开始成为新的组织智能主体后，企业应该如何重新设计决策权、责任、协调机制、企业边界和组织学习？**

当前阶段先把手头三份研究报告真正“学懂”，不是只完成 AI 的七问提炼：

1. Phanish Puranam｜Human–AI collaborative decision-making as an organization design problem ← **P-001 本轮精读完成（2026-09-07）**
2. Amir Goldberg & Phanish Puranam｜Purpose not prediction: the role of managers in the age of AI ← **P-002 原文准备中；尚未开始正文精读**
3. 吕源｜管理者—人工智能关系中的管理主体扩展 ← 待开始

当前 Active Research Question：**P-002 如何界定管理者的工作与 AI 的作用？**先取得原文，从作者自己的问题与论证顺序开始，不根据标题预设结论。

## 2. 公开研究框架已稳定为“两类公开证据 + 一条产业路线”

Q1–Q5 仍然是长期问题地图。

公开仓从两类公开证据寻找答案：

### Academic Theory

用于理解概念、机制、经典问题和边界条件。

### Public Industry Evidence

包括：

- `[Product Fact]`
- `[Product Claim]`
- `[Industry Case]`
- `[Analyst View]`
- `[Policy / Standard]`
- `[Counter Evidence]`

研究链条：

`Q1–Q5 → Theory + Public Industry Evidence → Hypothesis → Judgment → Engineering / Governance Implication`

公开仓硬边界：

> **私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。**

公开仓不保存、引用或描述私人、客户、公司内部或非公开项目材料，也不使用公共 `[Field Observation]` 标签。

## 3. Industry Roadmap 已建立

产业路线不按厂商划分，而从智能主体进入企业必须解决的 Engineering + Governance 问题反推。

### Track E｜Intelligent Subject Engineering

- E1 Agent Production / Harness / Runtime
- E2 Enterprise Context / World Model / Ontology
- E3 Capability / Action Infrastructure
- E4 Feedback / Evaluation / Evolution

### Track G｜Intelligent Subject Governance

- G1 Identity / Ownership
- G2 Authority / Policy
- G3 Human Control / Accountability
- G4 Trace / Audit / Lifecycle

完整路线：`industry/ROADMAP.md`

记忆方式：

> **主体成立 → 理解企业 → 作用企业 → 企业学习**
>
> 治理同步经历：**身份 → 权限 → 人类控制与责任 → 追溯与生命周期**

厂商、产品、框架与公开案例只是 Observation Targets，不是路线本身。

## 4. 认知演进开始单独记录

新增：`EVOLUTION.md`

它不保存聊天流水，而只记录发生了实质变化的认知节点。

当前研究资产职责：

- `NOW.md`：现在研究到哪里；
- `EVOLUTION.md`：为什么认知发生变化；
- `JUDGMENTS.md`：现在有哪些判断值得保留和承担；
- `topics/`：成熟判断如何形成完整公开表达。

重大认知节点尽量标记观点来源：

- `User Insight`
- `External Trigger`
- `Co-developed`
- `AI Proposal`

2026-09-04 的仓库基础框架和六个关键认知转折已经作为 Baseline 写入 `EVOLUTION.md`。

## 5. 当前论文学习方法

原来的：

`论文 → 原文压缩 → 七问 → Judgment`

仍然太快，因为压缩会丢掉概念形成和作者论证过程。

现在固定改为：

`Source Walkthrough 原文精读`

→ `Concept Reconstruction 概念/理论教学`

→ `Q1-Q5 + 七问研究映射`

→ `Human Takeaways`

→ `是否更新 JUDGMENTS`

详见：`research/paper-review-plan.md`。

## 6. P-001 当前状态｜本轮精读完成

**完成的是理论理解与本轮研究解释，不是企业应用方法的验证。**

2026-09-07 的恢复检查发现并补清了以下混淆：

- 专业化收益 / 聚合收益是收益机制，不是 Figure 2 的两个分类维度；
- Figure 2：相同 / 不同决策任务 × 并行 / 串行；
- Table 1：独立 / 相互依赖的反馈 × 交流受限 / 交流可行；
- 任务依赖不等于反馈依赖；Coupled 不以“看不清对方”为必要条件；Vicarious 不能只凭“独立反馈”判定；
- Learning Configuration 描述学习信息条件；Censored Inputs 描述可见样本受筛选；Superstitious Learning 涉及错误归因形成或强化错误认识；
- 理解分类之后仍需收益条件、失败条件与比较验证，才能形成应用方法。

本轮已完成 A/B 概念理解、C 七问校正和 D 吸收记录。以后恢复时先读导航与吸收记录；只有出现具体概念缺口才回看原文，不重复整套分类检查。

- 原文与概念导读：[P001 source walkthrough](research/paper-reviews/P001_puranam_2021_source-walkthrough.md)
- 七问、吸收记录与应用缺口：[P001 research review](research/paper-reviews/P001_puranam_2021_hacd.md)

### 应用验证待办｜暂不启动

**U-P001-01：给定一个具体企业决策任务，怎样选择单主体、专业化分工或判断聚合，并设计能验证整体收益的反馈？**

状态：Backlog。不是 P-001 精读未完成，也不新增一级问题。

启动条件：明确任务、现有流程、可公开核查或明确标记为合成的样例，以及质量、成本、责任与运行约束。公开结论最终必须由公开证据独立支撑；合成例子只验证机制可行性，不代表企业效果。

详细候选方法与证据缺口见 P-001 阅读卡。当前不建设通用企业选型方法，也不批量搜集厂商案例。

## 7. 当前最重要原则

1. **先理解作者，再评价作者。**
2. **七问是研究映射，不是论文阅读入口。**
3. 不熟悉的管理学概念必须解释，不允许只保留术语。
4. 必须区分 `[原文] / [作者引用] / [背景补充] / [我们的推论]`。
5. 用户没有形成自己的理解以前，不急着用论文修改 JUDGMENTS。
6. **Q1–Q5 是问题，Theory + Public Industry Evidence 是公开证据。**
7. **Industry Roadmap 是 Engineering + Governance 的问题路线，不是厂商分类。**
8. 不让教授论文垄断研究，也不让产品营销或 Analyst View 替代验证。
9. 任何公开 Judgment 都必须能够由公开证据独立成立。
10. 重大认知变化进入 `EVOLUTION.md`；AI 提出的漂亮表述不能自动升级为“我的判断”。

## 8. 当前 JUDGMENTS 状态

P-001 对 J-001 / J-002 / J-005 已提出更新建议，但暂时不直接修改。

本轮理论理解已完成，但没有新增足以支持判断升级的企业验证证据。J-001 / J-002 / J-005 的关联解释保留在阅读卡；JUDGMENTS.md 的内容与状态均不修改。后续通过 P-002 / P-003 和公开产业证据继续交叉验证。

## 9. 下一步唯一动作

**取得 P-002 的合法可读全文，按 Part A Source Walkthrough 开始精读。**

- 论文：Amir Goldberg & Phanish Puranam (2026), *Purpose not prediction: the role of managers in the age of AI*。
- [期刊入口 / DOI](https://doi.org/10.1007/s41469-026-00205-y)；期刊标注为 Editorial。
- 2026-09-07 本轮访问仅取得期刊预览，未取得全文；公开检索未找到可读的作者稿。此处描述本次获取状态，不宣称全文不存在。
- 可使用研究者合法持有的 PDF 或作者公开稿；获取合法阅读权限不代表有权把订阅 PDF 上传到公开仓。
- 全文未取得前，不用标题、媒体报道、作者其他文章替代原文精读，不生成完成态的 A/B/C/D 记录。

## 10. Resume Here

> P-001 于 2026-09-07 完成本轮精读。核心是两种收益机制、两套二维分类，以及组织结构对学习机会和归因的影响。
>
> 企业应用验证仍是 Backlog（U-P001-01）；这不构成重开 P-001 概念补课的理由。
>
> 当前唯一下一步：取得 P-002 原文，再从作者自己的问题、文章性质与论证顺序开始 Part A。
>
> P-001 的应用建议仍是 AI Proposal；EVOLUTION 新增候选方法节点，JUDGMENTS 未升级。公开仓不接收私人项目证据链。

_Last updated: 2026-09-07_
