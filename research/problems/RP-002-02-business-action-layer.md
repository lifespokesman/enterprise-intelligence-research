# RP-002-02｜Business Action Layer：企业 AI 如何安全地改变企业世界

Status: Open / Exploratory  
Created: 2026-09-17  
Parent: RP-002 Enterprise Data–Model Relationship / Enterprise World Model  
Cross-link: RP-004 Effective Agency / Authority / Accountability  
Primary Track: E2 Enterprise Context / World Model → Operational Layer  
Related: E3 Agent-callable Capability / G2 Authority / G3 Human Control / G4 Traceability

> 核心子问题：**企业级 AI 应该如何把“对企业世界的理解”转换为“对企业世界的行动”，同时避免 Agent 直接耦合底层业务系统、API 和数据库？**

本文件记录一条由 Ontology / Semantic Layer 研究继续向执行层推进后形成的新问题。当前只保留为 Working Hypothesis，不进入 `JUDGMENTS.md` / `PRINCIPLES.md`。

---

## 1. Trigger｜问题来源

在研究企业本体与 Palantir Ontology 时，原有关注点主要集中在：

```text
Object
→ Relation
→ State
→ Rule
→ 数据映射 / 物化
```

这类能力能够回答：

- 企业世界中有什么对象；
- 对象之间是什么关系；
- 当前处于什么状态；
- 应遵守什么规则。

但当 Agent 进一步需要完成：

- 创建任务；
- 修改状态；
- 分配责任人；
- 发起审批；
- 调整计划；
- 写回业务系统；
- 触发其他组织或系统产生责任后果；

现实工程链路通常仍然是：

```text
业务需求
→ 找系统接口
→ 编写调用逻辑
→ 封装服务
→ 暴露为 API / MCP Tool
→ 配置给 Agent
```

由此暴露出一个新的架构断点：

> **能够描述企业世界，并不意味着 AI 已经能够安全、稳定地改变企业世界。**

Semantic Layer 与 Agent Execution Layer 之间，可能缺少一个面向“业务状态改变”的稳定抽象层。

---

## 2. Cognition Change｜认知演进

### 2.1 初始认知

最初容易把执行链理解为：

```text
Ontology
↓
Agent
↓
MCP
↓
Business System
```

因此会自然形成一个判断：

> MCP 是 Ontology 走向 Agent 执行所缺失的那一层。

但继续拆解以后发现，这个判断把“能力如何被 AI 调用”与“企业究竟允许发生什么业务动作”混在了一起。

### 2.2 当前认知

MCP / API / SDK 更接近：

> **Capability Exposure / Invocation Protocol**

它们解决的是：

- Agent 如何发现某个 Tool；
- Tool 参数是什么；
- Agent 如何调用；
- 调用结果怎样返回。

但它们本身并不天然回答：

- 这个调用在业务上意味着什么；
- 哪个对象允许被改变；
- 当前状态是否允许发生该动作；
- 谁有权执行；
- 是否需要人工确认；
- 会形成什么目标状态和业务责任；
- 失败后如何补偿；
- 应记录哪些审计证据。

因此新的工作判断是：

> **MCP 解决 Tool 如何被 AI 发现和调用，但不负责定义企业业务动作本身的语义、治理和执行约束。**

GAP-001 之后需要进一步收窄这一判断：

> **当前证据支持的是“稳定业务变更契约 + model-facing governance requirements”这一问题组合真实存在，但尚不足以证明所有企业都需要新增独立的 Business Action Layer、Agent Control Plane 或专门 Runtime。**

这些能力可以由既有 Application Service / Command / Workflow / Policy / MCP Adapter 组合承担，也可能在高影响、跨系统、多调用者条件下值得被进一步资产化为独立 Action Contract / Registry。

---

## 3. Core Question｜核心研究问题

> **企业级 AI 应该如何把“对企业世界的理解”转换为“对企业世界的行动”，同时避免 Agent 直接耦合底层业务系统、API 和数据库？**

进一步拆成五个子问题：

1. Object、Relation、State、Rule 与 Action 应是什么关系？
2. Action、Function、Workflow、API、MCP、Agent 各自属于什么层级？
3. 哪些底层接口应该被提升为稳定的 Business Action？
4. Business Action 的粒度与治理边界如何确定？
5. Action Runtime 应如何承担权限、审批、事务、补偿、审计和多系统执行？

---

## 4. Working Hypothesis v0.1｜业务动作层假设

### H-RP002-06｜Business Action as Governed Mutation Contract

> **企业 AI 要从“理解企业世界”进入“运行企业世界”，可能需要在 Agent 与现有 IT 系统之间建立独立的 Business Action 抽象；Action 不应只是 API 别名，而应成为企业允许发生的、受治理的业务状态改变契约。**

候选架构：

```text
Business World
│
├─ Object
├─ Relation
├─ State
└─ Rule
        ↓
Business Action Contract
        ↓
Business Action Runtime
        ↓
Function / Workflow / Adapter
        ↓
API / Event / RPA / DB / Human Task
        ↓
Existing Enterprise Systems
```

Agent 从另一条路径进入：

```text
LLM / Agent
     ↓
Tool Discovery / Invocation
MCP / API / SDK
     ↓
Business Action Contract
     ↓
Business Action Runtime
     ↓
Enterprise Systems
```

两条链路汇合在：

> **Business Action。**

当前状态：Hypothesis，不升级为 Architecture Principle。

---

## 5. Business Action 的候选定义

Business Action 不是某个底层 API 的业务化命名。

一个完整 Action 至少可能需要表达：

```text
Action Name
Target Object
Business Intent
Allowed Current State
Input
Precondition
Business Rule
Permission / Authority
Risk Level
Human Confirmation Requirement
Expected Effect
Target State / State Transition
Runtime Binding
Failure / Compensation
Audit Requirement
Execution Result
```

示例：

```text
Action:
ApproveInspectionTask

Object:
InspectionTask

Current State:
PendingApproval

Preconditions:
资料完整
审批人具备权限

Input:
ApprovalOpinion

Expected Effect:
PendingApproval → Approved

Runtime Binding:
调用查验系统审批接口或既有审批流程

Risk:
High-impact business action

Human-in-the-loop:
Required

Audit:
记录人员、时间、依据、输入、执行结果
```

这个定义强调：

> **Action 连接的是业务语义与 IT 实现，而不是把 IT 接口换一个业务名字。**

---

## 6. Action Contract 与 Action Runtime 的概念分离

为避免把业务语义和执行实现混为一谈，研究上先将二者作为两个概念分析；这不代表工程上必须部署为两个独立产品或层。

建议先分成：

```text
Action Contract
= 企业允许发生什么

Action Runtime
= 这个动作怎样被安全、可靠地执行
```

### Action Contract

负责表达：

- Business Intent；
- Target Object；
- Preconditions；
- State Transition；
- Policy / Permission；
- Risk / Approval；
- Expected Effect；
- Audit Contract。

### Action Runtime

候选职责：

```text
Validate
→ Authorize
→ Resolve Binding
→ Orchestrate
→ Execute
→ Retry
→ Compensate
→ Audit
→ Return Result
```

Runtime 下方才连接：

- Function；
- Workflow；
- API；
- Event；
- RPA；
- Database Adapter；
- Legacy System；
- Human Task。

因此目标是让：

```text
ApproveInspectionTask
```

在底层系统从旧 API 改为新 Workflow 时仍然保持稳定。

---

## 7. 两个核心解耦

### 7.1 Agent 与业务系统解耦

直接模式：

```text
Agent
├─ System A API
├─ System B API
└─ System C API
```

长期可能带来：

- 每个 Agent 重复理解接口；
- API 变化导致 Agent 修改；
- 权限和规则散落在 Tool / Prompt / 代码中；
- Agent Prompt 被大量技术细节污染；
- 跨系统迁移和多 Agent 复用困难。

候选目标模式：

```text
Agent
↓
Business Action
↓
Action Runtime
↓
System A / B / C
```

Agent 应尽量理解：

> **企业允许我做什么。**

而不是必须长期理解：

> **每个业务系统具体怎样实现。**

### 7.2 业务能力与 AI 协议解耦

Business Action 不应直接等同于 MCP Tool。

因为同一个业务能力未来可能同时被：

- Agent；
- 传统应用；
- Workflow；
- Human UI；
- 移动端；
- RPA；
- 外部系统；

共同调用。

候选关系：

```text
                 MCP
                  ↑
Agent → Tool Exposure
                  ↓
             Business Action
                  ↑
Application ──────┤
Workflow ─────────┤
Human UI ─────────┘
                  ↓
          Action Runtime
                  ↓
            Enterprise IT
```

因此当前工作判断：

> **MCP 是协议 / 暴露层，Action 是业务能力层。Action 的生命周期应尽量长于具体 AI 协议。**

---

## 8. Ontology 的潜在变化｜Semantic → Operational

如果 Action 假设成立，企业世界模型不能长期只表达：

```text
Noun
Object
Relation
Attribute
State
Rule
```

还需要逐渐表达：

```text
Verb
Action
State Transition
Permission
Effect
```

因此暂时提出一个研究概念：

```text
Semantic Ontology
企业世界是什么
        ↓
Operational Ontology
企业世界允许怎样被改变
```

注意：

> **Operational Ontology 目前只是本仓库的研究抽象，不把它预设为业界正式标准术语，也不预设所有企业都必须把 Action 直接放进 Ontology 产品中。**

后续需要验证：

```text
Operational Ontology
是否可以理解为：
Action
+ State Transition
+ Policy
+ Permission
+ Effect
+ Runtime Binding
```

以及：

- Action 应成为 Ontology 一等公民；
- 还是应独立成为 Action Registry；
- 两者分别适合什么企业和工程条件。

---

## 9. Action、Function、Workflow、Agent 的边界假设

### 9.1 Function

候选定义：

> **Computational Capability：完成查询、计算、验证或技术执行的可复用能力。**

例如：

```text
calculateRiskScore()
queryERP()
validateInventory()
callApprovalAPI()
```

Function 不一定改变企业业务状态，也不一定只服务某一个 Action。

### 9.2 Action

候选定义：

> **Governed Business Mutation：一个被组织承认、受规则和权限约束、可形成业务状态变化和责任后果的动作。**

例如：

```text
ApproveOrder
AssignTask
CloseAlarm
CreateWorkOrder
```

### 9.3 Workflow

候选定义：

> **已知步骤与顺序下，如何协调多个 Action / Function 完成一个业务流程。**

### 9.4 Agent Planning

候选定义：

> **面对不确定环境，根据当前状态动态决定下一步采取哪个 Action。**

因此形成一个待验证分层：

```text
Atomic Action
      ↓
Composite / Transactional Action
      ↓
Deterministic Workflow
      ↓
Agent Planning
```

该分层需要通过真实场景继续验证，不作为既定原则。

---

## 10. Action 粒度假设

当前不再把“Action 粒度没有原则”留为空白，而先提出一个可验证假设：

> **Action 粒度不应主要按 API / CRUD 划分，而应按业务意图、状态迁移和治理边界划分。**

例如：

```text
UpdateOrder
```

通常可能过粗。

而：

```text
ChangeDeliveryDate
AdjustOrderQuantity
CancelOrder
ApproveOrder
```

可能更适合作为不同 Action，因为它们可能拥有不同的：

- Business Intent；
- Preconditions；
- Permission；
- Risk；
- Approval；
- State Transition；
- Compensation；
- SLA；
- Accountability。

候选判断问题：

> **两个操作是否具有不同的业务意图、授权边界、风险责任或状态迁移？**

如果明显不同，倾向拆成不同 Action。

---

## 11. Read Path 与 Write Path 的区分

本轮同时修正一个过于绝对的原则：

> “Agent 不应该直接面向企业 IT 接口。”

这个表述过强。

很多低风险、只读、技术型能力，例如：

- 查询数据；
- 读取文件；
- 获取服务器指标；
- 检索知识；

未必都需要重新包装为 Business Action。

更值得优先 Action 化的是：

> **能够改变企业业务状态、产生组织责任、形成外部副作用或需要被治理的操作。**

因此形成一个更有解释力的候选分层：

```text
Read Path
Agent → Query / Function → Data / Knowledge

Write / Mutation Path
Agent → Business Action → Policy / Runtime → System
```

这也成为 RP-002 与 RP-004 的关键连接点：

- RP-002：世界如何被表达、读取和理解；
- 本问题：世界如何被改变；
- RP-004：谁有权改变、怎样控制和追责。

---

## 12. 与 RP-002 / RP-004 的映射

### 为什么挂在 RP-002 下

RP-002 当前已经提出：

- Semantic / Ontology 是企业现实进入模型的一种机制；
- Tool / API 是否属于 Data–Model 关系还是更上位的 Capability / Action 关系仍待澄清。

本问题正是从这个边界继续向下推导：

```text
Enterprise Reality
↓
Semantic / World Representation
↓
Business Action
↓
Execution
```

因此暂时作为 RP-002 的 Operational Layer 子问题，而不新增一个新的顶层 Research Problem。

### 为什么强关联 RP-004

一旦 Action 可以真正改变业务状态，就立即进入：

- Authority；
- Policy；
- Human Control；
- Accountability；
- Audit；
- Runtime Safety。

这些属于 RP-004。

因此关系可以表示为：

```text
RP-002
世界如何进入 AI / 被 AI 理解
        ↓
RP-002-02
世界如何被 Action 改变
        ↓
RP-004
谁有权改变 / 如何安全控制 / 如何追责
```

这三个问题应关联，但暂时不合并。

---

## 13. Engineering Hypothesis｜最小可验证架构

当前不开发完整 Action Platform。

选择一个真实但可抽象的业务流程：

```text
风险发现
↓
创建任务
↓
分配人员
↓
人工确认
↓
任务状态更新
```

手工定义：

```text
Object
State
Rule
Action
Function
Runtime Binding
Permission
Audit
```

比较两组实现。

### A｜Direct Tool / API Agent

```text
Agent
→ API / MCP Tool
→ Business System
```

### B｜Business Action Agent

```text
Agent
→ Business Action
→ Action Runtime
→ API / Workflow / System
```

观察：

- Agent Prompt 复杂度；
- Tool 数量；
- API 变化影响范围；
- 权限治理复杂度；
- 多 Agent 复用程度；
- Trace 可解释性；
- 业务人员理解难度；
- 关键动作审批与审计能力；
- Runtime 适配成本。

如果 B 组在这些指标上持续改善，才进一步支持 Business Action Layer 成为企业 AI 基础架构的一部分。

---

## 14. Counter Hypotheses｜必须主动寻找的反例

不能只寻找支持 Action Layer 的证据。

需要主动验证：

1. 强模型 + 清晰 MCP Tool Schema 是否已经足够，额外 Action Layer 只会增加复杂度？
2. 传统 Service / Domain API / Application Service 是否已经承担了 Business Action 的角色，只是名称不同？
3. 在微服务和领域驱动设计成熟的企业中，Action Layer 是否只是既有 Service Layer 的重新包装？
4. 对低风险、低复用、系统单一的场景，直接 Tool / API 是否更经济？
5. Action Contract 是否会因为企业流程频繁变化而失去所谓“稳定性”？
6. 将 Action 放入 Ontology 是否会造成模型层与执行层过度耦合？

只有能够解释这些反例，Action Layer 才可能从漂亮架构图升级为稳定架构原则。

---

## 15. Evidence Plan｜下一步证据方向

优先寻找：

- `[Product Fact]`：Palantir Ontology Actions / Functions、Salesforce、ServiceNow、SAP、Microsoft 等企业平台怎样定义业务动作、状态改变和 Agent 执行；
- `[Architecture Pattern]`：DDD Application Service / Command、CQRS、Workflow / BPM、Capability API、Policy Enforcement 等传统架构与本问题的关系；
- `[Protocol / Standard]`：MCP、API / Tool Schema、Agent Tool-use 协议到底负责什么、不负责什么；
- `[Open-source Implementation]`：Action Registry、Agent Runtime、Workflow、Policy Engine、Durable Execution 等实现；
- `[Industry Case]`：企业 Agent 如何完成真实写操作、审批、派单、变更和跨系统动作；
- `[Counter Evidence]`：不需要独立 Action Layer 也能长期稳定运行的工程案例。

重点不是继续寻找“Action”这个词，而是验证以下机制是否真实存在：

```text
Stable Business Mutation Contract
×
Decoupled Execution Binding
×
Policy / Authority
×
Durable Runtime
×
Audit / Evidence
```

---

## 15A. GAP-001 Evidence Update｜H0 → H1

本轮证据显示，Business Action 的核心职责并非全部由 AI 时代新创造：

- DDD Application/Domain Service 已承担业务操作边界、领域过程契约、事务协调与领域规则委托；
- CQRS Command 已把业务意图表达为高于字段更新的写操作，并由 Handler 调用领域模型；
- BPMN 与 Durable Workflow 已承担流程语义、状态持久化、检查点、重试与恢复；
- Agent 时代显著强化的是模型控制调用带来的授权范围发现、Typed Schema、人工确认/权限、显式状态句柄、非可信元数据、输入输出校验、限流和审计控制面。

### H1｜Conditional Action Contract / Model-facing Governance Boundary

> **Business Action 更准确地应被视为一种有条件的、跨调用者的受治理业务变更契约，而不是在所有企业系统中都必须新增的独立领域层。**

GAP-001 目前只支持 Agent 带来一组更强的 model-facing governance requirements：动态发现、Typed Schema、授权/确认、输入输出校验、状态句柄和审计等。它们是否应独立形成所谓 “Agent Control Plane” 尚未得到充分证据支持。

当动作具有高影响、跨系统、审批密集、长时运行或需要在多个 Agent / 应用 / Workflow 之间保持稳定语义时，独立 Action Registry、专门治理边界或 Runtime 可能值得存在；对于低风险、单系统、可逆的 CRUD 类动作，强 Domain API 或 Command 加 Typed Tool Schema 仍可能足够。

### H0 → H1 变化记录

- 旧假设：Agent 与 IT 之间可能需要独立 Business Action 抽象与 Action Runtime；
- 触发证据：GAP-001 的 E-001 至 E-005；
- 变化原因：传统架构已覆盖大部分业务语义与可靠执行机制，Agent 的新增量集中在模型控制调用的治理与安全边界；
- 新边界：不能把独立 Action Layer 作为普遍架构要求，必须证明跨系统稳定性、高影响治理或多调用者复用带来的增量价值；
- 尚未解决：什么样的风险/协调阈值使独立 Action Registry/Runtime 相比既有 Service/Command/Workflow 组合产生可测收益。

本轮不修改 `PRINCIPLES.md`，也不把 H1 升级为 Architecture Principle。

## 16. Candidate Architecture Judgment｜暂不升级 Principle

GAP-001 之后，原先“企业 AI 普遍需要独立 Business Action Layer”的表达需要降级和收窄。

当前更稳妥的候选判断是：

> **对高影响、跨系统、审批密集、长时运行或多调用者共享的业务变更，企业可能需要一个稳定、受治理的 mutation contract，使业务意图、状态迁移、授权 / 确认、审计与底层 Service / Command / Workflow 绑定解耦。这个契约是否需要表现为独立 Business Action Layer、Action Registry 或专门 Runtime，应由现有架构能力和可测收益决定。**

因此当前不把 “Action Layer” 本身当作原则。下一步需要通过 Palantir 等产品机制与工程验证判断：

- Ontology-native Action 是否提供超出传统 Application Service / Command / Workflow 的稳定机制；
- model-facing governance requirements 是否需要独立层承载；
- 哪些风险 / 协调 / 复用阈值足以支持额外抽象成本。

该判断仍属于 `Working Hypothesis / Candidate Judgment`，不得直接写入 `PRINCIPLES.md`。

---

## 17. Child Questions｜后续问题树

本问题后续不继续把所有内容塞进一个文件，而拆成子问题：

- **AQ-002-06A｜Action Boundary**：Business Action 应如何划定粒度与边界？
- **AQ-002-06B｜Action Contract**：Action Contract 的最小语义集合是什么？
- **AQ-002-06C｜Action vs Workflow vs Agent Planning**：三者如何分工？
- **EQ-002-06A｜Action Runtime**：授权、审批、事务、补偿、重试和审计怎样实现？
- **EQ-002-06B｜Legacy Modernization**：现有 API / Service / Legacy System 如何逐步提升为可复用 Business Action？
- **VQ-002-06A｜Direct Tool vs Action Layer**：怎样实证比较直接 Tool 与 Action Layer？
- **CQ-002-06A｜Ontology Boundary**：Action 应成为 Ontology 一等公民还是独立 Action Registry？
- **CQ-002-06B｜Action Discovery**：AI 能否从 API、流程、日志和人工操作中自动发现候选 Action？

这些问题只在真正启动研究时再独立成文件，当前先保持为问题树。

---

## 18. Current Stop Point｜当前停止点

本轮完成：

1. 将“AI 如何改变企业世界”映射为 RP-002 的 Operational Layer 子问题；
2. 明确它与 RP-004 的 Authority / Control / Accountability 交叉关系；
3. 将认知从 `Ontology → Agent → MCP → System` 修正为 `Semantic World → Business Action Contract → Action Runtime → Enterprise IT`；
4. 将 MCP 降回能力暴露 / 调用协议，而不是业务动作本体；
5. 分离 Action Contract 与 Action Runtime；
6. 初步划分 Action / Function / Workflow / Agent Planning；
7. 提出 Action 粒度、Read / Write Path 和最小验证假设；
8. 通过 GAP-001 对照 DDD、CQRS、BPMN、Durable Workflow 与 MCP，形成 H0 → H1；
9. 明确独立 Action Layer 的适用边界，以及直接 Domain API + Tool Schema 的反例条件；
10. 暂不把任何判断升级为正式 Principle。

下次继续本问题时，优先从：

> **对照 Palantir / ServiceNow / Salesforce / SAP 与 DDD / CQRS / Workflow 等传统架构，验证“Business Action Layer”究竟是 AI 时代新增层，还是已有企业应用能力在 Agent 时代的重新显性化与资产化。**

开始；下一轮具体执行 `GAP-002`，核验 Palantir Ontology Actions / Functions 是否提供超出传统 Service / Command / Workflow 的稳定机制。


---

## 19. Cross-cutting Question｜AI 接管认知与操作后，传统企业机制还剩什么？

### Trigger

随着 Agent 逐渐接管传统业务系统中的：

```text
Information Retrieval
→ Understanding
→ Judgment
→ Planning
→ Operation
```

一个更上位的问题开始出现：

> **如果大量“找信息、理解信息、判断下一步、点击系统操作”的工作都可以由 AI 完成，那么 Workflow、System of Record、Policy 和 Human Responsibility 还承担什么不可替代的职责？**

这个问题不预设“AI 会替代传统业务系统”，而是尝试区分：

- 哪些传统职责只是为了帮助 Human 操作复杂系统，因此可能被 AI 吸收；
- 哪些职责属于企业正式运行本身，不能因为交互主体从 Human 变成 Agent 就消失。

### H-RP002-07｜Enterprise Control Anchors

当前提出一个待验证工作假设：

> **AI 更可能吸收传统应用中的 Cognitive / Interaction / Adaptive Orchestration 职责，而 Workflow、System of Record、Policy 与 Human Responsibility 中仍会保留一组确定性的 Enterprise Control Anchors，用来锚定过程承诺、权威事实、允许边界和最终责任。**

候选四类 Anchor：

| Mechanism | 可能被 AI 吸收的部分 | 候选不可替代职责 |
|---|---|---|
| **Workflow** | 流程理解、下一步选择、动态分支、填表与触发 | Durable Process State、必须执行的控制点、等待 / 超时、事务 / 补偿、恢复、跨步骤承诺 |
| **System of Record** | 查询、解释、汇总、跨系统信息获取 | Authoritative Object Identity、正式业务状态、交易事实、一致性、审计与可追溯事实基线 |
| **Policy** | 规则解释、情境判断、规则适用建议 | Allowed / Denied / Approval Required 等正式约束，Authority、Risk、Compliance 与 Exception Boundary |
| **Human Responsibility** | 常规判断、操作、审核、信息整合 | Authority Source、Delegation Boundary、Accountability Anchor、价值冲突处理、重大例外与制度治理 |

这里的“不可替代”目前只是研究假设，不是稳定判断。后续必须寻找反例，包括：

1. 某些 Workflow 是否可以完全由 Agent + Event Log + Durable Runtime 重构，而不再保留传统 Workflow Engine；
2. 某些业务是否可以采用 Event Sourcing / Ledger / Data Product 等方式承担 SoR 职责，而不依赖传统应用系统；
3. Policy 是否可以部分由模型动态生成，仍通过形式化 Guard / Constraint 验证；
4. Human Accountability 是否会在某些低风险、强监管自动化场景中被重新配置，而不是始终保持逐动作人工确认。

### 19.1 Workflow：从 Process Intelligence 收缩到 Durable Coordination？

传统 Workflow 往往同时承担：

```text
理解流程
+ 决定下一步
+ 记录流程状态
+ 保证关键步骤发生
+ 等待 / 超时 / 重试 / 恢复
```

Agent 能力增强后，前两项可能逐渐转向概率性的动态 Planning；但后几项属于企业已经承诺发生的过程状态与可靠协调。

因此形成待验证边界：

```text
Agent Planning
= 根据当前 Context 决定“现在应该做什么”

Workflow / Durable Execution
= 保证“已经承诺的事情可靠发生”
```

这会进一步修正本文件此前的 `Action vs Workflow vs Agent Planning` 问题：研究重点不只是三者粒度不同，而是 **Adaptive Decision 与 Durable Commitment 是否构成更稳定的边界**。

### 19.2 System of Record：Application UI 可能弱化，但 Authoritative Reality 不会自动消失

Agent 可能使用户不再频繁进入 ERP / CRM / OA / 工单系统界面，但企业仍然必须回答：

- 一个业务对象究竟是谁；
- 当前正式状态是什么；
- 哪笔交易真实发生过；
- 哪一次修改具有法律 / 财务 / 业务效力；
- 谁在什么时间基于什么权限改变了什么。

因此需要明确：

```text
System of Record
≠ Agent Context
≠ RAG Knowledge
≠ Agent Memory
```

候选关系：

```text
System of Record
= Authoritative Runtime Facts

World Model / Semantic Layer
= 企业如何理解这些事实

Task Context
= 当前任务需要让 Agent 看见什么

Agent
= 基于 Context 判断、计划并提出 / 执行动作
```

这使 RP-002 的“Enterprise Reality → Context → Agent”链路增加一个重要约束：

> **Context 可以是动态、裁剪和推理友好的，但关键业务事实必须能追溯到正式事实来源，而不能由 Agent 自己成为默认事实权威。**

### 19.3 Policy：从“告诉人怎么做”转向“约束 Agent 可以做什么”

需要区分：

```text
Judgment
vs
Policy
```

例如：

- “这个客户风险较高”更接近 Judgment；
- “风险等级达到 X 且金额超过 Y 必须人工审批”更接近 Policy。

模型可以参与前者，但后者表达的是组织正式决定：

> **什么主体，在什么条件下，被允许以什么权限改变企业世界。**

因此 Policy 不应仅作为 Prompt 文本存在。对于高影响 Action，更值得验证如下结构：

```text
Agent Proposal
      ↓
Policy / Authority Check
      ↓
Allowed
Denied
Approval Required
Limited Delegation
```

这与 RP-004 的 Authority / Human Control / Accountability 直接交叉。

### 19.4 Human Responsibility：从 Every-step Operator 转向 Authority / Accountability Anchor？

Agent 接管更多操作以后，需要避免把三个概念混为一谈：

```text
AI can make a decision
≠ AI owns the decision right
≠ AI bears accountability
```

人类角色可能从：

> Human-in-the-loop for every action

逐步转为：

> Human as Authority Source + Delegation Designer + Accountability Anchor + Exception Governor

重点研究不再只是“是否人工确认”，而是：

- 谁授予 Agent 什么 Decision / Action Right；
- 授权范围、金额、风险和持续时间如何限定；
- 什么情况下 Agent 必须停止并升级；
- 谁有权修改 Policy；
- 出现错误、冲突或外部后果时由谁接管和承担责任。

### 19.5 Candidate Operating Model｜概率性智能与确定性控制边界

当前可形成一个研究用草图：

```text
Human
  │
  ├─ Intent
  ├─ Authority Source
  └─ Accountability
        ↓
      Policy
        ↓
Enterprise Reality → Task Context
        ↓
   Agent / Harness
Understand → Judge → Plan
        ↓
   Business Action
        ↓
Workflow / Durable Execution
        ↓
 System of Record
        ↓
Enterprise Reality
```

候选四类稳定锚点：

```text
System of Record
= Reality Anchor

Policy
= Constraint / Authority Anchor

Workflow / Durable Execution
= Commitment / Execution Anchor

Human Responsibility
= Accountability Anchor

Agent / Harness
= Cognitive / Adaptive Coordination
```

这个模型当前只用于组织后续 Evidence，不进入 `JUDGMENTS.md` 或 `PRINCIPLES.md`。

### 19.6 与现有问题体系的关系

本问题不新增 RP，原因是它可以被现有问题共同解释：

- **RP-002 / RP-002-04**：SoR / Enterprise Reality 如何进入 World Model 与 Task Context；
- **RP-002-02**：Agent 的 Judgment 如何转换为受治理 Business Action；
- **RP-006**：AI 如何持续执行“获取—理解—判断—操作”循环；
- **RP-004**：Policy、Authority、Human Control 与 Accountability 如何限制和授权行动；
- **Q1**：哪些 Decision Rights 可以动态委托给 AI；
- **Q2**：责任和 Authority 最终锚定在哪里；
- **Q3**：Human、Agent、Workflow、Software 如何形成稳定协调。

当前更适合把它视为一个 **cross-cutting cognitive / architecture question**：

> **当 AI 接管传统业务系统中的信息获取、理解、判断和操作后，哪些企业运行职责可以被概率性智能吸收，哪些职责必须继续由确定性系统、制度与责任主体承担？**

### 19.7 Evidence Plan｜下一步验证什么

后续如果启动这一问题，不先证明“四锚点模型正确”，而围绕以下问题寻找 Theory / Product / Case / Standard / Counter Evidence：

1. **Workflow**：Agent Planning 与 Durable Workflow 的边界是否在不同产品 / 案例中稳定存在？
2. **SoR**：AI-native 应用是否仍显式保留 authoritative state / ledger / transaction source？
3. **Policy**：高影响 Agent 是否把关键授权和约束从 Prompt 外置到 Policy / Guard / Approval 机制？
4. **Responsibility**：企业如何把 Delegated Authority 与最终 Accountability 绑定到 Human / Role / Organization？
5. **Counter Evidence**：有没有场景表明上述四类 Anchor 可被合并、替换或完全由新的 AI-native runtime 重构？

如果这些机制跨多种架构持续出现，再判断是否值得上升为更稳定的 Architecture Principle 或新的问题演化。
