---
description: Build a polished, print-ready HTML summary of an ideation run that you can save as a PDF (Cmd/Ctrl+P → Save as PDF).
argument-hint: "[run-id, e.g. 2026-06-19-2234 — omit to use the most recent run]"
model: sonnet
---

# /report — package an ideation run into a printable summary

Turn a completed ideation run into a single, self-contained HTML report the
founder can save as a PDF.

**$ARGUMENTS**

## Step 0 — Resolve the run directory

- If `$ARGUMENTS` contains a run ID, use `output/<run-id>/`.
- Otherwise, determine the **most recently created** subdirectory of `output/`
  and use that. If you cannot list directories, ask the user which run to
  summarize (show them the run IDs if you can).

Confirm the chosen run directory contains at least `scorecard.md`. If it does
not, tell the user the run isn't ready (run `/ideate` or the `governance` agent
first) and stop.

## Step 1 — Generate the report

Invoke the `reporter` subagent with this instruction prepended:

> Run directory for this session: `output/<run-id>/`. Read all artifacts from
> this folder and write `output/<run-id>/summary.html`.
> [then the normal reporter task]

Confirm `output/<run-id>/summary.html` was written.

## Step 2 — Hand it off

Tell the user:
- The full path to `summary.html`.
- How to get the PDF: open the file in any browser, then **Cmd/Ctrl + P →
  Save as PDF** (enable "Background graphics" for the colored gate badges).
- The headline result: the #1 ranked idea, its composite score, and its gate.

## Notes

- This command only reads and reformats existing artifacts — it never re-scores
  or re-researches. If the underlying artifacts are stale, re-run `/ideate` (or
  the relevant agent) first, then `/report`.
- The report focuses depth on ideas that reached the **Advance** gate; if none
  did, it details the single highest-composite idea instead.
