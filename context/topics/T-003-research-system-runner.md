---
topic_id: T-003
title: Research System & Research Runner
status: active
updated: 2026-09-23
keywords:
  - research loop
  - research runner
  - evidence gap
  - hypothesis
  - weekly synthesis
  - git delivery
related_topics:
  - T-001
  - T-002
  - T-004
related_questions: []
related_hypotheses: []
---

# Scope

本 Topic 负责恢复仓库的研究工作方式：

> 如何让真实问题持续牵引理论 / 产品 / 案例 / 工程证据，并让证据真正修改 Hypothesis，而不是形成资料堆积？

同时记录 Research Runner 的当前运行边界，但不替代 `research/RESEARCH_STATE.yaml`。

---

# Current Questions

1. 自动研究如何从“搜索与摘要”升级为对问题和假设有实际增量的 Research Finding？
2. Strategic Thesis 如何满足 Theory / Product / Case / Counter Evidence 多域约束？
3. Research Runner 如何自动工作又不越权修改正式认知？
4. 如何让 Human / ChatGPT / Codex 的 Git 写入都回到同一个 main + PR 审核闭环？

---

# Current State

研究基本单位已从 Paper 升级为 **Problem + Hypothesis Package**。

主闭环：

```text
Real Problem
→ Hypothesis
→ Evidence Gap
→ Targeted Research
→ Research Finding
→ Hypothesis Revision
→ Engineering Validation
→ Principle / New Problem
```

当前 Research Runner v0.4：

- 单 Active Problem 运行；
- Heartbeat 只推进一个 Evidence Gap；
- Research Finding 优先于 Evidence Card；
- 战略级 Gap 使用 WHAT / WHY / STRUCTURAL / TRANSITIONAL / EMERGING / FUTURE；
- Strategic Thesis 至少覆盖 4 个证据域中的 3 个；
- 必须保留 Alternative Hypothesis 与 Falsifiable Predictions；
- GitHub `main` 是唯一正式状态；
- 所有 AI 修改使用独立 branch + PR，不自动 merge。

---

# Decisions

- 自动 Research Heartbeat 不直接修改正式 Problem / NOW / JUDGMENTS / PRINCIPLES。
- Hypothesis 正式版本变化由 Weekly Synthesis 或人工审核完成。
- 无高价值增量时允许 `NO_MATERIAL_UPDATE`，不制造伪进展。
- 不要求所有研究问题同时自动运行；当前 v0.4 仍是局部试运行。
- Context Continuity Layer 加入后，研究系统本身不再承担所有跨会话恢复职责。

---

# Linked Research

- `AGENTS.md`
- `research/RESEARCH_LOOP.md`
- `research/RESEARCH_STATE.yaml`
- `NOW.md`
- `RESEARCH_MAP.md`
- `EVOLUTION.md`

---

# Open Gaps

- v0.4 的战略研究深度是否能稳定产生真正新洞察？
- 工程验证如何尽量使用公开、可运行、可审计的最小实现？
- Weekly Synthesis 的更新节奏是否会造成正式状态与 Runner state 暂时分叉？
- Context / Topic 层加入后，哪些旧 AI context 文档可以进一步瘦身？

---

# Recent Changes

- 2026-09-18：Research Loop 升级为 v2.2，问题—假设包成为核心研究单位。
- 2026-09-20：RP-002-02 的战略 Thesis 获得合成工程验证的条件性支持。
- 2026-09-23：新增 Context Continuity Layer，跨会话恢复职责从“靠长上下文 / PROJECT_CONTEXT”转向 CURRENT + Topic + Checkpoint。

---

# Next

> 继续验证 Research Runner v0.4 的研究深度，同时观察 Context Continuity Layer 是否能减少新会话对全仓扫描和长聊天历史的依赖。
