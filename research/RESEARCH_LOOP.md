# Enterprise AI Research Loop｜企业 AI 问题驱动研究闭环

> 研究的基本单位不是“论文”，而是**一个真实、可解释、可工程化的问题**。
>
> 核心原则：**以真实问题牵引理论，以工程翻译连接研究，以小规模验证筛选假设，以架构与方法原则沉淀认知。**

## 1. 主闭环

`真实问题 → 理论 / 产业搜索 → 理解 → 工程翻译 → 小规模验证 → 架构 / 方法原则 → 新问题`

对应七步：

1. **真实问题｜Problem**  
   先回答：到底什么地方解释不了、设计不清、反复出现、或者现有架构原则无法解释？
2. **理论 / 产业搜索｜Search**  
   论文、开源项目、产品机制、公开案例、Analyst View、Policy / Standard 中，谁研究或工程化过类似问题？
3. **理解｜Understand**  
   材料真正提出了什么机制、变量、因果关系、条件、反例或新视角？
4. **工程翻译｜Translate**  
   如果这个机制成立，对架构、组件、流程、治理、角色和评价意味着什么？形成 Engineering Hypothesis，而不是直接升级为原则。
5. **小规模验证｜Validate**  
   通过公开案例、开源实现、合成 Demo、公开 Benchmark 或其他可复核方式验证关键假设。私人工作可以启发问题，但不进入本公开仓的证据链。
6. **架构 / 方法原则｜Principle**  
   只有经过足够理解与验证后，才沉淀为可复用原则，并明确适用条件、反例和证据来源。
7. **新问题｜Next Problem**  
   问：原则在哪些边界下失效？又暴露出什么新的工程或组织问题？进入下一轮。

一句话：

> **问题牵引研究，理论支撑解释，工程完成翻译，实践负责验证，原则负责沉淀，新问题推动下一轮。**

---

## 2. 仓库中的层级关系

Q1–Q5 仍然是长期问题地图，但真正执行研究时需要把它们拆成更具体的问题。

```text
Q1–Q5 Long-term Questions
          ↓
Concrete Research Problem
          ↓
Theory + Public Industry Evidence
          ↓
Engineering Hypothesis
          ↓
Validation
          ↓
Architecture / Method Principle
          ↓
New Problem
```

各类资产职责：

- `research/research-questions.md`：当前具体问题、证据缺口、工程翻译与验证状态；
- `research/reading-list.md`：论文与材料索引，不承担“必须依次读完”的队列职责；
- `research/paper-reviews/`：必要的原文理解、概念还原与研究解释；
- `industry/`：公开产品、案例与产业机制证据；
- `PRINCIPLES.md`：已形成或正在验证的架构 / 方法原则；
- `JUDGMENTS.md`：关于企业智能本身的阶段判断；
- `EVOLUTION.md`：记录为什么认知发生变化。

`Judgment` 与 `Principle` 不同：

- **Judgment**：我们目前认为“世界可能是怎样的”；
- **Principle**：如果这些判断和证据成立，“工程上应该怎样设计”。

---

## 3. 论文不是默认都精读：A / B / C 三层

论文等级是**相对于当前问题动态判断**的，不是论文永久属性。同一篇论文在不同问题下可以从 C 升为 B，也可以从 B 升为 A。

### A 类｜问题型论文——精读

直接影响当前核心问题或工程设计。

适用条件：

- 当前已经有清晰问题；
- 论文的核心机制可能改变设计选择；
- 需要理解作者完整论证、条件和边界才能工程翻译。

处理方式：

`Source Walkthrough → Concept Reconstruction → Research Interpretation → Human Takeaways → Engineering Bridge`

目标不是“读完”，而是足够形成可验证的 Engineering Hypothesis。

### B 类｜原则型论文——理解核心机制即可

当前不能马上解决问题，但可能改变长期架构或方法原则。

只保留：

- 核心观点 / 机制；
- 它改变了什么旧判断；
- 可能影响哪条 Principle；
- 未来什么条件下需要重新升级精读。

不要求完整逐段 walkthrough，不制造“以后必须补完”的学习债务。

### C 类｜启发型论文——候选池

有意思、可能重要，但当前没有真实问题承接。

只登记：

- 题录；
- 一句话可能价值；
- 可能关联的问题；
- 升级条件。

不精读、不强行内化、不因为收藏而形成待办压力。

---

## 4. Part E｜Engineering Bridge｜工程桥接卡

每篇真正重要的论文，不以“论文总结”为终点。至少回答五件事：

1. **它解释了什么现实问题？**
2. **它改变了我什么旧判断？**
3. **如果成立，对工程设计意味着什么？**
4. **我可以在哪里、用什么方式验证？**
5. **验证后可能沉淀成什么架构 / 方法原则？**

建议模板：

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

工程桥接卡允许答案是“当前还不能翻译成工程原则”。没有工程含义不等于论文没有价值，但不应为了填表而虚构设计结论。

---

## 5. 从论文知识到原则库

长期资产链应逐渐形成：

```text
Enterprise Problem
   ↓
Theory / Paper / Product / Case
   ↓
Mechanism Understanding
   ↓
Engineering Hypothesis
   ↓
Public / Synthetic Validation
   ↓
Architecture / Method Principle
   ↓
Applicable Conditions + Counter Evidence
```

研究进度不以“读了多少论文”衡量，而优先看：

- 解决了几个真实问题；
- 形成了几个清晰 Engineering Hypothesis；
- 哪些假设得到了验证或被否定；
- 形成了几条可复用原则；
- 哪些旧原则被新证据修正。

---

## 6. 公开仓边界

真实工作、私人或公司内部经验可以触发研究问题，但公开仓只保留**抽象后的问题**。

公开验证优先使用：

- Academic Theory；
- Product Fact / Product Claim；
- Public Industry Case；
- Analyst View；
- Policy / Standard；
- Counter Evidence；
- Open-source implementation；
- Synthetic / public benchmark。

本仓库不记录私人项目的来源、行业身份、数据、系统、客户或验证细节。私人验证不会自动成为公开结论的证据。

---

## 7. 停止条件

一轮研究可以在任何环节停止，不要求七步一次走完。

- 问题不够清楚：停止搜索，先定义问题；
- 材料只是 C 类：登记后停止；
- B 类已获得原则性增量：停止，不补完整精读；
- A 类已足以形成 Engineering Hypothesis：可以结束论文阅读，进入验证；
- 验证证据不足：保留 Candidate Principle，不升级；
- 原则边界已经暴露：形成新问题，进入下一轮。

> **研究闭环的完成标志不是“读完材料”，而是问题获得了更好的解释、设计或验证。**

_Last updated: 2026-09-11_
