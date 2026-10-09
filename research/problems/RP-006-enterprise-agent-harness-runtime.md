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
