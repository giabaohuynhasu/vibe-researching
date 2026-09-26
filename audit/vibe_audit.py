"""
vibe_audit.py -- Bridge between Vibe Researching projects and the Third-Order Audit engine.

Integrates the 7-step Vibe Researching protocol with Huynh (2026), "The Third-Order Audit".
Evaluates any Vibe Researching project directory against:
  - Order 1: Stated, specific falsification condition in research_question.md.
  - Order 2: Outward external empirical grounding (external sources, datasets, and closed escape routes).
  - Order 3: Lakatosian programme-level trajectory across research_log/log.md (Constraint Ratio).

Usage:
  python audit/vibe_audit.py demo-project
  python audit/vibe_audit.py . --output audit_report.md
"""

from __future__ import annotations
import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure local audit directory is importable
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from sandbox import (
    ResearchObject,
    FalsificationCondition,
    Revision,
    DeltaType,
    ResearchSandbox
)


def parse_markdown_sections(text: str) -> Dict[str, str]:
    """Extracts markdown sections by ## Heading."""
    sections = {}
    current_key = "preamble"
    current_content = []
    
    for line in text.splitlines():
        if line.startswith("## "):
            if current_content:
                sections[current_key] = "\n".join(current_content).strip()
            current_key = line[3:].strip().lower()
            current_content = []
        else:
            current_content.append(line)
            
    if current_content:
        sections[current_key] = "\n".join(current_content).strip()
    return sections


def audit_vibe_project(project_path: str | Path) -> Dict[str, Any]:
    """
    Audits a Vibe Researching project folder across Orders 1, 2, and 3.
    Returns the ResearchObject and formatted audit report metadata.
    """
    root = Path(project_path).resolve()
    if not root.exists():
        raise FileNotFoundError(f"Project directory not found: {root}")

    project_id = root.name
    rq_path = root / "research_question.md"
    log_path = root / "research_log" / "log.md"
    models_dir = root / "analysis" / "models"
    raw_data_dir = root / "data" / "raw"
    references_dir = root / "references"

    falsification_conditions: List[FalsificationCondition] = []
    revisions: List[Revision] = []
    audit_notes: List[str] = []

    # --- ORDER 1: Check research_question.md for Falsification Condition ---
    title = project_id
    rq_content = ""
    falsification_text = ""
    external_sources_found: List[str] = []

    if rq_path.exists():
        rq_content = rq_path.read_text(encoding="utf-8")
        sections = parse_markdown_sections(rq_content)
        
        # Extract title / question
        if "question" in sections:
            title = sections["question"].splitlines()[0] if sections["question"] else project_id
        
        # Check falsification section
        for k in sections:
            if "falsification" in k:
                falsification_text = sections[k]
                break

        # Check for external references in text (URLs, DOIs, named datasets, citations)
        urls = re.findall(r'https?://[^\s\)]+', rq_content)
        dois = re.findall(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', rq_content, re.IGNORECASE)
        external_sources_found.extend(urls)
        external_sources_found.extend(dois)
    else:
        audit_notes.append("MISSING_RESEARCH_QUESTION_MD: Project lacks mandatory research_question.md gate.")

    # Check raw data folder for external empirical assets
    if raw_data_dir.exists():
        raw_files = [f.name for f in raw_data_dir.iterdir() if f.is_file() and not f.name.startswith('.')]
        if raw_files:
            external_sources_found.append(f"raw_data_files: {', '.join(raw_files)}")

    # Check references directory
    if references_dir.exists():
        ref_files = [f.name for f in references_dir.iterdir() if f.is_file() and not f.name.startswith('.')]
        if ref_files:
            external_sources_found.append(f"references: {', '.join(ref_files)}")

    # Construct Order 1 & 2 objects
    if falsification_text and not any(placeholder in falsification_text.lower() for placeholder in ["tbd", "to be determined", "none"]):
        # Check if condition points OUTWARD
        has_outward_reference = len(external_sources_found) > 0 or any(kw in falsification_text.lower() for kw in ["p >", "p <", "slope", "reversal", "threshold", "dataset", "control"])
        
        source_note = (
            f"Extracted from {rq_path.name} (Falsification section). "
            f"External anchors: {'; '.join(external_sources_found[:3]) if external_sources_found else 'none'}"
        )
        
        falsification_conditions.append(
            FalsificationCondition(
                id=f"{project_id}-FC1",
                text=falsification_text,
                references_external_source=has_outward_reference,
                source_note=source_note
            )
        )
    else:
        audit_notes.append("ORDER_1_FAIL: No explicit, actionable falsification condition identified in research_question.md.")

    # --- ORDER 2: Substantive Decision Cards & Escape Routes ---
    decision_cards = []
    if models_dir.exists():
        for f in models_dir.glob("*.md"):
            card_text = f.read_text(encoding="utf-8")
            card_sections = parse_markdown_sections(card_text)
            decision_cards.append({
                "file": f.name,
                "sections": card_sections
            })
            # If a decision card documents alternatives, it demonstrates closed escape routes
            if "plausible alternatives considered" in card_sections or "what was chosen" in card_sections:
                external_sources_found.append(f"decision_card: {f.name}")

    # --- ORDER 3: Session Logs & Lakatosian Trajectory ---
    if log_path.exists():
        log_content = log_path.read_text(encoding="utf-8")
        # Split by date headers: ## YYYY-MM-DD
        entries = re.split(r'\n(?=## \d{4}-\d{2}-\d{2})', log_content)
        for entry in entries:
            entry = entry.strip()
            if not entry or not entry.startswith("## "):
                continue
            lines = entry.splitlines()
            date_header = lines[0].replace("##", "").strip()
            body = "\n".join(lines[1:])
            
            # Infer delta type from log entry
            body_low = body.lower()
            delta = DeltaType.EXTENDED
            if any(kw in body_low for kw in ["narrowed", "restricted", "dropped", "excluded outliers", "tightened", "robustness check"]):
                delta = DeltaType.NARROWED
            elif any(kw in body_low for kw in ["withdrawn", "retracted", "rejected hypothesis", "failed check"]):
                delta = DeltaType.WITHDRAWN
            elif any(kw in body_low for kw in ["reaffirmed", "confirmed unchanged", "maintained despite"]):
                delta = DeltaType.REAFFIRMED
            elif any(kw in body_low for kw in ["added", "generated", "scaffolded", "initial"]):
                delta = DeltaType.EXTENDED
                
            revisions.append(
                Revision(
                    delta_type=delta,
                    trigger=f"Session {date_header}: {lines[1][:60] if len(lines) > 1 else 'Progress'}",
                    note=body[:200].replace("\n", " "),
                    source_note=f"Parsed from {log_path.name} date {date_header}"
                )
            )
    else:
        audit_notes.append("MISSING_RESEARCH_LOG: No contemporaneous research_log/log.md found.")

    # Instantiate ResearchObject
    research_obj = ResearchObject(
        id=project_id,
        title=title,
        falsification_conditions=falsification_conditions,
        revisions=revisions,
        self_referential_audit_present=False
    )

    sandbox = ResearchSandbox(objects=[research_obj])
    report = sandbox.full_report()

    return {
        "project_id": project_id,
        "path": str(root),
        "research_object": research_obj,
        "sandbox_report": report,
        "external_anchors": external_sources_found,
        "decision_cards_count": len(decision_cards),
        "audit_notes": audit_notes
    }


def format_markdown_audit_report(audit_result: Dict[str, Any]) -> str:
    """Formats the audit results into a high-grade markdown report."""
    obj: ResearchObject = audit_result["research_object"]
    report = audit_result["sandbox_report"]
    prog = report["programme_level"]
    flags = obj.flags()
    anchors = audit_result["external_anchors"]

    o1_status = "✅ PASS" if obj.order1_pass() else "❌ FAIL"
    o2_status = "✅ PASS" if obj.order2_pass() else "❌ FAIL"
    
    constraint_ratio = prog.get("constraint_ratio")
    c_ratio_str = f"{constraint_ratio:.3f}" if constraint_ratio is not None else "N/A (No revisions)"
    
    # Lakatosian Verdict
    if constraint_ratio is not None and constraint_ratio > 0:
        o3_badge = "✅ PROGRESSIVE"
        o3_detail = "Claims constrained/narrowed by empirical evidence"
    elif prog.get("reaffirmed_unchanged", 0) > 0 and (constraint_ratio is None or constraint_ratio == 0):
        o3_badge = "⚠️ DEGENERATING RISK"
        o3_detail = "Reaffirming claims without narrowing under challenge"
    else:
        o3_badge = "ℹ️ BASELINE"
        o3_detail = "Initial baseline established / No challenge events recorded yet"

    o3_status = f"{o3_badge}: {o3_detail}"

    md = f"""# Third-Order Epistemic Audit Report: {obj.id}

**Audited Target**: `{audit_result['path']}`  
**Theoretical Architecture**: Huynh (2026), *The Third-Order Audit* & *The Research Sandbox*  
**Auditor**: Antigravity Stateless Auditor Engine (`sandbox.py`)  

---

## 📊 Audit Scorecard

| Level | Order Name | Status | Evaluated Metric / Criterion |
| :--- | :--- | :---: | :--- |
| **Order 1** | **Object-Level Falsification** | **{o1_status}** | Explicit falsification condition stated in `research_question.md` |
| **Order 2** | **External Grounding & Escape Routes** | **{o2_status}** | Outward linkage to independent data/records; closed analytical escape routes |
| **Order 3** | **Programme-Level Lakatosian Trajectory** | **{o3_badge}** | Constraint Ratio = `{c_ratio_str}` ({prog.get('narrowed_or_withdrawn', 0)} narrowed/withdrawn of {prog.get('total_revision_events', 0)} total revisions) — {o3_detail} |

---

## 🔍 Detailed Evidence & Audit Trail

### 1. Order 1: Falsification Criterion
"""
    if obj.falsification_conditions:
        for fc in obj.falsification_conditions:
            md += f"- **ID**: `{fc.id}`\n"
            md += f"- **Condition**: *\"{fc.text.strip()}\"*\n"
            md += f"- **Source Note**: `{fc.source_note}`\n\n"
    else:
        md += "> ⚠️ **Warning**: No falsification condition found in `research_question.md`. The project is currently structurally unfalsifiable.\n\n"

    md += f"""### 2. Order 2: External Grounding & Closed Escape Routes
- **External Anchors Detected**: {len(anchors)}
"""
    for a in anchors[:6]:
        md += f"  - `{a}`\n"
    md += f"- **Decision Cards Verified**: `{audit_result['decision_cards_count']}` documented choices in `analysis/models/`.\n"
    md += f"- **Third Break Boundary Risk**: `{'FLAGGED' if obj.third_break_boundary_risk() else 'CLEAR (No self-referential model state queries)'}`\n\n"

    md += f"""### 3. Order 3: Programme Dynamics (Lakatosian Ratio)
- **Total Documented Revisions**: `{prog.get('total_revision_events', 0)}`
- **Narrowed / Withdrawn**: `{prog.get('narrowed_or_withdrawn', 0)}`
- **Reaffirmed Unchanged**: `{prog.get('reaffirmed_unchanged', 0)}`
- **Extended New Material**: `{prog.get('extended_new_material', 0)}`
- **Constraint Ratio**: `{c_ratio_str}`

**Programme Assessment**:
{o3_status}

---

## 🚩 Audit Flags & Recommendations
"""
    if flags:
        md += "The following structural flags were raised:\n"
        for f in flags:
            md += f"- 🔴 `{f}`\n"
    else:
        md += "- 🟢 **Zero Structural Flags**: The project satisfies structural falsifiability, external grounding, and progressive empirical revision.\n"

    if audit_result["audit_notes"]:
        md += "\n**Audit Notes**:\n"
        for n in audit_result["audit_notes"]:
            md += f"- ℹ️ {n}\n"

    return md


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    res = audit_vibe_project(target)
    markdown_report = format_markdown_audit_report(res)
    
    # Save report inside project audit folder
    target_audit_dir = Path(target) / "audit"
    target_audit_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = target_audit_dir / "third_order_audit_report.md"
    report_file.write_text(markdown_report, encoding="utf-8")
    
    # Save sandbox JSON
    json_file = target_audit_dir / "audit_object.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump({"objects": [res["research_object"].to_dict()]}, f, indent=2)
        
    print(markdown_report)
    print(f"\n[+] Audit Report saved to: {report_file}")
    print(f"[+] Sandbox JSON saved to: {json_file}")


if __name__ == "__main__":
    main()
