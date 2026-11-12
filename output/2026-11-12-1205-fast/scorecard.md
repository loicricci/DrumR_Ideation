# Scorecard — run 2026-11-12-1205-fast (v4, re-scored under the revised evidence rules)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage**
> **from scratch** under two newly-tightened governance rules plus a thesis
> change. The evidence base is identical to v3 (same `signals.md`, same
> `market-research.md`, same `revenue-model.md`); what changed is how the rules
> tell me to read that evidence.
>
> **Governance advises; the founder decides.** The ranking and the checklist are
> reasons to learn from, not a verdict on what may be pursued. The gate line is
> an **advisory Recommendation**, and each card closes with a **For the founder**
> note on why it ranks where it does and what evidence would move it.
>
> **What changed since v3**
> 1. **"Absence of evidence is not evidence of absence."** A criterion with no
>    evidence either way is scored at the **neutral midpoint 5** and flagged
>    "unknown, test in P/S Fit". A score **below 5 needs cited disconfirming
>    evidence**. So the "publicly unsized sub-market" and "payout acceptance is
>    unproven" are **unknowns** — they no longer drag a score below neutral; they
>    are logged as the biggest unknown instead.
> 2. **"Indirect evidence counts."** A competitor that raised serious funding or
>    earns real revenue in the same job is **strong indirect evidence** that the
>    market and demand are real, and can justify **up to 7** on Demand evidence,
>    Willingness to pay and Market size **on its own**. Differences between the
>    competitor's model and Avee (AI-vs-human delivery, single-expert-vs-bundle)
>    are a question for **Defensibility** and the **biggest unknown** — **not** a
>    reason to discount the market signal. Here that indirect evidence is
>    **Delphi's $16M Sequoia Series A (~$18.7M total, verified SIG-09)** and
>    **JustAnswer's paid, credential-gated expert-answer market (SIG-16)**.
> 3. **Thesis K5 and K6 retired as kill rules.** K5 (reachability) is now the
>    gate's G2 distance; K6 (missing evidence) is now an **evidence flag**
>    (Direct / Indirect / Unknown), recorded but never a kill. Neither can park
>    an idea anymore.
>
> **The headline:** the idea score rises **6.25 → 6.65**, entirely rule-driven.
> Delphi's Sequoia round and JustAnswer's credential-gated market now count as
> strong indirect evidence (Demand 6→7, WTP 6→7, Market size 6→7), capped at the
> rule's ceiling of 7 by the **genuine** disconfirming signals (SIG-05 generic
> clone, SIG-10 experts refuse, SIG-11 audiences distrust clones), which are
> weighed as real evidence, not absence. The AI-delivery and bundle-vs-single
> model differences moved to **Defensibility** and the **biggest unknown**, where
> the rule puts them. The advisory Recommendation is still **Iterate**, driven by
> **G4 alone (6.65 < 7.5)**: G1 passes, G2 distance is **2 (Cold but mapped)**
> which does not block Advance, and the ≤4-week cold-outreach test is runnable at
> that distance. **Thresholds were not lowered.**
>
> Corrected creator payout used throughout (one-to-one own-audience usage,
> revenue-model §3): **~$7.96 at $20 (40% of price), ~$9.55 with the 10% referral
> bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)**. The old "~$3–5" applies **only**
> to incidental cross-traffic from other experts' subscribers — extra upside, not
> the core case.
>
> Weights: **Composite = 0.40×D + 0.35×V + 0.25×F** (CLAUDE.md default). Gate
> bands (advisory): Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (thresholds never
> lowered). Evidence base: `signals.md` (18 signals), `market-research.md`
> (confidence: **Medium**), `revenue-model.md` (v1 spec §7). The "Deliverables"
> bullet has **no external evidence** — under rule 1 its effects are **unknown
> (neutral)**, not a penalty, and are labelled **inference** wherever cited.

## Evidence flag (thesis.md, recorded — never a kill)

- **Direct:** first-hand, dated, fetched-verbatim **pain** on the supply side —
  SIG-01 (Ken Deng, DEV, Mar 6, "I'd run out of time"; "a waitlist of 20+ …
  adding even one more would break me"), SIG-02 (Josh Spector).
- **Indirect (strong):** **Delphi $16M Sequoia Series A, ~$18.7M total**
  (SIG-09, verified) — a funded incumbent on exactly the AI-expert-clone premise;
  **JustAnswer** credential-gated recurring paid Q&A at ~$46–55/mo (SIG-16);
  **Intro** four-figure WTP for a specific named expert (SIG-03). Per rule 2 these
  justify up to 7 on Demand, WTP and Market size on their own.
- **Unknown (to test in P/S Fit, not a penalty):** recurring WTP for an **AI**
  agent of a credentialed expert (vs the human); whether credentialed experts
  **accept** a ~40–48% usage share over keeping ~85–90% of a self-set price; the
  deliverables premium over Gamma/Beautiful.ai.
- **Genuine disconfirming (real evidence, weighed honestly):** SIG-05 (clone
  "sounds just like a normal chatgpt chat"), SIG-10 (respected experts refuse to
  clone), SIG-11 (audiences distrust clones — "it feels fake / I want the real
  person"). These cap Demand/WTP at the rule's 7 ceiling rather than above it.

## Kill-rule check (thesis.md K1–K7) — feeds gate check G1

Checked **before** scoring. A broken rule forces **Park** (G1 fail) regardless
of composite. **K5 and K6 are retired as kills** (see thesis.md): K5 is now the
gate's G2 distance, K6 is the evidence flag above.

| Rule | Verdict | Why |
|---|---|---|
| K1 — No sales calls | **Pass** | Self-serve consumer subscription, web checkout, credit card. |
| K2 — Ops automatable solo | **Pass (conditional)** | Payouts/KYC/holds automate via Stripe Connect Express. Conditional: credential verification must stay **automated** (Europass digital credentials, work-email domain, LinkedIn); a manual review queue would grow with supply and break K2. The founder names automated verification as the core build, so this holds *by design*, at build risk. |
| K3 — MVP testable ≤ 4 weeks | **Pass** | Product exists (Avee V2 v0.6.0), incl. image/video/voice for deliverables. A demand-test MVP (3–5 experts with lightweight credential checks, pre-sell their audiences) is ≤ 4 weeks. Full automated credential verification is a later scale build, not an MVP blocker. |
| K4 — Economics work small | **Pass (only with the cap)** | Gross-margin-positive from the first paying user **only** because the fair-use inference cap + media-on-credits keep cost C < net N; the literal "50% of gross" model goes negative on heavy users (revenue-model §2). Deliverables run on credits (cost × 2), keeping K4 intact if generation is metered. |
| K5 — *(retired as a kill)* | **n/a — now G2** | Reachability is no longer a kill. It is measured as founder–target **distance** in the gate (G2 below = 2, Cold but mapped). |
| K6 — *(retired as a kill)* | **n/a — evidence flag** | Missing evidence is "unknown, to be tested", not "bad". Recorded in the evidence flag above (Direct pain + strong Indirect demand; the AI-delivery/payout-acceptance leaps are Unknown). Never parks the idea. |
| K7 — No high-liability space | **Pass (conditional, at-risk)** | Expert-advice agents in health/finance/legal give advice *as the expert*; the credential-first angle *raises* K7 stakes (a falsely verified "Harvard-trained" badge is itself a liability; a deck sold "from a VC" must be framed as *built with that expert's agent*). Structurally removable in the wedge: exclude regulated categories, verify conservatively, label AI deliverables honestly. Manageable, not forcing. |

**Forcing verdict:** **No kill rule fires** → **G1 passes**. K2/K7 are conditional
on automated, conservative credential verification and honest deliverable framing.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate | Distance |
|---|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 7 | 6 | 7 | 6.65 | Iterate | 2 |

*The "Gate" column is the advisory **Recommendation**, not a verdict — the
founder decides.*

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 6.65  ·  Recommendation: Iterate

> The composite is the **idea score**, used for ranking only. The recommendation
> is advisory — the founder decides. Missing traction never lowers a score.

**Desirability — 7**
- Pain intensity: 7 — Painkiller-grade evidence on both sides: the capacity-capped expert turning away paying demand (SIG-01, strong, verbatim — "I had a waitlist of 20+ … adding even one more would break me") and recurring WTP for *credential-gated* answers (SIG-16, JustAnswer ~$46–55/mo). Held at 7, not higher, because the AI-substitution objection (SIG-11 "it feels fake / I want the real person"; SIG-05 "sounds just like a normal chatgpt chat") shows the *human* is the proven painkiller and the AI agent inherits only part of that intensity — a genuine disconfirmer, not absence.
- Demand evidence: 7 — **Raised under rule 2 (indirect evidence counts).** Delphi's **$16M Sequoia Series A (~$18.7M total, verified SIG-09)** is a funded incumbent built on exactly the AI-expert-clone premise, and **JustAnswer** (SIG-16, strong) proves a real credential-gated paid-answer market; adjacent WTP for a *specific named expert* is strong (SIG-03 — Intro $776–$5k, Nikita Bier $122.3k/95 bookings; SIG-12). Per the rule these justify up to 7 on their own, and the bundle-vs-single-expert and AI-vs-human **model differences are routed to Defensibility and the biggest unknown, not used to discount the market signal**. Held **at** the 7 ceiling (not above) by the genuine disconfirmers SIG-05 (generic clone), SIG-10 (experts refuse to clone), SIG-11 (audiences distrust clones) — weighed as real evidence. Deliverables have no external demand evidence (unknown/inference only, not a penalty).
- Willingness to pay: 7 — **Raised under rule 2.** JustAnswer proves durable **recurring** WTP for credential-gated answers at ~$46–55/mo — *above* Avee's $20–25 price (SIG-16, strong); Intro proves four-figure WTP for a specific expert (SIG-03, strong). These are strong indirect evidence that the price point is payable (justifies up to 7). The human-vs-AI delivery difference is a **model difference → biggest unknown**, not a discount. Held at the 7 ceiling by SIG-05/SIG-11 (negative WTP for a generic AI stand-in). The "Deliverables" premium over Gamma/Beautiful.ai is **unknown (inference)**, scored neither up nor down.

*Desirability average: (7+7+7)/3 = 7.0 → **7**.*

**Viability — 6**
- Market size & growth: 7 — **Raised under rule 2.** Containing creator economy is large and growing (~$234–324B 2026, double-digit CAGR, research §1). The specific AI-expert-agent sub-market is **publicly unsized** (research §1; SIG "found nothing") — under rule 1 that is an **unknown (neutral), not a drag**. The funded incumbent (Delphi, SIG-09) and the proven credential-gated market (JustAnswer, SIG-16) are strong indirect evidence the market is real, justifying up to 7. Held at 7 (not higher) precisely because the sub-market is genuinely unsized.
- Monetization & unit economics: 7 — Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** (revenue-model §3), not the ~$3–5 the superseded bundle framing implied. The platform keeps a structural ~40–45% of gross with the cap. The "central competitive headwind" (market-research §3) is materially weaker: for *small / audience-less* experts Avee clearly beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06); for own-audience experts ~40–48% of a platform-set price with inference, agent and deliverables included is defensible. Held below 8 because experts who can set and collect their *own* price on Delphi (~85%) / Patreon (~90%) still keep more per subscriber at scale — a real comparative fact (research §3). Payout acceptance is an **unknown** logged below, not a drag here.
- Defensibility / moat: 5 — **The home of the model-difference question (rule 2).** Pro-moat: automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard and attacks documented Delphi gaps (no structured credentials, SIG-13; no EU/GDPR posture, SIG-14); the fraud-resistant user-centric payout architecture is validated (SoundCloud Fan-Powered Royalties, research §5). Anti-moat: Delphi is Sequoia-funded and could add a credential layer; multi-owner "compare a VC's vs a founder's vs a designer's deck" is a genuine Delphi gap but the deliverable itself sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment, not the renderer. Genuinely two-sided → neutral **5**.
- Distribution path: 6 — Judged on channel plausibility, never traction or warm access. A reachable, low-CAC channel exists: the **expert-led sharing loop** — each expert shares their own agent with their own audience, with a direct financial interest and a 10% referral bonus (revenue-model §4) — a built-in growth loop (thesis preference), and the communities are nameable (r/coaching, r/consulting, Intro, MentorCruise, creator comment threads — SIG-01/03/18). Held at 6, not higher, because (a) two-sided liquidity makes the *first* cohort hard to seed, and (b) GPT Store is **genuine disconfirming evidence** that usage-based AI-payout platforms struggle to pull long-tail supply (research §7) and conversion is uncertain while the AI-delivery question is open (SIG-05/11).
- Timing ("why now"): 6 — The competitive whitespace is open *now*: Delphi raised $16M but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Enabling tech (RAG + memory + cheap routing) and payout rails (Stripe Connect) are commoditized. Counterweight (genuine): GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

*Viability average: (7+7+5+6+6)/5 = 6.2 → **6**. (Market size rose 6→7 under rule 2; the average still rounds to 6.)*

**Feasibility — 7** *(judged intrinsically for a small technical team, not against this founder's runway)*
- Technical complexity: 7 — A modern RAG/memory/multi-model agent platform with a usage-attribution payout layer is well within a small technical team's reach; the comparable product (Avee V2 v0.6.0, incl. image/video/voice generation) already exists as proof the stack is tractable. The novel hard part is **automated credential/employment verification**, which is load-bearing and partly outside standard agent work — that keeps this below 8.
- Capital intensity: 7 — Intrinsically capital-light: software on cheap, routed inference, commoditized Stripe Connect rails, no hardware/inventory. The fair-use cost cap + media-on-credits keep per-user cost below price so heavy use doesn't invert margin (revenue-model §3). Third-party credential/identity verification and metered inference are the only real recurring costs.
- Time to testable MVP: 7 — The product exists; the billing/payout layer is a bounded build and demand is testable with lightweight/manual verification of a handful of experts — a matter of weeks, not months, intrinsically.
- External dependencies: 5 — The genuine drag: Stripe Connect (KYC, DAC7/1099, chargebacks, 45-day holds), mobile-IAP avoidance (sell on web), credential-verification dependencies (Europass, LinkedIn/work-email, employer policy for current employees), and K7 expert-advice **plus** deliverable-attribution liability. Several are outside the team's control — neutral 5.

*Feasibility average: (7+7+7+5)/4 = 6.5 → **7**.*

**Composite (idea score):** `0.40×7 + 0.35×6 + 0.25×7` = **6.65**

**Gate checklist**
- G1 — Thesis (no kill rule fires): **Pass** — no K1–K7 fires (table above); K5/K6 are retired as kills. K2/K7 conditional on automated, conservative verification and honest deliverable framing.
- G2 — Founder–target distance: **2 — Cold but mapped** — the founder is not the persona and has no warm network in it (founder-profile: AI/agent-dev and indie-hacker communities; "named no expert segment and no privileged access"), but the persona gathers in **known, open public channels** (r/consulting, r/coaching, r/freelance, Skool, Intro, MentorCruise — SIG-01/03/18). Not distance 1, because credentialed professionals and expert-followers are not the founder's own indie-hacker/dev crowd; not distance 3, because the channels are public and gated by no gatekeeper. Route to the first 10: cold outreach into one named niche (e.g. independent consultants in r/consulting) over 4 weeks. Distance 2 does **not** block Advance, and the G3 test is runnable via exactly this cold-outreach plan within 4 weeks.
- G3 — Riskiest assumption testable in ≤ 4 weeks: **Pass** — riskiest assumption = *will an expert's own audience pay $20–25/mo for that expert's AI agent (not the human), and will a credentialed expert publish one for ~$7.96–9.55/engaged sub rather than keep ~85–90% of a self-set price elsewhere?* Testable on the existing product in ≤ 4 weeks at distance 2: cold-recruit 3–5 credentialed experts from one niche, publish credential-fronted agents with one paid deliverable, pre-sell their audiences on the one-to-one subscription.
- G4 — Idea strength (≥ 7.5 Advance, < 6.0 Park): **6.65** — Iterate band (neither Advance nor Park). **This is the single deciding check.**

**Recommendation (advisory; the founder decides):** **Iterate** — G1 passes, G2 distance is 2 (≤ 2, does not block), G3 passes and its test is runnable at distance 2; the **only** thing short of the Advance band is **G4 (composite 6.65 < 7.5)**. The composite is ≥ 6.0 and no kill rule fires, so it does not sit in the Park band. The one move that would lift it into the Advance band is to run the G3 experiment and convert the AI-delivery and payout-acceptance unknowns from untested into evidenced demand.
**Biggest unknown:** Will an expert's own audience pay a recurring subscription for that expert's **AI agent** (or an AI-made deck in their style), not the human — and will credentialed experts accept **~$7.96–9.55 per engaged subscriber** (40–48% of a platform-set price) over keeping ~85–90% of a self-set price elsewhere? The strong indirect evidence (Delphi Sequoia round, JustAnswer, Intro) shows the market and the price are real; these two AI-delivery/payout-acceptance leaps are the model differences the rule routes here, and SIG-05/SIG-11 actively disconfirm the AI-substitution half.
**De-risking step:** Pick one named credentialed niche the founder can cold-reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18 — the distance-2 route), recruit 3–5 to publish credential-fronted agents with one paid deliverable, and pre-sell their existing audiences the one-to-one subscription. This single test captures both halves of the biggest unknown (audience WTP for AI delivery **and** expert payout acceptance) and demonstrates the distance-2 cold-outreach route works.
**For the founder:** This is the only idea in the run, so it has no neighbours to rank against; it lands mid-band (6.65) rather than high because the evidence is strongest on the two things *adjacent* products prove — that people pay real, recurring money to reach a trusted expert (Intro, JustAnswer) and that investors back AI-clone-of-an-expert as a category (Delphi's Sequoia round) — and weakest on the two leaps this specific product needs: that an audience will pay for the *AI* rather than the human (SIG-05/11 push back), and that credentialed experts will accept a ~40–48% usage share when Delphi/Patreon let them keep ~85–90% of a price they set. **What would move it up:** a pre-sell test where real subscribers pay for an expert's AI agent and ≥3 credentialed experts opt in at the usage-share terms (that alone could carry Demand/WTP past 7 and the composite toward the Advance band); evidence the deliverables command a premium over Gamma/Beautiful.ai; a signal that experts prefer usage-share to a self-set price. **What would move it down:** a pre-sell that converts no AI-delivery subscribers, credentialed experts declining the share in favour of self-set-price platforms, or credential verification proving un-automatable at acceptable accuracy (which would also threaten K2/K7).

---

## Changes vs previous scorecards (v1: 5.1 Park → v2: 5.9 Park → v2.1: 6.25 Iterate → v3: 6.25 Iterate → **v4: 6.65 Iterate**)

The idea score rises **6.25 → 6.65**. **No evidence changed since v3** — same
signals, same research, same corrected payout. Every rise is **[rule]**, driven
by the two new evidence rules (indirect evidence counts; absence is not evidence
of absence) and the retirement of K5/K6 as kills. The genuine disconfirmers
(SIG-05/10/11), now weighed as real evidence, are what **cap** the raised
sub-scores at the rule's ceiling of 7 — an **[evidence]** brake, not a lift.

| Dimension | v3 | v4 | What moved and why |
|---|---|---|---|
| Desirability | 6 (Pain 7, Demand 6, WTP 6) | **7** (Pain 7, Demand 7, WTP 7) | **[rule]** Demand 6→7 and WTP 6→7: under "indirect evidence counts", Delphi's $16M Sequoia round (SIG-09) and JustAnswer's credential-gated recurring market (SIG-16) justify up to 7 on their own, and the AI-vs-human / bundle-vs-single **model differences moved to Defensibility and the biggest unknown** instead of discounting the market signal. **[evidence]** Held exactly at the 7 ceiling (not above) by the genuine disconfirmers SIG-05/10/11. Average 6.33 → 7.0. |
| Viability | 6 (Market 6, Monet. 7, Moat 5, Distribution 6, Timing 6) | **6** (Market **7**, Monet. 7, Moat 5, Distribution 6, Timing 6) | **[rule]** Market size 6→7: the funded incumbent + proven credential-gated market are strong indirect evidence, and the "publicly unsized sub-market" is now an **unknown (neutral)**, not a drag (rule 1). Moat held at neutral 5 as the designated home of the model-difference question. Average 5.6→6.2; still rounds to **6**. |
| Feasibility | 7 (intrinsic) | **7** (intrinsic) | Unchanged. Sub-scores 7/7/7/5 → 6.5 → 7. No rule touched this dimension. |
| Composite | 6.25 | **6.65** | **[rule]** Desirability 6→7 (0.40 weight) lifts the idea score by 0.40; Viability and Feasibility round unchanged. Net 6.25 → 6.65 — a measure of the *idea on the evidence*, risen only because the rules now let strong indirect evidence count. |
| Recommendation basis | Checklist G1–G4; Iterate via G4 (6.25<7.5) | **Advisory; checklist G1–G4; Iterate via G4 (6.65<7.5)** | **[rule]** K5/K6 retired as kills (now G2 distance + evidence flag), so G1 rests only on K1–K4, K7 — all pass. The gate is now an **advisory Recommendation** (the founder decides), not a verdict. Same band (**Iterate**); the only thing short of Advance is still **G4**, now at 6.65. Thresholds unchanged. |

**Honest note on not inflating:** v4 does **not** claim the AI-delivery demand
leap or payout acceptance are now proven — SIG-05/SIG-11 still disconfirm the
former and no signal evidences the latter, which is why the sub-scores stop at
the rule's **7 ceiling** and the composite stays well under the 7.5 Advance band.
The rise from 6.25 to 6.65 is only the correct accounting of strong indirect
evidence (a Sequoia-backed incumbent and a proven credential-gated paid market)
that the old rules under-counted. The practical read (Iterate, run the one
pre-sell test) is unchanged.

---

## Revenue model verdict (revenue-model.md §7 v1 spec) — unchanged, retained

**What holds (strong):**
- **The margin is structural, not hopeful.** 50% of net contribution P = max(N − C, 0) keeps the platform at ~40–45% of gross on every subscriber (§3), fixing the §2 contradiction where paying creators out of *gross* goes negative on heavy users.
- **The fair-use cost cap + media-on-credits is what makes K4 true** and absorbs the deliverables cost (decks/images on credits, cost × 2). Keep it non-negotiable.
- **Fraud resistance is the model's best property and it is evidenced** — user-centric attribution makes self-dealing and collusion lose money (SoundCloud Fan-Powered Royalties, research §5). Do not switch to a pooled model.
- **Ops stay solo-operable** via Stripe Connect Express, 45-day holds, $25 minimum payout (K2) — conditional on credential verification staying automated.

**The corrected creator economics (the material fact carried forward):**
- Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** — not ~$3–5. The ~$3–5 band applies **only** to cross-traffic from other experts' subscribers (extra upside, not the core case).
- **The "≥ $5" promise is met at a plain $20** at ~100% own-audience usage; the earlier "needs $24.99 or a 60% split" caveat was an artefact of the superseded 50%-usage bundle math. Drop it.
- **The "central competitive headwind" is materially weaker.** Avee still pays less per sub than *self-set-price* alternatives for big experts (~85–90%), but beats Delphi outright for small/audience-less experts (Delphi is a $79–299/mo cost with no built-in monetization, SIG-06), and ~40–48% of a platform-set price with inference, agent and deliverables included is a defensible offer.

**What is still weak (evidence confirms, not relieves):**
- **The AI-delivery demand leap is unproven** — SIG-05 and SIG-11 are active disconfirmers; the deliverables premium over Gamma/Beautiful.ai is inference-only.
- **Payout acceptance is unproven** — no signal shows experts choosing a ~40–48% usage share over keeping ~85–90% of a self-set price; this is the dominant open question on the supply side (an **unknown** under the new rules, logged as the biggest unknown rather than scored below neutral).
- **Long-tail payout friction** — $25 minimum + ~$2/account/month Stripe fees mean audience-less experts net ~$0 until discovery traffic exists (the SIG-18 cold-start problem).

**Single change that would most raise the score:** Lead the creator pitch with the
corrected own-audience economics (**~$8–9.55/engaged sub at $20, no monthly fee,
infra + deliverables included**) plus the small-expert wedge where Avee beats
Delphi (SIG-06), and a high-share private-agent / paid-escalation / paid-deliverable
layer (expert keeps ~80%). That frames the offer accurately and attacks the real
open risk — payout *acceptance*, not payout *size*.

---

## Top recommendation

There is one idea this run. **IDEA-01 is Iterate (advisory) at composite 6.65**
(idea score, for ranking only). Under the revised rules the score rose from 6.25
because a Sequoia-backed incumbent (Delphi, SIG-09) and a proven credential-gated
paid market (JustAnswer, SIG-16) now count as the strong indirect evidence they
are — lifting Demand, WTP and Market size to the rule's 7 ceiling, where the
genuine disconfirmers (SIG-05/10/11) honestly hold them. **G1** passes (K5/K6
retired; no kill fires), **G2** reads distance **2 (Cold but mapped)** which does
not block Advance, and **G3** passes with a test runnable at that distance — so the
only thing short of the Advance band is **G4, the idea's own strength (6.65 <
7.5)**. The most useful next move lifts the idea on evidence, not on reachability.

**Highest-priority validation step:** commit to **one** named credentialed niche
and cold-reach 10 of the persona this week (e.g. independent consultants in
r/consulting, SIG-18 — the distance-2 route), recruit **3–5 experts** to publish
credential-fronted agents with one paid deliverable, and **pre-sell their existing
audiences** the one-to-one $20–25 subscription. One test resolves the deciding
unknowns at once — it shows whether an audience pays for AI delivery and whether
experts accept the ~$7.96–9.55/engaged-sub payout, which is exactly what would
carry G4 into the Advance band. A positive result points toward Advance; a
negative one toward Park. The founder decides what to do with that read.
