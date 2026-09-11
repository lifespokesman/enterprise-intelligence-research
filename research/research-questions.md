# Problem Map｜企业 AI 问题地图

Updated: 2026-09-11  
本文件不再只是“研究问题清单”，而是用于管理**问题之间的层级、派生关系、证据、架构翻译与工程验证**。

> **知识管理的基本单位从“论文 / 对话 / 资料”逐步切换为“问题”。**

完整研究闭环见 [`RESEARCH_LOOP.md`](RESEARCH_LOOP.md)。论文、产品、案例和开源项目都只是问题的 Evidence Provider，不构成独立阅读队列。

---

## 1. 问题地图的四层结构

```text
Q1–Q5 Long-term Questions
长期组织问题
        ↓
RP｜Research Problem
阶段性母问题 / 问题域
        ↓
CQ / AQ / EQ / VQ
认知 / 架构 / 工程 / 验证问题
        ↓
Evidence → Mechanism → Engineering Hypothesis → Validation → Principle
```

四类子问题：

- **CQ｜Cognitive Question**：现实为什么会这样？真正机制、变量和边界是什么？
- **AQ｜Architecture Question**：如果这个认知成立，企业 AI 架构应该怎样设计？
- **EQ｜Engineering Question**：这个架构怎样实现、运行、治理和观测？
- **VQ｜Validation Question**：怎样用公开案例、开源实现、合成实验或 Benchmark 判断它是否真的成立？

这些不是四个文件夹，而是同一个 Research Problem 的不同纵深阶段。一个问题通常会经历：

`现象 → CQ → AQ → EQ / VQ → Principle → 新现象 / 新问题`

---

## 2. Problem Map 总览

| RP | Research Problem｜母问题 | 主要 Q1–Q5 | 主要 E/G Track | Principle Link | 状态 |
|---|---|---|---|---|---|
| **RP-001** | Human 与 AI 的决策结构如何设计？何时单主体、专业化分工或判断聚合，最终决策权和反馈怎样配置？ | Q1 / Q3 / Q5 | E1 / E4；G3 | MP-001；未来候选 AP | **Active** |
| **RP-002** | 企业已有的数据资产，与大模型之间到底应该建立什么关系？怎样从“有数据”走向模型可理解、可调用、可验证的企业上下文？ | 主 Q3；强关联 Q5；关联 Q1 | 主 E2；关联 E3 / E4 | AP-002；未来新增候选 | **Candidate｜High Priority** |
| **RP-003** | Agent 的局部运行经验如何变成可保留、可复用、可验证的组织长期能力？ | Q5 | E4 / G4 | AP-004 | Candidate |
| **RP-004** | Agent 有能力调用工具以后，Business Validity、Capability、Authority、Human Control 与 Accountability 应如何组合？ | Q2 / Q1 | E3；G2 / G3 / G4 | AP-003 | Candidate |
| **RP-005** | AI 降低发现、调用和协调能力的成本后，哪些能力仍应企业内部化，哪些可以动态外部调用？ | Q4 | E3；G2 | 尚无 | Backlog |

说明：

- 一个 RP 可以同时关联多个 Q 和 E/G Track，不强行单归属；
- 只有反复出现、影响架构设计、需要外部证据支撑的问题才升级为 RP；
- 临时灵感先作为 Signal，不为了“地图完整”批量创建母问题。

---

# RP-001｜Human–AI Decision Structure

**Core Problem**  
给定一个高价值判断任务，Human 与 AI 应何时单主体、专业化分工或判断聚合？最终决策权和反馈怎样设计，才能既获得能力收益，又保持责任、学习与可验证性？

**Mappings**  
Q1 / Q3 / Q5；E1 / E4；G3。

### Cognitive Questions

- **CQ-001-01**：单主体、专业化分工、判断聚合分别依靠什么机制产生收益？
- **CQ-001-02**：Task Interdependence、Agent Interdependence、反馈结构如何改变 Human–AI 协作效果？
- **CQ-001-03**：能力更强是否等于应拥有最终 Decision Rights？

### Architecture Questions

- **AQ-001-01**：Human / AI 决策链应怎样配置串行、并行、审核、聚合与例外处理？
- **AQ-001-02**：决策权、反馈权、否决权与责任是否应该分开设计？

### Engineering / Validation Questions

- **EQ-001-01**：怎样把不同 Human–AI 决策结构做成可运行的流程 / Agent Pattern？
- **VQ-001-01**：怎样在同一任务上比较质量、成本、责任与学习效果？

### Current Evidence

- P-001：分工、任务依赖、学习结构；已完成本轮精读；
- P-002：管理者工作、purpose / normative appropriateness；待按当前问题判断 A/B 阅读深度；
- P-005：聚合何时可能有效；候选理论证据。

旧条目 `U-P001-01` 并入本 RP。

---

# RP-002｜Enterprise Data–Model Relationship

## 企业已有的数据资产，与大模型之间到底应该建立什么关系？

**Status**：Candidate｜High Priority  
**Origin**：`User Insight`（由真实工作现象触发后抽象为公开研究问题）

## Trigger｜抽象后的现象

企业已经长期积累结构化数据、非结构化文档、指标体系、数据治理规则和数据服务能力，但这些资产并不会自动转化为模型能够**可靠理解、正确调用、保持新鲜并可追溯验证**的企业上下文。

“数据治理完成以后就可以服务 AI”经常被作为一句整体表述，但中间至少存在多个尚未拆开的关系：

- 什么数据需要进入模型参数？
- 什么数据应该作为外部知识？
- 什么事实必须实时查询？
- 什么业务语义需要显式表达？
- 什么信息只应在当前任务动态进入 Context？
- 什么历史数据应该成为 Eval / Benchmark？
- Agent 运行结果怎样重新回到数据与学习体系？

因此真正的母问题不是“怎样做一套新的数据治理平台”，而是：

> **企业真实世界究竟通过哪些机制进入模型？企业数据资产应该分别以什么关系服务 Model / Agent？**

---

## 2.1 Cognitive Questions｜认知问题

### CQ-002-01｜企业数据对模型到底扮演哪些不同角色？

当前先形成一个待验证的角色地图：

```text
Enterprise Data / Enterprise Reality
│
├─ Learning Material
│  → Dataset / Training / Fine-tuning
│
├─ External Knowledge
│  → Knowledge Base / RAG
│
├─ Current Facts
│  → SQL / API / Tool / Query
│
├─ Business Semantics
│  → Semantic Layer / Ontology / World Representation
│
├─ Task Context
│  → Context Engineering / Context Compilation
│
├─ Evaluation Evidence
│  → Eval Set / Benchmark / Ground Truth
│
└─ Runtime Feedback
   → Trace / Outcome / Human Feedback / Learning Asset
```

这不是最终分类，后续需要用公开理论、产品架构与案例验证边界和遗漏。

### CQ-002-02｜为什么“数据治理完成”不等于“AI-ready”？

需要区分至少几组容易混淆的概念：

- Data Availability ≠ Context Usability
- Schema ≠ Business Semantics
- 数据集成 ≠ 模型理解业务关系
- 指标口径统一 ≠ Agent 知道当前任务应使用哪个指标
- 历史数据存在 ≠ 当前事实新鲜、可信、可追溯
- 数据质量问题 ≠ 所有模型错误的来源

**Working Hypothesis H-RP002-01**：

> AI 时代的数据瓶颈可能逐渐从“有没有数据”扩展为“能否把正确、可解释、足够新鲜且与当前任务相关的数据编译成模型可使用的 Context”。

状态：Hypothesis，不进入 JUDGMENTS。

### CQ-002-03｜模型需要的是更多数据，还是更好的企业世界表达？

需要继续区分：

`Raw Data → Governed Data → Semantic Data → Task Context → Enterprise World Representation`

其中 Ontology 只是显式语义 / 世界表达的一种当前工程形态，不预设所有 Agent 都需要完整 Ontology。

### CQ-002-04｜哪些模型错误能够靠数据治理解决，哪些不能？

至少需要区分：

- 源数据错误 / 缺失；
- 口径冲突；
- 时效性问题；
- 业务语义缺失；
- Context 选择错误；
- 模型推理错误；
- 工具调用 / 权限 / 执行错误。

否则“减少幻觉”会成为无法验证的总目标。

---

## 2.2 Architecture Questions｜架构问题

### AQ-002-01｜企业数据进入 Model / Agent 有哪些主要接口模式？

当前先建立 **Data-to-Model Interface Map v0.1**：

| Interface Pattern | 核心关系 | 典型机制 | 主要解决的问题 |
|---|---|---|---|
| **Training Interface** | 数据进入模型学习过程 | Dataset / Pretrain / Fine-tune | 模型长期学会什么 |
| **Knowledge Interface** | 数据作为外部可检索知识 | RAG / Knowledge Base / Vector Search | 模型临时查什么知识 |
| **Fact Query Interface** | 模型读取当前结构化事实 | SQL / Query / Data API | 当前事实是什么 |
| **Tool / Action Interface** | 模型通过工具访问或操作企业系统 | API / MCP / Tool | 如何获取或改变企业状态 |
| **Semantic Interface** | 显式描述对象、关系、状态、规则 | Semantic Layer / Ontology | 数据在业务上意味着什么 |
| **Context Interface** | 按当前任务动态选择和组织信息 | Context Engineering / Context Compiler | 此时此任务应该给模型什么 |
| **Evaluation Interface** | 数据作为正确性与质量基线 | Eval Set / Benchmark / Ground Truth | 模型做得对不对 |
| **Feedback Interface** | 运行结果重新成为学习材料 | Trace / Outcome / Human Feedback | 系统如何持续改进 |

后续研究重点不是继续增加名词，而是验证：这些 Pattern 是否互斥、互补、分层，哪些可以被统一，哪些必须独立。

### AQ-002-02｜Dataset / Knowledge Base / SQL / Tool / Ontology / Context / Eval 到底处于什么层次？

当前需要避免把这些组件并列堆在一张 AI 架构图里。

候选区分：

- Dataset：模型学习什么；
- Knowledge Base：模型需要时查什么；
- SQL / API：当前事实从哪里来；
- Ontology / Semantic Layer：事实在业务上是什么意思；
- Context Engineering：当前任务到底给模型什么；
- Eval：如何判断输出是否正确；
- Trace / Feedback：运行经验如何重新进入资产体系。

### AQ-002-03｜传统 Data Service 是否需要演化出 AI Context / Semantic / Evidence Service？

**Working Hypothesis H-RP002-02**：

传统数据平台主要围绕 Human / Application 消费数据构建：

`Source → Integration → Governance → Warehouse/Lake → Data Service → Application`

AI 时代可能新增一条面向 Model / Agent 的服务链：

`Source → Governance → Semantic / Context → AI-ready Asset → Model / Agent`

这并不意味着传统数据平台必须被替代。需要研究的是：

> **原有 Data Service 之上，是否需要增加面向智能主体的 Semantic / Context / Evidence 能力，以及边界应该在哪里。**

### AQ-002-04｜历史数据与实时业务状态应该如何同时进入 Agent？

历史知识、当前状态和事件流不能简单都塞入 RAG。需要研究：

- Historical Knowledge；
- Operational State；
- Event / Change；
- Rule / Policy；
- Evidence / Freshness；

在 Enterprise Context 中怎样组合。

---

## 2.3 Engineering Questions｜工程问题

- **EQ-002-01**：同一任务分别使用 RAG、SQL/API、Semantic Model / Ontology、组合 Context 时，效果和成本如何比较？
- **EQ-002-02**：如何把既有治理后的数据转换成 Dataset、Knowledge Asset、Eval Set、Semantic Asset 等不同 AI-ready Asset？
- **EQ-002-03**：Context 如何携带 Source、Lineage、Freshness、Permission、Evidence，让模型结果可追溯？
- **EQ-002-04**：实时业务状态怎样进入 Agent Runtime，而不是只依赖历史知识？
- **EQ-002-05**：Semantic Model / Ontology 应由专家预建、AI 自动发现还是 Human-governed 动态生成？怎样校验？

---

## 2.4 Validation Questions｜验证问题

- **VQ-002-01**：能否用一个公开 / 合成业务任务，对比 `RAG only`、`RAG + structured facts`、`RAG + semantic/world context` 三种方案？
- **VQ-002-02**：评价指标除了回答准确率，还应该包含哪些 Context 指标：Consistency、Freshness、Traceability、Action Success、Maintenance Cost？
- **VQ-002-03**：公开产品与架构中，哪些已经把 Data Service 扩展为 Semantic / Context / Evidence 能力？哪些只是产品主张？
- **VQ-002-04**：有没有公开反例证明更强的显式语义层在某些任务中成本高于收益？

---

## 2.5 当前 Evidence Gap

当前**不立即进入论文队列**。先需要建立公开产业和理论证据地图：

1. 数据平台 / Lakehouse / Data Cloud 如何定义 AI-ready data；
2. Knowledge / RAG 产品怎样处理结构化事实与实时状态；
3. Semantic Layer / Ontology / World Model 产品怎样解决业务语义；
4. Context Engineering / Context Platform 怎样组织任务上下文；
5. Eval / Observability 怎样把企业数据变成验证资产；
6. 找 Counter Evidence：哪些简单任务无需显式语义层，哪些复杂任务即使做了本体也不能解决模型错误。

任何厂商主张先标记 `[Product Claim]`，不能直接升级成架构原则。

---

## 2.6 当前与已有认知的关系

### Related Evolution

- `EV-007`：从“本体是企业 AI 基础”到“静态本体是语义鸿沟的阶段性桥梁”。

### Related Principle

- `AP-002`：显式业务语义强度应匹配任务复杂度，不默认所有 Agent 都需要完整 Ontology。

### Derived / Absorbed Question

原来的 **R-002｜AI 需要多强显式 Enterprise Context / Semantic Model / Ontology？** 不再单独作为母问题，正式并入 RP-002，成为 `CQ-002-03 / AQ-002-02 / EQ-002-05` 等子问题。

这次调整避免把“Ontology”本身误当成问题入口。更上位的问题是：

> **企业真实世界怎样通过数据、知识、语义、上下文、工具、评价和反馈机制进入 Model / Agent。**

---

## 2.7 RP-002 的下一步最小动作

先不要搜一堆论文，也不要立即设计完整“AI 数据平台”。

第一步只产出一张：

> **Enterprise Data-to-Model Interface Map v0.1**

目标回答三件事：

1. 业界公开架构中实际存在几种 Data → Model / Agent 关系？
2. Dataset / Knowledge Base / SQL / API / Ontology / Context / Eval / Feedback 的边界与组合关系是什么？
3. 哪些问题属于传统数据治理，哪些是 AI 时代新增的 Context / Semantic / Evidence 问题？

完成这张地图后，再决定需要哪些 Theory、Product Fact、Public Case 和 Counter Evidence。

---

# RP-003｜Agent Experience → Organizational Learning

**Core Problem**  
Agent 的局部运行经验如何变成可保留、可复用、可验证的组织长期能力？

**Mappings**：Q5；E4 / G4。  
**Evidence**：P-001 只解释部分反馈 / 学习条件；组织学习理论和长期公开案例仍缺。  
**Engineering Direction**：`Trace → Eval → Candidate Change → Validation → Governed Promotion`。  
**Principle Link**：AP-004。  
**Status**：Candidate。

---

# RP-004｜Effective Agency / Authority / Accountability

**Core Problem**  
Agent 有能力调用工具后，Business Validity、Capability、Authority、Human Control 与 Accountability 应如何组合？

**Mappings**：Q2 / Q1；E3；G2 / G3 / G4。  
**Engineering Direction**：Action Policy、审批、授权、审计、例外与生命周期。  
**Principle Link**：AP-003。  
**Status**：Candidate。

---

# RP-005｜AI 与企业边界

**Core Problem**  
AI 降低发现、调用和协调能力的成本后，哪些能力仍应企业内部化，哪些可以动态外部调用？

**Mappings**：Q4；E3 / G2。  
**Evidence Gap**：交易成本理论、治理理论与公开产业案例。  
**Status**：Backlog。

---

## 3. Signal → Problem 的升级规则

日常研究允许从零散现象开始，不要求每个想法立刻体系化。

```text
Phenomenon / Signal
        ↓
和 AI 讨论、澄清
        ↓
Existing RP ?
  ├─ Yes → 挂入已有 CQ / AQ / EQ / VQ
  └─ No
       ↓
是否反复出现 / 影响设计 / 需要持续证据？
  ├─ No → 保留为 Signal，不制造研究债务
  └─ Yes → 新建 RP
```

新问题优先写关系，而不是新建目录：

- **Parent**：属于哪个 Q / RP；
- **Derived From**：由哪个现象、Evidence 或 Evolution 派生；
- **Related To**：与哪些问题互相影响；
- **Challenges**：挑战哪个 Judgment / Principle；
- **Produces**：可能产生哪个 Principle；
- **Validated By**：由什么公开验证支撑。

---

## 4. Active Problem 规则

一个时期原则上只保留一个主要 Active Problem；其他高价值问题允许标记 `Candidate｜High Priority`，防止真实工作中的重要信号丢失。

**论文编号不能充当 Active Problem。**例如“下一步读 P-002”不是研究问题；必须先写清“P-002 被用来解释哪个 RP / CQ / AQ”。

切换 Active Problem 前只问两件事：

1. 新问题是否比当前问题更直接影响正在形成的架构判断？
2. 当前问题是否已经达到一个可暂停的明确停止点？

---

## 5. 一轮问题研究何时可以暂停

不要求获得永久答案。满足以下条件即可暂停或关闭一轮：

- 母问题边界已经清楚；
- CQ 中的核心机制获得足够解释；
- AQ 已形成候选 Engineering Hypothesis；
- EQ / VQ 已知道最小验证方法，或者完成一次验证；
- 已形成 Candidate / Supported Principle，或明确为什么暂时不能形成原则；
- 新的边界与问题已经可见。

研究完成度优先看：

> **问题是否从“现象”推进到了“可解释、可设计、可验证”。**

而不是阅读了多少论文、收集了多少厂商或创建了多少文件。
