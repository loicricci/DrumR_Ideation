# Solo-founder thesis

> The hard filter for `/engine`. Every idea is checked against the kill rules
> **before** it is researched, and again by governance before scoring. An idea
> that breaks any kill rule is parked, whatever its score. Edit this file to
> change what the engine looks for; the agents read it on every run.

## Goal
Find ideas worth pushing to Problem–Solution Fit that **one person can build,
run and grow with minimal resources**, and that can scale without a team.

Target: **10 ideas handed off to P/S Fitter** (tracked in `ideas-bank.md`).

## Allowed business shapes
- **Self-serve consumer** apps and subscriptions.
- **Self-serve prosumer / small-business** tools bought with a credit card,
  no sales call (creators, freelancers, indie devs, small shops).
- Marketplaces only if one side can be seeded by the founder alone.

## Kill rules (any one → Park; K5 and K6 are retired as kills)
- **K1 — No sales calls.** The buyer can discover, try and pay without talking
  to anyone. No enterprise or procurement-led sales.
- **K2 — Ops automatable by one person.** No manual moderation queue, no
  human-in-the-loop fulfilment, no support load that grows linearly with users.
- **K3 — MVP testable in ≤ 4 weeks** of part-time work by the founder.
- **K4 — Economics work small.** Gross margin positive from the first paying
  user; the per-user infra cost is below the price at small scale.
- **K5 — (moved to the gate).** Reachability is measured as founder–target
  distance (G2 in governance), not as a kill rule. Almost anyone is reachable.
- **K6 — (no longer a kill rule).** Missing evidence at the idea stage means
  **unknown, to be tested**, not "bad". Evidence status is recorded as a flag
  (see below) and feeds the scores, but never parks an idea on its own.
- **K7 — No licence-gated or high-liability space** (gambling, regulated
  finance/health advice, defamation-prone content) unless the risk is
  structurally removed in the wedge.

## Evidence flag (recorded, never a kill)
- **Direct:** first-hand, dated customer language or payments for this job.
- **Indirect:** funded or revenue-making competitors, adjacent products people
  pay for, platform shifts. A competitor that raised serious money is strong
  indirect evidence that the market is real.
- **Unknown:** nothing found yet. That's a question for P/S Fit, not a verdict.

## Preferences (raise scores, never override kill rules)
- Leans on the founder's edge: agent/LLM systems, cheap infra, agent design.
- Has a built-in growth loop (sharing, output that carries the brand, SEO).
- Recurring revenue.
- Pain the persona already pays to solve badly (switching beats creation).
