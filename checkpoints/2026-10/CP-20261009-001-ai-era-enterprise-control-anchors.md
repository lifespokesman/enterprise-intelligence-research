# CP-20261009-001｜AI-era Enterprise Control Anchors

Date: 2026-10-09  
Type: Conversation → Research Delta Checkpoint  
Related: RP-002-02 / RP-004 / RP-006 / Q1 / Q2 / Q3

## 1. Trigger

讨论触发问题：

> 当 AI 逐渐接管传统业务系统中的“信息获取—理解—判断—操作”后，传统 Workflow、System of Record、Policy 和 Human Responsibility 分别还承担什么不可替代的职责？

这不是“传统业务系统是否会被 AI 替代”的产品判断，而是一个更底层的架构边界问题：

> **哪些企业职责可以被概率性智能吸收，哪些职责仍需要确定性的事实、约束、执行承诺和责任锚点？**

## 2. Delta

本轮形成新的 Working Hypothesis：

### H-RP002-07｜Enterprise Control Anchors

- System of Record → Reality Anchor；
- Policy / Authority → Constraint Anchor；
- Workflow / Durable Execution → Commitment / Execution Anchor；
- Human / Organization → Accountability Anchor；
- Agent / Harness → Cognitive / Adaptive Coordination。

同时形成四个重要区分：

1. Agent Planning ≠ Durable Commitment；
2. Agent Context / Memory ≠ Authoritative Business State；
3. Judgment ≠ Enforceable Policy；
4. AI can decide ≠ AI owns Decision Right ≠ AI bears Accountability。

## 3. Problem Routing

本轮不新增 RP。

原因：

- SoR / Reality / Context 已由 RP-002 / RP-002-04 覆盖；
- Workflow / Business Action 已由 RP-002-02 覆盖；
- Agent 持续执行已由 RP-006 覆盖；
- Policy / Authority / Human Control / Accountability 属于 RP-004；
- Q1 / Q2 / Q3 分别覆盖 Decision Rights、Responsibility 与 Coordination。

因此该问题当前登记为 **RP-002-02 × RP-004 × RP-006 的 cross-cutting cognitive / architecture question**。

## 4. What Changed

此前研究更偏向：

```text
Context
→ Agent
→ Business Action
→ Runtime
→ Enterprise System
```

本轮增加一个反向约束视角：

```text
AI / Agent 可以成为业务操作的主要认知与交互入口
≠
AI / Agent 自动成为企业事实、规则、承诺与责任的最终权威
```

这为后续判断“哪些传统系统能力会消失、弱化、重构或保留”提供了新的研究轴。

## 5. What Did Not Change

- 不改变 RP-002-01 Human Frontier；
- 不改变 Research Runner 当前 Automation Frontier；
- 不新增 RP-007；
- 不创建新的顶层 Topic；
- 不修改 JUDGMENTS.md / PRINCIPLES.md；
- 不把“四锚点”视为已验证事实。

## 6. Open Questions

1. Workflow 的稳定内核是否真的是 Durable State / Commitment，而不是传统 Workflow Engine 本身？
2. SoR 是否必须由传统业务应用承担，还是可被 Event Log / Ledger / AI-native transactional substrate 重构？
3. Policy 中哪些规则必须形式化 enforce，哪些可以交给模型解释？
4. Accountability 是否始终需要具体 Human，还是可以锚定到 Role / Organization / Licensed Entity？
5. 四类 Anchor 是否独立，还是在部分架构中可以合并？
6. AI-native Runtime 是否会把这些机制物理整合，但仍保持逻辑职责分离？

## 7. Next Evidence Direction

若后续启动研究，优先按机制找跨路线证据，而不是找支持“四锚点”的材料：

- Workflow / Durable Execution；
- System of Record / Ledger / Event Sourcing；
- Policy-as-Code / Authorization / Approval；
- Delegated Authority / Accountability；
- AI-native application architecture；
- Counter Evidence。

Stop condition：第一轮只判断这些逻辑职责是否跨多种实现稳定出现，不直接设计新的 Enterprise Control Plane。
