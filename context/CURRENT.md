# CURRENT｜仓库当前上下文入口

Updated: 2026-09-23

> 本文件只回答：**一个新的 AI 第一次进入仓库时，当前最值得知道的少数状态是什么？**
>
> 它不是第二个 README，也不替代 `REPOSITORY_STATE.yaml`、`NOW.md`、`RESEARCH_STATE.yaml` 或 Topic State。
>
> 机器需要判断“当前状态属于哪个运行面”时，先读取根目录 `REPOSITORY_STATE.yaml`；本文件负责把这些状态转换为新会话可快速恢复的人类可读视图。

---

## 1. 当前主线

### 主线 A｜企业世界模型与任务上下文

当前研究长期主线仍位于 **RP-002｜Enterprise Data–Model / World Relationship**。

近期关键变化：

- 世界模型 / Ontology 不再被简单等同于 AI Context；
- 新增 **RP-002-04｜World Model → Task Context**，研究稳定企业世界表达如何被动态转换成任务运行时上下文；
- Context Engine / Context Runtime 目前仍只是 candidate mechanism，不视为已成立独立层。

相关 Topic：[`T-001`](topics/T-001-enterprise-world-model-context.md)

### 主线 B｜企业 AI 如何安全改变企业世界

**RP-002-02｜Business Action Layer** 已形成更收敛的候选判断：

- 传统 Application Service / Command / Workflow 已承担大量业务动作与可靠执行职责；
- Agent 时代更可能强化受治理能力契约、Identity、Delegated Authority、Policy、Approval、Audit、Provenance 等边界；
- 独立 Action Runtime 仍是条件性工程选择，不是既定长期架构。

相关 Topic：[`T-002`](topics/T-002-business-action-capability.md)

---

## 2. 当前研究与自动化运行态

这里需要区分两条“当前”：

- **人工研究驾驶舱**：`NOW.md` 当前 Frontier 为 **RP-002-01｜World Model Conflict & Evolution**；
- **Research Runner v0.4 试运行**：`research/RESEARCH_STATE.yaml` 当前 scope 为 **RP-002-02｜Business Action Layer**，下一步做工程验证。

这不是默认冲突，而是：

> 人工研究前沿与自动化试运行对象目前不同。

新任务不要只看到其中一个文件就假设“整个仓库只有一个当前问题”。

相关 Topic：[`T-003`](topics/T-003-research-system-runner.md)

---

## 3. 本轮新增的运行机制

仓库新增 **Context Continuity Layer**，用于解决 ChatGPT / Codex 多会话之间的状态继承：

```text
Conversation
→ Checkpoint
→ Topic State
→ Context Router
→ New Task
```

核心规则：

- Chat 是临时计算过程，不作为长期状态数据库；
- Checkpoint 只记录相对此前状态的 Delta；
- Topic 保存某个长期主题的最新有效状态；
- 新任务采用 Progressive Context Loading，不默认扫描全仓库；
- 没有长期变化就不沉淀 Checkpoint。

相关 Topic：[`T-004`](topics/T-004-context-continuity.md)

---

## 4. 新任务默认恢复顺序

```text
1. AGENTS.md
2. REPOSITORY_STATE.yaml
3. context/CURRENT.md
4. context/TOPIC_INDEX.md
5. 与任务最相关的 1–3 个 Topic
6. 信息不足时，再读：
   Question / Hypothesis / 最近 Checkpoint / Research / Evidence
```

Research Runner Heartbeat / Weekly Synthesis 仍需继续读取 `ops/research-runner.md`，并遵守其中的专项读取、写权限与验收协议。

---

## 5. 当前不要做

- 不全仓 Topic 化；
- 不补录所有历史会话；
- 不把 CURRENT 扩成 PROJECT_CONTEXT；
- 不把 Topic 变成所有历史内容汇总；
- 不为了路由引入向量数据库或外部服务；
- 不把 Context Runtime / Action Runtime 等 candidate mechanism 提前升级为既定架构层。

---

## 6. 最近关键变化

- 2026-09-23：新增 RP-002-04，区分 World Model 与 Task Context。
- 2026-09-23：建立最小 Context Continuity Layer，使跨会话状态可由 Git 恢复。
- 2026-09-23：新增 `REPOSITORY_STATE.yaml`，显式区分 human frontier、automation frontier 与 context maintenance 三个运行面。

最近 Checkpoint：[`CP-20260923-001`](checkpoints/2026-09/CP-20260923-001-context-continuity-layer.md)
