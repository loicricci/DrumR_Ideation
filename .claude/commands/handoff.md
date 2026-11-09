---
description: >
  Export an idea that passed the gate to P/S Fitter: project-start-<IDEA-ID>.yaml
  (machine input), statement-<IDEA-ID>.md (human-readable, rendered from the
  YAML) and evidence-<IDEA-ID>.json when there are more than 20 evidence items.
argument-hint: "<IDEA-ID | all> [run-id]  e.g. IDEA-03 2026-06-19-2234"
model: claude-opus-4-8
---

# /handoff — export to P/S Fitter

**Arguments:** $ARGUMENTS

- **TARGET** — an idea ID (e.g. `IDEA-03`), or `all` for every idea whose gate
  is **Advance**. Required; if missing, ask.
- **RUN_ID** — optional; defaults to the most recently created subfolder of
  `output/`. `RUN_DIR` is `output/<RUN_ID>`.

## Step 1 — Validate

- `RUN_DIR` must contain `founder-profile.md`, `ideas.md`, `market-research.md`
  and `scorecard.md`. If not, say which are missing and what to run, then stop.
- Only ideas that **passed the gate** are exported. Read the ranked table in
  `scorecard.md`:
  - If TARGET is an idea with gate Iterate or Park, tell the user it can't be
    exported, give its composite and gate reason, and suggest `/boost` or
    `/challenge`. Stop for that idea.
  - If TARGET is `all`, collect the Advance ideas. If none, say so and stop.

## Step 2 — Country and language

P/S Fitter needs **one country and one language** per idea (where ads run, how
the persona speaks). Infer them from the founder profile's *Geography* and the
idea. If it is unclear, or the idea spans several countries, ask the user with
`AskUserQuestion` (offer the likely options). If they want several countries,
explain that each becomes a separate export, and do one at a time.

## Step 3 — Run the export

For each idea, invoke the `handoff` subagent with:

> Run directory: `<RUN_DIR>`. Idea: `<IDEA_ID>`. Country: `<CC>`. Language:
> `<ll>`. Read the four run artifacts and `templates/project-start.yaml`, mine
> evidence, and write `<RUN_DIR>/project-start-<IDEA_ID>.yaml` (plus
> `<RUN_DIR>/evidence-<IDEA_ID>.json` if more than 20 evidence items).

Several ideas can run in parallel; they write separate files.

## Step 4 — Self-check, then render

For each idea:

1. Run `python3 scripts/handoff.py check <RUN_DIR>/project-start-<IDEA_ID>.yaml`.
2. If anything fails, send the failures back to the `handoff` subagent once and
   ask it to fix them **without inventing evidence**. Run the check again.
3. If failures remain, run the check with `--record-warnings`. This writes them
   to `meta.warnings`, as the spec allows ("export with warnings").
4. Run `python3 scripts/handoff.py render <RUN_DIR>/project-start-<IDEA_ID>.yaml`
   to write `statement-<IDEA_ID>.md` from the YAML. Never write or edit the
   Markdown by hand: the YAML is the source of truth.

If `python3` or PyYAML isn't available, do the self-check yourself against
section 9 of the spec, and write the Markdown strictly from the YAML.

## Step 5 — Hand off

Tell the user, per idea: the file paths; the one-liner; the number of verbatim
quotes and sources; any `meta.warnings`; and that `experiment.total_budget` is
left empty for them to fill in before importing into P/S Fitter.
