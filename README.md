# DrumR Ideation Kit

A downloadable [Claude Code](https://code.claude.com) agent kit that turns a
one-line prompt into a **ranked, evidence-backed shortlist of product ideas**.

It deploys three specialist subagents that run as a pipeline:

| # | Agent | What it does | Output |
|---|-------|--------------|--------|
| 1 | **Ideator** | Interviews you (the founder/team) across **5 rounds** for background, problem proximity, edge, motivation, and constraints, then generates **exactly 10** product ideas from your prompt | `output/founder-profile.md`, `output/ideas.md` |
| 2 | **Market Intelligence** | Researches each idea on the open web — market size, trends, competitors, demand signals, risks — with citations | `output/market-research.md` |
| 3 | **Governance** | Scores every idea on **Desirability, Viability, Feasibility**, ranks them, and gives each a gate decision (Advance / Iterate / Park) | `output/scorecard.md` |
| ★ | **Reporter** *(on demand)* | Packages a finished run into one polished, print-ready HTML summary you save as a PDF (`/report`) | `output/summary.html` |

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

> **Tip:** You can also run any agent on its own, e.g.
> *"Use the ideator subagent to brainstorm around on-device health AI"* — or
> re-run just `governance` after tweaking the scoring weights.

---

## Install globally (use it in any project)

To make the agents available everywhere, copy them into your user scope:

```bash
cp .claude/agents/*.md ~/.claude/agents/
cp .claude/commands/ideate.md ~/.claude/commands/
```

Project-scoped files (`.claude/` in this repo) always take priority over the
global ones when you're inside the project.

---

## How it fits together

```
drumr-ideation-kit/
├── .claude/
│   ├── agents/
│   │   ├── ideator.md              # 1. founder intake + 10 ideas
│   │   ├── market-intelligence.md  # 2. web research per idea
│   │   ├── governance.md           # 3. scoring + ranking + gate
│   │   └── reporter.md             # ★ printable HTML/PDF summary
│   ├── commands/
│   │   ├── ideate.md               # /ideate orchestrator
│   │   └── report.md               # /report — export a PDF summary
│   └── settings.json               # tool permissions
├── templates/                      # the shapes the agents fill
│   ├── founder-profile.md
│   ├── idea.md
│   └── scorecard.md
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
- **Intake questions** — tailor the interview in `.claude/agents/ideator.md`.

---

## Requirements

- [Claude Code](https://code.claude.com) installed and authenticated.
- Web access enabled for the `market-intelligence` agent (it uses `WebSearch`
  and `WebFetch`).

## License

MIT — see [LICENSE](./LICENSE).
