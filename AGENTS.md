# AGENTS.md｜Enterprise AI Research Runner v0.2.1

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
→ Proposed Hypothesis Change
→ Synthesis
→ Next Evidence Gap
```

v0.2 将“找证据”和“改正式认知”拆成两个节奏：

- **Research Heartbeat**：搜证据、评估证据、更新研究状态；
- **Weekly Synthesis**：综合多轮证据后，才更新 Problem / NOW 中的正式认知。

---

## 2. 两类自动任务及写权限

### 2.1 Research Heartbeat

职责：

- 读取当前研究状态；
- 只推进一个 Evidence Gap；
- 搜索 3–5 条 Material Evidence；
- 判断 Evidence 对 Hypothesis 的作用；
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

## 6. 每条 Evidence 必须回答

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

每轮最多保留 3–5 条**真正改变判断**的高价值证据。

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
2. `research/RESEARCH_STATE.yaml`；
3. 明确 `next_action`。

如果证据暗示 Hypothesis 应改变：

- 写入 `proposed_revision`；
- 不直接改 Problem 主文件。

---

## 13. 当前试运行范围

Research Runner v0.2 只围绕：

`RP-002-02｜Business Action Layer`

运行。

在 v0.2 验证完成前，不自动切换到其他正式问题。

成功标准：

> 在用户不持续贡献新观点的情况下，AI 能基于外部证据持续推进 Evidence Gap，提出可审计的 Hypothesis 修正，并通过 Weekly Synthesis 将成熟变化写回正式 Problem。


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
