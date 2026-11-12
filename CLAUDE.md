# DrumR Ideation Kit — project context

This repo is a Claude Code agent kit that turns a rough prompt into a ranked,
evidence-backed shortlist of product ideas. It mirrors the first stage of the
DrumR innovation platform (Idea → Problem–Solution Fit → Product–Market Fit).

## What this tool is (and isn't)

This is **not** a source of absolute truth. It's an evidence-based process that
gathers information and gives the founder:

1. A **relative ranking**: based on what we know, this idea is stronger than
   that one, judged on coherence with market signals and with the founder profile.
2. A **readiness checklist** for P/S Fit: which boxes an idea ticks, and which
   are still open.
3. **Reasons the founder can learn from**: why an idea ranks where it does and
   what would change it.

**The founder decides.** Agents recommend; they never tell the founder what
to do. Any idea can go to P/S Fit when the founder chooses (`/handoff` records
it as a founder push, listing the open boxes). Missing evidence at the idea
stage means "unknown, to test in P/S Fit", never "bad".

## The pipeline

The **orchestrator** (the top-level agent running `/ideate` or `/ideate-fast`)
first conducts a structured founder interview, then runs three specialist
subagents in sequence, each writing an artifact the next one consumes:

0. **Founder interview** — run by the orchestrator, *not* a subagent. Subagents
   are non-interactive and cannot use `AskUserQuestion`, so the interview lives
   at the orchestrator level (spec in `.claude/founder-interview.md`).
   → `output/<run>/founder-profile.md`
1. **`ideator`** — reads the founder profile and generates exactly 10 ideas.
   → `output/<run>/ideas.md`
2. **`market-intelligence`** — researches each idea with cited evidence.
   → `output/<run>/market-research.md`
3. **`governance`** — scores each idea on Desirability / Viability / Feasibility,
   ranks them, and assigns a gate decision. → `output/<run>/scorecard.md`

Run the whole thing with the `/ideate "<your prompt>"` slash command. You can
invoke `ideator`, `market-intelligence`, or `governance` on their own too, but
the `ideator` needs a `founder-profile.md` to exist first (run the interview via
`/ideate`, or write the profile manually).

### Optional packaging step

- **`reporter`** — on demand, consolidates a finished run's four artifacts into a
  single print-ready `summary.html` the founder saves as a PDF. Run with
  `/report` (optionally `/report <run-id>`). It only reformats existing
  artifacts — it never re-scores or re-researches.
  → `output/<run-id>/summary.html`
- **`handoff`** — on demand, exports an idea to P/S Fitter: an Advance idea, or
  any idea the founder decides to push (recorded as `founder_push` with the open
  checklist boxes and the founder's reason), following the handoff requirements v1. Run with
  `/handoff <IDEA-ID | all> [run-id]`. The agent mines verbatim customer quotes
  and competitor data and writes the YAML; `scripts/handoff.py` runs the
  self-check and renders the Markdown from the YAML.
  → `output/<run-id>/project-start-<IDEA-ID>.yaml` (source of truth, shape in
  `templates/project-start.yaml`), `statement-<IDEA-ID>.md` (rendered, never
  hand-edited), and `evidence-<IDEA-ID>.json` when there are more than 20
  evidence items. It never includes prices, max CAC, budgets, thresholds, CTAs
  or copy — P/S Fitter decides those — and leaves `experiment.total_budget` empty.

- **`/psfit`**: produces the P/S Fitter `project-start-<IDEA-ID>.yaml` for
  **every validated idea** (final verdict Advance) across all runs that hasn't
  been exported yet (`/psfit all` re-exports, `/psfit <IDEA-ID>` does one). It
  lists them with `scripts/bank.py validated` and runs the `handoff` flow per idea,
  seeded with the scorecard's "Ready for P/S Fit" note.

### The idea engine (`/engine`)

The goal: **every session ships one idea worth pushing to P/S Fit**, feeding a
target of 10 handed-off ideas. `/engine [focus]` runs:

1. **`signal-scout`** — mines evidenced pain signals (verbatim quotes,
   triggers, WTP) before any idea exists, filtered by the thesis.
   → `output/<run>/signals.md`
2. **ideator → market-intelligence → governance**, with every idea tied to a
   signal and checked against the thesis kill rules.
3. **A capped loop** (max 3 rounds): parked ideas are replaced from unused
   signals and the top Iterate ideas are reframed around their biggest unknown.
   Only new IDs are researched and scored; earlier scores carry forward.
4. **`idea-challenger`** on any Advance idea; only a challenged Advance passes.
5. **`handoff`** exports it to P/S Fitter.
6. **`scripts/bank.py sync`** rebuilds `ideas-bank.md` (every idea across runs,
   status, signals, parent) and the handed-off counter.

Persistent inputs live in `founder/`: `profile.md` (copied into each run) and
`thesis.md` (allowed business shapes and kill rules K1–K7). Edit the thesis to
change what the engine looks for. The gate thresholds are never lowered to get
a pass.

## Conventions

- Ideas keep stable IDs `IDEA-01` … `IDEA-10` across all artifacts. Never
  renumber them — downstream agents join on these IDs. Engine refill rounds add
  `IDEA-11`, `IDEA-12`… (a reframe records its `Parent`).
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
use them.

**Idea score vs recommendation.** The composite is the **idea score**. It ranks
ideas against each other and nothing else. It measures the idea on evidence,
never the founder's current situation, and **missing traction is never
penalized** at the idea stage. The **recommendation** (Advance / Iterate / Park) is a
separate checklist in `.claude/agents/governance.md`:
- G1: no thesis kill rule fires.
- G2: founder–target distance, 0 (inside) to 3 (far); 3 blocks Advance.
- G3: the riskiest assumption is testable in ≤ 4 weeks.
- H1: market exists (Desirability ≥ 7).
- H2: money can work (Monetization ≥ 6, K4 passes).
- H3: a named, plausible edge vs the closest competitor (proof not required).

The gate checks that **enough core hypotheses hold to justify testing**, not
that every answer is known. Advance needs G1, distance ≤ 2, G3 and H1–H3; the
card then includes a short "Ready for P/S Fit" note (broad target, edge, open
questions on persona, problem and solution; P/S Fitter defines the hypotheses). Park is a kill rule or a composite < 6.0. Everything else is Iterate.
These bars are never lowered to produce an Advance; the founder can still push
any idea with `/handoff`, and the open boxes travel with it.

## House style

Be concrete and honest. "AI for X" is not an idea — name the customer, the job
to be done, the wedge, and the money. Surface disconfirming evidence. The goal
is the leanest path to a decision, not a pitch deck.
