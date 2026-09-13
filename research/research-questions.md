# Problem Map｜企业 AI 问题地图

Updated: 2026-09-13  
本文件用于管理**问题之间的层级、派生关系、证据、架构翻译与工程验证**。

> **知识管理的基本单位从“论文 / 对话 / 资料”切换为“问题”。**

完整研究闭环见 [`RESEARCH_LOOP.md`](RESEARCH_LOOP.md)。论文、产品、案例、开源项目、标准和分析报告都是 Evidence Provider，不构成独立阅读队列。

---

## 1. Problem Map 的基本结构

```text
Phenomenon / Signal
现实刺激
        ↓
RP｜Research Problem
阶段性母问题 / 问题域
        ↓
CQ / AQ / EQ / VQ
认知 / 架构 / 工程 / 验证问题
        ↓
Theory + Public Industry Evidence
        ↓
Mechanism
        ↓
Engineering Hypothesis
        ↓
Validation
        ↓
Architecture / Method Principle
        ↓
New Problem
```

四类子问题：

- **CQ｜Cognitive Question**：现实为什么会这样？真正机制、变量和边界是什么？
- **AQ｜Architecture Question**：如果这个认知成立，企业 AI 架构应该怎样设计？
- **EQ｜Engineering Question**：这个架构怎样实现、运行、治理和观测？
- **VQ｜Validation Question**：怎样用公开案例、开源实现、合成实验或 Benchmark 判断它是否真的成立？

这些不是四个文件夹，而是同一个 Research Problem 的不同纵深阶段。

一个问题通常经历：

`现象 → CQ → AQ → EQ / VQ → Principle → 新现象 / 新问题`

Q1–Q5 仍然是长期组织问题地图；RP 是真正执行研究时的阶段性母问题。一个 RP 可以跨多个 Q 和 E/G Track。

---

## 2. Problem Map 总览

| RP | Research Problem｜母问题 | 主要 Q1–Q5 | 主要 E/G Track | Principle Link | 状态 |
|---|---|---|---|---|---|
| **RP-001** | Human 与 AI 的决策结构如何设计？何时单主体、专业化分工或判断聚合，最终决策权和反馈怎样配置？ | Q1 / Q3 / Q5 | E1 / E4；G3 | MP-001；未来候选 AP | Paused / Candidate |
| **RP-002** | 企业已有的数据资产，与大模型之间到底应该建立什么关系？怎样从“有数据”走向模型可理解、可调用、可验证的企业上下文？ | 主 Q3；强关联 Q5；关联 Q1 | 主 E2；关联 E3 / E4 | AP-002；未来新增候选 | **Active** |
| **RP-003** | Agent 的局部运行经验如何变成可保留、可复用、可验证的组织长期能力？ | Q5 | E4 / G4 | AP-004 | Candidate |
| **RP-004** | Agent 有能力调用工具以后，Business Validity、Capability、Authority、Human Control 与 Accountability 应如何组合？ | Q2 / Q1 | E3；G2 / G3 / G4 | AP-003 | Candidate |
| **RP-005** | AI 降低发现、调用和协调能力的成本后，哪些能力仍应企业内部化，哪些可以动态外部调用？ | Q4 | E3；G2 | 尚无 | Backlog |

原则：

- 只有反复出现、影响架构设计、需要持续外部证据的问题才升级为 RP；
- 临时灵感先作为 Signal，不为了“地图完整”批量创建母问题；
- 一个时期原则上只保留一个主要 Active Problem。

---

# RP-001｜Human–AI Decision Structure

**Core Problem**  
给定一个高价值判断任务，Human 与 AI 应何时单主体、专业化分工或判断聚合？最终决策权和反馈怎样设计，才能既获得能力收益，又保持责任、学习与可验证性？

**Mappings**：Q1 / Q3 / Q5；E1 / E4；G3。  
**Status**：Paused / Candidate。

### Cognitive Questions

- **CQ-001-01**：单主体、专业化分工、判断聚合分别依靠什么机制产生收益？
- **CQ-001-02**：Task Interdependence、Agent / Feedback Interdependence 如何改变 Human–AI 协作？
- **CQ-001-03**：能力更强是否等于应拥有最终 Decision Rights？

### Architecture Questions

- **AQ-001-01**：Human / AI 决策链应怎样配置串行、并行、审核、聚合与例外处理？
- **AQ-001-02**：决策权、反馈权、否决权与责任是否应该分开设计？

### Engineering / Validation Questions

- **EQ-001-01**：怎样把不同 Human–AI 决策结构做成可运行的流程 / Agent Pattern？
- **VQ-001-01**：怎样在同一任务上比较质量、成本、责任与学习效果？

### Current Evidence

- P-001：分工、任务依赖、学习结构；已完成本轮精读；
- P-002：管理者工作、purpose / normative appropriateness；保留为定向证据候选；
- P-005：聚合何时可能有效；候选理论证据。

旧条目 `U-P001-01` 并入本 RP。当前暂停不代表关闭，后续有明确业务 / 架构问题时从已有状态继续。

---

# RP-002｜Enterprise Data–Model Relationship

## 企业已有的数据资产，与大模型之间到底应该建立什么关系？

**Status**：**Active**  
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

真正的母问题不是“怎样做一套新的数据治理平台”，而是：

> **企业真实世界究竟通过哪些机制进入模型？企业数据资产应该分别以什么关系服务 Model / Agent？**

---

## 2.1 Cognitive Questions｜认知问题

### CQ-002-01｜企业数据对模型到底扮演哪些不同角色？

当前先形成待验证的角色地图：

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
│  → SQL / API / Query
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

这不是最终分类。后续要用公开 Theory、Product Fact、Open-source、Industry Case 和 Counter Evidence 检验边界与遗漏。

### CQ-002-02｜为什么“数据治理完成”不等于“AI-ready”？

需要持续区分：

- Data Availability ≠ Context Usability；
- Schema ≠ Business Semantics；
- 数据集成 ≠ 模型理解业务关系；
- 指标口径统一 ≠ Agent 知道当前任务应使用哪个指标；
- 历史数据存在 ≠ 当前事实新鲜、可信、可追溯；
- 数据质量问题 ≠ 所有模型错误的来源。

**Working Hypothesis H-RP002-01**：

> AI 时代的数据瓶颈可能逐渐从“有没有数据”扩展为“能否把正确、可解释、足够新鲜且与当前任务相关的数据编译成模型可使用的 Context”。

状态：Hypothesis，不进入 JUDGMENTS。

### CQ-002-03｜模型需要的是更多数据，还是更好的企业世界表达？

需要继续区分：

`Raw Data → Governed Data → Semantic Data → Task Context → Enterprise World Representation`

其中 Ontology 只是显式语义 / 世界表达的一种当前工程形态，不预设所有 Agent 都需要完整 Ontology。

### CQ-002-04｜哪些模型错误能够靠数据治理解决，哪些不能？

至少区分：

- 源数据错误 / 缺失；
- 口径冲突；
- 时效性问题；
- 业务语义缺失；
- Context 选择错误；
- 模型推理错误；
- 工具调用 / 权限 / 执行错误。

否则“通过数据治理减少模型错误 / 幻觉”会成为无法验证的总目标。

### CQ-002-05｜AI Context 建设是否应该由企业既有数字化 / 数据基础决定？

同一个“企业上下文”目标，在不同企业起点下可能不是同一条建设路径。需要先验证三种常见起点是否足以构成有解释力的路径模型：

1. **业务系统存在，但没有统一大数据 / 数据平台**；
2. **业务系统与大数据 / 数据平台都已经存在**；
3. **业务系统本身都不完整或尚未建立**。

核心认知问题是：

> **AI Context 是一套固定平台能力，还是一组目标能力，其建设顺序与承载位置应由企业当前的 System of Record、数据治理成熟度和业务数字化程度决定？**

该问题暂不预设三种类型已经穷尽所有企业形态，也不预设三条路径最终一定收敛到同一技术平台。

---

## 2.2 Architecture Questions｜当前第一轮研究重点

认知问题说明“为什么值得研究”；下一轮实际研究先围绕四个架构问题寻找证据。其中 A / B / C 先澄清机制，D 再把机制映射到不同企业起点。

### RQ-002-A / AQ-002-01｜Data–Model Relationship Types

> **业界现在真实存在几种 Data → Model / Agent 关系？**

当前候选 **Data-to-Model Interface Map v0.1**：

| Interface Pattern | 核心关系 | 典型机制 | 主要解决的问题 |
|---|---|---|---|
| **Training Interface** | 数据进入模型学习过程 | Dataset / Pretrain / Fine-tune | 模型长期学会什么 |
| **Knowledge Interface** | 数据作为外部可检索知识 | RAG / Knowledge Base / Vector Search | 模型运行时查什么知识 |
| **Fact Query Interface** | 模型读取当前结构化事实 | SQL / Query / Data API | 当前事实是什么 |
| **Tool / Action Interface** | 模型通过工具访问或操作企业系统 | API / MCP / Tool | 如何获取或改变企业状态 |
| **Semantic Interface** | 显式描述对象、关系、状态、规则 | Semantic Layer / Ontology | 数据在业务上意味着什么 |
| **Context Interface** | 按当前任务动态选择和组织信息 | Context Engineering / Context Compiler | 此时此任务应该给模型什么 |
| **Evaluation Interface** | 数据作为正确性与质量基线 | Eval Set / Benchmark / Ground Truth | 模型做得对不对 |
| **Feedback Interface** | 运行结果重新成为学习材料 | Trace / Outcome / Human Feedback | 系统如何持续改进 |

研究目标不是增加名词，而是验证：

- 哪些真的是不同关系；
- 哪些只是实现方式；
- 哪些处于不同生命周期；
- 哪些应该合并 / 拆分；
- 当前分类遗漏什么。

**预期产物：`Enterprise Data–Model Relationship Map v0.1`**。

### RQ-002-B / AQ-002-02｜Mechanism Boundaries

> **Dataset、Knowledge Base、SQL、API、Tool、Ontology、Context、Eval、Feedback 的边界是什么，又怎样组合？**

当前候选区分：

- Dataset：模型学习什么；
- Knowledge Base：模型运行时查什么知识；
- SQL / API：当前事实从哪里来；
- Tool：如何读取或改变企业状态；
- Ontology / Semantic Layer：事实在业务上意味着什么；
- Context Engineering：当前任务到底给模型什么；
- Eval：如何判断输出是否正确；
- Trace / Feedback：运行经验如何重新进入资产体系。

需要特别判断：

- Ontology 是“接口关系”还是“语义机制”？
- Context 是独立架构层，还是对多种资产的动态编译过程？
- Tool / API 属于 Data–Model 关系，还是更上位的 Capability / Action 关系？
- Knowledge、Fact、Semantic、Context 是否应该按运行时角色而不是产品形态区分？

**预期产物：`Data–Model Mechanism Boundary Table v0.1`**。

### RQ-002-C / AQ-002-03｜Traditional Data Platform → AI-ready Context Architecture

> **哪些仍属于传统数据治理 / 数据平台问题，哪些是 Model / Agent 成为新消费者后显著新增的 Context / Semantic / Evidence 问题？**

传统数据平台候选链路：

`Source → Integration → Governance → Warehouse / Lake → Data Service → Application`

当前 AI 时代候选扩展：

`Source → Governance → Semantic / Context / Evidence → AI-ready Asset → Model / Agent`

**Working Hypothesis H-RP002-02**：

> 原有 Data Service 之上，可能逐步增加面向智能主体的 Semantic / Context / Evidence 能力；但这不等于传统数据平台被替代，也不预设一定需要一个独立的“AI 数据平台”。

研究必须区分：

- **Inherited Capability**：传统数据治理仍然必须解决的数据质量、标准、集成、血缘、权限等能力；
- **Extended Capability**：为模型消费而增强的检索、结构化查询、AI-ready Asset 等能力；
- **AI-native / Newly Salient Capability**：Context Assembly、Semantic / World Representation、Evidence Packaging、Eval / Runtime Feedback 等因 Model / Agent 成为新消费者而显著上升的问题；
- **To Be Validated**：只是当前假设、尚无充分证据证明必须成为独立平台能力的部分。

**预期产物：`Traditional Data Platform → AI-ready Context Architecture v0.1`**。

### RQ-002-D / AQ-002-04｜AI Context Starting-State Pathways

> **企业在不同数字化 / 数据基础下，AI Context 应该沿什么路径建设？**

当前先保留三种典型起点作为待验证的路径假设，而不是直接给出标准答案：

#### Path A｜有业务系统，但没有统一大数据 / 数据平台

典型条件：业务事实已经存在于若干业务系统中，但缺少统一的数据汇聚、治理、语义和服务层。

需要研究：

- AI Context 是否应该围绕高价值业务任务，直接连接 System of Record / API / SQL / 文档，先构建任务级 Context，而不是先补齐一套完整大数据平台？
- 哪些最小公共能力必须先补：数据目录、权限、标识映射、数据质量、主数据、事件、Evidence / Lineage？
- 场景级 Context 如何避免重新制造新的数据烟囱和重复 ETL？
- 当场景增多到什么程度，才需要上升为共享 Data / Semantic / Context Foundation？

#### Path B｜已经有大数据 / 数据平台

典型条件：已有数据湖 / 仓、治理、指标、元数据、血缘、权限和数据服务，但主要消费者过去是报表、分析和应用系统。

需要研究：

- 哪些既有能力可以直接复用，哪些不能直接等同于 AI Context？
- 是否应该在现有 Data Service 之上增加 Semantic / Context / Evidence / Eval 能力，而不是重新建设第二套 AI 数据底座？
- 如何把历史批数据、实时事实、文档知识、业务语义和权限共同编译成任务上下文？
- 现有数据平台的元数据 / 语义层能否直接被 Agent 使用，还是需要新的机器可消费表达？

#### Path C｜业务系统本身都不完整或尚未建立

典型条件：缺少稳定 System of Record，业务对象、状态、事件和流程还没有被信息系统持续记录。

需要研究：

- 此时“先建数据平台再做 AI”是否成立，还是应该先把业务对象、事件、状态、规则和责任链数字化？
- 能否采用业务建模 / World Model / Ontology 牵引 Application + Data + AI 协同设计，而不是先复制传统“应用建完再汇数据”的路径？
- 哪些事实必须由业务系统 / 事务系统成为权威记录，不能让 LLM / Agent Context 代替 System of Record？
- 在绿地场景中，怎样避免为 AI 预建过重语义体系，仍以最小业务闭环形成真实数据与反馈？

**Working Hypothesis H-RP002-03**：

> AI Context 更可能是一组目标能力，而不是所有企业都按同一顺序建设的一套固定平台。企业的 System of Record 完整度、数据平台成熟度与业务数字化程度，可能决定不同的迁移路径；但不同路径是否最终收敛到相似的 Context / Semantic / Evidence 能力，仍需公开案例和工程实践验证。

状态：Hypothesis，不进入 JUDGMENTS / PRINCIPLES。

### Working Hypothesis H-RP002-04｜Business Reality → Dynamic Context → Action → Feedback Loop

三种起点虽然可能采取不同建设路径，但它们是否会逐步收敛到一条相似的**逻辑能力链**，值得单独验证。当前先记录如下候选闭环：

```text
业务事实
↓
业务对象与统一身份
↓
状态 / 事件 / 关系
↓
规则 / 知识 / 风险基线
↓
角色 / 任务 / 权限
↓
证据 / 历史 / 当前环境
↓
【动态上下文组装】
↓
模型 / Agent
↓
建议 / 行动
↓
人工确认 / 真实结果
↓
反馈更新
```

当前理解不是把它当成固定技术栈或强制建设顺序，而是把它视为一个**待验证的 Enterprise Context 逻辑闭环**：

- 上半段负责把企业现实转成可被机器引用的事实、对象、状态、关系、规则、权限和证据；
- `动态上下文组装` 负责根据当前任务把必要信息编译成 Model / Agent 可消费的 Context；
- Model / Agent 负责判断、建议或行动，但不是新的事实权威源；
- 人工确认与真实结果提供 Ground Truth / Outcome；
- 反馈更新使事实、知识、风险基线、规则、Eval 或后续 Context 有机会被修正。

与三条起点路径的关系当前暂定为：

- **Path A｜有业务系统无数据平台**：更可能从已有 System of Record / API / SQL / 文档抽取“业务事实”开始，逐步补对象统一、语义、证据和动态 Context；
- **Path B｜已有数据平台**：更可能复用治理后的数据、元数据、指标、血缘和权限，重点补业务对象 / 状态 / 事件表达、动态 Context、Evidence 与 Feedback；
- **Path C｜业务系统尚不完整**：更可能先建立业务对象、状态、事件和真实记录机制，使业务事实能够持续产生，再建设 Context 与 Agent 闭环。

需要重点验证三个问题：

1. 这条链中的哪些环节是企业 AI 的结构性需求，哪些只是当前工程阶段的实现形态？
2. 是否所有高价值 Agent 场景都需要完整经过这条链，还是应按任务复杂度裁剪？
3. `人工确认 / 真实结果 → 反馈更新` 是否足以形成可靠学习闭环，还是还需要 Eval、治理审批和版本化 Promotion 机制？

**状态：Hypothesis / Architecture Sketch，不进入 JUDGMENTS / PRINCIPLES。**

**预期产物：`AI Context Starting-State Pathway Matrix v0.1`**，至少比较：

- 企业起点；
- 可复用资产；
- 当前缺口；
- 首个建设动作；
- 最小公共能力；
- 何时需要共享平台化；
- 主要风险；
- 目标 Context 能力；
- 各路径从哪一段进入 H-RP002-04 的逻辑闭环，以及哪些环节可以复用 / 跳过 / 延后。

### AQ-002-05｜历史数据与实时业务状态如何同时进入 Agent？

这一问题暂不作为第一轮主研究对象，但保留为后续架构深化：

- Historical Knowledge；
- Operational State；
- Event / Change；
- Rule / Policy；
- Evidence / Freshness。

需要判断它们在 Enterprise Context 中如何组合，而不是全部塞入 RAG。

---

## 2.3 Evidence Plan｜下一步怎么研究，而不是直接给答案

下一轮不先继续论文队列，也不先画完整平台架构。围绕 RQ-002-A / B / C 定向找证据；在机制边界基本清楚后，用 RQ-002-D 检查三种不同企业起点的建设路径，并验证 H-RP002-04 是否真的是不同路径可以共同收敛的逻辑闭环。

### 优先证据类型

- **[Product Fact]**：数据平台 / Lakehouse / Data Cloud / AI Platform 的公开架构与产品文档；
- **[Open-source Implementation]**：RAG、structured query、semantic / knowledge graph、context、eval 的真实工程实现；
- **[Theory]**：知识表示、语义、信息整合、Context、数据与推理关系等理论 / 论文；
- **[Industry Case]**：公开企业实践，看机制是否进入实际业务闭环；特别关注不同数字化成熟度企业的路径差异；
- **[Analyst View] / [Policy / Standard]**：判断产业共性、标准和治理要求；
- **[Counter Evidence]**：简单任务无需复杂语义层、复杂本体仍不能解决模型错误的反例，以及“先补完整数据平台”或“完全绕过数据平台”失败的路径反例。

### 研究顺序

```text
Research Question
        ↓
Evidence Search
        ↓
Evidence Identity
Theory / Product Fact / Claim / Case / Open-source / Counter Evidence
        ↓
Mechanism Synthesis
        ↓
Architecture Hypothesis
        ↓
后续才进入 Engineering / Validation
```

不要先画一个完整答案，再只寻找支持已有判断的材料。

---

## 2.4 Engineering Questions｜第二阶段，不抢跑

当 Relationship Map、Boundary Table 与 Starting-State Pathway 更清楚以后，再决定哪些工程问题值得做 Demo / Benchmark：

- **EQ-002-01**：同一任务分别使用 RAG、SQL/API、Semantic Model / Ontology、组合 Context 时，效果和成本如何比较？
- **EQ-002-02**：如何把既有治理后的数据转换成 Dataset、Knowledge Asset、Eval Set、Semantic Asset 等不同 AI-ready Asset？
- **EQ-002-03**：Context 如何携带 Source、Lineage、Freshness、Permission、Evidence，让模型结果可追溯？
- **EQ-002-04**：实时业务状态怎样进入 Agent Runtime，而不是只依赖历史知识？
- **EQ-002-05**：Semantic Model / Ontology 应由专家预建、AI 自动发现还是 Human-governed 动态生成？怎样校验？
- **EQ-002-06**：三种起点下，怎样定义“最小可行 Context Foundation”，既不重复造数据平台，又不把场景能力做成新烟囱？
- **EQ-002-07**：如何把 H-RP002-04 的“事实 → 对象 / 状态 / 规则 / 权限 / 证据 → 动态 Context → Agent → Outcome → Feedback”做成可运行、可观测、可版本化的最小闭环？

---

## 2.5 Validation Questions｜第二阶段

- **VQ-002-01**：能否用公开 / 合成业务任务对比 `RAG only`、`RAG + structured facts`、`RAG + semantic/world context`？
- **VQ-002-02**：除了回答准确率，还应比较哪些指标：Consistency、Freshness、Traceability、Action Success、Maintenance Cost？
- **VQ-002-03**：公开产品和案例中，哪些已将 Data Service 扩展为 Semantic / Context / Evidence 能力？哪些只是 Product Claim？
- **VQ-002-04**：有没有公开反例说明更强显式语义层在某些任务中成本高于收益？
- **VQ-002-05**：能否找到三类不同起点的公开案例，比较其首个建设动作、复用资产、平台化时机和最终上下文能力，验证“三条路径”是否真实存在且具有解释力？
- **VQ-002-06**：不同成熟度企业是否都能找到“事实 → Context → Agent → Outcome → Feedback”的可观察闭环？哪些环节缺失时会导致模型判断不可验证或无法形成持续改进？

---

## 2.6 当前成果定义｜这轮研究最终要留下什么

RP-002 当前一轮不以“读完多少论文”结束，而暂定形成六类成果：

1. **Relationship Map**：Data 与 Model / Agent 到底存在多少种结构性关系；
2. **Mechanism Boundary Table**：Dataset / KB / SQL / API / Tool / Ontology / Context / Eval / Feedback 分别解决什么、怎样组合；
3. **Architecture Evolution Map**：传统数据平台哪些能力延续，哪些因 Model / Agent 成为新消费者而需要增强 / 新增；
4. **Starting-State Pathway Matrix**：有业务系统无数据平台、已有数据平台、业务系统尚不完整三种起点下，AI Context 的复用资产、首个动作、公共能力与迁移路径如何不同；
5. **Context Assembly Loop Sketch**：验证 H-RP002-04 这条“业务现实 → 动态 Context → Agent → Outcome → Feedback”逻辑链是否成立，以及三条路径从哪里进入这条链；
6. **Principle Decision**：研究后哪些 Working Hypothesis 被支持、修改或否定，是否足以进入 `PRINCIPLES.md` 成为 Candidate Architecture Principle。

候选 Principle 现在不预写结论。只有 Theory + Public Industry Evidence 和必要的工程 / 反例验证足以支撑时，才收敛。

---

## 2.7 与已有认知的关系

### Related Evolution

- `EV-007`：从“本体是企业 AI 基础”到“静态本体是语义鸿沟的阶段性桥梁”。

### Related Principle

- `AP-002`：显式业务语义强度应匹配任务复杂度，不默认所有 Agent 都需要完整 Ontology。

### Derived / Absorbed Question

原来的“AI 需要多强显式 Enterprise Context / Semantic Model / Ontology？”不再单独作为母问题，而并入 RP-002。

这避免把 Ontology 本身误当成问题入口。更上位的问题是：

> **企业真实世界怎样通过数据、知识、语义、上下文、工具、评价和反馈机制进入 Model / Agent。**

本次新增的“三类企业起点”也不单独升级为新的 RP，而作为 RP-002 的路径型 Architecture Question：它研究的不是第三套问题，而是**相同 Data–Model / Context 问题在不同既有信息化基础下怎样落地**。

H-RP002-04 进一步把“三条起点路径”与一个候选目标闭环连接起来：**路径可能不同，但长期需要验证它们是否都在解决“如何把真实业务世界稳定编译成可执行 Context，并用真实结果持续校正”这一共同问题。**

---

## 2.8 Resume Point｜下次继续研究的位置

下一次恢复 RP-002 时，从这里开始：

> 不先继续论文，也不直接给出“AI 数据平台标准答案”。
>
> 先围绕三个机制问题找公开证据：
>
> **RQ-002-A：业界真实存在几种 Data → Model / Agent 关系？**  
> **RQ-002-B：Dataset / KB / SQL / API / Tool / Ontology / Context / Eval / Feedback 的机制边界与组合关系是什么？**  
> **RQ-002-C：哪些是传统数据平台能力，哪些是 AI 时代新增 / 显著上升的 Semantic / Context / Evidence 问题？**
>
> 在 A / B / C 基本清楚后，用 **RQ-002-D** 检查三类不同企业起点：①有业务系统无数据平台；②已有数据平台；③业务系统尚不完整。比较可复用资产、首个建设动作、最小公共能力、平台化时机和风险。
>
> 同时把 **H-RP002-04** 当成待验证的目标闭环，而不是既定答案：检查三条路径是否都能映射到“业务事实 → 对象 / 状态 / 规则 / 权限 / 证据 → 动态 Context → Model / Agent → 行动 → 真实结果 → 反馈更新”，以及哪些环节可以按任务复杂度裁剪。
>
> 第一轮形成 Relationship Map、Boundary Table、Architecture Evolution Map、Starting-State Pathway Matrix、Context Assembly Loop Sketch v0.1；再判断需要哪些理论深化、工程验证和 Candidate Principle。

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
Agent 有能力调用工具以后，Business Validity、Capability、Authority、Human Control 与 Accountability 应如何组合？

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

一个时期原则上只保留一个主要 Active Problem；其他高价值问题允许标记 `Candidate` 或 `Paused`。

**论文编号不能充当 Active Problem。**例如“下一步读 P-002”不是研究问题；必须先写清“P-002 被用来解释哪个 RP / CQ / AQ”。

切换 Active Problem 前只问两件事：

1. 新问题是否比当前问题更直接影响正在形成的架构判断？
2. 当前问题是否已经达到一个可暂停的明确停止点？

当前答案：RP-001 已达到可暂停点；RP-002 因直接影响企业 AI 数据 / Context 架构判断，成为当前 Active Problem。

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