# Enterprise AI Research Loop｜企业 AI 问题驱动的假设—验证研究闭环

Version: **v2.0**  
Updated: 2026-09-13

> 研究的基本单位不再只是“一个问题”，而是一个 **Problem + Hypothesis Package｜问题—假设包**。
>
> 核心原则：**现实负责出题，Human–AI 共创先形成候选解释与解决路径，理论与产业证据负责压力测试，工程实践负责验证，原则只保存经得起检验的结果。**

---

## 1. 为什么从 v1 升级到 v2

v1 的主闭环是：

`Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle → New Problem`

它解决了“论文驱动学习”的问题，但仍隐含一个假设：遇到问题以后，先去外部材料里寻找答案。

实际研究过程往往不是这样。现实问题出现后，研究者通常已经会基于经验、已有认知和 Human–AI 讨论形成一个**初始解释**，甚至一个**候选解决办法**。真正的研究任务不是假装自己没有想法，而是把这个想法明确降级为 Hypothesis，再主动寻找支持、限制、修正和反驳它的证据。

因此 v2 增加“研究前状态”和“假设演进状态”。

---

## 2. v2 主闭环

```text
Phenomenon / Signal
现实刺激
        ↓
Problem Abstraction
问题抽象
        ↓
Initial Hypothesis / Candidate Solution Path
初始假设 / 候选解决路径
        ↓
Evidence Search
Theory / Product / Open Source / Case / Standard / Counter Evidence
        ↓
Mechanism Understanding
机制理解
        ↓
Hypothesis Update
Support / Revise / Reject / Split
        ↓
Engineering Hypothesis
可工程验证的设计主张
        ↓
Validation
Demo / Benchmark / Public Case / Comparative Test
        ↓
Architecture / Method Principle
        ↓
Boundary / New Problem
```

一句话：

> **先把“我现在怎么猜”保存下来，再研究“这个猜测到底对不对”，最后才决定“工程上应该怎么做”。**

---

## 3. Problem + Hypothesis Package｜最小研究包

一个值得持续研究的问题，最先沉淀的不是长篇资料，而是下面五项。

### 3.1 Phenomenon｜现象

现实中看到了什么反常、重复、解释不清或设计困难的现象？

公开仓只保留可公开表达的抽象现象，不保存私人项目来源、客户身份或非公开证据链。

### 3.2 Problem｜问题

真正解释不了、设计不清或需要做选择的是什么？

Problem 应尽量能映射到现有 RP / CQ / AQ / EQ / VQ，而不是因为出现新名词就建立新问题域。

### 3.3 Initial Hypothesis｜初始假设 H0

基于当前认知，我们暂时认为：

- 为什么会出现这个现象？
- 哪个机制可能最关键？
- 哪些变量可能决定结果？

H0 是研究起点，不是结论。

### 3.4 Candidate Solution Path｜候选解决路径 S0

如果 H0 大体成立，当前可能的解决方向是什么？

它可以是一条架构链、方法、建设路径、分类框架或诊断模型。允许暂时粗糙，但必须明确标记为 Candidate / Hypothesis，不能直接写成 Principle。

并非所有问题一开始都有 Solution Path；没有就留空，不强行补答案。

### 3.5 Evidence Needed｜需要什么证据

至少考虑：

- 什么证据会**支持**这个假设？
- 什么证据会**限制 / 修正**这个假设？
- 什么证据会**直接反驳**它？
- 有没有合理的 **Alternative Hypothesis｜替代解释**？

这一步用于防止问题驱动退化成“给自己的直觉找论据”。

---

## 4. 假设状态与演进

建议对重要假设使用以下状态：

- **Initial**：现实刺激 + Human–AI 讨论形成，尚未系统检验；
- **Exploring**：正在寻找理论 / 产品 / 案例 / 反例；
- **Supported**：多源证据支持，但仍有边界；
- **Revised**：原假设部分成立，已被证据修改；
- **Rejected**：关键预测或机制被证据否定；
- **Split**：发现原来把多个不同机制混成了一个假设。

研究价值不只来自“证明 H0 正确”。

> **H0 → H1 的变化本身就是研究成果。**

因此 Evidence 进入以后，要明确记录它对当前假设的作用：

`Supports / Challenges / Narrows / Revises / Rejects / Opens Alternative`

而不是只记录“这篇材料讲了什么”。

---

## 5. 从 Initial Hypothesis 到 Engineering Hypothesis

二者必须区分。

### Initial Hypothesis

回答：

> 世界为什么可能是这样？问题可能由什么机制产生？

例如：AI Context Readiness 可能主要受真实事实捕获、对象 / 流程稳定度和反馈闭环影响。

### Candidate Solution Path

回答：

> 如果这个解释大体成立，目前可以怎样设计？

例如：业务事实 → 对象 / 状态 / 规则 / 权限 / 证据 → 动态 Context → Agent → Outcome → Feedback。

### Engineering Hypothesis

回答：

> 哪个具体设计选择能够被比较、测量或推翻？

例如：在某类任务中，`RAG + structured facts + task context` 是否比 `RAG only` 在 Freshness / Traceability / Accuracy 上显著更好。

只有到了这一层，才进入 Demo、Benchmark、公开案例对比或其他工程验证。

---

## 6. Evidence Search｜证据不是为了“证明自己对”

公开研究优先使用：

- **[Theory]** Academic Theory；
- **[Product Fact]** 可核验产品机制；
- **[Product Claim]** 厂商自身主张；
- **[Open-source Implementation]** 可检查的工程实现；
- **[Industry Case]** 公开企业实践；
- **[Analyst View]** 第三方分析；
- **[Policy / Standard]** 政策与标准；
- **[Counter Evidence]** 失败案例、反例、替代实现；
- Synthetic / public benchmark 等可复核验证。

证据搜索时优先问：

1. 它支持 H0 的哪一部分？
2. 它要求给 H0 增加什么条件？
3. 它是否说明我们混淆了两个机制？
4. 有没有另一条更简单的解释同样能解释现象？
5. 有没有不采用当前 Solution Path 也能成功的反例？

纪律：

> **研究不是寻找支持假设的证据，而是寻找足以判断假设是否成立的证据。**

---

## 7. 论文仍按 A / B / C 动态分级

论文等级相对于当前 Problem / Hypothesis 动态判断，不是论文永久属性。

### A 类｜问题型论文

直接改变当前 H0、机制解释或 Engineering Hypothesis，需要精读。

处理：

`Source Walkthrough → Concept Reconstruction → Research Interpretation → Human Takeaways → Engineering Bridge`

### B 类｜原则型论文

提供长期机制或边界，但暂不直接决定当前设计。理解核心即可。

### C 类｜启发型论文

当前没有 Problem / Hypothesis 承接，只登记，不制造学习债务。

论文不再只回答“它说了什么”，还要回答：

> **它对当前哪个 Hypothesis 产生了 Supports / Challenges / Revises / Rejects？**

---

## 8. Engineering Bridge｜工程桥接卡 v2

重要论文、产品或案例的桥接记录至少回答：

```markdown
## Engineering Bridge

Problem:

Current hypothesis (H0/H1):

Candidate solution path:

What this evidence explains:

Effect on hypothesis:
Supports / Challenges / Narrows / Revises / Rejects / Alternative

Mechanism learned:

Revised hypothesis:

Engineering hypothesis:

Validation plan:

Candidate principle:

Boundary / counterexample:
```

允许结论是：

- H0 暂时不成立；
- 只能形成 Revised Hypothesis；
- 暂时没有工程含义；
- 还不足以提出 Principle。

不要为了填表制造结论。

---

## 9. 从假设到原则

长期资产链调整为：

```text
Real-world Signal
   ↓
Problem
   ↓
Initial Hypothesis / Candidate Path
   ↓
Theory + Public Industry Evidence + Counter Evidence
   ↓
Mechanism Understanding
   ↓
Revised Hypothesis
   ↓
Engineering Hypothesis
   ↓
Public / Synthetic Validation
   ↓
Architecture / Method Principle
   ↓
Applicable Conditions + Counter Evidence
```

原则不是“一个看起来合理的解决办法”。

只有当一个解决思路经过足够的机制理解和验证后，才考虑进入 `PRINCIPLES.md`。

研究进度优先看：

- 形成了几个清晰 Problem + Hypothesis Package；
- 哪些 H0 被支持、修改、拆分或否定；
- 哪些 Solution Path 被工程证据支持或淘汰；
- 形成了哪些可验证 Engineering Hypothesis；
- 哪些最终成为 Architecture / Method Principle。

---

## 10. 与 Problem Map 的关系

Q1–Q5 仍是长期问题地图；RP / CQ / AQ / EQ / VQ 负责组织问题纵深。

每个 RP 内部允许存在多个 Hypothesis 和 Candidate Solution Path。

```text
Q1–Q5
  ↓
RP
  ↓
CQ / AQ / EQ / VQ
  ↓
H0 / Candidate Path
  ↓
Evidence
  ↓
H1 / Engineering Hypothesis
  ↓
Validation
  ↓
Principle
```

因此“问题分类”和“假设验证”是两套正交结构：

- Problem Map 回答：**我们在研究什么问题？**
- Hypothesis Loop 回答：**我们现在怎么猜？怎样知道这个猜测靠不靠谱？**

---

## 11. 公开仓边界

真实工作、私人或公司内部经验可以触发 Signal / Problem / H0，但公开仓只保留抽象后的问题与假设。

公开 Hypothesis、Principle 和 Judgment 的论证不得依赖私人项目来源才能成立。

私人工作可以帮助发现“什么值得研究”，但公开验证重新依赖公开 Theory / Product / Case / Open-source / Standard / Counter Evidence。

---

## 12. 停止条件

一轮研究不要求走完整个闭环。

- 现象尚未抽象成清楚问题：停止搜索；
- 有 Problem 但没有合理 H0：允许保持 Open Problem；
- H0 已有但没有证据：保持 Initial，不伪装成结论；
- 证据足以修改 H0：先记录 H1，不急于进入工程；
- Engineering Hypothesis 已可验证：进入最小 Demo / Benchmark；
- 验证不足：停在 Candidate，不升级 Principle；
- 假设被否定：记录 Rejected / Revised，本轮仍然是有效研究成果；
- 新边界出现：形成 New Problem，进入下一轮。

> **研究闭环的完成标志，不是“证明最初想法是对的”，而是问题、假设和解决路径经过证据与实践后变得更接近真实。**

---

## 13. 版本与回滚

本文件采用可回滚的方法版本管理。

- **v1.0**：Problem-driven Evidence Research  
  `Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle`
- **v2.0**：Problem-driven Hypothesis–Validation Research  
  `Signal → Problem → H0 / Candidate Path → Evidence → Mechanism → H1 → Engineering Validation → Principle`

v2.0 是当前试运行方法，不宣称永久优于 v1.0。

如果后续发现 v2.0 导致以下问题，可以回退或收缩：

- 初始假设让研究确认偏误更强；
- 为每个小问题维护 H0/H1 产生过重管理成本；
- 很多探索型问题在研究前根本不适合提出 Solution Path；
- 方法记录开始压过真实研究本身。

**升级前仓库回滚基线：** `b56caf344de02cfef30b9a7d607baf9d609615b5`。

如需回滚方法，不代表要丢弃升级后形成的研究内容；优先恢复 v1 的执行规则，再人工保留已经证明有价值的 Hypothesis 资产。
