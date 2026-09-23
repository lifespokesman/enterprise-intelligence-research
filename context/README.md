# Context Continuity Layer｜会话上下文持续化层

Version: **v1.0**  
Updated: 2026-09-23

> 目标：让不同 ChatGPT / Codex / AI 会话不依赖完整聊天历史，也能恢复“现在认为是什么、为什么、下一步是什么”。

核心原则：

> **Chat 是运行过程，Checkpoint 是增量变化，Topic 是当前状态，Question 是未知，Hypothesis 是待验证判断，Research / Evidence 是支撑，Context Router 决定当前任务真正需要读取什么。**

本层只保存**长期可恢复状态**，不保存完整会话，也不替代现有研究资产。

---

## 1. 与现有体系的职责边界

| 对象 | 回答什么 | 是否长期保留 |
|---|---|---|
| Conversation | 这轮正在怎么探索、试错、推翻？ | 否，临时运行环境 |
| Checkpoint | 相对此前状态，本轮改变了什么？ | 是，增量事件 |
| Topic State | 某个长期主题现在最新有效状态是什么？ | 是，当前状态 |
| Question | 还不知道什么？ | 是 |
| Hypothesis | 当前猜测 / 待验证判断是什么？ | 是 |
| Research / Evidence | 为什么形成这个判断？有哪些支撑、反例和边界？ | 是 |
| `REPOSITORY_STATE.yaml` | 当前不同运行面的机器可读状态是什么？ | 是，Canonical State Registry |
| `NOW.md` | 当前人工研究前沿与下一步研究动作是什么？ | 是，研究驾驶舱 |
| `context/CURRENT.md` | 整个仓库当前最值得恢复的少数工作状态是什么？ | 是，跨会话入口 |

`CURRENT.md` 不替代 `NOW.md`。前者面向**仓库级恢复与多执行器协作**，后者面向**研究前沿管理**。

---

## 2. Topic 创建规则

只有同时满足以下特征的对象才创建 Topic：

- 会跨越多次会话持续演进；
- 未来会被重复调用；
- 已形成一组相对稳定的问题、判断或架构关系；
- 单靠某一张 Question / Hypothesis / Research Card 无法表达“当前整体状态”。

创建前必须先判断：

1. 是否已有高度相关 Topic；
2. 是否只是已有 Topic 的演进；
3. 是否只是一个 Question / Hypothesis；
4. 是否确实形成新的长期研究对象。

普通一次性任务、单个产品问题、单次会话不要 Topic 化。

### Topic ID

使用：

`T-001`、`T-002`、`T-003` …

文件名：

`T-001-<slug>.md`

Topic ID 不与 Q / RP / H / E 等研究 ID 混用。

---

## 3. Topic State Schema

Topic 文件重点保存**当前最新有效状态**，而不是历史流水账。

建议结构：

```markdown
---
topic_id:
title:
status:
updated:
keywords:
related_topics:
related_questions:
related_hypotheses:
---

# Scope
这个 Topic 长期负责什么，不负责什么。

# Current Questions
当前真正还没解决的问题。

# Current State
当前有效认识 / 架构判断 / 概念关系。

# Decisions
已经形成并仍有效的决策。

# Linked Research
关联 Question / Hypothesis / Problem / Research / Evidence。

# Open Gaps
仍未解决或待验证的缺口。

# Recent Changes
只保留最近少量重要变化，并链接 Checkpoint。

# Next
下一步最值得推进什么。
```

更新原则：

```text
原 Topic State
+ 新 Checkpoint
↓
新增 / 修正 / 覆盖 / 冲突 / 待验证
↓
重写“当前有效状态”
```

Topic 不是 append-only 日志。历史演变交给 Checkpoint / EVOLUTION / Git。

---

## 4. Checkpoint Schema

Checkpoint 不是“这次聊天聊了什么”的摘要，而是**认知 / 项目状态的增量事件日志**。

### Checkpoint ID

使用：

`CP-YYYYMMDD-NNN`

例如：`CP-20260923-001`

按月份存放：

`context/checkpoints/YYYY-MM/`

### 推荐结构

```markdown
---
checkpoint_id:
date:
source:
primary_topic:
related_topics:
related_questions:
related_hypotheses:
---

# Trigger
为什么产生这轮变化。

# Delta

## 新增认识

## 修正认识

## 被否定 / 降级的认识

## 新决策

# Open Questions

# Impact
影响哪些 Topic / Question / Hypothesis / Research State。

# Next
下一步最值得推进什么。
```

Checkpoint 优先记录 **Delta**，不要：

- 复制长对话；
- 写流水账摘要；
- 重复 Topic 正文；
- 保存已稳定且未变化的背景知识。

如果一轮工作没有产生长期状态变化，不创建 Checkpoint。

---

## 5. Progressive Context Loading

默认采用逐层展开，而不是全仓扫描：

```text
AGENTS.md
→ REPOSITORY_STATE.yaml
→ context/CURRENT.md
→ context/TOPIC_INDEX.md
→ 1–3 个相关 Topic State
→ 必要时 Question / Hypothesis / 最近 Checkpoint
→ 必要时 Research / Evidence / 原始材料
```

只有当上一层不足以完成任务时，才向下一层加载。

---

## 6. Checkpoint → Topic 更新协议

当本轮形成长期变化：

1. 先生成 Checkpoint，写清 Delta；
2. 读取受影响 Topic 当前状态；
3. 判断变化属于：新增 / 修正 / 覆盖 / 冲突 / 待验证；
4. 更新 Topic，仅保留最新有效状态；
5. 必要时再更新 Question / Hypothesis / NOW / CURRENT；
6. 若只是证据增加但没有状态变化，按原研究协议更新 Research / Evidence，不必强制写 Checkpoint。

---

## 7. Compaction 原则

Checkpoint 可以持续增加，但 Active Context 必须保持小。

当某 Topic 的历史 Checkpoint 已明显增加读取负担时：

```text
Checkpoint History
→ 提炼当前仍有效的认识
→ 更新 Topic State
→ 旧 Checkpoint 原样保留
→ 默认检索只读 Topic State，不再批量读取旧 Checkpoint
```

不设置机械数量阈值。触发条件是：

> **历史变化记录已经开始增加 Context Retrieval 成本，而 Topic State 已能承载当前有效状态。**

---

## 8. 与 EVOLUTION.md 的区别

- **Checkpoint**：任意长期 Topic 的增量变化事件，粒度可以较小；
- **EVOLUTION.md**：研究体系中真正改变问题定义、核心假设或研究方向的重要认知转折。

并非每个 Checkpoint 都进入 EVOLUTION；只有研究认知发生重大转折时，才按现有 EVOLUTION 规则升级。

---

## 9. 非目标

本层暂不引入：

- 向量数据库；
- 外部状态服务；
- 自动全量会话抓取；
- 全仓 Topic 化；
- 历史会话补录；
- 复杂自动路由程序；
- 数据库式知识图谱。

先验证 Markdown + Git + Progressive Loading 是否足够。
