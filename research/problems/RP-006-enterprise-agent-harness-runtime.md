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

## 13. 2026-10-20｜从业务结果选择应用、语义与任务执行路径（Field Signal → Working Analysis）

**本轮实质修正：** 既有 §12 已要求以 Business Task 而非 Agent 产品作为需求侧入口，但尚未充分区分**产品/需求起点、业务能力生产与复用、交互方式**。把「先建 Ontology」「先生成 App」「优先聊天」说成两三套互斥架构，会混淆不同决策：Task-first 不是纯 Agent，Application-first 不是手工编码，Ontology 也是可选的软件工程能力，Domain Model 同样具有语义。本增量**不推翻 §12 的 Task-driven 选型，而是扩展其选择空间**；不主张行业通用优胜路线。

### 13.1 三个独立决策维度及权威边界

| 决策维度 | 候选路线 | 不应推导出的结论 |
|---|---|---|
| 需求与产品组织 | **Task-first**：先定义结果、约束、最小交互；**Application-first**：优先确立领域应用的完整生命周期 | Task-first ≠ 对话入口 / 独立 Agent；应用优先 ≠ 不考虑任务 |
| 能力生产与复用 | **Semantic/Ontology-assisted**：跨应用对象、关系、规则与事实绑定；**Domain-engineering-first**：领域状态、服务、命令、稳定 API | Ontology ≠ DB Schema；Domain Model ≠ 无语义；两者可混合 |
| 交互与执行入口 | 自然语言 / 核验卡片、表单、统一待办、批处理、事件、既有系统 UI | 自然语言 ≠ Ontology；同一任务的不同动作可使用不同入口 |

**Runtime Pattern** 是以上判断在 Task Duration、Risk、State、Authority、Isolation 等约束下进一步得到的配置，不是第四个必须独立建设的平台。一个可行组合是：**Task-first 交互设计 + Application/SoR 权威后端 + 按需 Semantic Task Context + 局部 Agent**。

建议的需求侧推导（待验证）：

`Business Outcome → Accepted Result → Constraints / Risk → Task / Decision / Action Decomposition → Human / Deterministic Software / Agent Allocation → Minimum Sufficient Capabilities → Interaction & Runtime Pattern → Validation`。

**判定顺序：** 先确认是否需要正式记录/写入、权威事实源、审批/责任；再检查既有 Domain API / Workflow / IAM 是否可复用；只有跨系统同义冲突、重复建模与动态 Context 成本可测时才考虑扩大共享语义资产。Agent 的一次 Run 成功不等于正式业务验收。

### 13.2 按业务模式的最小充分路线矩阵（候选，非选型标准）

| 场景与约束 | 起始路径 | 不优先引入 / 后续触发条件 |
|---|---|---|
| 单次资料研究、无正式写入 | 检索 / LLM + 人工核验 | 不先建 SoR / Ontology / 持久 Agent 平台；有长期状态责任再升级 |
| 低频、资料非结构化、目标清楚 | Task-first 辅助整理 + 原系统 API / 表单 + 核验卡片 | 不强制纯对话；无正式状态时先补最小 Domain Service |
| 高频、规则稳定、可批量 | 规则 / Workflow / 确定性应用优先 | 不逐笔使用 Agent；出现跨系统语义分歧才补共享映射 |
| 单部门独立申请 / 工单 / 费用业务，长期正式记录 | 最小 Domain App / SoR + 受控 API；Agent 可选 | 不预建全企业 Ontology；第二应用重复对象/规则再检验抽取 |
| 已有成熟业务系统，界面难用或材料难输入 | 原 SoR + AI 预填 / 查询 / 异常辅助 | 不新造第二份业务状态；只在跨域事实冲突时增语义能力 |
| 多应用共享人员/项目/资产，但定义冲突 | 共享领域契约/语义映射 + 源系统绑定 + Task Context | 若既有领域 API / 数据字典足够，不建设独立 Ontology 平台 |
| 无可信事实源，又需要正式审批写入 | 最小 Domain Service + IAM / Workflow，再选择 AI 入口 | Agent 对话不能自行创建具有正式效力的权威事实 |
| 高风险跨部门、长等待、部分失败 | 现有 SoR + Policy / IAM + Durable Workflow + 受限 Agent | 不让 Harness 独占审批/状态；跨域复用显著才加语义 / Action 契约 |

**停止扩张规则：** 第一条业务路径尚未完成、源系统不可确定、复用收益不清时，不扩大 Ontology；多个应用尚未出现重复语义/接口成本时，不急于建设共享层；批量/确定性方式已更好满足 SLA 时，不为使用 AI 而增加对话或 Agent Loop。平台沉没成本、政策与迁移成本也可能使理论上的最轻路线并非实际最低总成本。

### 13.3 Human / Software / Agent 按动作分工，不按流程贴单一标签

| Task / Decision / Action | 候选执行者 | 必须保留的控制点 |
|---|---|---|
| 非结构化意图与材料整理 | Agent 或人 | 来源、缺失信息、人工核验 |
| 字段合法性、金额/公式、状态前置条件 | 确定性软件 | 版本化规则、测试、服务端重验 |
| 行为身份和委托范围 | IAM / Business Authority | 服务端鉴权、最小权限 |
| 正式业务提交 | 用户显式确认 + Domain Command / Action | 可见后果、幂等、状态与授权校验；确认本身不是授权 |
| 审批人归属、等待、超时、恢复 | Workflow / Durable Service | 过程权威状态、关联与审计 |
| 审批结论 | 获授权人或制度允许的自动化规则 | 责任锚点，不由 Agent 声称批准 |
| 异常解释与建议 | Agent + 人 | 置信边界、升级通道 |
| 正式对象/交易状态 | SoR / Domain Service | 并发、一致性、可追溯 |

本表只按职责分工，**不强制物理拆分组件**。低频审批宜复用统一待办，专业复杂审查可再考虑嵌入 AI 辅助；页面是否减少由完成效率、差错与用户选择决定，不预设“聊天替代页面”。

### 13.4 三路线、双任务反驳实验（不新增 Research Plan）

用公开/合成数据，固定模型与算力预算、后端与制度规则、风险约束、UI 最低可用性、身份和审批验收，以及共同测试环境。**任务 1**：独立申请，有创建/确认/审批与状态追踪；**任务 2**：另一领域应用复用相同组织、人员、项目对象，并故意引入一个可解释的语义差异。

- **A｜Domain App-first**：Domain App / SoR / API → MCP/Tool → 可选 Agent；
- **B｜Semantic-first**：共享语义对象、事实与规则映射 → Task Context / Action 映射 → 应用 / Agent；
- **C｜Hybrid-on-demand**：先做 Task 1 最小领域闭环；Task 2 出现重复/冲突后才抽取共享语义或领域契约。

三组均需实现**相同正式业务结果与治理要求**，不能只拿 A 的生产就绪系统对比 B 的 Schema 原型。分开计量应用生成、身份/审批/通知接入、集成调试、测试与持续维护，比较：

1. 首条**真实可完成的业务闭环**耗时、人工专家介入与返工；
2. 越权/审批绕过、重复副作用、状态未知和故障后恢复；
3. 第二应用对象/接口/语义复用率、冲突和跨团队协调成本；
4. 规则升级后变更半径、回归结果与总维护成本；
5. 用户实际完成时间、差错、核验负担与对话/表单/批量偏好；
6. Agent Run 成功率与 SoR 业务验收成功率是否发生分离。

**反证与架构收缩：** 若 A 在两个任务中相同或更好、Domain API + Policy 足够，则不引入独立 Ontology；若 B/C 仅在 Task 2 起显著降低可复现总成本，才讨论共享语义规模化；若对话更慢或更易误确认，不以聊天实现 Task-first；若所有路线主要耗时均来自标准身份、流程、待办、通知接入，则优先研究**应用集成契约和示例工程**而非新 Runtime/Plane。

**证据与归属：** 这是从脱敏 Field Signal 抽象的 Working Analysis / 实验设计，不是公开 Evidence 或生产 ROI。Semantic / Context 边界由 [RP-002-04](RP-002-04-world-model-to-task-context.md) 持有；Domain API、Action 与应用集成契约由 [RP-002-02](RP-002-02-business-action-layer.md) 持有；Authority 属 RP-004；任务运行选择及本矩阵由 RP-006 持有。复用既有 GAP-004 的治理故障测试，不把它改写为三路线完整实验结果；下一步先在 Task 1 测出完整闭环，再用 Task 2 检验共享语义的边际收益。不新增 RP/H-ID、平台层，不改 Frontier 或 Runner。
## 14. 2026-11-06｜从业务对象与执行主体倒推企业 AI 基础架构（Cognitive Reframing / Working Analysis）

**来源与证据等级**：抽象的需求侧思考（User Input / Inference / Hypothesis），不是公开工程事实、产品事实或已验证行业共识。本节精炼 §12–§13 的 `Business Outcome → Task Characteristics → Minimum Sufficient Capabilities`，不新增 RP/H-ID、独立技术层或正式架构原则，也不改变 RP-002-01 人工研究前沿、RP-002-02 Runner。

### 14.1 真正新增的分析问题与此前已覆盖的部分

**已被既有研究覆盖**：
- §12 已把 Business Task 定位为需求侧分析对象，不预设 Task Platform；一个 Task 可由 Human / Software / Agent 协作完成；
- §13 已把 Task-first、Domain Application、Semantic/Ontology、交互入口拆成可独立选择的维度；
- RP-002-04 已要求由 Task / Risk / Information Dependency 推导 Context，并允许无独立 Ontology 的轻量路线；
- RP-002-02 已区分 Business Action 与传统 Application Service / Command / Workflow，不预设新 Action Runtime。

**本次待检验增量**：传统基础架构规划通常把 Application/业务系统工作负载及其治理作为主要输入；出现 Agent 类型的执行工作负载后，是否应进一步显式区分**业务世界中需要完成什么**与**信息化运行世界中由谁、用什么机制提供和执行能力**，从而把 AI 能力选型变为可解释的需求推导，而非预设“智算/本体/Harness/Agent 平台”清单。

**重要修正**：“Application 与 Agent 是企业两类并列且互斥的本体对象/执行主体”这一说法过强。Agent 本身可能实现为一个 Application、嵌入既有应用、由 Workflow 调度，甚至只是短时模型调用。更适合把 **(a) 业务执行角色** 与 **(b) 软件/运行时工作负载** 作为相交但不等价的两个轴。Application 既可能是被动的 Capability Provider / SoR，也可能通过事件和规则主动执行；Agent 的自主性也受任务、授权和运行环境约束。

### 14.2 候选概念边界（不是统一强制本体）

| 概念 | 研究中用于回答的问题 | 应避免的混淆 |
|---|---|---|
| Business Object / Event / State | 哪类现实业务事物发生了什么变化？ | 业务对象不等于数据库表；实例变化不等于 Ontology Evolution |
| Business Outcome / Acceptance | 什么才算业务成功，谁有权验收？ | Agent Run 完成不等于业务成功 |
| Business Task | 为结果需要完成哪一项可界定的工作？ | Task 可能随组织重构变化，不必成为统一任务平台的持久实体 |
| Business Action / Policy | 允许对业务对象请求何种改变，受什么约束？ | Action definition 不等于可执行 API / 已获授权 |
| Human / Business Owner | 谁负责判断、授权、验收与后果？ | 有人点击确认不等于权限天然合法 |
| Application / Domain Service / Workflow | 哪些既有系统提供事实、规则、命令和确定性协调？ | 不应将所有 Application 统称自治 Execution Actor |
| Agent / Agent Run | 哪些开放性判断或任务操作需要模型主导的执行循环？ | Agent 是软件形态/执行角色，不自动取得业务责任 |
| IT Operational Object | 哪些应用实例、Agent definition/run、模型部署、工具、资源和策略需要运维？ | IT 运行资源 ≠ 现实业务对象；目录 ≠ 权威运行态 |

**候选术语约束**：
- `Execution Actor` 仅在主体确实可以发起/实施某种行为、且明确代理身份/授权时使用；`Capability Provider`、`Execution Mechanism`、`System of Record` 是不同角色，并非总能互换。
- `Business Task` 可以作为**分析与跨方案比较单位**，但其稳定性相对于 Application/Agent 只是待验证假设；更稳定的可能是业务结果与验收约束，而任务划分也可能改变。
- 不强制要求将业务本体与 IT 运行本体物理合并。可以使用分域模型，以 `Task ↔ Capability/Contract ↔ Execution Binding ↔ Operational Run/Resource` 关联；各自业务事实/运行状态仍由相应 SoR、Domain Service、Workflow 和 Control Plane 持有。关系映射不意味着一个巨大 Ontology 平台。

### 14.3 需求到基础架构的最小充分推导（候选，不是施工顺序）

```text
Business Goal / Accepted Outcome / Organization & Legal Constraints
               ↕
Business Object / Task / Decision / Action / Policy
               ↓
Allocation: Human / Deterministic Software / Agent / Mixed
               ↓
Required Capability & Control:
  Evidence / Facts / Semantic / Context | API / Action / IAM / Policy
  State / Recovery / Approval / Trace | Model / Tool / Environment
               ↓
Reuse Existing SoR / Workflow / Data / IAM / Cloud / API First
               ↓
Only the Verified Gaps → Incremental AI/IT Infrastructure
               ↓
Observable Outcome & Feedback → Reconsider Task and Capability
```

这里的 `定 → 用 → 管 → 建` 是**售前与架构需求论证顺序**，并非要求工程先完成整个业务建模再部署资源。安全合规、基础设施国产化/迁移、现网约束、预算、运维 SLA 也可能是独立的正当建设驱动，而非都必须由单个 Agent Task 推导。路线应允许从底层现实约束反向迭代。

| 场景或反例 | 首先验证的最低充分方式 | **不应直接推导**出的建设 |
|---|---|---|
| 简单知识问答/单轮模型 API | 已授权数据/文档检索 + 现有模型服务 + 人工核验 | 统一 Ontology、独立 Harness、私有 GPU |
| 规则明确的状态修改/审批 | 既有 Domain API、Command、IAM、Workflow / SoR | Agent、统一 Task Controller、单独 Action Runtime |
| 长程跨系统、需人工等待与故障恢复 | 既有 SoR/Workflow + 受限 Agent + 幂等/审计；按失败模式选 durable state | 所有场景专有 Harness 平台；把 Agent 状态当业务权威状态 |
| 多应用语义不一致 | 先测 Domain Contract / API / 数据字典的协调能力，再测共享语义净收益 | 大一统企业 Ontology |
| 算力扩容、信创迁移、基础设施资源运营 | IT Operational Object / 资产、利用率、合规、运维 SLA、容量预测 | 为证明合理性而杜撰 Agent Business Task |

**必要能力 ≠ 必须新建平台**：Agent 可能新增/强化任务生命周期、可恢复执行、状态与上下文隔离、工具治理、委托权限、运行审计及成本配额；其实现仍可能由已有 Workflow、API Gateway、IAM、Model API、Container 和监控能力扩展。显式需求要先与存量能力比对，并标注重用、补齐或新建。

### 14.4 与 Ontology / Context / Action 的横向关系

此处只登记**分域与映射问题**，不改写 RP-002 的 canonical 解释：

- **Business-world model**：描述业务对象、关系、状态、事件、规则、动作以及责任等；其建模边界由业务目标、监管约束和领域专家共同限定。
- **IT-operation model**：描述 Application/Agent/Model/Tool/Deployment/Runtime/Resource/Execution 与它们的运行约束；其状态可来自 CMDB、编排/监控/计量系统等。
- **Task Context**：在一次具体任务中按身份、权限、时效和来源组装事实/知识/运行状态；既不等于全部 Ontology，也不意味着将状态复制入模型 Prompt。
- **Action & Control**：Ontology 的动作语义不能自动生成执行权限、事务一致性或可恢复性；应以可信系统的授权和执行契约为准。

**开放问题**：何时分域模型之间的 `Task/Capability/Execution` 关系产生真实复用与治理收益，何时它只是另一个维护负担？单一业务流程中的普通领域对象可同时具有业务与 IT 视角；领域划分是治理选择，不是形而上的绝对边界。

### 14.5 可反驳假设、替代解释与验证方式

**候选 H-A（精炼 H-RP006-04，不新编号）**：引入 Agent 执行工作负载后，基础架构需求分类需要增加条件性运行/控制能力。**替代**：既有应用/工作流/运维平台扩展即足够，无须独立 AI 基础设施类别。**验证**：对相同任务逐项映射新增状态、恢复、授权、成本与隔离要求，记录现有设施覆盖率和新增机制带来的净改进。

**候选 H-B（精炼 §12 Task-led 分析）**：采用 `Outcome/Acceptance → Task → Actor/Mechanism → Capability` 能减少组件先行的无谓建设。**替代**：合规迁移/容量运营/数据治理等任务不以 Agent 为入口，技术约束可能先于业务任务。**验证**：同一批知识、确定性事务、长程高风险、纯 IT 运营场景，对比“预设 AI 技术栈”与“任务/现有能力缺口”两种规划法的过度建设、必需能力遗漏、总成本、变更复杂度；保持业务结果和合规要求一致。

**候选 H-C（跨 RP-002-04 / RP-002-02 关系，不新编号）**：业务世界与 IT 运行世界分域表达、通过 Task/Capability/Execution 关联，有助于避免语义与运行状态混淆。**替代**：单领域 Domain Model + Schema/API/CMDB 已充分，无需显式跨域本体。**验证**：同一业务任务跨两个应用/执行者运行时，比较领域模型单独实现与分域关联在对象识别、运行追踪、授权回溯、维护/同步成本的差异。

**证据状态**：以上均是 Working Hypothesis / Test Design；尚无本轮新增 Source Fact 或生产验证结果，不创建 Evidence Card，不进入 `JUDGMENTS.md` / `PRINCIPLES.md`。本轮不重复 §13 的 A/B/C 三路线实验；下一步优先给既有双任务对照加上“角色划分 × 运行需求 × IT 资源映射”记录列，外加一个纯基础设施迁移负例。若结果表明传统设施已足够或模型映射增加成本，应主动收缩本假设。

**归属决定**：本节仅作为 RP-006 下的跨域需求推导视角；RP-002-04 持有 Ontology → Task Context 问题，RP-002-02 持有受治理 Action，RP-004 持有 Authority/Accountability，RP-006 持有 Task → Runtime/Infrastructure Pattern。未证明出现现有问题域无法容纳的新长期 Problem，不新增 RP-007 / 独立 Topic / 平台层。
