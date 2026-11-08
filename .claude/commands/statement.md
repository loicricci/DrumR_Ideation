---
description: >
  Write a one-page idea statement for one idea — persona, problem statement,
  triggers, value proposition, rough economics, scores and assumptions to test —
  as Markdown for people and JSON for import into Problem-Solution Fit.
argument-hint: "<IDEA-ID | advance> [run-id]  e.g. IDEA-03 2026-06-19-2234"
model: claude-opus-4-8
---

# /statement — idea statement for Problem–Solution Fit

**Arguments:** $ARGUMENTS

Parse the arguments as:
- **TARGET** — an idea ID (e.g. `IDEA-03`), or `advance` to write a statement
  for every idea whose gate is **Advance**. Required; if missing, ask.
- **RUN_ID** — optional. If omitted, use the most recently created subfolder of
  `output/`. `RUN_DIR` is `output/<RUN_ID>`.

## Step 1 — Validate

- `RUN_DIR` must contain `founder-profile.md`, `ideas.md`, `market-research.md`
  and `scorecard.md`. If any is missing, tell the user which and what to run
  first (`/ideate`, or the missing agent), then stop.
- If TARGET is an idea ID, check it exists in `ideas.md`; if not, list the
  valid IDs and ask.
- If TARGET is `advance`, read the ranked table in `scorecard.md` and collect
  the Advance ideas. If there are none, say so and offer the top-ranked idea
  instead.

## Step 2 — Write the statement(s)

For each target idea, invoke the `statement` subagent with:

> Run directory: `<RUN_DIR>`. Target idea: `<IDEA_ID>`.
> Read the four run artifacts plus `templates/statement.md` and
> `templates/statement.schema.json`. Write `<RUN_DIR>/statement-<IDEA_ID>.md`
> and `<RUN_DIR>/statement-<IDEA_ID>.json`.

Several ideas can run in parallel; they write separate files.

## Step 3 — Check and hand off

- Confirm both files exist for each idea, and that the JSON file parses.
- Tell the user, per idea: the two paths, the problem statement in one line,
  the rank and gate, and the max CAC (flagged as an assumption).

## Notes

- This command never re-scores: scores, rank and gate come from
  `scorecard.md`.
- The `.md` is for people; the `.json` (schema in
  `templates/statement.schema.json`) is for P/S Fitter to import.
- Re-running overwrites that idea's statement files only.
