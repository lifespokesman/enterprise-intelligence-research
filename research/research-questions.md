# Research Questions｜具体问题、证据缺口与工程桥接

Updated: 2026-09-11  
Q1–Q5 仍然是长期问题地图；本文件负责把大问题落到**可以被解释、搜索、工程翻译和验证的具体问题**。

> 研究的基本单位是问题，不是论文。

完整方法见 [`RESEARCH_LOOP.md`](RESEARCH_LOOP.md)。论文只是 Theory Evidence 的一种来源；公开产品、案例、开源实现、Analyst View、Policy / Standard 和 Counter Evidence 都可以参与回答问题。

---

## 1. 从问题到原则

每个值得持续研究的问题尽量沿下面的链条推进：

`Concrete Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle → New Problem`

问题卡至少记录：

- **Problem**：到底哪里解释不了 / 设计不清？
- **Q1–Q5**：它属于哪个长期问题？允许跨多个 Q；
- **Evidence Gap**：目前缺什么理论、产品、案例或反例？
- **Engineering Translation**：如果当前解释成立，对架构或治理意味着什么？
- **Validation**：如何用公开、开源、合成或可复核方式检验？
- **Principle Link**：是否已经进入 [`PRINCIPLES.md`](../PRINCIPLES.md)；
- **Status**：Active / Candidate / Backlog / Closed。

私人工作经验可以启发 Problem，但公开仓不保存其来源、行业身份或项目证据链。

---

## 2. 当前具体问题地图

以下条目是研究导航，不等于最终判断。

| ID | Concrete Problem | Q1–Q5 | 当前证据 / 候选材料 | Engineering Translation | Principle Link | 状态 |
|---|---|---|---|---|---|---|
| **R-001** | 给定一个高价值判断任务，Human 与 AI 应何时单主体、专业化分工或判断聚合？最终决策权和反馈怎样设计？ | Q1 / Q3 / Q5 | P-001 已提供分工、依赖与学习框架；P-002 可补管理者工作与目的/规范边界；P-005 可补聚合条件 | 任务分解、串并行结构、决策权、反馈架构与评价基线 | MP-001；未来候选 AP | **Active** |
| **R-002** | 当企业语义隐性、碎片化、跨系统不一致时，AI 到底需要多强的显式 Enterprise Context / Semantic Model / Ontology？ | Q3；关联 Q1 | EV-007；E2；P-006 提供路线图候选但没有企业比较验证；当前理论与公开案例仍不足 | Retrieval → Context → Semantic Model → Operational Ontology / World Model 的分级选择 | AP-002 | **Candidate** |
| **R-003** | Agent 的局部运行经验如何变成可保留、可复用、可验证的组织长期能力？ | Q5 | P-001 只解释部分反馈/学习条件；组织学习理论与长期案例仍缺 | Trace → Eval → Candidate Change → Validation → Governed Promotion | AP-004 | **Candidate** |
| **R-004** | Agent 有能力调用工具后，Business Validity、Capability、Authority、Human Control 与 Accountability 应如何组合？ | Q2 / Q1 | J-004；G2/G3/G4；公开治理产品、Policy / Standard 与案例待补 | Action Policy、审批、授权、审计、例外与生命周期 | AP-003 | **Candidate** |
| **R-005** | AI 降低发现、调用和协调能力的成本后，哪些能力仍应企业内部化，哪些可以动态外部调用？ | Q4 | 当前核心论文证据薄弱；需要 Coase / Williamson 与公开产业证据 | Capability Registry、外部 Agent / Service 调用、风险与交易成本边界 | 尚无 | **Backlog** |

当前不为了“填满地图”强行增加问题。一个问题只有在反复出现、影响设计，或现有原则无法解释时才升级。

---

## 3. 旧条目映射

### U-P001-01｜企业决策协作选型与反馈验证

原条目并入 **R-001**。

原问题：给定一个具体企业决策任务，怎样选择单主体、专业化分工或判断聚合，并设计能验证整体收益的反馈？

保留的验证要求：

- 明确任务和现有流程；
- 有比较基线；
- 有可核查或明确标记为合成的样例；
- 同时评价质量、成本、责任与运行约束；
- 合成例子只能检验机制可行性，不代表企业效果。

### RQ-VSM-01｜VSM 是否可以作为 Human-Agent 混合企业的组织元模型？

状态：**Backlog**。

VSM 仍是候选理论观察线，不因框架完整性要求而启动。只有某个 Active Problem 明确需要 VSM 才进入搜索或阅读。

详见：[`vsm-ai-research.md`](vsm-ai-research.md)。

---

## 4. Active Problem 规则

一个时期只保留一个 Active Problem。

**论文编号不能充当 Active Problem。**例如“下一步读 P-002”不是研究问题；必须先写成“P-002 被用来解释哪个具体问题”。

当没有明确 Active Problem 时，下一步不是继续论文队列，而是：

1. 从工作、研究或已有判断中抽象一个公开可表达的问题；
2. 判断它影响哪个设计决策；
3. 再去选择 Theory / Industry Evidence；
4. 对论文动态判断 A / B / C，而不是默认精读。

---

## 5. 关闭问题的条件

问题不要求获得“永久答案”才关闭一轮研究。满足以下条件即可阶段关闭：

- 已形成足够清晰的机制解释；
- 已完成工程翻译；
- 已知道怎样验证或已经完成一次验证；
- 已形成 Candidate / Supported Principle，或明确证明暂时不能形成原则；
- 已记录适用边界和下一问题。

研究完成度优先看“问题是否得到更好的解释、设计或验证”，而不是阅读篇数。
