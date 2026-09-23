#!/usr/bin/env python3
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []


def read(path):
    p = ROOT / path
    if not p.exists():
        errors.append(f"missing required file: {path}")
        return ""
    return p.read_text(encoding="utf-8")


def load_yaml(path):
    text = read(path)
    if not text:
        return {}
    try:
        data = yaml.safe_load(text)
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML: {path}: {exc}")
        return {}


def parse_front_matter(path):
    text = read(path)
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"missing YAML front matter: {path}")
        return {}
    try:
        data = yaml.safe_load(match.group(1))
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError as exc:
        errors.append(f"invalid front matter YAML: {path}: {exc}")
        return {}


def normalize_version(value):
    if value is None:
        return ""
    return str(value).strip().lstrip("vV")


def extract_markdown_version(text):
    match = re.search(r"Version:\s*\*\*v?([0-9.]+)\*\*", text)
    return match.group(1) if match else ""


def extract_runner_version(text):
    match = re.search(r"Research Runner v([0-9.]+)", text)
    return match.group(1) if match else ""


def active_topics_from_index(text):
    active = set()
    for line in text.splitlines():
        if not line.startswith("| **T-"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 8:
            continue
        topic_id = parts[0].replace("*", "").replace(chr(96), "")
        status = parts[6].lower()
        if status == "active":
            active.add(topic_id)
    return active


def extract_q3_title_from_topics(text):
    match = re.search(r"^##\s+Q3｜(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_q3_title_from_now(text):
    match = re.search(r"^\*\*Q3｜(.+?)\*\*\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


state = load_yaml("REPOSITORY_STATE.yaml")
runner = load_yaml("research/RESEARCH_STATE.yaml")
now_meta = parse_front_matter("NOW.md")

now_text = read("NOW.md")
topic_index_text = read("context/TOPIC_INDEX.md")
topics_text = read("topics/README.md")
research_loop_text = read("research/RESEARCH_LOOP.md")
runner_protocol_text = read("ops/research-runner.md")
context_protocol_text = read("context/README.md")
method_changelog_text = read("research/METHOD_CHANGELOG.md")
paper_mode_text = read("ai-context/PAPER_READING_MODE.md")
reading_list_text = read("research/reading-list.md")
p001_text = read("research/paper-reviews/P001_puranam_2021_hacd.md")

authority = state.get("authority", {})
for key, declared in authority.items():
    if not isinstance(declared, str):
        errors.append(f"authority.{key} must be a path string")
        continue
    target = ROOT / declared.rstrip("/")
    if not target.exists():
        errors.append(f"authority.{key} points to missing path: {declared}")

planes = state.get("research_planes", {})
for plane_name, plane in planes.items():
    if not isinstance(plane, dict):
        errors.append(f"research_planes.{plane_name} must be a mapping")
        continue
    source = plane.get("source")
    if source and not (ROOT / source).exists():
        errors.append(f"research plane {plane_name} source missing: {source}")

human = planes.get("human_frontier", {})
if now_meta.get("problem_family") != human.get("problem_family"):
    errors.append(
        "human problem_family mismatch: "
        f"REPOSITORY_STATE={human.get('problem_family')} NOW={now_meta.get('problem_family')}"
    )
if now_meta.get("frontier") != human.get("frontier"):
    errors.append(
        "human frontier mismatch: "
        f"REPOSITORY_STATE={human.get('frontier')} NOW={now_meta.get('frontier')}"
    )

automation = planes.get("automation_frontier", {})
runner_problem = (runner.get("active_problem") or {}).get("id")
runner_gap = (runner.get("next_action") or {}).get("gap")
if runner_problem != automation.get("problem"):
    errors.append(
        "automation problem mismatch: "
        f"REPOSITORY_STATE={automation.get('problem')} RESEARCH_STATE={runner_problem}"
    )
if runner_gap != automation.get("active_gap"):
    errors.append(
        "automation gap mismatch: "
        f"REPOSITORY_STATE={automation.get('active_gap')} RESEARCH_STATE={runner_gap}"
    )

context_plane = planes.get("context_maintenance", {})
registry_topics = set(context_plane.get("active_topics") or [])
index_topics = active_topics_from_index(topic_index_text)
if registry_topics != index_topics:
    errors.append(
        "active Topic mismatch: "
        f"REPOSITORY_STATE={sorted(registry_topics)} TOPIC_INDEX={sorted(index_topics)}"
    )
for topic_id in registry_topics:
    matches = list((ROOT / "context" / "topics").glob(f"{topic_id}-*.md"))
    if not matches:
        errors.append(f"missing Topic State file for {topic_id}")

canonical_q3 = extract_q3_title_from_topics(topics_text)
now_q3 = extract_q3_title_from_now(now_text)
if not canonical_q3:
    errors.append("cannot extract canonical Q3 title from topics/README.md")
elif now_q3 != canonical_q3:
    errors.append(f"Q3 identity mismatch: topics={canonical_q3!r} NOW={now_q3!r}")

versions = state.get("protocol_versions", {})
method_version = extract_markdown_version(research_loop_text)
runner_version = extract_runner_version(runner_protocol_text)
context_version = extract_markdown_version(context_protocol_text)
state_schema_version = normalize_version(state.get("version"))

expected_method = normalize_version(versions.get("research_method"))
expected_runner = normalize_version(versions.get("runner_protocol"))
expected_context = normalize_version(versions.get("context_continuity_protocol"))
expected_schema = normalize_version(versions.get("repository_state_schema"))

if method_version != expected_method:
    errors.append(f"research method version mismatch: registry={expected_method} RESEARCH_LOOP={method_version}")
if runner_version != expected_runner:
    errors.append(f"runner protocol version mismatch: registry={expected_runner} ops={runner_version}")
if context_version != expected_context:
    errors.append(f"context protocol version mismatch: registry={expected_context} context/README={context_version}")
if state_schema_version != expected_schema:
    errors.append(f"repository state schema mismatch: registry field={expected_schema} file version={state_schema_version}")

current_method_marker = f"| **v{expected_method}**"
if current_method_marker not in method_changelog_text or "**Current / Trial**" not in method_changelog_text:
    errors.append("METHOD_CHANGELOG does not mark the registered research method as Current / Trial")

if "REPOSITORY_STATE.yaml" not in paper_mode_text:
    errors.append("PAPER_READING_MODE does not route through REPOSITORY_STATE.yaml")
if "**当前驱动对象是 R-001" in reading_list_text:
    errors.append("reading-list still presents R-001 as current rather than historical")
if "当前 Active Problem R-001" in p001_text:
    errors.append("P001 card still presents R-001 as current rather than historical")

for path in [
    "AGENTS.md",
    "NOW.md",
    "README.md",
    "README.zh-CN.md",
    "context/CURRENT.md",
    "context/README.md",
]:
    text = read(path)
    if r"\n" in text:
        errors.append(f"literal escaped newline found in state-facing Markdown: {path}")

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
            errors.append(
                f"broken relative link: {md.relative_to(ROOT)} -> {target}"
            )

if errors:
    print("Repository integrity check FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Repository integrity check passed.")
