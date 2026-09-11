# Paper Review Plan｜问题驱动的论文学习执行计划

> 论文不是研究主线，只是回答具体问题的一类证据。
>
> 先有 Problem，再决定论文是否值得读、读多深。完整研究闭环见 [`RESEARCH_LOOP.md`](RESEARCH_LOOP.md)；新会话执行规则见 [`PAPER_READING_MODE.md`](../ai-context/PAPER_READING_MODE.md)。

## 1. 入口职责

- [`NOW.md`](../NOW.md)：当前唯一动作与停止位置；
- [`research-questions.md`](research-questions.md)：当前具体 Problem、证据缺口、工程翻译与验证状态；
- [`reading-list.md`](reading-list.md)：论文身份、来源、相对增量与可读性索引；
- 本文件：论文 A/B/C 分级、完成标准与 Part E；
- [`PAPER_READING_MODE.md`](../ai-context/PAPER_READING_MODE.md)：新会话实际执行方式；
- [`PRINCIPLES.md`](../PRINCIPLES.md)：最终要沉淀的架构 / 方法原则。

论文编号不是顺序，reading-list 不是必须读完的队列。

---

## 2. 先分类，再阅读：A / B / C

论文类别是相对于当前 Problem 动态判断的，同一篇论文在不同问题下可以改变等级。

### A 类｜问题型论文——精读

直接解释当前核心问题，且作者的完整论证可能改变工程设计。

执行：

`A Source Walkthrough → B Concept Reconstruction → C Research Interpretation → D Human Takeaways → E Engineering Bridge`

停止条件：已经足以形成清晰的 Engineering Hypothesis，并知道还缺什么验证。**不要求为了“学术完整”把所有旁支都读完。**

### B 类｜原则型论文——定向理解

当前不会直接改变工程方案，但可能修正长期判断或原则。

执行只需：

1. 核实论文类型、边界与核心问题；
2. 理解 1–3 个真正有增量的机制 / 概念；
3. 说明改变了什么旧判断；
4. 说明影响哪条 Candidate Principle；
5. 写一个简版 Engineering Bridge；
6. 满足当前增量后停止。

不要求完整逐段 walkthrough，不制造“以后必须补完”的学习债务。

### C 类｜启发型论文——候选池

感觉重要或有趣，但当前没有具体 Problem 承接。

只登记：题录、一句话潜在价值、可能关联问题、未来升级条件。**不精读、不强行内化。**

---

## 3. A 类论文五阶段

### Part A｜Source Walkthrough

按作者顺序恢复：文章类型、原始问题、论证链、证据、图表、例子、结论和未解决问题。

### Part B｜Concept Reconstruction

只解释阻碍当前理解的关键概念，保留英文术语并区分 `[原文] / [作者引用] / [背景补充] / [我们的推论]`。

### Part C｜Research Interpretation

主要概念理解后，再回答 Q1–Q5、经典理论、关键假设、AI 改变了什么、对 JUDGMENTS 的支持/挑战及阶段性边界。

### Part D｜Human Takeaways

形成真正掌握的概念、长期记忆、认知变化、EVOLUTION 候选和剩余问题。

### Part E｜Engineering Bridge

重要论文必须继续回答：

1. 它解释了什么现实问题？
2. 它改变了什么旧判断？
3. 如果成立，对工程设计意味着什么？
4. 在哪里、用什么方式验证？
5. 验证后可能沉淀成什么架构 / 方法原则？

Part E 的结果首先是 **Engineering Hypothesis / Candidate Principle**，不能因为论文逻辑完整就直接升级为稳定原则。

---

## 4. 当前材料的处理方式｜2026-09-11

- **P-001**：理论理解已完成。它不再因为“编号最前”被重复精读；已转化出的具体问题见 R-001 / R-003。
- **P-002**：原文已具备，但不再自动作为“下一篇必须读完”。只有在当前 Problem 需要判断管理者工作、目的、规范适当性或决策权边界时，才作为 A / B 类进入。
- **P-003**：题录与原文待核验；没有当前问题承接时保持 C / Backlog。
- **P-004**：多 Agent 组织方向候选；只有 R-001 / Q3 需要扩展到多 Agent 失效机制时升级。
- **P-005**：与 R-001 的“聚合何时值得”直接相关，若 R-001 进入 Active，可优先升级为 A 类。

原计划 `P-001 → P-002 → P-003` 只保留为历史记录，不再作为研究执行顺序。

---

## 5. 每篇重要论文最终产物

终点不是“论文总结”，而是**工程桥接卡**。

```markdown
## Engineering Bridge

Problem:

What the paper explains:

Changed judgment:

Engineering hypothesis:

Validation plan:

Candidate principle:

Boundary / counterexample:
```

允许结论是：

- 当前只能解释机制，尚不能工程化；
- 工程含义存在，但没有验证方法；
- 对当前 Problem 没有足够增量，应停止阅读。

---

## 6. 阅读与研究停止条件

| 情况 | 正确动作 |
|---|---|
| Problem 还不清楚 | 停止搜论文，先定义问题 |
| C 类论文 | 登记后停止 |
| B 类已经获得原则性增量 | 停止，不补全文 |
| A 类已形成 Engineering Hypothesis | 结束阅读，转向验证 |
| 理论理解完成但企业应用仍缺证据 | 分开管理，不继续用更多论文假装完成验证 |
| Candidate Principle 缺验证 | 保持 Candidate，不升级 |
| 新证据推翻假设 | 记录 Counter Evidence / EVOLUTION，修改原则 |

**阅读速度不是目标，但深度也不等于把每篇论文都读到同一深度。**

---

## 7. 新材料准入

发现新论文时先问：

1. 当前具体 Problem 是什么？
2. 它相比已有材料新增什么机制、数据、边界或反例？
3. 它是 A、B 还是 C？
4. 读后要得到什么 Engineering Bridge？

不能回答以上问题，就先不读。

---

## 8. 仓库更新规则

一次研究结束后按需更新：

1. `research-questions.md`：Problem、Evidence Gap、Engineering Translation、Validation；
2. 当前 paper review：原文理解 / Engineering Bridge；
3. `reading-list.md`：材料身份与实际增量；
4. `PRINCIPLES.md`：只有形成明确 Candidate Principle 或原则状态变化时更新；
5. `EVOLUTION.md`：只有认知发生实质变化时更新；
6. `JUDGMENTS.md`：只有研究者明确认可且证据足够时更新；
7. `NOW.md`：保存唯一下一步。

公开仓不记录私人项目证据链。

_Last updated: 2026-09-11_
