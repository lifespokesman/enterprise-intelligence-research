# AGENTS.md｜Enterprise AI Research Runner v0.1

本仓库不是资料收藏库，而是一个**问题驱动、假设演进、证据约束**的企业 AI 研究系统。

Codex / 自动化任务在本仓库执行研究时，必须遵循以下规则。

---

## 1. 研究目标

每次自动研究的目标不是“搜更多资料”，而是：

> **推进当前 Active Problem 的一个最高优先级 Evidence Gap，并判断新证据是否改变当前 Hypothesis。**

研究闭环：

```text
Active Problem
→ Current Hypothesis
→ Evidence Gap
→ Targeted Research
→ Evidence Evaluation
→ Hypothesis Update
→ Next Evidence Gap
```

---

## 2. 每轮开始前必须读取

按顺序读取：

1. `NOW.md`
2. `research/RESEARCH_STATE.yaml`
3. 当前 active problem 文件
4. 对应 evidence ledger
5. 必要时再读取 `research/RESEARCH_LOOP.md`

如果这些文件之间存在冲突，以 `research/RESEARCH_STATE.yaml` 的当前运行状态为准，并在本轮结果中记录冲突。

---

## 3. 每轮只推进一个 Evidence Gap

只研究：

- `status: active`
- 且优先级最高
- 且由 `next_action` 指向

的 Evidence Gap。

禁止为了“完整”同时扩展多个主题。

如果当前 Gap 太大，允许拆成更小的 research task，但不要直接创建新的正式 Research Problem。

---

## 4. 证据搜索优先级

优先顺序：

1. 官方技术文档 / 产品文档
2. 开源实现 / 官方 GitHub
3. 学术论文 / 正式出版物
4. 官方工程博客 / 官方案例
5. 标准 / 协议 / 规范
6. 高质量第三方分析
7. 社区讨论

优先使用 Primary Source。

厂商宣传只能标记为 `Product Claim`，不能直接当作 `Product Fact`。

---

## 5. 每条 Evidence 必须回答

每条保留证据至少记录：

- Source
- URL
- Date
- Evidence Type
- Observed Fact
- Mechanism
- Target Hypothesis
- Effect
- Confidence

其中 Effect 只能使用：

- Supports
- Challenges
- Narrows
- Revises
- Rejects
- Opens Alternative

禁止只写“这篇材料讲了什么”。

---

## 6. 研究纪律

每轮最多保留 3–5 条**真正改变判断**的高价值证据。

禁止：

- 批量堆论文
- 批量堆产品链接
- 为支持既有观点而选择性找材料
- 把 Product Claim 写成 Architecture Fact
- 把 Working Hypothesis 升级为 Principle
- 自动修改 `PRINCIPLES.md`
- 自动创建新的正式 Research Problem
- 因出现新名词就扩展研究范围

必须主动寻找：

- Counter Evidence
- Alternative Hypothesis
- Boundary Condition
- Existing Architecture Pattern

---

## 7. Hypothesis 更新规则

当前假设必须保留版本演进。

允许：

```text
H0 → H1 → H2
```

每次变化必须写清：

- 旧假设
- 触发变化的 Evidence
- 变化原因
- 新假设
- 新增边界条件
- 尚未解决的 Gap

不允许为了“有进展”而强行修改假设。

如果证据不足，保持原状态。

---

## 8. 新问题处理

研究中发现的新问题只进入：

`candidate_questions`

只有人工审核后，才允许升级为：

- AQ
- CQ
- EQ
- VQ
- RP

自动化任务不得自行扩大正式问题树。

---

## 9. 停止条件

某个 Evidence Gap 满足以下任一条件时可设为 `saturated` 或 `closed`：

1. 已有 2–3 个独立来源，且至少 1 个 Primary / Implementation 级证据；
2. 已同时获得支持证据、限制条件和至少一种反例 / 替代解释；
3. 连续两轮没有 Material Update；
4. 已足以形成下一步 Engineering Hypothesis。

没有高价值增量时，明确记录：

`NO_MATERIAL_UPDATE`

不要制造伪进展。

---

## 10. 每轮结束必须更新

至少更新：

1. 当前 evidence ledger
2. `research/RESEARCH_STATE.yaml`

如确有认知变化，再更新当前 active problem 中的：

- Hypothesis Evolution
- Current Judgment
- Open Gaps

最后必须留下明确的：

`next_action`

使下一次自动任务无需人工重新解释背景即可继续。

---

## 11. 当前试运行范围

Research Runner v0.1 只围绕：

`RP-002-02｜Business Action Layer`

运行。

在 v0.1 验证完成前，不自动切换到其他正式问题。

成功标准：

> 在用户不持续贡献新观点的情况下，AI 能基于外部证据推动 H-RP002-06 从 H0 演化为更成熟的 H1 / H2，并主动识别下一 Evidence Gap。
