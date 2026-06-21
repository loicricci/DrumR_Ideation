---
description: >
  Fast-track DrumR ideation pipeline. Produces 5 ideas (instead of 10),
  uses lighter market research, and runs entirely on Sonnet. Use when you
  want a ranked shortlist in roughly half the time of /ideate.
argument-hint: "<initial idea, problem, or domain prompt>"
model: claude-opus-4-8
---

# /ideate-fast — DrumR fast ideation pipeline

Run the accelerated DrumR ideation pipeline for this prompt:

**$ARGUMENTS**

This is the **speed-optimised variant**: 5 ideas, lighter research, Sonnet
throughout. It follows the same structure as `/ideate` but with tighter scope
at every step.

> **Important:** the founder interview is run by **you** (the orchestrator), not
> by a subagent. Subagents are non-interactive and cannot use `AskUserQuestion`.
> You run the interview, then hand the finished profile to the `ideator`.

---

## Step 0 — Create a run directory

Before anything else, generate a run ID using the current date and time
in the format `YYYY-MM-DD-HHmm-fast` (e.g. `2026-06-19-2234-fast`). Create the
directory `output/<run-id>/` using the Write tool (write an empty `.run` file
inside it to materialise the folder). Use this path as `RUN_DIR` for all
subsequent steps.

Tell the user: "Starting fast run `<run-id>` — all artifacts will be saved to `output/<run-id>/`."

## Steps

### 1. Founder interview (you run this)

Read `.claude/founder-interview.md` and conduct the interview yourself using the
`AskUserQuestion` tool. For speed, use the **3-round** compressed variant
described at the bottom of that file. Write the completed profile to
`output/<run-id>/founder-profile.md` and confirm it exists before continuing.

### 2. Ideate (fast)

Invoke the `ideator` subagent with this instruction:

> Run directory for this session: `output/<run-id>/`. Read and write all files
> relative to this folder. The founder profile already exists at
> `output/<run-id>/founder-profile.md` — load it (do not interview the user).
> Then generate exactly **5** ideas — apply the same quality rules but halve the
> count. Write them to `output/<run-id>/ideas.md` using IDs `IDEA-01` … `IDEA-05`.

Confirm `output/<run-id>/ideas.md` (with exactly 5 ideas) exists before continuing.

### 3. Research (fast)

Invoke the `market-intelligence` subagent with this instruction:

> Run directory for this session: `output/<run-id>/`. Read
> `output/<run-id>/ideas.md`. Research all 5 ideas in **one parallel batch** —
> fire all WebSearch calls simultaneously. Hard cap: **1 WebSearch + 1 WebFetch
> per idea**. Focus on the single highest-signal finding for each of: market
> size, top competitor, demand evidence, and key risk. Confidence level is
> required. Write `output/<run-id>/market-research.md`.

Confirm `output/<run-id>/market-research.md` exists before continuing.

### 4. Score & gate (fast)

Invoke the `governance` subagent with this instruction:

> Run directory for this session: `output/<run-id>/`. Read ideas and market
> research from `output/<run-id>/`. Score all 5 ideas using the standard rubric
> and weights. For speed, provide one rationale sentence per dimension (not per
> sub-criterion). Assign gate decisions and write `output/<run-id>/scorecard.md`.

Confirm `output/<run-id>/scorecard.md` exists.

### 5. Summarize

Present a concise final summary to the user:
- The run ID and folder where all artifacts are stored.
- The ranked top 2 with their composite scores and gate decisions.
- The single highest-priority validation step for the #1 idea.

---

## Notes

- Each run creates its own isolated folder — previous runs are never overwritten.
- Profile reuse: if `output/<run-id>/founder-profile.md` already exists, the
  orchestrator confirms the key facts in one message and skips the interview. To
  reuse a profile from a previous run, copy it into the new run folder before
  starting.
- To get more depth on any idea after this run, invoke `market-intelligence`
  directly on the idea of interest.
