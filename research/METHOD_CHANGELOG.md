# METHOD CHANGELOG｜研究方法版本变更记录

> 本文件只记录**研究方法为什么变化、变化了什么、如何判断是否继续保留，以及怎样回滚**。它不是研究结论，也不进入 `JUDGMENTS.md`。

---

## v2.0｜从“问题驱动证据研究”升级为“问题驱动的假设—验证研究”

Date: 2026-09-13  
Origin: `User Insight + Co-developed`

### Before｜v1.0

此前主闭环：

`真实问题 → 理论 / 产业搜索 → 理解 → 工程翻译 → 小规模验证 → 原则 → 新问题`

结构化表达：

`Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle → New Problem`

v1.0 解决了“按论文顺序学习”的问题，使研究回到真实问题本身。

### Trigger｜为什么要升级

在 RP-002 的讨论中，连续出现了多个现实问题刺激后形成的初步解决想法，例如：

- 不同企业数字化基础可能对应不同 AI Context 建设路径；
- 不同路径可能收敛到“业务事实 → 动态 Context → Agent → Outcome → Feedback”的逻辑闭环；
- 判断 AI Context Readiness 可能不能简单用“有没有大数据平台”代理，而要看事实捕获、对象 / 流程稳定和反馈闭环。

这些想法出现时还没有经过理论、产品、公开案例或工程验证，但如果只记录 Problem，研究者会丢失“当时为什么觉得这个问题值得研究、最初是怎么猜的”。

同时，如果把这些想法直接写成 Engineering Translation 或 Principle，又会模糊“研究前直觉”和“研究后结论”的边界。

### Shift｜关键变化

研究的最小沉淀对象从：

> `Problem`

升级为：

> `Problem + Initial Hypothesis + Candidate Solution Path`

新的主闭环：

`Signal → Problem → H0 / Candidate Path → Evidence → Mechanism → H1 → Engineering Hypothesis → Validation → Principle → New Problem`

核心变化不是简单增加步骤，而是引入了**研究前状态**和**假设演进状态**。

### Why It Matters｜为什么重要

这更贴近实际思考过程：

1. 现实先刺激出问题；
2. Human–AI 讨论通常会先形成一个暂时解释或解决办法；
3. 研究不是从零找答案，而是压力测试这个暂时解释；
4. Theory / Product / Case / Open Source / Counter Evidence 的作用，是支持、限制、修正或推翻假设；
5. 工程验证再判断候选解决路径是否有效；
6. 只有经过检验的结果才进入 Principle。

因此真正值得积累的不只是最终答案，还包括：

> **H0 → Evidence → H1 的认知变化。**

### Anti-confirmation Rule｜防止确认偏误

v2.0 最大风险是“先有假设以后，只找证明自己正确的材料”。

因此每个重要 H0 尽量同时记录：

- Supporting Evidence Needed；
- Disconfirming Evidence Needed；
- Alternative Hypothesis；
- Counter Evidence；
- 当前证据对 H0 的作用：Supports / Challenges / Narrows / Revises / Rejects / Opens Alternative。

核心纪律：

> **研究不是寻找支持假设的证据，而是寻找足以判断假设是否成立的证据。**

### What Does Not Change｜不变的部分

此次升级不改变以下长期规则：

- Problem-driven，而不是 Paper-driven；
- Q1–Q5 / RP / CQ-AQ-EQ-VQ 的 Problem Map 继续有效；
- 论文仍按 A / B / C 相对当前问题动态分级；
- 公开仓只研究公开世界；
- Theory 与 Public Industry Evidence 共同提供证据；
- Product Claim 不等于事实或理论；
- Judgment 与 Principle 分开；
- Principle 必须经过足够机制理解与验证；
- AI Proposal 不自动成为研究者 Judgment。

### Trial Criteria｜怎样判断 v2 是否值得保留

后续几个 RP 中观察：

1. 是否更容易从中断状态恢复“问题为什么重要、当时怎么想”；
2. Evidence 搜索是否因此更聚焦，而不是更窄；
3. 是否能清楚看到 H0 被支持、修改或否定；
4. Candidate Solution Path 是否更容易进入工程验证；
5. 方法维护成本是否低于它带来的研究收益；
6. 是否因为提前写假设而明显增加确认偏误。

### Rollback｜如何回滚

v2.0 被视为**可逆的研究方法试验**，不是不可修改的制度。

升级前仓库基线 commit：

`b56caf344de02cfef30b9a7d607baf9d609615b5`

如果未来判断 v2 不适合，可以有三种回退方式：

1. **轻回退**：保留 H0 记录，但不强制每个 Problem 都写 Candidate Solution Path；
2. **中回退**：恢复 v1 执行链，已有 Hypothesis 仅作为普通 Working Note 保留；
3. **完整方法回滚**：以升级前 commit 为参考恢复 `research/RESEARCH_LOOP.md` 等方法文件。

回滚方法不意味着删除 v2 期间形成的有效研究成果。研究内容与研究流程要分开判断。

### Related Files

- `research/RESEARCH_LOOP.md`：v2.0 正式执行规则；
- `research/research-questions.md`：Problem Map 与具体 Hypothesis；
- `NOW.md`：当前 Active Problem 和下一步；
- `EVOLUTION.md`：若该方法长期证明有效，再视需要把此次变化纳入长期认知演进主记录。

---

## Version Index

| Version | Date | Core | Status |
|---|---|---|---|
| v1.0 | 2026-09-11 | Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle | Historical baseline |
| **v2.0** | **2026-09-13** | Signal → Problem → H0 / Candidate Path → Evidence → H1 → Engineering Validation → Principle | **Current / Trial** |
