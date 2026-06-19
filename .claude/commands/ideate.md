---
description: Run the full DrumR ideation pipeline — founder intake, 10 ideas, market research, and ranked scoring with gate decisions.
argument-hint: "<initial idea, problem, or domain prompt>"
model: opus
---

# /ideate — DrumR ideation pipeline

Run the complete DrumR ideation pipeline for this prompt:

**$ARGUMENTS**

Orchestrate the three specialist subagents **in order**, passing each one's
output to the next. Do not do their work yourself — delegate, then verify the
artifact was written before moving on.

## Step 0 — Create a run directory

Before invoking any subagent, generate a run ID using the current date and time
in the format `YYYY-MM-DD-HHmm` (e.g. `2026-06-19-2234`). Create the directory
`output/<run-id>/` using the Write tool (write an empty `.run` file inside it to
materialise the folder). Use this path as `RUN_DIR` for all subsequent steps.

Tell the user: "Starting run `<run-id>` — all artifacts will be saved to `output/<run-id>/`."

## Steps

1. **Ideate.** Invoke the `ideator` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read and write all
   > files relative to this folder, not to `output/` directly.
   > [then the normal ideator task]

   If the prompt above is empty, the ideator should ask the user for a domain
   or starting point. Confirm `output/<run-id>/founder-profile.md` and
   `output/<run-id>/ideas.md` exist before continuing.

2. **Research.** Invoke the `market-intelligence` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read `output/<run-id>/ideas.md`
   > and write all output to `output/<run-id>/market-research.md`.

   Confirm `output/<run-id>/market-research.md` exists before continuing.

3. **Score & gate.** Invoke the `governance` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read ideas and market
   > research from `output/<run-id>/` and write `output/<run-id>/scorecard.md`.

   Confirm `output/<run-id>/scorecard.md` exists.

4. **Summarize.** Present a concise final summary to the user:
   - The run ID and folder where all artifacts are stored.
   - The ranked top 3 with their composite scores and gate decisions.
   - The single most important next validation step for the #1 idea.

## Notes

- Run the steps sequentially — each depends on the previous artifact.
- If any artifact is missing or malformed, re-run that step before proceeding
  rather than fabricating its content.
- Keep the founder's constraints and anti-goals (from the profile) in view the
  whole way through.
- Each `/ideate` invocation creates its own isolated folder — previous runs are
  never overwritten.
