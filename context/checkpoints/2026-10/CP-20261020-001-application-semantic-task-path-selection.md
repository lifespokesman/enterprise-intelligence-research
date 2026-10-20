---
checkpoint_id: CP-20261020-001
date: 2026-10-20
source: "脱敏 Field Signal → Cognitive Reframing → Working Hypotheses（非公开证据）"
primary_topic: T-001
related_topics:
  - T-002
related_questions:
  - RP-006
  - RP-002-04
  - RP-002-02
  - RP-004
  - RP-003
related_hypotheses:
  - H-RP006-04
  - H-RP002-06
---

# Trigger

观察到 AI 可通过两条不同建设路径辅助实现同类申请原型：先建语义模型/物化，再建应用；或先做完整领域应用/受控 API，再通过 MCP/Agent 辅助执行。这些只是抽象、脱敏的 Field Signal；不支持声称某类产品普遍慢、某一路线必然更好或开发者能力差距必然扩大。

# Delta

## 新增认识

- 将容易误判为路线二选一的内容拆为**需求/产品起点、能力生产与复用、交互与执行入口**三个可独立配置的维度；Task-first 不等于对话，Domain engineering 含语义，Ontology 不等于 Schema 物化。
- 补充**应用优先 / 语义优先 / 按需混合**三路线在两个合成任务中的可证伪对照：先跑可验收独立业务闭环，再验证第二应用共享对象与规则的边际收益；同时保留 Domain API + Policy 足够的负例。
- 增加**应用集成契约**工作假说：身份委托、Workflow、待办/通知、深链、业务状态对账和故障恢复可能成为 AI 生成应用规模化交付的主要成本来源。

## 旧判断的实质修正与限定

- **修正的是过去的选型表达，不是宣称仓库曾有一个已证实的「本体优先定律」**：RP-006 已有 Business Task → Runtime Pattern，但未完整描述「应用生产/共享语义/交互」的独立选项。现在以业务验收、既有 SoR 和复用成本决定最小充分路线。
- 「Ontology 物化即可支撑 Agent」被限定为不足以推出权威事实、授权 Task Context 与正式 Action；「有 MCP 即有业务动作」「有页面即完成交付」「自然语言总优于表单」都不成立为通用命题。
- 业务动作的强制授权、持久状态及责任仍归适格的 Domain Service / SoR / Workflow / IAM / 人，而非模型或 Harness 的自我声明。

## 新决策

- 按现有 Problem 分工：RP-006 主持路线选型与人/软件/Agent 分工；RP-002-04 主持语义复用净收益；RP-002-02 主持业务动作及应用接入契约；RP-004 治理约束，不创建新 RP / H-ID / Topic / Plane。
- 保留已有人工研究 Frontier、Runner 协议和 GAP-004，未升级到 JUDGMENTS/PRINCIPLES。仅需通过公开资料及控制变量验证。

# Open Questions

1. 共享 Ontology 相比共享 Domain API、数据字典、Policy 的净收益从第二个还是第 N 个业务才开始显现？
2. AI 生成应用的接入契约应如何机读、可测试，才能降低而非扩大治理/运维总成本？
3. 业务任务内哪一类 Decision/Action 必须保持人在环，何时规则批处理而非 Agent 最优？
4. 专业开发者与非开发者在同一受控任务中质量与纠错差距究竟如何变化？

# Impact

- Canonical: `research/problems/RP-006-enterprise-agent-harness-runtime.md` §13；`RP-002-04` 语义阈值增量；`RP-002-02` §21。
- Topic: `context/topics/T-001-enterprise-world-model-context.md` 与 `T-002-business-action-capability.md`。
- 不改 `REPOSITORY_STATE.yaml`、`NOW.md`、`research/RESEARCH_STATE.yaml`、`topics/README.md`、`JUDGMENTS.md`、`PRINCIPLES.md`。

# Next

使用公开或合成数据完成 Task 1 端到端应用与审批闭环，记录生成与接入成本；再完成 Task 2 同对象跨应用复用，比较 A Domain App-first、B Semantic-first、C Hybrid-on-demand 的综合成本、正确性、恢复率与用户完成表现。尚无实验结果，不创建公开 Evidence Card。
