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
