#!/usr/bin/env python3
"""Render and check P/S Fitter handoff files (handoff requirements v1).

Usage:
  python3 scripts/handoff.py render <project-start-IDEA-NN.yaml>
      Writes statement-IDEA-NN.md next to the YAML, built only from the YAML
      (and evidence-IDEA-NN.json if referenced), so the two never disagree.

  python3 scripts/handoff.py check <project-start-IDEA-NN.yaml> [--record-warnings]
      Runs the self-check from section 9. Exit code 0 = all pass, 1 = failures.
      With --record-warnings, every failure is written to meta.warnings in the
      YAML (the spec's "export with warnings" route) and the exit code is 0.

Requires PyYAML (pip install pyyaml).
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

EVIDENCE_TYPES = {"customer_quote", "paraphrase", "competitor_ad", "competitor_page",
                  "review", "stat", "article", "regulation"}
ALT_TYPES = {"diy", "competitor", "service", "do_nothing"}
PERSONA_MATCH = {"yes", "likely", "unclear"}
STRENGTH = {"strong", "medium", "weak"}
RISK_CATEGORIES = {"desirability", "viability", "feasibility"}
SUPPORTS_RE = re.compile(r"^(problem|trigger:\d+|alternative:.+|wtp|market|counter)$")
# Keys P/S Fitter decides itself (section 8). Prices of alternatives/competitors are allowed.
FORBIDDEN_KEY_RE = re.compile(
    r"(price_recommendation|recommended_price|target_price|max_cac|cac|acquisition_cost|"
    r"conversion|budget_split|threshold|success_criteria|cta|call_to_action|ad_copy|"
    r"landing_copy|landing_page_copy|gdpr|legal_text)", re.I)
# Words that describe a solution rather than a pain (EN + FR + DE + ES), checked in problem text.
SOLUTION_WORDS_RE = re.compile(
    r"(?i:\b(app|application|tool|platform|software|saas|automat\w*|dashboard|solution|"
    r"outil|logiciel|plateforme|automatis\w*|werkzeug|plattform|herramienta|plataforma)\b)"
    r"|(?<!['’])\b(AI|IA|KI)\b")
PERSONAL_DATA_RES = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "email address"),
    (re.compile(r"(?<![\w/])u/[\w-]{3,}"), "Reddit username"),
    (re.compile(r"(?<![\w.])@[A-Za-z0-9_]{3,}"), "@handle"),
]


def load(path):
    path = Path(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    evidence = list(data.get("evidence") or [])
    ev_file = data.get("evidence_file")
    if ev_file:
        p = Path(ev_file)
        if not p.is_absolute() and not p.exists():
            p = path.parent / p.name
        if p.exists():
            extra = json.loads(p.read_text(encoding="utf-8"))
            extra = extra.get("evidence", extra) if isinstance(extra, dict) else extra
            seen = {e.get("id") for e in evidence}
            evidence += [e for e in extra if e.get("id") not in seen]
    return data, evidence


def as_date(value):
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        for fmt, n in (("%Y-%m-%d", 10), ("%Y-%m", 7), ("%Y", 4)):
            try:
                return dt.datetime.strptime(value.strip()[:n], fmt).date()
            except ValueError:
                pass
    return None


def blank(v):
    return v is None or (isinstance(v, (str, list, dict)) and len(v) == 0)


def walk_keys(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}" if path else str(k)
            yield p, str(k), v
            yield from walk_keys(v, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_keys(v, f"{path}[{i}]")


def walk_strings(node, path=""):
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}" if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")


def check(data, evidence, yaml_path):
    fails = []
    f = fails.append
    g = lambda *keys: _get(data, keys)

    # meta
    for k in ("schema_version", "idea_id", "run_id", "generated_at", "generated_by"):
        if blank(g("meta", k)):
            f(f"meta.{k} is missing")
    if str(g("meta", "schema_version")) != "1":
        f('meta.schema_version must be "1"')
    idea_id = str(g("meta", "idea_id") or "")
    if idea_id and not re.fullmatch(r"IDEA-\d{2}", idea_id):
        f("meta.idea_id must look like IDEA-03")
    if idea_id and idea_id not in Path(yaml_path).name:
        f(f"file name does not match meta.idea_id ({idea_id})")
    ga = g("meta", "generated_at")
    if ga and not isinstance(ga, dt.datetime):
        try:
            dt.datetime.fromisoformat(str(ga).replace("Z", "+00:00"))
        except ValueError:
            f("meta.generated_at is not ISO 8601")
    if blank(g("source", "statement")):
        f("source.statement is missing")

    # gate
    gate = str(g("ideation", "gate_decision") or "").lower()
    if gate not in ("pass", "founder_push"):
        f(f'ideation.gate_decision must be "pass" or "founder_push" (got "{gate or "empty"}")')
    if gate == "founder_push" and blank(g("ideation", "founder_rationale")):
        f("ideation.founder_rationale is required when gate_decision is founder_push")

    # project: one country, one language
    for k in ("name", "one_liner", "country", "language"):
        if blank(g("project", k)):
            f(f"project.{k} is missing")
    if g("project", "country") and not re.fullmatch(r"[A-Z]{2}", str(g("project", "country"))):
        f("project.country must be one ISO 3166-1 alpha-2 code (e.g. FR)")
    if g("project", "language") and not re.fullmatch(r"[a-z]{2}", str(g("project", "language"))):
        f("project.language must be one ISO 639-1 code (e.g. fr)")
    ol = str(g("project", "one_liner") or "")
    if len(ol.split()) > 25:
        f(f"project.one_liner has {len(ol.split())} words (max 25)")
    name_words = len(str(g("project", "name") or "").split())
    if name_words and not 2 <= name_words <= 4:
        f("project.name should be 2–4 words")

    # persona
    for k in ("name", "role", "context"):
        if blank(g("persona", k)):
            f(f"persona.{k} is missing")
    if blank(g("persona", "where_they_are")):
        f("persona.where_they_are is empty (strongly recommended: name where 10 of them can be found)")
    if blank(g("persona", "not_this_persona")):
        f("persona.not_this_persona is empty (recommended: at least one exclusion)")

    # problem
    pw = str(g("problem", "in_their_words") or "")
    if not pw:
        f("problem.in_their_words is missing")
    m = SOLUTION_WORDS_RE.search(pw)
    if m:
        f(f'problem.in_their_words contains a solution word ("{m.group(0)}")')

    ids = {}
    for e in evidence:
        eid = e.get("id")
        if eid in ids:
            f(f"evidence id {eid} is duplicated")
        ids[eid] = e

    def refs_ok(where, refs):
        for r in refs or []:
            if r not in ids:
                f(f"{where} references unknown evidence id {r}")

    refs_ok("problem.evidence_ids", g("problem", "evidence_ids"))

    # triggers
    triggers = g("triggers") or []
    if not 2 <= len(triggers) <= 3:
        f(f"triggers must have 2–3 items (has {len(triggers)})")
    for i, t in enumerate(triggers, 1):
        if blank(t.get("text")):
            f(f"trigger {i} has no text")
        if blank(t.get("evidence_ids")):
            f(f"trigger {i} is not linked to any evidence")
        refs_ok(f"trigger {i}", t.get("evidence_ids"))

    # alternatives
    alts = g("alternatives") or []
    types = [a.get("type") for a in alts]
    if "do_nothing" not in types:
        f("alternatives must include do nothing (type: do_nothing)")
    if len([t for t in types if t != "do_nothing"]) < 1:
        f("alternatives need at least one option besides do nothing")
    for a in alts:
        if a.get("type") not in ALT_TYPES:
            f(f'alternative "{a.get("name")}" has invalid type "{a.get("type")}"')
        if blank(a.get("why_insufficient")):
            f(f'alternative "{a.get("name")}" has no why_insufficient')
        refs_ok(f'alternative "{a.get("name")}"', a.get("evidence_ids"))

    # solution
    if blank(g("solution", "hypothesis")):
        f("solution.hypothesis is missing")

    # evidence items
    today = dt.date.today()
    for e in evidence:
        eid = e.get("id", "?")
        if not re.fullmatch(r"E\d{2,}", str(eid)):
            f(f"evidence id {eid} must look like E01")
        if e.get("type") not in EVIDENCE_TYPES:
            f(f'{eid}: invalid type "{e.get("type")}"')
        if e.get("type") in ("customer_quote", "paraphrase", "review") and blank(e.get("quote")):
            f(f"{eid}: quote is missing")
        for k in ("source_name", "date", "persona_match", "supports", "strength"):
            if blank(e.get(k)):
                f(f"{eid}: {k} is missing")
        if blank(e.get("url")):
            f(f"{eid}: no url (required when the source is public)")
        if e.get("persona_match") and e["persona_match"] not in PERSONA_MATCH:
            f(f'{eid}: invalid persona_match "{e["persona_match"]}"')
        if e.get("strength") and e["strength"] not in STRENGTH:
            f(f'{eid}: invalid strength "{e["strength"]}"')
        if e.get("supports") and not SUPPORTS_RE.match(str(e["supports"])):
            f(f'{eid}: invalid supports "{e["supports"]}"')
        if e.get("type") == "paraphrase" and e.get("strength") != "weak":
            f(f"{eid}: paraphrases must be strength: weak")
        d = as_date(e.get("date"))
        if d and (today - d).days > 730 and e.get("strength") != "weak":
            f(f"{eid}: older than 24 months but not marked weak")
        if e.get("type") == "competitor_ad" and blank(e.get("running_since")):
            f(f"{eid}: competitor ads need running_since")

    gaps = " ".join(str(x) for x in (g("evidence_gaps") or [])).lower()
    quotes = [e for e in evidence if e.get("type") == "customer_quote"]
    q_sources = {str(e.get("source_name", "")).split("–")[0].split(" - ")[0].strip().lower()
                 for e in quotes}
    if len(quotes) < 10:
        f(f"only {len(quotes)} verbatim customer quotes (minimum 10)")
    if len(q_sources) < 3:
        f(f"customer quotes come from {len(q_sources)} distinct sources (minimum 3)")
    competitors = (g("market", "known_competitors") or [])
    n_comp = max(len([c for c in competitors if c.get("name")]), types.count("competitor"))
    if n_comp < 2 and "competitor" not in gaps:
        f(f'{n_comp} competitors described (minimum 2, or "none found" in evidence_gaps)')
    if not any(e.get("supports") == "counter" for e in evidence) and "counter" not in gaps:
        f("no counter-evidence and no note in evidence_gaps that none was found")
    if len(evidence) > 20 and blank(g("evidence_file")):
        f("more than 20 evidence items but no evidence_file")

    # risks
    risks = g("risks") or []
    if not 3 <= len(risks) <= 7:
        f(f"risks must have 3–7 items (has {len(risks)})")
    for i, r in enumerate(risks, 1):
        if blank(r.get("assumption")):
            f(f"risk {i} has no assumption")
        if r.get("category") not in RISK_CATEGORIES:
            f(f'risk {i} has invalid category "{r.get("category")}"')
        if blank(r.get("why_uncertain")):
            f(f"risk {i} has no why_uncertain")
        refs_ok(f"risk {i}", r.get("evidence_ids"))

    # decisions P/S Fitter owns
    if not blank(g("experiment", "total_budget")):
        f("experiment.total_budget must be left empty (the founder sets it)")
    for path, key, _ in walk_keys({k: v for k, v in data.items() if k != "notes"}):
        if FORBIDDEN_KEY_RE.search(key):
            f(f"{path}: P/S Fitter decides this (section 8) — remove it or move it to notes")

    # personal data
    rest = {k: v for k, v in data.items() if k != "evidence"}
    for path, text in list(walk_strings(rest)) + list(walk_strings(evidence, "evidence")):
        if path.endswith(".url") or path.endswith("url"):
            continue
        for rx, label in PERSONAL_DATA_RES:
            if rx.search(text):
                f(f"{path}: looks like personal data ({label})")
    return fails


def _get(d, keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def esc(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def render(data, evidence, yaml_path):
    g = lambda *keys: _get(data, keys)
    by_id = {e.get("id"): e for e in evidence}
    out = []
    w = out.append

    def refs(ids):
        return f" ({', '.join(ids)})" if ids else ""

    meta = g("meta") or {}
    w(f"# {meta.get('idea_id', '')} · {g('project', 'name')}")
    w("")
    w(f"> {g('project', 'one_liner')}")
    w("")
    w(f"**Country:** {g('project', 'country')} · **Language:** {g('project', 'language')} · "
      f"**Run:** {meta.get('run_id')} · **Generated:** {meta.get('generated_at')} by {meta.get('generated_by')}"
      + (f" · **Variation of:** {meta['parent_idea_id']}" if meta.get("parent_idea_id") else ""))
    if meta.get("warnings"):
        w("")
        w("> ⚠️ **Exported with warnings:**")
        for x in meta["warnings"]:
            w(f"> - {x}")

    w("\n## Persona\n")
    w(f"**{g('persona', 'name')}** — {g('persona', 'role')}\n")
    w(f"{g('persona', 'context')}\n")
    if g("persona", "where_they_are"):
        w("- **Where they are:** " + "; ".join(map(str, g("persona", "where_they_are"))))
    if g("persona", "not_this_persona"):
        w("- **Not this persona:** " + "; ".join(map(str, g("persona", "not_this_persona"))))

    w("\n## Problem\n")
    w(f"> “{g('problem', 'in_their_words')}”{refs(g('problem', 'evidence_ids'))}\n")
    if g("problem", "how_often"):
        w(f"- **How often:** {g('problem', 'how_often')}")
    if g("problem", "what_it_costs_them"):
        w(f"- **What it costs them:** {g('problem', 'what_it_costs_them')}")
    for s in g("problem", "severity_signals") or []:
        w(f"- **Severity signal:** {s}")

    w("\n## Triggers — when it hurts most\n")
    for i, t in enumerate(g("triggers") or [], 1):
        w(f"{i}. {t.get('text')}{refs(t.get('evidence_ids'))}")

    w("\n## Alternatives today\n")
    w("| Alternative | Type | Why it falls short | Price | Link |")
    w("|---|---|---|---|---|")
    for a in g("alternatives") or []:
        w(f"| {esc(a.get('name'))} | {esc(a.get('type'))} | {esc(a.get('why_insufficient'))}"
          f"{esc(refs(a.get('evidence_ids')))} | {esc(a.get('price'))} | {esc(a.get('url'))} |")

    mk = g("market") or {}
    if any(mk.get(k) for k in ("conditions", "size_signal", "timing", "known_competitors")):
        w("\n## Market\n")
        for c in mk.get("conditions") or []:
            w(f"- {c.get('text')} — {c.get('source')} ({c.get('date')})")
        if mk.get("size_signal"):
            w(f"- **Size signal:** {mk['size_signal']}")
        if mk.get("timing"):
            w(f"- **Timing:** {mk['timing']}")
        comps = [c for c in mk.get("known_competitors") or [] if c.get("name")]
        if comps:
            w("\n| Competitor | Positioning | Public price | Target persona |")
            w("|---|---|---|---|")
            for c in comps:
                name = f"[{esc(c['name'])}]({c['url']})" if c.get("url") else esc(c["name"])
                w(f"| {name} | {esc(c.get('positioning'))} | {esc(c.get('price'))} | {esc(c.get('target_persona'))} |")

    w("\n## Solution hypothesis\n")
    w(f"{g('solution', 'hypothesis')}\n")
    if g("solution", "wedge"):
        w(f"- **Wedge:** {g('solution', 'wedge')}")
    if g("solution", "mvp_shape"):
        w(f"- **MVP shape:** {g('solution', 'mvp_shape')}")
    if g("solution", "not_doing"):
        w("- **Not doing:** " + "; ".join(map(str, g("solution", "not_doing"))))

    w("\n## Risks — riskiest first\n")
    w("| # | Assumption | Category | Why uncertain | Evidence | How to test |")
    w("|---|---|---|---|---|---|")
    for i, r in enumerate(g("risks") or [], 1):
        w(f"| {i} | {esc(r.get('assumption'))} | {esc(r.get('category'))} | {esc(r.get('why_uncertain'))} | "
          f"{esc(', '.join(r.get('evidence_ids') or []))} | {esc(r.get('how_to_test'))} |")

    w(f"\n## Evidence ({len(evidence)} items)\n")
    for e in evidence:
        head = f"**{e.get('id')}** · {e.get('type')} · {e.get('source_name')} · {e.get('date')} · " \
               f"persona: {e.get('persona_match')} · supports: {e.get('supports')} · {e.get('strength')}"
        if e.get("running_since"):
            head += f" · running since {e['running_since']}"
        w(f"- {head}")
        if e.get("quote"):
            w(f"  > “{e['quote']}”")
        if e.get("translation"):
            w(f"  > *{e['translation']}*")
        if e.get("url"):
            w(f"  <{e['url']}>")
    if g("evidence_gaps"):
        w("\n**Evidence gaps (searches that found nothing):**\n")
        for x in g("evidence_gaps"):
            w(f"- {x}")

    ide = g("ideation") or {}
    w("\n## Ideation scores (context only)\n")
    scores = ", ".join(f"{k} {v}" for k, v in (ide.get("scores") or {}).items())
    w(f"Rank {ide.get('rank')} · {scores} · composite {ide.get('composite')} · "
      f"gate {ide.get('gate_decision')} · scored by {ide.get('scored_by')}")
    if str(ide.get("gate_decision") or "").lower() == "founder_push":
        w("")
        w(f"**Pushed by founder decision** (governance recommendation: "
          f"{ide.get('recommendation') or '—'}). Reason: {ide.get('founder_rationale')}")
        if ide.get("open_checks"):
            w("Open checklist boxes for P/S Fit to test: " + "; ".join(map(str, ide["open_checks"])))

    if g("notes"):
        w("\n## Notes (opinions, not inputs)\n")
        w(str(g("notes")))

    w("\n---")
    w(f"*Generated from `{Path(yaml_path).name}` (the source of truth). "
      f"Do not edit this file by hand — edit the YAML and re-render.*")
    unknown = sorted({r for t in g("triggers") or [] for r in t.get("evidence_ids") or []} - set(by_id))
    if unknown:
        w(f"\n*Unresolved evidence ids: {', '.join(unknown)}*")
    return "\n".join(out) + "\n"


def main(argv):
    if len(argv) < 3 or argv[1] not in ("render", "check"):
        sys.exit(__doc__)
    cmd, path = argv[1], Path(argv[2])
    if not path.exists():
        sys.exit(f"not found: {path}")
    try:
        data, evidence = load(path)
    except yaml.YAMLError as exc:
        print(f"FAIL: YAML does not parse: {exc}")
        return 1
    if cmd == "render":
        md_name = path.name.replace("project-start-", "statement-").rsplit(".", 1)[0] + ".md"
        md = path.parent / md_name
        md.write_text(render(data, evidence, path), encoding="utf-8")
        print(f"wrote {md}")
        return 0
    fails = check(data, evidence, path)
    if not fails:
        print(f"PASS: {path.name} meets the handoff self-check")
        return 0
    for x in fails:
        print(f"FAIL: {x}")
    if "--record-warnings" in argv:
        meta = data.setdefault("meta", {})
        meta["warnings"] = sorted(set((meta.get("warnings") or []) + fails))
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100),
                        encoding="utf-8")
        print(f"recorded {len(fails)} warning(s) in meta.warnings")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
