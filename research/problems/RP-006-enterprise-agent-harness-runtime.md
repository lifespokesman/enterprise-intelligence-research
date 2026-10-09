# RP-006｜Enterprise Agent Harness Runtime

Status: Candidate / Exploratory  
Created: 2026-09-29  
Primary Mapping: Q3 Human-Agent Coordination  
Related: Q2 Responsibility / Authority, Q5 Organizational Learning  
Derived From: RP-002-04 World Model → Task Context Runtime  
Related Problems: RP-002-02 Business Action Layer / RP-004 Effective Agency / RP-003 Agent Experience → Organizational Learning

> 核心问题：**当 Agent 从一次模型调用升级为需要持续观察、规划、调用工具、执行动作、保持状态、恢复任务并在受控环境中长期运行的执行主体时，企业需要什么样的 Harness / Agent Runtime 机制？这些机制与 Task Context、Business Action、Security / Governance、Execution Environment 以及 Runtime Feedback 应如何划分边界？**

本文件只登记一个新的候选问题域，不预设 Harness 已经是独立产品层、控制平面或统一技术类别，也不把任何具体厂商实现视为标准答案。

---

## 1. Trigger｜抽象后的现象

企业级 AI 交流中开始同时出现以下需求：

- 多种 Entry：Desktop / Web / Collaboration Client / API；
- Long-running Task 与 Session / Context 持续管理；
- Tool / MCP 调用、文件与代码执行；
- Sandbox / Execution Environment；
- Checkpoint / Resume / Failure Recovery；
- Master Agent / Sub-Agent / Parallel Task；
- Identity / Tenant / Policy / Approval / Audit；
- Runtime Isolation / Resource / Quota / Cost / SLA；
- 与 AI Gateway、Model Serving、GPU Runtime 和资源运营的衔接。

这些现象共同暴露出一个当前研究体系尚未直接回答的问题：

> **已有研究较多解释“Agent 看见什么 Context”“Agent 可以调用什么 Capability”“谁有权让 Action 发生”，但对“Agent 本身怎样作为一个可持续、可恢复、可隔离、可观测的执行系统运行”缺少稳定问题定义。**

公开仓只保留这一抽象 Trigger，不记录具体客户、企业、内部产品、资源配置或非公开技术路线。

---

## 2. Problem Placement｜为什么不继续塞入已有 RP

### 2.1 与 RP-002-04 的边界

RP-002-04 研究：

> World Model / Facts / Knowledge / Policy / Runtime 如何生成 Task-specific Context？

RP-006 研究：

> Agent 在取得 Context 后，怎样进入持续执行循环，并管理任务生命周期、环境、状态、并行、恢复与运行资源？

因此：

```text
RP-002-04
World / Facts / Knowledge / Policy
        ↓
Task Context
        ↓
RP-006
Agent Execution Lifecycle / Harness Runtime
```

Context 是 Harness 的重要输入与内部状态之一，但 **Context Engineering ≠ Agent Execution Runtime**。

### 2.2 与 RP-002-02 的边界

RP-002-02 研究：

> 企业允许哪些 Business Action，动作语义、状态约束、执行绑定和治理契约如何设计？

RP-006 研究：

> Agent 如何在任务执行过程中发现、选择、调用并协调 Tool / Capability / Action，以及如何处理长程执行、失败和恢复？

因此：

- Business Action 更接近 **受治理的业务状态改变契约**；
- Harness 更接近 **执行这些能力的 Agent lifecycle / orchestration runtime**；
- Tool / MCP 是二者之间可能使用的 capability exposure / invocation mechanism。

### 2.3 与 RP-004 的边界

RP-004 研究：

> 谁有权执行、什么条件下允许执行、Human Control 与 Accountability 如何配置？

RP-006 研究：

> 这些控制在实际 Agent 运行生命周期中如何被挂接和强制执行，但不重新定义 Authority / Accountability 本身。

因此 Identity / Policy / Approval / Sandbox Isolation 会同时出现在两边：

- **RP-004**：研究控制权与责任边界；
- **RP-006**：研究运行时如何承载 / 调用 / enforce 这些边界。

### 2.4 与 RP-003 的边界

RP-006 会产生：

- Trace；
- State Transition；
- Failure；
- Tool Result；
- Human Intervention；
- Cost / Resource；
- Outcome。

这些可成为 RP-003 的 Evidence Source，但：

> **产生 Runtime Feedback ≠ 已经形成 Organizational Learning。**

只有当运行记录经过 Eval、验证、治理并进入 Knowledge / Skill / Rule / World Model / Policy 等长期资产，才进入 RP-003。

---

## 3. Core Cognitive Questions

### CQ-006-01｜为什么需要 Harness？

> **Harness 相对于 Model API、Workflow、Agent Framework 到底新增解决了什么结构性问题？**

需要研究以下演化是否真实存在，以及边界在哪里：

```text
LLM API
→ Tool Calling
→ Workflow
→ Agent Loop
→ Long-running Agent
→ Harness / Agent Runtime
```

重点不是证明“越新越高级”，而是识别：

- 哪些任务只需要单次模型调用；
- 哪些适合确定性 Workflow；
- 哪些必须维护 Agent 的持续观察—判断—行动循环；
- Long-running / resumable / environment-coupled execution 为什么会产生新的 Runtime 问题。

### CQ-006-02｜Harness 是否存在稳定的不变量？

候选机制：

```text
Agent Loop
Context
Tool / Capability Access
Environment
State
Orchestration
Control Hook
Observability
```

需要验证：

1. 哪些是 Harness / Agent Runtime 的稳定职责；
2. 哪些属于 Context Runtime；
3. 哪些属于 Business Action / Capability；
4. 哪些属于 Enterprise Control Plane；
5. 哪些只是当前具体产品的实现选择。

---

## 4. Architecture Questions

### AQ-006-01｜Harness 与 Execution Environment / Sandbox 如何划分？

研究：

- Agent orchestration 是否应与实际执行环境解耦；
- Environment Provider 是否可以替换；
- Host / Container / MicroVM / Remote Sandbox 等模式分别解决什么问题；
- 文件、代码、浏览器、Shell、企业系统连接是否属于同一种 Environment abstraction；
- Context / State 应由 Harness 保存还是随 Environment 生命周期绑定。

当前不预设“解耦一定更好”。

### AQ-006-02｜Multi-Agent 应如何进入 Harness？

候选链路：

```text
Master / Coordinator
        ↓
Task Delegation
        ↓
Sub-Agent
        ↓
Independent Context / Runtime
        ↓
Result Aggregation
```

重点研究：

- Context isolation；
- Permission inheritance；
- Shared vs isolated state；
- Parallel execution；
- Failure propagation / recovery；
- Result aggregation；
- 子 Agent 是否需要独立 Environment / Sandbox；
- Multi-Agent 是 Harness 的核心能力，还是上层 application / orchestration pattern。

### AQ-006-03｜Entry 与 Harness 是否应解耦？

研究：

```text
Desktop / Web / Collaboration Client / API
                    ↓
             Harness Runtime ?
```

需要验证：

- 多入口是否真的要求统一 Session / Task Runtime；
- Entry 负责交互，Harness 负责执行是否具有稳定边界；
- Personal Agent 与 Enterprise Agent 在 identity/session ownership 上是否存在不同模式。

---

## 5. Engineering Question

### EQ-006-01｜个人 Harness 企业化后新增了什么结构性工程要求？

候选集合：

```text
Identity
Tenant
Permission
Policy
Approval
Sandbox Isolation
State Persistence
Checkpoint / Resume
Failure Recovery
Resource / Quota
Audit
Cost
Operation / SLA
```

研究目标不是整理功能清单，而是判断：

> **哪些要求来自企业规模、责任边界、共享基础设施与持续运营，而不是 Agent Loop 本身。**

同时需要区分：

- Harness-owned responsibility；
- External control-plane service；
- Infrastructure / platform responsibility；
- Business Action / domain responsibility。

### EQ-006-02｜Harness 与 AI Infrastructure 的资源边界是什么？

需要研究 Agent Runtime 如何与：

- AI Gateway；
- Model Routing；
- Model Serving；
- GPU / Accelerator Runtime；
- Token / Cost Metering；
- Resource Scheduling

发生连接。

当前只登记为工程边界问题，不预设 Harness 应直接拥有模型服务或 GPU 调度。

---

## 6. Validation Question

### VQ-006-01｜不同任务应选择什么 Harness Runtime Pattern？

候选变量：

```text
Task Type
× Task Duration
× Action Risk
× Execution Environment
× Parallelism
× State Persistence
× Isolation Requirement
× User / Tenant Scale
× Resource Model
→
Harness Runtime Pattern
```

需要验证：

- 这些变量是否足够；
- 哪些是主变量，哪些高度相关或可合并；
- 是否存在无需 Harness 的任务区域；
- 是否存在必须 Durable / Isolated / Distributed 的任务区域。

长期目标是形成：

> **Business Outcome / Constraint → Task Characteristics → Capability Requirements → Runtime Pattern**

这里必须先判断任务是否需要 AI；即使需要 AI，也未必需要 Agent。候选基线应同时包含：单次模型调用、确定性规则/算法、固定 Workflow、简单 Agent Loop、持久化/隔离式 Harness。不同实现不是线性“技术成熟度等级”。

为了避免从“Agent 名称/入口”推断架构，需要在同一任务上记录 Task Complexity、Duration、Environment、Freshness、Data/Tool Dependency、Risk/Reversibility、Authority、Human Responsibility，并检查它们能否预测必要的 Model / Harness / Context 配置。

**三层评估（仅为可检验的候选映射）：**

- Technical：模型/工具/上下文的正确性、成本、时延、Token 等；
- Task / Operational：端到端任务完成率、恢复率、人工接管、越权/重复操作、交付周期；
- Business Outcome：在成本、质量、风险、时效或用户服务等业务约束下的净改善。

需要对照非 AI 约束与基线流程，不能把“模型 Benchmark 提升”或“Agent 局部成功”自动归因为业务改善。对于低风险标准化任务，轻量任务指标可能已经足够，避免制造复杂归因体系。

而不是寻找“一套所有场景通吃的 Harness 平台”。

---

## 7. Working Hypotheses｜全部待验证

### H-RP006-01｜Harness as Controlled Agent Execution System

> Harness 的稳定价值可能不在于提供更多 Agent 功能，而在于把概率性的模型行为组织成一个可以持续观察、判断、调用能力、执行动作、保持状态、恢复失败并接受外部控制的执行系统。

**Counter-hypothesis**：这些职责可能只是 Workflow Engine、Application Runtime、Tool Layer 与 Sandbox 的组合，并不存在独立 Harness abstraction 的长期必要性。

### H-RP006-02｜Harness / Environment Separation

> 较成熟的实现可能倾向于把 Agent orchestration lifecycle 与具体 execution environment 分离，使 Host / Container / MicroVM / Remote Sandbox 可以按任务替换。

**Counter-hypothesis**：对大量个人生产力与低风险任务，Harness 与本地环境紧耦合可能更简单、更高效，抽象 Environment Provider 反而增加成本。

### H-RP006-03｜Enterprise Complexity Is Mostly Control + Operations

> 企业 Harness 相比个人 Harness 的主要复杂度增长，可能更多来自 Identity、Tenant、Policy、Isolation、Persistence、Recovery、Quota、Audit、Cost 与 SLA，而不是 Agent Loop 本身。

**Counter-hypothesis**：复杂企业业务本身可能显著改变 planning / memory / multi-agent / environment model，不能把企业化简单理解成“个人 Harness + 控制平面”。

### H-RP006-04｜No Universal Best Harness

> Harness Runtime Pattern 可能由 Task Duration、Action Risk、Environment、Parallelism、Persistence、Isolation、Scale 与 Resource Model 等变量共同决定，不存在统一最佳实现。

该假设需要通过公开实现与反例建立更小、更稳定的决策变量集合。

**2026-10-09 增量限定（WH-A）**：原假设已经覆盖 Task-driven 配置，不新增平行 H。将 Information Dependency、Identity / Responsibility 与 *AI Applicability* 作为待测变量；反向解释是通用模型 + 标准 Runtime + 少量配置足以覆盖主要场景。必须用同任务多实现对照决定是否需要复杂分类。

### H-RP006-05｜Model Capability Shift vs. Stable Execution Constraints（新增，待验证）

> 随着模型能力提升，部分补偿性 Harness / Context 脚手架（固定细步骤、频繁上下文重置、重复人工组织上下文、冗余模型自评）可能降低边际价值，甚至被删除；但持续状态、外部事实、执行环境故障、实际授权、可强制的控制与审计等需求不会只因为模型更聪明而自动消失。**系统约束持续存在，不代表必须由名为 Harness 的独立组件承担。**

**Counter-hypothesis**：更强模型与原生 Agent 平台可能进一步吸收这些职责，使应用侧 Harness 简化；也可能因更复杂的新任务产生更多 Harness 机制，而非整体减少。

**Falsifiable predictions / V1**：

1. 在可比较任务与验收口径下，升级模型后应能删除至少一类补偿性机制而不明显损失任务质量；若删除后持续退化，应保留该机制。
2. 即使更换模型，发生进程中断、审批等待、权限撤销或真实系统状态更新时，仍需可测试的外部状态 / 控制来源；但可由既有 Workflow、Policy、Application 或托管平台承载。
3. 发现“模型升级即可替代外部持久状态/授权强制执行”的可复现案例，应收窄本假设；发现复杂任务扩展反而增加外部机制，也应记录为边界而非反例失效。

**WH-C｜共享能力的条件性假设（暂不单独编号）**：模型接入、权限、Context 检索/选择、工具适配、评估等可能在多 Agent 之间复用；但安全域、数据主权、时延、自治、故障域可能使局部专属实现更优。与 H-RP006-03、H-RP006-04 和 RP-002-04 共同研究；不预设共享平台必然获益。

**WH-D｜业务结果评估（暂不单独编号）**：作为 VQ-006-01 的跨层测量要求，结果反馈后续关联 RP-003 / Q5；避免把组织学习问题复制成 RP-006 新问题。

---

## 8. Relationship Map｜与现有研究体系的关系

当前只登记关系，不强行升级为新的 Layer：

```text
Enterprise Reality
        ↓
RP-002 World Model / Semantic
        ↓
RP-002-04 Task Context
        ↓
RP-006 Harness Runtime
        ↓
Tool / Capability Exposure
        ↓
RP-002-02 Business Action
        ↓
Enterprise World Change
        ↓
Runtime Trace / Outcome / Failure
        ├─→ RP-002-01 World Model Conflict & Evolution
        └─→ RP-003 Organizational Learning

Cross-cutting control:
RP-004 Authority / Policy / Human Control / Accountability
        ↓
applies across Context / Harness / Tool / Action / Environment
```

这里最重要的边界是：

- **Context**：当前任务应该让 Agent 看见什么；
- **Harness**：Agent 如何持续运行；
- **Business Action**：企业允许 Agent 以什么业务语义改变世界；
- **Governance / Authority**：谁允许什么在何种条件下发生；
- **Organizational Learning**：运行经验如何升级为长期组织资产。

---

## 9. Evidence Provider Rule

后续如果正式研究，不建立“Codex 研究 / OpenHands 研究 / WorkBuddy 研究”等产品主线。

产品、开源实现、论文、标准和案例只作为 Evidence Provider，用来回答 CQ / AQ / EQ / VQ。

首轮证据至少应覆盖：

- Open-source implementation；
- Product architecture；
- Engineering blog；
- Academic paper；
- Standard / specification；
- Enterprise case；
- Counter evidence。

所有公开结论必须由公开证据独立支撑。

---

### 9.1 V1｜模型升级导致 Harness 职责迁移：公开材料初核（2026-10-09）

**初步发现（不是充分验证）：** 至少存在一例工程作者报告：模型变强后删除了此前为弥补模型长程能力不足而设置的部分 Harness 结构；另外几类持久化/恢复机制继续以外部软件形式被提供。它支持“逐项重测机制必要性”，尚不能证明任何机制是永久不变量。

| 公开来源 | 具体事实 / 机制 | 对 H-RP006-05 的作用 | 证据限制 |
|---|---|---|---|
| [Anthropic, Harness design for long-running application development, 2026-03-24](https://www.anthropic.com/engineering/harness-design-long-running-apps) | 工程作者报告从 Sonnet 4.5 到 Opus 4.5 后，不再使用原先的 Context Reset；在使用 Opus 4.6 更新 Harness 时取消 Sprint 分段，将评价改为完成后执行。Planner 仍然保留，Evaluator 对部分前沿任务仍有收益。 | **Supports / Narrows**：已有实际删除、简化机制及保留机制的同案对比。 | 作者自述、任务/模型/结构不完全恒定；“删除可行”不等于证明由模型升级单独导致，更非企业生产验证。 |
| [LangGraph Persistence 文档](https://langchain-ai.github.io/langgraph/concepts/durable_execution/) | Checkpoint 保存 Thread State，支持中断恢复、人审等待和容错；Store 用于跨线程持久记忆。 | **Supports requirement; not architectural exclusivity**：显示需要外部持久状态的一种实现。 | 说明产品实现存在，不证明所有 Agent 都需要该机制，更不证明 Harness 必须自行建设。 |
| [OpenAI Agents SDK, Running agents](https://openai.github.io/openai-agents-python/running_agents/)；[Temporal Durable AI](https://docs.temporal.io/ai) | Agents SDK 文档将跨等待/进程重启的 Durable Orchestration 交给 Temporal、Dapr、Restate 等集成；Temporal 描述故障恢复及等待人工批准后的继续执行。 | **Opens alternative**：稳定的是故障恢复需求，所有权可在外部 Workflow / Durable 服务，不必属于独立 Agent Harness。 | 官方实现说明，不构成模型升级前后 A/B；可靠性能力的宣称仍需故障注入复核。 |

**目前不能得出的结论：** Model×Harness×Context 是独立三层或严格乘积；更强模型一定减少 Harness 总体规模；持久化机制必须由单独的 Agent Runtime 拥有；Agent 成功等于业务收益。

**下一验证动作（V1 最小复现）：** 固定同一任务、模型工具、数据快照、验收口径，交叉比较两个模型版本与“完整 Harness / 删去单一补偿机制 / 仅保留必要持久化和控制”的配置；分别执行上下文溢出、进程中断、工具失败、权限撤销。记录成功率、恢复能力、人工干预、成本与错误副作用，公开来源不足以做归因时标为待验证。若 V1 缺少真正的模型×Harness 消融对照，不升级 H-RP006-05。

---

## 10. Current Stop Point｜本轮只登记问题

本轮完成：

```text
Trigger
→ Existing Problem Check
→ Problem Boundary
→ CQ / AQ / EQ / VQ
→ Working Hypotheses
→ Relations
→ Next Research Plan
```

本轮不做：

- 不启动 Research Runner；
- 不批量创建 Evidence Card；
- 不改变 Human Frontier；
- 不改变 Automation Frontier；
- 不新建 Topic；
- 不修改 JUDGMENTS.md / PRINCIPLES.md；
- 不把 Harness、Agent Server、ACI、Dynamic Sandbox 等术语直接升级成架构层。

---

## 11. Next Research Step

如果后续启动 RP-006，只推进第一组最小证据问题：

> **先验证 Harness 是否存在稳定不变量，以及 Harness / Execution Environment 是否存在跨产品、开源实现与工程文献都可识别的边界。**

第一轮可以选择少量公开实现作为 Evidence Provider，例如 Codex、DeepSeek Harness、OpenHands 等，同时必须加入至少一种不同实现路线与 Counter Evidence。

2026-10-09 的增量研究输入已路由到现有 RP-006 / RP-002-04：先用上文 V1 验证补偿机制是否随模型升级迁移，作为既有“稳定职责与 Environment 边界”研究的一个可证伪切口；后续再用 VQ-006-01 做不同任务的实现对照。V1 的初核只形成 Evidence Lead，不改变当前 Frontier，也不启动 Research Runner。

在这一步之前，不展开完整 Multi-Agent、Enterprise Control Plane 或 AI Resource Operation 研究。


---

## 12. Cross-cutting Boundary｜Harness 是认知执行中心，但不是最终权威

RP-006 与 RP-002-02 新增的 `H-RP002-07｜Enterprise Control Anchors` 形成一个重要边界：

> **Harness 可以承载 Agent 的持续观察、理解、判断、规划和工具调用，但不应因此默认成为企业正式事实、授权规则、过程承诺或最终责任的唯一权威。**

候选分工：

```text
System of Record
= Reality Anchor

Policy / Authority
= Constraint Anchor

Workflow / Durable Execution
= Commitment / Execution Anchor

Human / Organization
= Accountability Anchor

Harness / Agent Runtime
= Cognitive / Adaptive Coordination
```

这一关系为 `CQ-006-02｜Harness 是否存在稳定不变量？` 增加一个反向判断标准：

> **如果某项职责要求成为跨 Agent、跨模型、跨会话仍然有效的正式企业事实、约束、承诺或责任，它更可能属于 Harness 外部的权威机制，Harness 负责读取、调用、enforce hook 或记录，而不应自动拥有其定义权。**

但这仍需验证。AI-native 系统可能把 Workflow、Policy Enforcement、State Store 等机制内嵌进统一 Runtime，因此“逻辑职责分离”不等于“必须物理组件分离”。

后续研究 Harness 时应额外检查：

- Harness-owned state 与 authoritative business state 是否混淆；
- Agent plan 与 durable commitment 是否混淆；
- Prompt instruction 与 enforceable policy 是否混淆；
- human approval UI 与真正的 delegated authority / accountability 是否混淆。

---

## 12. 2026-10-09｜需求侧增量：Business Task 与 Agent 执行组织（Working Hypothesis，非新 Problem）

### 12.1 为什么属于 RP-006

本轮将 VQ-006-01 的 `Business Outcome / Constraint → Task Characteristics → Runtime Pattern` 进一步检验为一个**架构选型方法**，不将「任务中心平台」预设为新基础设施，也不覆盖既有 H-RP006-04、H-RP006-05。相关：RP-002-04（Task Context）、RP-002-02（Action）、RP-004（Authority）、Q3（协调）。

### 12.2 关键主体概念与关系矩阵

| 主体 | 职责／解决的问题 | 常见实现／关系 | 独立建设是否必要／替代方式／争议 |
|---|---|---|---|
| Business Application | 领域交互、规则、事实与权威状态；承接业务责任 | SoR、领域服务、API；可发起/验收任务 | 既有企业常必需其**能力**，但不必新建应用；不能一概退化为 Agent Tool |
| Agent | 对不确定目标动态判断、选工具和行动 | LLM+工具+循环；在 Harness/Workflow 内执行 | 可用规则、单次 LLM、服务或人工替代；不自动拥有审批权 |
| Agent Harness | Agent 循环、上下文装配、工具调用和控制钩子 | SDK loop、代码、图状态机；调用 Runtime 能力 | **功能条件性必要**；与 Runtime 重叠，不等于必须独立服务 |
| Agent Runtime | 执行状态、隔离、持久化、恢复、并发与资源 | SDK、Workflow、容器/沙箱、托管服务 | 对短任务可轻量内嵌；对长任务可复用既有 durable engine |
| Agent Workspace | 人机任务可视化入口；或执行文件/代码的工作空间（需拆分） | 业务 UI/任务列表；沙箱/文件系统 | 两种 Workspace 不同义；无需统一 Agent 门户 |
| Master-Agent | 开放任务的规划、委派和综合 | manager-as-tool、动态 handoff、代码 orchestration | 可选模式；不能因「Master」自动取得业务授权 |
| Sub-Agent | 隔离上下文、专业处理、并行子工作 | as-tool、handoff、worker | 仅在专业化/并行收益超过协调成本时使用；可用函数/服务替代 |
| Workflow（关键对照） | 已知业务过程、等待、人审、持久协调 | BPMN / durable workflow | 不是新 Agent 组件；Agent 可作为流程内局部活动 |

**四种关系不可混同**：业务关系（责任与权威状态归 Business Owner/SoR）、执行关系（Agent 或 Workflow 组织任务）、运行关系（Harness/Runtime/Workflow 可复用基础设施）、治理关系（Policy/Identity/Approval/Audit 的真实强制执行点）。Tool invocation 是技术调用，不等于通过业务前置条件、授权、事务及审计后的正式业务变更。

### 12.3 五个身份／生命周期对象（候选词汇，不要求统一模型）

- `Business Task`：业务目标、结果验收、责任归属、风险与状态；可由人、流程、系统、Agent 混合完成。
- `Workflow Instance`：一个明确流程定义的一次持久执行；可承载一个任务或多个业务任务。
- `Agent Definition`：策略、模型、工具与执行配置模板；不是运行中的主体授权。
- `Agent Instance / Run`：某一执行主体及一次具体执行尝试；一个业务任务可跨多个 Run、重试、人工等待。
- `Session`：对话／记忆连续性标识；跨轮上下文不等于业务任务的权威状态。各产品对 Instance/Run 的命名不一致，此处仅用于比较。

### 12.4 需求侧任务分类与最低充分实现（Working Analysis）

| 任务情形 | 最低充分候选方式 | 何时追加机制 |
|---|---|---|
| A 确定性查询／写字段 | 现有 App / API / Rule / Command | 无须默认 Agent；写入遵守现有 Policy 与 SoR |
| B 知识／认知分析 | 搜索/RAG + LLM，必要时单 Agent | 需要多轮工具选择、环境操作才用 Harness |
| C 固定流程的智能判断 | BPMN/Workflow + AI 节点 | 判断局部开放时嵌 Agent；流程审批权不随之迁移 |
| D 开放多步骤研究／执行 | 单 Agent + 轻量状态管理 | 复杂并行/专业隔离的净收益明确时才 Master/Sub；长程运行才加 durable |
| E 长期事件触发／高风险跨系统任务 | Event + Workflow / Domain App + 受限 Agent | 引入幂等、补偿、审批、跨系统审计与恢复；只有既有设施不能承载时再研究独立 Task Control |

**建议的需求侧推导顺序**：Business Goal → Accepted Outcome → Constraint / Risk → AI Applicability → Business Task → Execution Requirements → Organization Pattern → Technical Capabilities。此为**分析流程而非规定平台拓扑**。

### 12.5 H1–H6 对既有假设的映射与反驳路径

| 本轮候选 | 映射／治理判断 | 边界与反证 |
|---|---|---|
| H1 Task 比 Agent 更适合需求侧入口 | 精炼 VQ-006-01 与 H-RP006-04，不新增 H | 简单问答的 Task 抽象仅增加负担 |
| H2 Business Task ≠ Run / Session / Workflow Instance | RP-006 生命周期 × RP-002-04 Task Context；保留 Working Hypothesis | 单次短调用可一一对应，无需独立存储 |
| H3 Master ≠ Business Authority | RP-004 Authority + AQ-006-02；不新增 H | 业务明确授权的 Master 可以发起受限写动作，但授权来自外部 |
| H4 Harness ≠ Business Workflow / SoR | H-RP006-01/05 + RP-002-02；既有边界精炼 | 同产品可以承载多项职责，不强制物理拆分 |
| H5 Workspace 非唯一入口 | AQ-006-03；不新增 H | 人机协作密集场景工作台仍有价值 |
| H6 关键可能是 Control / Execution / Authority / Accountability 分离 | RP-004 × RP-006 跨问题关系；仅作为治理假设 | 当业务规则简单且低风险，分离为新控制平台没有净收益 |

### 12.6 四个反例与平台化停止条件

1. **简单知识问答**：一次检索与模型输出即可；统一 Business Task 平台通常是重新包装。
2. **成熟 BPM 审批**：BPM 已有状态、人审与稽核，AI 只做局部判断；新 Task Controller 极可能重复建设。
3. **研究型 Agent**：结果是报告，无正式业务状态写入；Harness + 版本化产物/验收常已充分。
4. **跨系统高风险长期任务**：有多次 Run、审批、部分失败与业务写入；需要跨参与者的 task correlation、权限、幂等、恢复、验收，但可以首先复用既有 Workflow/SoR，不直接推出独立平台。

**候选采用阈值**：只有跨系统任务无法被既有流程一致标识和追踪、存在多执行者长等待/责任交接、严格证据与审计一致性要求，且复用收益能覆盖新组件维护、迁移与治理成本时，才考虑独立任务治理层。技术委派**永远不等于**业务授权转移，Agent 宣称完成**永远不等于**业务验收完成。

### 12.7 小样本原始资料校验与证据限制（2026-10-09）

- [OpenAI Agents SDK — Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)：LLM/代码编排并存，manager-as-tool 与 handoff 是两种可选模式；**产品机制证据**，非 Master 必需性证明。
- [OpenAI Agents SDK — Running agents](https://openai.github.io/openai-agents-python/running_agents/)：Session/continuation 有不同状态路径；跨等待恢复提供 Temporal、Dapr、Restate、DBOS 集成；**反对 Harness 必须独占 durable orchestration**。
- [Camunda — AI agents](https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/)：LLM 选工具，BPMN 执行活动/重试/人工任务；**支持 Workflow 内含 Agent 的替代路径**，不证明企业实际 ROI。
- [LangGraph — Thinking in LangGraph](https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph)：checkpoint + interrupt + resume 展示另一种长任务组织方式；只证明实现可行。
- 仓内已有：RP-002-02 的 GAP-001 传统 Service/Command/Workflow 对照；RP-006 的 H-RP006-05 模型/Harness 机制迁移；RP-002-04 的任务上下文变量。以上均不能支持「统一 Task Control Plane 是行业必需品」。

**待补证据**：跨企业案例中谁拥有任务正式状态、授权撤销后委派是否仍执行、业务验收与 Run 完成率差距、独立 Task Controller 对可靠性和总成本的净增益。禁止在缺这些对照前升格 Judgment/Principle。

**最小可证伪比较**：同一跨系统任务对比 (A) BPM + AI 局部节点、(B) 单 Agent + domain APIs + durable integration、(C) 独立 Task Controller + Agent；固定业务验收与权限规则，测端到端完成、重复副作用、审批/恢复、审计缺口、开发与运维成本。对简单问答与报告任务做负例控制。

**治理决定**：本轮不新建 RP、H 或 Research Plan；不改变 Q3 身份、RP-002-01 人工 Frontier、RP-002-02 Runner、H-RP006-04/05 既有结论状态；后续仅在对照证据显示无法被既有问题解释时重新判断。
