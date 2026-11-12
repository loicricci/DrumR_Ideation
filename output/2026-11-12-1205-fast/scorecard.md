# Scorecard — run 2026-11-12-1205-fast (v2.1, re-scored)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage** on
> the standard rubric. v2.1 corrects a factual error carried from v2: the
> per-engaged-subscriber creator payout was quoted as "~$3–5", a figure from the
> **superseded bundle framing** (subscriber splits usage 50/50 across agents).
> Under the **corrected one-to-one distribution model** in `ideas.md` (the expert
> brings their own audience, which mostly uses that expert's agent → ~100% usage),
> revenue-model §3 gives **~$7.96 at $20 (40% of price), ~$9.55 with the 10%
> referral bonus (48%), and ~$10.36–12.43 at $24.99 (41–50%)**. The ~$3–5 only
> applies to incidental cross-traffic from *other* experts' subscribers — extra
> upside, not the core case. That correction raises Monetization and flips the gate.
>
> Weights: **Composite = 0.40×D + 0.35×V + 0.25×F**. Gates: Advance ≥ 7.5,
> Iterate 6.0–7.4, Park < 6.0 (thresholds never lowered). Evidence base:
> `signals.md` (18 signals), `market-research.md` (confidence: Medium),
> `revenue-model.md` (v1 spec §7). The "Deliverables" bullet has **no external
> evidence yet**, so every effect from it is labelled **inference**.
> v1 scored 5.1 Park (thesis kill K6, bundle framing); v2 scored 5.9 Park.

## Kill-rule check (thesis.md K1–K7)

Checked **before** scoring. A broken rule forces **Park** regardless of composite.
K6 is re-judged against the new `signals.md`.

| Rule | Verdict | Why |
|---|---|---|
| K1 — No sales calls | **Pass** | Self-serve consumer subscription, web checkout, credit card. Unchanged. |
| K2 — Ops automatable solo | **Pass (conditional)** | Payouts/KYC/holds automate via Stripe Connect Express. New conditional: credential verification must be **automated** (Europass digital credentials, work-email domain, LinkedIn) — if it degrades to a manual review queue it grows with supply and breaks K2. The founder names automated verification as the core build, so this holds *by design*, at build risk. |
| K3 — MVP testable ≤ 4 weeks | **Pass** | Product exists (Avee V2 v0.6.0), including image/video/voice generation for deliverables. A demand-test MVP — recruit 3–5 experts with lightweight/manual credential checks, pre-sell their audiences — is ≤ 4 weeks. The *fully automated* credential asset is a later scale-up build, not an MVP blocker. |
| K4 — Economics work small | **Pass (only with the cap)** | Gross-margin-positive from the first paying user **only** because the fair-use inference cap + media-on-credits keep cost C < net N; the literal "50% of gross" model goes negative on heavy users (revenue-model §2). Deliverables (decks/images) run on credits (cost × 2), which keeps K4 intact *if* generation is metered. Unchanged verdict. |
| K5 — Reachable persona | **Pass (weak)** | Upgraded from v1's effective fail. The credential-first reframe names a reachable persona — credentialed professionals who want to monetize without an audience (SIG-18: r/consulting, r/freelance, Skool) — and the demand side is findable (SIG-03/04: Intro, MentorCruise, creator comment threads). The founder still has **no privileged access** to either side; places exist, a warm channel does not. |
| K6 — Evidenced pain | **Pass** | **The decisive change from v1.** `signals.md` now carries first-hand, dated customer language: SIG-01 (Ken Deng, DEV, Mar 6 — "I'd run out of time", fetched verbatim), SIG-02 (Josh Spector, fetched verbatim), SIG-05/06 (Delphi Trustpilot + help-center, fetched verbatim), SIG-16 (JustAnswer recurring ~$46–55/mo, credential-gated). K6 is comfortably met. |
| K7 — No high-liability space | **Pass (conditional, at-risk)** | Expert-advice agents in health/finance/legal give advice *as the expert*; the credential-first angle *raises* K7 stakes because a falsely verified "Harvard-trained" badge is itself a liability, and a deck sold "from a VC" must be framed as *built with that expert's agent*, not endorsed by the human. Structurally removable in the wedge: exclude regulated categories, verify conservatively, label AI deliverables honestly. Manageable, not forcing. |

**Forcing verdict:** **No kill rule fires.** K6 — the v1 killer — now passes on strong,
dated, first-hand signals. K2/K7 are conditional on automated, conservative
credential verification and honest deliverable framing; K5 passes weakly. The idea
is therefore gated on its **composite**, not force-parked.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 6 | 6 | 7 | 6.25 | Iterate |

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 6.25  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 7 — Painkiller-grade evidence now exists on both sides: the capacity-capped expert turning away paying demand (SIG-01, strong, verbatim) and recurring WTP for *credential-gated* answers (SIG-16, JustAnswer ~$46–55/mo). Tempered by the AI-substitution objection — SIG-11 ("it feels fake / I want the real person") and SIG-05 ("sounds just like a normal ChatGPT chat") — which show the *human* is the proven painkiller; the AI agent inherits only part of that intensity.
- Demand evidence: 6 — Strong for the adjacent behaviours the corrected framing relies on: WTP for a *specific named expert* (SIG-03 strong — Intro $776–$5k; SIG-12), credential-gated recurring WTP (SIG-16 strong), and a category validated by Delphi's $16M Sequoia Series A (SIG-09). Capped below 7 because the specific leap — paying recurring for an *AI agent* of a credentialed expert — is still disconfirmed by SIG-05, SIG-10 (experts refuse) and SIG-11 (audiences distrust clones). The one-to-one correction *aligns* the idea with SIG-12 (demand is for one named expert, not a bundle). No external demand evidence for deliverables (inference only).
- Willingness to pay: 6 — JustAnswer proves durable recurring WTP for credential-gated answers at ~$46–55/mo, *above* Avee's $20–25 (SIG-16); Intro proves four-figure WTP for specific experts (SIG-03). Both are for **human-delivered** output, so they de-risk the price point but not AI delivery. *Inference:* the new "Deliverables" bullet plausibly raises WTP vs pure Q&A, but Gamma/Beautiful.ai render slides cheaply/free, so the premium rests on "the expert's judgment/style" — unproven. Held at 6. (Note: the figure correction is about creator *payout*, not buyer WTP, so it does not move this sub-score.)
- Founder–market resonance: 4 — The persistent weakness. Solo technical founder, observer of these communities, **named no expert segment and no privileged access** (founder-profile). Credential-first and deliverable-tooling play to his technical edge (verification, generation pipelines already built), but he still has no warm channel into either side of a two-sided trust market.

**Viability — 6**
- Market size & growth: 6 — Containing creator economy large and growing (~$234–324B 2026, double-digit CAGR, research §1); the specific AI-expert-agent sub-market is **publicly unsized** (research §1) but externally validated by Delphi's Sequoia round (SIG-09) and JustAnswer's proven credential-gated market (SIG-16).
- Monetization & unit economics: **7** (was 6) — **Raised on the figure correction.** Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40% of price), ~$9.55 with the referral bonus (48%), and ~$10.36–12.43 at $24.99 (41–50%)** (revenue-model §3), not the ~$3–5 the superseded bundle framing implied. The platform still keeps a structural ~40–45% of gross with the cap. So the "central competitive headwind" that dominated market-research §3 ("structurally far less generous per engaged subscriber") is materially weaker: for *small / audience-less* experts Avee clearly beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06) and, for own-audience experts, ~40–48% of a platform-set price with inference, agent and deliverables included is a defensible offer. Held below 8 because experts who can set and collect their *own* price on Delphi (~85%) / Patreon (~90%) still keep more per subscriber at scale, and **payout acceptance is unproven** (no signal of experts choosing usage-share over a self-set price). *Inference:* deliverables run on credits (cost × 2), margin-accretive if metered.
- Defensibility / moat: 5 — Automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard and attacks a real gap (Delphi shows no structured credentials, SIG-13; no EU/GDPR posture, SIG-14). *Inference, net-neutral:* multi-owner "compare a VC's vs a founder's vs a designer's deck" is a genuine Delphi gap and a reason to use several agents, but the deliverable itself sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment, not the renderer. Held at 5 — the figure correction does not touch the moat.
- Go-to-market realism: 4 — Two-sided cold start under 50 users, no seeded side, no named niche, founder has no warm channel. Better creator economics (above) make the supply pitch easier, but GTM realism is dominated by the unsolved no-warm-channel / no-seeded-side problem, which the correction does not fix. Held at 4. Credential discovery is a post-liquidity flywheel, not a cold-start engine (see SIG-18).
- Timing ("why now"): 6 — The competitive whitespace is open *now*: Delphi raised but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Counterweight: GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

**Feasibility — 7**
- Technical complexity vs. capability: 7 — Product already built on the founder's core stack (agents, RAG, semantic memory, cheap routing), **and image/video/voice generation already ships** (founder-profile), so deliverable tooling is incremental. The new credential-verification layer (diploma/employment checks) is partly outside the demonstrated stack and is load-bearing, which holds this below an 8.
- Capital / resources vs. runway: 7 — Bootstrapped and solo; the cost cap + media-on-credits keep infra below price so heavy users and heavy generation don't burn runway. Third-party credential/identity verification adds some cost.
- Time to testable MVP: 7 — The billing/payout layer is ≤ 4 weeks part-time on an existing product; deliverables and generation already exist; demand can be tested with lightweight/manual verification of a handful of experts.
- External dependencies: 5 — Stripe Connect (KYC, DAC7/1099, chargebacks), mobile-IAP avoidance, credential-verification dependencies (Europass, LinkedIn/work-email, employer policy), K7 expert-advice **and** deliverable-attribution liability.

**Composite:** `0.40×6 + 0.35×6 + 0.25×7` = **6.25**
**Gate decision:** **Iterate** (was Park at 5.9) — the figure correction raises Monetization 6→7, which lifts Viability's sub-score average to 5.6 → **6**, and the composite to 6.25, into the 6.0–7.4 Iterate band. No kill rule fires. It is Iterate, not Advance, because the demand leap (pay for the *AI*, not the human) and payout acceptance remain unproven, and the founder has no warm channel into either side.
**Biggest unknown:** Will an expert's own audience pay $20–25/month for that expert's **AI agent** (or an AI-made deck in their style), not the human — and will credentialed experts publish one for **~$7.96–9.55 per engaged subscriber** (40–48% of a platform-set price) rather than keeping ~85–90% of a self-set price elsewhere? Every strong signal (SIG-03, SIG-16) proves WTP for the *human*; SIG-05/SIG-11 disconfirm the AI substitution; the deliverables upside is inference-only.
**De-risking step (the one Iterate experiment):** Pick one named credentialed niche the founder can reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18), recruit 3–5 to publish credential-fronted agents with one paid deliverable, and pre-sell the one-to-one subscription to their existing audiences. This captures, in a single test, both unknowns: audience WTP for AI delivery **and** expert acceptance of the corrected ~$7.96–9.55/sub payout. A positive result moves this toward Advance; a negative one back to Park.

---

## Factoring "Deliverables, not just answers" (founder input — inference only)

No external evidence exists for this bullet yet, so every effect below is **inference**;
none changed a rounded sub-score, and the net is roughly zero.

- **WTP (inference, mild positive, hedged):** Deliverables have an explicit market price,
  so WTP is plausibly higher than for Q&A — but Gamma/Beautiful.ai/Tome already render
  decks cheaply/free, so any premium rests on the expert's judgment/style, unproven.
  Mild lift, fully offset → WTP held at 6.
- **Differentiation vs Delphi (inference, positive):** Delphi's clones are chat-only
  (SIG-13). Tool-made deliverables + a multi-owner **compare** are a clear, if copyable,
  gap Delphi does not occupy. Folded into moat/timing.
- **Cross-agent usage for the payout model (inference, positive):** "Request several
  versions from several owners and compare" is a native reason to use multiple agents,
  which spreads the creator pool to agents beyond the one that brought the subscriber.
  Note this is the *extra-upside* cross-traffic case (the ~$3–5 band), layered on top of
  the ~$7.96–9.55 an expert earns from their own audience's concentrated usage. Folded
  into monetization.
- **Generation cost on credits (inference, neutral-to-positive):** Decks/images route to
  credits at cost × 2 (revenue-model §3), so deliverables are margin-accretive if metered
  and do not threaten the K4 cap.
- **Competition from Gamma/Beautiful.ai (inference, negative — main caution):** Enters a
  crowded, well-funded horizontal market whose incumbents out-render generic output; the
  only defensible layer is the expert's judgment + credential trust. Caps upside; why
  differentiation/WTP are held, not raised.
- **Framing honesty (flag):** Second scope expansion this run (credentials, then
  deliverables), each adding build and competitive surface with no external evidence. An
  AI deck "from the best VC" must be framed as *built with that expert's agent* (optional
  paid human review via escalation), not the human's endorsed work — otherwise a
  misrepresentation and K7 liability. Risk of drifting toward "a worse Gamma with experts
  attached" if the expert-judgment premium is not validated first.

**Net effect on scores:** inference-positive on bundle/payout coherence and
differentiation, offset by commoditised competition and scope risk. Rounded scores from
this bullet unchanged: it did **not** drive the gate change — the **figure correction**
did. Current: **D 6 / V 6 / F 7 / Composite 6.25 / Iterate.**

---

## The SIG-18 tension: does credential-based discovery resolve "own audience" vs "audience-less"?

The corrected idea makes two claims that pull against each other, and SIG-18 flags it
(strength: medium, "in tension with the stated distribution model"):

1. **Expert brings own audience** — each expert shares *their own* agent with *their own*
   audience; demand rests on "A's audience wants on-demand access to A" (the Delphi /
   SIG-12 pattern). This **requires** an audience — and it is exactly this concentrated,
   ~100%-usage case that yields the corrected ~$7.96–9.55/sub economics.
2. **Pedigree, not personality** — verified credentials let users *discover by credentials*,
   so an **audience-less** professional can earn (SIG-18 persona). This **requires Avee to
   supply** demand-side discovery traffic.

**Does credential-discovery resolve the conflict? Partially, and only after liquidity — not
at cold start.** The two models are sequential and complementary:

- Credential-based discovery can only monetize an audience-less professional if there is a
  pool of users *searching by credential* on Avee — traffic that does not exist at cold
  start (under 50 users, SIG-18 counter-signal).
- Those searching users arrive because **audience-bringing experts** (model 1) dragged
  their audiences on first. So audience-bringing experts are simultaneously the cold-start
  supply *and* the engine that generates the discovery traffic that later lets
  audience-less professionals earn.
- The pedigree bullet therefore **widens the eventual supply TAM and adds a second supply
  channel**, but does **not** relieve the two-sided cold start. The first cohort of experts
  must still bring their own audiences.

Net: credential-discovery is a real asset for *later* expansion and a genuine Delphi gap
(SIG-13), but SIG-18's counter-signal stands for the phase that matters now. The reframe
does resolve a *different* tension correctly: moving from an all-access bundle to one-to-one
matches the evidence that WTP is for a single named/credentialed expert (SIG-12, SIG-03),
not a bundle (research §2). The deliverables/compare feature cuts slightly *against* strict
one-to-one (multi-owner comparison is multi-agent) — useful for the payout model's upside,
but it reopens the "why a bundle" question the one-to-one correction had closed.

---

## Changes vs previous scorecard (v1: 5.1 Park → v2: 5.9 Park → v2.1: 6.25 Iterate)

| Dimension | v1 | v2 | v2.1 | Why it moved |
|---|---|---|---|---|
| Kill rules | **K6 FAIL** (force-park) | No kill fires | No kill fires | `signals.md` supplies first-hand, dated, fetched-verbatim pain (SIG-01, 02, 05, 06, 16). K6 — the v1 killer — now passes. K5 upgraded to weak-pass. Unchanged in v2.1. |
| Desirability | 4 | 6 | **6** | Demand 3→6, pain 5→7: corrected one-to-one framing aligns with proven single-expert WTP (SIG-03, SIG-12) and credential-gated recurring WTP (SIG-16). Unchanged in v2.1 (the figure fix is about creator payout, not buyer WTP). |
| Viability | 5 | 5 | **6** | **v2.1 change.** Monetization 6→7 after the per-engaged-sub payout was corrected from "~$3–5" (superseded bundle framing) to **~$7.96–9.55 at $20, ~$10.36–12.43 at $24.99** (one-to-one model, revenue-model §3). That lifts the Viability sub-average to 5.6 → 6. Moat (5), GTM (4), market (6), timing (6) unchanged — the correction does not justify moving them. |
| Feasibility | 7 | 7 | **7** | Product-already-built advantage (incl. generation pipelines); offset by the load-bearing automated-credential build. Unchanged. |
| Composite / Gate | 5.1 / Park (thesis kill) | 5.9 / Park (near-miss) | **6.25 / Iterate** | The figure correction alone moved Viability across the rounding boundary (5.6→6) and the composite from 5.9 to 6.25, into the Iterate band. No threshold was lowered. |

**Honest note on not inflating:** v2.1 moves **only** the sub-score the correction justifies
(Monetization, on a factual error that roughly doubled the core-case payout). I deliberately
did **not** move WTP, demand, moat, GTM, or resonance, because the correction does not bear
on them — the demand leap (pay for the AI, not the human) and the founder's missing warm
channel are untouched, which is why this is Iterate, not Advance.

---

## Revenue model verdict (revenue-model.md §7 v1 spec)

**What holds (unchanged and strong):**
- **The margin is structural, not hopeful.** 50% of net contribution P = max(N − C, 0)
  keeps the platform at ~40–45% of gross on every subscriber (§3), fixing the §2
  contradiction.
- **The fair-use cost cap + media-on-credits is what makes K4 true** and absorbs the new
  deliverables cost (decks/images on credits, cost × 2). Keep it non-negotiable.
- **Fraud resistance is the model's best property and it is evidenced** — user-centric
  attribution makes self-dealing and collusion lose money (SoundCloud Fan-Powered
  Royalties, research §5). Do not switch to a pooled model.
- **Ops stay solo-operable** via Stripe Connect Express, 45-day holds, $25 minimum payout
  (K2), conditional on credential verification staying automated.

**What the figure correction changes (the material v2.1 update):**
- **Creator economics are roughly double what v2 stated.** Under the corrected one-to-one
  model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55
  with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** — not ~$3–5. The ~$3–5
  band applies only to *cross-traffic* from other experts' subscribers, which is **extra
  upside** on top, not the core case.
- **The "≥ $5" promise is actually met at $20.** v2's caveat that "≥$5 requires $24.99 or a
  60% split" was itself an artefact of the 50%-usage bundle math; at ~100% own-audience
  usage the expert clears ~$7.96 at a plain $20. Drop that caveat.
- **The "central competitive headwind" is materially weaker.** Market-research §3's
  "structurally far less generous per engaged subscriber" rested on the mis-framed number.
  Avee still pays less per sub than *self-set-price* alternatives for big experts (~85–90%),
  but beats Delphi outright for small/audience-less experts (Delphi is a $79–299/mo cost
  with no built-in monetization, SIG-06), and ~40–48% of a platform-set price with inference,
  agent and deliverables included is defensible.

**What is still weak (evidence confirms, not relieves):**
- **The AI-delivery demand leap is unproven** — SIG-05 and SIG-11 are active disconfirmers;
  the deliverables premium over Gamma/Beautiful.ai is inference-only.
- **Payout acceptance is unproven** — no signal shows experts choosing a ~40–48% usage share
  over keeping ~85–90% of a self-set price; this is now the dominant open question on the
  supply side (it replaces the old, overstated "~$3–5 is too little" framing).
- **Long-tail payout friction** — $25 minimum + ~$2/account/month Stripe fees mean
  audience-less experts net ~$0 until discovery traffic exists (the SIG-18 cold-start
  problem).

**Single change that would most raise the score:** Lead the creator pitch with the corrected
own-audience economics (**~$8–9.55/engaged sub at $20, no monthly fee, infra + deliverables
included**) plus the small-expert wedge where Avee beats Delphi (SIG-06), and a high-share
private-agent / paid-escalation / paid-deliverable layer (expert keeps ~80%). This frames the
offer accurately and attacks the real open risk — payout *acceptance*, not payout *size*.

---

## Top recommendation

There is one idea this run and it now clears the Iterate bar: **IDEA-01 is Iterate at
6.25** (up from v2's 5.9 Park), solely because the per-engaged-subscriber creator payout was
corrected from "~$3–5" — a figure from the superseded bundle framing — to **~$7.96–9.55 at
$20 (up to ~$12.43 at $24.99)** under the actual one-to-one model, which raised Monetization
6→7 and Viability 5→6. No threshold was lowered and no other sub-score moved. It is Iterate,
not Advance, because two things remain unproven: that an expert's audience will pay for the
**AI** rather than the human (SIG-05/SIG-11 disconfirm), and that credentialed experts will
accept a ~40–48%-of-price usage share over keeping ~85–90% of a self-set price — and the
founder has no warm channel into either side. Highest-priority validation step: recruit 3–5
credentialed experts from one named niche (e.g. r/consulting, SIG-18), publish
credential-fronted agents with one paid deliverable, and pre-sell their own audiences on the
one-to-one subscription — capturing audience WTP for AI delivery *and* expert payout
acceptance in a single test. That result decides whether IDEA-01 advances or returns to Park.
