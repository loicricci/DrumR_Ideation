---
description: >
  Deep-dive a single idea before entering PSF. Runs extended market research,
  gives founder-specific strategic advice, a risk mitigation playbook, and a
  6-week PSF preparation plan. Run after /ideate or /ideate-fast has scored
  your ideas.
argument-hint: "<IDEA-ID> <run-dir>  e.g. IDEA-03 output/2026-06-19-2234"
model: sonnet
---

# /boost — Idea Booster

Boost a single idea before it enters Problem-Solution Fit.

**Arguments:** $ARGUMENTS

Parse the arguments as:
- **IDEA_ID** — the idea to boost (e.g. `IDEA-03`). Required.
- **RUN_DIR** — the run directory containing the artifacts (e.g.
  `output/2026-06-19-2234`). Required.

If either is missing, ask the user for it before proceeding.

---

## Steps

### 1. Validate inputs

Check that the following files exist in `RUN_DIR`:
- `<RUN_DIR>/founder-profile.md`
- `<RUN_DIR>/ideas.md`
- `<RUN_DIR>/market-research.md`
- `<RUN_DIR>/scorecard.md`

If any are missing, tell the user which ones and what to run first (`/ideate`
and/or the `governance` agent).

Check that `IDEA_ID` appears in `<RUN_DIR>/ideas.md`. If not, list the valid
IDs and ask the user to pick one.

### 2. Run the booster

Invoke the `idea-booster` subagent with this instruction:

> Run directory: `<RUN_DIR>`. Target idea: `<IDEA_ID>`.
> Read `<RUN_DIR>/founder-profile.md`, `<RUN_DIR>/ideas.md`,
> `<RUN_DIR>/market-research.md`, and `<RUN_DIR>/scorecard.md`.
> Produce the full boost analysis and write it to
> `<RUN_DIR>/boost-<IDEA_ID>.md`.

### 3. Confirm and summarize

Confirm `<RUN_DIR>/boost-<IDEA_ID>.md` was written.

Present a brief summary to the user:
- The booster verdict (one sentence).
- The single most important action from the 30-day list.
- The path to the full boost document.

---

## Notes

- Run `/boost IDEA-03 output/2026-06-19-2234` to boost idea 03 from that run.
- You can boost multiple ideas from the same run by running `/boost` again with
  a different IDEA_ID and the same RUN_DIR. Each produces its own
  `boost-IDEA-NN.md` file.
- The booster does not modify any existing artifacts — it only adds a new file.
