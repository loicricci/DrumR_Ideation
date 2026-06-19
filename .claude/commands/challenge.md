---
description: >
  Challenge the governance verdict for a single idea. An independent counter-agent
  verifies every scored claim, runs targeted research where evidence is weak, and
  always lands on one reconciled final verdict — never two competing opinions.
  Run after /ideate has produced a scorecard.
argument-hint: "<IDEA-ID> <run-dir> [optional: your specific concern]  e.g. IDEA-03 output/2026-06-19-2234 'viability score seems too low'"
model: opus
---

# /challenge — Idea Challenger

Challenge the governance verdict for a single idea.

**Arguments:** $ARGUMENTS

Parse the arguments as:
- **IDEA_ID** — the idea to challenge (e.g. `IDEA-03`). Required.
- **RUN_DIR** — the run directory containing the artifacts (e.g.
  `output/2026-06-19-2234`). Required.
- **CONCERN** — an optional free-text concern from the founder (e.g. "the
  feasibility score seems too harsh given my background"). If provided, pass
  it to the challenger so it can prioritise that dimension. Optional.

If IDEA_ID or RUN_DIR is missing, ask the user before proceeding.

---

## Steps

### 1. Validate inputs

Check that the following files exist in RUN_DIR:
- `<RUN_DIR>/ideas.md`
- `<RUN_DIR>/market-research.md`
- `<RUN_DIR>/scorecard.md`

If any are missing, tell the user which ones and what to run first.

Check that IDEA_ID appears in `<RUN_DIR>/scorecard.md`. If not, list the valid
IDs from the scorecard and ask the user to pick one.

Read the governance gate decision for IDEA_ID from the scorecard and tell the
user: "Challenging governance verdict for <IDEA_ID>: [Gate] with composite
[score]. Running independent audit…"

### 2. Run the challenger

Invoke the `idea-challenger` subagent with this instruction:

> Run directory: `<RUN_DIR>`. Target idea: `<IDEA_ID>`.
> Read `<RUN_DIR>/founder-profile.md`, `<RUN_DIR>/ideas.md`,
> `<RUN_DIR>/market-research.md`, and `<RUN_DIR>/scorecard.md`.
> [If CONCERN was provided]: The founder's specific concern is: "<CONCERN>".
> Prioritise auditing that dimension first.
> Produce the full challenge analysis and write it to
> `<RUN_DIR>/challenge-<IDEA_ID>.md`. You MUST end with one final verdict —
> a single composite score and a single gate decision.

### 3. Confirm and summarize

Confirm `<RUN_DIR>/challenge-<IDEA_ID>.md` was written.

Present a summary to the user that includes:
- Whether the challenge **confirmed** or **revised** the governance verdict.
- The final composite score and gate decision (from Section 5 of the output).
- If revised: the delta (e.g. "Composite moved from 6.8 → 7.6, Gate: Iterate → Advance").
- The single most actionable takeaway from Section 6.
- The path to the full challenge document.

---

## Notes

- `/challenge` operates on **one idea at a time** — it is not a full scorecard
  re-run. For a different idea, run `/challenge` again with a different IDEA_ID.
- The challenger never modifies the original `scorecard.md`. The final verdict
  lives exclusively in `challenge-<IDEA_ID>.md`.
- You can run both `/boost` and `/challenge` on the same idea — they produce
  independent documents and complement each other.
