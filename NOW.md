# NOW｜当前研究驾驶舱

> 本文件只服务于“快速恢复研究状态”。当前研究单位是 **Active Problem + Hypothesis Package**，不是 Active Paper。

Updated: 2026-09-13

---

## 1. 当前研究方法｜v2.0 Hypothesis–Validation

研究方法已从“问题驱动证据研究”进一步升级为“问题驱动的假设—验证研究”。

当前主闭环：

> **现实刺激 → 问题抽象 → Initial Hypothesis / Candidate Solution Path → 定向找证据 → 机制理解 → Revised Hypothesis → Engineering Hypothesis → Validation → Principle → 新问题**

结构化表达：

`Signal → Problem → H0 / Candidate Path → Evidence → Mechanism → H1 → Engineering Validation → Principle`

核心纪律：

> **研究不是寻找支持假设的证据，而是寻找足以判断假设是否成立的证据。**

v2.0 是试运行方法，不是永久规则。升级原因、试用标准与回滚方式见：

- [`research/RESEARCH_LOOP.md`](research/RESEARCH_LOOP.md)
- [`research/METHOD_CHANGELOG.md`](research/METHOD_CHANGELOG.md)

升级前回滚基线：`b56caf344de02cfef30b9a7d607baf9d609615b5`。

---

## 2. 当前 Active Problem｜RP-002 Enterprise Data–Model Relationship

> **企业已有的数据资产，与大模型之间到底应该建立什么关系？企业真实世界究竟通过哪些机制进入 Model / Agent？**

公开仓只保留抽象后的问题与假设，不记录私人项目来源、客户身份或非公开证据链。

完整问题树与 H-RP002 系列见 [`research/research-questions.md`](research/research-questions.md)。

---

## 3. RP-002 当前 Problem + Hypothesis Package

### Problem

企业长期积累的数据、文档、系统和经验，并不会因为“已经治理过”就自动成为 Model / Agent 可以可靠理解、调用、验证和持续更新的 Context。

### 当前 Initial Hypotheses / Candidate Paths

- **H-RP002-01**：`Data Availability ≠ Context Usability`。AI 数据瓶颈可能从“有没有数据”扩展到“能否把正确、相关、新鲜、可解释的数据编译成当前任务可用 Context”。
- **H-RP002-02**：传统 Data Service 之上，可能逐步出现面向智能主体的 Semantic / Context / Evidence 能力；候选机制是 Model / Agent 成为不同于 Human / BI / Application 的新消费者，而不是传统数据治理本身失效。
- **H-RP002-03**：AI Context 更可能是一组目标能力，而不是所有企业按同一顺序建设的一套平台；System of Record、数据平台成熟度、业务数字化程度与既有数据 / 能力的机器可调用性可能共同决定不同建设路径。
- **H-RP002-04｜Candidate Solution Path**：不同起点可能收敛到一个候选逻辑闭环：`业务事实 → 对象 / 身份 → 状态 / 事件 / 关系 → 规则 / 知识 / 风险基线 → 角色 / 任务 / 权限 → 证据 / 历史 / 当前环境 → 动态 Context → Model / Agent → 建议 / 行动 → 真实结果 → 反馈更新`。
- **H-RP002-05**：AI Context Readiness 不能简单由“有没有大数据平台”代理，可能更取决于 `Reality Capture × Object / Process Stability × Feedback Closure`。该表达只是短板效应假设，不是数学公式。

以上均为 Working Hypothesis，不进入 JUDGMENTS / PRINCIPLES。

---

## 4. 当前第一轮研究问题

### RQ-002-A｜Relationship Types

> 业界真实存在几种 Data → Model / Agent 关系？

候选包括：Training / Dataset、Knowledge / RAG、Fact Query / SQL / API、Tool / Action、Semantic / Ontology、Context、Eval、Feedback。

目标：`Enterprise Data–Model Relationship Map v0.1`。

### RQ-002-B｜Mechanism Boundaries

> Dataset、Knowledge Base、SQL、API、Tool、Ontology、Context、Eval、Feedback 的边界与组合关系是什么？

目标：`Data–Model Mechanism Boundary Table v0.1`。

### RQ-002-C｜Architecture Evolution

> 哪些仍是传统数据治理 / 数据平台能力，哪些因 Model / Agent 成为新消费者而显著新增或强化？

本轮额外验证一个候选机制：

> **Semantic / Context / Evidence 等新增能力，是否可以主要解释为 Model / Agent 成为新的企业数据消费者后，对 Data Service 提出了不同于 Human / BI / Application 的消费要求？**

如果该机制不成立，需要寻找更好的解释，而不是把新能力直接归因于“AI 时代”。

目标：`Traditional Data Platform → AI-ready Context Architecture v0.1`。

### RQ-002-D｜Starting-State Pathways

> 不同企业起点下，AI Context 应怎样建设？

当前三类待验证路径：

1. 有业务系统，无统一数据平台；
2. 已有业务系统 + 大数据 / 数据平台；
3. 业务系统本身尚不完整。

矩阵横向增加 **Machine-accessible Capability** 维度（L0：封闭于 UI / 人工操作 → L4：Agent 可发现、可授权、可调用的 Tool / Capability），用于解释相同数据成熟度下不同的接入成本与行动边界；不在 RP-002 中展开完整 E3 问题。

目标：`AI Context Starting-State Pathway Matrix v0.1`。

---

## 5. 下一步证据研究怎么做

不先继续论文编号，也不先画完整解决方案。

围绕 RQ-002-A / B / C 优先寻找：

- **[Theory]**：Knowledge Representation、Semantic / Context、Information Integration、Data–Reasoning 关系；
- **[Product Fact]**：主流 Data / Lakehouse / AI Platform 如何真实向 Model / Agent 提供数据；
- **[Open-source Implementation]**：RAG、structured query、semantic graph、context、eval 的工程实现；
- **[Industry Case]**：公开企业实践，尤其是不同数字化成熟度起点；
- **[Policy / Standard] / [Analyst View]**：行业共性与治理边界；
- **[Counter Evidence]**：不需要复杂语义层也能工作的场景、复杂本体仍失败的案例、不同于当前路径的成功方式。

每条 Evidence 不只问“讲了什么”，而要标记它对当前 H 的作用：

`Supports / Challenges / Narrows / Revises / Rejects / Opens Alternative`。

---

## 6. 当前预期成果

RP-002 第一轮暂定形成：

1. **Relationship Map**；
2. **Mechanism Boundary Table**；
3. **Architecture Evolution Map**；
4. **Starting-State Pathway Matrix**；
5. **Context Assembly Loop Sketch**；
6. **AI Context Readiness Diagnostic v0.1**（若 H-RP002-05 获得足够支持）；
7. **Hypothesis Decision**：H-RP002-01～05 分别被支持、修正、拆分还是否定；
8. **Principle Decision**：只有证据与必要验证足够时，才考虑进入 `PRINCIPLES.md`。

---

## 7. 当前不要做什么

- 不因为已经有 H0 就只找支持材料；
- 不默认 Ontology、RAG、Context Platform 或 Data Platform 是答案；
- 不为了完整性收集所有厂商；
- 不按论文编号顺序继续阅读；
- 不把 Human–AI 初步讨论直接升级成 Principle；
- 不让方法记录的维护成本超过研究本身。

---

## 8. Resume Here｜下次从这里继续

> 当前 Active Problem：**RP-002 Enterprise Data–Model Relationship**。
>
> 当前方法：**Problem-driven Hypothesis–Validation v2.0**。
>
> 下一步优先从 RQ-002-A / B / C 开始公开证据研究；每个证据明确判断它对 H-RP002-01～05 的作用，而不是只做资料摘要。
>
> A / B / C 基本清楚后，再用 RQ-002-D 检验三类企业起点，并判断 H-RP002-04 / 05 是否需要修正。
>
> 最终目标不是证明最初想法正确，而是得到更接近真实的 H1、可验证的 Engineering Hypothesis，以及少量真正站得住的 Architecture Principle。
