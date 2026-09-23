---
topic_id: T-004
title: Context Continuity & AI Collaboration
status: active
updated: 2026-09-23
keywords:
  - conversation
  - checkpoint
  - topic state
  - context routing
  - progressive loading
  - compaction
related_topics:
  - T-003
related_questions: []
related_hypotheses: []
---

# Scope

本 Topic 负责：

> ChatGPT、Codex 和未来其他模型在多个独立会话中，如何依靠仓库恢复长期状态，而不是依赖完整聊天历史或每次扫描整个仓库。

---

# Current Questions

1. 哪些会话变化值得写 Checkpoint，哪些不值得？
2. Topic State 如何保持足够完整但不膨胀？
3. Progressive Context Loading 是否能在实际任务中显著减少读取成本？
4. `CURRENT.md`、`NOW.md`、`PROJECT_CONTEXT.md` 的边界是否足够清晰？
5. 未来是否需要半自动生成 / 更新 Checkpoint，还是人工触发已足够？

---

# Current State

当前采用最小机制：

```text
Conversation
→ 判断是否有长期 Delta
→ Checkpoint
→ 更新 Topic State
→ 必要时更新 CURRENT / Question / Hypothesis
→ 新任务经 TOPIC_INDEX 路由
→ 只加载 1–3 个 Topic
→ 信息不足再向 Research / Evidence 深挖
```

关键定义：

- Conversation = 临时运行环境；
- Checkpoint = 增量变化事件；
- Topic State = 长期主题最新有效状态；
- TOPIC_INDEX = 轻量 Context Routing Index；
- CURRENT = 仓库当前少数重点的快速恢复入口；
- Git history = 文件版本与历史回退机制，不由 Topic 内部重复承担。

---

# Decisions

- 不保存所有对话。
- 不为所有历史会话补 Checkpoint。
- 不为所有问题建立 Topic。
- 不引入向量数据库或外部状态服务。
- 不强制机械的 Checkpoint 数量阈值；当历史读取负担明显上升时做 Compaction。
- Topic 是 current-state 文档，不是 append-only 日志。
- `NOW.md` 保持研究驾驶舱角色，不迁移、不替代。

---

# Linked Research

- `context/README.md`
- `context/CURRENT.md`
- `context/TOPIC_INDEX.md`
- `AGENTS.md`
- `ai-context/PROJECT_CONTEXT.md`

---

# Open Gaps

- 如何判断“长期 Delta”的最低写入门槛？
- 如何避免 Topic 数量逐步重新膨胀成第二套问题库？
- 当多个 Topic 受影响时，如何避免一次会话产生过多同步维护？
- 是否需要在未来 Research Runner / Codex 提示词中加入“结束时做 Checkpoint 判定”的轻量动作？

---

# Recent Changes

- 2026-09-23：首次建立 Context Continuity Layer。

---

# Next

> 用后续真实 ChatGPT / Codex 新会话验证一次完整的“AGENTS → CURRENT → INDEX → Topic → 下钻”流程，再决定是否需要自动化。
