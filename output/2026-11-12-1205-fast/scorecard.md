# Scorecard — run 2026-11-12-1205-fast (v3, re-scored under the new rules)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage**
> **from scratch** under the revised governance rules. Several rules changed how
> this idea is judged; the change is structural rather than numeric:
>
> 1. **The composite is now an idea score for ranking only.** It answers "how
>    good is the idea on the evidence," not "should this founder ship it now."
>    The gate is decided separately by an explicit checklist **G1–G4**.
> 2. **Founder–market resonance was removed from Desirability.** Desirability is
>    now Pain / Demand / WTP only. Founder fit no longer drags the idea score —
>    it lives in the gate as **G2**.
> 3. **"Go-to-market realism" became "Distribution path."** It judges whether a
>    reachable channel to the first buyers exists and whether the acquisition
>    cost is plausible — **never current traction, never the founder's warm
>    access**.
> 4. **Feasibility is judged intrinsically** (technical complexity, capital
>    intensity, time to MVP, external dependencies) for a small technical team,
>    **not against this founder's runway**.
> 5. **Missing traction is never penalized** anywhere (under-50-users, pre-launch,
>    no revenue are the normal state of an idea).
> 6. **G2 is a founder–target distance 0–3**, not a yes/no reach test: 0 Inside,
>    1 Adjacent, 2 Cold but mapped, 3 Far. Distance 3 blocks Advance; 0–2 does
>    not, provided the G3 test is runnable at that distance. The ranked table
>    carries a **Distance** column.
>
> **The headline:** the composite lands at **6.25** again, but for cleaner
> reasons. The founder-fit penalty that used to sit inside the idea score
> (resonance 4, GTM 4) has moved to the gate, where it belongs; the idea score
> rose on Distribution (4→6) and absorbed the removal of the low resonance
> sub-score, netting back to the same number. **No evidence changed since v2.1** —
> same `signals.md`, same `market-research.md`, same corrected payout. The gate
> is **Iterate**, now decided by **G4 alone (6.25 < 7.5)**: G2 distance is **2
> (Cold but mapped)**, which does *not* block Advance, and the ≤4-week cold-outreach
> test is runnable at that distance.
>
> Corrected creator payout used throughout (one-to-one own-audience usage,
> revenue-model §3): **~$7.96 at $20 (40% of price), ~$9.55 with the 10% referral
> bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)**. The old "~$3–5" applies **only**
> to incidental cross-traffic from other experts' subscribers — extra upside, not
> the core case.
>
> Weights: **Composite = 0.40×D + 0.35×V + 0.25×F** (CLAUDE.md default). Gates:
> Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (thresholds never lowered). Evidence
> base: `signals.md` (18 signals), `market-research.md` (confidence: **Medium**),
> `revenue-model.md` (v1 spec §7). The "Deliverables" bullet has **no external
> evidence**, so every effect from it is labelled **inference**.

## Kill-rule check (thesis.md K1–K7) — feeds gate check G1

Checked **before** scoring. A broken rule forces **Park** (G1 fail) regardless
of composite.

| Rule | Verdict | Why |
|---|---|---|
| K1 — No sales calls | **Pass** | Self-serve consumer subscription, web checkout, credit card. |
| K2 — Ops automatable solo | **Pass (conditional)** | Payouts/KYC/holds automate via Stripe Connect Express. Conditional: credential verification must stay **automated** (Europass digital credentials, work-email domain, LinkedIn); a manual review queue would grow with supply and break K2. The founder names automated verification as the core build, so this holds *by design*, at build risk. |
| K3 — MVP testable ≤ 4 weeks | **Pass** | Product exists (Avee V2 v0.6.0), incl. image/video/voice for deliverables. A demand-test MVP (3–5 experts with lightweight credential checks, pre-sell their audiences) is ≤ 4 weeks. Full automated credential verification is a later scale build, not an MVP blocker. |
| K4 — Economics work small | **Pass (only with the cap)** | Gross-margin-positive from the first paying user **only** because the fair-use inference cap + media-on-credits keep cost C < net N; the literal "50% of gross" model goes negative on heavy users (revenue-model §2). Deliverables run on credits (cost × 2), keeping K4 intact if generation is metered. |
| K5 — Reachable persona | **Pass (weak)** | The credential-first reframe names a reachable persona — credentialed professionals who want to monetize without an audience (SIG-18: r/consulting, r/freelance, Skool) — and the demand side is findable (SIG-03/04: Intro, MentorCruise, creator comment threads). Places exist; *how far* the founder is from them is the **gate (G2 distance)** question, not a kill rule. |
| K6 — Evidenced pain | **Pass** | `signals.md` carries first-hand, dated, fetched-verbatim pain: SIG-01 (Ken Deng, DEV, Mar 6 — "I'd run out of time"), SIG-02 (Josh Spector), SIG-05/06 (Delphi Trustpilot + help-center), SIG-16 (JustAnswer credential-gated recurring ~$46–55/mo). Comfortably met. |
| K7 — No high-liability space | **Pass (conditional, at-risk)** | Expert-advice agents in health/finance/legal give advice *as the expert*; the credential-first angle *raises* K7 stakes (a falsely verified "Harvard-trained" badge is itself a liability; a deck sold "from a VC" must be framed as *built with that expert's agent*). Structurally removable in the wedge: exclude regulated categories, verify conservatively, label AI deliverables honestly. Manageable, not forcing. |

**Forcing verdict:** **No kill rule fires** → **G1 passes**. K2/K7 are conditional
on automated, conservative credential verification and honest deliverable framing.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate | Distance |
|---|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 6 | 6 | 7 | 6.25 | Iterate | 2 |

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 6.25  ·  Gate: Iterate

> The composite is the **idea score**, used for ranking only. The gate comes from
> the checklist below. Missing traction never lowers a score.

**Desirability — 6**
- Pain intensity: 7 — Painkiller-grade evidence on both sides: the capacity-capped expert turning away paying demand (SIG-01, strong, verbatim — "I had a waitlist of 20+ … adding even one more would break me") and recurring WTP for *credential-gated* answers (SIG-16, JustAnswer ~$46–55/mo). Held at 7, not higher, because the AI-substitution objection (SIG-11 "it feels fake / I want the real person"; SIG-05 "sounds just like a normal chatgpt chat") shows the *human* is the proven painkiller and the AI agent inherits only part of that intensity.
- Demand evidence: 6 — Strong for the adjacent behaviours the one-to-one framing rests on: WTP for a *specific named expert* (SIG-03 strong — Intro $776–$5k, Nikita Bier $122.3k/95 bookings; SIG-12), credential-gated recurring WTP (SIG-16 strong), category validated by Delphi's $16M Sequoia Series A (SIG-09). Capped below 7 because the *specific* leap — paying recurring for an **AI agent** of a credentialed expert — is actively disconfirmed by SIG-05, SIG-10 (experts refuse to clone), SIG-11 (audiences distrust clones). Deliverables have no external demand evidence (inference only).
- Willingness to pay: 6 — JustAnswer proves durable recurring WTP for credential-gated answers at ~$46–55/mo, *above* Avee's $20–25 (SIG-16); Intro proves four-figure WTP for a specific expert (SIG-03). Both are for **human-delivered** output, so they de-risk the price point but not AI delivery. *Inference:* the "Deliverables" bullet plausibly raises WTP vs pure Q&A, but Gamma/Beautiful.ai render slides cheaply/free, so any premium rests on "the expert's judgment/style," unproven. Held at 6.

*Desirability average: (7+6+6)/3 = 6.33 → **6**. (With resonance removed, the raw average rises from v2.1's 5.75 but still rounds to 6.)*

**Viability — 6**
- Market size & growth: 6 — Containing creator economy large and growing (~$234–324B 2026, double-digit CAGR, research §1); the specific AI-expert-agent sub-market is **publicly unsized** (research §1, SIG "found nothing") but externally validated by Delphi's Sequoia round (SIG-09) and JustAnswer's proven credential-gated market (SIG-16).
- Monetization & unit economics: 7 — Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** (revenue-model §3), not the ~$3–5 the superseded bundle framing implied. The platform keeps a structural ~40–45% of gross with the cap. The "central competitive headwind" (market-research §3) is materially weaker: for *small / audience-less* experts Avee clearly beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06); for own-audience experts ~40–48% of a platform-set price with inference, agent and deliverables included is defensible. Held below 8 because experts who can set and collect their *own* price on Delphi (~85%) / Patreon (~90%) still keep more per subscriber at scale, and **payout acceptance is unproven** (no signal of experts choosing usage-share over a self-set price).
- Defensibility / moat: 5 — Automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard and attacks a real gap (Delphi shows no structured credentials, SIG-13; no EU/GDPR posture, SIG-14). The fraud-resistant user-centric payout architecture is validated (SoundCloud Fan-Powered Royalties, research §5) but is a mechanism, not a lasting moat. *Inference, net-neutral:* multi-owner "compare a VC's vs a founder's vs a designer's deck" is a genuine Delphi gap, but the deliverable itself sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment, not the renderer. Held at 5.
- Distribution path: 6 — **Reframed under the new rule (channel plausibility, never traction or the founder's warm access).** A reachable channel to the first buyers *does* exist and it is low-CAC by design: the **expert-led sharing loop** — each expert shares their own agent with their own audience, with a direct financial interest and a 10% referral bonus (revenue-model §4). That is a built-in growth loop (a thesis preference), and the expert/subscriber communities are nameable (r/coaching, r/consulting, Intro, MentorCruise, creator comment threads — SIG-01/03/18). Acquisition cost of an expert's own audience is essentially the expert's own promotion — plausible for a $20–25 price. Held at 6, not higher, because (a) two-sided liquidity makes the *first* cohort hard to seed, and (b) conversion down the channel is uncertain while the "pay for the AI, not the human" question is open (SIG-05/11) and GPT Store shows usage-based AI-payout platforms struggle to pull long-tail supply (research §7). Credential discovery is a post-liquidity flywheel, not a cold-start engine.
- Timing ("why now"): 6 — The competitive whitespace is open *now*: Delphi raised $16M but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Enabling tech (RAG + memory + cheap routing) and payout rails (Stripe Connect) are commoditized. Counterweight: GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

*Viability average: (6+7+5+6+6)/5 = 6.0 → **6**. (Distribution rose 4→6 under the rule change; the average still rounds to 6.)*

**Feasibility — 7** *(judged intrinsically for a small technical team, not against this founder's runway)*
- Technical complexity: 7 — A modern RAG/memory/multi-model agent platform with a usage-attribution payout layer is well within a small technical team's reach; the comparable product (Avee V2 v0.6.0, incl. image/video/voice generation) already exists as proof the stack is tractable. The novel hard part is **automated credential/employment verification**, which is load-bearing and partly outside standard agent work — that keeps this below 8.
- Capital intensity: 7 — Intrinsically capital-light: software on cheap, routed inference, commoditized Stripe Connect rails, no hardware/inventory. The fair-use cost cap + media-on-credits keep per-user cost below price so heavy use doesn't invert margin (revenue-model §3). Third-party credential/identity verification and metered inference are the only real recurring costs.
- Time to testable MVP: 7 — The product exists; the billing/payout layer is a bounded build and demand is testable with lightweight/manual verification of a handful of experts — a matter of weeks, not months, intrinsically.
- External dependencies: 5 — The genuine drag: Stripe Connect (KYC, DAC7/1099, chargebacks, 45-day holds), mobile-IAP avoidance (sell on web), credential-verification dependencies (Europass, LinkedIn/work-email, employer policy for current employees), and K7 expert-advice **plus** deliverable-attribution liability. Several are outside the team's control.

*Feasibility average: (7+7+7+5)/4 = 6.5 → **7**.*

**Composite (idea score):** `0.40×6 + 0.35×6 + 0.25×7` = **6.25**

**Gate checklist**
- G1 — Thesis (no kill rule fires): **Pass** — no K1–K7 fires (table above). K2/K7 conditional on automated, conservative verification and honest deliverable framing.
- G2 — Founder–target distance: **2 — Cold but mapped** — the founder is not the persona and has no warm network in it (founder-profile: AI/agent-dev and indie-hacker communities; "named no expert segment and no privileged access"), but the persona gathers in **known, open public channels** (r/consulting, r/coaching, r/freelance, Skool, Intro, MentorCruise — SIG-01/03/18). Not distance 1, because credentialed professionals and expert-followers are not the founder's own indie-hacker/dev crowd; not distance 3, because the channels are public and unmapped by no gatekeeper. Route to the first 10: cold outreach into one named niche (e.g. independent consultants in r/consulting) over 4 weeks. Distance 2 does **not** block Advance, and the G3 test is runnable via exactly this cold-outreach plan within 4 weeks.
- G3 — Riskiest assumption testable in ≤ 4 weeks: **Pass** — riskiest assumption = *will an expert's own audience pay $20–25/mo for that expert's AI agent (not the human), and will a credentialed expert publish one for ~$7.96–9.55/engaged sub rather than keep ~85–90% of a self-set price elsewhere?* Testable on the existing product in ≤ 4 weeks at distance 2: cold-recruit 3–5 credentialed experts from one niche, publish credential-fronted agents with one paid deliverable, pre-sell their audiences on the one-to-one subscription.
- G4 — Idea strength (≥ 7.5 Advance, < 6.0 Park): **6.25** — Iterate band (neither Advance nor Park). **This is the single deciding check.**

**Gate decision:** **Iterate** — G1 passes, G2 distance is 2 (≤ 2, does not block), G3 passes and its test is runnable at distance 2; the **only** bar to Advance is **G4 (composite 6.25 < 7.5)**. The composite is ≥ 6.0 and no kill rule fires, so it is not a Park. The one move that would flip G4 is to run the G3 experiment and convert the AI-delivery and payout-acceptance unknowns from disconfirmed/untested into evidenced demand.
**Biggest unknown:** Will an expert's own audience pay a recurring subscription for that expert's **AI agent** (or an AI-made deck in their style), not the human — and will credentialed experts accept **~$7.96–9.55 per engaged subscriber** (40–48% of a platform-set price) over keeping ~85–90% of a self-set price elsewhere? Every strong signal (SIG-03, SIG-16) proves WTP for the *human*; SIG-05/SIG-11 disconfirm the AI substitution; the deliverables upside is inference-only.
**De-risking step:** Pick one named credentialed niche the founder can cold-reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18), recruit 3–5 to publish credential-fronted agents with one paid deliverable, and pre-sell their existing audiences the one-to-one subscription. This single test captures both the riskiest assumption (G3) — audience WTP for AI delivery **and** expert payout acceptance — and demonstrates the distance-2 cold-outreach route works. A positive result moves this toward Advance; a negative one toward Park.

---

## Changes vs previous scorecards (v1: 5.1 Park → v2: 5.9 Park → v2.1: 6.25 Iterate → v3: 6.25 Iterate)

The composite is unchanged from v2.1 (6.25) and so is the gate (Iterate), but the
**reasons** are now cleanly separated. Below, each move is tagged **[rule]** (it
comes from the governance-rule change) or **[evidence]** (it comes from the
evidence base). **No evidence changed since v2.1** — same signals, same research,
same corrected payout — so every change in v3 is **[rule]**.

| Dimension | v2.1 | v3 | What moved and why |
|---|---|---|---|
| Desirability | 6 (Pain 7, Demand 6, WTP 6, Resonance 4) | **6** (Pain 7, Demand 6, WTP 6) | **[rule]** Founder–market resonance (the 4) was **removed** from Desirability and relocated to gate check **G2** (now a distance). Raw average rose 5.75 → 6.33; both round to 6, so the number is unchanged but it is now a cleaner "do people want it" score, no longer dragged by founder fit. |
| Viability | 6 (Market 6, Monet. 7, Moat 5, **GTM 4**, Timing 6) | **6** (Market 6, Monet. 7, Moat 5, **Distribution 6**, Timing 6) | **[rule]** "GTM realism 4" → "Distribution path 6". The old 4 was dominated by "founder has no warm channel / no seeded side" — now explicitly **excluded** (that is G2 distance and "never penalize traction"). Judged purely on channel plausibility, the expert-led sharing loop is a real, low-CAC channel → 6. Average rose 5.6 → 6.0; still rounds to 6. |
| Feasibility | 7 (vs the founder's runway) | **7** (judged intrinsically) | **[rule]** Re-labelled "Capital/resources vs runway" → "Capital intensity" and judged for a small technical team, not this founder's limited runway. Intrinsically the product is capital-light; score holds at 7 (6.5 → 7). External dependencies (5) unchanged — they are intrinsic to the space. |
| Composite | 6.25 | **6.25** | **[rule]** The two rule-driven moves (removing a low sub-score from D; raising Distribution in V) roughly cancel, so the idea score lands on the same 6.25 — now a measure of the *idea*, not the founder's situation. |
| Gate basis | Composite banding (Iterate because 6.0–7.4) | **Checklist G1–G4, G2 = distance** | **[rule]** The gate is now an explicit checklist with G2 as a 0–3 distance. Same outcome (**Iterate**), but the deciding reason is now **G4 alone** (6.25 < 7.5). G2 distance is **2 (Cold but mapped)** — it does *not* block Advance, and the ≤4-week cold-outreach test is runnable at that distance. The founder-fit concern that used to suppress the idea score is now expressed as a *manageable* distance, not a disqualifier. |

**Honest note on not inflating:** nothing in v3 is an evidence-driven upgrade.
The AI-delivery demand leap (SIG-05/11) and payout acceptance are as unproven as
in v2.1, which is why the idea score did not rise. The rule change made the score
*cleaner*, not *higher*: it moved the founder-fit penalty out of the idea score,
and G2 now reads it as distance 2 (acceptable), so the sole bar to Advance is the
idea's own strength (G4). The practical verdict (Iterate, run the one pre-sell
test) is identical.

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
- **Payout acceptance is unproven** — no signal shows experts choosing a ~40–48% usage share over keeping ~85–90% of a self-set price; this is the dominant open question on the supply side.
- **Long-tail payout friction** — $25 minimum + ~$2/account/month Stripe fees mean audience-less experts net ~$0 until discovery traffic exists (the SIG-18 cold-start problem).

**Single change that would most raise the score:** Lead the creator pitch with the
corrected own-audience economics (**~$8–9.55/engaged sub at $20, no monthly fee,
infra + deliverables included**) plus the small-expert wedge where Avee beats
Delphi (SIG-06), and a high-share private-agent / paid-escalation / paid-deliverable
layer (expert keeps ~80%). That frames the offer accurately and attacks the real
open risk — payout *acceptance*, not payout *size*.

---

## Top recommendation

There is one idea this run. **IDEA-01 is Iterate at composite 6.25** (idea score,
for ranking only). Under the new rules the score is the same as v2.1 but earned
more cleanly: founder-fit no longer suppresses the idea score — it reads as **G2
distance 2 (Cold but mapped)**, which does *not* block Advance. **G1** passes (no
kill rule fires) and **G3** passes with a test runnable at distance 2, so the
**sole** bar to Advance is **G4 — the idea's own strength (6.25 < 7.5)**. The path
forward is therefore singular: lift the idea on evidence, not on reachability.

**Highest-priority validation step:** commit to **one** named credentialed niche
and cold-reach 10 of the persona this week (e.g. independent consultants in
r/consulting, SIG-18 — the distance-2 route), recruit **3–5 experts** to publish
credential-fronted agents with one paid deliverable, and **pre-sell their existing
audiences** the one-to-one $20–25 subscription. One test resolves the deciding
unknowns at once — it proves (or kills) audience WTP for AI delivery and expert
acceptance of the ~$7.96–9.55/engaged-sub payout, which is exactly what would move
G4 across the Advance line. A positive result moves IDEA-01 toward Advance; a
negative one returns it to Park.
