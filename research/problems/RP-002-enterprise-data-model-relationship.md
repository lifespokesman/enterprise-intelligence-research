# RP-002｜Enterprise Data–Model Relationship

Status: Active  
Updated: 2026-09-17  
Primary Track: E2 Enterprise Context / World Model  
Related: Q3 Coordination / Q5 Organizational Learning / E4 Feedback-Evaluation-Evolution / E3 Agent-callable Capability

> 核心母问题：**企业已有的数据资产，与 Model / Agent 到底应该建立什么关系？企业真实世界究竟通过哪些机制进入模型？**

本文件保存 RP-002 的当前研究状态。它不是结论页，而是后续恢复研究时的工作入口。

---

## 1. Trigger｜抽象后的现象

很多企业已经建设数据平台、数据治理、数据服务和知识体系，但这些资产并不会自动转化为 Model / Agent 能够可靠理解、调用、验证和持续使用的企业上下文。

因此，“数据治理服务 AI”不能只理解为把更多数据接给模型。真正需要研究的是：

> **企业数据在什么情况下是训练材料、知识、当前事实、业务语义、任务上下文、评价依据或运行反馈？不同关系需要不同的架构机制。**

进一步研究 Ontology / Semantic Layer 后，又出现了两个继续向下的问题：

1. **企业真实世界不仅需要进入模型，还可能被 Agent 改变。能够描述世界，并不等于已经具备安全、稳定地改变世界的机制。**
2. **即使 Semantic / Operational / Evolution Model 有价值，如果仍要求业务人员从零人工建模，企业级生产使用门槛可能仍然过高。**

因此 RP-002 当前逐渐形成三个相互关联的方向：

```text
World → Model / Agent
企业世界如何被 AI 理解

Model / Agent → World
AI 如何通过受治理的业务动作改变企业世界

Semantic Sources / Runtime Evidence → World Model
企业世界模型如何被低门槛地构建与持续维护
```

对应已登记的子问题：

- [`RP-002-01｜Enterprise World Model Conflict & Evolution`](RP-002-01-world-model-conflict-evolution.md)
- [`RP-002-02｜Business Action Layer：企业 AI 如何安全地改变企业世界`](RP-002-02-business-action-layer.md)
- [`RP-002-03｜Semantic-to-Executable World Model`](RP-002-03-semantic-to-executable-world-model.md)

公开仓只保留抽象问题，不记录私人项目来源、客户身份、系统细节或非公开证据。

---

## 2. Problem Structure｜问题纵向结构

本问题按三类问题逐层推进：

`Cognitive Question → Architecture Question → Engineering Question → Evidence / Validation → Principle`

三类问题不是并列分类，而是一条纵向推导链：

- **Cognitive**：先搞清楚现实机制和概念边界；
- **Architecture**：如果这个认知成立，企业 AI 架构应该怎样组织；
- **Engineering**：这些架构关系如何实现、比较和验证。

工程结果反过来修正架构判断和认知判断。

---

## 3. Cognitive Questions｜认知问题

### CQ-002-01｜企业历史数据对模型究竟可以扮演哪些不同角色？

当前候选角色，不作为最终分类：

- 学习材料：Dataset / Training / Fine-tuning；
- 外部知识：Knowledge Base / RAG；
- 当前事实：SQL / API / Operational Data；
- 业务语义：Semantic Model / Ontology；
- 当前任务上下文：Context Engineering；
- 评价依据：Eval Set / Benchmark；
- 运行反馈：Trace / Outcome / Feedback。

需要验证：这些到底是同一层“接口类型”，还是混合了资产角色、访问机制和生命周期阶段。

### CQ-002-02｜为什么传统数据治理并不天然等于 AI-ready？

需要研究以下差异是否成立：

- Data Quality ≠ Context Quality；
- Schema ≠ Business Semantics；
- Data Integration ≠ Model Understanding；
- Data Service ≠ Task-specific Context；
- Data Availability ≠ Context Usability。

### CQ-002-03｜模型真正需要的是“更多数据”，还是“可正确理解和使用企业现实的机制”？

当前假设：随着任务复杂度提高，问题可能从“访问数据”逐渐转向“理解对象、状态、关系、事件、规则、权限、证据与当前任务”。

该假设需要理论、产品与工程证据共同验证。

### CQ-002-06｜企业世界模型只需要描述“是什么”，还是还需要表达“允许怎样被改变”？

当前候选区分：

```text
Semantic Ontology
Object / Relation / State / Rule
企业世界是什么

Operational Layer / Operational Ontology（研究概念）
Action / State Transition / Permission / Effect
企业世界允许怎样被改变
```

这里暂不预设 `Operational Ontology` 是业界标准术语，也不预设 Action 必须直接属于 Ontology 产品。详细问题见 `RP-002-02`。

### CQ-002-07｜企业世界模型是否必须主要依赖人工显式建模？

新的认知不是“不再需要结构化模型”，而是：

> **结构化模型可能仍是生产运行的必要表示，但人工从零建模未必应该继续作为主要建设入口。**

需要验证：自然语言、制度、Schema、API、Workflow、权限、Trace 等既有企业语义，是否足以让 AI 自动发现并生成可用的候选 `Object / Relation / State / Rule / Action / Permission / Effect`，并把人的工作集中到冲突、规范性规则、授权和高风险变更审核。

详细问题见 `RP-002-03`。

---

## 4. Architecture Questions｜当前第一轮重点

当前下一轮主研究仍先聚焦前三个架构问题，不因为新增子问题而打断当前 Active 路线。

### AQ-002-01｜业界真实存在几种 Data → Model / Agent 关系？

研究目标：形成 **Data–Model Relationship Map v0.1**。

候选机制包括但不限于：

- Dataset / Training；
- Knowledge Base / RAG；
- SQL / Data Query；
- API / Tool / MCP；
- Semantic Layer / Ontology；
- Context Engineering；
- Eval / Benchmark；
- Runtime Feedback / Trace。

研究时重点区分：

1. 这是“数据资产角色”还是“模型访问方式”？
2. 是训练时、运行时还是评测/反馈阶段？
3. 模型获得的是知识、事实、语义、能力还是评价信号？

### AQ-002-02｜Dataset、Knowledge Base、SQL、API、Ontology、Context、Eval、Feedback 的边界是什么？

研究目标：形成 **Mechanism Boundary Table v0.1**。

至少回答：

- 每种机制解决什么问题；
- 输入 / 输出是什么；
- 运行时机是什么；
- 是否改变模型参数；
- 是否提供当前事实；
- 是否提供显式业务语义；
- 是否负责动态上下文组装；
- 是否用于评价或反馈；
- 与其他机制如何组合；
- Tool / API 属于 Data–Model 关系，还是更上位的 Capability / Action 关系；
- 哪些常见架构图把不同层级混在了一起。

### AQ-002-03｜哪些仍是传统数据治理问题，哪些是 AI 时代新增或显著放大的问题？

研究目标：形成 **Traditional Data Platform → AI Context / Semantic / Evidence Architecture v0.1**。

重点验证，而不是预设：

- 哪些能力可以直接继承 Data Integration / Quality / Metadata / Lineage / Data Service；
- Model / Agent 成为新的数据消费者后，是否新增或显著强化 Semantic、Context、Evidence、Eval、Feedback 等能力；
- “AI-ready Data Foundation”是否只是传统治理升级，还是出现了新的架构层；
- 新层与原数据平台是替代、叠加还是能力重构关系。

### AQ-002-06｜Business Action Layer 是否是 Semantic Layer 与 Agent Execution 之间需要独立存在的架构层？

当前工作问题：

> **Object、Rule、Action、Function、Workflow、API、MCP 与 Agent 应是什么关系？**

当前工作模型：

```text
Business World
Object / Relation / State / Rule
        ↓
Business Action Contract
        ↓
Business Action Runtime
        ↓
Function / Workflow / Adapter
        ↓
API / Event / RPA / DB / Human Task
        ↓
Enterprise Systems
```

Agent 侧通过 MCP / API / SDK 等暴露机制调用 Business Action，而不是把 MCP Tool 本身等同于 Business Action。

该问题已拆入 `RP-002-02`，本文件只保留索引和与 RP-002 主线的关系。

### AQ-002-07｜Semantic-to-Executable World Model 是否可以成为企业世界模型的主要建设机制？

候选结构：

```text
Enterprise Semantic Sources
Natural Language / Documents / Schema / API / Workflow / Trace
                         ↓
               AI World Model Compiler
                         ↓
      Evidence-backed Candidate World Model
                         ↓
          Conflict / Exception Review
                         ↓
            Production World Model
```

核心不是用自然语言替代模型，而是形成：

> **Semantic-first, Model-backed：Semantic 作为主要的人机建设入口，Structured World Model 作为生产运行表示。**

该问题已拆入 `RP-002-03`。

---

## 5. Engineering Questions｜架构收敛后再启动

当前先登记，不立即全部研究。

- **EQ-002-01**：同一任务下，RAG-only、Structured Facts、Semantic / Ontology Context 等方案如何比较？
- **EQ-002-02**：传统治理数据如何转换为 Training / Knowledge / Eval / Semantic 等不同 AI 资产？
- **EQ-002-03**：Source、Lineage、Freshness、Permission、Evidence 如何随 Context 一起交给 Agent？
- **EQ-002-04**：实时业务状态怎样进入 Agent Runtime，而不是只依赖历史知识？
- **EQ-002-05**：Ontology / Semantic Model 应由专家建设、AI 自动发现还是运行时动态生成？如何校验？
- **EQ-002-06**：Direct Tool / API 与 Business Action Runtime 两种执行模式，在 Prompt 复杂度、接口变更影响、权限治理、多 Agent 复用和 Trace 可解释性上有什么差异？
- **EQ-002-07**：从 SOP + Schema + API + Permission + Trace 自动生成 Semantic / Operational 候选模型，与人工建模相比在成本、准确率、治理风险和维护成本上有什么差异？

---

## 6. Evidence Plan｜下一步怎么研究

问题驱动不等于“问题提出后直接由 AI 给答案”。每个问题应选择合适的证据类型。

### 对 AQ-002-01 / AQ-002-02

优先证据：

- 公开云 / 数据平台 / AI 平台架构文档；
- 开源框架和参考实现；
- Product Fact；
- 技术标准 / 协议；
- 必要时补学术定义和经典机制。

这些问题首先是工程机制识别，不必先找管理学论文。

### 对 CQ-002-02 / CQ-002-03

优先证据：

- Knowledge Representation / Semantic / Information Integration / Context Engineering 等理论或论文；
- 能说明“数据存在”与“模型可正确使用”之间差异的研究；
- Counter Evidence：强模型在无显式语义层条件下是否也能稳定完成任务。

### 对 AQ-002-03 与 Engineering Questions

优先证据：

- 公开企业案例；
- 产品架构演进；
- 开源 Demo / Benchmark；
- Synthetic comparison；
- Counter Evidence。

### 对 AQ-002-06 / EQ-002-06

优先证据：

- Palantir Ontology Actions / Functions 等 Product Fact；
- Salesforce / ServiceNow / SAP / Microsoft 等企业 Agent 与业务动作设计；
- DDD Application Service / Command、CQRS、BPM / Workflow、Capability API 等传统架构模式；
- MCP / Tool-use 协议边界；
- Durable Execution、Policy Engine、IAM、Approval、Audit 等 Runtime 实现；
- 不需要独立 Action Layer 的反例。

### 对 AQ-002-07 / EQ-002-07

优先证据：

- Ontology Learning / Ontology Evolution / Schema Matching / Semantic Parsing / Process Mining 等理论与方法；
- 企业语义层、Knowledge Graph、Process Intelligence 产品中的 AI-assisted modeling；
- 从 Schema / API / Code / Log 自动发现领域模型、流程或工具语义的开源实现；
- 自动建模在对象边界、权限、规范性规则和高风险 Action 上的反例；
- Manual Modeling 与 AI-assisted Compilation 的小规模对照验证。

证据身份继续区分 `[Theory] / [Product Fact] / [Product Claim] / [Industry Case] / [Analyst View] / [Policy / Standard] / [Counter Evidence]`。

---

## 7. Current Hypotheses｜当前只保留为假设

### H-RP002-01

> **Data Availability ≠ Context Usability.**

企业已经拥有并治理的数据，不代表当前 Model / Agent 可以在正确时间、正确语义、正确权限和正确证据条件下使用它。

### H-RP002-02

> 传统 Data Service 之上，可能逐步出现面向 Model / Agent 的 Semantic / Context / Evidence 能力，但这些能力究竟是新层、原平台升级还是运行时机制，需要进一步验证。

### H-RP002-03

> “数据服务 AI”不是单一接口关系，而是 Training、Knowledge、Fact、Semantic、Context、Evaluation、Feedback 等多种关系的组合。

### H-RP002-06｜Business Action as Governed Mutation Contract

> **企业 AI 要从“理解企业世界”进入“运行企业世界”，可能需要把具有业务状态改变、组织责任或外部副作用的操作抽象为受治理的 Business Action；Action Contract 描述允许发生什么，Action Runtime 负责怎样安全可靠地执行，MCP / API / SDK 负责把能力暴露给调用者。**

详细定义、反例与验证方案见 [`RP-002-02-business-action-layer.md`](RP-002-02-business-action-layer.md)。

### H-RP002-07｜Semantic-first World Model Compilation

> **企业级世界模型的主要生产方式可能从“人工显式建模”逐渐转向“AI 从自然语言、企业系统和运行证据中自动编译候选结构，人主要处理冲突、授权、高风险规则和最终责任确认”。**

这里不是用自然语言替代结构化模型，而是区分：

```text
Human-facing
Semantic Interface

      ↓ compile

Machine-facing
Structured / Executable World Model
```

详细定义、自动化边界与验证方案见 [`RP-002-03-semantic-to-executable-world-model.md`](RP-002-03-semantic-to-executable-world-model.md)。

以上均不升级为 Architecture Principle。

---

## 8. Planned Outputs｜第一轮预期成果

第一轮主研究仍只追求三个成果：

1. **Data–Model Relationship Map v0.1**  
   说明企业数据与 Model / Agent 存在哪些不同关系。

2. **Mechanism Boundary Table v0.1**  
   说明 Dataset / Knowledge Base / SQL / API / Ontology / Context / Eval / Feedback 各自解决什么问题、边界在哪里、如何组合。

3. **Traditional Data → AI Architecture Evolution v0.1**  
   说明哪些能力继承传统数据治理，哪些是 AI 时代新增或显著增强的 Semantic / Context / Evidence / Eval / Feedback 能力。

新增但不抢占当前 Active 顺序的后续产物：

4. **Business Action Architecture v0.1**  
   说明 Semantic World、Action Contract、Action Runtime、Function / Workflow、MCP / API 与 Agent 的边界和组合关系。

5. **Semantic-to-Executable World Model Compiler v0.1**  
   说明企业既有语义 / 系统 / 运行证据如何生成 Evidence-backed Candidate World Model，以及人工 Review / Governance 应保留在哪些边界。

这些成果完成后，再判断：

- 是否已经形成清晰 Engineering Hypothesis；
- 是否值得启动小规模工程验证；
- 是否足以沉淀 Candidate Architecture Principle；
- 还是需要继续补理论 / 产品 / 反例。

---

## 9. Next Action｜恢复研究时从这里开始

**RP-002 当前主线仍先研究 AQ-002-01：业界真实存在几种 Data → Model / Agent 关系。**

执行顺序：

1. 搜集公开产品架构、开源实现和必要理论定义；
2. 不预设现有候选分类一定正确；
3. 区分“资产角色 / 接口机制 / 生命周期阶段”；
4. 形成 Data–Model Relationship Map v0.1；
5. 再进入 AQ-002-02 做边界表；
6. 最后处理 AQ-002-03 的传统数据架构与 AI 架构演进关系。

`RP-002-02 Business Action Layer` 与 `RP-002-03 Semantic-to-Executable World Model` 都作为已经注册的派生研究方向保存，不要求当前立即展开。

真正继续 `RP-002-03` 时，先做一个最小验证：

> **选一个真实小流程，比较“人工建模”与“AI 从 SOP + Schema + API + Permission + Trace 编译候选 Semantic / Operational Model”两种方式，验证是否真的降低建模成本，同时保持关键规则、权限与高风险动作可治理。**

当前时间不足时，停在这里即可。后续新会话只需要读取 `PROJECT_CONTEXT.md`、`NOW.md`、`research/research-questions.md`、本文件及相关子问题文件即可继续。

---

## 10. Principle Gate｜什么时候允许进入 PRINCIPLES.md

只有满足以下至少一部分条件后，才考虑把 RP-002 的结论升级为 Candidate Principle：

- 不同公开产品 / 实现之间出现相对稳定的共同机制；
- 有理论解释说明为什么这种机制必要；
- 有案例、Benchmark 或小实验支持其工程价值；
- 已明确替代路线和不适用边界；
- 研究者理解并明确接受该判断。

在此之前，所有漂亮的架构图都只属于 Working Model / Engineering Hypothesis。
