#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(path):
    p = ROOT / path
    if not p.exists():
        errors.append(f"missing required file: {path}")
        return ""
    return p.read_text(encoding="utf-8")

state = read("REPOSITORY_STATE.yaml")
now = read("NOW.md")
runner = read("research/RESEARCH_STATE.yaml")
topics = read("topics/README.md")
research_map = read("RESEARCH_MAP.md")
readme = read("README.md")\nreadme_zh = read("README.zh-CN.md")

required_state_tokens = [
    'canonical_state: "REPOSITORY_STATE.yaml"',
    'frontier: "RP-002-01"',
    'problem: "RP-002-02"',
    'active_gap: "GAP-004"',
    'q_map_source: "topics/README.md"',
]
for token in required_state_tokens:
    if token not in state:
        errors.append(f"REPOSITORY_STATE.yaml missing token: {token}")

if "RP-002-01" not in now:
    errors.append("NOW.md does not contain canonical human frontier RP-002-01")
if 'scope: "RP-002-02"' not in runner or 'gap: "GAP-004"' not in runner:
    errors.append("RESEARCH_STATE.yaml does not match canonical automation frontier")
if "Q3｜Human-Agent 的协调机制" not in topics:
    errors.append("topics/README.md no longer preserves Q3 historical identity")
if "Human、Agent、Software、Asset 如何形成稳定协作" not in research_map:
    errors.append("RESEARCH_MAP.md Q3 meaning drifted from canonical Q map")
if "The current Active Problem is R-001" in readme:
    errors.append("README.md still advertises stale R-001 current state")

# Verify active Topic files declared in repository state.
for topic_id in re.findall(r'- "(T-\d{3})"', state):
    matches = list((ROOT / "context" / "topics").glob(f"{topic_id}-*.md"))
    if not matches:
        errors.append(f"missing Topic State file for {topic_id}")

# Lightweight relative Markdown link check.
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        candidate = (md.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not candidate.exists():
            errors.append(f"broken relative link: {md.relative_to(ROOT)} -> {target}")

if errors:
    print("Repository integrity check FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Repository integrity check passed.")
