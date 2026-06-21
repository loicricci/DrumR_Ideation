# DrumR Ideation Kit — project context

This repo is a Claude Code agent kit that turns a rough prompt into a ranked,
evidence-backed shortlist of product ideas. It mirrors the first stage of the
DrumR innovation platform (Idea → Problem–Solution Fit → Product–Market Fit).

## The pipeline

Three specialist subagents run in sequence, each writing an artifact the next
one consumes:

1. **`ideator`** — interviews the founder/team, then generates exactly 10 ideas.
   → `output/founder-profile.md`, `output/ideas.md`
2. **`market-intelligence`** — researches each idea with cited evidence.
   → `output/market-research.md`
3. **`governance`** — scores each idea on Desirability / Viability / Feasibility,
   ranks them, and assigns a gate decision. → `output/scorecard.md`

Run the whole thing with the `/ideate "<your prompt>"` slash command, or invoke
any agent on its own (e.g. "use the ideator subagent to …").

### Optional packaging step

- **`reporter`** — on demand, consolidates a finished run's four artifacts into a
  single print-ready `summary.html` the founder saves as a PDF. Run with
  `/report` (optionally `/report <run-id>`). It only reformats existing
  artifacts — it never re-scores or re-researches.
  → `output/<run-id>/summary.html`

## Conventions

- Ideas keep stable IDs `IDEA-01` … `IDEA-10` across all artifacts. Never
  renumber them — downstream agents join on these IDs.
- Each pipeline run writes to its own timestamped subfolder inside `output/`,
  e.g. `output/2026-06-19-2234/`. This means multiple runs never overwrite each
  other. The orchestrator commands (`/ideate`, `/ideate-fast`) create the folder
  automatically and pass the path to every subagent. Templates live in
  `templates/` (shared, read-only).
- Market claims must be cited. Inferences and estimates must be labeled as such.
- Only the **governance** agent scores or ranks ideas. The ideator and
  market-intelligence agents stay neutral so scoring isn't biased.

## Scoring weights (configurable)

Default early-stage composite:

```
Composite = 0.40 × Desirability + 0.35 × Viability + 0.25 × Feasibility
```

To change the emphasis, edit these weights here and tell the governance agent to
use them. Gate thresholds: **Advance ≥ 7.5**, **Iterate 6.0–7.4**, **Park < 6.0**.

## House style

Be concrete and honest. "AI for X" is not an idea — name the customer, the job
to be done, the wedge, and the money. Surface disconfirming evidence. The goal
is the leanest path to a decision, not a pitch deck.
