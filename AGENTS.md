# AGENTS.md｜Repository Bootstrap

本仓库是一个**问题驱动、假设演进、证据约束**的企业 AI 长期研究系统。

本文件只承担 **Bootstrap / Context Routing / 最小治理规则**。不要把所有专项协议重新堆回本文件。完整 Research Runner 协议已迁移到 `ops/research-runner.md`；其他任务按下述路由渐进加载。

---

## 1. First Read｜默认启动顺序

任何新的 AI / Agent 进入仓库时，先按顺序读取：

1. `AGENTS.md`
2. `REPOSITORY_STATE.yaml`
3. `context/CURRENT.md`
4. `context/TOPIC_INDEX.md`
5. 根据当前任务只选择最相关的 **1–3 个 Topic State**
6. 只有信息不足时，再继续读取 Problem / Hypothesis / Checkpoint / Research / Evidence / Source

核心原则：

> **Progressive Context Loading：先加载最小足够上下文，不默认扫描整个仓库。**

---

## 2. Canonical State｜状态权威

`REPOSITORY_STATE.yaml` 是仓库运行状态的机器可读注册表，用于回答：

- 当前人工研究前沿是什么；
- Research Runner 当前试运行什么；
- 当前有哪些长期 Topic；
- 各专项协议版本是什么。

它不替代正文：

- `NOW.md`：人工研究驾驶舱；
- `research/RESEARCH_STATE.yaml`：Research Runner 机器运行态；
- `context/CURRENT.md`：新会话恢复视图；
- `topics/README.md`：Q1–Q5 长期问题身份；
- `research/problems/*.md`：每个 Problem ID 的唯一 canonical body。

若这些视图看起来不一致，先判断是否属于不同 `research_planes`，不要自行猜测哪个“全局 Active Problem”才是真的。

---

## 3. Problem Identity｜问题身份与演化

Q1–Q5 的当前权威定义以 `topics/README.md` 为准。

研究问题允许随着证据和讨论深入发生演化，包括：

- `refines`
- `splits_into`
- `derived_from`
- `reframes`
- `merges`
- `related_to`
- `supersedes`

规则不是冻结问题，而是：

> **问题可以演化，但 ID 不应偷偷换意思。**

如果新研究对象已超出原问题含义，优先创建 RP / 子问题并建立演化关系。若原问题本身需要实质重构，应在 `EVOLUTION.md` 显式记录，而不是静默覆盖历史身份。

### Historical Context｜历史状态不追写

Paper Card、Evidence Card、Checkpoint、Git History 可以保留**当时**的 Active Problem / Hypothesis / Research Context，不要求追随当前 Frontier 重写。

若历史文件中的“current / 当前”可能被误解，应补充 Historical Context / Current Pointer，而不是把过去的 R-001、H1 等直接改成今天的 RP / Hypothesis。

当前运行状态只由 `REPOSITORY_STATE.yaml` 及其声明的当前视图负责。

---

## 4. Task Routing｜按任务读取专项协议

### 4.1 Research Heartbeat / Weekly Synthesis / Research Runner

必须继续读取：

1. `ops/research-runner.md`
2. `research/RESEARCH_STATE.yaml`
3. 当前 Runner problem
4. 对应 Evidence Ledger
5. 必要时 `research/RESEARCH_LOOP.md`

Research Runner 的 allow-list、deny-list、Evidence、Finding、Strategic Thesis、语言、验收等详细规则以 `ops/research-runner.md` 为准。

### 4.2 跨会话恢复 / Checkpoint / Topic State

读取：

- `context/README.md`
- `context/CURRENT.md`
- `context/TOPIC_INDEX.md`
- 相关 Topic

遵守：

`Conversation → Checkpoint → Topic State → Context Routing → New Task`

Checkpoint 只记录 Delta；Topic 保存当前有效状态；没有长期状态变化就不创建 Checkpoint。

### 4.3 论文研究

按需读取：

- `research/paper-review-plan.md`
- `ai-context/PAPER_READING_MODE.md`
- `research/reading-list.md`

论文是 Evidence Provider，不是研究主线本身。

### 4.4 产业 / 产品 / 案例研究

先定位对应 RP / Q / E-G Track，再研究对象。不得因为出现新产品或新术语就自动创造顶层框架。

---

## 5. Core Research Discipline｜最小研究纪律

无论使用哪个专项协议，都必须遵守：

- 先问题，后材料；
- 先机制，后工程；
- 先假设，后原则；
- 主动寻找 Counter Evidence / Alternative Hypothesis / Boundary Condition；
- Product Claim ≠ Product Fact；
- Synthetic Validation ≠ Enterprise Outcome；
- AI Proposal 不自动升级为 Judgment / Stable Principle；
- 私人经验可以启发问题，但公开仓的公开结论必须由公开证据独立支撑；
- 不因新名词直接创造 Layer / Plane / Platform / Runtime。

---

## 6. Public Repository Boundary｜公开仓边界

本仓库是公开研究作品，不保存：

- 客户名称与身份；
- 公司内部或非公开项目资料；
- 非公开数据、截图、投标材料、架构；
- 可反向识别的私人项目证据链。

私人 / 项目经验若触发研究，只保留抽象后的问题，再使用公开 Theory / Product / Case / Standard / Open-source / Counter Evidence 独立验证。

---

## 7. Git Delivery｜所有写入任务的最低规则

GitHub `main` 是唯一正式版本。

产生有效修改时统一使用：

`origin/main → isolated branch → modify → self-check → commit/push → Pull Request → Human Review → Merge`

必须：

- 从最新 `main` 开始；
- 一个任务一个独立 branch；
- PR base 为 `main`；
- 不直接 push `main`；
- 不自动 merge；
- 不绕过 branch protection；
- 最终报告列出 Changed Files、branch、PR 与检查结果。

无有效修改时，不制造空 PR。

Research Runner 的更细 Git / Acceptance 规则见 `ops/research-runner.md`。

---

## 8. Write-back｜何时更新哪些状态

任务结束前判断是否产生长期状态变化：

### 没有长期变化

只更新任务本身需要的文件，不创建无意义 Checkpoint，不机械更新所有入口。

### 有长期变化

按需更新：

1. Problem / Hypothesis / Evidence 等任务正文；
2. 相关 Topic 当前状态；
3. 必要时创建 Checkpoint；
4. 若人工研究前沿变化，更新 `NOW.md` 与 `REPOSITORY_STATE.yaml`；
5. 若 Runner 状态变化，更新 `research/RESEARCH_STATE.yaml` 与 `REPOSITORY_STATE.yaml` 对应 automation plane；
6. 只有重大认知转折才更新 `EVOLUTION.md`。

不要让 README、NOW、CURRENT、Topic、State 各自维护一份独立“当前现实”。

---

## 9. Repository Integrity｜最低自检

仓库提供：

`python3 scripts/check_repository_state.py`

用于检查：

- Canonical State 与 human / automation plane 的基本一致性；
- Q3 等长期问题身份没有被静默改写；
- README 不再指向已过时的 Active Problem；
- Active Topic 文件存在；
- Markdown 相对链接没有明显断裂。

CI 会在 PR 和 main push 时执行该检查。

---

## 10. Rule of Thumb

遇到不确定时，优先问：

> **这是研究内容本身，还是仓库运行状态？它的唯一正文 / 唯一状态来源在哪里？**

目标不是让所有文件内容一致，而是：

> **Single Research State + Multiple Views + Progressive Context Loading。**
