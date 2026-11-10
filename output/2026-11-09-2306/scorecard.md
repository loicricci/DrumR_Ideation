# Scorecard — run 2026-11-09-2306

> Scored by Governance against `ideas.md`, `market-research.md`, `signals.md` and
> `founder-profile.md`. Weights (from CLAUDE.md): **Composite = 0.40·Desirability
> + 0.35·Viability + 0.25·Feasibility**. Gates: **Advance ≥ 7.5**,
> **Iterate 6.0–7.4**, **Park < 6.0**.
>
> **Thesis kill check (run first).** All 10 ideas pass K1–K7. I re-verified the
> two edge cases myself: **K6** holds for IDEA-08 (anchors the weak SIG-14 but
> also the strong, dated SIG-02) and IDEA-09 (weak SIG-10 but also the strong,
> dated SIG-09); **K7** is structurally removed for the three reliability plays
> (ProofKit, GroundWire, Checkpoint) because the product is builder-embedded infra
> and the founder never operates a customer-facing conversation. No idea is
> force-Parked on a kill rule — every Park below is on evidence/composite.
>
> **Calibration note.** This is a homogeneous, hot-but-crowding builder-tooling
> set. Demand is genuinely evidenced for most ideas, but *no* idea has
> differentiation evidence strong enough to clear Advance (≥7.5) — market research
> confidence is Medium or lower on all ten, and "no competitors" was false in
> every case. The honest result is a tight band: **0 Advance, 8 Iterate, 2 Park**,
> spread 5.3–7.0 by composite.
>
> **Founder-fit caveat (applies to the whole set).** On *skills* the founder
> resonates strongly everywhere (agent/LLM systems, cheap infra, observability).
> But the founder's stated headline goal is **viral consumer traction + a social
> home for agent-builders**; these ten are all B2B/prosumer dev-tools with no
> consumer growth loop except Hatch (public page) and ProofKit (shareable trust
> page). Resonance scores below reward technical credibility and trust ("will
> *these* founders be trusted here"), but the motivation/energy mismatch is a real
> drag on execution stamina and is flagged per idea where it bites.

> **Round 2 (refill) note.** Scored IDEA-11…15 only; IDEA-01…10 scores and cards
> are carried forward verbatim. All five new ideas pass the K1–K7 kill check (K6
> watched per idea; none force-Parked). Reframes are scored on their own evidence,
> not their parent's: **IDEA-11 Billback** ties Aftercare at 7.00 (it swaps the
> "will they sell a report?" unknown for a new "will the client approve a paid
> fix?" unknown), while **IDEA-12 Rehearse** scores *below* its parent AgentProbe
> (6.65 → 5.90) because research found the exact PR surface it targets is already
> occupied by a **free, OpenAI-owned promptfoo action** plus Braintrust's PR
> action. The three new-signal plays (Eject, PlainFlow, SwapStep) land in
> heavily venture-funded or platform-risk-capped territory. Net Round-2 result:
> **1 Iterate (SwapStep, Billback) / 3 Park** new, with Billback the standout.

> **Round 3 (refill, final round) note.** Scored IDEA-16…20 only; IDEA-01…15
> scores and cards are carried forward verbatim. All five pass the K1–K7 kill
> check (none force-Parked): K6 holds on each (Keepwell→SIG-03 strong; Backstop→
> SIG-06/09 strong; Pier→SIG-16 strong; Runnable→SIG-19 fetched; Throughline→
> SIG-17 fetched); **K7** is structurally removed for Backstop (refunds run on the
> *builder's own* Stripe — no fund custody) and Runnable (standard payments rail,
> one-sided marketplace, automated verification → **K2** manual-moderation rule
> also holds); **K2** is watched for Keepwell (auto-remediation must be automated,
> not a founder support channel). Scored on their own evidence, not their parents':
> **IDEA-16 Keepwell** lands *below* its parents Aftercare/Billback (6.75 vs 7.00)
> — it rides the now-evidenced "$1k–5k/mo retainer" norm with a cleaner
> breakage-independent billing model, but stakes itself on a *harder* auto-
> remediation build. **IDEA-17 Backstop** lands *below* its parent ProofKit (6.40
> vs 6.65) — it moves trust off the discredited self-issued score onto own-data +
> an enforced refund, a real improvement, but adds refund-staking + buyer-data-
> upload + Stripe-Connect dependencies that lower feasibility. Of the three
> new-signal plays, **Pier (6.30)** has the strongest Round-3 pain (SIG-16) but the
> most commoditized wedge (a **free official MCP conformance suite** + $5/mo
> hosting); **Runnable (6.00)** is the cleanest whitespace (no template marketplace
> verifies that templates run) on medium evidence; **Throughline (5.90, Park)** is
> weakest on both counts — Mem0/OpenMemory already ship its exact cross-tool MCP
> memory wedge and WTP is unevidenced. Net Round-3 result: **4 Iterate (Keepwell,
> Backstop, Pier, Runnable) / 1 Park (Throughline)**, with Keepwell the standout.
> No reframe was inflated for being a reframe; no late idea was credited for being
> late. Final tally across all 20: **0 Advance, 14 Iterate, 6 Park.**

## Ranked summary

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|------|------|-----------|:---:|:---:|:---:|:---:|:-------|
| 1 | IDEA-03 | Aftercare | 7 | 7 | 7 | 7.00 | Iterate |
| 2 | IDEA-11 | Billback | 7 | 7 | 7 | 7.00 | Iterate |
| 3 | IDEA-16 | Keepwell | 7 | 7 | 6 | 6.75 | Iterate |
| 4 | IDEA-01 | AgentProbe | 7 | 6 | 7 | 6.65 | Iterate |
| 5 | IDEA-07 | ProofKit | 7 | 6 | 7 | 6.65 | Iterate |
| 6 | IDEA-04 | Hatch | 7 | 6 | 6 | 6.40 | Iterate |
| 7 | IDEA-17 | Backstop | 7 | 6 | 6 | 6.40 | Iterate |
| 8 | IDEA-02 | BudgetWall | 7 | 5 | 7 | 6.30 | Iterate |
| 9 | IDEA-18 | Pier | 7 | 5 | 7 | 6.30 | Iterate |
| 10 | IDEA-10 | Checkpoint | 6 | 6 | 7 | 6.25 | Iterate |
| 11 | IDEA-09 | GroundWire | 6 | 6 | 6 | 6.00 | Iterate |
| 12 | IDEA-08 | MeterMark | 6 | 6 | 6 | 6.00 | Iterate |
| 13 | IDEA-15 | SwapStep | 6 | 6 | 6 | 6.00 | Iterate |
| 14 | IDEA-19 | Runnable | 6 | 6 | 6 | 6.00 | Iterate |
| 15 | IDEA-06 | ShipAgent | 6 | 5 | 7 | 5.90 | Park |
| 16 | IDEA-12 | Rehearse | 6 | 5 | 7 | 5.90 | Park |
| 17 | IDEA-20 | Throughline | 6 | 5 | 7 | 5.90 | Park |
| 18 | IDEA-13 | Eject | 6 | 5 | 6 | 5.65 | Park |
| 19 | IDEA-14 | PlainFlow | 6 | 5 | 6 | 5.65 | Park |
| 20 | IDEA-05 | KeyRoom | 6 | 4 | 6 | 5.30 | Park |

---

## Detailed cards (ranked order)

### IDEA-03 — Aftercare  ·  Composite: 7.00  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — Month-4 churn is an existential, recurring-revenue pain for the freelancer, not a vitamin; SIG-03 "almost always churned out by month four," "by day 30 someone… quietly gone back to doing the work manually."
- Demand evidence: 7 — Strong, fetched SIG-03 + SIG-15 (the "unpaid support / integration janitor" trap); research rates it Medium confidence with pain clearly evidenced.
- Willingness to pay: 7 — Freelancers already charge retainers and gate engagements; the tool marks up into an existing retainer (sold to the freelancer, not the SMB), so it rides a proven payment.
- Founder–market resonance: 8 — Monitoring + drift-detection pipeline is squarely the founder's observability/systems wheelhouse.

**Viability — 7**
- Market size & growth: 6 — Agent monitoring/drift is expanding (the "five drifts" framing shows a maturing category), inside the ~$10.9–15B 2026 agent market; no discrete sub-size (gap).
- Monetization & unit economics: 7 — $10–25/agent/mo recurring, marked up into the retainer; cheap infra keeps per-agent monitoring margin-positive.
- Defensibility / moat: 7 — Research's single clearest finding: incumbents (Galileo, AgentOps, Langfuse, Phoenix…) sell to the team running the agent; **nobody sells the white-label freelancer→client health report + multi-client billing** — the cleanest unoccupied slot in the run.
- Go-to-market realism: 7 — Buyer is the freelancer, reachable in the exact AI-agency Discords/Skool communities the founder can access (K5).
- Timing ("why now"): 7 — The 2025 agency wave hitting its first month-4 retention cliff is coherent and consistent with SIG-03/15; no disconfirming evidence found.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Log/endpoint watching + drift/anomaly detection is core founder engineering.
- Capital / resources vs. runway: 8 — Cheap per-agent monitoring; bootstrap-friendly.
- Time to testable MVP: 6 — Monitor + scheduled white-label report is shippable in ≤4 weeks, but the multi-client dashboard adds scope.
- External dependencies: 6 — Needs access to each client agent's logs/endpoints, and adoption depends on the freelancer changing how they sell upkeep.

**Composite:** 0.40×7 + 0.35×7 + 0.25×7 = **7.00**
**Gate decision:** Iterate — Best-evidenced demand married to the cleanest whitespace; held below Advance only because monetization hinges on unproven freelancer selling behavior.
**Biggest unknown:** Will freelancers actually fold a white-label health report into a billable retainer, or is the churn fix organizational ("name an internal owner," SIG-03 counter-signal) rather than a tool they'll pay for?
**De-risking step:** Pre-sell to 5 AI-automation freelancers — show the mock "your agent did X, caught Y" report and ask whether they'd attach it to a client retainer at a stated price before any build.

---

### IDEA-01 — AgentProbe  ·  Composite: 6.65  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — "Silent hallucination… you don't even know somethings wrong until downstream stuff breaks" (SIG-01); a painkiller for live-agent builders, though the counter-signal ("good evals are just testing") caps it.
- Demand evidence: 7 — Strong, fetched SIG-01/SIG-04; the step-level-diff framing maps one-to-one onto "observability into what the agent decided at each step, not just the final output."
- Willingness to pay: 5 — No explicit price in signals, and free OSS (Langfuse, Phoenix, Evidently) anchors the price near zero; paid conversion vs. self-host is unproven.
- Founder–market resonance: 8 — Observability/eval pipelines are the founder's core stated skill.

**Viability — 6**
- Market size & growth: 6 — Observability+evals clearly expanding (2026 roundup glut, two 2026 acquisitions = consolidation signal); no discrete sub-size (gap).
- Monetization & unit economics: 6 — $19–49/mo + metered trace retention; cheap infra helps but trace storage is a real cost line.
- Defensibility / moat: 4 — Crowded (LangSmith, Langfuse, Braintrust, Arize, AgentOps, Galileo…) and partly free OSS; the "frozen-inputs-as-a-product + per-step diff" wedge is narrower/cheaper than any major but incumbents are racing into step-tracing.
- Go-to-market realism: 7 — Self-serve, community-led, exactly the founder's reachable persona.
- Timing ("why now"): 6 — Real wall now, but the differentiating feature window may be short as incumbents add agent-step tracing.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — SDK wrapper + record/replay + per-step diff is the founder's wheelhouse.
- Capital / resources vs. runway: 7 — Cheap except trace retention storage.
- Time to testable MVP: 6 — Record-and-replay with behavior diffs is buildable but non-trivial inside 4 weeks.
- External dependencies: 8 — Minimal; wraps the builder's own stack.

**Composite:** 0.40×7 + 0.35×6 + 0.25×7 = **6.65**
**Gate decision:** Iterate — Strongest, most directly-quoted demand in the set, but sits on a crowded, partly-free floor; the feature-not-a-company risk is live.
**Biggest unknown:** Will solo builders pay $19–49/mo when free OSS (Langfuse/Phoenix) and "CI + unit tests already cover it" are the status quo?
**De-risking step:** Put the per-step-diff replay in front of 10 builders already using free OSS and measure how many switch or pay vs. "my tests cover it."

---

### IDEA-07 — ProofKit  ·  Composite: 6.65  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — "The real problem is distribution and trust… they want proof the agent works" (SIG-06, strong); a painkiller for the solo seller stuck at the trust wall.
- Demand evidence: 7 — SIG-06 (seller side) + SIG-09 (buyer-side trust anxiety, SMBs burned by unreliable voice agents) both strong/fetched.
- Willingness to pay: 5 — Sellers add support fees, but whether they pay $39–99/mo for a badge that may not move buyer behavior is unproven.
- Founder–market resonance: 8 — Eval/observability engineering plus agent-design taste (knowing what a convincing proof looks like); the shareable public page is also a growth loop that fits the founder's distribution goal.

**Viability — 6**
- Market size & growth: 6 — "Agent trust/certification" emerging fast in 2026 — validates the thesis but signals a land-grab.
- Monetization & unit economics: 6 — $39–99/mo for live monitoring/custom scenarios; cheap infra keeps it margin-positive.
- Defensibility / moat: 5 — Certo already targets "AI agencies that need to prove reliability to clients" (near-named competitor); AIUC-1 is the credentialed heavyweight; the deliberate non-marketplace framing is differentiated but the space is crowding fast.
- Go-to-market realism: 7 — Public trust page = built-in growth loop; persona reachable in builder communities.
- Timing ("why now"): 6 — Hot, but the 2026 entrant surge means multiple funded teams move simultaneously.

**Feasibility — 7**
- Technical complexity vs. capability: 7 — Scenario battery + continuously-updated public report is within the founder's eval skillset.
- Capital / resources vs. runway: 7 — Cheap to run.
- Time to testable MVP: 6 — Scenario runner + hosted report page is a ≤4-week MVP with scoping.
- External dependencies: 7 — Minimal; sandboxes the builder's own agent.

**Composite:** 0.40×7 + 0.35×6 + 0.25×7 = **6.65**
**Gate decision:** Iterate — Real demand and a defensible non-marketplace wedge, but the core value prop (a self-issued score moves buyer trust) is unproven.
**Biggest unknown:** Does a builder-supplied trust score actually change buyer behavior? AgentRisk concedes "today the badge is just a badge" and Centific found benchmark scores "overstated reliability."
**De-risking step:** A/B a real seller's landing page — ProofKit report present vs. absent — and measure buyer trust/conversion lift; no lift kills the thesis cheaply.

---

### IDEA-04 — Hatch  ·  Composite: 6.40  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 6 — Strong supply-side pain ("no real way to build something sustainable through the GPT Store," SIG-05) but it is income-aspiration (vitamin-leaning) for the creator, not a bleeding wound.
- Demand evidence: 7 — SIG-05 strong/fetched with explicit buyer-side (creator) WTP: wanting per-GPT subscriptions and to keep ~77–80% of revenue.
- Willingness to pay: 5 — Creator WTP is real, but a platform %-of-revenue is worth little if buyers of the agents don't convert ("supply may exceed demand").
- Founder–market resonance: 9 — This is the single idea that maps directly onto the founder's stated motivation (the missing monetization layer for agent makers) and headline goal (public-page growth loop → viral distribution).

**Viability — 6**
- Market size & growth: 6 — Agent/GPT monetization infra is nascent but active; usage-based pricing spreading (~44% of SaaS meters usage, via OpenView).
- Monetization & unit economics: 5 — Free-to-publish + % of creator revenue + paid tier; revenue is thin until buyers actually convert.
- Defensibility / moat: 5 — Several thin tools exist (BuyMyGPT, ibl.ai, Lingo Blocks, CustomGPT.ai) but none dominant; the end-to-end import + public-page growth loop is the differentiator.
- Go-to-market realism: 7 — Creator communities + public-page virality fit the founder's community-led, build-in-public comfort.
- Timing ("why now"): 5 — OpenAI's invite-only/US-only revenue-share gap is the whole thesis but rests on secondary sources, and OpenAI could ship native monetization and vaporize it.

**Feasibility — 6**
- Technical complexity vs. capability: 7 — Hosted endpoint + Stripe + metering on cheap infra is feasible for this founder.
- Capital / resources vs. runway: 8 — Cheap per-agent infra is exactly the founder's edge.
- Time to testable MVP: 6 — Import → hosted endpoint → Stripe public page is moderate scope.
- External dependencies: 5 — Heavy OpenAI platform risk (policy + no-embed could change either way) plus Stripe.

**Composite:** 0.40×7 + 0.35×6 + 0.25×6 = **6.40**
**Gate decision:** Iterate — Best motivation-fit and a genuine growth loop, but gated by demand-side conversion and platform risk.
**Biggest unknown:** Do buyers actually pay for published agents (demand side), or does supply vastly exceed paying demand so creators publish and nobody converts?
**De-risking step:** Recruit 10 creators with a "useful" agent, publish paywalled pages, and measure real buyer conversion + revenue over 30 days before building metering depth.

---

### IDEA-02 — BudgetWall  ·  Composite: 6.30  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — "$80 in API costs on a task I thought would cost $8… learned that one the expensive way" (SIG-02, strong); a concrete painkiller.
- Demand evidence: 7 — SIG-02 strong/fetched, reinforced by the dated, re-verified June-15-2026 Zapier AI repricing (SIG-13) creating live cost anxiety in exactly this buyer base.
- Willingness to pay: 5 — Positions as net-savings, but LiteLLM ships the core free; builders may not pay for what they already DIY or self-host.
- Founder–market resonance: 8 — Cost-control proxy is an explicit founder strength ("one person most credible building it cheaply").

**Viability — 5**
- Market size & growth: 6 — LLM cost-optimization / AI-gateway category expanding as agentic workloads multiply spend.
- Monetization & unit economics: 4 — % of routed spend or $15–39/mo, but the free LiteLLM anchor and proxy latency/trust objection squeeze pricing.
- Defensibility / moat: 3 — Lowest in the set: LiteLLM (OSS, hard budgets + request-path enforcement) is essentially this for free, and Portkey bakes USD budgets in; only preflight estimation is relatively uncommoditized.
- Go-to-market realism: 6 — Self-serve, reachable persona, but competing against free devtools.
- Timing ("why now"): 6 — Strengthened by Zapier repricing, but incumbents filled the gap during 2025–26 — the founder arrives after the free tooling.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Base-URL-swap proxy with budget/loop enforcement is core founder engineering.
- Capital / resources vs. runway: 8 — Cheap to run.
- Time to testable MVP: 7 — A proxy with per-task caps + preflight estimate is a fast MVP.
- External dependencies: 6 — Sits in the request path of every LLM call → latency/trust + provider-API change exposure.

**Composite:** 0.40×7 + 0.35×5 + 0.25×7 = **6.30**
**Gate decision:** Iterate (weakest Iterate, one failed differentiation test from Park) — Strong, dated demand but the highest feature-not-a-company risk in the set; research confidence is Medium-Low.
**Biggest unknown:** Is there a paid wedge above the free LiteLLM / built-in-Portkey line — i.e. will non-technical builders pay for a zero-config per-task preflight + dashboard they won't self-host?
**De-risking step:** Offer the hosted preflight-estimate + live dashboard to 10 builders currently hand-rolling caps and measure whether any pay rather than add LiteLLM for free.

---

### IDEA-10 — Checkpoint  ·  Composite: 6.25  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — "a bad value sat there for 2 days because the agent kept running"; the autonomy-backlash pain is real (SIG-04/SIG-15 medium), but demand for *per-action approval* specifically is adjacent, not direct.
- Demand evidence: 5 — SIG-04 and SIG-15 are medium-strength; the SIG-04 counter-signal ("Never, ever let AI run loose") supports the contrarian thesis but also shrinks the autonomous-agent market.
- Willingness to pay: 6 — HumanLayer Pro reportedly ~$100/user/mo and withHuman has a paid motion — some proven WTP for HITL approval.
- Founder–market resonance: 8 — Pause/resume durable-step orchestration is core founder engineering.

**Viability — 6**
- Market size & growth: 6 — HITL agent controls emerging; the autonomy backlash is a genuine 2026 sub-current.
- Monetization & unit economics: 6 — $15–39/mo by approval volume, recurring, cheap to run.
- Defensibility / moat: 5 — Contingent opening: HumanLayer reportedly pivoted up-market to coding agents (possibly vacating this niche — verify), but withHuman/Heed.io exist and LangGraph-native interrupts commoditize the primitive for technical users.
- Go-to-market realism: 6 — Freelancers who sold "autonomous" agents are reachable, but the pitch fights the "autonomous" selling point they made.
- Timing ("why now"): 6 — 2025 autonomous builds hitting months-later breakage; coherent with SIG-04/15.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Durable pause/resume + approval card is squarely the founder's state-management strength.
- Capital / resources vs. runway: 7 — Cheap.
- Time to testable MVP: 6 — SDK marker + mobile/Slack approval card + timeout default is a ≤4-week MVP.
- External dependencies: 6 — Slack/push plus per-framework integration hooks.

**Composite:** 0.40×6 + 0.35×6 + 0.25×7 = **6.25**
**Gate decision:** Iterate — A real pattern with a possibly-vacated incumbent niche, but the gating sweet spot is narrow and framework-native substitutes loom.
**Biggest unknown:** Which steps are worth gating — is the band wide enough that buyers want *more* approvals (not fewer interruptions), and has HumanLayer genuinely vacated the approval-SDK niche?
**De-risking step:** Verify HumanLayer's current SDK status on its own repo, then interview 8 freelancers on exactly which agent actions they'd gate and whether added latency is acceptable.

---

### IDEA-09 — GroundWire  ·  Composite: 6.00  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 7 — Accuracy pain is strongly evidenced: SMBs pay real money ($299, $1,428) then find output "inconsistent, unreliable… unusable" (SIG-09, strong/fetched); bots "invent policies" and get switched off (SIG-10).
- Demand evidence: 6 — SIG-09 is strong, but it proves demand for *accurate agents*, not specifically for a *standalone guardrail bought by the builder* — that buyer is an inference; SIG-10 is weak/search-surfaced.
- Willingness to pay: 5 — End customers pay for the agent, but builder WTP for a separate guardrail is inferred, and full suites bundle grounding for free.
- Founder–market resonance: 8 — Retrieval/grounding and multimodal pipelines are core founder skills.

**Viability — 6**
- Market size & growth: 6 — Guardrails/grounding expanding fast; adjacent voice-agent market ~$3.51B 2026 at ~39% CAGR (single-firm estimate); no discrete guardrail sizing (gap).
- Monetization & unit economics: 6 — Per-checked-message metered + flat floor; cheap infra keeps checks margin-positive.
- Defensibility / moat: 4 — Incumbent-heavy (Guardrails AI, NeMo, Patronus, Cleanlab, Vectara) and end-to-end suites (Intercom Fin, Shopify native, Tidio) bake grounding in; "accuracy" is table-stakes everyone chases.
- Go-to-market realism: 5 — Sold to the builder, but competing against both dev-tool libraries and bundled suites.
- Timing ("why now"): 7 — Strongest "why now" of the reliability trio: 2026 chatbot-hallucination/merchant-liability reporting makes safety a live buying criterion.

**Feasibility — 6**
- Technical complexity vs. capability: 6 — Grounding/retrieval is core, but a guardrail "may not fully stop hallucination" — the hard part is genuinely hard.
- Capital / resources vs. runway: 7 — Cheap per-message checks.
- Time to testable MVP: 6 — Middleware constrain-to-docs + confidence score + handoff is a feasible MVP.
- External dependencies: 7 — Minimal; builder-embedded.

**Composite:** 0.40×6 + 0.35×6 + 0.25×6 = **6.00**
**Gate decision:** Iterate (at the floor) — Accuracy pain is strongly evidenced but the specific standalone-guardrail buyer is inferred and the field is incumbent-heavy.
**Biggest unknown:** Will the *builder* pay for a standalone grounding guardrail when the full chat suites their clients already use bundle grounding?
**De-risking step:** Interview 8 freelancers building SMB support/voice agents — do they currently buy a separate guardrail, or get accuracy from their platform — and would they pay per-checked-message?

---

### IDEA-08 — MeterMark  ·  Composite: 6.00  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — Real margin-eating pain (usage runs 2–5× the flat quote), but the primary anchor SIG-14 is the weakest signal in the set; SIG-02 (strong) carries the cost-blowup evidence.
- Demand evidence: 5 — Weakest demand anchor; SIG-14 is search-surfaced, propped by SIG-02/SIG-15; research confidence Low-Medium.
- Willingness to pay: 6 — Retainer + usage-allowance norm (SIG-14/15) shows clients pay recurring for managed runs; freelancers want to meter/markup.
- Founder–market resonance: 7 — Metering/cost-attribution is a direct offshoot of the founder's cost-control infra edge.

**Viability — 6**
- Market size & growth: 5 — Metering infra is consolidating hard into payment giants (Stripe↔Metronome Jan 2026, Adyen↔Orb mid-2026) — commoditization pressure from above.
- Monetization & unit economics: 6 — $19–49/mo + small per-client fee, recurring, aligned to the retainer norm.
- Defensibility / moat: 6 — Same structural gap as Aftercare: billing engines (Metronome, Orb, Lago…) are developer back-ends; none ships a white-label freelancer→client portal with an auto invoice line.
- Go-to-market realism: 6 — Freelancer communities reachable.
- Timing ("why now"): 5 — Coherent (agentic workloads broke flat quotes, Zapier credit repricing) but the layer is consolidating into giants.

**Feasibility — 6**
- Technical complexity vs. capability: 7 — Metering wrap + portal + invoice line is feasible.
- Capital / resources vs. runway: 7 — Cheap.
- Time to testable MVP: 6 — Billing/invoicing is fiddly but a portal MVP fits ~4 weeks.
- External dependencies: 6 — Payment/invoice rails + client agent access.

**Composite:** 0.40×6 + 0.35×6 + 0.25×6 = **6.00**
**Gate decision:** Iterate (at the floor) — Attractive white-label packaging gap, but the thinnest demand evidence and a rapidly-consolidating underlying market.
**Biggest unknown:** Is the pricing pain big enough to pay a tool for, or is it solved by discipline (measure one run × frequency × margin) — and is demand real given the weakest signal anchor?
**De-risking step:** Re-verify SIG-14 on the live source, then show 6 freelancers the white-label credit portal + auto invoice line and test whether they'd pay vs. a spreadsheet markup.

---

### IDEA-15 — SwapStep  ·  Composite: 6.00  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — Dated, concrete cost pain: the June-15-2026 AI-by-Zapier repricing (AI steps default to the most expensive tier) means "bills are climbing… most teams haven't adjusted" (SIG-13) — real but more an annoyance than a bleeding wound.
- Demand evidence: 5 — SIG-13's *trigger* is now first-hand confirmed on `help.zapier.com`, but the customer *quotes* are weak/competitor-blog and actual migration volume is unverified ("intent loud in content, thin in practice").
- Willingness to pay: 6 — This persona already pays Zapier and is actively shopping Make/Pabbly/n8n (switching WTP), but Zapier's own "bring your own AI account at 1x" is a free substitute that blunts the savings pitch.
- Founder–market resonance: 8 — Cheap, cost-efficient multi-model routing is the founder's single strongest edge; the free "audit your Zapier AI bill" tool is exactly the SEO/shareable growth loop the founder wants.

**Viability — 6**
- Market size & growth: 5 — Narrow, dated, time-boxed window (no-code AI-step cost optimization); the opportunity can close as fast as it opened via another re-price.
- Monetization & unit economics: 6 — Flat $9–29/mo or small markup on routed calls; the founder's cheap-routing edge is the margin.
- Defensibility / moat: 4 — No third-party "cheap AI action" Zapier app was found (opportunity), **but** Zapier's Integration Publishing Requirements §2(i) allow removing integrations deemed *competing* — an app that undercuts AI-by-Zapier is a candidate; plus Zapier's own 1x own-account option substitutes.
- Go-to-market realism: 7 — The free account-scanning audit tool rides live "Zapier AI pricing" search intent — a genuine, dated growth loop; persona reachable via r/Zapier and no-code newsletters.
- Timing ("why now"): 7 — The strongest, most concrete, most dated "why now" in the Round-2 set: a specific June-15-2026 repricing event creating live migration intent, confirmed first-hand.

**Feasibility — 6**
- Technical complexity vs. capability: 8 — A Zapier app + cheap multi-model routing endpoint is a direct expression of the founder's single strongest skill.
- Capital / resources vs. runway: 8 — Cheap-infra routing; bootstrap-friendly.
- Time to testable MVP: 7 — Free audit tool + a Zapier AI action is a ≤4-week MVP.
- External dependencies: 3 — The crux risk: a **confirmed** Zapier competing-app policy (publishing requirements §2(i)) directly threatens the in-platform delivery, and Zapier can re-price or cut app-store AI actions at will — the whole product lives on someone else's platform.

**Composite:** 0.40×6 + 0.35×6 + 0.25×6 = **6.00**
**Gate decision:** Iterate (at the floor) — The best founder-edge fit and the strongest dated "why now" of the new ideas, but capped at the floor by a confirmed platform-policy risk and unverified migration volume.
**Biggest unknown:** Would a SwapStep AI action survive Zapier's competing-app policy (§2(i)), or does the entire in-platform delivery mechanism get removed — and is the migration intent real enough to monetize before the window closes?
**De-risking step:** Ship the *free audit tool first* (no Zapier app required) to measure real "Zapier AI pricing" migration demand and capture emails; in parallel, get a written read on §2(i) from Zapier's developer channel before building the paid AI action.

---

### IDEA-06 — ShipAgent  ·  Composite: 5.90  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — "Self hosted is cool right up until someone meets their first env var" (SIG-08, medium); real but medium-strength.
- Demand evidence: 5 — SIG-08 medium; buyers reportedly pay a managed-hosting premium.
- Willingness to pay: 6 — Evidence buyers pay a managed-hosting premium / setup fee exists.
- Founder–market resonance: 8 — Cheap, scalable agent infra is the founder's single strongest advantage; this is its most direct expression.

**Viability — 5**
- Market size & growth: 5 — Managed agent hosting expanding but already crowded/low-differentiation (2026 roundup glut).
- Monetization & unit economics: 4 — $9–29/mo floor crushed by $3.99/mo hosts and $29 one-time self-deploy kits; thesis K4 (infra cost under the floor) is the central risk.
- Defensibility / moat: 3 — Agntable already occupies almost exactly the "one-click OSS-agent gallery, no DevOps" position — a near-clone.
- Go-to-market realism: 6 — Self-serve gallery, reachable persona.
- Timing ("why now"): 5 — The market already responded in 2026; only the infra-cost edge keeps it non-redundant.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Hosted runtime is the founder's strongest edge.
- Capital / resources vs. runway: 6 — Per-user infra cost genuinely threatens the floor price (K4).
- Time to testable MVP: 6 — Deploy-from-template runtime is moderate scope.
- External dependencies: 7 — OSS agents + hosting substrate.

**Composite:** 0.40×6 + 0.35×5 + 0.25×7 = **5.90**
**Gate decision:** Park — Demand is real and it is the founder's strongest-skill expression, but it is the most directly-cloned (Agntable) and thinnest-margin idea; viability is the blocker.
**Biggest unknown:** Can cheap infra hold a positive margin under a $9–29 floor against $3.99/mo hosts and $29 one-time kits (K4)?
**De-risking step:** Model true per-user infra cost at the floor price against Agntable/Agent37 pricing; if margin isn't clearly positive, don't build.

---

### IDEA-12 — Rehearse  ·  Composite: 5.90  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 7 — Same strongly-evidenced pain as its parent AgentProbe: "you can't just diff it like code," a prompt change silently alters behavior (SIG-01/04, strong/fetched); a painkiller for shipping agents from a repo.
- Demand evidence: 7 — Strong, fetched SIG-01/04 carry over, and a June-2026 practitioner survey treats CI/CD eval wiring as an active unsolved workflow problem; but the specific "put it in the PR as a required check" surface is the bet, not the evidenced part.
- Willingness to pay: 4 — The crux: the exact PR surface is already occupied by a **free, OpenAI-owned promptfoo GitHub action** (before/after PR comparisons) plus Braintrust's PR action; public repos are free, so paid conversion faces direct free pressure — lower than AgentProbe's WTP for that reason.
- Founder–market resonance: 8 — Record/replay + behavioral-diff is the founder's eval core, and the public-PR footprint is the growth loop governance said Round 1 lacked.

**Viability — 5**
- Market size & growth: 6 — Evals-in-CI/CD expanding and consolidating (OpenAI acquired promptfoo Mar 2026); no discrete sub-size (gap).
- Monetization & unit economics: 5 — $15–49/mo private repos, but free public repos + a free MIT competitor squeeze the paid line.
- Defensibility / moat: 4 — promptfoo (free, OpenAI-owned) and Braintrust's `eval-action` already sit on this surface; differentiation rests only on plain-English diff + zero-config + public-repo loop, not the primitive — highest already-free-competitor pressure of the Round-2 set.
- Go-to-market realism: 6 — The Codecov/Vercel-bot public-repo loop is a real growth mechanic, but only pays off if enough agent code is actually open-source.
- Timing ("why now"): 5 — Coherent (agent code moved into Git/CI), but the 2026 promptfoo acquisition + Braintrust's action mean incumbents are already on the surface as the idea arrives.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Record/replay + behavioral diff + a GitHub/GitLab app is the founder's wheelhouse.
- Capital / resources vs. runway: 7 — Cheap, though free public-repo runs are a real infra cost line.
- Time to testable MVP: 6 — GitHub app + scenario replay + human-readable diff comment is buildable but non-trivial in 4 weeks.
- External dependencies: 7 — GitHub/GitLab platform dependency, otherwise self-contained.

**Composite:** 0.40×6 + 0.35×5 + 0.25×7 = **5.90**
**Gate decision:** Park — The reframe moves off the crowded free-OSS tracing floor onto the PR surface, but that surface is already occupied by a free, OpenAI-owned promptfoo action plus Braintrust's PR action; scored on its own evidence it falls *below* its parent AgentProbe (6.65), not above it — no reframe inflation.
**Biggest unknown:** Is there a paid wedge above a free, OpenAI-owned promptfoo action that already posts before/after PR comparisons — i.e. will teams pay for plain-English zero-config diffs rather than wire up the free tool once?
**De-risking step:** Put the plain-English behavioral-diff PR comment in front of 10 teams already running promptfoo/Braintrust in CI and measure whether any switch or pay vs. "the free action is good enough."

---

### IDEA-13 — Eject  ·  Composite: 5.65  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — "You're renting a prettier box"; makers abandon platform after platform over hidden complexity and lock-in (SIG-11) — a genuine frustration, but more an ownership preference than an acute, bleeding wound.
- Demand evidence: 6 — SIG-11 is unusually **price-anchored** ("$19 starter was enough," would pay "only if they can export and own the code"), but it is search-surfaced and needs re-verification; corroborated by SIG-08/SIG-12.
- Willingness to pay: 6 — An explicit $19/mo anchor and a stated condition ("only if I can own it") is the clearest WTP articulation of the new ideas, though export may be a nice-to-have, not a must-buy.
- Founder–market resonance: 8 — Agent-design taste + cheap orchestration infra fit "generate a good agent AND run it cheaply," and the "built with Eject" share page fits the founder's build-in-public growth comfort.

**Viability — 5**
- Market size & growth: 7 — Large, hot, and heavily venture-funded (Lovable, Replit, Gumloop, Emergent all raised big in 2026) — demand is not the question.
- Monetization & unit economics: 6 — $19/mo + higher tiers, cheap-infra margin on hosted runs.
- Defensibility / moat: 4 — Crowded and extremely well-capitalized; OSS builders (Langflow exports JSON, Flowise self-hosts) already blunt "no lock-in," and export-as-headline may be a feature, not a moat — though a true agent-specific "describe → eject clean source" product looks under-occupied.
- Go-to-market realism: 5 — A solo bootstrapper's distribution is dwarfed by funded incumbents iterating the same UX; the "built with" loop is unproven.
- Timing ("why now"): 5 — The lock-in backlash is plausible, but the funding wave means many well-funded teams are chasing the same UX simultaneously.

**Feasibility — 6**
- Technical complexity vs. capability: 5 — Codegen good enough to *actually own and run* is genuinely hard; the eject promise raises the quality bar well above a demo.
- Capital / resources vs. runway: 7 — Cheap infra for hosted runs; bootstrap-friendly.
- Time to testable MVP: 5 — A narrow template/export set is scoped to 4 weeks, but production-grade codegen quality in that window is a real risk.
- External dependencies: 7 — LLM providers; relatively low platform risk vs. the Zapier/OpenAI-dependent ideas.

**Composite:** 0.40×6 + 0.35×5 + 0.25×6 = **5.65**
**Gate decision:** Park — Price-anchored ownership demand and an under-occupied agent-specific eject wedge, but a crowded, heavily-funded category where export-as-headline may not out-pull incumbent distribution, and codegen quality is a real feasibility risk.
**Biggest unknown:** Does "own and export your agent's clean source" out-pull funded incumbents' distribution, or is it a nice-to-have that doesn't change platform choice?
**De-risking step:** Land a no-build "export my agent to a clean repo" offer in r/nocode/r/AI_Agents against SIG-11's exact complaint and measure how many of the "I'd pay to own it" makers actually put down a $19 deposit.

---

### IDEA-14 — PlainFlow  ·  Composite: 5.65  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 5 — Non-technical owners bounce off n8n/Make JSON and webhooks (SIG-12), but the counter-signal is strong — many "stick with Zapier because templates make it hard to break things," so the pain may not be acute enough to switch for.
- Demand evidence: 5 — SIG-12 is the weakest anchor of the three new-signal ideas (search-surfaced), and funded challengers (Gumloop, Lindy) already chase this exact persona.
- Willingness to pay: 6 — The persona **already pays** for Zapier/Make, so switching WTP exists, but it is indirect (no price anchored to *this* product).
- Founder–market resonance: 7 — Orchestration + cheap infra make a "just works, we run it" experience viable at a low price; the vertical template gallery fits the founder's community-led GTM.

**Viability — 5**
- Market size & growth: 6 — Large and expanding, but the "simplicity for non-devs" slot is actively contested by funded players (Gumloop ~$37/mo, Lindy).
- Monetization & unit economics: 6 — $15–39/mo undercutting a freelancer; cheap-infra margin.
- Defensibility / moat: 4 — "Describe it in plain English, never see JSON" is *exactly* Gumloop/Lindy's pitch; only the vertical-niche narrowing (e.g. salon "missed-call text-back") is differentiated.
- Go-to-market realism: 6 — The vertical template gallery is a plausible SEO/growth loop and fits community-led GTM.
- Timing ("why now"): 5 — The same 2025–26 wave that raised the skill floor also produced the funded challengers now filling the gap as the idea arrives.

**Feasibility — 6**
- Technical complexity vs. capability: 6 — A self-healing, chat-first, guardrailed automation builder is non-trivial; the narrow-vertical scope makes it tractable.
- Capital / resources vs. runway: 7 — Cheap-infra; bootstrap-friendly.
- Time to testable MVP: 6 — One or two verticals keeps the MVP in the 4-week window.
- External dependencies: 5 — K2 watch: "we run it" must self-heal or it becomes a founder support queue; plus per-integration third-party app risk.

**Composite:** 0.40×6 + 0.35×5 + 0.25×6 = **5.65**
**Gate decision:** Park — Plausible non-dev complexity pain and a persona that already pays, but the weakest signal anchor (SIG-12), a "good-enough" incumbent (Zapier templates), and funded AI-native challengers (Gumloop, Lindy) already own the "plain-English builder" positioning.
**Biggest unknown:** Is the non-dev owner's pain acute enough to switch from Zapier's safe templates — and can a solo founder out-focus funded challengers on a single high-demand vertical?
**De-risking step:** Re-verify SIG-12 live, then run a single-vertical landing page (e.g. "salon missed-call text-back, we build and run it") and measure sign-ups/pre-orders against Zapier's existing template for the same job.

---

### IDEA-05 — KeyRoom  ·  Composite: 5.30  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — "Credential onboarding is the silent killer… ~8–12 API keys" (SIG-07, medium); real but medium.
- Demand evidence: 5 — SIG-07 medium, and the person raising it (NyxID) sells an auth product, so the pain may be talked up.
- Willingness to pay: 4 — None found; whether solo builders pay for what venture-funded incumbents give away at the low end is the open question.
- Founder–market resonance: 7 — Secure integration plumbing is core founder skill.

**Viability — 4**
- Market size & growth: 6 — Embedded-integrations/auth is large and well-funded, repositioning to "AI agents" in 2026.
- Monetization & unit economics: 4 — $29–79/mo, but incumbents give the low end away.
- Defensibility / moat: 3 — Most saturated idea in the set: Nango, Composio, Paragon (Connect Portal ≈ this idea's branded connect page), Merge, Pipedream, Arcade, WorkOS… all better-capitalized.
- Go-to-market realism: 5 — Self-serve, but entering against funded incumbents selling the same wedge.
- Timing ("why now"): 4 — The founder is late to a well-funded party that pivoted to exactly this story in 2026.

**Feasibility — 6**
- Technical complexity vs. capability: 6 — OAuth dances + token rotation across many SaaS is substantial, ongoing connector-maintenance work.
- Capital / resources vs. runway: 6 — Maintaining a connector set is a recurring resource drain for a solo founder.
- Time to testable MVP: 5 — A meaningful connector set likely exceeds the 4-week MVP window.
- External dependencies: 5 — Many third-party OAuth providers, each a platform-risk surface.

**Composite:** 0.40×6 + 0.35×4 + 0.25×6 = **5.30**
**Gate decision:** Park — Genuine pain but the most competitively saturated idea, a price/segment wedge rather than a capability gap, against venture-funded incumbents already selling it.
**Biggest unknown:** Will solo builders pay for what Nango/Paragon/Composio already offer at/near free on the low end?
**De-risking step:** None worth running yet — park unless a sharply narrower, un-served connector niche with evidenced solo-builder WTP appears.

---

## Round 2 — new ideas scored

Cards for IDEA-11 (Billback, rank 2, Iterate), IDEA-15 (SwapStep, rank 13, Iterate),
IDEA-12 (Rehearse, rank 16, Park), IDEA-13 (Eject, rank 18, Park) and IDEA-14
(PlainFlow, rank 19, Park) are placed in ranked order above. Below is the
Billback card (the only new idea that cracked the top tier); the other four new
cards appear at their composite rank in the list above.

### IDEA-11 — Billback  ·  Composite: 7.00  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — The strongest pain in the maintenance cluster: agents break months later and the freelancer becomes "unpaid support, on-call dev, integration janitor" (SIG-15, medium) while clients churn by month four (SIG-03, strong/fetched) — a bleeding, recurring-revenue wound, not a vitamin.
- Demand evidence: 7 — SIG-03 (strong, fetched) + SIG-15 (medium), reinforced by a June-2026 agency incident-playbook framing the antidote as "monitoring that turns silent failures into loud ones" — the firefighting pain is strongly evidenced (the *paid-fix conversion* is the unproven part, not the pain).
- Willingness to pay: 6 — Rides the existing "fixed build fee + maintenance retainer" norm (SIG-15) and pays for itself on the first recovered fix, but neither per-incident client approval nor breakage *frequency* is evidenced in the signals (SIG-03/15 are WTP-absent).
- Founder–market resonance: 8 — Drift/breakage detection and monitoring pipelines are the founder's observability wheelhouse; the branded client-approval page is a genuine growth loop (every approving client sees the platform).

**Viability — 7**
- Market size & growth: 6 — Agent monitoring / incident-management, expanding (plentiful 2026 "AI agent failure detection / incident management" roundups), inside the broader agent market; no discrete sub-size (gap).
- Monetization & unit economics: 7 — Flat $19–39/mo + per-agent monitoring fee + optional small % of approved fixes; cheap infra keeps per-agent monitoring margin-positive and the model monetizes recovered revenue, not an upsell.
- Defensibility / moat: 7 — Research's specific check found **no tool that converts agent failures into client-approved, paid fix tickets**; adjacent prior art (Augment Cosmos, Monte Carlo Agent Health, Datadog, Better Stack) is all **internal dev-team** tooling — the freelancer→SMB-client branded approval/billing layer is unoccupied, the same structural gap Aftercare exploits.
- Go-to-market realism: 7 — Buyer is the freelancer, reachable in the exact AI-agency Discords/Skool/Indie-Hackers communities the founder can access (K5); the branded approval page doubles as distribution.
- Timing ("why now"): 7 — Well-supported: the 2025 autonomous-client-build cohort is hitting first-wave months-later breakage (SIG-15) exactly as agencies feel the month-4 churn cliff (SIG-03), with 2026 agency incident-playbook content appearing now.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Breakage/drift detection + auto-drafted incident + a branded approval page is squarely the founder's systems-engineering strength.
- Capital / resources vs. runway: 8 — Cheap per-agent monitoring; bootstrap-friendly.
- Time to testable MVP: 6 — Monitor → incident draft → client-approval page is shippable in ≤4 weeks, though the detect-and-scope-a-fix loop and the client-facing billing veneer add scope.
- External dependencies: 6 — Needs access to each client agent's logs/endpoints and a client-approval/billing flow; adjacent incumbents (Monte Carlo, Augment) could bolt on a client-billing veneer.

**Composite:** 0.40×7 + 0.35×7 + 0.25×7 = **7.00**
**Gate decision:** Iterate — Scored on its own evidence, the reframe genuinely sidesteps Aftercare's "will the freelancer *sell* a report?" unknown by attaching to firefighting they're already forced to do, and lands on the same cleanest-whitespace in the run — but it swaps in a new, un-evidenced conversion (will the client approve per-incident *paid* fixes?), which keeps it at Iterate, not Advance. No reframe inflation: it ties Aftercare at 7.00 on merit, it does not inherit or exceed it.
**Biggest unknown:** Will SMB clients approve per-incident "approve a 2-hour fix" charges (rather than feel nickel-and-dimed), and is agent-breakage frequency high enough to generate meaningful recovered revenue that justifies the monitoring fee?
**De-risking step:** Interview 6 AI-automation freelancers to measure real breakage frequency per client agent, then show 5 of their SMB clients the mock "your Invoicing Agent stopped reading POs — approve a 2-hour fix?" page and test whether they'd tap approve at a stated price — before any build.

---

## Round 3 — new ideas scored

Scored IDEA-16…20 only; IDEA-01…15 carried forward verbatim. The five cards below
appear here in composite order (they also sit at their true rank in the summary
table). Round-3 result: **4 Iterate (Keepwell, Backstop, Pier, Runnable) / 1 Park
(Throughline)**, with **Keepwell (6.75)** the standout — the third framing of the
run's best-evidenced whitespace, now with the cleanest billing model, held below
Advance only by the auto-remediation build bar.

### IDEA-16 — Keepwell  ·  Composite: 6.75  ·  Gate: Iterate  ·  Parent: IDEA-11

**Desirability — 7**
- Pain intensity: 7 — The strongest, best-evidenced pain in the run carries over: agents break months later and the freelancer becomes the "unpaid support, on-call dev, integration janitor" (SIG-15, medium), while clients silently revert and churn by month four (SIG-03, strong/fetched) — a bleeding, recurring-revenue wound.
- Demand evidence: 7 — SIG-03 (strong/fetched) + SIG-15 (medium), now reinforced by research with concrete retainer price points (2026 pricing guides: ~$1,000–5,000/mo maintenance retainers, £500–5,000/mo for "monitoring, prompt fixes when an upstream API changes, small adjustments") — the retainer norm Keepwell rides is well-corroborated.
- Willingness to pay: 6 — Rides an *evidenced* "build fee + monthly retainer" norm (cleaner than Billback's unproven per-incident approval), but research is explicit that this validates the retainer, not that freelancers will pay a per-agent SaaS fee *on top* of it — so WTP sits a notch below Aftercare's "marks up into an existing retainer" (7).
- Founder–market resonance: 8 — Drift/breakage detection, auto-remediation and monitoring pipelines are the founder's observability wheelhouse; the branded per-client status page is a growth loop (every client, and any other freelancer they work with, sees the platform).

**Viability — 7**
- Market size & growth: 6 — Agent monitoring / incident-management + the agency maintenance-retainer motion, expanding (2026 "AI agent uptime / outage monitoring" content); no discrete sub-size (gap).
- Monetization & unit economics: 7 — Flat $12–29/agent/mo (or portfolio tier), **breakage-independent** and riding the evidenced retainer norm rather than inventing a per-incident billing event; cheap infra keeps per-agent monitoring margin-positive. The cleanest monetization model of the three maintenance framings.
- Defensibility / moat: 7 — Same cleanest-whitespace Aftercare/Billback exploit: incumbents sell monitoring to the team running the agent; research found **none that auto-remediates routine failure classes *and* publishes a branded per-client uptime page sold to a freelancer** (IncidentHub does per-client status pages for teams, but not the care-plan package). The white-label freelancer→client care-plan slot is open.
- Go-to-market realism: 7 — Buyer is the freelancer, reachable in the exact AI-agency Discords/Skool/Indie-Hackers communities (K5); the branded status page doubles as distribution.
- Timing ("why now"): 7 — Well-supported: the 2025 autonomous-build cohort is hitting first-wave months-later breakage (SIG-15) as agencies feel the month-4 churn cliff (SIG-03), and 2026 agency incident-playbook content frames "turn silent failures into loud ones" as the fix.

**Feasibility — 6**
- Technical complexity vs. capability: 6 — Monitoring + branded status page is core founder engineering, but **robust cross-client auto-remediation** (re-auth OAuth, patch schema shifts, restart on timeout) is a genuinely hard bar research flags as "the hardest part" — this is the new scope that pulls feasibility below Aftercare/Billback (both 8 here).
- Capital / resources vs. runway: 8 — Cheap per-agent monitoring; bootstrap-friendly.
- Time to testable MVP: 5 — Detection + status page + one-click escalation is ≤4 weeks, but reliable auto-remediation of routine failure classes adds scope beyond the window (MVP must scope remediation narrowly; K3 watch).
- External dependencies: 6 — Needs access to each client agent's logs/endpoints/auth to remediate; adoption assumes the freelancer already runs a retainer (if not, Keepwell must *create* that habit).

**Composite:** 0.40×7 + 0.35×7 + 0.25×6 = **6.75**
**Gate decision:** Iterate — Scored on its own evidence, Keepwell is the most de-risked *billing model* of the maintenance cluster: it rides an evidenced flat-retainer norm (no per-incident approval, no dependence on breakage frequency) on the same cleanest whitespace. It lands **below** its parents Aftercare/Billback (7.00) — not above — because it stakes itself on a harder auto-remediation build (F 6 vs 7) and its "per-agent SaaS fee on top of the retainer" WTP is one step less directly evidenced. No reframe inflation.
**Biggest unknown:** Can auto-remediation cover enough of the routine failure classes to make a flat per-agent fee feel earned (shallow remediation leaves the freelancer still firefighting), and will freelancers pay a per-agent SaaS fee on top of a retainer they already charge?
**De-risking step:** With 6 AI-automation freelancers, inventory the *actual* recurring failure classes across their client agents (auth expiry, schema shift, timeouts) and measure what share is safely auto-remediable; in parallel, pre-sell the branded status page + flat per-agent price and confirm they'd add it to an existing retainer — before building the remediation engine.

---

### IDEA-17 — Backstop  ·  Composite: 6.40  ·  Gate: Iterate  ·  Parent: IDEA-07

**Desirability — 7**
- Pain intensity: 7 — Buyers "want proof the agent works" and won't trust an unknown agent (SIG-06, strong/fetched); SMBs paid real self-serve money ("$299," "$1,428") for agents that were "inconsistent, unreliable… unusable," then "felt the cancellation and refund policies were applied very strictly" (SIG-09, strong/fetched) — a painkiller for the exact "couldn't trust it and couldn't get my money back" wound.
- Demand evidence: 7 — SIG-06 + SIG-09 both strong/fetched; Backstop's evidence is arguably a touch richer than ProofKit's because it adds the refund-frustration dimension the signals explicitly voice.
- Willingness to pay: 5 — Sellers add support fees, but whether a builder pays $39–99/mo **and stakes a real refund** is unproven — the refund-staking is a new barrier on top of ProofKit's price question.
- Founder–market resonance: 8 — Sandbox-run-on-arbitrary-inputs + eval/transcript tooling is the founder's observability + agent-design core; the "powered by Backstop · money-back if it fails your test" badge on every seller's page is a distribution surface.

**Viability — 6**
- Market size & growth: 6 — Agent trust/conversion (risk-reversal) tooling, a visibly emerging 2026 pattern; rides the SMB-agent buyer base (SIG-09).
- Monetization & unit economics: 6 — $39–99/mo flat, recurring; cheap per-trial sandbox runs keep it margin-positive.
- Defensibility / moat: 6 — The **own-data trial + auto-enforced refund, drop-in for *any* builder** fusion is a genuine gap (Intercom Fin's "$1M guarantee," Richpanel, Fini, Ringly all guarantee only *their own* agent, not a layer builders embed), and it moves trust off ProofKit's discredited self-issued score — an improvement (6 vs ProofKit's 5). But each half (guarantees; try-before-buy) is individually well-occupied at the incumbent top.
- Go-to-market realism: 7 — The badge on every seller's landing page is a built-in growth loop; persona reachable in builder communities.
- Timing ("why now"): 7 — Strong: a 2025–26 surge of solo agents hit a buyer base now actively burned by unreliability + aggressive billing, and the visible 2026 rise of incumbent guarantees shows risk-reversal is becoming a buying expectation.

**Feasibility — 6**
- Technical complexity vs. capability: 7 — Sandbox run-on-buyer-data + guarantee tracking + Stripe refund automation is within the founder's eval skillset.
- Capital / resources vs. runway: 7 — Cheap per-trial runs.
- Time to testable MVP: 6 — Embed flow + sandbox + guarantee tracking + Stripe refund API is a ≤4-week MVP with scoping.
- External dependencies: 5 — More moving parts than ProofKit's pure sandbox: the buyer must upload their own real examples (a privacy ask — cf. SIG-18, where exactly this access stalls SMB deals), and the refund runs on the **builder's own Stripe/Connect** (K7-clean — no fund custody — but needs verification against Stripe Connect refund docs).

**Composite:** 0.40×7 + 0.35×6 + 0.25×6 = **6.40**
**Gate decision:** Iterate — A real improvement on its parent's make-or-break flaw: it replaces ProofKit's "self-issued score buyers distrust" with two things buyers *do* believe (their own eyes on their own data + a refund they'll actually get). Scored on its own evidence it lands **below** ProofKit (6.65) — not above — because the refund-staking + data-upload + Stripe-Connect dependencies lower feasibility (F 6 vs 7). No reframe inflation.
**Biggest unknown:** Will indie builders actually stake a real money-back guarantee (fear of abuse, or of genuine failure on messy real data), or does adoption stall at the guarantee step even though the run-on-your-own-data proof has standalone value?
**De-risking step:** Offer the "trial on your own data + money-back if it fails an agreed bar" flow to 8 indie builders selling a working agent and measure how many will turn the guarantee *on* at a stated pass bar — if most take the proof but refuse the refund, ship the proof-only flow and test whether it still moves buyer conversion.

---

### IDEA-18 — Pier  ·  Composite: 6.30  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 7 — The strongest Round-3 pain: "console.log to stdout silently corrupts JSON-RPC framing. No error. Just silence"; "errors are silent, the protocol is unforgiving… invisible until production"; "the cross-client testing situation is killing me"; "15 min to deploy, 15 hours a week to keep running" (SIG-16, strong/fetched). A painkiller for MCP builders.
- Demand evidence: 7 — SIG-16 is strong, fetched, dated (Oct 7 2025) with multiple verbatim quotes, corroborated by SIG-19 demand-validation chatter ("would people pay for vetted MCP servers vs free GitHub repos?").
- Willingness to pay: 4 — The cap: WTP is "none found," SIG-16's own counter-signal says the fix may be an OSS linter + docs, and an **official FREE MCP conformance suite** already exists — the closest WTP signals are founders asking "would people pay?" (interest, not purchase). Free official tooling anchors price near zero.
- Founder–market resonance: 8 — Hosting multi-process agent/tool infra cheaply is the founder's single strongest advantage, and a protocol-conformance harness is exactly the systems problem that energises him; the verified-install pages/directory are a distribution loop.

**Viability — 5**
- Market size & growth: 6 — MCP infra exploding (official registry launched Sept 2025; 23,700–111,899 servers across directories) but the land-grab is already underway.
- Monetization & unit economics: 4 — Hosting is crowded and cheap ($5/mo Cloudflare, plus Smithery/Glama/mcp.run), the conformance half is commoditized by the free official suite, and WTP is unproven — margin is compressed even with the cheap-infra edge.
- Defensibility / moat: 4 — An **official, free MCP conformance suite + Inspector** sit directly on the testing wedge; hosting is generic. The only wedge is the "keep-it-running" bundle (hosted + continuous conformance + production alerting), and Smithery reportedly shutting its hosted proxy (Oct 2026) shows how fragile pure-MCP-hosting economics are.
- Go-to-market realism: 6 — Verified-install pages + a conformance-verified directory are a plausible distribution loop; persona reachable in r/mcp, r/ClaudeAI, MCP Discords.
- Timing ("why now"): 6 — MCP exploded and the pain is live, but the official registry + conformance suite landing in 2025–26 means the ecosystem is standardizing the exact primitives Pier builds on — the free baseline is rising fast as the idea arrives.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Hosting multi-process infra + a cross-client conformance harness is the founder's strongest edge.
- Capital / resources vs. runway: 6 — Cheap-infra edge, but hosting margin is compressed by $5/mo competition (K4 watch).
- Time to testable MVP: 6 — Host + one cross-client conformance check + uptime alert is scoped to ~4 weeks (K3 watch).
- External dependencies: 6 — MCP spec/registry/official-tooling evolving fast (platform-shaping risk); reference servers ship breaking changes often.

**Composite:** 0.40×7 + 0.35×5 + 0.25×7 = **6.30**
**Gate decision:** Iterate — The strongest, most directly-quoted Round-3 demand (SIG-16) and the founder's single best skill fit pull it over the floor, but it is pinned there by the weakest viability of the new ideas: a **free official conformance suite** sits on its differentiating wedge and $5/mo commodity hosting crushes margin, so monetization is the make-or-break.
**Biggest unknown:** Will MCP builders pay for a hosted "keep-it-running" bundle (continuous conformance + uptime + production alerting) when an official *free* conformance suite + Inspector exist and generic hosting is $5/mo — i.e. is the recurring value real above the free/official baseline?
**De-risking step:** Put the hosted "deploy once, we run cross-client conformance on every change + alert you on protocol-level failures" offer in front of 10 builders currently maintaining ≥2 MCP servers by hand, and measure how many pay vs. "the free official suite + Cloudflare is enough" — the one-time conformance lint is not the wedge; the keeping-it-running is.

---

### IDEA-19 — Runnable  ·  Composite: 6.00  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — Non-delivery ("paid for a template and got nothing after payment, no email, no instructions") and "doesnt work as stated by it's creator" (SIG-19) is a real trust/frustration pain, but it's a transactional annoyance more than a bleeding operational wound.
- Demand evidence: 6 — SIG-19 is medium/fetched with first-hand buyer complaints clustered on the n8n forum (dated 2025); buyers are **already paying** ($29 packs). Real but medium-strength, and the customer Runnable sells to is the *creator*, while the pain quotes are buyer-side.
- Willingness to pay: 6 — Buyers already pay for templates (paid, self-serve, evidenced) and creators pay storefronts, so payment behavior exists — better than "none found"; creator WTP for Runnable's fee/subscription specifically is inferred.
- Founder–market resonance: 7 — The sandbox that safely imports and runs an arbitrary n8n/agent template to verify it is an agent-infra problem the founder solves cheaply; one-click deploy rides the cheap-hosting edge; the branded storefront + "verified on Runnable" badge is a distribution loop. Creators are seedable by the founder alone via no-code/agent communities (K5).

**Viability — 6**
- Market size & growth: 6 — The template-resale cottage industry is fast-growing but crowding with would-be marketplaces (N8N Central, n8nMarkets, No-Code Marketplace, neura.market).
- Monetization & unit economics: 6 — Small transaction fee per sale + optional creator subscription + one-click-deploy hosting margin; recurring-leaning, but the fee model needs volume.
- Defensibility / moat: 6 — **Automated "test-import-and-run in a sandbox → verified working" proof + guaranteed delivery + money-back** is a genuine gap: research found none of the many marketplaces or generic storefronts (Gumroad/LemonSqueezy) verify a template actually runs before listing. The moat is real but narrow — verification can't prove the template works on the *buyer's* stack.
- Go-to-market realism: 6 — One-sided by design (creators seeded by founder; buyers arrive via each creator's own audience) keeps it off the parked two-sided-marketplace failure mode, but creator acquisition competes with the multiplying marketplaces.
- Timing ("why now"): 6 — The cottage industry sprang up faster than any trust/delivery/verification layer and buyer complaints are clustering now, but the wave of new marketplaces means it's a race, not an empty field.

**Feasibility — 6**
- Technical complexity vs. capability: 6 — A sandbox that safely imports and runs arbitrary n8n workflows / agent templates (credentials, varied APIs, isolation) is non-trivial, but within the founder's infra skill.
- Capital / resources vs. runway: 7 — Cheap infra for sandbox verification + hosted deploys.
- Time to testable MVP: 5 — Storefront + sandbox verification + guaranteed Stripe delivery + money-back for one narrow template type (e.g. n8n) is scoped, but the safe-arbitrary-run sandbox is real scope for a 4-week window.
- External dependencies: 6 — Payments rail (Stripe), per-platform import formats (n8n etc.), and creators to seed the supply side.

**Composite:** 0.40×6 + 0.35×6 + 0.25×6 = **6.00**
**Gate decision:** Iterate (at the floor) — The cleanest *whitespace* of the three new-signal plays (automated run-verification + guaranteed delivery is genuinely unoccupied) on first-hand, paid-buyer evidence, and it is the one marketplace the thesis permits (one side seedable by the founder alone). Capped at the floor by medium demand, multiplying competing marketplaces, and the hard limit that verification proves a template *runs*, not that it does what the creator *claims* on the buyer's stack.
**Biggest unknown:** Does "verified it actually runs + guaranteed delivery + money-back" out-pull the done-for-you-setup direction the market may drift toward (the SIG-19 seller counter-signal), and will enough creators choose Runnable over the crowd of new marketplaces to seed supply?
**De-risking step:** Recruit 5 template creators from no-code/agent communities, run their next launch through a manual "we verified it runs + guaranteed delivery" badge (no full build), and measure whether the verified badge lifts their conversion/price and whether buyers cite it — before building the automated sandbox.

---

### IDEA-20 — Throughline  ·  Composite: 5.90  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — "Every single morning, I had to re-explain everything… that's not automation, that's babysitting" (SIG-17, fetched) — ~10 min/session plus weekly CONTEXT.md upkeep is a real daily productivity tax, but a mild recurring annoyance rather than an acute wound.
- Demand evidence: 6 — SIG-17 medium/fetched, and the cross-tool portability pain is independently corroborated (2026 sources confirm native memory doesn't port between ChatGPT/Claude; imports are one-time snapshots, not live sync). Real but medium.
- Willingness to pay: 4 — "None found"; the cheap workaround (a single CONTEXT.md) is "good enough" for many, and native cross-session memory went free-tier on Claude/ChatGPT in Mar 2026 — the price anchor is near zero.
- Founder–market resonance: 8 — Agent memory, retrieval and orchestration are named founder strengths ("orchestration, tools, memory, multimodal pipelines"), a fast cheap memory store is the cheap-infra edge, and shipping as an MCP server rides the exploding MCP ecosystem as a distribution surface.

**Viability — 5**
- Market size & growth: 6 — AI agent/assistant memory is hot and well-populated in 2026.
- Monetization & unit economics: 5 — $9–19/mo, cheap-infra margin, but free-tier native memory + the CONTEXT.md workaround + free OSS (OpenMemory, local) compress it; WTP unevidenced.
- Defensibility / moat: 3 — The most occupied wedge of Round 3: the exact "portable cross-tool MCP memory" pitch is **already shipped** by Mem0/OpenMemory (a shared-across-clients MCP memory server), Zep's Context MCP, and Supermemory, plus a crop of consumer apps marketing "sync memory across ChatGPT/Claude/Gemini." Differentiation rests only on solo-operator simplicity + ownership, not the concept.
- Go-to-market realism: 5 — MCP server as a distribution surface and reachable communities, but the idea itself concedes the growth loop is thinner than the other Round-3 plays, and it competes with funded memory players.
- Timing ("why now"): 5 — Live why-now (multi-session, days-long agent work made cross-session memory a daily tax; MCP arrived as the standard plug), but the same why-now already pulled Mem0/Zep/Supermemory + consumer apps in — the opening is contested on arrival.

**Feasibility — 7**
- Technical complexity vs. capability: 7 — A memory store exposed as an MCP server is squarely the founder's memory/retrieval wheelhouse.
- Capital / resources vs. runway: 7 — Cheap per-user memory infra keeps margin positive under a low price.
- Time to testable MVP: 7 — Memory store + MCP server is a ≤4-week MVP.
- External dependencies: 6 — MCP ecosystem (platform-shaping risk) and native memory improving underneath it.

**Composite:** 0.40×6 + 0.35×5 + 0.25×7 = **5.90**
**Gate decision:** Park — The easiest build of the new ideas (F 7) and a real, corroborated portability pain, but it is the weakest on both viability counts: the precise "portable cross-tool MCP memory" wedge is already shipped by Mem0/OpenMemory, Zep and Supermemory (defensibility 3), WTP is unevidenced, native memory is now free-tier, and the growth loop is thin. Easy to build is not the constraint; an occupied wedge with no evidenced WTP is.
**Biggest unknown:** Is the cross-tool/portability benefit *felt* strongly enough to pay for — over both free-tier native memory (good enough for single-tool operators) and the free CONTEXT.md workaround — when Mem0/OpenMemory already ship a shared-across-clients MCP memory server?
**De-risking step:** None worth a full build yet — before anything, put a landing page offering "one memory that follows you across Claude, Cursor and your own agents, yours to export" in front of solo operators and measure email/deposit conversion against the fact that Mem0/OpenMemory already exist for free; park unless portability pulls real paid intent.

---

## Top 3 recommendation

Round 3 does not change the top tier's shape but adds the most de-risked framing yet of
the run's single best opportunity. The **agency-maintenance play** now has three framings
clustered at the top — **Aftercare (7.00)**, **Billback (7.00)** and the new
**Keepwell (6.75)** — all exploiting the same cleanest unoccupied slot in the run
(nobody sells the white-label freelancer→client packaging/billing layer). It remains the
run's clear lead.

1. **Agency-maintenance: Keepwell (6.75) / Billback (7.00) / Aftercare (7.00)** — The same best-evidenced demand (SIG-03 strong month-4 churn + SIG-15 the "unpaid integration janitor" trap, now with real $1k–5k/mo retainer price points) on the cleanest whitespace. **Keepwell is the most de-risked billing model** (a flat, breakage-independent per-agent fee riding an *evidenced* retainer norm — it removes Billback's "will the client approve each paid fix?" unknown and Aftercare's "will they sell a report?" unknown), but it stakes itself on a harder auto-remediation build, which is why it scores just under its parents. **Highest-priority validation:** with 6 freelancers, inventory the actual recurring failure classes across their client agents and measure what share is safely auto-remediable, while pre-selling the branded status page + flat per-agent price into an existing retainer — before building the remediation engine.
2. **IDEA-01 AgentProbe (6.65)** — The most directly-quoted dev-tool pain in the run and a tight skill fit, but it must prove it can clear the free-OSS floor. **Highest-priority validation:** show the per-step-diff replay to 10 builders already on free OSS and count how many switch or pay vs. "my tests cover it." (Prefer AgentProbe over its reframe Rehearse, which scored lower at 5.90 against a free, OpenAI-owned promptfoo action.)
3. **Trust wall: ProofKit (6.65) / Backstop (6.40)** — Real trust-wall demand (SIG-06/09) with a built-in growth loop that fits the founder's distribution goal. **Backstop is the de-risked framing** — it moves trust off ProofKit's discredited self-issued score onto the buyer's own data + an enforced refund — but hinges on builders being willing to stake a real guarantee. **Highest-priority validation:** offer the "trial on your own data + money-back if it fails an agreed bar" flow to 8 indie sellers and measure how many turn the guarantee *on*; if they take the proof but refuse the refund, A/B the proof-only flow for buyer-conversion lift.

> Honorable mentions. **IDEA-04 Hatch (6.40)** remains the strongest *motivation* fit (the monetization layer for agent makers + a public-page growth loop the founder explicitly wants). Of the Round-3 new-signal plays, **IDEA-18 Pier (6.30, Iterate)** has the strongest demand (SIG-16) and the founder's best skill fit but the most commoditized wedge — a *free official* MCP conformance suite + $5/mo hosting — so it must prove recurring "keep-it-running" value above the free baseline; **IDEA-19 Runnable (6.00, Iterate)** is the cleanest whitespace (no template marketplace verifies that templates run) and the one thesis-permitted one-sided marketplace, worth a no-build verified-badge test. **IDEA-20 Throughline (5.90, Park)** is easy to build but its exact cross-tool-memory wedge is already shipped by Mem0/OpenMemory with no evidenced WTP — park unless portability pulls real paid intent.
