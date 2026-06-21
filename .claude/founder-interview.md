# Founder interview spec

> **Who runs this:** the **orchestrator** (the top-level agent running `/ideate`
> or `/ideate-fast`), never a subagent. Subagents in Claude Code run
> non-interactively and **cannot** use `AskUserQuestion`. The interview must
> happen at the orchestrator level; the `ideator` subagent then generates ideas
> from the profile you produce here.

The goal of this phase is to understand who the founder is, what they know, and
what constraints they operate under, then write `<run-dir>/founder-profile.md`
so the `ideator` can ground every idea in the founder's real edge.

You MUST complete this interview and write the profile **before** invoking the
`ideator` subagent.

## How to run the interview

- Use the `AskUserQuestion` tool for every single round — **never** ask
  questions as plain text. If you find yourself typing a numbered list of
  questions, stop and use the tool instead.
- **Every question MUST include 3–4 concrete, selectable answer options** that
  you generate and tailor to the founder's domain. The tool always adds an
  "Other" free-text escape automatically, so the founder can type a custom
  answer, but your job is to do the thinking and offer real choices.
- **Use multi-select** wherever more than one answer is naturally true (hard
  skills, GTM motions, anti-goals, what energizes them). Use single-select for
  mutually-exclusive questions (solo vs. team, lifestyle vs. venture).
- Run exactly **5 rounds**. Each round is **one `AskUserQuestion` call
  containing its 3 questions** (the tool supports up to 4 questions per call).
  That is 5 tool calls total, one per round.
- **Tailor every question AND its options to the domain or prompt the user
  gave you.** Generic options produce generic profiles.
- After each round's answers come back, briefly acknowledge them in one
  sentence before firing the next round.
- If an answer is vague — especially on unfair advantage, customer access, or
  runway — ask one follow-up `AskUserQuestion` probe before continuing.

### Check for an existing profile first

Before starting, try to read `<run-dir>/founder-profile.md`. If it exists and
is complete, confirm the key facts with the user in one message and skip
straight to writing/confirming the profile. Otherwise, run the 5 rounds below.

#### Example of a well-formed question

For a founder exploring B2B SaaS, Round 1 Q1 ("Team") should be sent via
`AskUserQuestion` roughly like:

- **Question:** "Who is building this, and at what commitment level?"
- **Options:** `Solo, full-time` · `Solo, alongside a job` · `Co-founders, full-time` · `Co-founders, part-time`
- **Multi-select:** off (single choice)

And Round 3 Q3 ("Hard skills & gaps") should offer multi-select options like
`Engineering / build` · `Design / UX` · `Sales / GTM` · `Domain / research`.

## Round 1 — Who you are

1. **Team** — Who is building this? Solo or co-founders? Full-time or alongside a job? What does each person bring?
2. **Background in this space** — Professional background relevant to [domain]? How many years, in what roles?
3. **Track record** — What have you built, shipped, sold, or led before that is relevant here?

## Round 2 — Problem proximity

1. **First-hand exposure** — Have you personally experienced the problem — as a user, operator, buyer, or expert? Describe a specific moment or workflow.
2. **Customer access** — Do you already know potential customers in [domain]? How would you reach your first 10 — warm intros, community, inbound, outbound, partnerships?
3. **Prior exploration** — Have you already tried ideas or side projects in this space? What did you learn, including what you would not repeat?

## Round 3 — Your edge

1. **Unfair advantage** — Given your background in [domain/role], what do you know, have access to, or can do that most people trying this would not?
2. **Deepest skill** — The single thing you are genuinely better at than most people, and how it applies to [domain]?
3. **Hard skills & gaps** — What can you personally build or do today? What would you need to hire, partner, or outsource to ship an MVP?

If the unfair-advantage answer is vague (e.g. "I have a lot of connections"),
probe once: "Can you be more specific — who are those connections, and why
would they give you an edge here?"

## Round 4 — Motivation & direction

1. **Motivation** — The specific change you want to see in [domain], and why it matters to you personally?
2. **Themes & energy** — What kinds of problems or business types energize you, and what drains you?
3. **Success definition** — What does a win look like in 12–24 months? What would make you stop or pivot?

## Round 5 — Constraints and anti-goals

1. **Resources & risk** — Capital and runway available today? Lifestyle business, venture scale, or in between?
2. **Hard constraints** — Geography, regulatory comfort, time horizon for traction, anything else that rules out certain businesses?
3. **Anti-goals & GTM comfort** — What business models, industries, or working styles do you explicitly NOT want? Which go-to-market motions are you willing to run yourself?

## Write the profile

Once all 5 rounds are complete, write `<run-dir>/founder-profile.md` using the
structure in `templates/founder-profile.md`. Then confirm to the user in one
sentence before handing off to the `ideator`.

> **Fast variant:** for `/ideate-fast`, you may compress to **3 rounds** —
> merge Rounds 1–2 (who you are + problem proximity), keep Round 3 (your edge),
> and merge Rounds 4–5 (motivation + constraints) — still one `AskUserQuestion`
> call per round.
