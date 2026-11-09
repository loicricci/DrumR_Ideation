# DrumR Ideation Kit

A downloadable [Claude Code](https://code.claude.com) agent kit that turns a
one-line prompt into a **ranked, evidence-backed shortlist of product ideas**.

The `/ideate` orchestrator first **interviews you** (the founder/team) across
**5 rounds** — background, problem proximity, edge, motivation, and constraints
— and saves the result to `output/<run>/founder-profile.md`. (The interview runs
at the orchestrator level because Claude Code subagents are non-interactive and
can't ask you questions.) It then runs three specialist subagents as a pipeline:

| # | Agent | What it does | Output |
|---|-------|--------------|--------|
| 1 | **Ideator** | Reads your founder profile and generates **exactly 10** product ideas grounded in your edge and constraints | `output/ideas.md` |
| 2 | **Market Intelligence** | Researches each idea on the open web — market size, trends, competitors, demand signals, risks — with citations | `output/market-research.md` |
| 3 | **Governance** | Scores every idea on **Desirability, Viability, Feasibility**, ranks them, and gives each a gate decision (Advance / Iterate / Park) | `output/scorecard.md` |
| ★ | **Signal Scout** *(engine)* | Mines evidenced pain signals — verbatim complaints, triggers, willingness to pay — before any idea is generated (`/engine`) | `output/signals.md` |
| ★ | **Reporter** *(on demand)* | Packages a finished run into one polished, print-ready HTML summary you save as a PDF (`/report`) | `output/summary.html` |
| ★ | **Handoff** *(on demand)* | Exports an idea that passed the gate to P/S Fitter: persona, problem in customers' words, triggers, alternatives, competitors, 10+ verbatim quotes, risks (`/handoff`) | `output/project-start-IDEA-NN.yaml` + `statement-IDEA-NN.md` |

It mirrors the first stage of the [DrumR](https://drumr.ai) innovation platform:
**Idea → Problem–Solution Fit → Product–Market Fit.**

---

## Quick start

### 1. Get the kit
Clone or download this repo:

```bash
git clone https://github.com/<you>/drumr-ideation-kit.git
cd drumr-ideation-kit
```

### 2. Open it in Claude Code
```bash
claude
```
Claude Code auto-discovers the agents in `.claude/agents/` and the `/ideate`
command in `.claude/commands/`. (If you started Claude Code before downloading,
run `/agents` or restart the session so they load.)

### 3. Run the pipeline
```text
/ideate "B2B tools for independent climbing gyms"
```

That single command will:
1. interview you about your background and constraints,
2. generate 10 ideas tailored to your edge,
3. research the market for each, and
4. hand you a ranked scorecard with gate decisions.

Everything lands in the `output/` folder as Markdown you can keep, share, or
feed into the next stage.

### 4. (Optional) Export a PDF summary
Once a run looks good, package it into a single printable report:

```text
/report
```

This writes `output/<run-id>/summary.html` — a self-contained, styled document.
Open it in any browser and **Cmd/Ctrl + P → Save as PDF** (enable "Background
graphics" so the colored gate badges print). Pass a run ID to summarize an older
run, e.g. `/report 2026-06-19-2234`.

### 5. (Optional) Hand an idea off to P/S Fitter
Export an idea that reached the **Advance** gate:

```text
/handoff IDEA-03
```

This writes, in the run folder:
- `project-start-IDEA-03.yaml` — the machine input P/S Fitter imports (shape
  in `templates/project-start.yaml`). It is the source of truth.
- `statement-IDEA-03.md` — the same content for people, rendered from the YAML.
- `evidence-IDEA-03.json` — the full evidence list, if there are more than 20 items.

The export digs for **verbatim customer quotes** (at least 10, from at least 3
sources), triggers, alternatives, competitors and counter-evidence, then runs
an automatic self-check (`python3 scripts/handoff.py check …`). Anything it
can't meet is listed in `meta.warnings` instead of being padded. It never sets
prices, budgets, thresholds or ad copy, and leaves `experiment.total_budget`
empty for you to fill in.

Use `/handoff all` to export every Advance idea, and add a run ID for an older
run (`/handoff IDEA-03 2026-06-19-2234`). Ideas that didn't pass the gate are
not exported. The checker needs Python 3 with PyYAML (`pip install pyyaml`).

> **Tip:** You can also run any agent on its own, e.g.
> *"Use the ideator subagent to brainstorm around on-device health AI"* — or
> re-run just `governance` after tweaking the scoring weights.

---

### 6. Run the idea engine (one PSF-ready idea per session)

```
/engine open
/engine "creator tools"
```

`/engine` starts from **evidence instead of a seed idea**: the Signal Scout
mines pain signals first, the ideator ties every idea to a signal, and
governance parks anything that breaks your thesis kill rules
(`founder/thesis.md`). If nothing reaches Advance, it loops (at most 3 rounds):
parked ideas are replaced from unused signals, and the top Iterate ideas are
reframed around their biggest unknown. Any Advance idea must survive an
independent `/challenge` before it is exported with `/handoff`. Progress across
sessions is tracked in `ideas-bank.md` (`python3 scripts/bank.py sync`).

Set it up once: put your profile in `founder/profile.md` and your filters in
`founder/thesis.md`.

## Install globally (use it in any project)

To make the agents available everywhere, copy them into your user scope:

```bash
cp .claude/agents/*.md ~/.claude/agents/
cp .claude/commands/ideate.md ~/.claude/commands/
cp .claude/founder-interview.md ~/.claude/
```

Project-scoped files (`.claude/` in this repo) always take priority over the
global ones when you're inside the project.

---

## How it fits together

```
drumr-ideation-kit/
├── .claude/
│   ├── agents/
│   │   ├── ideator.md              # 1. reads profile -> 10 ideas
│   │   ├── market-intelligence.md  # 2. web research per idea
│   │   ├── governance.md           # 3. scoring + ranking + gate
│   │   ├── signal-scout.md         # ★ engine: evidenced pain signals first
│   │   ├── reporter.md             # ★ printable HTML/PDF summary
│   │   └── handoff.md              # ★ P/S Fitter export
│   ├── commands/
│   │   ├── ideate.md               # /ideate orchestrator
│   │   ├── engine.md               # /engine — loop until one PSF-ready idea
│   │   ├── report.md               # /report — export a PDF summary
│   │   └── handoff.md              # /handoff — export to P/S Fitter
│   ├── founder-interview.md        # interview spec (run by orchestrator)
│   └── settings.json               # tool permissions
├── templates/                      # the shapes the agents fill
│   ├── founder-profile.md
│   ├── idea.md
│   ├── scorecard.md
│   └── project-start.yaml          # P/S Fitter handoff shape
├── scripts/
│   ├── handoff.py                  # handoff self-check + Markdown renderer
│   └── bank.py                     # rebuilds ideas-bank.md, loop status for /engine
├── founder/                        # persistent profile.md + thesis.md (kill rules)
├── ideas-bank.md                   # every idea across runs + handed-off counter
├── output/                         # generated artifacts land here
├── CLAUDE.md                       # shared project context + config
├── LICENSE
└── README.md
```

Each agent is a Markdown file with YAML frontmatter (`name`, `description`,
`tools`, `model`) followed by its system prompt — the standard Claude Code
subagent format. Edit them freely to fit your taste.

---

## Customizing

- **Scoring weights & gate thresholds** — edit `CLAUDE.md`. The default leans on
  desirability: `Composite = 0.40·D + 0.35·V + 0.25·F`.
- **Number of ideas** — change "exactly 10" in `.claude/agents/ideator.md`.
- **Models / cost** — each agent sets `model:` in its frontmatter. `ideator` and
  `governance` use `opus` for reasoning quality; `market-intelligence` uses
  `sonnet`. Drop them to `sonnet`/`haiku` to cut cost, or set `inherit` to use
  your session model.
- **Intake questions** — tailor the interview in `.claude/founder-interview.md`.

---

## Requirements

- [Claude Code](https://code.claude.com) installed and authenticated.
- Web access enabled for the `market-intelligence` agent (it uses `WebSearch`
  and `WebFetch`).

## License

MIT — see [LICENSE](./LICENSE).
