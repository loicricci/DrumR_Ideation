---
description: Run the full DrumR ideation pipeline — founder intake, 10 ideas, market research, and ranked scoring with gate decisions.
argument-hint: "<initial idea, problem, or domain prompt>"
model: claude-opus-4-8
---

# /ideate — DrumR ideation pipeline

Run the complete DrumR ideation pipeline for this prompt:

**$ARGUMENTS**

Orchestrate the pipeline **in order**, passing each step's output to the next.
You (the orchestrator) run the founder interview yourself, then delegate idea
generation, research, and scoring to the specialist subagents. Verify each
artifact was written before moving on.

> **Important:** the founder interview is run by **you**, not by a subagent.
> Subagents are non-interactive and cannot use `AskUserQuestion`, so the
> interview must happen at this (orchestrator) level. You then hand the finished
> `founder-profile.md` to the `ideator` subagent.

## Step 0 — Create a run directory

Before anything else, generate a run ID using the current date and time
in the format `YYYY-MM-DD-HHmm` (e.g. `2026-06-19-2234`). Create the directory
`output/<run-id>/` using the Write tool (write an empty `.run` file inside it to
materialise the folder). Use this path as `RUN_DIR` for all subsequent steps.

Tell the user: "Starting run `<run-id>` — all artifacts will be saved to `output/<run-id>/`."

## Steps

1. **Founder interview (you run this).** Read `.claude/founder-interview.md` and
   conduct the full 5-round interview yourself using the `AskUserQuestion` tool,
   tailoring every question and its options to the prompt above. If the prompt
   is empty, your first `AskUserQuestion` round should establish the domain or
   starting point. Write the completed profile to
   `output/<run-id>/founder-profile.md` (per `templates/founder-profile.md`) and
   confirm it exists before continuing.

2. **Generate ideas.** Invoke the `ideator` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read and write all
   > files relative to this folder, not to `output/` directly. The founder
   > profile already exists at `output/<run-id>/founder-profile.md` — load it
   > and generate the 10 ideas (do not attempt to interview the user).

   Confirm `output/<run-id>/ideas.md` exists before continuing.

3. **Research.** Invoke the `market-intelligence` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read `output/<run-id>/ideas.md`
   > and write all output to `output/<run-id>/market-research.md`.

   Confirm `output/<run-id>/market-research.md` exists before continuing.

4. **Score & gate.** Invoke the `governance` subagent with this instruction prepended:

   > Run directory for this session: `output/<run-id>/`. Read ideas and market
   > research from `output/<run-id>/` and write `output/<run-id>/scorecard.md`.

   Confirm `output/<run-id>/scorecard.md` exists.

5. **Summarize.** Present a concise final summary to the user:
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
