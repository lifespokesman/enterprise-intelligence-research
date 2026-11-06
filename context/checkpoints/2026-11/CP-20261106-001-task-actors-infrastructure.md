---
checkpoint_id: CP-20261106-001
date: 2026-11-06
source: "抽象需求侧思考 → Cognitive Reframing → Working Analysis（非公开证据）"
primary_topic: T-001
related_topics:
  - T-002
related_questions:
  - RP-006
  - RP-002-04
  - RP-002-02
  - RP-004
related_hypotheses:
  - H-RP006-04
  - H-RP002-08B
---

# Trigger

在企业云、数据、应用、AI 平台的规划中，技术组件堆叠往往容易先于“业务究竟需要什么”。新的抽象问题是：Agent 参与业务之后，企业 AI 基础架构应围绕哪些需求对象与运行对象组织，怎样从业务结果、任务、执行要求与存量资产反推最低充分能力？

此为用户的研究命题输入，而非经公开案例核验的产业事实。公开仓不保留具体项目或用户身份。

# Delta

## 真正新增的工作视角

1. 将 **Business World**（对象/任务/动作/结果/责任）与 **IT Operation World**（应用、Agent、模型、运行态、工具、部署及资源）作为可能不同的模型域；通过 Task/Capability/Execution 关联，不自动合并为统一大本体。
2. 区分 **执行角色与软件形态**：Application 可承载 SoR/Domain Service/Workflow，Agent 可内嵌应用或由其调用；二者既不互斥，也不天然是同级自主 Execution Actor。
3. 把 `定→用→管→建` 限定为需求论证顺序；基础设施迁移、合规、运维和容量管理也有独立需求来源，不能强制为每个建设活动寻找 Agent Task。

## 已有认识的重述或精炼

- RP-006 §12–§13 已提出 Business Task 作为需求分析单位、按任务风险和执行要求选择 Runtime Pattern，并允许现有 Workflow/SoR 优先；本轮不重新发明 Task-first。
- RP-002-04 已区分 Ontology 与任务 Context，RP-002-02 已区分动作定义与受治理执行。此次补的是 **业务与 IT 运行需求的可追溯映射**，不是新增平台。
- “Business Task 比 Application 和 Agent 更稳定”不能直接当结论；Business Outcome / Acceptance 可能较稳，但业务任务的划分同样可能改变。

## 候选假设与反证

- **H-A / 精炼 H-RP006-04**：Agent 新增条件性执行与治理要求；反证是既有 IAM/Workflow/运行平台扩展已充分。
- **H-B / §12 的需求推导精炼**：Outcome/Task → Role → Capability → Infrastructure 比组件清单更能避免冗余；反证是合规迁移、纯算力资源运营与其他非 Agent 驱动场景。
- **H-C / 跨 RP-002-04 与 RP-002-02 的关系**：分域与映射能避免语义/运行态混淆；反证是现有 Domain Model/API/CMDB 已足够，显式模型反增同步成本。

均是 Hypothesis / Test Design，没有新增 Source Fact 或可证实企业 Outcome。

# Decision / Scope

- **归属**：RP-006 负责 Task → Execution Role / Pattern → Infrastructure 的需求推导；T-001 保留业务世界与 IT 运行模型的关系视角；相关治理仍由 RP-002-02 / RP-002-04 / RP-004 持有。
- **不新增**：Research Problem、Hypothesis ID、Topic、Action/Context/Task/IT Ontology Platform，亦不修改现有 Research Runner 或人工 Frontier。
- **不升级**：JUDGMENTS / PRINCIPLES，直到公开证据与反例充分。

# Open Questions

1. Business Task 比 Application / Agent 更稳定在何种业务变化下成立？能否由 Outcome / Acceptance 提供更稳的锚点？
2. Execution Actor、Capability Provider、SoR、Execution Mechanism 怎样在架构描述中严格划界？
3. Business World 与 IT Operation World 的分域映射何时带来净价值，何时只是重复维护？
4. 哪些 Agent 运行约束是传统 IT 机制的扩展，哪些才是条件性新增的机制？

# Impact

- Canonical: [RP-006 §14](../../../research/problems/RP-006-enterprise-agent-harness-runtime.md)。
- Topic: [T-001](../../topics/T-001-enterprise-world-model-context.md)。
- 无新 H-ID 与 Evidence；不修改 `NOW.md`、`REPOSITORY_STATE.yaml`、`research/RESEARCH_STATE.yaml`、`RESEARCH_MAP.md`、`context/TOPIC_INDEX.md`。

# Next

复用 RP-006 §13 的既有**双任务 A/B/C 路线对照**，附加角色分工、能力复用与 IT 资源映射记录；增加**纯基础设施/合规迁移负例**。验证传统 Domain API + Workflow + IAM 是否已经满足要求，比较误建组件、遗漏控制、总成本和业务验收差异。第一轮不扩展成新的研究计划。
