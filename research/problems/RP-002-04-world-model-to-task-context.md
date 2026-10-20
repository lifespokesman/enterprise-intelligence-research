# RP-002-04｜World Model → Task Context Runtime

Status: Open / Exploratory  
Created: 2026-09-23  
Parent: RP-002 Enterprise Data–Model Relationship  
Primary Track: E2 Enterprise Context / World Model  
Related: RP-002-01 World Model Conflict & Evolution / RP-002-02 Business Action Layer / RP-002-03 Semantic-to-Executable World Model / E1 Agent Runtime / E3 Capability / G2 Authority & Policy

> 核心子问题：**企业业务世界模型如何被动态转换成面向当前任务的 AI Context，以及 Ontology、Context Runtime、Agent Runtime、Action 与模型演化之间应该如何分工？**

本文件保存一个新的待验证研究问题。它不是“Ontology 和 Context 有什么区别”的术语比较，也不预设 Context Engine / Context Runtime 已经是业界稳定、独立的工程组件。

---

## 1. Trigger｜问题如何一步步演化出来

此前围绕企业业务本体，曾形成一个直观划分：

- 静态本体：Object / Relation / Rule；
- 动态本体：State / Event / Action；
- 本体演化：AI 根据运行事实发现新结构，人审核后更新 Ontology。

继续推演后发现，这种划分可能混合了三个不同问题：

1. 企业世界本身由什么构成？
2. 企业世界此刻怎样运行和变化？
3. 企业对这个世界的模型什么时候应该变化？

因此，“静态本体 / 动态本体 / 本体演化”未必首先需要被发明成新的 Ontology 分类，更可能只是观察同一个企业业务世界的不同叙事视角。

问题随之从：

> Ontology 应该怎样继续扩展？

转向：

> **企业业务本体（Ontology）与企业级 AI Context 到底是什么关系？**

进一步观察发现，两者虽然大量共享对象、状态、规则、权限等信息，但组织信息的出发点并不相同：

- Ontology 更接近 World-centric View：企业世界是什么、如何关联、允许怎样变化；
- AI Context 更接近 Task-centric View：当前任务为了完成目标，此刻需要知道企业世界中的哪些内容。

因此真正需要研究的不是简单概念边界，而是：

> **企业世界模型如何被解析、检索、过滤、授权并组装为当前任务可使用的动态 Context？**

---

## 2. Core Tension｜核心矛盾

### 2.1 World-centric View

当前观察（待验证）：

Ontology / Enterprise World Model 的典型组织方式更接近：

~~~text
Core Object
→ Relation
→ Property
→ State
→ Event
→ Rule
→ Action
→ Permission / Responsibility
~~~

它回答：

> 企业在管理什么，这些业务对象怎样存在、关联、变化和被治理？

### 2.2 Task-centric View

而 Agent 当前运行时的 Context 可能同时需要：

- Task / Goal；
- 当前业务对象与对象状态；
- 实时业务事实；
- 历史案例、制度、文档和专家知识；
- 用户身份和权限；
- Session / short-term Memory；
- 当前 Agent Plan；
- Tool / API availability 与 Tool State；
- Event；
- Runtime 状态与中间执行结果。

其路径更接近：

~~~text
Task
→ identify relevant objects
→ resolve facts / knowledge / rules
→ apply identity / policy
→ include runtime state
→ assemble task context
~~~

它回答：

> **企业世界中，哪些信息与当前这个任务有关，并且此刻允许以什么方式提供给 Agent？**

### 2.3 本轮核心矛盾

> **Ontology 以企业世界为中心组织稳定语义，Context 以当前任务为中心组织相关信息。二者大量交叉，但不是同一个东西。企业 AI 架构中，二者的职责、转换机制和运行边界应如何划分？**

---

## 3. Current Observations｜当前观察，不作为结论

1. Ontology 可能更适合作为企业世界的共享语义骨架，而不是直接承担所有 Agent Context。
2. Context 可能是一个运行时产物：它必须同时包含世界事实、知识、身份策略和 Agent 自身的短期运行状态。
3. 同一个 Ontology 在不同 Task 下应产生不同 Context；因此“有 Ontology”不等于“Context 已经准备好”。
4. Session、Plan、短期 Memory、Tool State 等运行信息很难被合理归入企业业务 Ontology。
5. Action 执行后的新事实会改变下一轮 Context，但只有在现有模型无法解释现实、需要新增或修改类型结构时，才应进入 Ontology Evolution。
6. Context Engine / Context Runtime 目前只能作为**候选机制名称**，不能在证据不足时直接升级为独立 Layer / Platform / Runtime。

---

## 4. Current Hypotheses｜H1–H4，全部待验证

### H1｜Ontology ≠ AI Context

**当前假设 / 待验证：**

> **Ontology 不是 AI Context 本身，而可能是企业 AI Context 的 World Model / Semantic Backbone。**

它主要解决：

- 企业中有哪些对象；
- 对象是什么；
- 对象如何关联；
- 有哪些状态和事件；
- 受到哪些规则约束；
- 能执行哪些业务动作；
- 权限 / 责任如何绑定业务语义。

它不能单独解决：

- 当前 Task / Goal；
- 用户即时意图；
- Session；
- 短期 Memory；
- Agent Plan；
- 当前实时 Tool Result / Tool State；
- Runtime 资源与执行状态。

待验证重点：主流产品和工程实现是否稳定呈现这一边界，还是有产品把二者合并为同一抽象。

### H2｜Context = Task-centric World Slice

**当前假设 / 待验证：**

> **AI Context 是围绕当前 Task，从企业世界、知识世界和运行环境中动态抽取并组装出的“相关世界切片”。**

候选表达：

~~~text
Task Context
=
World Context
+
Knowledge Context
+
Runtime Context
+
Identity / Policy
~~~

其中：

**World Context**
- Ontology / Semantic Model；
- Object Instance；
- Relation；
- Current State；
- Business Rule；
- Action definition。

**Knowledge Context**
- Document；
- Policy / SOP；
- Case；
- Expert Knowledge；
- Knowledge Base；
- RAG / Search / KG。

**Runtime Context**
- Task；
- Session；
- Memory；
- Event；
- Tool State；
- Agent Plan；
- intermediate result；
- real-time environment。

**Identity / Policy**
- 当前是谁 / 什么 Agent；
- 可见哪些数据；
- 可调用哪些 Tool；
- 可执行哪些 Action；
- 是否需要 Approval。

这里的“World Slice”是**工作抽象**，不是已经验证的行业术语。

### 2026-10-09 增量｜由业务任务与风险倒推 Context 配置（H2 精炼，非新增平行假设）

本轮外部 Signal 触发一个需求侧修正：**先明确业务结果、约束与具体任务是否适合 AI，再判断模型需要什么 Context**；而不是以“已经有统一知识库 / Ontology / Context 平台”作为 Agent 设计起点。

在不改变 H2 身份的前提下，增加一组待验证的 Context 选择变量：

- **Task / Goal**：要做知识解释、跨系统分析、长程产出还是高风险状态修改；
- **Information Dependency**：需要历史知识、当前业务事实、业务语义、运行过程状态中的哪些组合；
- **Freshness / Provenance**：允许多旧的事实、怎样追溯依据与冲突；
- **Identity / Risk / Responsibility**：能看什么、能依据什么做判断、能否产生高影响动作；
- **Environment / Execution State**：中途是否需要读取文件、工具结果、检查点或外部环境变化。

候选机制为 `Business Outcome / Constraints → Task → Context Requirements → Retrieve / Query / Resolve / Filter / Assemble`。这是一条需求推导启发式，**不是必须建设 Context Engine 的论证**，更不是说所有信息必须注入 Prompt；部分信息应维持为外部事实查询、受限工具结果与可强制执行的 Policy。

**反向解释：** 对大量低风险、事实依赖简单的任务，模型原生长上下文、直接 API 查询或简单 RAG 已足够；跨任务共享 Context 基础设施未必比应用内轻量组合更有价值。共享机制只有在多个任务之间带来净复用、治理或一致性收益，且不会显著损害安全域隔离、时延和自治时才值得考虑。

**连接：** RP-006 / VQ-006-01 比较不同任务的 Model / Harness / Context 配置；RP-004 负责 Authority 与 Accountability 的决定权；RP-003 负责结果反馈如何形成组织长期能力。此处仅精炼 H2 的需求条件，不把 Business Outcome 重新定义为 RP-002-04 的独立母问题。

### H3｜Ontology / Business Runtime 与 Context Runtime 是两个不同循环

**当前假设 / 待验证：**

企业世界运行可能更接近：

~~~text
Ontology / World Model
→ Object Instance
→ State
→ Event
→ Rule
→ Action
→ New State
→ New Fact
~~~

它关注：

> 企业世界本身发生了什么变化。

面向任务的 Context 运行可能更接近：

~~~text
Task
→ identify required information
→ use World Model to locate business objects
→ retrieve Data / Knowledge / Rule / Policy
→ filter / authorize
→ assemble Context
→ Agent Reasoning
→ Action
~~~

它关注：

> 当前任务需要怎样观察企业世界。

二者候选闭环：

~~~text
Action
→ New Fact
→ Enterprise World Change
→ Next Context Change
~~~

关键待验证点：

- 是否真的存在可独立识别的 Context Runtime；
- Retrieve / Resolve / Filter / Authorize / Assemble 是否属于同一组件；
- 这些职责是由 Agent Runtime、Semantic Layer、Data Platform、Policy Engine 分担，还是形成稳定独立机制。

### H4｜Ontology Evolution 是第三个、更慢的认知循环

**当前假设 / 待验证：**

必须区分**实例变化**和**模型变化**。

对象实例按既有模型发生：

~~~text
待查验
→ 查验中
→ 待复核
→ 已完成
~~~

只是按照既有 Ontology / State Model 运行，**不等于 Ontology 被修改**。

只有当运行事实暴露出：

- 新对象类型；
- 新关系；
- 新事件类型；
- 新状态；
- 新规则；
- 新 Action；
- 或已有概念边界无法解释现实；

才进入候选模型演化：

~~~text
Runtime Facts
→ Model cannot explain reality
→ AI / system discovers candidate structure
→ evidence & expert review
→ governed Ontology Evolution
~~~

因此当前候选治理假设为：

> **人负责最小可信世界模型及治理边界；系统持续记录世界事实；AI 负责发现世界模型与现实之间的差异；人决定是否升级正式世界模型。**

该假设与 RP-002-01 强相关，但本问题只负责说明它与 Context Runtime 的节奏差异，不重复研究“冲突最终如何裁决”。

---

## 5. Candidate Architecture｜总体架构候选，仅作研究对象

~~~text
Enterprise AI Context Architecture

1. Enterprise World Model
   Ontology
   Object / Relation / State / Event / Rule / Action

2. Enterprise Facts
   Database / API / Metric / Event / Current State

3. Enterprise Knowledge
   Document / Case / Policy / Expert Knowledge

4. Identity & Policy
   User / Agent / Permission / Security / Approval

5. Agent Runtime
   Task / Session / Memory / Plan / Tool State

6. Context Mechanism ?   [待验证是否应独立]
   Retrieve
   Resolve
   Filter
   Authorize
   Assemble

                ↓

              Agent

                ↓

              Action

                ↓

        Enterprise World Change
~~~

研究目标不是验证这张图“是否漂亮”，而是验证：

> **这些职责是否真的需要独立？哪些只是逻辑概念，哪些已经形成稳定工程边界，哪些应归入现有 Agent Runtime / Data / Semantic / Policy / Action 基础设施？**

---

## 6. Research Questions｜需要验证的关键问题

### Cognitive Questions

1. Ontology 是否可以被合理理解为 Enterprise World Model，而不是 AI Context 本身？
2. Context 是否本质上是面向 Task 的动态相关世界切片？
3. 什么信息属于企业世界的稳定语义，什么信息只属于一次任务运行？
4. Session / Intent / Plan / short-term Memory / Tool State / Runtime State 是否应明确排除在业务 Ontology 之外？
5. “实时事实”属于 World Model、Data Source 还是 Context，三者应如何区分表示与实例？

### Architecture Questions

6. Ontology 在 Context 构建中应承担哪些职责：语义解释、对象定位、关系遍历、状态理解、规则发现、Action discovery？
7. RAG、Knowledge Graph、Ontology、Data Platform、Memory、Policy、Tool / API 分别为 Context 提供什么？
8. 企业是否需要独立的 Context Engine / Context Runtime，还是该能力应由 Agent Runtime + Semantic/Data/Policy 服务组合完成？
9. Ontology Runtime 与 Context Runtime 应怎样解耦？
10. Identity / Policy 应在数据检索前、Context 组装时还是 Action 执行时生效？是否需要多阶段授权？
11. Context 的 Source / Lineage / Freshness / Permission / Evidence 应怎样随 Context 一起进入 Agent？

### Closed-loop / Evolution Questions

12. Agent Action 产生的新事实怎样更新 Object Instance / State / Event？
13. 新事实怎样进入下一轮 Context，而不触发不必要的 Ontology Change？
14. 什么信号意味着“实例变化”已经升级为“模型解释失败”，应该转交 RP-002-01 的 Ontology Evolution 机制？
15. Context Runtime 的运行 Trace 能否成为世界模型演化的关键 Evidence Source？

---

## 7. Relationship to Existing Problems｜与已有问题的关系

本问题**不升级为新的 Problem Family / 母 RP**。它属于 RP-002 的派生子问题。

### Parent｜RP-002 Enterprise Data–Model Relationship

RP-002 的上位问题是：

> 企业真实世界如何通过 Data / Knowledge / Semantic / Context / Feedback 进入 Model / Agent，并持续保持与现实一致？

RP-002-04 进一步研究其中缺失的一段转换机制：

> **World Model / Facts / Knowledge / Policy / Runtime → Task-specific Context。**

### Related｜RP-002-01 World Model Conflict & Evolution

RP-002-01 研究：

> 世界模型与现实冲突后，什么时候以及怎样修改正式模型？

RP-002-04 研究：

> 在模型未被修改的多数运行时刻，怎样从当前世界状态生成任务 Context？

关系：

~~~text
Context Runtime Trace / Failure
→ Evidence of model mismatch
→ RP-002-01 Evolution
~~~

### Related｜RP-002-02 Business Action Layer

RP-002-02 研究：

> Agent 如何通过受治理 Action 改变企业世界？

RP-002-04 研究 Action 前后的 Context：

~~~text
Task Context
→ Agent Reasoning
→ Business Action
→ New Fact / New State
→ Next Task Context
~~~

二者共同构成“观察世界 → 改变世界 → 再观察世界”的闭环。

### Related｜RP-002-03 Semantic-to-Executable World Model

RP-002-03 研究：

> 企业语义 / Schema / API / Workflow / Trace 如何形成可执行世界模型？

RP-002-04 假设：

> 即使已有 Structured / Executable World Model，仍需要研究它如何进入具体任务的 Runtime Context。

因此：
- -03 偏**世界模型如何生产 / 维护**；
- -04 偏**世界模型如何被任务运行时消费**。

### Related｜E1 Agent Runtime / E3 Capability / G2 Policy

本问题处在三个已有长期方向的交界：
- E2 提供企业世界语义；
- E1 提供 Task / Session / Memory / Plan 等运行状态；
- E3 提供 Action / Tool capability；
- G2 约束可见数据和可执行动作。

因此它天然适合作为连接问题，而不是新建“Context Platform”研究 Track。

---

## 8. Evidence Plan｜后续证据路径

本轮不开展外部研究。后续验证至少覆盖四类证据，并必须寻找反例。

### 8.1 Theory / Papers

优先寻找：
- Ontology / Enterprise Ontology；
- Knowledge Representation；
- World Model；
- Context-aware Systems；
- Context Engineering；
- Task-oriented Context；
- Semantic Layer；
- Dynamic Ontology / Ontology Evolution；
- Agent Memory / Runtime Context。

重点不是收集定义，而是验证：

> 是否已有研究明确区分相对稳定的 World Representation 与面向任务、状态依赖的 Context。

### 8.2 Product Routes

重点观察：
- Palantir Ontology / AIP；
- Microsoft Fabric Ontology；
- Databricks semantic / agent capabilities；
- Salesforce Data Cloud / Agentforce；
- ServiceNow；
- SAP；
- Neo4j / GraphRAG；
- Google / Microsoft Agent runtime ecosystems。

统一比较问题：
- 如何表示企业世界？
- 如何绑定真实数据和实时状态？
- Agent 如何取得 Context？
- Context 是预定义还是动态生成？
- 权限在哪里生效？
- Tool / Action 如何与业务对象绑定？
- 执行后怎样回写世界？
- Runtime Trace 能否反向驱动语义模型变化？

### 8.3 Engineering Architecture

寻找：
- Context assembly 是否形成独立组件；
- Agent Runtime 怎样做 retrieval / state resolution / policy filtering；
- Ontology query 如何进入 Prompt 或 Tool 调用；
- Semantic Layer 与 RAG / KG 的组合；
- Policy 如何参与 Context filtering；
- Context provenance / freshness / evidence 的工程实现；
- 不存在独立 Context Engine 但仍能稳定运行的 Counter Evidence。

### 8.4 Enterprise Cases

优先真实业务运行，而非单纯知识问答：
- 企业世界模型由谁维护；
- Agent 运行依赖哪些 Context；
- 实时状态从哪里来；
- Action / Tool 怎样与业务对象和权限绑定；
- 结果怎样回写；
- 是否真的发生持续 Ontology Evolution，还是主要只发生实例状态变化。

---

## 9. First Validation Order｜下一轮最值得优先验证的顺序

### Gap A｜World Model 与 Task Context 的概念边界

先验证：

> **“稳定世界表达”与“任务运行时上下文”是否是跨理论 / 产品 / 工程都存在的稳定区分？**

没有这个区分，不应继续设计 Context Runtime。

### Gap B｜Context Assembly 是否形成稳定工程边界

再验证：

> Retrieve / Resolve / Filter / Authorize / Assemble 是独立 Context 机制，还是 Agent Runtime 与既有 Semantic / Data / Policy 能力的组合职责？

这是当前证据最薄弱、也最容易被命名冲动误导的部分。

### Gap C｜Action → Fact → Next Context → Evolution 的闭环边界

最后验证：

> Action 后的新事实如何只更新运行世界与下一轮 Context；什么条件下才应该升级为 Ontology Evolution？

这将连接 RP-002-01 与 RP-002-02，但不重复它们各自的研究。

---

## 10. Non-goals｜本轮明确不做

- 不把 Context Engine 直接定义成新的架构层；
- 不把 Context Runtime 写成已成立的产品类别；
- 不把所有 Runtime 状态塞进 Ontology；
- 不重新定义新的“静态本体 / 动态本体”分类体系；
- 不因为新增问题改变当前 Research Runner v0.4 的 RP-002-02 试运行范围；
- 不修改 JUDGMENTS.md / PRINCIPLES.md；
- 不把 H1–H4 写成已验证结论。

---

## 11. Resume Point

下一轮如启动本问题，只推进 **Gap A**：

> **先用理论 + 至少两类产品 / 工程实现验证“World Model 与 Task Context 是否存在稳定边界”，同时寻找把二者合并建模的反例。**

在 Gap A 之前，不继续扩展完整 Context Platform 架构。


---

## 2026-10-12 增量｜Ontology → Task Context → Controlled Action 的接口与验证

**性质：** 对 H1–H4 的工程细化，不新增问题族或正式 Hypothesis ID；关联 RP-002-02（Action 契约与执行）、RP-002-03（语义辅助建模）、RP-002-01（证据与演化）、RP-004（授权）、RP-006（Harness）。所有建议均为待验证候选。

### 1. 从本体物化转向任务可完成性

由自然语言生成 Object / Relation / State / Rule 并物化为数据库，只说明构建了一种结构表示，不能证明业务语义完整、任务有足够事实、Action 具备执行约束，更不能证明结果有效。候选路线是 **Business Outcome / Task → Decision / Evidence Requirements → Semantic Model / Data Queries → Governed Action → State Feedback**；同时保留数据驱动、领域驱动的反向校验，不主张任何任务都必须建设 Ontology。

职责区分用于**诊断而非新增部署层**：Model 负责概率性判断；Context 是当前任务可用信息的运行时产物；Harness 负责任务循环、调用和状态组织；Ontology / Business 负责业务语义与能力映射。正式数据可由分布式 System of Record 持有，规则可由 Domain Service、Workflow、IAM、Policy 执行。统一业务语义不意味着物理集中事实、规则和执行权。

### 2. 三组候选语义接口（尚非标准 API）

| 接口 | 输入/输出问题 | 最小候选操作 | 边界 |
|---|---|---|---|
| Metadata / Discovery | 当前业务概念和能力有哪些？ | describe_object_type、list_available_actions | 需权限过滤、版本与适用范围；不要求把完整 Schema 放进 Prompt |
| Query / Facts | 此任务能读哪些对象、关系、状态和证据？ | search_objects、get_object、get_linked_objects | 按身份授权，返回来源、时间和事实版本；不能把检索缓存冒充权威现状 |
| Action / Capability | 能请求什么业务变化，结果如何？ | describe_action、validate_action、invoke_action、get_action_result | Model-facing Tool Schema 不等于服务器 Business Execution Contract |

**工作假设：** 治理后的机器可读定义（JSON Schema、DSL、元数据注册表、代码/规则组合等）可以按调用者需要投影成查询、文档、工具 Schema 与部分校验；但业务复杂逻辑和跨系统副作用仍需权威服务实现。是否采用 YAML、动态工具发现或独立语义服务，应由 POC 比较决定，不应提前选型。

### 3. Action Contract 与可信执行

Action 候选契约至少记录：业务含义、作用对象、参数、前置条件、授权来源、状态版本、审批要求、实现引用、幂等、结果/异常状态、审计与后置条件。模型只能**提出请求**；Harness 组织调用；服务器从可信凭据建立 actor / delegation 上下文，并在实际执行点再次执行权限、状态、前置条件和审批校验。

必须分别管理 **Ontology Schema Version**（契约兼容）和 **Object State Version**（并发状态）。对跨系统动作不假定原子事务；研究幂等键、乐观锁、Outbox、补偿、对账及人工接管。结果不能只有布尔值；至少需要区分 accepted、pending_approval、executing、succeeded、rejected、failed、partially_completed、unknown。**调用超时不等于未执行**；Dry Run 不可代替提交时校验。

### 4. 三层验证与四类故障诊断（不可混为一谈）

| 验证层 | 主要问题 | 判据 |
|---|---|---|
| L1 本体正确性 | 结构、语义、映射和约束是否反映目标业务？ | 专家走查、真实/脱敏样例、权威规则对照 |
| L2 任务可完成性 | Agent + Context + 查询 + Action 是否完成给定任务？ | 固定任务集、工具及动作轨迹、最终任务断言 |
| L3 业务结果有效性 | 执行后是否带来真实业务价值？ | 业务指标、试点对照和责任人复盘 |

定位 L2 失败时，选择最有区分力的实验：**T1 理想上下文**（隔离检索因素，不能证明模型全面可靠）；**T2 本体可表达性**（分别看 Schema、语义、数据映射、运行可获取性）；**T3 专家相同接口走查**（辨别任务/能力与 Agent 使用偏差）；**T4 绕过模型的 Action 正反请求**（权限、状态并发、重复提交、超时与审计）。记录任务/期望结果、实际 Context、来源与新鲜度、工具 Schema 和调用、Action 状态、版本及可见 Trace；不把不可观察的模型内部推理当证据。

模型/Agent 失败**不自动意味着本体错误**。本体变更根据不变量违反、证据强度、影响和最小修复路径决定，不设置“必须两个任务复现”的机械阈值。修复候选包括 Schema、实例、数据映射、Context 策略、Harness、Policy、Action 服务，而不是全部归入 Ontology Evolution。

### 5. Palantir 官方材料初步核查（产品事实与推论分开）

- **官方文档支持：** Ontology MCP 在 Developer Console 中把 Object Types、Action Types、Query Functions 作为 MCP 工具暴露，并区分供外部 Agent 使用的 Ontology MCP 与面向建设者的 Palantir MCP。来源：https://www.palantir.com/docs/foundry/ontology-mcp
- **官方文档支持：** Ontology MCP 继承应用 OAuth 2.0、范围限制及用户/服务主体的底层资源权限。来源：https://www.palantir.com/docs/foundry/ontology-mcp/authentication-and-authorization
- **官方文档支持：** Ontology 中 Object / Link 有代码绑定，Functions 可查询对象与关系；具体运行差异需分 API 版本核查。来源：https://www.palantir.com/docs/foundry/functions/functions-on-objects
- **研究解释，尚未验证：** 这些机制提示 Palantir 的差异不只是“有 MCP”，而是将语义、对象查询、函数、动作和授权联结为消费接口；不能据此推定自动建模质量、外部事务一致性、Webhook/Writeback 的全部语义或任意业务规则可自动执行。Action 类型、Webhook 副作用与一致性仍待更细官方资料核查和 POC。

### 6. 最小 POC 任务卡（合成场景，无真实监管规则）

模拟“检测结论和业务状态一致性检查；疑似异常生成复核任务”。预备合成 Object / Relation、两版定义、两版对象状态、权限角色、受控动作假实现和固定任务期望结果。

| 编号 | 输入与操作 | 预期可观察输出 | 失败判定 |
|---|---|---|---|
| P1 定义投影 | 修改 Action 参数并生成工具、校验和文档 | 差异报告、版本号、兼容性判断 | 三者不一致或旧客户端静默误用 |
| P2 查询语义 | 从任务要求查询对象、关系、来源 | 正确对象集、来源与事实时间 | 无法表达/查询，或访问未授权事实 |
| P3 动作控制 | 合法、非法、越权、状态竞争、重复和超时调用 | 明确拒绝/审批/执行状态、审计、幂等结果 | 绕过权限/状态检查或超时重复副作用 |
| P4 诊断 | 注入关系、映射、检索、Tool 描述、Action 故障 | T1–T4 对照轨迹及候选根因 | 将所有失败无依据归因本体 |
| P5 任务回归 | 先 3–5 个代表任务，扩大到 15–20 个 | L1/L2 断言及单独的 L3 指标草案 | Action 成功却误报业务目标完成 |

### 7. 未解决的研究边界与下一步

1. **官方资料：** Palantir 的 Actions、Functions、Webhook、Writeback、审批及副作用的执行边界，尤其与传统 Command / Domain Service / Durable Workflow 的差异。
2. **架构实验：** 固定工具 vs 动态发现；独立语义服务 vs 直接领域 API；模型可见 Tool Contract 与服务端完整契约的同步收益与成本。
3. **业务验证：** 任务驱动建模是否比仅描述对象的自然语言建模更能提升 L2 / L3，及 Action 粒度在复杂流程中何时越界。

本增量不改变 RP-002-04 的原有 H1–H4、Frontier、研究运行面或正式原则。避免与已有 H-RP002-07 编号出现混用：此处**不分配新 Hypothesis ID**；如后续独立建卡，先检查现有 ID 注册与冲突。

## 2026-10-20 增量｜语义优先的适用阈值与 Task Context 的真实可用性

**来源及状态：** 脱敏 Field Signal → Working Hypothesis Refinement；只细化已有 H1/H2 与 2026-10-12 接口验证，不新增 H-ID 或 Ontology 平台假设。相关的业务路线矩阵与 A/B/C 实验由 [RP-006 §13](RP-006-enterprise-agent-harness-runtime.md) 承载。

### 从本体定义到任务可用信息之间仍有缺口

`Ontology Definition ≠ Object Instance ≠ Authoritative SoR ≠ Task Context ≠ Agent Run State`。即使 AI 已生成 Object / Relation / Rule 并物化数据库，也不能由此推断：组织身份与成员实例正确、实时事实可查、用户有读取权限、业务动作可提交、任务验收已通过。

在合成申请场景中，应分别检验：

1. **Schema / Meaning**：组织、人员、项目及关系是否被表达且可区分业务差异；
2. **Source Binding**：当前实例来自哪个权威业务系统，是否有事实版本、更新时间和冲突解释；
3. **Task Resolution**：给定任务与身份，能否动态解析所需对象、属性、关联和证据；
4. **Authorized Access**：是否在查询/装配阶段按身份与 Policy 裁剪，不以提示词替代权限；
5. **Action Availability**：工具可见不等于可授权执行，业务服务仍要校验状态/委托/审批；
6. **Task vs. Business Outcome**：上下文回答正确、Agent 调用成功，与正式 SoR 状态和组织验收分别记录。

### 共享语义的候选收益不在单次 Schema 物化

| 条件 | 候选最小路径 | 语义资产何时值得扩张 |
|---|---|---|
| 单一领域、对象权威明确、应用/API 健全 | Domain Model/API + 直接授权事实查询 | 暂无证据时不建独立 Ontology |
| 两个以上应用对同一对象反复解释且定义冲突 | 对照共享 Domain Contract、数据字典和 Ontology | 后者对上下文组装、变更与治理的**净收益**可复现时 |
| 多 Agent 反复检索跨系统事实，且需要按任务裁剪 | 先优化可访问的查询/授权契约和任务映射 | 动态语义发现比显式 API 编排降低总成本时 |
| 现有事实来源不明、实例无权威性 | 先补 SoR / Source Mapping / 数据质量 | 不因语义平台存在就制造第二套“真相” |

**反向解释：** 复用共享 Domain API / Policy / Schema Registry 可能已足够；Ontology-first 在已有成熟语义资产及生成工具时也可能更快。应以 Task 2 新业务的增量开发、对象/连接器复用、语义错误、数据新鲜度、授权正确性、修改传播和维护总成本反驳，而不是以静态 Schema 数量证明价值。Ontology 与 Domain Model 可互补，不应被伪装成相互排斥的技术信仰。

此研究不把 Context Engine 定义为新层；只有发现稳定、重复、跨任务且难由已有 Domain API / Query Service / Agent Runtime 承担的 Context 组装义务，才研究独立部署的必要性。保留 RP-002-04 原有 H1–H4 和 Gap A/B/C 顺序。
