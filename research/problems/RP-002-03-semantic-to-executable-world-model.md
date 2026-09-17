# RP-002-03｜Semantic-to-Executable World Model

Status: Open / Exploratory  
Created: 2026-09-17  
Parent: RP-002 Enterprise Data–Model Relationship / Enterprise World Model  
Cross-link: RP-002-01 World Model Conflict & Evolution / RP-002-02 Business Action Layer / RP-004 Authority & Control  
Primary Track: E2 Enterprise Context / World Model  
Related: E3 Agent-callable Capability / E4 Feedback-Evaluation-Evolution / G2 Authority / G4 Traceability

> 核心子问题：**企业世界模型能否主要通过自然语言、制度文档、数据结构、API、流程和真实运行轨迹等既有业务语义，由 AI 自动发现并编译为可执行、可治理、可演化的结构化模型，而不是要求业务人员从零进行人工本体建模？**

本文件记录一次关于企业世界模型“建设入口”的认知变化。当前只保留为 Working Hypothesis，不进入 `JUDGMENTS.md` / `PRINCIPLES.md`。

---

## 1. Trigger｜问题来源

前序研究逐渐形成三个候选组成部分：

```text
Semantic Model
世界是什么

Operational Model
世界允许怎样变化

Evolution Model
世界模型怎样被现实挑战并演化
```

如果这三个部分都要求业务专家、本体专家或开发者手工完成对象、关系、状态、规则、动作、权限、状态迁移和演化规则建模，那么企业级生产使用门槛可能仍然过高。

这暴露出一个新的问题：

> **AI 时代是否仍然应该把“建模工作台”作为企业世界模型的主要入口？**

企业其实已经以大量既有形式表达业务：自然语言、制度 / SOP / 规范、表单与页面、数据库 Schema、API / 服务定义、BPM / Workflow、代码、权限表、历史业务数据、Runtime Trace / Event Log，以及人员真实操作与反馈。

因此问题从：

> “怎样让人更方便地建设 Ontology？”

进一步转变成：

> **“怎样让 AI 从企业已经存在的业务语义和运行证据中，持续编译出机器可运行的企业世界模型？”**

---

## 2. Cognition Change｜认知变化

### Before｜人工建模作为主要入口

```text
业务专家 / 本体专家
        ↓
Ontology Workbench
        ↓
Object / Relation / Rule / Action
        ↓
Agent 使用
```

这一模式的隐含前提是：企业需要先学习并掌握一套显式建模方法，再把现实世界重新表达给 AI。

其风险包括：初始建设成本高、业务人员需要学习建模语言、模型容易滞后于业务变化、大量已有业务知识需要重新人工录入，以及世界模型规模扩大后的持续维护成本。

### Now｜Semantic-first, Model-backed

当前更值得验证的路线是：

> **不要取消结构化世界模型，而是取消“人工从零建模”作为主要入口。**

候选模式：

```text
Natural Language / Documents / Systems / Data / API / Workflow / Trace
                              ↓
                    Semantic Understanding
                              ↓
                  AI World Model Compiler
                              ↓
          Candidate Structured World Model
                              ↓
             Evidence / Confidence / Conflict
                              ↓
              Review only when necessary
                              ↓
                  Production World Model
```

即：

> **Semantic 是主要交互与建设入口，Structured Model 是机器运行表示。**

---

## 3. Core Question｜核心研究问题

> **企业能否让业务人员主要通过已有业务语义、制度、系统和真实运行来表达业务，由 AI 自动完成结构发现、模型生成、证据绑定和增量维护，只把冲突、低置信度、高风险权限与关键变更交给人工确认？**

进一步问题：

1. 哪些世界模型结构可以从语义中可靠提取？
2. 哪些必须结合系统事实、权限配置和运行轨迹验证？
3. 哪些属于规范性授权，不能由模型仅凭语义自行决定？
4. AI 生成的候选模型如何附带 Evidence、Confidence 和 Provenance？
5. 如何把持续业务变化转化为 Model Diff / Change Proposal，而不是定期人工重建？
6. 最终产品应更像 Ontology Workbench，还是 World Model Compiler + Exception Review Workbench？

---

## 4. Working Hypothesis v0.1｜Semantic-to-Executable Compilation

### H-RP002-07｜Semantic-first World Model Compilation

> **企业级世界模型的主要生产方式可能从“人工显式建模”逐渐转向“AI 从自然语言、企业系统和运行证据中自动编译候选结构，人主要处理冲突、授权、高风险规则和最终责任确认”。**

候选架构：

```text
              Semantic Interface
      人主要表达业务事实、规则和目标
                    │
                    ▼
          AI World Model Compiler
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Semantic Model Operational Model Evolution Model
 世界是什么       世界怎样变化      模型怎样演化
      │             │             │
      └─────────────┼─────────────┘
                    ▼
          Executable World Model
                    │
                    ▼
        Agent Context / Action Runtime
```

当前状态：Hypothesis，不升级为 Architecture Principle。

---

## 5. 三类目标模型如何自动生成｜Candidate Compilation Targets

### 5.1 Semantic Model｜世界是什么

候选结构：`Object / Relation / Attribute / State / Event / Rule`。

潜在语义来源包括业务术语与制度、数据库 Schema / 元数据、API Schema、页面 / 表单、业务文档、历史数据和实体共现、Process / Event Log。

初步判断：这部分 AI 自动发现潜力较高，但仍需解决对象边界、同义词、跨系统身份统一和事实冲突。

### 5.2 Operational Model｜世界允许怎样变化

候选结构：`Action / State Transition / Precondition / Permission / Effect / Risk / Responsibility / Runtime Binding`。

AI 可以从 SOP、UI 操作、API、流程、权限表和历史调用日志中发现候选 Action，例如 `ApproveTask / AssignTask / ReturnTask / CloseTask / ChangePlan`。

但生产化时不能只靠语言模型猜测谁真正有权执行、哪个阈值有效、是否必须人工审批、是否允许自动执行、失败后能否补偿，以及谁承担业务责任。

因此候选链路为：

```text
AI Discover / Draft
        ↓
System / Policy Verification
        ↓
Risk-based Human Confirmation
        ↓
Production Action Contract
```

### 5.3 Evolution Model｜模型怎样演化

候选结构：

```text
Expected World
      ×
Observed World
      ↓
Conflict Detection
      ↓
Evidence Collection
      ↓
Model Change Proposal
      ↓
Impact Analysis / Simulation
      ↓
Approval / Auto-apply by Risk
      ↓
Versioned World Model
```

AI 很适合承担偏差发现、冲突聚类、证据汇总、候选结构提出、Model Diff 生成和影响范围分析。

但“发现现实与模型不一致”不等于“自动修改正式业务真相”，具体裁决机制继续归 `RP-002-01` 研究。

---

## 6. 关键边界｜不是“自然语言直接替代结构化模型”

本问题必须避免一种过度推论：

> 大模型理解自然语言，因此企业不再需要 Ontology / Schema / State / Action 等结构化模型。

当前假设恰好相反：

```text
Human-facing Interface
Natural Language / Semantic Interaction

              ↓ compile

Machine-facing Representation
Object / Relation / State / Rule / Action / Policy / Effect
```

即：

> **自然语言可以成为建模入口，但稳定生产运行仍需要可验证、可版本化、可治理的结构表示。**

原因包括权限必须可验证、状态迁移需要确定边界、高风险动作不能依赖每次自由解释、审计需要稳定语义、多 Agent / 多应用需要共享契约，以及模型升级后仍需保持业务规则连续性。

因此当前候选原则不是 `No Model`，而是：

> **Semantic-first, Model-backed.**

---

## 7. 人的角色变化｜Model Builder → Reviewer / Governor

如果假设成立，人的工作不再主要是从零画对象、定义每条关系、填写全部字段、手工登记每个 Action 并持续同步所有变化，而逐渐变成：确认关键业务语义、处理冲突、确认低置信度候选、批准规范性规则、确认权限 / 责任，以及评估高风险 Model Change。

即：

> **人从 Model Builder 逐渐转向 Model Reviewer / Business Governor。**

这不是取消人的责任，而是把人工集中在 AI 最不应该自行决定的地方。

---

## 8. Automation Boundary｜什么可以自动，什么必须治理

| 知识 / 模型内容 | AI 自动化潜力 | 主要治理要求 |
|---|---:|---|
| 术语 / 对象 / 属性候选 | 高 | 去重、实体边界、证据来源 |
| 关系 / 状态 / 流程候选 | 中高 | 跨系统一致性、运行证据 |
| 描述性运行模式 | 高 | 防止把异常 / 违规当标准流程 |
| Action 候选 | 中高 | 状态、副作用、接口验证 |
| 规范性业务规则 | 中 | 权威制度 / 责任主体确认 |
| Permission / Authority | 低到中 | 必须与 IAM / Policy / 授权事实校验 |
| 高风险 Action 自动执行权 | 低 | 审批、责任、不可逆性控制 |
| Model Change Proposal | 高 | Evidence / Impact / Version |
| 正式模型自动变更 | 取决于风险 | 分级审批 / 回滚 / 审计 |

该表只是工作假设，需要通过产品、标准和工程验证继续修正。

---

## 9. Product Hypothesis｜从 Ontology Workbench 到 World Model Compiler

传统产品形态更像：

```text
Ontology Workbench
→ 人创建对象 / 关系 / 规则
```

AI-native 产品形态可能更像：

```text
Enterprise Semantic Sources
        ↓
Discovery / Extraction
        ↓
World Model Compiler
        ↓
Evidence-backed Candidate Model
        ↓
Conflict / Exception Review Workbench
        ↓
Versioned Executable World Model
```

因此真正需要降低的可能不是“Ontology 编辑器操作步骤”，而是：

> **企业世界数字化表达的门槛。**

候选产品定位：`Enterprise World Model Compiler / Enterprise Semantic Compiler`。

当前只是 Product / Architecture Hypothesis，不预设该术语必须成为最终产品名。

---

## 10. 与三个子模型的关系｜World Representation / Operation / Evolution

当前可以把 RP-002 下已经出现的研究方向暂时组织成：

```text
Enterprise World Model
│
├─ World Representation
│  Semantic Model
│  世界如何被描述
│
├─ World Operation
│  Operational Model / Business Action
│  世界如何被改变
│
└─ World Evolution
   Conflict / Evidence / Version
   世界模型如何被现实持续修正
```

`RP-002-03` 研究的不是第四种世界模型，而是：

> **上述三类模型应如何被低门槛地生产、维护与更新。**

也就是说，它是一条横向的 **Construction / Compilation Mechanism**。

---

## 11. Relation to RP-002-01｜与世界模型演化的关系

`RP-002-01` 已经指出：人工本体、专家经验、制度规则与 AI 判断都不是企业世界本身，而是对世界的不同表达，需要 Evidence + Conflict + Governance 判断什么进入正式模型。

本问题进一步推进：

> **既然人工初始模型也不是天然真相，就不应默认“人先完整建模，AI 后续补洞”是唯一建设路线。AI 可以从多种证据源直接生成候选初始模型和持续增量，但正式升级仍受 RP-002-01 的证据与裁决机制约束。**

因此：

```text
RP-002-03
负责 Candidate Model Generation

RP-002-01
负责 Conflict / Evidence / Model Change Governance
```

---

## 12. Relation to RP-002-02｜与 Business Action Layer 的关系

`RP-002-02` 研究企业允许发生哪些受治理的业务状态变化，以及这些 Action 怎样与 Runtime / API / Workflow 解耦。

本问题补充：

> **Action Contract 本身是否也可以从 SOP、API、UI、权限表、状态变化和 Runtime Trace 中被 AI 自动发现与生成。**

因此：

```text
Semantic Sources / Runtime Evidence
           ↓
AI discovers Candidate Action
           ↓
Action Contract Draft
           ↓
Permission / Policy / Risk Verification
           ↓
RP-002-02 Business Action Runtime
```

但权限、授权和高影响行为不能仅由语义推断直接进入生产；这部分继续与 RP-004 交叉研究。

---

## 13. Minimum Validation｜最小验证

暂时不开发完整 World Model Compiler。

选择一个真实、边界清楚的小流程，同时准备自然语言 SOP、数据库 / 表结构、API 定义、角色权限和少量 Runtime Trace。

比较两种建设方式：

### A｜Manual Modeling

业务人员 / 架构师手工形成 `Object / Relation / State / Rule / Action / Permission / Transition`。

### B｜Semantic Compilation

AI 从上述材料自动生成候选模型，人只做 Review / Correction。

至少观察：

- 初始建模时间；
- 人工参与时间；
- Object / Rule / Action 覆盖率；
- 关键规则准确率；
- 权限 / 高风险动作错误率；
- 多源冲突发现率；
- 业务人员理解和修正成本；
- 增量变更后的维护成本；
- 模型可追溯性；
- 从模型到 Agent / Runtime 的可用性。

如果 B 能显著降低人工建模成本，同时关键授权与高风险错误可被 Evidence / Policy / Review 控制，则继续发展本假设。

---

## 14. Evidence Plan｜后续证据方向

优先寻找：

- `[Theory]`：Ontology Learning / Ontology Evolution / Schema Matching / Semantic Parsing / Process Mining；
- `[Product Fact]`：企业语义层 / Knowledge Graph / Process Intelligence 产品中的 AI-assisted modeling；
- `[Open Source]`：从 Schema / API / Code / Log 自动发现领域模型、流程或工具语义的实现；
- `[Industry Case]`：企业知识图谱 / 本体 / 流程模型自动或半自动建设案例；
- `[Counter Evidence]`：自动发现模型在对象边界、权限、规范性规则、高风险动作上的失败；
- `[Benchmark]`：结构抽取、Schema Matching、Process Discovery、Ontology Learning 等可比较评价方法。

研究时重点区分：

1. AI 能生成候选结构；
2. AI 能验证候选结构；
3. AI 能决定规范性规则；
4. AI 能把候选结构自动升级为生产模型。

这四者不是同一件事。

---

## 15. Child Questions｜后续只登记，不立即拆文件

- **CQ-002-07A｜Semantic Sufficiency**：仅靠自然语言语义可以可靠生成哪些业务结构，哪些必须依赖系统事实与运行证据？
- **AQ-002-07A｜World Model Compiler**：从多源业务语义到结构化世界模型，需要哪些编译阶段和中间表示？
- **AQ-002-07B｜Evidence-backed Modeling**：每个 Object / Rule / Action 如何绑定来源、证据、置信度与版本？
- **EQ-002-07A｜Multi-source Model Discovery**：文档、Schema、API、日志、流程怎样联合发现候选模型？
- **EQ-002-07B｜Incremental Compilation**：业务变化后怎样只生成 Model Diff，而不是整体重建？
- **VQ-002-07A｜Manual vs Semantic Compilation**：如何比较人工建模与 AI-assisted Compilation 的成本、准确率、治理风险和长期维护成本？

当前不继续创建更多文件，等真正启动某一个研究问题时再拆。

---

## 16. Current Stop Point｜当前停止点

本轮只完成四个认知推进：

1. **不是取消结构化模型，而是取消人工从零建模作为默认入口。**
2. **Semantic 可以成为人机交互入口，Structured World Model 继续作为生产运行表示。**
3. **AI 的主要角色从“辅助填写 Ontology”上升为“从多源企业语义与运行证据编译 Candidate World Model”。**
4. **人逐渐从 Model Builder 转向 Reviewer / Governor，把精力集中到冲突、规范性规则、权限、高风险动作和正式模型变更。**

下一步不要继续扩展产品功能，而应先验证：

> **在一个真实小流程中，AI 是否真的可以从 SOP + Schema + API + Permission + Trace 自动生成足够可用的 Semantic + Operational 候选模型，并显著降低人工建模门槛？**
