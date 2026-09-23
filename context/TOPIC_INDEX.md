# TOPIC_INDEX｜Context Routing Index

Updated: 2026-09-23

> 只用于 **Context Routing**。不要把正文、历史讨论或长结论复制到这里。

| Topic ID | 名称 | 说明 | 关键词 | 相关 Topic | 关联研究 | 状态 | 文件 |
|---|---|---|---|---|---|---|---|
| **T-001** | Enterprise World Model & Context | 企业世界如何被表达、验证，并转换为 Agent 当前任务可消费的 Context | ontology, world model, context engineering, task context, evolution, semantic | T-002, T-003 | RP-002, RP-002-01, RP-002-03, RP-002-04 | active | [T-001](topics/T-001-enterprise-world-model-context.md) |
| **T-002** | Business Action & Governed Capability | Agent 如何在权限、状态和责任边界下改变企业世界 | action, capability, tool, command, workflow, policy, approval, audit | T-001, T-003 | RP-002-02, H-RP002-06, ST-RP002-01 | active | [T-002](topics/T-002-business-action-capability.md) |
| **T-003** | Research System & Research Runner | 问题—假设—证据研究闭环、自动研究运行态与 Git 交付规则 | research loop, runner, evidence gap, hypothesis, weekly synthesis, git delivery | T-001, T-002, T-004 | RESEARCH_LOOP, RESEARCH_STATE, NOW | active | [T-003](topics/T-003-research-system-runner.md) |
| **T-004** | Context Continuity & AI Collaboration | ChatGPT / Codex 多会话如何通过 Checkpoint、Topic State 和 Progressive Loading 继续长期工作 | conversation, checkpoint, topic state, context routing, progressive loading, compaction | T-003 | Context Continuity Layer | active | [T-004](topics/T-004-context-continuity.md) |

---

## Routing 规则

新任务先根据**目标和问题**匹配 Topic，而不是根据出现了哪些技术词匹配。

通常只读取最相关的 **1–3 个 Topic**。

当多个 Topic 都相关时：

- 企业世界表达 / Ontology / Context → 优先 T-001；
- Agent 执行动作 / Tool / Capability / Action Governance → 优先 T-002；
- 研究方法、自动研究、Evidence / Hypothesis 演进 → 优先 T-003；
- 多会话继承、Checkpoint、AI 协作、Context Loading → 优先 T-004。

Topic 信息不足时，再向下追溯关联的 Question / Hypothesis / Checkpoint / Research / Evidence。
