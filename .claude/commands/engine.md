---
description: >
  The DrumR idea engine: start from evidenced pain signals, generate ideas that
  fit the solo-founder thesis, research and score them, and loop (refill parked
  ideas, reframe Iterate ideas) until one idea passes the gate AND an
  independent challenge — then export it to P/S Fitter. Updates ideas-bank.md.
argument-hint: "[focus domain | open]  e.g. open · \"creator tools\" · \"small e-commerce\""
model: claude-opus-4-8
---

# /engine — ship one PSF-ready idea per session

**Focus:** $ARGUMENTS (empty means `open`: no domain, let the signals decide)

The aim of every session: **one idea that passes the gate (Advance: checklist G1–G3 pass and composite ≥ 7.5),
survives an independent challenge, and is exported to P/S Fitter.** The bar is
never lowered to hit the aim. If the loop runs out, say so plainly and record
what was learned in the bank.

You are the orchestrator. Subagents are non-interactive, so any question to
the founder is asked by you, at the start, so the rest can run unattended.

## Step 0 — Set up

1. Run ID `YYYY-MM-DD-HHmm`; `RUN_DIR = output/<run-id>/`. Create it with an
   empty `.run` file. Tell the user: "Starting engine run `<run-id>`."
2. **Founder profile.** If `founder/profile.md` exists, copy it to
   `<RUN_DIR>/founder-profile.md`. If it does not, run the interview from
   `.claude/founder-interview.md`, then save the result to both
   `founder/profile.md` and `<RUN_DIR>/founder-profile.md`.
3. **Thesis.** `founder/thesis.md` must exist. If it does not, stop and tell
   the user to create it (the kill rules are what make this an engine rather
   than a brainstorm).
4. Run `python3 scripts/bank.py sync` and read the counter line of
   `ideas-bank.md`.
5. **One question round, then no more.** With a single `AskUserQuestion` call,
   confirm: (a) the profile is still accurate (show the 3–4 key facts);
   (b) the focus, if empty (offer `open` plus 2–3 spaces close to the founder's
   edge that the bank has not covered); (c) the **country and language** for
   the P/S Fitter export (infer from the profile's Geography and offer the
   likely options). Write the answers into `<RUN_DIR>/.run` as
   `focus=…`, `country=…`, `language=…`.

## Step 1 — Signals

Invoke `signal-scout`:

> Run directory: `<RUN_DIR>`. Focus: `<focus>`. Read
> `<RUN_DIR>/founder-profile.md`, `founder/thesis.md` and `ideas-bank.md`.
> Write `<RUN_DIR>/signals.md`.

Check it has at least 10 `## SIG-` sections
(`grep -c '^## SIG-' <RUN_DIR>/signals.md`). If fewer, run it once more with
"refill round 1: widen the search"; if still fewer than 10, continue but tell
the user at the end.

## Step 2 — Round 1: ideate, research, score

1. `ideator`: "Run directory: `<RUN_DIR>`. Engine run. The founder profile is
   at `<RUN_DIR>/founder-profile.md`. Read `founder/thesis.md`,
   `<RUN_DIR>/signals.md` and `ideas-bank.md`. Generate exactly 10 ideas
   (`IDEA-01`…`IDEA-10`), each answering at least one signal and passing the
   thesis kill rules. Write `<RUN_DIR>/ideas.md`."
2. `market-intelligence`: "Run directory: `<RUN_DIR>`. Read
   `<RUN_DIR>/ideas.md` and `<RUN_DIR>/signals.md`; write
   `<RUN_DIR>/market-research.md`."
3. `governance`: "Run directory: `<RUN_DIR>`. Engine run: apply the thesis
   kill check from `founder/thesis.md`, use `<RUN_DIR>/signals.md` as evidence,
   and write `<RUN_DIR>/scorecard.md`."

Confirm each artifact exists before the next step.

## Step 3 — The loop (at most 3 rounds in total)

After each round, run `python3 scripts/bank.py status <RUN_DIR>` and decide:

1. **`advance_unchallenged` is not empty** → challenge the highest one (Step 4).
   If it fails the challenge, challenge the next one. At most **2 challenges
   per session**.
2. **`challenged_advance` is not empty** → go to Step 5 (export).
3. **Otherwise, if this was round 1 or 2** → run a refill round N+1:
   - **Reframes:** the top 2 of `iterate_not_reframed`. For each, take the
     scorecard's "biggest unknown" and ask for one reframe that removes it.
   - **Replacements:** up to 3 new ideas, from `unused_signals`. If fewer than
     3 signals are unused, first run `signal-scout` with "refill round N+1:
     read `<RUN_DIR>/scorecard.md`; find signals in spaces it did not cover".
   - `ideator`: "Refill round N+1 in `<RUN_DIR>`. Append `## Round N+1` to
     `ideas.md` with: reframes of <IDs> (set Parent) and <k> new ideas from
     signals <SIG-IDs>. Start at `<next_free_id>`."
   - `market-intelligence`: "Refill round N+1 in `<RUN_DIR>`: research only
     <new IDs>; append to `market-research.md`."
   - `governance`: "Refill round N+1 in `<RUN_DIR>`: score only <new IDs>,
     carry all earlier scores forward verbatim, rewrite the ranked table,
     append the new cards."
   - Back to the top of Step 3.
4. **Otherwise (3 rounds done, nothing passed)** → go to Step 6 and report
   honestly.

## Step 4 — Independent challenge

Invoke `idea-challenger` exactly as `/challenge` does, for `<IDEA_ID>` in
`<RUN_DIR>`, with the concern: "This idea reached Advance inside an engine
loop. Check for score inflation from iteration, and check it against the kill
rules in founder/thesis.md." It writes `<RUN_DIR>/challenge-<IDEA_ID>.md`. The
challenger's final gate is the one that counts: only a challenged **Advance**
is exported.

## Step 5 — Export to P/S Fitter

For the challenged Advance idea, follow `.claude/commands/handoff.md` Steps 3–4
with the country and language from `<RUN_DIR>/.run`: the `handoff` subagent
writes `project-start-<IDEA_ID>.yaml`, then run
`python3 scripts/handoff.py check …` (one fix pass, then `--record-warnings`
if needed) and `python3 scripts/handoff.py render …`.

Export **one idea per session** by default. If a second idea is also a
challenged Advance, record it in the summary as ready for `/handoff`.

## Step 6 — Update the bank and report

1. `python3 scripts/bank.py sync`.
2. If the project is a git repository, commit the run folder and
   `ideas-bank.md`.
3. Tell the user:
   - the run ID and folder;
   - **shipped:** the exported idea, its one-liner, composite (governance and
     challenge), the files written, any `meta.warnings`, and that
     `experiment.total_budget` is empty for them to fill in;
   - **or not shipped:** the best idea, how close it got, and the one thing
     that kept it below the bar — plus what the next session should focus on;
   - the bank counter: handed off X / target.

## Rules

- Never lower the gate thresholds, skip the challenge, or re-score an
  unchanged idea to get a pass.
- Never renumber ideas; new ideas take the next free ID.
- The only question round is Step 0. After that, run to the end.
