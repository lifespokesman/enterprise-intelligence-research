# Enterprise Intelligence Research｜论文阅读模式

Version: 2.0  
Updated: 2026-09-11  
用途：供新的 AI 会话按**问题驱动**方式开始或恢复论文学习。论文不是默认精读对象；先确认当前 Problem，再动态判断 A / B / C。

## 新会话短指令

> 请读取 GitHub 仓库 `lifespokesman/enterprise-intelligence-research`，依次读取 `ai-context/PROJECT_CONTEXT.md`、`NOW.md`、`research/RESEARCH_LOOP.md`、`research/research-questions.md`、`research/paper-review-plan.md`、`ai-context/PAPER_READING_MODE.md`。
>
> 本次材料：<论文 / URL / PDF>。
>
> 先告诉我：它在回答哪个当前 Concrete Problem？相对于这个问题属于 A / B / C 哪一类？为什么？不要默认开始全文精读。
>
> 如果是 A 类，再按 Part A–E 推进；如果是 B 类，只做定向理解与简版 Engineering Bridge；如果是 C 类，登记价值与升级条件后停止。

如果当前还没有清晰 Active Problem，先帮助研究者把问题写成一句可研究、可工程翻译的问题，再决定是否需要这篇论文。

---

## 1. 开始前｜先读问题，不先读论文队列

按需读取：

1. `PROJECT_CONTEXT.md`：项目定义、证据纪律与公开边界；
2. `NOW.md`：当前唯一动作；
3. `RESEARCH_LOOP.md`：问题 → 原理的主闭环；
4. `research-questions.md`：当前 Concrete Problem 与证据缺口；
5. `paper-review-plan.md`：A / B / C 与完成标准；
6. 当前论文原文；
7. 只有选文或比较材料时，再读 `reading-list.md`。

不要无差别加载整个仓库。

先核实标题、作者、版本、文献类型与原文是否完整可读。区分期刊论文、Editorial、Working Paper、预印本、综述和未核实材料。

---

## 2. 先做 A / B / C 判断

论文类别是**相对于当前 Problem**的动态关系，不是论文永久标签。

### A｜问题型论文

直接影响当前设计问题；若不理解作者完整论证，就无法形成可靠 Engineering Hypothesis。

→ 使用完整 Part A–E。

### B｜原则型论文

对当前问题只有长期原则性增量，或只需要其中某个机制。

→ 只做：来源边界 → 核心机制 → 改变的判断 → Principle 影响 → 简版 Engineering Bridge。

### C｜启发型论文

当前没有具体问题承接。

→ 只登记题录、潜在价值、可能关联问题、未来升级条件。停止。

如果 AI 无法说清论文为什么值得现在读，默认不进入 A 类。

---

# A 类论文｜Part A–E

## Part A｜Source Walkthrough 原文精读

目标：按作者自己的顺序恢复论证，而不是先用我们的框架总结。

解释：

1. 文献类型、证据与适用边界；
2. 作者真正想解决的问题；
3. A → B → C 的原始论证链；
4. Figure / Table / Typology 的维度、作用与限定条件；
5. 重要例子；
6. 作者明确的结论；
7. 作者没有解决的问题。

全程区分：

- `[原文]`
- `[作者引用的既有研究]`
- `[背景补充]`
- `[我们的推论]`

不要把 Q1–Q5、E/G Roadmap 或现有 JUDGMENTS 提前套到作者身上。

## Part B｜Concept Reconstruction 概念还原

只解释真正阻碍当前 Problem 理解的概念。每个重要概念回答：

1. 本文里是什么意思？
2. 为什么作者需要它？
3. 用一个简单、明确标记为虚构的企业例子解释；
4. 与相邻概念有什么区别？
5. 最容易误解成什么？
6. 作者自己讲到哪里？
7. 必要的经典理论补充是什么？

保留关键英文术语，不为了“完整课程”补所有背景。

## Part C｜Research Interpretation 研究解释

主要概念理解后，才进入研究映射：

1. 它对应 Q1–Q5 哪些问题？
2. 继承哪些经典理论？
3. 原理论的关键假设是什么？
4. AI 改变了哪个假设？也允许答案是“没有证明改变”；
5. 它带来的是新问题，还是旧问题的新解法？
6. 支持、挑战或修改哪些 JUDGMENTS？有哪些反例？
7. 哪些结论可能只在当前技术阶段成立？

**作者结论 ≠ 我们的研究解释 ≠ 研究者最终判断。**

## Part D｜Human Takeaways 人类吸收

形成：

- 真正掌握的 3–5 个概念 / 机制；
- 2–3 条长期记忆；
- 哪些旧认识发生变化；
- 是否值得写 EVOLUTION；
- 是否足以影响 JUDGMENTS；
- 还缺什么证据。

## Part E｜Engineering Bridge 工程桥接

这是问题驱动论文阅读的必要收尾，不以“论文总结”结束。

回答五件事：

1. **它解释了什么现实问题？**
2. **它改变了我什么旧判断？**
3. **如果成立，对工程设计意味着什么？**
4. **我可以在哪里、用什么方式验证？**
5. **验证后可能沉淀成什么架构 / 方法原则？**

模板：

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

Part E 的工程含义首先是 Hypothesis，不是论文“证明”出来的架构原则。

---

# B 类论文｜定向阅读模式

B 类不按 A–E 全流程展开。

一次完成以下内容即可：

1. 文献身份、问题与适用边界；
2. 1–3 个最有增量的机制 / 概念；
3. 它改变、支持或挑战什么已有判断；
4. 对哪条 Candidate Principle 有影响；
5. 简版 Engineering Bridge；
6. 什么时候值得升级为 A 类。

只要增量已经获得，就停止。不要为了“以后可能用到”把旁支全部读完。

---

# C 类论文｜候选池模式

只登记：

- Citation / Source；
- 一句话潜在价值；
- 可能关联的 Concrete Problem / Q；
- 当前为什么不读；
- 升级 A / B 的触发条件。

不输出长摘要，不创建学习债务。

---

## 3. 研究节奏

- 一次只保留一个 Active Problem，不是一个 Active Paper。
- 可以围绕同一 Problem 同时搜索多种证据，但不要同时深读多篇。
- A 类论文的阅读深度以“足够工程翻译”为停止条件，不以页数或论文完整度为目标。
- B / C 类材料不进入连续多轮教学。
- 论文无法解释当前 Problem 时，允许直接停止或降级。

研究进度优先看：

> 解决了几个问题？形成了哪些 Engineering Hypothesis？验证了什么？沉淀 / 修正了哪些 Principle？

而不是：

> 读完了多少篇论文？

---

## 4. 公开边界与验证

私人工作经验可以触发问题，但本公开仓不保存私人项目证据链。

Part E 的 Validation Plan 在公开研究中优先使用：

- 公开案例；
- 开源项目；
- 合成 Demo；
- 公开 Benchmark；
- Product Fact / Industry Case；
- Policy / Standard；
- Counter Evidence。

不能把虚构教学例子或私人经验包装成公开实证。

---

## 5. 收尾与仓库更新

结束一轮论文工作时按需更新：

- `research/research-questions.md`：Problem / Evidence Gap / Engineering Translation / Validation；
- 当前 paper review：必要的原文理解与 Engineering Bridge；
- `reading-list.md`：材料的实际增量与状态；
- `PRINCIPLES.md`：只有出现明确 Candidate Principle / 状态变化时；
- `EVOLUTION.md`：只有发生实质认知变化时；
- `JUDGMENTS.md`：未经研究者确认不升级；
- `NOW.md`：保存下一步唯一动作。

AI Proposal 不能自动成为研究者 Judgment 或 Stable Principle。
