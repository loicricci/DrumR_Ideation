# Scorecard — run 2026-11-12-1205-fast (v5, re-scored under the "weigh evidence by who says it" rule)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage**
> under one newly-added governance rule: **"Weigh evidence by who says it."** The
> evidence base is identical to v4 (same `signals.md`, same `market-research.md`,
> same `revenue-model.md`, same corrected one-to-one payout). What changed is how
> the rule tells me to read the **disconfirming** evidence — in particular who is
> speaking, and about which job.
>
> **Governance advises; the founder decides.** The ranking and the checklist are
> reasons to learn from, not a verdict on what may be pursued. The gate line is an
> **advisory Recommendation**, and the card closes with a **For the founder** note
> on why it lands where it does and what evidence would move it.
>
> **What changed since v4 — the one new rule**
>
> "Weigh evidence by who says it." A quote only counts against an idea at **full
> weight** when it comes from the **target persona** about the **job the idea
> does**. Disconfirming evidence is sorted:
> - `non-target` / `conflicted` → **context only**; never lowers Desirability,
>   Demand or WTP.
> - `boundary` ("I want the real person", from people outside the persona) → sizes
>   the market's **edge**, can temper **Market size** slightly; does **not** lower
>   demand inside the target.
> - `quality` complaints from `current-user`s of a **competitor** ("sounds like
>   ChatGPT") → **product requirements and opportunity** under **Defensibility**
>   and the biggest unknown — often evidence **for** a better entrant, not missing
>   demand.
> - `rejection` from **target-buyers** → **full weight** against Demand and WTP.
>
> **The headline:** the idea score is **unchanged at 6.65**. The new rule does not
> raise the composite, and that is the honest result. In v4 I used **SIG-05,
> SIG-10 and SIG-11 to cap Demand and WTP at 7**, calling them "genuine
> disconfirmers weighed as real evidence." Under the new rule that was the **wrong
> home** for all three: SIG-05 is a competitor **current-user quality** complaint
> (→ Defensibility/opportunity), SIG-11 is a **boundary** statement from people
> outside the AI-agent persona (→ Market-size edge), and SIG-10 is a **supply-side
> rejection** (→ Distribution/cold start). None of them should have been docking
> Demand or WTP. **But Demand and WTP still sit at 7** — because the independent,
> unchanged rule ("indirect evidence justifies up to 7 on its own; above 7 needs
> **direct** evidence") caps them there: the strong indirect evidence (Delphi's
> Sequoia round, JustAnswer, Intro) earns the 7, and there is **no direct
> target-persona demand evidence for paying for an expert's AI agent** to push past
> it. So v5 re-attributes the cap to the correct cause and moves the three
> disconfirmers to their correct dimensions. The only sub-score that moves is
> **Pain intensity 7 → 8** (the SIG-05/SIG-11 brake that held it at 7 is
> reclassified away from demand, and direct, dated, verbatim supply-side pain —
> SIG-01 — justifies above 7). That raises the Desirability average from 7.0 to
> 7.33, which still **rounds to 7**. Composite stays **6.65**. **Thresholds were
> not lowered; nothing was inflated** — the binding cap on Demand/WTP is the
> direct-evidence ceiling, exactly as before, just correctly named.
>
> Corrected creator payout carried forward unchanged (one-to-one own-audience
> usage, revenue-model §3): **~$7.96 at $20 (40% of price), ~$9.55 with the 10%
> referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)**. The old "~$3–5" applies
> **only** to incidental cross-traffic from other experts' subscribers.
>
> Weights: **Composite = 0.40×D + 0.35×V + 0.25×F** (CLAUDE.md default). Gate bands
> (advisory): Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (never lowered). Evidence
> base: `signals.md` (18 signals), `market-research.md` (confidence: **Medium**),
> `revenue-model.md` (v1 spec §7).

## Disconfirming evidence — classified by who says it (the v5 lens)

`signals.md` predates source-role tags, so each signal that cuts against the idea
is classified here by **source role** (target-buyer / target-supplier /
current-user / non-target / conflicted / observer) and **kind** (rejection /
quality / boundary), with the weight the new rule assigns and where it lands.

| Signal | What it says (against the idea) | Source role | Kind | Weight under the rule | Lands in |
|---|---|---|---|---|---|
| **SIG-05** | Delphi clone "sounds just like a normal chatgpt chat … no real reason to use this" | **current-user** of competitor (Delphi) | **quality** | **Context / opportunity** — never a Demand/WTP drag; evidence *for* a better entrant | Defensibility + biggest unknown |
| **SIG-11** | Audiences: "it feels fake," **"I want the real person"** | **non-target / boundary** (people who reject AI substitution — outside the AI-agent-buyer persona) | **boundary** | **Context** — sizes the market's edge; tempers **Market size** slightly; does **not** lower demand inside the target | Market size (edge) + biggest unknown |
| **SIG-10** | Respected writer refuses to clone — "founded on predation" | **target-supplier** (a potential supply-side expert) | **rejection** (supply-side, ethics-grounded) | **Full weight on the supply-pull / cold-start question** (genuine target-supplier), tempered by the documented split (many experts *do* build) and wedge-fit (pedigree-first, name-optional targets SIG-18 professionals). **Not** a demand/WTP drag | Distribution (cold start) + Defensibility + biggest unknown |
| **SIG-07** | Delphi "scammers … charged my card … without notice" | **current-user** of competitor | **quality** (billing/trust) | **Context / opportunity** — transparent public earnings dashboard + clear billing is Avee's differentiator | Defensibility (opportunity) |
| **SIG-18** (counter) | Audience-less professionals want to earn **without** building an audience — in tension with "expert brings own audience" | **target-supplier** | **boundary** (defines which suppliers fit the one-to-one model) | **Context** — real supply sub-segment that needs platform-supplied discovery | Distribution + biggest unknown |
| **SIG-12** (counter) | Clone earnings concentrate in 100k+ audiences; long tail earns little | **observer** (market structure) | **boundary** (supply economics edge) | **Context** — defines who the payout economics work for | Distribution + revenue-model caveat |
| **SIG-01** (counter) | Same capacity-capped coach's *fix* was systems/automation, not an AI clone | **target-supplier** | **quality** (solution-fit, not pain severity) | **Context** — solution-fit question, not a pain-intensity drag | Biggest unknown |
| GPT Store (research §7) | Usage-based AI-creator payouts stayed invite-only; most builders earned **$0** | **observer** (platform precedent) | **quality / boundary** | **Genuine disconfirming** on usage-based AI payouts — a real platform-outcome precedent, kept weighted | Distribution + Timing |

**Read of the three the orchestrator named.** All three were *mis-filed in v4* as
Demand/WTP drags:
- **SIG-05 (current-user, quality)** — a competitor's own user complaining the
  clone is generic is, under the rule, evidence **for** a better entrant with
  stronger RAG + semantic memory and credential-first trust. It belongs in
  **Defensibility** (the opportunity) and the biggest unknown (Avee's AI must
  clear the "not-just-ChatGPT" bar), **not** against demand.
- **SIG-11 (non-target / boundary)** — "I want the real person" is the rule's
  literal boundary example: it comes from people **outside** the AI-agent-buyer
  persona and sizes the **edge** of the market. It tempers **Market size**
  slightly (it is one reason Market size sits at 7, not 8) and feeds the
  AI-vs-human biggest unknown. It does **not** lower demand among those who **do**
  want on-demand AI access to an expert.
- **SIG-10 (target-supplier, rejection)** — this one **is** a genuine
  target-persona rejection, so it is **not dropped**: it carries full weight on
  the **supply-side** question (will credentialed experts publish and accept the
  usage share), where it lives in **Distribution/cold start** and the biggest
  unknown. It is tempered — not erased — by the documented split (Spector, Lenny,
  Halligan, Rabois, Lemkin all build clones) and by the pedigree-first,
  name-optional wedge aimed at SIG-18 professionals, whose objection is weaker.
  It was never demand-side evidence.

**Why this does not inflate.** Removing SIG-05/10/11 from the Demand/WTP cap does
**not** free those sub-scores to rise, because the **"above 7 needs direct
evidence"** rule independently caps them at 7: every proven demand/WTP data point
is for the **human** expert (Intro, JustAnswer) or is a competitor **company
claim** (Delphi earnings) — strong **indirect** evidence (ceiling 7), with **no
direct target-persona evidence of paying for an expert's AI agent** to justify
exceeding it. So Demand = 7 and WTP = 7, same numbers, correct cause.

## Evidence flag (thesis.md, recorded — never a kill)

- **Direct:** first-hand, dated, fetched-verbatim **pain** on the supply side —
  SIG-01 (Ken Deng, DEV, Mar 6: "I'd run out of time"; "a waitlist of 20+ …
  adding even one more would break me"), SIG-02 (Josh Spector). This is the direct
  evidence that now carries **Pain intensity above 7**.
- **Indirect (strong):** **Delphi $16M Sequoia Series A, ~$18.7M total** (SIG-09,
  verified); **JustAnswer** credential-gated recurring paid Q&A at ~$46–55/mo
  (SIG-16); **Intro** four-figure WTP for a specific named expert (SIG-03). Per the
  indirect-evidence rule these justify **up to 7** on Demand, WTP and Market size —
  and, with no direct demand evidence to exceed 7, they set the ceiling.
- **Unknown (to test in P/S Fit, not a penalty):** recurring WTP for an **AI**
  agent of a credentialed expert (vs the human); whether credentialed experts
  **accept** a ~40–48% usage share over keeping ~85–90% of a self-set price; the
  deliverables premium over Gamma/Beautiful.ai.
- **Disconfirming, now correctly filed (v5):** SIG-05 → Defensibility/opportunity;
  SIG-11 → Market-size boundary; SIG-10 → supply-side cold start; GPT Store →
  Distribution/Timing. **None of these dock Demand or WTP** under the new rule.

## Kill-rule check (thesis.md K1–K7) — feeds gate check G1

Checked **before** scoring. A broken rule forces **Park** (G1 fail) regardless of
composite. **K5 and K6 are retired as kills** (thesis.md): K5 is the gate's G2
distance; K6 is the evidence flag above. No change from v4.

| Rule | Verdict | Why |
|---|---|---|
| K1 — No sales calls | **Pass** | Self-serve consumer subscription, web checkout, credit card. |
| K2 — Ops automatable solo | **Pass (conditional)** | Payouts/KYC/holds automate via Stripe Connect Express. Conditional: credential verification must stay **automated** (Europass, work-email domain, LinkedIn); a manual review queue would grow with supply and break K2. The founder names automated verification as the core build, so this holds *by design*, at build risk. |
| K3 — MVP testable ≤ 4 weeks | **Pass** | Product exists (Avee V2 v0.6.0, incl. image/video/voice). A demand-test MVP (3–5 experts, lightweight credential checks, pre-sell their audiences) is ≤ 4 weeks. Full automated verification is a later scale build, not an MVP blocker. |
| K4 — Economics work small | **Pass (only with the cap)** | Gross-margin-positive from the first paying user **only** because the fair-use inference cap + media-on-credits keep cost C < net N; the literal "50% of gross" model goes negative on heavy users (revenue-model §2). |
| K5 — *(retired as a kill)* | **n/a — now G2** | Reachability is measured as founder–target **distance** in the gate (G2 below = 2, Cold but mapped). |
| K6 — *(retired as a kill)* | **n/a — evidence flag** | Missing evidence is "unknown, to be tested," not "bad." Recorded in the evidence flag. Never parks the idea. |
| K7 — No high-liability space | **Pass (conditional, at-risk)** | Expert-advice agents in health/finance/legal advise *as the expert*; credential-first *raises* K7 stakes (a falsely verified badge is itself a liability; a deck "from a VC" must be framed as *built with that expert's agent*). Structurally removable: exclude regulated categories, verify conservatively, label AI deliverables honestly. Manageable, not forcing. |

**Forcing verdict:** **No kill rule fires** → **G1 passes.** K2/K7 conditional on
automated, conservative verification and honest deliverable framing.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate | Distance |
|---|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 7 | 6 | 7 | 6.65 | Iterate | 2 |

*The "Gate" column is the advisory **Recommendation**, not a verdict — the founder
decides.*

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 6.65  ·  Recommendation: Iterate

> The composite is the **idea score**, used for ranking only. The recommendation is
> advisory — the founder decides. Missing traction never lowers a score.

**Desirability — 7**
- Pain intensity: **8** — **[rule-moved from 7.]** Direct, dated, fetched-verbatim painkiller pain on the supply side: the capacity-capped expert turning away paying demand (SIG-01, strong — "I had a waitlist of 20+ … adding even one more would break me"), plus recurring demand-side WTP for *credential-gated* answers (SIG-16, JustAnswer ~$46–55/mo). In v4 this was held at 7 by SIG-05 ("sounds like ChatGPT") and SIG-11 ("I want the real person"). Under the new rule those are a **competitor current-user quality** complaint and a **boundary** statement — neither measures the severity of the problem, so the brake is removed and **direct** evidence (SIG-01) justifies above 7. Held at 8, not 9, because the demand-side pain for the **AI** version specifically is indirect, and SIG-01's own counter (the author's fix was automation, not a clone) is a live **solution-fit** question (logged in the biggest unknown).
- Demand evidence: **7** — Earned by **indirect** evidence (rule: up to 7 on its own): Delphi's **$16M Sequoia Series A** on exactly the AI-expert-clone premise (SIG-09, verified), **JustAnswer**'s real credential-gated paid-answer market (SIG-16), and four-figure WTP for a *specific named expert* (SIG-03 — Intro $776–$5k, Nikita Bier $122.3k/95 bookings; SIG-12). **Capped at 7 by the direct-evidence ceiling, not by disconfirmers** — there is no direct target-persona evidence of paying for an expert's **AI agent** (all direct demand is for the human, or is a competitor company claim). SIG-05 and SIG-11 **no longer dock this score** (reclassified to Defensibility and Market-size edge); SIG-10 is a supply-side rejection filed under Distribution.
- Willingness to pay: **7** — **Indirect** evidence (rule: up to 7): JustAnswer proves durable **recurring** WTP at ~$46–55/mo — *above* Avee's $20–25 (SIG-16); Intro proves four-figure WTP for a specific expert (SIG-03). Capped at 7 by the **direct-evidence ceiling** (the human-vs-AI delivery difference is the biggest unknown, and no direct evidence shows the AI version is paid for). SIG-05/SIG-11 do **not** lower this under the new rule (current-user quality and boundary respectively). The deliverables premium over Gamma/Beautiful.ai is **unknown (inference)**, scored neither up nor down.

*Desirability average: (8+7+7)/3 = 7.33 → **7**. (Pain rose 7→8; the dimension still rounds to 7.)*

**Viability — 6**
- Market size & growth: **7** — Containing creator economy is large and growing (~$234–324B 2026, double-digit CAGR, research §1). The specific AI-expert-agent sub-market is **publicly unsized** (research §1; SIG "found nothing") — an **unknown (neutral), not a drag**. The funded incumbent (Delphi, SIG-09) and the proven credential-gated market (JustAnswer, SIG-16) are strong **indirect** evidence the market is real (up to 7). **SIG-11 is the boundary that tempers it:** a real segment wants "the real person," which is one reason Market size sits at 7 rather than pushing toward 8 — and, lacking direct evidence, 7 is the indirect ceiling anyway.
- Monetization & unit economics: **7** — Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** (revenue-model §3), not the ~$3–5 the superseded bundle framing implied. Platform keeps a structural ~40–45% of gross with the cap. For *small / audience-less* experts Avee clearly beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06). Held below 8 because experts who set and collect their *own* price on Delphi (~85%) / Patreon (~90%) still keep more per subscriber at scale (research §3). Payout **acceptance** is an **unknown** logged below, not a drag here.
- Defensibility / moat: **5** — **The home the new rule assigns to the competitor quality complaints.** Pro-moat / opportunity: SIG-05 (Delphi clones feel generic) and SIG-07 (billing-trust complaints) are, under the rule, **evidence for a better entrant** — Avee's RAG + semantic memory, credential-first trust (attacks SIG-13, no structured credentials), EU/GDPR posture (SIG-14), and a transparent public earnings dashboard are the differentiated response. Automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard; user-centric payout is fraud-resistant and validated (SoundCloud Fan-Powered Royalties, research §5). Anti-moat: Delphi is Sequoia-funded and could add a credential layer; the deliverable renderer sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment. These net to a genuine two-sided **5** — the quality complaints are an **opportunity to capture demand**, not yet a durable moat.
- Distribution path: **6** — Judged on channel plausibility, never traction. A reachable, low-CAC channel exists: the **expert-led sharing loop** (each expert shares their own agent with their own audience, with a direct financial interest and a 10% referral bonus, revenue-model §4) — a built-in growth loop (thesis preference) into nameable communities (r/coaching, r/consulting, Intro, MentorCruise — SIG-01/03/18). Held at 6, not higher, because this is where the **genuine supply-side frictions** now live: **SIG-10** (some credible target-suppliers refuse — full weight on the supply-pull question, tempered by the split and the pedigree wedge), **SIG-18** (audience-less professionals don't fit "bring your own audience"), and the **GPT Store precedent** (usage-based AI payouts stayed invite-only and paid most builders $0, research §7). The channel is plausible; supply **conversion** is the open risk.
- Timing ("why now"): **6** — The whitespace is open *now*: Delphi raised $16M but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Enabling tech (RAG + memory + cheap routing) and payout rails (Stripe Connect) are commoditized. Counterweight (genuine, observer): GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

*Viability average: (7+7+5+6+6)/5 = 6.2 → **6**.*

**Feasibility — 7** *(judged intrinsically for a small technical team, not against this founder's runway)*
- Technical complexity: **7** — A RAG/memory/multi-model agent platform with a usage-attribution payout layer is within a small technical team's reach; Avee V2 v0.6.0 (incl. image/video/voice) already exists as proof the stack is tractable. The novel hard part — **automated credential/employment verification** — is load-bearing and partly outside standard agent work, which keeps this below 8.
- Capital intensity: **7** — Intrinsically capital-light: software on cheap, routed inference, commoditized Stripe Connect rails, no hardware/inventory. The fair-use cost cap + media-on-credits keep per-user cost below price (revenue-model §3). Third-party credential/identity verification and metered inference are the only real recurring costs.
- Time to testable MVP: **7** — The product exists; the billing/payout layer is a bounded build and demand is testable with lightweight verification of a handful of experts — weeks, not months.
- External dependencies: **5** — The genuine drag: Stripe Connect (KYC, DAC7/1099, chargebacks, 45-day holds), mobile-IAP avoidance, credential-verification dependencies (Europass, LinkedIn/work-email, employer policy for current employees), and K7 expert-advice **plus** deliverable-attribution liability — several outside the team's control. Neutral 5.

*Feasibility average: (7+7+7+5)/4 = 6.5 → **7**.*

**Composite (idea score):** `0.40×7 + 0.35×6 + 0.25×7` = **6.65**

**Gate checklist**
- G1 — Thesis (no kill rule fires): **Pass** — no K1–K7 fires (table above); K5/K6 retired as kills. K2/K7 conditional on automated, conservative verification and honest deliverable framing.
- G2 — Founder–target distance: **2 — Cold but mapped** — the founder is not the persona and has no warm network in it (founder-profile: AI/agent-dev and indie-hacker communities; "named no expert segment and no privileged access"), but the persona gathers in **known, open public channels** (r/consulting, r/coaching, r/freelance, Skool, Intro, MentorCruise — SIG-01/03/18). Not distance 1 (credentialed professionals are not the founder's own crowd); not distance 3 (channels are public, no gatekeeper). Route to the first 10: cold outreach into one named niche over 4 weeks. Distance 2 does **not** block Advance, and the G3 test is runnable via exactly this plan.
- G3 — Riskiest assumption testable in ≤ 4 weeks: **Pass** — riskiest assumption = *will an expert's own audience pay $20–25/mo for that expert's AI agent (not the human), and will a credentialed expert publish one for ~$7.96–9.55/engaged sub rather than keep ~85–90% of a self-set price elsewhere?* Testable on the existing product in ≤ 4 weeks at distance 2: cold-recruit 3–5 credentialed experts from one niche, publish credential-fronted agents with one paid deliverable, pre-sell their audiences the one-to-one subscription.
- G4 — Idea strength (≥ 7.5 Advance, < 6.0 Park): **6.65** — Iterate band. **This is the single deciding check.**

**Recommendation (advisory; the founder decides):** **Iterate** — G1 passes, G2 distance is 2 (≤ 2, does not block), G3 passes and its test is runnable at distance 2; the **only** thing short of the Advance band is **G4 (composite 6.65 < 7.5)**. Composite ≥ 6.0 and no kill fires, so it is not in the Park band. The one move that lifts it into Advance is to run the G3 experiment and convert the AI-delivery and payout-acceptance **unknowns** into evidenced demand.
**Biggest unknown:** Will an expert's own audience pay a recurring subscription for that expert's **AI agent** (or an AI-made deck in their style), not the human — and will credentialed experts accept **~$7.96–9.55 per engaged subscriber** (40–48% of a platform-set price) over keeping ~85–90% of a self-set price elsewhere? Strong indirect evidence (Delphi Sequoia round, JustAnswer, Intro) shows the market and the price are real; these two AI-delivery/payout-acceptance leaps are the open questions. Note the honest asymmetry the new rule surfaces: **SIG-05 (a competitor's user calling the clone generic) is now read as opportunity for a better entrant, not as proof demand is absent** — but it still sets the bar Avee's AI must clear; and **SIG-11 ("I want the real person") sizes the market's edge, not the demand inside it.** The one genuine target-persona rejection, **SIG-10**, is a **supply-side** risk (will experts publish), weighed at full weight there.
**De-risking step:** Pick one named credentialed niche the founder can cold-reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18 — the distance-2 route), recruit 3–5 to publish credential-fronted agents with one paid deliverable, and pre-sell their existing audiences the one-to-one subscription. This single test captures both halves of the biggest unknown (audience WTP for AI delivery **and** expert payout acceptance) and demonstrates the distance-2 route works.
**For the founder:** The score is unchanged from v4 (6.65) and that is the honest outcome of the new "weigh evidence by who says it" rule — but *why* it sits at 6.65 is now cleaner. In v4 I was docking your Demand and WTP with three signals that, on inspection, don't belong there: a Delphi **user** saying the clone feels generic (SIG-05) is really a complaint about *Delphi's* execution — if anything it is an opening for a better-built agent, and it now sits under Defensibility; "I want the real person" (SIG-11) comes from people **outside** your buyer persona and only marks the market's edge; and the expert who refused to clone (SIG-10) is a **supply-side** objection about recruiting experts, not about whether buyers want this. Moving them to their right homes did **not** raise the score, because the real ceiling on Demand and WTP is that all your hard evidence is for the **human** expert or is a competitor's own revenue claim — strong *indirect* evidence (worth a 7) but **no direct proof yet that people pay for the AI version**. That is the gap, and it is exactly what one pre-sell test resolves. **What would move it up:** real subscribers paying for an expert's **AI** agent and ≥3 credentialed experts opting in at the usage-share terms (that is the **direct** evidence that lets Demand/WTP pass 7 and carries the composite toward Advance); evidence the deliverables command a premium over Gamma/Beautiful.ai; a signal that experts prefer usage-share to a self-set price. **What would move it down:** a pre-sell that converts no AI-delivery subscribers, credentialed experts declining the share in favour of self-set-price platforms, or credential verification proving un-automatable at acceptable accuracy (which would also threaten K2/K7).

---

## Changes vs previous scorecards (v1: 5.1 Park → v2: 5.9 Park → v2.1: 6.25 Iterate → v3: 6.25 Iterate → v4: 6.65 Iterate → **v5: 6.65 Iterate**)

The idea score is **unchanged at 6.65**. **No evidence changed since v4** — same
signals, research and corrected payout. The single new rule ("weigh evidence by
who says it") **re-files** the disconfirming evidence; it does not move the
composite, which is the correct, non-inflating result.

| Dimension | v4 | v5 | What moved and why |
|---|---|---|---|
| Desirability | 7 (Pain 7, Demand 7, WTP 7) | **7** (Pain **8**, Demand 7, WTP 7) | **[rule]** Pain 7→8: v4 held Pain at 7 using SIG-05 and SIG-11 as brakes; the new rule reclassifies SIG-05 (competitor **current-user quality**) and SIG-11 (**boundary**) away from demand, so **direct** supply-side painkiller evidence (SIG-01) lifts Pain above 7. Demand and WTP **stay at 7** — the v4 story ("disconfirmers cap them") is corrected to "the **direct-evidence ceiling** caps them; indirect evidence earns the 7, and no direct demand evidence exists to exceed it." Dimension average 7.0 → 7.33, still rounds to **7**. |
| Viability | 6 (Market 7, Monet. 7, Moat 5, Distribution 6, Timing 6) | **6** (same sub-scores) | **[rule]** No numeric change, three re-filings: SIG-05/SIG-07 (competitor quality) now sit in **Defensibility** as *opportunity* (evidence for a better entrant) — they do not raise it to a moat, so 5 holds; SIG-11 (boundary) is now the explicit reason **Market size** sits at 7 not 8; SIG-10 (supply rejection) + SIG-18 now sit in **Distribution** as the supply-conversion risk, which 6 already reflected. Average 6.2 → **6**. |
| Feasibility | 7 (7/7/7/5) | **7** (7/7/7/5) | **[—]** Untouched by the rule. |
| Composite | 6.65 | **6.65** | **[rule]** Pain 7→8 lifts Desirability's average but not its rounded value (7), and Viability/Feasibility are unchanged, so the composite holds. The new rule corrected *where* evidence is counted, not *how much* net evidence there is. |
| Recommendation basis | Advisory; G1–G4; Iterate via G4 (6.65<7.5) | **Advisory; G1–G4; Iterate via G4 (6.65<7.5)** | **[—]** Same band. G1 passes, G2 distance 2, G3 passes; the only thing short of Advance is G4. Thresholds unchanged. |

**Honest note on not inflating.** v5 **removes an improper drag** on Demand/WTP
(SIG-05/10/11 were mis-filed as demand evidence in v4) — and the score **still does
not rise**, because the genuine, independent cap is the "above 7 needs direct
evidence" rule, and that direct demand evidence does not yet exist. The only
sub-score to move (Pain 7→8) is itself gated by **direct** evidence (SIG-01) and
is transparent about not changing the dimension's rounded value. The practical
read — Iterate, run the one pre-sell test — is unchanged. Equally, v5 does **not
drop** the one genuine target-persona rejection: SIG-10 keeps full weight on the
supply-side question, where it honestly belongs.

---

## Revenue model verdict (revenue-model.md §7 v1 spec) — unchanged, retained

**What holds (strong):**
- **The margin is structural, not hopeful.** 50% of net contribution P = max(N − C, 0) keeps the platform at ~40–45% of gross on every subscriber (§3), fixing the §2 contradiction where paying creators out of *gross* goes negative on heavy users.
- **The fair-use cost cap + media-on-credits is what makes K4 true** and absorbs the deliverables cost (decks/images on credits, cost × 2). Keep it non-negotiable.
- **Fraud resistance is the model's best property and it is evidenced** — user-centric attribution makes self-dealing and collusion lose money (SoundCloud Fan-Powered Royalties, research §5). Do not switch to a pooled model.
- **Ops stay solo-operable** via Stripe Connect Express, 45-day holds, $25 minimum payout (K2) — conditional on credential verification staying automated.

**The corrected creator economics (carried forward):**
- Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** — not ~$3–5. The ~$3–5 band applies **only** to cross-traffic from other experts' subscribers.
- **The "≥ $5" promise is met at a plain $20** at ~100% own-audience usage; the earlier "needs $24.99 or a 60% split" caveat was an artefact of the superseded 50%-usage bundle math. Drop it.
- **The "central competitive headwind" is materially weaker.** Avee still pays less per sub than *self-set-price* alternatives for big experts (~85–90%), but beats Delphi outright for small/audience-less experts (Delphi is a $79–299/mo cost with no built-in monetization, SIG-06), and ~40–48% of a platform-set price with inference, agent and deliverables included is a defensible offer.

**What is still weak (evidence confirms, not relieves):**
- **The AI-delivery demand leap is unproven** — but note the v5 re-reading: SIG-05 is a *competitor quality* complaint (the bar Avee must clear, and an opening), not proof demand is absent; SIG-11 marks the market's *edge*. The leap is an **unknown to test**, not disconfirmed.
- **Payout acceptance is unproven** — no signal shows experts choosing a ~40–48% usage share over keeping ~85–90% of a self-set price; SIG-10 (a genuine target-supplier rejection) sharpens this as the dominant **supply-side** open question.
- **Long-tail payout friction** — $25 minimum + ~$2/account/month Stripe fees mean audience-less experts (SIG-18) net ~$0 until discovery traffic exists.

**Single change that would most raise the score:** Lead the creator pitch with the
corrected own-audience economics (**~$8–9.55/engaged sub at $20, no monthly fee,
infra + deliverables included**) plus the small-expert wedge where Avee beats
Delphi (SIG-06), and a high-share private-agent / paid-escalation / paid-deliverable
layer (expert keeps ~80%). That attacks the real open risk — payout **acceptance**
(SIG-10), not payout *size*.

---

## Top recommendation

There is one idea this run. **IDEA-01 is Iterate (advisory) at composite 6.65**
(idea score, for ranking only) — unchanged from v4. The new "weigh evidence by who
says it" rule **re-filed** the disconfirming evidence without moving the number:
SIG-05 (competitor **current-user quality**) → Defensibility/opportunity; SIG-11
(**boundary**) → Market-size edge; SIG-10 (**target-supplier rejection**) →
supply-side cold start. None of those should have docked Demand or WTP, and
removing them still did not raise the score, because the genuine cap is the
**direct-evidence ceiling** (strong indirect evidence earns a 7; no direct proof
yet that people pay for the AI version). **G1** passes, **G2** reads distance **2
(Cold but mapped)** which does not block Advance, and **G3** passes with a test
runnable at that distance — so the only thing short of the Advance band is **G4,
the idea's own strength (6.65 < 7.5)**.

**Highest-priority validation step:** commit to **one** named credentialed niche
and cold-reach 10 of the persona this week (e.g. independent consultants in
r/consulting, SIG-18 — the distance-2 route), recruit **3–5 experts** to publish
credential-fronted agents with one paid deliverable, and **pre-sell their existing
audiences** the one-to-one $20–25 subscription. One test resolves the deciding
unknowns at once — whether an audience pays for **AI** delivery (the direct
evidence that would let Demand/WTP pass 7) and whether experts accept the
~$7.96–9.55/engaged-sub payout (the SIG-10 supply question). A positive result
points toward Advance; a negative one toward Park. The founder decides what to do
with that read.
