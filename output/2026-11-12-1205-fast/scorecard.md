# Scorecard — run 2026-11-12-1205-fast (v6, re-scored under the "ideation, not P/S Fit" calibration)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage**
> under one newly-added governance rule: **"This is ideation, not P/S Fit."** The
> evidence base is identical to v5 (same `signals.md`, same `market-research.md`,
> same `revenue-model.md`, same corrected one-to-one payout, same
> `founder-profile.md`). What changed is the calibration the rule imposes.
>
> **Governance advises; the founder decides.** The ranking and the checklist are
> reasons to learn from, not a verdict on what may be pursued. The gate line is an
> **advisory Recommendation**, and the card closes with a **For the founder** note
> on why it lands where it does and what evidence would move it.
>
> **What changed since v5 — the one new rule**
>
> "This is ideation, not P/S Fit." Proof that customers pay for *this* product is
> what P/S Fit produces; at the idea stage it isn't expected, isn't required, and
> **no longer sets a ceiling**. The full 0–10 range is now calibrated on the
> **strength, independence and convergence of the evidence available at the idea
> stage** — funded/revenue-making competitors in the same job, adjacent paid
> markets, verbatim target pain, dated platform/regulatory shifts:
> - **9–10:** several independent sources converge (funded competitor with
>   revenue in the same job + an adjacent paid market + first-hand target pain +
>   a dated why-now), with **no full-weight disconfirming evidence**.
> - **7–8:** two or more independent, strong sources point the same way.
> - **5–6:** a single source or analogy, or no evidence either way (unknown).
> - **Below 5:** credible full-weight disconfirming evidence.
>
> The v5 "weigh evidence by who says it" rule is retained: a quote only counts
> **against** an idea at full weight when it is a `rejection` from a
> **target-buyer** about the job the idea does. The source-classification table
> below is carried forward unchanged.
>
> **The headline:** the idea score rises from **6.65 → 7.05**, entirely because
> the removed ceiling frees **Demand (7 → 8)** and **WTP (7 → 8)** to be scored on
> convergence. In v5 I stated plainly that the *binding* cap on those two
> sub-scores was the "above 7 needs **direct** evidence" ceiling — not the
> disconfirmers, which the v5 rule had already moved off demand. With that ceiling
> gone, the honest question is only: **how many independent, strong idea-stage
> sources converge?** For paying to access a specific expert's knowledge on
> demand, several do — a **funded competitor in the same job** (Delphi, $16M
> Sequoia Series A), an **adjacent recurring paid market priced *above* Avee**
> (JustAnswer ~$46–55/mo, credential-gated), a **premium adjacent market** (Intro
> $776–$5k for a named expert), and a **functioning paid-AI-message market** (Poe)
> — with **no full-weight target-buyer rejection** against demand. That is the
> 7–8 band (two or more strong independent sources), and it sits at **8**. It does
> **not** reach 9 — and I am deliberately not inflating it there — because the
> evidence on the *exact* job (paying for an expert's **AI agent** at a
> platform-set price and split) rests on a **single** funded competitor whose own
> revenue is unverified first-party/press (SIG-12), with the rest being adjacent
> markets for the **human** expert. Same discipline on WTP: recurring,
> credential-gated WTP *above* Avee's price (JustAnswer) plus premium WTP (Intro)
> is a solid **8**, not a 9, because the proven recurring money is for the human /
> self-set price, and the AI-at-this-split leap is the open P/S-Fit question.
>
> **Pain intensity stays at 8** (it was already above the old ceiling, lifted in
> v5 by direct supply-side pain SIG-01). **Viability (6) and Feasibility (7) are
> untouched** — none of their sub-scores were ceiling-bound. Desirability's
> average therefore moves from 7.33 (→7) to **8.0 (→8)**, and the composite moves
> **6.65 → 7.05**. **Thresholds were not lowered; the move is only what the
> convergence bands honestly support.** 7.05 is still **below the 7.5 Advance
> line** — the recommendation stays **Iterate**, now one good experiment away from
> Advance.
>
> Corrected creator payout carried forward unchanged (one-to-one own-audience
> usage, revenue-model §3): **~$7.96 at $20 (40% of price), ~$9.55 with the 10%
> referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)**. The old "~$3–5" applies
> **only** to incidental cross-traffic from other experts' subscribers.
>
> Weights: **Composite = 0.40×D + 0.35×V + 0.25×F** (CLAUDE.md default). Gate bands
> (advisory): Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (never lowered). Evidence
> base: `signals.md` (18 signals), `market-research.md` (confidence: **Medium**),
> `revenue-model.md` (v1 spec §7), `founder-profile.md`.

## Disconfirming evidence — classified by who says it (carried forward from v5)

`signals.md` predates source-role tags, so each signal that cuts against the idea
is classified here by **source role** and **kind**, with the weight the rule
assigns and where it lands. Unchanged from v5; the new calibration does not move
any of these classifications.

| Signal | What it says (against the idea) | Source role | Kind | Weight under the rule | Lands in |
|---|---|---|---|---|---|
| **SIG-05** | Delphi clone "sounds just like a normal chatgpt chat … no real reason to use this" | **current-user** of competitor (Delphi) | **quality** | **Context / opportunity** — never a Demand/WTP drag; evidence *for* a better entrant | Defensibility + biggest unknown |
| **SIG-11** | Audiences: "it feels fake," **"I want the real person"** | **non-target / boundary** (people who reject AI substitution — outside the AI-agent-buyer persona) | **boundary** | **Context** — sizes the market's edge; tempers **Market size** slightly; does **not** lower demand inside the target | Market size (edge) + biggest unknown |
| **SIG-10** | Respected writer refuses to clone — "founded on predation" | **target-supplier** (a potential supply-side expert) | **rejection** (supply-side, ethics-grounded) | **Full weight on the supply-pull / cold-start question** (genuine target-supplier), tempered by the documented split (many experts *do* build) and wedge-fit (pedigree-first, name-optional). **Not** a demand/WTP drag | Distribution (cold start) + Defensibility + biggest unknown |
| **SIG-07** | Delphi "scammers … charged my card … without notice" | **current-user** of competitor | **quality** (billing/trust) | **Context / opportunity** — transparent public earnings dashboard + clear billing is Avee's differentiator | Defensibility (opportunity) |
| **SIG-18** (counter) | Audience-less professionals want to earn **without** building an audience — in tension with "expert brings own audience" | **target-supplier** | **boundary** (defines which suppliers fit the one-to-one model) | **Context** — real supply sub-segment that needs platform-supplied discovery | Distribution + biggest unknown |
| **SIG-12** (counter) | Clone earnings concentrate in 100k+ audiences; long tail earns little; Delphi revenue is first-party/press | **observer** (market structure) | **boundary** (supply economics edge) | **Context** — defines who the payout economics work for; also why Demand sits at 8 not 9 | Distribution + Demand caveat |
| **SIG-01** (counter) | Same capacity-capped coach's *fix* was systems/automation, not an AI clone | **target-supplier** | **quality** (solution-fit, not pain severity) | **Context** — solution-fit question, not a pain-intensity drag | Biggest unknown |
| GPT Store (research §7) | Usage-based AI-creator payouts stayed invite-only; most builders earned **$0** | **observer** (platform precedent) | **quality / boundary** | **Genuine disconfirming** on usage-based AI payouts — a real platform-outcome precedent, kept weighted | Distribution + Timing |

**Why no full-weight disconfirming lands on Demand or WTP.** The only kind that
docks Demand/WTP at full weight is a **`rejection` from a target-buyer** about
this job. There is none in `signals.md`: SIG-05 is a competitor **current-user
quality** complaint (→ Defensibility/opportunity), SIG-11 is a **boundary** from
people **outside** the AI-agent-buyer persona (→ Market-size edge), and SIG-10 is
a **target-supplier** rejection (→ Distribution/cold start). So with the
ceiling removed, Demand and WTP are scored purely on the **strength and
convergence of the supporting evidence**, with no full-weight brake — which is
exactly why they move to 8.

## Evidence flag (thesis.md, recorded — never a kill)

- **First-hand target pain:** dated, fetched-verbatim **pain** on the supply side
  — SIG-01 (Ken Deng, DEV, Mar 6: "I'd run out of time"; "a waitlist of 20+ …
  adding even one more would break me"), SIG-02 (Josh Spector). Carries **Pain
  intensity at 8**.
- **Funded competitor in the same job:** **Delphi $16M Sequoia Series A, ~$18.7M
  total** (SIG-09, verified) on exactly the AI-expert-clone premise. Under the new
  calibration this is strong same-job evidence the market and demand are real; the
  AI-vs-human and model differences are a **Defensibility / biggest-unknown**
  question, not a demand discount.
- **Adjacent paid markets (recurring + premium):** **JustAnswer** credential-gated
  recurring paid Q&A at **~$46–55/mo — above Avee's $20–25** (SIG-16); **Intro**
  four-figure WTP for a specific named expert (SIG-03); **Poe** functioning
  paid-per-message AI market (research §2). Together with Delphi these are the
  independent, converging sources that carry **Demand = 8** and **WTP = 8**.
- **Unknown (to test in P/S Fit, not a penalty, scored neutral):** recurring WTP
  for an **AI** agent of a credentialed expert (vs the human); whether
  credentialed experts **accept** a ~40–48% usage share over keeping ~85–90% of a
  self-set price; the deliverables premium over Gamma/Beautiful.ai; the specific
  AI-expert-agent **market size** (publicly unsized).
- **Disconfirming, correctly filed (carried from v5):** SIG-05 →
  Defensibility/opportunity; SIG-11 → Market-size edge; SIG-10 → supply-side cold
  start; GPT Store → Distribution/Timing. **None dock Demand or WTP.**

## Kill-rule check (thesis.md K1–K7) — feeds gate check G1

Checked **before** scoring. A broken rule forces **Park** (G1 fail) regardless of
composite. **K5 and K6 are retired as kills** (thesis.md). No change from v5.

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
| 1 | IDEA-01 | Avee: expert agents paid by usage | 8 | 6 | 7 | 7.05 | Iterate | 2 |

*The "Gate" column is the advisory **Recommendation**, not a verdict — the founder
decides.*

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 7.05  ·  Recommendation: Iterate

> The composite is the **idea score**, used for ranking only. The recommendation is
> advisory — the founder decides. Missing traction never lowers a score.

**Desirability — 8**
- Pain intensity: **8** — Direct, dated, fetched-verbatim painkiller pain on the supply side: the capacity-capped expert turning away paying demand (SIG-01, strong — "I had a waitlist of 20+ … adding even one more would break me"), the repeat-question grind (SIG-02), plus demand-side pain for credentialed answers now (SIG-16, SIG-17). Multiple independent sources converge on "painkiller, not vitamin." Held at 8, not 9, because the demand-side pain for the **AI** version specifically is indirect, and SIG-01's own counter (the author's fix was automation, not a clone) is a live **solution-fit** question (logged in the biggest unknown). No full-weight disconfirming on pain severity.
- Demand evidence: **7 → 8** — **[rule-moved; the removed ceiling is the whole move.]** Calibrated on convergence: a **funded competitor in the same job** (Delphi, $16M Sequoia Series A on the AI-expert-clone premise, SIG-09 verified), an **adjacent recurring paid market** (JustAnswer credential-gated Q&A, SIG-16), a **premium adjacent market** for a specific named expert (Intro $776–$5k; Nikita Bier $122.3k/95 bookings, SIG-03/12), and a **functioning paid-AI-message market** (Poe ~$30–65M, research §2). That is four independent, strong-to-medium sources pointing the same way — squarely the **7–8 band** — with **no full-weight target-buyer rejection** against demand (SIG-05 = competitor quality → Defensibility; SIG-11 = boundary → Market edge; SIG-10 = supply-side → Distribution). Scored **8**, not 9, because the evidence on the *exact* job (paying for an expert's **AI agent**) rests on a **single** funded competitor whose own revenue is unverified first-party/press (SIG-12), with the rest being adjacent markets for the **human** expert.
- Willingness to pay: **7 → 8** — **[rule-moved.]** **JustAnswer** proves durable **recurring** WTP at ~$46–55/mo — *above* Avee's $20–25 — gated behind verified credentials, the closest adjacent proof (SIG-16, strong). **Intro** proves four-figure WTP for a specific expert (SIG-03, strong). Delphi's creator-set memberships and Patreon/Substack recurring plans corroborate recurring WTP for creator access. Two-plus independent strong sources converge → **8**. Held at 8, not 9, because the proven recurring money is for the **human** / a self-set price, and whether the same buyers pay recurring for the **AI** version at Avee's platform-set price and split is the biggest unknown (a P/S-Fit question, not a ceiling). The deliverables premium over Gamma/Beautiful.ai is **unknown**, scored neither up nor down.

*Desirability average: (8+8+8)/3 = 8.0 → **8**. (Demand and WTP each rose 7→8 once the direct-evidence ceiling was removed and they were re-scored on convergence.)*

**Viability — 6**
- Market size & growth: **7** — The containing creator economy is large and growing (~$234–324B in 2026, double-digit CAGR, research §1 — directional, single-aggregator caveat). The specific AI-expert-agent sub-market is **publicly unsized** (research §1; signals "found nothing") — an **unknown (neutral), not a drag**. The funded incumbent (Delphi, SIG-09) and the proven credential-gated market (JustAnswer, SIG-16) are strong evidence the market is real. Held at **7**, not 8, because the binding constraint here is **not** the removed ceiling but the genuinely **unsized specific sub-market** (a neutral-5 component) and the directional softness of the size figures; **SIG-11 is the boundary** that tempers the edge (a real segment wants "the real person"). Honest: this is the one Viability sub-score people might expect to rise with the ceiling gone, and it does not, because its cap was always the unsized niche, not the ceiling.
- Monetization & unit economics: **7** — Under the corrected one-to-one model, an engaged own-audience subscriber earns the expert **~$7.96 at $20 (40%), ~$9.55 with the referral bonus (48%), ~$10.36–12.43 at $24.99 (41–50%)** (revenue-model §3), not the ~$3–5 the superseded bundle framing implied. Platform keeps a structural ~40–45% of gross with the cap. For *small / audience-less* experts Avee clearly beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06). Held below 8 because experts who set and collect their *own* price on Delphi (~85%) / Patreon (~90%) still keep more per subscriber at scale (research §3). Payout **acceptance** is an **unknown** logged below, not a drag here.
- Defensibility / moat: **5** — The home for the competitor quality complaints. Pro-moat / opportunity: SIG-05 (Delphi clones feel generic) and SIG-07 (billing-trust complaints) are **evidence for a better entrant** — Avee's RAG + semantic memory, credential-first trust (attacks SIG-13, no structured credentials), EU/GDPR posture (SIG-14), and a transparent public earnings dashboard are the differentiated response. Automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard; user-centric payout is fraud-resistant and validated (SoundCloud Fan-Powered Royalties, research §5). Anti-moat: Delphi is Sequoia-funded and could add a credential layer; the deliverable renderer sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment. These net to a genuine two-sided **5**.
- Distribution path: **6** — Judged on channel plausibility, never traction. A reachable, low-CAC channel exists: the **expert-led sharing loop** (each expert shares their own agent with their own audience, with a direct financial interest and a 10% referral bonus, revenue-model §4) — a built-in growth loop (thesis preference) into nameable communities (r/coaching, r/consulting, Intro, MentorCruise — SIG-01/03/18). Held at 6, not higher, because this is where the **genuine supply-side frictions** live: **SIG-10** (some credible target-suppliers refuse — full weight on the supply-pull question, tempered by the split and the pedigree wedge), **SIG-18** (audience-less professionals don't fit "bring your own audience"), and the **GPT Store precedent** (usage-based AI payouts stayed invite-only and paid most builders $0, research §7). The channel is plausible; supply **conversion** is the open risk.
- Timing ("why now"): **6** — The whitespace is open *now*: Delphi raised $16M but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Enabling tech (RAG + memory + cheap routing) and payout rails (Stripe Connect) are commoditized. Counterweight (genuine, observer): GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

*Viability average: (7+7+5+6+6)/5 = 6.2 → **6**. (Unchanged — none of these sub-scores was ceiling-bound.)*

**Feasibility — 7** *(judged intrinsically for a small technical team, not against this founder's runway)*
- Technical complexity: **7** — A RAG/memory/multi-model agent platform with a usage-attribution payout layer is within a small technical team's reach; Avee V2 v0.6.0 (incl. image/video/voice) already exists as proof the stack is tractable. The novel hard part — **automated credential/employment verification** — is load-bearing and partly outside standard agent work, which keeps this below 8.
- Capital intensity: **7** — Intrinsically capital-light: software on cheap, routed inference, commoditized Stripe Connect rails, no hardware/inventory. The fair-use cost cap + media-on-credits keep per-user cost below price (revenue-model §3). Third-party credential/identity verification and metered inference are the only real recurring costs.
- Time to testable MVP: **7** — The product exists; the billing/payout layer is a bounded build and demand is testable with lightweight verification of a handful of experts — weeks, not months.
- External dependencies: **5** — The genuine drag: Stripe Connect (KYC, DAC7/1099, chargebacks, 45-day holds), mobile-IAP avoidance, credential-verification dependencies (Europass, LinkedIn/work-email, employer policy for current employees), and K7 expert-advice **plus** deliverable-attribution liability — several outside the team's control. Neutral 5.

*Feasibility average: (7+7+7+5)/4 = 6.5 → **7**. (Unchanged.)*

**Composite (idea score):** `0.40×8 + 0.35×6 + 0.25×7` = **7.05**

**Gate checklist**
- G1 — Thesis (no kill rule fires): **Pass** — no K1–K7 fires (table above); K5/K6 retired as kills. K2/K7 conditional on automated, conservative verification and honest deliverable framing.
- G2 — Founder–target distance: **2 — Cold but mapped** — the founder is not the persona and has no warm network in it (founder-profile: AI/agent-dev and indie-hacker communities; "named no expert segment and no privileged access"), but the persona gathers in **known, open public channels** (r/consulting, r/coaching, r/freelance, Skool, Intro, MentorCruise — SIG-01/03/18). Not distance 1 (credentialed professionals are not the founder's own crowd); not distance 3 (channels are public, no gatekeeper). Route to the first 10: cold outreach into one named niche over 4 weeks. Distance 2 does **not** block Advance, and the G3 test is runnable via exactly this plan.
- G3 — Riskiest assumption testable in ≤ 4 weeks: **Pass** — riskiest assumption = *will an expert's own audience pay $20–25/mo for that expert's AI agent (not the human), and will a credentialed expert publish one for ~$7.96–9.55/engaged sub rather than keep ~85–90% of a self-set price elsewhere?* Testable on the existing product in ≤ 4 weeks at distance 2: cold-recruit 3–5 credentialed experts from one niche, publish credential-fronted agents with one paid deliverable, pre-sell their audiences the one-to-one subscription.
- G4 — Idea strength (≥ 7.5 Advance, < 6.0 Park): **7.05** — Iterate band. **This is the single deciding check**, and it is now only 0.45 short of Advance (was 0.85 short in v5).

**Recommendation (advisory; the founder decides):** **Iterate** — G1 passes, G2 distance is 2 (≤ 2, does not block), G3 passes and its test is runnable at distance 2; the **only** thing short of the Advance band is **G4 (composite 7.05 < 7.5)**. Composite ≥ 6.0 and no kill fires, so it is not in the Park band. The single move that lifts it into Advance is to run the G3 experiment and convert the two AI-delivery/payout-acceptance **unknowns** into evidenced demand — which, under the new calibration, is exactly the evidence that would push Demand/WTP toward 9 and carry the composite over 7.5.
**Biggest unknown:** Will an expert's own audience pay a recurring subscription for that expert's **AI agent** (or an AI-made deck in their style), not the human — and will credentialed experts accept **~$7.96–9.55 per engaged subscriber** (40–48% of a platform-set price) over keeping ~85–90% of a self-set price elsewhere? The convergent idea-stage evidence (Delphi's Sequoia round, JustAnswer's recurring credential-gated WTP *above* Avee's price, Intro's premium) now shows the market, the recurring behaviour and the price are real — strong enough to carry Demand/WTP to 8. The two remaining leaps — **AI delivery** and **payout acceptance** — are what P/S Fit exists to resolve. Note the honest asymmetry the source rule surfaces: **SIG-05** (a competitor's user calling the clone generic) is read as opportunity for a better entrant and the bar Avee's AI must clear, **not** proof demand is absent; **SIG-11** ("I want the real person") sizes the market's edge, not the demand inside it; and the one genuine target-persona rejection, **SIG-10**, is a **supply-side** risk, weighed at full weight there.
**De-risking step:** Pick one named credentialed niche the founder can cold-reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18 — the distance-2 route), recruit 3–5 to publish credential-fronted agents with one paid deliverable, and pre-sell their existing audiences the one-to-one subscription. This single test captures both halves of the biggest unknown (audience WTP for AI delivery **and** expert payout acceptance) and demonstrates the distance-2 route works.
**For the founder:** The score rose from 6.65 to **7.05**, and the reason is a single rule change, not new evidence. Until now I was holding your Demand and your Willingness-to-pay at exactly 7 because of an old rule that said anything above 7 needed *direct* proof that people pay for **this** product — proof that, by definition, only comes from launching. That rule is gone: at the idea stage you are judged on how much strong, independent evidence points the same way, and for "people pay to reach a specific expert's knowledge on demand" a lot does — a **Sequoia-funded competitor doing exactly this** (Delphi), a **recurring paid service priced higher than you** gated behind verified credentials (JustAnswer at ~$46–55/mo), **four-figure cheques for a single named expert** (Intro), and a **working paid-per-message AI market** (Poe). Four independent sources, no target-buyer actually rejecting the job — that is an 8 on both, and it lifts your Desirability to 8. I stopped there, not at 9, on purpose: every one of those proofs is either for the **human** expert or is Delphi's **own unverified** revenue claim, so the precise thing you are betting on — that an audience pays recurring for the **AI** version at your price and split — is still the unproven leap. **What would move it up:** real subscribers paying for an expert's **AI** agent and ≥3 credentialed experts opting in at the usage-share terms (that single result is what pushes Demand/WTP toward 9 and carries the composite over 7.5 into Advance); evidence the deliverables command a premium over Gamma/Beautiful.ai; a signal that experts prefer usage-share to a self-set price. **What would move it down:** a pre-sell that converts no AI-delivery subscribers (that *would* be a target-buyer rejection and would pull Demand/WTP back below 7), credentialed experts declining the share in favour of self-set-price platforms, or credential verification proving un-automatable at acceptable accuracy (which would also threaten K2/K7).

---

## Changes vs previous scorecards (v1: 5.1 Park → v2: 5.9 Park → v2.1: 6.25 Iterate → v3: 6.25 Iterate → v4: 6.65 Iterate → v5: 6.65 Iterate → **v6: 7.05 Iterate**)

The idea score moves **6.65 → 7.05**. **No evidence changed since v5** — same
signals, research, corrected payout and founder profile. The single new rule
("this is ideation, not P/S Fit") **removes the direct-evidence ceiling** that was
the binding cap on Demand and WTP, and re-scores them on the convergence bands.

| Dimension | v5 | v6 | What moved and why |
|---|---|---|---|
| Desirability | 7 (Pain 8, Demand 7, WTP 7) | **8** (Pain 8, Demand **8**, WTP **8**) | **[rule]** The v5 card stated explicitly that Demand and WTP were "capped at 7 by the direct-evidence ceiling." That ceiling is removed. Re-scored on convergence: **Demand 7→8** — a funded same-job competitor (Delphi) + an adjacent recurring paid market *above* Avee's price (JustAnswer) + a premium adjacent market (Intro) + a paid-AI-message market (Poe), with no full-weight target-buyer rejection → the 7–8 band, placed at 8 (not 9, because the exact-job proof is a single competitor with unverified revenue). **WTP 7→8** — recurring credential-gated WTP above Avee's price (JustAnswer) + premium WTP (Intro) → 8 (not 9, because it's for the human/self-set price). Dimension average 7.33 → **8.0**. |
| Viability | 6 (Market 7, Monet. 7, Moat 5, Distribution 6, Timing 6) | **6** (same sub-scores) | **[—]** No sub-score was ceiling-bound. Market size stays 7: the v5 note called 7 "the indirect ceiling anyway," but on re-inspection its real cap is the **unsized specific sub-market** (a neutral-5 component) plus the SIG-11 boundary and directional size figures — not the removed ceiling. So it honestly does not rise. Average 6.2 → **6**. |
| Feasibility | 7 (7/7/7/5) | **7** (7/7/7/5) | **[—]** Untouched by the rule. |
| Composite | 6.65 | **7.05** | **[rule]** Desirability 7→8 lifts the composite by 0.40×1 = 0.40. Viability and Feasibility unchanged. 0.40×8 + 0.35×6 + 0.25×7 = **7.05**. |
| Recommendation basis | Advisory; G1–G4; Iterate via G4 (6.65<7.5) | **Advisory; G1–G4; Iterate via G4 (7.05<7.5)** | **[—]** Same band, same single failing check (G4). The gap to Advance narrows from 0.85 to **0.45**. Thresholds unchanged. |

**Honest note on not inflating.** The move is **+0.40 and no more**. Only the two
sub-scores that the v5 card itself named as ceiling-bound (Demand, WTP) rise, and
each rises exactly **one band step to 8 — not two to 9** — because on the *exact
job* the convergent evidence still leans on one funded competitor (unverified
revenue) plus adjacent human-expert markets. Pain stayed at 8, Market size stayed
at 7 (its cap was never the ceiling), and Viability and Feasibility did not move
at all. The practical read — **Iterate, run the one pre-sell test** — is unchanged;
the idea is simply now **0.45 from Advance** rather than 0.85, and the same single
experiment is what closes the gap. The thesis's "proof that customers pay is P/S
Fit's job, not a requirement here" is now honoured in the numbers, not just the
narrative.

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
- **The AI-delivery demand leap is unproven** — but note: SIG-05 is a *competitor quality* complaint (the bar Avee must clear, and an opening), not proof demand is absent; SIG-11 marks the market's *edge*. The leap is an **unknown to test**, not disconfirmed — and under the new calibration the convergent indirect evidence is already enough to carry Demand/WTP to 8.
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

There is one idea this run. **IDEA-01 is Iterate (advisory) at composite 7.05**
(idea score, for ranking only) — up from 6.65 in v5. The rise is entirely the new
"this is ideation, not P/S Fit" calibration: with the **direct-evidence ceiling
removed**, Demand and WTP are re-scored on the **convergence** of idea-stage
evidence and each moves **7 → 8** — a funded same-job competitor (Delphi), an
adjacent recurring paid market priced *above* Avee (JustAnswer), a premium adjacent
market (Intro) and a paid-AI-message market (Poe), with **no full-weight
target-buyer rejection** against demand. They are placed at 8, not 9, because the
*exact-job* evidence still leans on a single competitor with unverified revenue —
honest discipline, not inflation. Viability (6) and Feasibility (7) are unchanged.
**G1** passes, **G2** reads distance **2 (Cold but mapped)** which does not block
Advance, and **G3** passes with a test runnable at that distance — so the only thing
short of the Advance band is **G4 (7.05 < 7.5)**, now just **0.45 away**.

**Highest-priority validation step:** commit to **one** named credentialed niche
and cold-reach 10 of the persona this week (e.g. independent consultants in
r/consulting, SIG-18 — the distance-2 route), recruit **3–5 experts** to publish
credential-fronted agents with one paid deliverable, and **pre-sell their existing
audiences** the one-to-one $20–25 subscription. One test resolves the deciding
unknowns at once — whether an audience pays for **AI** delivery (the evidence that
pushes Demand/WTP toward 9 and carries the composite over 7.5 into Advance) and
whether experts accept the ~$7.96–9.55/engaged-sub payout (the SIG-10 supply
question). A positive result points toward Advance; a negative pre-sell would be a
genuine target-buyer rejection and would pull the score back down. The founder
decides what to do with that read.
