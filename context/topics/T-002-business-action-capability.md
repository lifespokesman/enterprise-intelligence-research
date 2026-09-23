---
topic_id: T-002
title: Business Action & Governed Capability
status: active
updated: 2026-09-23
keywords:
  - action
  - capability
  - tool
  - command
  - workflow
  - policy
  - approval
  - audit
related_topics:
  - T-001
  - T-003
related_questions:
  - RP-002-02
related_hypotheses:
  - H-RP002-06
  - ST-RP002-01
---

# Scope

本 Topic 负责恢复：

> 当 Agent 不只是理解企业世界，而需要创建任务、修改状态、发起审批、调用系统和产生真实副作用时，企业应如何提供稳定、受治理、可审计的行动能力？

---

# Current Questions

1. Agent 时代真正新增的 Action 机制是什么，哪些只是既有 Application Service / Command / Workflow 的重表达？
2. 长期稳定资产更可能是独立 Action Runtime、Governed Capability Contract，还是 Policy + API / MCP Schema？
3. 哪些风险、跨系统协调和多调用者复用阈值，足以让显式 Capability Contract 产生净价值？
4. Agent Identity、Delegated Authority、Policy、Approval、Audit、Provenance 应分别由谁承担？

---

# Current State

当前有效认识：

- DDD Application / Domain Service、CQRS Command 与 Workflow / Durable Runtime 已经承担 Business Action 的大量业务语义和可靠执行职责。
- Agent 时代新增或显著强化的主要是**模型控制调用的治理边界**：Identity、授权范围、Schema、State Constraint、Approval、Validation、Audit、Provenance 等。
- Palantir Ontology Action 提供了“对象 / 状态绑定 + 提交条件 + 权限 + 执行绑定 + Action Log”的强样本，但不能据此证明行业必须存在独立 Agent Action Runtime。
- 当前战略候选判断是 **Governed Capability Contract** 可能比“独立 Action Runtime”更稳定；但它仍只是候选概念。
- 跨系统副作用、补偿、幂等、长时运行仍主要需要 Workflow / Durable Runtime 一类工程机制。
- 简单、低风险、单系统、可逆 CRUD 可以继续由 Domain API / Command + Tool Schema 承担。

---

# Decisions

- 不把 Business Action Layer 自动升级为新的长期固定架构层。
- 不再通过堆更多厂商清单证明观点，下一步优先工程验证。
- 需要同时保留替代假设：`Agent Identity + Policy Engine + 通用 API / MCP Schema` 可能已足够。

---

# Linked Research

- `research/problems/RP-002-02-business-action-layer.md`
- `research/RESEARCH_STATE.yaml`
- Evidence：E-001 ～ E-021
- Active Hypothesis：H-RP002-06
- Strategic Thesis Candidate：ST-RP002-01

---

# Open Gaps

- 真实多 Agent、跨团队 API 演进下，显式契约的治理收益是否大于维护成本？
- 权限撤销、并发、重复提交、部分失败时，两条路线差异多大？
- 主流平台未来是否持续强化显式 Capability / Action contract，还是逐步被通用 Policy + API 吸收？

---

# Recent Changes

- 2026-09-18 ～ 2026-09-20：研究从“Business Action Layer 是否需要存在”收敛到“治理边界是否需要显式契约”，并形成 ST-RP002-01。
- 当前 Research Runner v0.4 正围绕该 Topic 的工程验证试运行。

---

# Next

> 寻找可运行公开实现或小型可审计仓库，加入并发、重复提交、权限撤销和部分失败注入，对比通用 API + Policy 与显式 Governed Capability Contract。
