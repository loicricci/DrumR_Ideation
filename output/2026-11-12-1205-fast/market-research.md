# Market Research — run 2026-11-12-1205-fast

> Single-idea run. Research keyed to **IDEA-01 — Avee: expert agents paid by
> usage**. Focused on the five questions the orchestrator set: market size,
> competitor monetization/splits, demand evidence, usage-based vs pro-rata
> payout precedent, and key risks. Every market claim is cited; inferences and
> estimates are labelled. No scoring (that is Governance's job).

---

## IDEA-01 — Avee: expert agents paid by usage

### 1. Market & trend

**Category:** Intersection of the creator economy and AI "digital clone" /
expert-agent tooling — i.e. creator monetization infrastructure where the
product sold is an expert's knowledge delivered by an AI agent.

**Size / direction (creator economy, the containing market):** Estimates for
2026 cluster between **~$234B and ~$324B**, all pointing up. One analysis cites
Precedence Research at ~$314B for 2026, +23.4% YoY; another gives ~$323B for
2026 vs ~$256B in 2025; Goldman Sachs is quoted projecting the addressable
market near **$480B by 2027** (fungies.io, 2026). Treat these as directional:
the figures come from a single aggregator blog citing firms without linking
primary reports, and definitions vary widely. **Direction is the reliable
signal — expanding, double-digit CAGR.** AI adoption inside the category is now
mainstream: ~84% of creators reported using AI tools in 2026 (fungies.io, 2026).

**Disconfirming / caution:** I found **no credible standalone market-size figure
for "AI digital clones" or "expert agents"** specifically — only general
commentary that digital twins will reshape how creator revenue is distributed
(khaby-8qm.pages.dev, 2026). So the specific sub-market Avee targets is
**unsized in public data** (inference: it is early/nascent, which cuts both ways
— greenfield but unproven).

### 2. Demand signals

- **Delphi.ai (the closest direct comp) reports creators at serious revenue
  scale.** A June 2025 CEO interview claimed some Delphi creators generate
  **multiple seven-figure annual revenues** from their clones (tbpn-digest,
  2025-06-24). This is a company/founder claim, not independently verified, but
  it is the strongest demand signal that end users *will* pay for access to a
  specific expert's AI clone.
- **Poe's price-per-message economy exists and is growing.** Launched April 2024;
  a third-party estimate (unverified) puts Poe revenue at ~$30M (2024) → ~$65M
  (2026) (usagepricing.com). Confirms a functioning paid-per-interaction AI
  chatbot market.
- **GPT Store proves pull-through value even where direct payouts fail:**
  Consensus says **10–15% of its new subscribers come via its GPT**; another
  builder gained ~3,500 LinkedIn subscribers from his GPT (WIRED mirror, 2024).
  Inference: expert agents work as a **top-of-funnel / lead-gen** channel even
  when the marketplace payout itself is thin — relevant to Avee's referral loop.

**Disconfirming:** No public evidence that *flat-rate all-access* bundles of
many experts (Avee's exact model) command willingness-to-pay. The proven demand
is for **a specific named expert** a user already trusts (Delphi's model), which
matches the revenue-model doc's own warning (section 6) that buyers pay for
specific experts, not "50 AI agents".

### 3. Competitive landscape & monetization (the core question)

| Player | Model | Creator take / split | Note |
|---|---|---|---|
| **Delphi.ai** | Expert digital clones; creator sets own price (memberships, per-session, paywalls, affiliate) | **~85% revenue share** reported on paid tiers; platform tiers Free / Builder ~$79/mo / Scaler ~$299/mo (custom top tier) | Creator-priced, SaaS + high rev-share. Reported inconsistently across listings — verify on delphi.ai. (agent37.com; delphiai.substack.com, 2025) |
| **OpenAI GPT Store** | Usage-based builder payouts | **Invite-only pilot; US-only.** One pilot dev: **$1,000/mo guaranteed minimum** + usage upside. Most builders paid **$0** | Formula never disclosed; weak analytics; creators call GPTs a "volunteer project" (WIRED mirror, 2024). Cautionary tale for usage-based pools. |
| **Poe (Quora)** | Price-per-message + subscription bounty | Creator sets per-message price (paid in $, users spend points); **$10/mo (or $20/yr) set aside per subscriber**, split among bots that converted them; Stripe payouts | Closest precedent to Avee's "pay the agents the subscriber used" (TechCrunch/Voicebot, 2024-04-09) |
| **Character.ai** | Companion chat | **No creator revenue share found** — creators are unpaid | Shows a large consumer base can exist with zero creator monetization (search returned nothing on payouts). |
| **Patreon** (benchmark) | Creator-priced memberships | New creators (post Aug 2025): **10% platform fee** + 2.9%+$0.30 card; legacy 5–12% | The take-rate experts will compare Avee against (schoolmaker.com; cartmango.com, 2026) |
| **Substack** (benchmark) | Creator-priced subscriptions | **10%** + Stripe (~13% all-in) | Same headline as Patreon (sacra.com; builtbyfoundry.io, 2026) |

**The competitive reality:** The two platforms experts *know* (Patreon,
Substack) and the leading clone platform (Delphi, ~85%) all let the creator
**keep 85–90% of a price they set themselves**. Avee proposes a **50% creator
share of net contribution** on a **platform-set $20–25 price** — structurally
far less generous per engaged subscriber. This is the central competitive
headwind, and it is corroborated by the idea's own "biggest risk" note.

### 4. Whitespace & wedge fit

- **Usage-based, user-centric attribution is genuinely differentiated.** Only
  Poe approximates "pay the agents the subscriber actually used," and Poe does
  it per-message rather than as a net-contribution split. GPT Store tried
  usage-based and stalled (invite-only, opaque). So Avee's **transparent,
  automated, public per-agent earnings dashboard** is real whitespace — the
  consistent creator complaint about GPT Store was **missing/opaque analytics**
  (WIRED mirror, 2024). Transparency is a credible wedge.
- **All-access discovery bundle** is a segment incumbents ignore: Delphi/Patreon
  are single-creator islands; a subscriber must already know whom to pay. An
  all-access pass could serve *discovery-driven* demand — but see risk 2.
- **Wedge fit caveat:** the whitespace is on the *supply-side rails
  (transparency, automated payouts, cost-efficient routing)*, not on *demand*.
  The demand-side value prop (why pay $20 for a bundle) is where comps are
  silent or negative.

### 5. Usage-based vs pro-rata payout precedent (the model's strongest claim)

The revenue model's choice of **user-centric** over **pro-rata pool** is
**well-supported by music-streaming precedent**:

- **SoundCloud "Fan-Powered Royalties"** is exactly the user-centric model:
  each subscriber's money is split only among the artists that subscriber
  actually played, not a shared pool. Runs for ~**100,000 indie artists**; a
  SoundCloud/MIDiA study of 118,000 accounts found a majority earned more, and
  SoundCloud claims indies earn **~60% more on average** vs pro-rata (company
  figure, not independently verified) (musicbusinessworldwide.com; musicweek.com).
- **Fraud resistance confirmed directionally:** commentators argue user-centric
  **"solves a lot of the fraud"** because inflating one shared pool stops paying
  off (Variety, 2023 — opinion). This validates the revenue-model doc's section 5
  claim that self-dealing loses money under user-centric attribution.
- **Deezer** is a *hybrid / capped pro-rata* ("artist-centric" with UMG), not
  pure user-centric — the pool stays finite (musicbusinessworldwide.com).

**Disconfirming nuance:** user-centric is **not uniformly fairer**. Reports
(nialler9.com; IMPALA 2025; ProMusik) find artists with **many passive
listeners earn less**, and the model mainly helps those with super-fans. Inferred
read-across: Avee's split rewards experts with **highly engaged niche audiences**
and penalizes broad-but-shallow ones — consistent with the "~250 engaged
subscriber-equivalents for ~$1,000/mo" math in the revenue doc.

### 6. Key risks

1. **Payout-per-expert is small vs alternatives (the dominant risk).** At $20–25
   with a 50/50 contribution split, an expert earns **~$3.20–5.18 per fully
   engaged subscriber** (revenue-model doc estimates). Patreon/Substack/Delphi
   let the same expert keep **85–90% of a self-set price**. **GPT Store is the
   cautionary precedent**: usage-based payouts reached a tiny invite-only group;
   most creators earned **$0** and migrated to affiliate/ads (WIRED mirror, 2024).
   This is a real, evidenced headwind, not a hypothetical.
2. **Two-sided cold start.** Subscribers won't pay for a bundle without experts
   they trust; experts won't bring audiences for cents. Character.ai shows demand
   can scale with **no** creator pay, but that is companion chat, not paid expert
   advice — not a safe read-across.
3. **Inference cost of heavy users on a flat plan.** Structural: the revenue-model
   doc itself shows a single power user on a frontier-model agent turns platform
   margin **negative** without the fair-use cap. Industry context (inference,
   widely reported): flat-rate AI subscriptions lose money on the heaviest users —
   the cost cap + credits design is **necessary, not optional**. (Inference: I
   could not within budget cite a specific operator's loss disclosure; the
   mechanism is established and modelled in the run's own revenue doc.)
4. **Expert-advice liability (K7).** Health/finance/legal agents give advice *as
   the expert*. The run's own thesis flags this; mitigation is excluding
   regulated categories or enforced disclaimers. No external citation added, but
   it is a recognized category risk.

### 7. Timing ("why now")

**Partially validated.** The enabling tech (RAG + memory + cheap model routing)
and payout rails (Stripe Connect) are real and commoditized, and competitors
ship on them today. The claim that "platforms are experimenting with usage-based
creator payouts for AI agents" is **validated but with a warning flag**: Poe
(2024) and OpenAI's GPT Store (2024) both launched usage-based AI-creator
payouts — but **GPT Store's remains invite-only and largely unpaid two years
on**, showing usage-based AI payouts are easy to announce and hard to make
meaningful. Timing for the *tech* is right; timing for *usage-based AI payouts
clearing real money to long-tail experts* is unproven.

### Confidence

**Medium.** High confidence on competitor monetization/splits and on the
user-centric-vs-pro-rata precedent (multiple direct sources). Lower confidence
on the specific "AI expert-agent" market size (no dedicated public figure) and
on end-user willingness-to-pay for an *all-access bundle* specifically (proven
demand is for single named experts). The evidence most strongly supports the
**payout-architecture** thesis and most strongly challenges the **creator-
economics attractiveness vs Patreon/Delphi** and the **demand for a bundle**.

### Sources

- Creator economy market size 2026: https://fungies.io/digital-creator-economy-2026-complete-analysis-data-trends-forecasts/ (2026)
- Digital twins reshaping creator revenue: https://khaby-8qm.pages.dev/blog/creator-economy-2026-attention-to-identity (2026)
- Delphi pricing / revenue share listing: https://www.agent37.com/blog/delphi-ai-alternative
- Delphi monetization features (own announcement): https://delphiai.substack.com/p/delphi-now-available-to-all (2025)
- Delphi creators at 7-figure revenue (CEO interview): https://tbpn-digest.vercel.app/story/2025-06-24/delphi-ceo-on-digital-clones-that-scale-personal-expertise-coaches-and-authors-generating-7-figure-revenues (2025-06-24)
- Poe price-per-message + subscription bounty: https://techcrunch.com/2024/04/09/poe-introduces-a-price-per-message-revenue-model-for-ai-bot-creators (2024-04-09)
- Poe mechanics / points-to-dollars: https://voicebot.ai/2024/04/09/poe-rolls-out-price-per-message-generative-ai-chatbot-monetization/ (2024-04-09)
- Poe revenue estimate (third-party, unverified): https://www.usagepricing.com/blueprint/poe
- GPT Store usage payouts invite-only, creators unpaid: https://wirednews.pages.dev/story/openai-gpt-store (2024)
- GPT Store status / revenue share thread: https://community.openai.com/t/what-is-the-status-with-gpt-store-revenue-share/839172
- SoundCloud Fan-Powered (user-centric) mechanics + scale: https://musicbusinessworldwide.com/soundcloud-is-about-to-revolutionize-streaming-payouts-launching-user-centric-royalties-for-100000-indie-artists
- SoundCloud/MIDiA one-year results, ~60% more: https://www.musicweek.com/digital/read/soundcloud-marks-one-year-of-user-centric-royalties-with-fan-powered-friday/085716
- User-centric reduces streaming fraud (opinion): https://variety.com/2023/music/opinion/how-to-stop-streaming-fraud-1235666090
- User-centric not uniformly fairer: https://nialler9.com/new-report-says-user-centric-streaming-models-may-not-be-fairer-for-all-artists
- Deezer artist-centric = capped pro-rata hybrid: https://musicbusinessworldwide.com/deezers-artist-centric-model-now-has-a-new-element-dubbed-user-centric
- Patreon fees 2026: https://schoolmaker.com/blog/patreon-pricing
- Substack 10% + Stripe (~13% all-in): https://www.builtbyfoundry.io/blog/substack-vs-patreon-2026-which-earns-creators-more

---

## Cross-cutting read

- **The payout *architecture* is the defensible part; the creator *economics*
  are the weak part.** User-centric net-contribution attribution is validated by
  SoundCloud's Fan-Powered Royalties (fraud-resistant, generally pays engaged-
  audience creators more) and is more rigorous than Poe or GPT Store. But every
  incumbent an expert knows (Patreon/Substack 10% fee; Delphi ~85% rev-share on
  a self-set price) lets them keep far more per engaged subscriber than Avee's
  ~$3–5 at a 50/50 split of a platform-set $20–25 price.
- **GPT Store is the single most instructive precedent — and it is a warning.**
  Usage-based AI-creator payouts launched in 2024, stayed invite-only/US-only,
  paid most builders nothing, and drove creators to affiliate/ads. Avee's
  transparent public earnings dashboard directly attacks GPT Store's worst flaw
  (opaque analytics) — real whitespace — but doesn't solve the "payouts are tiny"
  problem.
- **Demand is proven for *specific trusted experts* (Delphi 7-figure creators),
  not for an *all-access multi-expert bundle*** at the ChatGPT-Plus price point.
  The idea's own risk notes and the revenue-model doc both flag this; external
  evidence corroborates rather than relieves it.
- **Evidence most supports:** the technical/payout wedge and the choice of
  user-centric over pro-rata. **Evidence most challenges:** demand-side WTP for a
  bundle, two-sided cold start under 50 users, and whether ~$3–5/engaged-sub can
  pull supply away from 85–90%-keep alternatives. The specific AI-expert-agent
  market is real and growing but **publicly unsized**.
