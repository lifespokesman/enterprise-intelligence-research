---
checkpoint_id: CP-20260923-001
date: 2026-09-23
source: ChatGPT conversation / repository governance change
primary_topic: T-004
related_topics:
  - T-003
related_questions: []
related_hypotheses: []
---

# Trigger

项目中的长期讨论已经分散在 ChatGPT、Codex 等多个会话中。

单个会话不断延长会增加模型读取和推理成本；直接开启新会话又容易丢失此前规划、判断、问题演进和下一步。

现有仓库已经有：

- `NOW.md`：研究驾驶舱；
- `RESEARCH_MAP.md`：长期研究地图；
- `research/problems/`：问题状态；
- `RESEARCH_STATE.yaml`：自动研究运行态；
- `EVOLUTION.md`：重大认知演进；
- `ai-context/PROJECT_CONTEXT.md`：AI 长期背景。

但仍缺少一个明确回答：

> **某个长期主题经过多轮会话后，现在最新有效状态是什么，以及新会话应加载哪些最小上下文？**

---

# Delta

## 新增认识

- Chat 不应该承担长期状态数据库职责。
- Question / Hypothesis / Research / Evidence 能描述未知、猜测和依据，但不足以独立表达“一个长期主题当前整体走到哪里”。
- 跨会话继承需要增加：
  - Checkpoint：记录相对此前状态的认知 / 项目 Delta；
  - Topic State：保存长期主题当前最新有效状态；
  - Topic Index：承担 Context Routing；
  - CURRENT：提供仓库级少量当前状态入口。
- 新任务应采用 Progressive Context Loading，而不是默认扫描整个仓库。

## 修正认识

原 `ai-context/PROJECT_CONTEXT.md + NOW.md + research files` 的组合虽然能提供背景，但仍偏“静态项目说明 + 单一研究前沿”，无法稳定承担多 Topic、多执行器、多会话的恢复职责。

因此不删除原机制，而是在其上增加轻量 Context Continuity Layer。

## 被否定 / 降级的认识

- “只要把所有背景都写进一个 PROJECT_CONTEXT 就能解决长期上下文”被降级；
- “每次新会话多读一些仓库文件即可恢复状态”被降级；
- “所有对话都需要摘要保存”被否定。

## 新决策

建立最小 Context Continuity Layer：

```text
Conversation
→ Checkpoint
→ Topic State
→ Context Routing
→ New Task
```

首批只创建少量 Topic，不迁移历史资产，不补历史 Checkpoint，不引入外部数据库。

---

# Open Questions

1. Topic 数量增长后，什么情况下需要合并或拆分？
2. Checkpoint 的最低写入门槛是否需要更明确的判断量表？
3. Context Router 规则仅靠 Markdown 是否已足够？
4. `PROJECT_CONTEXT.md` 后续是否可以进一步缩短为稳定背景说明？

---

# Impact

- 新增 `context/` 作为跨会话状态层；
- `AGENTS.md` 增加 Context Loading / Checkpoint / Topic Update / Compaction 协议；
- `README.md` 增加 Context Continuity Layer 导航与职责说明；
- `ai-context/PROJECT_CONTEXT.md` 的默认加载规则需要让位于新的 Progressive Context Loading 入口；
- 现有 Question / Hypothesis / Research / Evidence 结构保持不迁移。

---

# Next

> 用下一次真实新会话验证：只读取 AGENTS + CURRENT + INDEX + 相关 Topic，是否足以继续工作；只有不足时再下钻到 RP / Hypothesis / Checkpoint / Evidence。
