---
topic_id: T-001
title: Enterprise World Model & Context
status: active
updated: 2026-09-23
keywords:
  - ontology
  - world model
  - context engineering
  - task context
  - semantic
  - evolution
related_topics:
  - T-002
  - T-003
related_questions:
  - RP-002
  - RP-002-01
  - RP-002-03
  - RP-002-04
related_hypotheses: []
---

# Scope

本 Topic 负责恢复以下长期状态：

> 企业真实世界如何被表达、验证、持续演化，并在 Agent 运行时转换为当前任务真正需要的 Context？

它不负责完整保存 RP-002 的所有研究细节；详细问题、证据和假设仍在 `research/`。

---

# Current Questions

1. 企业世界模型如何判断自己已经无法解释现实？
2. Ontology / World Model 与 Task Context 的稳定边界是什么？
3. World Model / Facts / Knowledge / Policy / Runtime 如何共同生成任务 Context？
4. Context Runtime 是否形成独立工程边界，还是 Agent Runtime + Semantic / Data / Policy 的组合职责？
5. Action 产生 New Fact 后，何时只更新实例 / Context，何时需要触发 Ontology Evolution？

---

# Current State

当前有效认识：

- **Ontology ≠ AI Context**。Ontology 更接近 World-centric 的企业世界表达；Context 更接近 Task-centric 的运行时相关世界切片。
- 当前候选表达：`Task Context = World Context + Knowledge Context + Runtime Context + Identity / Policy`。
- 必须区分 **Object Instance / State Change** 与 **Ontology Change**。
- 当前候选存在三个不同节奏的循环：
  1. Business / Ontology Runtime；
  2. Task Context assembly / runtime；
  3. 更慢的 Ontology Evolution。
- “Context Engine / Context Runtime”目前只是 candidate mechanism，尚未被证据证明为独立 Layer / Platform / Runtime。
- 世界模型应被视为可被运行事实持续挑战的当前可执行解释，而不是最终真相。

---

# Decisions

- RP-002-04 已作为 RP-002 的派生子问题登记，不新建 Problem Family。
- 不继续用“静态本体 / 动态本体”无限扩展 Ontology 分类。
- 下一步验证优先从 **World Model 与 Task Context 是否存在稳定边界** 开始。
- 不因为 Context 问题重要，就提前建立新的 Context Platform 研究 Track。

---

# Linked Research

- `research/problems/RP-002-enterprise-data-model-relationship.md`
- `research/problems/RP-002-01-world-model-conflict-evolution.md`
- `research/problems/RP-002-03-semantic-to-executable-world-model.md`
- `research/problems/RP-002-04-world-model-to-task-context.md`
- `RESEARCH_MAP.md`
- `EVOLUTION.md`：EV-012
- `NOW.md`

---

# Open Gaps

- World Model / Context 的边界是否得到理论、产品、工程多源支持？
- Retrieve / Resolve / Filter / Authorize / Assemble 是否值得作为稳定独立机制？
- Context Provenance / Freshness / Permission / Evidence 如何随上下文进入 Agent？
- Expected World ≠ Observed World 的冲突分类是否稳定存在？
- 哪些反例说明强 Runtime Context 可以替代预建 Ontology？

---

# Recent Changes

- **2026-09-23**：问题从“继续扩展 Ontology 分类”转向“World Model → Task Context 转换机制”，见 `EVOLUTION.md#EV-012`。
- **2026-09-23**：Context Continuity Layer 建立后，本 Topic 成为跨会话恢复入口；研究细节仍保留在 RP 文件。

---

# Next

若继续本 Topic：

> 先验证“稳定世界表达”与“任务运行时上下文”是否是跨理论 / 产品 / 工程都存在的稳定区分，同时主动寻找二者合并建模的反例。
