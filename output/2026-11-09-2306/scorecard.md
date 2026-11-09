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

## Ranked summary

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|------|------|-----------|:---:|:---:|:---:|:---:|:-------|
| 1 | IDEA-03 | Aftercare | 7 | 7 | 7 | 7.00 | Iterate |
| 2 | IDEA-01 | AgentProbe | 7 | 6 | 7 | 6.65 | Iterate |
| 3 | IDEA-07 | ProofKit | 7 | 6 | 7 | 6.65 | Iterate |
| 4 | IDEA-04 | Hatch | 7 | 6 | 6 | 6.40 | Iterate |
| 5 | IDEA-02 | BudgetWall | 7 | 5 | 7 | 6.30 | Iterate |
| 6 | IDEA-10 | Checkpoint | 6 | 6 | 7 | 6.25 | Iterate |
| 7 | IDEA-09 | GroundWire | 6 | 6 | 6 | 6.00 | Iterate |
| 8 | IDEA-08 | MeterMark | 6 | 6 | 6 | 6.00 | Iterate |
| 9 | IDEA-06 | ShipAgent | 6 | 5 | 7 | 5.90 | Park |
| 10 | IDEA-05 | KeyRoom | 6 | 4 | 6 | 5.30 | Park |

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

## Top 3 recommendation

1. **IDEA-03 Aftercare (7.00)** — Best-evidenced demand (SIG-03/15) on the cleanest whitespace in the run (nobody sells the white-label freelancer→client health report), riding an existing retainer payment. **Highest-priority validation:** pre-sell the mock monthly report to 5 AI-automation freelancers and confirm they'd attach it to a client retainer at a named price before any build.
2. **IDEA-01 AgentProbe (6.65)** — The most directly-quoted pain in the set and a tight skill fit, but it must prove it can clear the free-OSS floor. **Highest-priority validation:** show the per-step-diff replay to 10 builders already on free OSS and count how many switch or pay vs. "my tests cover it."
3. **IDEA-07 ProofKit (6.65)** — Real trust-wall demand plus a built-in growth loop that fits the founder's distribution goal, but the whole thesis rests on one unproven claim. **Highest-priority validation:** A/B a real seller's landing page with vs. without the ProofKit report and measure buyer conversion lift — no lift kills it cheaply.

> Honorable mention: **IDEA-04 Hatch** is the strongest *motivation* fit (the monetization layer for agent makers + a public-page growth loop the founder explicitly wants); it ranks 4th only because demand-side buyer conversion and OpenAI platform risk are unresolved. If the founder weights "builds toward the viral-consumer home" over pure evidence, Hatch is the one to run alongside the top 3.
