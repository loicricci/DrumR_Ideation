# Ideas — run 2026-11-12-1205-fast

> Single-idea run. The founder asked to score **Avee V2 with usage-based expert
> payouts** against governance, instead of generating 5 new ideas. The idea is
> written by the orchestrator from the founder's brief (`avee-brief.md`) and the
> stress-tested revenue model (`revenue-model.md`, v1 spec in section 7). It is
> neutral and unscored.

---

## IDEA-01 — Avee: expert agents paid by usage

- **One-liner:** An all-access subscription to AI agents trained by real
  experts (consultants, coaches, advisors, creators, founders), where each
  subscriber's net contribution is paid out to the experts whose agents that
  subscriber actually used.
- **Target customer:** Two sides. **Supply:** solo experts with a knowledge
  base and an audience that asks repeat questions, who want an agent that
  answers 24/7 and escalates only what it can't handle. **Demand:** people who
  want on-demand answers from specific experts they trust, more grounded than a
  general chatbot. No single expert segment is chosen yet.
- **Problem / job to be done:** Experts trade time for money and answer the
  same questions over and over. Their audiences can't reach them on demand.
  Today experts use FAQs, courses, communities (Circle, Skool), Patreon /
  Substack, or AI "digital clone" tools they price and market themselves.
  Subscribers make do with general chatbots that lack the expert's specific
  knowledge and voice.
- **Distribution model (founder correction, this run):** Avee is **not** a
  bundle of unknown experts. Each expert shares **their own agent** with **their
  own audience** (they have a direct financial interest in doing so), and every
  conversation is **one-to-one** between one user and one agent. A subscriber who
  joins through expert A mostly uses A's agent; other agents are optional
  discovery. Demand therefore rests on "A's audience wants on-demand access to
  A", the pattern Delphi evidences. If B uses only A's agent, A earns ~$7.96 of
  B's $20 (~40% of price), or ~$9.55 with a 10% referral bonus. Delphi experts
  reportedly keep ~85% of a price they set themselves.
- **Differentiation vs Delphi.ai (founder input, this run):** Delphi
  ($18.7M raised; $16M Series A June 2025 led by Sequoia, per founder; being
  verified) validates the category and is the direct competitor. Avee's claimed
  edges: (1) **Credential-first trust.** Each agent prominently displays the
  expert's verified résumé and background ("ask a Harvard-trained marketer with
  20 years at P&G, not a random chatbot"); the founder states Delphi doesn't
  surface this on its home page (to be verified). Credentials must be verified
  automatically, or the trust asset is hollow and adds K7 liability.
  (2) **Europe-based:** GDPR, EU data hosting, EU AI Act transparency
  compliance, and multilingual European experts and audiences. (3) **Lower
  barrier for small experts:** no monthly fee and model costs covered, so Avee
  pays more than Delphi's estimated "85% minus $79/mo" below ~9 paying
  subscribers (estimate, orchestrator calculation).
- **Trust = pedigree, not personality (founder input, this run):** credibility
  comes from **verifiable credentials** (degree or PhD, years of experience,
  school, previous or current company or institution), not from the
  expert's name or fame; the name could even be hidden. Consequences:
  (1) supply widens from influencers to any credentialed professional;
  (2) users can **discover by credentials** (e.g. "marketing · Harvard ·
  20 yrs FMCG"), so a new expert can earn without an audience, which partly
  solves cold start alongside expert-led sharing; (3) **automated credential
  verification** (diplomas, e.g. Europass digital credentials; employment via
  work-email domain or LinkedIn) becomes the core asset and the main build.
  Risks: employer policy for current employees, and K7 liability if
  verification is weak. Closest precedent to check: JustAnswer (verified
  professionals shown by credential).
- **Delphi home page as observed (founder screenshot, 2026-11-12):** headline
  "Find people who've been there — Describe your situation. Get their
  perspective." Category chips (Career, Startups, Productivity, Health,
  Relationships, Marketing, Sales, Business, Design) and cards framed by
  **lived experience or group**: "Ask short-form video creators…", "Ask
  marathoners…", "Ask Stanford alums whether it was worth it". **No individual
  credentials** (degree, years, employer) are shown. Delphi positions on
  personal-growth, life-advice "lived experience"; Avee's opening is
  **individually verified professional credentials** for professional
  questions. Note: Delphi already does group-by-background discovery
  ("Stanford alums"), so the differentiator is verification and professional
  depth, not grouping itself.
- **Deliverables, not just answers (founder input, this run):** agents carry
  **tools** as well as knowledge: generate a pitch deck, PPT slides, images or
  designs, shaped by the expert's judgment and style ("get your deck from the
  best entrepreneur or VC", "get a visual from the best designer"). Users can
  request **several versions**, from one agent or from **several owners**
  (e.g. a VC's deck vs a founder's deck vs a designer's deck) and compare them.
  Effects: (1) higher willingness to pay than Q&A (deliverables have a market
  price); (2) multi-owner comparison creates **cross-agent usage**, so the
  usage-share payout spreads across experts; (3) a clear gap vs Delphi's chat-only
  clones. Risks: generation cost (decks and images run on **credits**, per
  revenue-model.md); generic AI deck tools (Gamma, Beautiful.ai) already render
  slides, so the moat is the expert's judgment, not the renderer; and honesty
  of the claim (an AI deck "from a VC" must be framed as built with that
  expert's agent, with an optional paid human review via escalation).
- **Pricing structure (founder decision, 2026-11-12):** **platform
  subscription, not per-agent.** Users subscribe to Avee (tiered plans with
  usage limits, like Claude or ChatGPT: each tier has a monthly allowance of
  tier-weighted messages; deliverables and media run on credits). Experts don't
  set prices. Creator payouts are reconciled monthly per subscriber:
  contribution = subscription − fees − that subscriber's metered model cost;
  50% goes to creators, split by that subscriber's usage across agents, so the
  most-used agents earn most. Per-agent subscriptions (Delphi's model) are
  rejected as too complex for users. The payout split is a parameter
  to calibrate in P/S Fit and PM Fit, not a hypothesis (founder decision).
- **Solution wedge:** The product exists (Avee V2, v0.6.0): create an agent,
  feed it documents/links/updates (auto-ingested into RAG + semantic memory),
  publish it publicly or privately, with human escalation. The wedge under test
  is the **monetization layer**: one $20–25/month All-Access plan, payouts by
  usage, and a public per-agent earnings dashboard.
- **Business model:** User-centric net contribution share, calculated per
  subscriber per month. Net revenue after fees and reserve, minus metered
  inference cost, gives the contribution. That is split 50% platform / 50%
  creators, and the creator half goes to each agent by tier-weighted message
  share. A fair-use inference cap (~$3/subscriber/month) protects the split;
  image/video/voice run on credits. Extra layers: referral bonus for experts who
  bring subscribers, paid human escalations, and expert-priced private-agent
  add-ons. **Estimate:** at $24.99 with $3 inference, an agent that gets 50% of
  a subscriber's usage earns ~$5.18 and the platform keeps ~41% of gross. At
  $20, ~$3.98 and ~40%.
- **Founder edge:** The product is already built by the founder. Cheap,
  routed inference is the variable the payout formula depends on. Agent-design
  taste. Solo technical speed.
- **Why now:** RAG + memory + cheap model routing make an expert-specific agent
  good and cheap enough to serve at a flat price. Creator-economy payout rails
  (Stripe Connect) are commoditised. Platforms are experimenting with usage-based
  creator payouts for AI agents (to be verified by market research).
- **Biggest risk:** Two-sided cold start at under 50 users: subscribers won't
  pay $20–25 without experts they already know, and experts won't bring their
  audience for ~$3–5 per engaged subscriber when Patreon/Substack let them keep
  ~90% of their own price.
- **Signals:** none (no signals.md in this run; the founder reports under 50
  users and no demand evidence yet).
- **Thesis check:** At risk on **K6** (no evidenced pain signal in this run).
  At risk on **K7** (expert-advice agents in health/finance/legal; avoidable by
  excluding regulated categories). The marketplace shape needs one side
  seeded by the founder alone. The 50+ prebuilt agents seed demand-side demo
  traffic but not paying supply. K1 passes (self-serve). K2 passes if payouts
  are automated via Stripe Connect. K3 passes (the product exists; the
  billing/payout layer is ≤ 4 weeks). K4 passes only with the cost cap.
  K5 is weak (no persona named).
- **Parent:** none
