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

## Steps

1. **Ideate.** Invoke the `ideator` subagent.
   - It will interview the founder/team (or read an existing
     `output/founder-profile.md`) and then generate exactly 10 ideas from the
     prompt above.
   - If the prompt above is empty, the ideator should ask the user for a domain
     or starting point.
   - Confirm `output/founder-profile.md` and `output/ideas.md` exist before
     continuing.

2. **Research.** Invoke the `market-intelligence` subagent.
   - It reads `output/ideas.md` and researches all 10 ideas with cited evidence.
   - Confirm `output/market-research.md` exists before continuing.

3. **Score & gate.** Invoke the `governance` subagent.
   - It reads the ideas and the market research, scores each idea on
     Desirability / Viability / Feasibility, ranks them, and assigns a gate
     decision.
   - Confirm `output/scorecard.md` exists.

4. **Summarize.** Present a concise final summary to the user:
   - The ranked top 3 with their composite scores and gate decisions.
   - The single most important next validation step for the #1 idea.
   - Pointers to the four artifacts in `output/`.

## Notes

- Run the steps sequentially — each depends on the previous artifact.
- If any artifact is missing or malformed, re-run that step before proceeding
  rather than fabricating its content.
- Keep the founder's constraints and anti-goals (from the profile) in view the
  whole way through.
