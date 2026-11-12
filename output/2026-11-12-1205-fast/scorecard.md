# Scorecard — run 2026-11-12-1205-fast

> Single-idea run. Scores **IDEA-01 — Avee: expert agents paid by usage** on the
> standard rubric. Weights: **Composite = 0.40×D + 0.35×V + 0.25×F**. Gates:
> Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (thresholds never lowered).
> Evidence base: `market-research.md` (confidence: Medium) and `revenue-model.md`
> (v1 spec, section 7). No `signals.md` exists this run.

## Kill-rule check (thesis.md K1–K7)

Checked **before** scoring. A broken rule forces **Park** regardless of composite.

| Rule | Verdict | Why |
|---|---|---|
| K1 — No sales calls | **Pass** | Self-serve consumer subscription, web checkout, credit card. |
| K2 — Ops automatable solo | **Pass (conditional)** | Payouts/KYC/holds automate via Stripe Connect Express; holds only if expert-advice categories are excluded so no manual moderation queue grows with users. |
| K3 — MVP testable ≤ 4 weeks | **Pass** | Product exists (Avee V2 v0.6.0); only the billing/payout layer is new and is ≤ 4 weeks part-time. |
| K4 — Economics work small | **Pass (only with the cap)** | Gross-margin-positive from the first paying user **only** because the fair-use inference cap + media-on-credits keep cost C < net N; the literal "50% of gross" model goes negative on heavy users (revenue-model §2). |
| K5 — Reachable persona | **At risk → effectively fail** | Founder named **no expert segment** and no privileged access; thesis requires naming a place to find 10 of the persona this week. Idea's own note: "K5 is weak (no persona named)." |
| K6 — Evidenced pain | **FAIL** | No `signals.md`, no first-hand dated customer language, under 50 users, no demand evidence. This breaks K6. |
| K7 — No high-liability space | **At risk** | Expert-advice agents in health/finance/legal give advice as the expert; avoidable only by excluding regulated categories in the wedge. |

**Forcing verdict:** **K6 fails** (no evidenced pain signal this run), and K5 is effectively unmet. Per engine rules this forces **Park — "thesis kill: K6 — no evidenced customer pain signal in this run"**, whatever the composite. K7 is a manageable at-risk; K4 holds only with the cost cap. The idea is still scored below so the bank records why it was parked.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 4 | 5 | 7 | 5.1 | Park |

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 5.1  ·  Gate: Park

**Desirability — 4**
- Pain intensity: 5 — Expert-side pain (answering the same questions, time-for-money) is real; demand-side is a vitamin — paying $20 for a multi-expert bundle is a nice-to-have, not a painkiller.
- Demand evidence: 3 — No signal this run; market research proves WTP for a **specific named expert** (Delphi 7-figure creators, tbpn-digest 2025-06-24), **not** for an all-access bundle (research §2 "disconfirming"). No signals → Desirability capped at 6; it lands well below.
- Willingness to pay: 4 — $20–25 is the ChatGPT-Plus/Claude-Pro price (revenue-model §6); proven for single trusted experts, unproven for a discovery bundle.
- Founder–market resonance: 4 — Technical founder who built the product, but is an observer of these communities with no named expert segment and no privileged supply access (founder-profile: "named no expert segment").

**Viability — 5**
- Market size & growth: 6 — Containing creator economy is large and expanding at double-digit CAGR (~$234–324B for 2026, fungies.io 2026), but the specific AI-expert-agent sub-market is **publicly unsized** (research §1).
- Monetization & unit economics: 6 — Platform side is now rigorous: user-centric net-contribution keeps a structural ~40–45% of gross with the cap (revenue-model §3). Creator side is weak: ~$3–5 per engaged subscriber vs 85–90% keep at Patreon/Substack/Delphi (research §3).
- Defensibility / moat: 4 — Transparent public payout dashboard + cost-efficient routing is genuine whitespace vs GPT Store's opaque analytics (research §4), but the dashboard is copyable; the only durable moat is two-sided liquidity that doesn't yet exist.
- Go-to-market realism: 3 — Two-sided cold start under 50 users with no seeded side and no named persona; community-led growth suits the founder but has no demand evidence to pull on (research §6 risk 2).
- Timing ("why now"): 5 — Tech + payout rails are ready and commoditized, but usage-based AI-creator payouts clearing real money is unproven: GPT Store stayed invite-only and paid most builders $0 two years on (research §7).

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Product already built; the payout layer sits squarely on the founder's core strengths (agents, RAG, cheap routing).
- Capital / resources vs. runway: 7 — Bootstrapped and solo, but the cost cap keeps infra below price, so runway isn't burned by heavy users.
- Time to testable MVP: 8 — Billing/payout layer is ≤ 4 weeks part-time on an existing product.
- External dependencies: 5 — Stripe Connect handles KYC/tax, but DAC7/1099 reporting, chargeback windows, mobile-IAP avoidance, and K7 expert-advice liability add real third-party and regulatory exposure.

**Composite:** `0.40×4 + 0.35×5 + 0.25×7` = **5.1**
**Gate decision:** **Park** — thesis kill: K6 (no evidenced pain signal this run); composite 5.1 is also below the 6.0 Iterate floor. The math is close to bulletproof; the **demand** is unproven.
**Biggest unknown:** Will experts with a trusted audience accept ~$3–5 per engaged subscriber (50/50 of a platform-set $20–25 price) when Patreon/Substack/Delphi let them keep 85–90% of a price they set? That single answer decides whether the supply side ever seeds.
**De-risking step:** Pick **one** named expert niche the founder can reach 10 of this week (satisfies K5), recruit 3–5 to publish agents, and pre-sell the all-access pass to their audiences — capturing first-hand WTP **and** payout-acceptance evidence (satisfies K6) before building anything else.

---

## Revenue model verdict (revenue-model.md §7 v1 spec)

**What holds (genuinely strengthened):**
- **The margin is now structural, not hopeful.** Switching from "50% of gross" to **50% of net contribution P = max(N − C, 0)** fixes the §2 contradiction: the platform keeps half of contribution on every subscriber every month (~40–45% of gross at $20–24.99), instead of its profit depending on user behaviour.
- **The fair-use cost cap + media-on-credits is what makes K4 true.** Without it a single power user on a frontier agent loses $20–90/month (§2 table). With it, gross margin is positive from the first paying user. This is the load-bearing rule — keep it non-negotiable.
- **Fraud resistance is the model's best property and it is evidenced.** User-centric attribution means self-dealing and collusion rings always lose money, corroborated by SoundCloud Fan-Powered Royalties and the user-centric-vs-pool precedent (research §5). Do not switch to a pooled model.
- **Ops stay solo-operable** via Stripe Connect Express, 45-day holds, $25 minimum payout (K2).

**What's still weak:**
- **The math is bulletproof; the demand is not.** §6 admits it: nothing in the spec explains why B pays $20 for a bundle rather than for one trusted expert, and the evidence says WTP is for the single expert (research §2).
- **Supply economics stay structurally unattractive.** ~$3–5 per engaged subscriber vs 85–90% keep elsewhere is the dominant evidenced risk (research §3, §6 risk 1); GPT Store is the cautionary precedent where tiny usage-based payouts drove creators to affiliate/ads.
- **The headline "≥ $5" promise isn't free** — it requires $24.99 pricing or a 60% split (§3); at a round $20 the expert gets ~$3.20–4.50.
- **$25 minimum payout + ~$2/account/month Stripe fees** mean long-tail experts net ~$0 for months, which can sour supply before liquidity builds.

**Single change that would most raise the score:** **Lead supply acquisition with the high-share private-agent / paid-escalation layer (expert keeps ~80%, Patreon-like), and demote the 50/50 all-access pool to passive discovery upside.** This realigns the creator pitch with what the evidence says experts will actually accept, directly attacking the dominant risk (thin payouts) and the cold-start, rather than asking experts to trade an 85–90% product for a ~$3–5 one on day one.

---

## Top recommendation

There is only one idea this run, and it does not clear the gate. **IDEA-01 is Parked**, not on its economics — the revenue model is now close to bulletproof on margin and fraud — but on **unproven demand (K6 fail) and an unnamed, unseeded supply side (K5)**. The highest-priority validation step: choose one named expert niche, recruit 3–5 experts to publish agents, and pre-sell the all-access pass to their audiences to capture first-hand willingness-to-pay and payout-acceptance evidence before building further. Resolving that one unknown is what could move this from Park toward Advance.
