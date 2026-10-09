# Human-confirmed Knowledge Notes

本目录只存放研究者确认已经理解、且值得长期复用的官方工程知识卡。自动发现任务不得批量创建或把条目标为 `HUMAN_UNDERSTOOD`。

## Card template

复制以下模板，使用稳定的 `OE-<ID>-<slug>.md` 文件名。没有复用价值时，留在 source queue，不建卡。

```markdown
# OE-<ID>｜<short title>

Source: <official URL>
Publisher: <OpenAI / Anthropic>
Published / version: <date or version>
Queue status: HUMAN_UNDERSTOOD
Human confirmation date: YYYY-MM-DD

## Source Understanding

### SOURCE_CLAIM
-

### SOURCE_MECHANISM
-

## Mechanism Reconstruction

### AI_EXPLANATION
- Why needed:
- How it works:
- Problem addressed:
- Adjacent mechanism:
- Failure / boundary:

## Architecture Variables

- Effective when:
- Fails or weakens when:
- Alternatives:
- Stage-dependent assumptions:

## Enterprise Translation

### RESEARCH_INFERENCE

Only map the relevant items among Business Application / Workflow / Agent / Context / Harness / Runtime / Action / Governance.

## Human Takeaways

### HUMAN_TAKEAWAY
- I can explain:
- I can distinguish:
- My prior view changed because:
- I still do not know:

## Optional Research Bridge

- Existing Problem / Topic:
- Supports / Challenges / Narrows / Revises / Opens Alternative:
- Candidate validation:
- Why this should remain outside Evidence for now:

## Confirmation

Researcher explicitly confirms: `I understand the mechanism and its boundary well enough to reuse it.`
```

`SOURCE_CLAIM` / `SOURCE_MECHANISM` 必须忠实于原文；`AI_EXPLANATION` 是辅助理解；`RESEARCH_INFERENCE` 是我们的推论；`HUMAN_TAKEAWAY` 只有研究者确认后才能填写为最终理解。厂商主张、合成验证和企业结果必须分别标注。
