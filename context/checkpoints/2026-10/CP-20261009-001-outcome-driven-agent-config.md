---
checkpoint_id: CP-20261009-001
date: 2026-10-09
source: "External Signal（《硅谷101》E255 收听记录，非逐字转录）→ Cognitive Reframing → Working Hypotheses"
primary_topic: T-001
related_topics:
  - T-002
related_questions:
  - RP-006
  - RP-002-04
  - RP-004
  - RP-003
related_hypotheses:
  - H-RP006-04
  - H-RP006-05
---

# Trigger

《硅谷101》E255 关于 AI 原生任务执行与产品演进的节目触发了 Model / Harness / Context 三种优化维度的思考。来源：https://podcasts.apple.com/us/podcast/id1498541229?i=1000758544481 。三维框架来自个人收听记录，**未核验是否为嘉宾逐字原话**，不作为节目已证明的技术公式。

# Delta

## 新增认识

- **研究设计方向的调整**：从“怎样让 Agent 更强”转为“Business Outcome / Constraint → Task → AI Applicability → Capability Requirement → Model / Harness / Context / Existing Systems → Execution / Verification / Feedback”。Agent、Workflow、算法与传统系统是候选实施方式而非必经步骤。
- **模型升级时的职责迁移可被具体验证**：优先找“实际删除的补偿机制”与“依旧需要外部保障的约束”，不将现有 Harness 产品边界视为天然永久。
- **Agent 多样化不等于基础设施多套建设**：共享收益应由跨任务复用、治理、隔离与总成本共同验证。

## 修正认识

- `Model × Harness × Context` 只作分析启发式，不作为严格数学模型或既定三层架构。
- `Task Characteristics → Runtime Pattern` 增加 AI Applicability、Information Dependency、Responsibility 与 Business Outcome 约束。
- Context 需要按任务目标、事实新鲜度、风险与权限选择；不是把所有材料放进 Prompt，也不是默认建设统一 Context Engine。

## 被否定 / 降级的认识

- 不将“统一 Agent 平台天然优于独立架构”“模型越强就不再需要 Harness”“模型外持久化必须归 Harness 所有”提升为判断。
- 不把节目观点直接当作业界证据或最终结论。

## 新决策

- 查重后未创建新的 RP。WH-A 精炼 H-RP006-04；WH-B 登记为 **H-RP006-05**；WH-C 作为现有 H-RP006-03/04 的条件性问题；WH-D 并入 VQ-006-01，关联 RP-003 / Q5；Context 侧精炼 RP-002-04 的 H2。
- 优先 V1：模型升级后的机制删减/保留与外部控制边界。初步公开材料已经登记到 RP-006；不把第一轮官方材料核验当作消融实验结果。

# Open Questions

1. 相同任务与评价标准下，模型升级真正可以删掉哪些 Harness / Context 机制，哪些必须保留？
2. Task 特征能否稳定预测独立式、共享式和轻量组合式运行方式的净收益？
3. 技术指标改善如何传导到企业可归因的业务结果？

# Impact

- 更新 `research/problems/RP-006-enterprise-agent-harness-runtime.md` 与 `research/problems/RP-002-04-world-model-to-task-context.md` 的候选问题/假设。
- 更新 `context/topics/T-001-enterprise-world-model-context.md` 的当前工作视图；不建立新的 Topic / Problem Family。
- **不修改** `REPOSITORY_STATE.yaml`、`NOW.md`、`research/RESEARCH_STATE.yaml`、`RESEARCH_MAP.md`、`JUDGMENTS.md`、`PRINCIPLES.md` 或当前 Frontier。

# Next

V1 在已有 RP-006 的稳定职责问题内开展最小模型×Harness 消融对照：固定任务、工具、数据与指标，试验撤去 Context Reset / Sprint / Evaluator 等补偿机制，再加入进程中断、权限撤销与工具失败。没有实测证据前，H-RP006-05 保持 Working Hypothesis。
