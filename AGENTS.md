# AGENTS.md｜Enterprise AI Research Runner v0.4

本仓库不是资料收藏库，而是一个**问题驱动、假设演进、证据约束**的企业 AI 研究系统。

Codex / 自动化任务在本仓库执行研究时，必须遵循以下规则。

---

## 1. 研究目标

自动研究的目标不是“搜更多资料”，而是：

> **推进当前 Active Problem 的一个最高优先级 Evidence Gap，并让证据持续改变或约束 Hypothesis。**

主闭环：

```text
Active Problem
→ Current Hypothesis
→ Evidence Gap
→ Targeted Research
→ Evidence Evaluation
→ Cross-source Synthesis
→ Research Finding
→ Proposed Hypothesis Change
→ Synthesis
→ Next Evidence Gap
```

v0.3 在“找证据”和“改正式认知”的两种节奏之间，新增 **Research Finding｜研究发现** 这一人类可读层：

- **Research Heartbeat**：围绕一个 Gap 研究多个来源，先形成跨来源判断，再用 Material Evidence 支撑该判断；
- **Research Finding**：回答“所以呢？这对原问题和原假设意味着什么？”；
- **Weekly Synthesis**：综合多轮 Finding 与 Evidence 后，才更新 Problem / NOW 中的正式认知。

默认原则：

> **结论先行、证据后置；先回答问题，再记录证据。**

---

## 2. 两类自动任务及写权限

### 2.1 Research Heartbeat

职责：

- 读取当前研究状态；
- 只推进一个 Evidence Gap；
- 先回答当前 Gap，再决定哪些证据值得保留；
- 从多个来源中识别重复模式、差异、反例和边界；
- 形成一条人类可读的 Research Finding；
- 普通 Heartbeat 通常保留 3–5 条真正支撑该 Finding 的 Material Evidence；战略级 Gap 为覆盖多证据域可保留 4–6 条，但都必须真正影响判断；
- 判断 Finding / Evidence 对 Hypothesis 的作用；
- 更新 Evidence Ledger；
- 更新 RESEARCH_STATE；
- 提出 proposed_revision；
- 留下 next_action。

**Heartbeat 允许写：**

- `research/evidence/*.md`
- `research/RESEARCH_STATE.yaml`

**Heartbeat 禁止写：**

- `research/problems/*.md`
- `NOW.md`
- `JUDGMENTS.md`
- `PRINCIPLES.md`

Heartbeat 即使发现 H0/H1 需要变化，也只能把变化写入：

`active_hypothesis.proposed_revision`

不得直接把 Problem 主文件改成新的正式版本。

### 2.2 Weekly Synthesis

职责：

- 读取一周内新增 Evidence；
- 判断 Hypothesis 是否应保持、修正、拆分或否定；
- 消除 Problem、State、Evidence 之间的冲突；
- 确定下一 Evidence Gap。

**Weekly Synthesis 允许写：**

- `research/RESEARCH_STATE.yaml`
- 当前 `research/problems/*.md`
- `NOW.md`
- 必要时整理 Evidence Ledger 的 Current Judgment

**Weekly Synthesis 禁止写：**

- `PRINCIPLES.md`

Principle 只能由人工审核后升级。

---

## 3. 每轮开始前必须读取

按顺序读取：

1. `NOW.md`
2. `research/RESEARCH_STATE.yaml`
3. 当前 active problem 文件
4. 对应 evidence ledger
5. 必要时读取 `research/RESEARCH_LOOP.md`

如果文件之间存在冲突：

- Heartbeat 以 `RESEARCH_STATE.yaml` 的运行状态为准，并记录冲突；
- Weekly Synthesis 负责决定是否消除冲突并更新正式 Problem / NOW。

---

## 4. 每次 Heartbeat 只推进一个 Evidence Gap

只研究：

- 由 `next_action` 指向；
- 且 `status: active` 的 Evidence Gap。

若 next_action 指向 `queued` Gap，Heartbeat 可在本轮开始时将其切换为 `active`。

禁止为了“完整”同时扩展多个主题。

如果当前 Gap 太大，允许拆成更小的 research task，但不得直接创建新的正式 Research Problem。

---

## 5. 证据搜索优先级

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

## 6. Evidence 是支撑材料，不是前台结论

Evidence 的职责是提供可追溯、可审计的依据，不承担“替人解释研究结果”的职责。

每轮首先要形成 Research Finding；Evidence Card 放在后面支撑 Finding。

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

## 7. 研究纪律

普通研究轮次通常保留 3–5 条**真正改变判断**的高价值证据；战略级 Gap 为满足多证据域覆盖可保留 4–6 条。数量不是 KPI：若更少的高质量证据已足够形成稳定 Finding，可以更少；若没有高价值增量，应明确记录 `NO_MATERIAL_UPDATE`。

禁止：

- 批量堆论文；
- 批量堆产品链接；
- 为支持既有观点而选择性找材料；
- 把 Product Claim 写成 Architecture Fact；
- 因为发现一组需求就立即创造新的“Layer / Plane / Platform”并把它当成既定架构；
- 自动修改 `PRINCIPLES.md`；
- 自动创建新的正式 Research Problem；
- 因出现新名词就扩展研究范围。

必须主动寻找：

- Counter Evidence
- Alternative Hypothesis
- Boundary Condition
- Existing Architecture Pattern

### 新概念命名纪律

如果证据只证明“一组需求或控制机制存在”，只能写成：

- candidate mechanism
- governance requirement
- control requirement
- possible boundary

除非有多源产品 / 工程实现证据证明其稳定独立存在，否则不得直接升级成：

- 独立 Layer
- Control Plane
- Platform
- Runtime

---

## 8. Hypothesis 更新规则

Hypothesis 必须保留版本演进：

```text
H0 → H1 → H2
```

Heartbeat 可以提出：

`proposed_revision`

但正式的 H0 → H1 / H1 → H2 版本变化，由 Weekly Synthesis 或人工审核完成。

每次正式变化必须写清：

- 旧假设
- 触发变化的 Evidence
- 变化原因
- 新假设
- 新增边界条件
- 尚未解决的 Gap

如果证据不足，保持原状态。

---

## 9. Evidence Gap 状态

使用以下状态：

- `queued`：待研究；
- `active`：当前正在研究；
- `provisionally_saturated`：概念层证据已足够，暂时停止继续搜，但仍可能被后续工程证据重新打开；
- `saturated`：多源理论 / 产品 / 工程证据已较充分；
- `closed`：问题已被验证、否定或转入 Engineering Validation。

对只有理论、标准、产品文档支撑、但尚缺工程验证的 Gap，优先使用：

`provisionally_saturated`

---

## 10. 新问题处理

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

## 11. 停止条件

某个 Evidence Gap 可设为 `provisionally_saturated`：

1. 已有 2–3 个独立来源，且至少 1 个 Primary / Implementation 级证据；
2. 已同时获得支持证据、限制条件和至少一种反例 / 替代解释；
3. 已能解释主要概念边界，但工程阈值仍未知。

可进一步设为 `saturated` / `closed`：

- 已有真实工程 / 产品实现对照；
- 或已经形成可验证 Engineering Hypothesis；
- 或连续两轮 `NO_MATERIAL_UPDATE` 且无关键未知量。

没有高价值增量时明确记录：

`NO_MATERIAL_UPDATE`

不要制造伪进展。

---

## 12. 每轮 Heartbeat 结束必须更新

至少更新：

1. 当前 evidence ledger；
2. 在 ledger 前部写入或更新本轮 Research Finding；
3. `research/RESEARCH_STATE.yaml`；
4. 明确 `next_action`。

如果证据暗示 Hypothesis 应改变：

- 写入 `proposed_revision`；
- 不直接改 Problem 主文件。

---

## 13. 当前试运行范围

Research Runner v0.4 试运行仍只围绕：

`RP-002-02｜Business Action Layer`

运行。

在 v0.4 验证完成前，不自动切换到其他正式问题。

成功标准：

> 在用户不持续贡献新观点的情况下，AI 能基于外部证据持续推进 Evidence Gap，把多来源证据加工成用户能直接理解的 Research Finding，再提出可审计的 Hypothesis 修正，并通过 Weekly Synthesis 将成熟变化写回正式 Problem。


---

## 14. Language Policy｜语言规则

本仓库面向中文研究与长期认知沉淀。

除非任务明确要求其他语言，否则所有 Research Heartbeat、Weekly Synthesis、Evidence Ledger 和正式研究认知输出，默认使用中文完成。

### 14.1 必须使用中文的内容

以下内容默认使用中文：

- Research Heartbeat Report；
- Evidence Ledger 中的研究分析；
- Observed Fact；
- Mechanism；
- Why it matters；
- Boundary / Limitation；
- Research implication；
- Hypothesis 影响判断；
- proposed_revision；
- candidate_questions；
- next_action；
- research_history 中的自然语言说明；
- Weekly Synthesis；
- Problem 文件中的正式认知更新；
- PR 摘要中的研究结论与认知变化说明。

### 14.2 保留原文的内容

以下内容保留原文，不强制翻译：

- 产品名、框架名、协议名、标准名；
- 官方技术术语，例如 Application Service、Command、Ontology Action、Submission Criteria；
- 论文标题、官方文档标题；
- URL；
- YAML key；
- Evidence ID、Gap ID、Hypothesis ID；
- branch、commit、PR title 中的技术标识；
- 必须精确引用的字段名、接口名、API 名称。

### 14.3 英文来源处理规则

对于英文来源：

1. 不生成完整英文研究稿后再翻译；
2. 直接以中文完成研究分析和仓库沉淀；
3. 证据事实必须以中文准确转述；
4. 必要的英文术语首次出现时可使用：
   `中文解释（Original Term）`；
5. 不为了中文化而改变官方概念含义；
6. 不大段翻译原文，只保留必要的原始术语和引用信息。

默认原则：

> **Source 保持原貌，Research Thinking 与 Knowledge Asset 使用中文。**

### 14.4 自动化任务语言验收

每次 Research Heartbeat / Weekly Synthesis 结束前必须检查：

- 新增研究正文是否以中文为主；
- proposed_revision 是否为中文；
- next_action 是否为中文；
- candidate_questions 是否为中文；
- 最终报告是否为中文；
- 是否避免先写完整英文版本再二次翻译。

若语言规则未满足，任务不得标记为完整通过，应标记：

`RUN_STATUS: NEEDS_REVIEW`


---

## 15. Git Delivery Policy｜Git 交付规则

GitHub 的 `main` 是本仓库唯一正式状态（Single Source of Truth）。

本地仓库、Codex Worktree、ChatGPT 云端修改、未来其他 AI 工具都只是工作环境，不得被视为正式版本。

统一交付链路：

```text
origin/main
→ isolated branch / worktree
→ modify
→ self-check
→ commit
→ push
→ Pull Request
→ Human Review
→ Merge to main
```

### 15.1 开始任务前

每次需要修改仓库的 AI 任务开始前必须：

1. 执行或等价完成：
   `git fetch origin`
2. 确认本轮工作基线来自最新 `origin/main`；
3. 如果当前 Worktree / branch 明显落后于 `origin/main`，必须先同步或基于最新 `origin/main` 新建工作分支；
4. 如果无法安全同步：
   - 停止写入；
   - 不继续研究修改；
   - 标记 `RUN_STATUS: NEEDS_REVIEW`；
   - 说明同步失败原因。

用户不需要为了定时任务手工维护本地 `main` 最新状态；自动任务应自行检查远程基线。

### 15.2 分支与 Worktree

所有 AI 写入任务必须使用独立 branch 或 Git Worktree。

规则：

- 一个任务使用一个独立工作分支；
- 不同自动任务不得共享同一工作分支；
- 分支名称应能体现任务类型和 Gap / Topic；
- 推荐格式：
  - `codex/research-heartbeat-<GAP-ID>-<YYYYMMDD>`
  - `codex/weekly-synthesis-<YYYYMMDD>`
  - `chore/<short-change>`

禁止：

- 直接在 `main` 上修改后 push；
- 多个 AI 同时复用同一 branch；
- 在未知基线状态下继续写入。

### 15.3 自动提交与 Push

如果任务没有产生有效修改：

- 不创建 branch；
- 不 commit；
- 不 push；
- 不创建 PR；
- 明确报告 `NO_MATERIAL_UPDATE`。

如果产生有效修改：

1. 只提交本任务允许修改的文件；
2. 运行 `git diff --check` 或等价检查；
3. commit message 应简洁说明任务，例如：
   - `research: complete GAP-003 heartbeat`
   - `research: weekly synthesis RP-002-02`
4. push 到远程独立分支。

### 15.4 Pull Request 是唯一交付接口

所有 AI 修改必须通过 Pull Request 进入 `main`。

PR 必须：

- `base: main`
- `head: 当前任务分支`
- 清楚说明本轮做了什么；
- 列出 Changed Files；
- 对研究任务说明 Evidence / Hypothesis / next_action 的变化；
- 对方法或治理规则修改说明影响范围。

PR 是用户的主要审核界面。

用户不应被要求日常执行：

- `git add`
- `git commit`
- `git push`
- 手工创建 branch
- 手工同步 Worktree

除非自动交付失败且需要人工恢复。

### 15.5 禁止自动 Merge

AI 可以：

- 创建 branch；
- commit；
- push；
- 创建 Pull Request。

AI 不得：

- 直接 push `main`；
- 自动 Merge PR；
- 绕过 branch protection；
- 自动关闭人工审核门。

最终进入 `main` 必须经过 Human Review。

### 15.6 多执行者协作规则

本仓库可能同时由 Codex、ChatGPT 或其他 AI 工具维护。

统一规则：

- GitHub `main` 是唯一正式状态；
- 所有执行者都从最新 `origin/main` 开始；
- 所有执行者都通过独立 branch / PR 交付；
- 同一个 Active Problem 同一时间尽量只有一个主要写入者；
- 其他执行者若修改同一问题，应优先等待当前 PR 合并，或基于最新 `origin/main` 新建后续 PR；
- 不通过复制本地文件、手工覆盖或私有中间版本解决冲突。

发生冲突时：

> 以 GitHub `main` + 已存在的开放 PR 为事实来源，不猜测哪个本地副本“更新”。

---

## 16. Automation Acceptance Check｜自动任务验收规则

每次 Research Heartbeat / Weekly Synthesis / 自动仓库修改任务结束前，必须执行自检。

### 16.1 Research Contract Check

检查：

1. 是否读取了最新 `AGENTS.md`；
2. 是否读取了最新 `RESEARCH_STATE.yaml`；
3. 是否只执行了 `next_action` 指向的一个当前任务；
4. 是否遵守当前任务的 allow-list / deny-list；
5. 是否先形成了人类可读的 Research Finding，而不是只堆 Evidence Card；
6. Research Finding 是否明确回答“发现了什么、改变了什么、有什么用、还缺什么”；
7. 是否只保留高价值 Evidence，或明确记录 `NO_MATERIAL_UPDATE`；
8. 是否包含 Counter Evidence / Boundary Condition / Alternative Hypothesis（适用时）；
9. 是否明确留下 `next_action`；
10. 是否遵守 Language Policy。

### 16.2 File Scope Check

最终报告必须列出：

- 实际修改文件；
- 是否修改任何 forbidden 文件。

如果修改了 forbidden 文件：

`RUN_STATUS: NEEDS_REVIEW`

并不得声称任务完整成功。

### 16.3 Git Delivery Check

如果本轮存在有效修改，必须检查：

- branch 是否创建；
- commit 是否成功；
- push 是否成功；
- PR 是否创建；
- PR base 是否为 `main`；
- 是否没有自动 Merge。

如果环境无法创建 PR：

- 至少完成 branch + commit + push；
- 明确报告失败环节和远程分支名；
- 标记 `RUN_STATUS: NEEDS_REVIEW`。

### 16.4 最终状态

只有以下条件全部满足，才能标记：

`RUN_STATUS: PASS`

- 研究协议通过；
- 文件范围通过；
- 语言规则通过；
- Git Delivery 通过；
- 没有自动 Merge；
- 没有未说明的错误。

否则：

`RUN_STATUS: NEEDS_REVIEW`

### 16.5 最终报告固定格式

自动任务最终报告必须**先给用户可读结论，再给运行与 Git 信息**：

```text
Research Finding
- 本轮问题
- 一句话结论
- 跨来源关键发现
- 对原 Hypothesis 的影响
- 对架构 / 工程的意义
- 当前最大未知量
- next_action
- Supporting Evidence IDs

Run Contract
- AGENTS version
- Active Problem
- Executed Gap / Task
- Evidence Count
- proposed_revision

File Scope
- Changed Files
- Forbidden Files Changed

Git Delivery
- branch
- commit
- push status
- PR URL
- merge status

Acceptance
- RUN_STATUS: PASS / NEEDS_REVIEW
- Notes
```

Research Heartbeat 不再以“Material Evidence 摘要”作为第一输出；Evidence 只作为 Finding 的依据与附录。

默认目标：

> 用户只需要审核 Pull Request，而不是维护 Git 操作流程。


---

## 17. Research Finding Policy｜研究发现规则

Research Runner v0.3 引入三层研究产物，解决“证据很多，但人看不懂它们对问题有什么帮助”的问题。

### 17.1 三层结构

每轮 Heartbeat 的产物按以下顺序组织：

```text
Level 1｜Research Finding
给人读：这轮研究到底发现了什么？

Level 2｜Cross-source Synthesis
给人和 AI 都能读：不同论文 / 产品 / 案例之间的共同模式、差异和反例是什么？

Level 3｜Evidence Ledger
给 AI 审计和追溯：每条结论由哪些来源、事实和机制支撑？
```

用户默认只需要阅读 Level 1；需要比较时看 Level 2；只有需要追溯来源时才进入 Level 3。

### 17.2 Research Finding 必须回答七个问题

每个完成的 Gap，都必须在 Evidence Ledger 前部形成一个 Research Finding，建议控制在约 300–800 个中文字符，回答：

1. **本轮问题是什么？**
2. **一句话结论是什么？**
3. **多个来源共同说明了什么？**
4. **有没有关键差异、反例或边界？**
5. **它改变了原来的哪个 Hypothesis / 判断？**
6. **对企业 AI 架构、产品或工程意味着什么？**
7. **还有什么没有搞清楚，为什么下一步值得继续？**

Finding 必须引用支撑它的 Evidence ID，但不得把 Evidence Card 原样搬到前台。

### 17.3 Cross-source Synthesis 优先于单条卡片

当研究对象包含多个论文、产品、开源项目或案例时，优先形成比较关系，例如：

| 对象 | 它提供了什么 | 真正由谁执行 | 治理 / 权限在哪里 | 对当前 Hypothesis 的意义 |
|---|---|---|---|---|

目标不是“分别总结 A、B、C”，而是回答：

> **A、B、C 放在一起后，出现了什么稳定模式、关键差异和反例？**

### 17.4 Heartbeat 的研究顺序

禁止默认采用：

```text
搜索 → 找 3–5 条资料 → 填证据卡 → 总结
```

默认采用：

```text
当前 Gap
→ 研究多个来源
→ 找重复模式 / 差异 / 反例
→ 形成 Research Finding
→ 选择最能支撑该 Finding 的 Material Evidence
→ 判断对 Hypothesis 的影响
→ 留下 next_action
```

### 17.5 Finding 与 Evidence 的关系

- Finding 可以被后续研究修正或推翻；
- Evidence 必须保留可追溯来源；
- Finding 不得超出 Evidence 能支持的范围；
- Evidence 之间冲突时，Finding 必须明确写出冲突，而不是强行统一；
- 单一厂商的产品设计不得直接上升为行业稳定规律；
- Finding 是“当前最好的解释”，不是 Principle。

### 17.6 Weekly Synthesis 的阅读顺序

Weekly Synthesis 默认先读取：

1. 本周新增 Research Findings；
2. 对应的 Cross-source Synthesis；
3. 只有需要核验时再深入 Evidence Detail。

Weekly Synthesis 的目标不是重新读一遍所有证据卡，而是判断：

> 多轮 Finding 合在一起后，Hypothesis 是否应该正式变化？

### 17.7 可读性验收

Research Finding 必须满足：

> 用户即使不展开 Evidence Detail，也能理解“研究了什么、发现了什么、为什么重要、下一步是什么”。

如果做不到，即使 Evidence 数量和格式都完整，也必须标记：

`RUN_STATUS: NEEDS_REVIEW`


---

## 18. Mechanism & Strategic Thesis Policy｜机制与战略洞察规则

Research Runner v0.4 的目标不再只是识别“当前产品怎么做”，而是回答：

> **为什么会形成这种模式？哪些是结构性约束，哪些只是当前 AI 能力不足造成的过渡形态？如果模型能力继续提升，什么仍会留下？**

### 18.1 结论成熟度分级

所有研究结论必须标记成熟度：

- `Observation`：单个可靠来源支持的事实；
- `Pattern`：多个独立来源重复出现的模式；
- `Mechanism`：有理论 / 工程证据解释“为什么”；
- `Strategic Thesis`：能区分结构性与过渡性，并对未来演化提出可证伪判断；
- `Architecture Principle`：经过跨问题 / 工程验证与人工审核后的稳定原则。

禁止从 Product Pattern 直接跳到 Strategic Thesis 或 Architecture Principle。

### 18.2 Strategic Thesis 的证据门槛

若要提出 `Strategic Thesis`，不得只依赖厂商产品文档。

至少覆盖以下 4 个证据域中的 3 个：

1. **Theory / Paper**：解释机制、授权、安全、组织或软件工程约束；
2. **Product / Implementation**：真实产品、协议、开源实现；
3. **Case / Engineering**：真实客户案例、公开工程实践、运行数据或失败经验；
4. **Counter Evidence / Alternative**：能够支持另一种解释或未来路径的证据。

证据域是覆盖要求，不是凑数量 KPI。弱证据不得为了满足数量被保留。

### 18.3 每个战略级 Gap 必须回答 WHAT / WHY / STRUCTURAL / FUTURE

#### WHAT｜发生了什么？

- 当前论文、产品、案例、开源实现分别显示什么？
- 哪些只是厂商口径，哪些是工程事实？

#### WHY｜为什么？

- 哪些底层机制能解释这个 Pattern？
- 是模型能力、软件架构、分布式系统、安全授权、组织责任还是法规约束导致？

#### STRUCTURAL vs TRANSITIONAL vs EMERGING

必须明确分三类：

- **Structural**：即使模型能力提高 10 倍仍大概率存在的约束；
- **Transitional**：主要由当前模型能力、工程成熟度或工具限制导致，未来可能被吸收；
- **Emerging**：AI 成为行动主体后真正新增或显著强化的机制。

#### FUTURE / SO WHAT

至少推演一个“模型能力显著增强”的情景：

> 如果 3–5 年后模型的推理、工具调用和长程执行能力明显增强，当前结论还成立吗？

最终说明这对企业 AI 的战略架构、产品路线或建设顺序意味着什么。

### 18.4 必须提出 Alternative Hypothesis

每个 Strategic Thesis 至少保留一个有竞争力的替代解释。

例如：

> 当前看到 Action Contract，不一定说明它是长期独立资产；也可能未来由 Policy Engine + API Schema + 更强模型直接承担。

不能只寻找支持当前观点的证据。

### 18.5 必须提出 Falsifiable Prediction｜可证伪预测

Strategic Thesis 至少提出 2 条可被未来事实推翻或强化的预测。

预测应包含：

- 如果 Thesis 成立，未来产品 / 工程应该出现什么；
- 如果 Alternative 成立，应该出现什么；
- 哪些观察结果会迫使我们修正判断。

禁止使用“未来 AI 会更智能”这类无法检验的表述。

### 18.6 当前产品现状不等于战略终局

自动研究不得把：

> “当前三家厂商都这样做”

直接写成：

> “未来企业 AI 必须这样做”。

必须检查：

- 是否只是历史包袱；
- 是否是当前模型不可靠造成的临时补丁；
- 是否由企业治理 / 权限 / 责任 / 事务等结构性问题决定；
- 是否存在模型能力提升后更简单的替代路线。

### 18.7 Case Evidence 纪律

客户案例必须区分：

- `Independent Case`
- `Vendor-published Case`
- `Demo / Claim`

厂商发布的客户故事不能自动当作独立验证；必须标记来源偏差与可验证范围。

### 18.8 Strategic Finding 固定输出

对于战略级 Gap，Research Finding 额外必须包含：

```text
Maturity Level
- Observation / Pattern / Mechanism / Strategic Thesis

WHAT
- 当前事实与跨来源模式

WHY
- 底层机制

STRUCTURAL
- 模型更强后仍存在的约束

TRANSITIONAL
- 可能被更强模型 / 更好工具吸收的部分

EMERGING
- Agent 时代新增或显著强化的机制

Alternative Hypothesis
- 最强替代解释

Falsifiable Predictions
- P1
- P2

Strategic Implication
- 对企业 AI 架构 / 产品 / 建设顺序意味着什么
```

若只完成 WHAT，没有可靠 WHY 与结构性分析，最高只能标记为 `Pattern`。
