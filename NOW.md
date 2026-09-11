# NOW｜当前研究驾驶舱

> 这个文件只服务于“快速恢复研究状态”。现在的研究单位是 **Active Problem**，不是 Active Paper。

Updated: 2026-09-11

## 1. 当前方法已经切换：从“论文驱动”到“问题驱动”

过去一周暴露的问题是：按 P-001 → P-002 → P-003 一篇篇读，容易把“读论文”本身当成任务。一篇论文即使理解很深，也不等于真实问题得到解释、工程翻译或验证。

现在采用主闭环：

> **真实问题 → 理论 / 产业搜索 → 理解 → 工程翻译 → 小规模验证 → 架构 / 方法原则 → 新问题**

研究进度优先看：

- 解决了几个真实问题；
- 形成了哪些 Engineering Hypothesis；
- 哪些假设被验证 / 否定；
- 形成或修正了哪些 Architecture / Method Principle。

完整方法：[`research/RESEARCH_LOOP.md`](research/RESEARCH_LOOP.md)。

---

## 2. 当前 Active Problem｜R-001

**给定一个高价值企业判断任务，Human 与 AI 应何时单主体、专业化分工或判断聚合？最终决策权和反馈怎样设计，才能既获得能力收益，又保持责任、学习与可验证性？**

关联：Q1 / Q3 / Q5；并与 G3 Human Control / Accountability 相连。

为什么现在值得研究：

- P-001 已经提供了分工、Task Interdependence、学习配置等理论语言；
- 但“理解分类”还没有自动变成企业任务的设计原则；
- 这个问题可以把论文知识真正桥接到任务设计、反馈架构和验证方法。

具体问题地图见 [`research/research-questions.md`](research/research-questions.md)。

---

## 3. 当前论文不再按编号顺序推进

论文按当前 Problem 动态分 A / B / C：

- **A 类**：直接改变当前问题的工程设计，需要精读；
- **B 类**：只提供长期原则或局部机制，定向理解即可；
- **C 类**：当前没有问题承接，只登记候选。

当前材料：

- **P-001**：对 R-001 属于 A 类，2026-09-07 已完成本轮理论理解；不重复整篇精读。
- **P-002**：先按 **B → 可升级 A** 处理。已完成文献类型、开场问题与五类管理者工作的初步梳理；接下来只定向处理 technical performance、normative appropriateness、purpose 及其决策权含义。如果形成重大工程增量，再升级为 A 类继续完整 A–E。
- **P-005**：对 R-001 的“判断聚合何时值得”更直接，进入该子问题时可升级为 A 类。
- **P-003 / P-004**：保持候选，不因编号或已收集就自动开启。
- **P-006**：世界模型 Position / roadmap paper；对 R-001 为 C 类登记，不打断 P-002。只有问题转向 Enterprise Context / World Model、Agent 自主性或跨主体编排时再升级 B 类。

`reading-list.md` 是材料索引，不是待读清单。

---

## 4. 论文阅读现在增加 Part E｜Engineering Bridge

重要论文不能停在摘要、七问或 Human Takeaways。

最终至少回答：

1. 它解释了什么现实问题？
2. 它改变了我什么旧判断？
3. 如果成立，对工程设计意味着什么？
4. 可以在哪里、用什么方式验证？
5. 验证后可能沉淀成什么架构 / 方法原则？

完整模式：[`ai-context/PAPER_READING_MODE.md`](ai-context/PAPER_READING_MODE.md)。

---

## 5. 新的长期沉淀对象｜PRINCIPLES

新增：[`PRINCIPLES.md`](PRINCIPLES.md)。

当前研究资产职责：

- `NOW.md`：当前 Active Problem 与下一步；
- `research/research-questions.md`：具体问题、证据缺口、工程翻译和验证；
- `EVOLUTION.md`：认知为什么变化；
- `JUDGMENTS.md`：目前认为“世界怎样”；
- `PRINCIPLES.md`：工程 / 研究应该怎样做；
- `topics/`：成熟观点的体系化公开表达。

原则状态区分 Candidate / Supported / Stable / Revised / Deprecated，不因论文写得好就自动升级。

---

## 6. P-001 当前状态

P-001 本轮理论理解完成。核心增量包括：

- 专业化收益 / 聚合收益是收益机制，不是 Figure 2 的分类维度；
- Figure 2：相同 / 不同决策任务 × 并行 / 串行；
- Table 1：独立 / 相互依赖反馈 × 交流受限 / 可行；
- Task Interdependence、Agent / Feedback Interdependence、Censored Inputs、Superstitious Learning 要分开；
- 组织结构会改变未来学习机会，而不只是利用当前能力差异。

但 P-001 只完成了“理解机制”。R-001 仍需工程翻译与验证。

相关：

- [`P001 source walkthrough`](research/paper-reviews/P001_puranam_2021_source-walkthrough.md)
- [`P001 research review`](research/paper-reviews/P001_puranam_2021_hacd.md)

---

## 7. 公开研究边界不变

公开仓只研究公开世界。

> **私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。**

公开验证优先使用 Theory、Product Fact / Claim、Industry Case、Analyst View、Policy / Standard、Counter Evidence、开源实现、合成 Demo 与公开 Benchmark。

---

## 8. 下一步唯一动作

**围绕 R-001，对 P-002 做一次 B 类定向阅读，而不是默认整篇精读。**

从已经完成的文献身份、开场问题与五类管理者工作继续，不重复开篇。

本轮只回答：

1. 作者怎样划分管理者工作？
2. “technical performance” 与 “normative appropriateness” 是否改变我们对 Human / AI 决策权配置的理解？
3. “purpose” 在作者论证里到底是什么，是否真的意味着某类工作必须由人承担？
4. 这些内容对 R-001 是否形成新的 Engineering Hypothesis？

如果答案是“有重大直接增量”，P-002 升级为 A 类并继续完整 Part A–E；如果只是原则性补充，就在获得 Engineering Bridge 后停止。

---

## 9. Resume Here

> 研究方法已从“按论文顺序推进”切换为“问题牵引研究”。
>
> 当前 Active Problem 是 R-001：高价值企业判断任务中 Human / AI 的分工、决策权与反馈怎样设计。
>
> P-001 已完成理论理解；P-002 不再是“必须读完的第二篇”，而是 R-001 的候选证据。先按 B 类定向阅读，只有真正影响设计时才升级 A 类。
>
> 长期终点是 `PRINCIPLES.md`：论文知识 → Engineering Hypothesis → Validation → Principle，而不是论文 → 笔记 → 更多论文。
