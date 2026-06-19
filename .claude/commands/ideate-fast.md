---
description: >
  Fast-track DrumR ideation pipeline. Produces 5 ideas (instead of 10),
  uses lighter market research, and runs entirely on Sonnet. Use when you
  want a ranked shortlist in roughly half the time of /ideate.
argument-hint: "<initial idea, problem, or domain prompt>"
model: sonnet
---

# /ideate-fast — DrumR fast ideation pipeline

Run the accelerated DrumR ideation pipeline for this prompt:

**$ARGUMENTS**

This is the **speed-optimised variant**: 5 ideas, lighter research, Sonnet
throughout. It follows the same three-agent structure as `/ideate` but with
tighter scope at every step.

---

## Steps

### 1. Ideate (fast)

Invoke the `ideator` subagent with this instruction:

> Run Phase 1 (founder intake) exactly as specified. Then in Phase 2, generate
> exactly **5** ideas instead of 10 — apply the same quality rules but halve
> the count. Write them to `output/ideas.md` using IDs `IDEA-01` … `IDEA-05`.

Confirm `output/founder-profile.md` and `output/ideas.md` (with exactly 5 ideas)
exist before continuing.

### 2. Research (fast)

Invoke the `market-intelligence` subagent with this instruction:

> Research all 5 ideas in **one parallel batch** — fire all WebSearch calls
> simultaneously. Hard cap: **1 WebSearch + 1 WebFetch per idea**. Focus on the
> single highest-signal finding for each of: market size, top competitor,
> demand evidence, and key risk. Confidence level is required. Write
> `output/market-research.md`.

Confirm `output/market-research.md` exists before continuing.

### 3. Score & gate (fast)

Invoke the `governance` subagent with this instruction:

> Score all 5 ideas using the standard rubric and weights. For speed, provide
> one rationale sentence per dimension (not per sub-criterion). Assign gate
> decisions and write `output/scorecard.md`.

Confirm `output/scorecard.md` exists.

### 4. Summarize

Present a concise final summary to the user:
- The ranked top 2 with their composite scores and gate decisions.
- The single highest-priority validation step for the #1 idea.
- Pointers to the four artifacts in `output/`.

---

## Notes

- Artifacts use the same file names as `/ideate` — running fast mode will
  overwrite any existing outputs. Rename the `output/` folder first if you want
  to preserve a previous run.
- Profile reuse works the same way: if `output/founder-profile.md` already
  exists the ideator skips the interview.
- To get more depth on any idea after this run, invoke `market-intelligence`
  directly on the idea of interest.
