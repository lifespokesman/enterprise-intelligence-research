---
checkpoint_id: CP-20261014-001
date: 2026-10-14
source: "脱敏 Field Signal → Cognitive Reframing → Existing Problem Evolution"
primary_topic: T-002
related_topics:
  - T-001
related_questions:
  - RP-002-02
  - RP-002-03
  - RP-002-04
  - RP-004
  - RP-006
  - RP-003
related_hypotheses:
  - H-RP002-06
---

# Trigger

一次不涉及可识别机构/系统/设施信息的企业 AI 规划反思：当知识检索、专业 Agent 和工具接入按部门建设时，“统一入口”仍可能掩盖多份语义解释、能力实现和治理规则。现实刺激只作为 **Field Signal**；尚无公开材料证明行业普遍发生相同现象。

# Delta

## 新增认识

- “智能烟囱”更适合作为 **Context / Semantic / Capability-Action / Governance** 四个可并存的诊断维度；Execution / Runtime 重复是额外对照。它们并非必须按某条链依次出现。
- Business Action 除了避免 Agent 直连后台，可能进一步承担 **跨 Agent、跨业务单元复用有业务含义的状态改变契约** 的职责；这是已有 H-RP002-06 / ST-RP002-01 的新的复用动因，尚未被实证证明。
- 区分两张图：**Capability / Logical Relations**（语义、契约、权威事实、治理的依赖）与 **Runtime Execution Loop**（目标、动态 Context、动作提议、授权、后端执行、事实/反馈）。世界模型演化属于更慢的独立治理过程。

## 修正 / 深化

- Ontology / Shared Semantic Core 不等于单一 RAG、唯一业务真相数据库或强制统一的物理系统；合法领域视图需要保留。
- Business Capability 包含读/分析/写；本研究的 **Governed Business Mutation Action** 专注正式业务变更/承诺。Tool/MCP 是暴露/调用机制，不是业务契约本身。
- Action Definition 与 Runtime **逻辑上分工**，但可由现有 Domain Service、Policy、Workflow、SoR 组合实现，不规定独立部署。
- Agent “变薄”、三模块共同智能基础设施仅保留为条件性架构解释，不固化为必然趋势或通用三层平台。

## 未成立 / 降级

- 未证明“应用/数据烟囱会逐级迁移到语义→动作→治理”；未证明独立 Action Runtime / Control Plane 必需；未证明单一 Ontology / Action Registry 是唯一解法。
- 私人项目刺激不进入公开仓 Evidence，也不推出行业 ROI 或普遍事实。

## 新决策

- 路由到 **RP-002-02 existing problem evolution**，增强 H-RP002-06 的多调用者验证方向；T-001 只吸收 Context / Semantic 关系。
- 不创建 RP、Hypothesis ID、Gap、Topic、公开 Evidence Card；不修改 Frontier、Runner Scope、JUDGMENTS 或 PRINCIPLES。

# Open Questions

1. Shared Semantic Core 与各部门合法差异的边界及成本？
2. Ontology-native Action 与 Domain Command / Action Registry 的等价及差异阈值？
3. 相同权限和后端条件下，Domain API + Policy 是否已足够，额外契约有无净收益？
4. Action Definition、执行强制点、Workflow 与 SoR 各持什么权威状态？
5. Business Task / Agent Run / Action Result / Business Outcome 怎样安全关联与反馈？
6. 哪些任务保留“厚 Agent”反而更有效？

# Impact

- Canonical problem: research/problems/RP-002-02-business-action-layer.md §20。
- Topic State: context/topics/T-001-enterprise-world-model-context.md、context/topics/T-002-business-action-capability.md。
- Index / context pointer: research/research-questions.md、context/CURRENT.md（仅恢复入口）。
- 不改 REPOSITORY_STATE.yaml、NOW.md、research/RESEARCH_STATE.yaml 或 RESEARCH_MAP.md：权威运行状态未变化。

# Next

在既有 GAP-004 后续验证中，固定一个脱敏合成的两 Agent 同业务状态变更任务，对比 (A) 独立 Tool/API 适配、(B) 共享 Domain API + Schema + Policy、(C) 共享 Governed Capability Contract；测试版本升级、授权撤销、并发、幂等和部分失败，并同时记录**业务验收、治理覆盖与总维护成本**。未完成复现前保持 Working Hypothesis。
