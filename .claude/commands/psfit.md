---
description: >
  Produce the P/S Fitter project-start file for every validated idea (final
  verdict Advance) across all runs that hasn't been exported yet, or for one
  named idea. One project-start-<IDEA-ID>.yaml (plus statement and evidence
  files) per idea, ready to import into P/S Fitter after the founder adds the budget.
---

# /psfit — one P/S Fitter project-start file per validated idea

**Arguments:** $ARGUMENTS

- Empty → every validated idea not yet exported, across all runs.
- `all` → every validated idea, including ones already exported (re-export).
- `<IDEA-ID> [run-id]` → that idea only (same as `/handoff <IDEA-ID> [run-id]`).

A **validated idea** is one whose final verdict is **Advance**: the governance
checklist (G1–G3, H1–H3) passed, and if `/challenge` ran, its verdict is Advance.
For an Iterate or Park idea the founder wants to push anyway, use
`/handoff <IDEA-ID>`, which records the founder push and the open boxes.

## Step 1 — Find the validated ideas

Run `python3 scripts/bank.py validated` (add `--all` when the argument is
`all`). It prints a JSON list of `{run, id, title, composite, challenged,
handed_off}`.

- If the list is empty, say so. Then run `python3 scripts/bank.py sync` and
  show the top 3 Iterate ideas from `ideas-bank.md`, so the founder can push one
  with `/handoff`. Stop.
- Otherwise show the founder a short table (run, ID, title, composite,
  challenged yes/no) and proceed with all of them. Don't ask for confirmation:
  running `/psfit` is the decision.

## Step 2 — Country and language per idea

P/S Fitter needs **one country and one language** per file. For each idea,
infer them from `<run>/founder-profile.md` (Geography) and the idea's card and
"Ready for P/S Fit" brief in `<run>/scorecard.md`. Ask once with
`AskUserQuestion`, covering every idea where it's unclear (up to 4 per call),
offering the likely options. Several countries for one idea → one export per
country, run one at a time.

## Step 3 — Export each idea

Follow `.claude/commands/handoff.md` Steps 3–5 for each idea, with
`gate_decision: "pass"` and `recommendation: Advance`. Give the `handoff`
subagent the idea's "Ready for P/S Fit" note from `scorecard.md` as the
starting point. Keep the export a first view: a broad persona, and open
questions on persona, problem and solution. P/S Fitter defines the hypotheses
and tests. Ideas in different runs or with different IDs write separate files, so
run them in parallel.

The output must follow `templates/project-start.yaml` exactly. That's the P/S
Fitter format (handoff requirements v1 §10). Never include prices, max CAC,
budgets, thresholds, CTAs or copy, and leave `experiment.total_budget` empty.

## Step 4 — Self-check, render, record

For each file:

1. `python3 scripts/handoff.py check <run>/project-start-<IDEA-ID>.yaml`. If it
   fails, send the failures back to the `handoff` subagent once (no invented
   evidence), check again, then use `--record-warnings` if failures remain.
2. `python3 scripts/handoff.py render <run>/project-start-<IDEA-ID>.yaml`.
3. After all ideas are done: `python3 scripts/bank.py sync`.

## Step 5 — Report

One block per idea: the paths of the YAML, statement and evidence files; the
one-liner; the persona; the top 3 risks; the number of verbatim quotes and
sources; any `meta.warnings`. End with the handed-off counter from
`ideas-bank.md` and a reminder that `experiment.total_budget` and `currency`
are the founder's to fill before importing into P/S Fitter.
