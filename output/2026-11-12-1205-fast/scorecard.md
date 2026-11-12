# Scorecard — run 2026-11-12-1205-fast (v2, re-scored)

> Single-idea run. Re-scores **IDEA-01 — Avee: expert agents paid by usage** on
> the standard rubric after three material changes since v1: (1) `ideas.md` was
> corrected with founder input (one-to-one distribution, credential-first trust,
> small-expert economics), (2) `signals.md` now exists with 18 evidenced signals,
> and (3) a further founder bullet, "Deliverables, not just answers" (tool-made
> decks/slides/designs + multi-owner compare). Weights: **Composite = 0.40×D +
> 0.35×V + 0.25×F**. Gates: Advance ≥ 7.5, Iterate 6.0–7.4, Park < 6.0 (thresholds
> never lowered). Evidence base: `signals.md` (18 signals), `market-research.md`
> (confidence: Medium), `revenue-model.md` (v1 spec §7). The "Deliverables" bullet
> has **no external evidence yet**, so every score effect from it is labelled
> **inference** and nets to roughly zero on the rounded scores (see its section).
> v1 scored 5.1 Park on a thesis kill (K6, no signals) and a bundle framing the
> founder has since corrected.

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
| K6 — Evidenced pain | **Pass** | **This is the decisive change from v1.** `signals.md` now carries first-hand, dated customer language: SIG-01 (Ken Deng, DEV, Mar 6 — "I'd run out of time", fetched verbatim), SIG-02 (Josh Spector, fetched verbatim), SIG-05/06 (Delphi Trustpilot + help-center, fetched verbatim), SIG-16 (JustAnswer recurring ~$46–55/mo, credential-gated). K6 is comfortably met. |
| K7 — No high-liability space | **Pass (conditional, at-risk)** | Expert-advice agents in health/finance/legal give advice *as the expert*; the credential-first angle *raises* K7 stakes because a falsely verified "Harvard-trained" badge is itself a liability, and a deck sold "from a VC" must be framed as *built with that expert's agent*, not endorsed by the human. Structurally removable in the wedge: exclude regulated categories, verify conservatively, label AI deliverables honestly. Manageable, not forcing. |

**Forcing verdict:** **No kill rule fires.** K6 — the v1 killer — now passes on strong,
dated, first-hand signals. K2/K7 are conditional on automated, conservative
credential verification and honest deliverable framing; K5 passes weakly. The idea
is therefore gated on its **composite**, not force-parked.

---

## Ranked summary table

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|---|---|---|---|---|---|---|---|
| 1 | IDEA-01 | Avee: expert agents paid by usage | 6 | 5 | 7 | 5.9 | Park |

---

## Detailed card

### IDEA-01 — Avee: expert agents paid by usage  ·  Composite: 5.9  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 7 — Painkiller-grade evidence now exists on both sides: the capacity-capped expert turning away paying demand (SIG-01, strong, verbatim) and recurring WTP for *credential-gated* answers (SIG-16, JustAnswer ~$46–55/mo). Tempered by the AI-substitution objection — SIG-11 ("it feels fake / I want the real person") and SIG-05 ("sounds just like a normal ChatGPT chat") — which show the *human* is the proven painkiller; the AI agent inherits only part of that intensity.
- Demand evidence: 6 — Strong for the adjacent behaviours the corrected framing relies on: WTP for a *specific named expert* (SIG-03 strong — Intro $776–$5k; SIG-12), credential-gated recurring WTP (SIG-16 strong), and a category validated by Delphi's $16M Sequoia Series A (SIG-09). Capped below 7 because the specific leap — paying recurring for an *AI agent* of a credentialed expert — is still disconfirmed by SIG-05, SIG-10 (experts refuse) and SIG-11 (audiences distrust clones). The founder's one-to-one correction *aligns* the idea with SIG-12 (demand is for one named expert, not a bundle). No external demand evidence for deliverables (inference only).
- Willingness to pay: 6 — JustAnswer proves durable recurring WTP for credential-gated answers at ~$46–55/mo, *above* Avee's $20–25 (SIG-16); Intro proves four-figure WTP for specific experts (SIG-03). Both are for **human-delivered** output, so they de-risk the price point but not AI delivery. *Inference:* the new "Deliverables" bullet (decks/slides/designs with a market price) plausibly raises WTP vs pure Q&A, but there is **no evidence** for it and Gamma/Beautiful.ai render slides cheaply/free, so the premium rests entirely on "the expert's judgment/style" — unproven. Net: held at 6.
- Founder–market resonance: 4 — The persistent weakness. Solo technical founder, observer of these communities, **named no expert segment and no privileged access** (founder-profile). Credential-first and deliverable-tooling play to his technical edge (verification, generation pipelines already built), but he still has no warm channel into either side of a two-sided trust market.

**Viability — 5**
- Market size & growth: 6 — Containing creator economy large and growing (~$234–324B 2026, double-digit CAGR, research §1); the specific AI-expert-agent sub-market is **publicly unsized** (research §1) but externally validated by Delphi's Sequoia round (SIG-09) and JustAnswer's proven credential-gated market (SIG-16).
- Monetization & unit economics: 6 — Two-sided read, and both the reframe and the deliverables bullet *improve the rationale*. Platform side rigorous: user-centric net contribution keeps ~40–45% of gross with the cap (revenue-model §3). Creator side split: ~$3–5/engaged-sub loses to Delphi ~85% / Patreon ~90% for *audience-rich* experts (research §3, the dominant evidenced risk), **but** for small/audience-less credentialed experts Avee beats Delphi (a $79–299/mo cost with no built-in monetization, SIG-06) below ~9 subscribers. *Inference:* deliverables run on credits (cost × 2), so they are margin-accretive rather than margin-eroding if metered — a positive for unit economics, unproven. Held at 6.
- Defensibility / moat: 5 — Up from v1. Automated credential verification + credential discovery is a harder-to-copy asset than a payout dashboard and attacks a real gap (Delphi shows no structured credentials, SIG-13; no EU/GDPR posture, SIG-14). *Inference, net-neutral:* multi-owner "compare a VC's deck vs a founder's vs a designer's" is a genuine Delphi gap **and** a reason to use several agents, but the deliverable itself sits in a crowded, well-funded market (Gamma, Beautiful.ai) where the only defensible layer is the expert's judgment, not the renderer — so it widens the surface as much as the moat. Held at 5.
- Go-to-market realism: 4 — Two-sided cold start under 50 users, no seeded side, no named niche, founder has no warm channel. The reframe gives a *coherent* loop (experts share their own agent with their own audience — matches SIG-12), and the compare-across-owners feature *inference* gives the bundle a reason to exist, but there is still zero demand traffic to pull on. Credential discovery is a post-liquidity flywheel, not a cold-start engine (see SIG-18).
- Timing ("why now"): 6 — Up from v1. The competitive whitespace is open *now*: Delphi raised but still ships with no built-in monetization (SIG-06), no verified credentials (SIG-13), no EU posture (SIG-14), and chat-only (no deliverables). Counterweight: GPT Store shows usage-based AI payouts stayed invite-only and paid most builders $0 two years on (research §7).

**Feasibility — 7**
- Technical complexity vs. capability: 7 — Product already built on the founder's core stack (agents, RAG, semantic memory, cheap routing), **and image/video/voice generation already ships** (founder-profile), so deliverable tooling is incremental, not net-new. The new credential-verification layer (diploma/employment checks) is partly outside the demonstrated stack and is load-bearing, which holds this below an 8.
- Capital / resources vs. runway: 7 — Bootstrapped and solo; the cost cap + media-on-credits keep infra below price so heavy users and heavy generation don't burn runway. Third-party credential/identity verification adds some cost.
- Time to testable MVP: 7 — The billing/payout layer is ≤ 4 weeks part-time on an existing product; deliverables and generation already exist; demand can be tested with lightweight/manual verification of a handful of experts. The fully automated credential asset is a scale-up build, not an MVP blocker.
- External dependencies: 5 — Stripe Connect (KYC, DAC7/1099, chargebacks), mobile-IAP avoidance, credential-verification dependencies (Europass, LinkedIn/work-email, employer policy), K7 expert-advice **and** deliverable-attribution liability. More third-party and regulatory surface than a pure billing layer.

**Composite:** `0.40×6 + 0.35×5 + 0.25×7` = **5.9**
**Gate decision:** **Park** — composite 5.9 sits ~0.1 below the 6.0 Iterate floor; thresholds are not lowered. No kill rule fires (K6 now passes), so this is an evidence-based near-miss, not a force-park. What holds it under the line is unproven *demand* for the AI delivery and weak founder–market resonance, against a strong-but-adjacent evidence base.
**Biggest unknown:** Will an expert's own audience pay $20–25/month to talk to that expert's **AI agent** (or buy an AI-made deck "in the expert's style"), not the human — and will credentialed experts accept ~$3–5 per engaged subscriber to publish one? Every strong signal (SIG-03, SIG-16) proves WTP for the *human*; SIG-05/SIG-11 disconfirm the AI substitution; the deliverables upside is inference-only. Resolving this moves the score most in either direction.
**De-risking step:** Pick one named credentialed niche the founder can reach 10 of this week (e.g. independent consultants in r/consulting, SIG-18), recruit 3–5 to publish credential-fronted agents, and pre-sell the one-to-one subscription — *including a paid deliverable* (an AI-made deck/design in the expert's style) — to their existing audiences. Capture first-hand WTP for AI delivery and the deliverable **and** expert payout-acceptance before building the automated verification asset.

---

## Factoring "Deliverables, not just answers" (founder input — inference only)

No external evidence exists for this bullet yet, so every effect below is **inference**;
none changed a rounded sub-score enough to move a dimension, and the net is roughly zero.

- **WTP (inference, mild positive, hedged):** Deliverables (pitch decks, PPT, images,
  designs) have an explicit market price, so WTP is plausibly higher than for Q&A.
  But Gamma/Beautiful.ai/Tome already render decks cheaply or free, so any premium
  rests on "shaped by the expert's judgment/style," which is unproven. Mild lift,
  fully offset by commoditised competition → WTP held at 6.
- **Differentiation vs Delphi (inference, positive):** Delphi's clones are chat-only
  (SIG-13 observed cards show perspective, not tools). Tool-made deliverables and a
  **multi-owner compare** (a VC's deck vs a founder's vs a designer's) are a clear gap
  Delphi does not occupy — a real, if copyable, differentiator. Folded into moat/timing.
- **Cross-agent usage for the payout model (inference, positive — the most useful
  effect):** The user-centric payout formula rewards the agents a subscriber *actually
  used*. v1's structural weakness was that a subscriber who joins via expert A mostly
  uses A's agent, so the "all-access" split rarely spreads. "Request several versions
  from several owners and compare" is a native reason to use multiple agents in one
  session, which both legitimises the all-access price and distributes the creator
  pool — directly strengthening the model's rationale. Still inference; folded into
  monetization.
- **Generation cost on credits (inference, neutral-to-positive):** Decks/images are
  expensive, but the revenue model already routes media to credits at cost × 2
  (revenue-model §3), so deliverables are margin-accretive if metered and do **not**
  threaten the K4 cost cap. Risk only if generation is bundled into the flat plan.
- **Competition from Gamma/Beautiful.ai (inference, negative — the main caution):**
  Entering deliverables puts Avee into a crowded, well-funded horizontal market whose
  incumbents out-render it on generic output. The only defensible layer is the expert's
  judgment/style + credential trust, not the renderer. This caps the deliverables upside
  and widens the competitive surface, which is why differentiation and WTP are held, not
  raised.
- **Framing honesty (flag):** This is the second scope expansion this run (credentials,
  then deliverables), each adding build and competitive surface with no external evidence.
  An AI deck "from the best VC" must be framed as *built with that expert's agent* (with
  optional paid human review via escalation), not as the human's endorsed work — otherwise
  it is a misrepresentation and a K7 liability. The feature is genuinely clever for the
  payout model, but risks the product drifting toward "a worse Gamma with experts attached"
  if the expert-judgment premium is not validated first.

**Net effect on scores:** inference-positive on the *coherence* of the bundle/payout story
and on differentiation, offset by commoditised competition and scope/execution risk.
Rounded scores unchanged: **D 6 / V 5 / F 7 / Composite 5.9 / Park.**

---

## The SIG-18 tension: does credential-based discovery resolve "own audience" vs "audience-less"?

The corrected idea makes two claims that pull against each other, and SIG-18
flags it explicitly (strength: medium, "in tension with the stated distribution
model"):

1. **Expert brings own audience** — each expert shares *their own* agent with
   *their own* audience; demand rests on "A's audience wants on-demand access to
   A" (the Delphi / SIG-12 pattern). This **requires** the expert to have an audience.
2. **Pedigree, not personality** — verified credentials let users *discover by
   credentials*, so an **audience-less** professional can earn (SIG-18 persona).
   This **requires Avee to supply** demand-side discovery traffic.

**Does credential-discovery resolve the conflict? Partially, and only after
liquidity — not at cold start.** The two models are sequential and complementary,
not simultaneous:

- Credential-based discovery can only monetize an audience-less professional if
  there is a pool of users *searching by credential* on Avee. That search traffic
  does not fall from the sky — at cold start (under 50 users, SIG-18 counter-signal)
  it does not exist.
- The users who search by credential arrive because **audience-bringing experts**
  (model 1) dragged their audiences onto the platform first. So the
  audience-bringing experts are simultaneously the cold-start supply *and* the
  engine that generates the discovery traffic that later lets audience-less
  professionals earn.
- Therefore the pedigree bullet **widens the eventual supply TAM and adds a second
  supply channel**, but it does **not** relieve the two-sided cold start. The first
  cohort of experts must still bring their own audiences; "audience-less
  professionals can earn" is a flywheel benefit that only switches on post-liquidity.

Net: credential-discovery is a real asset for *later* expansion and a genuine
Delphi gap (SIG-13), but SIG-18's counter-signal stands for the phase that
actually matters now — the founder cannot lean on "credentials let audience-less
experts earn" to solve cold start. The reframe does, however, resolve a *different*
tension correctly: by moving from an all-access bundle to one-to-one, the idea now
matches the evidence that WTP is for a single named/credentialed expert (SIG-12,
SIG-03), not a bundle (research §2 disconfirming). The deliverables/compare feature
cuts slightly *against* the strict one-to-one framing — multi-owner comparison is an
inherently multi-agent behaviour — which is helpful for the payout model but reopens
the "why a bundle" question the one-to-one correction had closed.

---

## Changes vs previous scorecard (v1: 5.1 Park)

| Dimension | v1 | v2 | Why it moved |
|---|---|---|---|
| Kill rules | **K6 FAIL** (force-park) | **No kill fires** | `signals.md` now supplies first-hand, dated, fetched-verbatim pain (SIG-01, 02, 05, 06, 16). K6 was the v1 killer; it now passes. K5 upgraded to weak-pass via the credential/SIG-18 persona. |
| Desirability | 4 | **6** | Demand evidence 3→6 and pain 5→7: the corrected one-to-one framing aligns the idea with proven single-expert WTP (SIG-03, SIG-12) and credential-gated recurring WTP (SIG-16), instead of the unproven bundle v1 scored. Deliverables add inference-only WTP upside. Still capped by AI-substitution disconfirmers (SIG-05, SIG-11) and resonance (held at 4). |
| Viability | 5 | **5** | Net flat, composition shifted: timing 5→6 and moat 4→5 (Delphi's live monetization/credential/EU/chat-only gaps are now evidenced whitespace — SIG-06, 13, 14), offset by the creator-economics headwind the evidence *confirms* (research §3) and, by inference, Gamma/Beautiful.ai competition on deliverables. Monetization reframed: Avee beats Delphi for small/audience-less experts (SIG-06), weak for stars; deliverables help the cross-agent payout rationale (inference). |
| Feasibility | 7 | **7** | Unchanged headline. Product-already-built advantage persists (incl. generation pipelines for deliverables); offset by the new, load-bearing automated-credential-verification build and its external dependencies (external-deps held at 5). |
| Composite / Gate | 5.1 / Park (thesis kill) | **5.9 / Park (near-miss)** | +0.8 on genuinely stronger, better-aligned evidence — but still under the 6.0 floor. The nature of the Park changed: v1 was a forced thesis kill; v2 is an evidence-based near-miss on unproven AI-delivery demand and thin founder–market resonance. |

**Honest note on not inflating:** the founder's pushback corrected the *framing*
(which the evidence rewards) and added features (credentials, deliverables) with no
external proof that audiences will pay for the *AI* rather than the human — the
strongest signals (SIG-03, SIG-16) remain human-delivered, and SIG-05/SIG-11 actively
disconfirm the substitution. Scoring 5.9 rather than nudging to 6.0, and holding the
deliverables effects as inference, reflects that the demand leap is still open.

---

## Revenue model verdict (revenue-model.md §7 v1 spec)

**What holds (unchanged and still strong):**
- **The margin is structural, not hopeful.** 50% of net contribution P = max(N − C, 0)
  fixes the §2 contradiction — the platform keeps ~40–45% of gross on every
  subscriber every month, instead of its profit depending on user behaviour.
- **The fair-use cost cap + media-on-credits is what makes K4 true.** Without it a
  single frontier-model power user loses $20–90/month (§2). It also absorbs the new
  deliverables cost — decks/images on credits (cost × 2) — so generation does not
  break the cap. Keep it non-negotiable.
- **Fraud resistance is the model's best property and it is evidenced.** User-centric
  attribution makes self-dealing and collusion rings lose money, corroborated by
  SoundCloud Fan-Powered Royalties (research §5). Do not switch to a pooled model.
- **Ops stay solo-operable** via Stripe Connect Express, 45-day holds, $25 minimum
  payout (K2) — conditional now on credential verification staying automated.

**What the new evidence/input changes:**
- **The small-expert wedge is now evidenced, and it is the right pitch.** SIG-06
  confirms Delphi ships with "Monetization isn't built into Delphi" while charging
  $79–$299/mo; SIG-08 shows Coachvox's flat $99/mo is "steep for coaches just
  starting out." For a credentialed expert *without* a large audience, Avee's
  free-to-join, model-costs-covered, usage-paid model is **more generous than
  Delphi below ~9 paying subscribers**. Lead supply acquisition here.
- **Credential-gated recurring WTP is real at a price above Avee's.** JustAnswer
  (SIG-16) proves consumers pay ~$46–55/mo recurring for answers gated behind a
  *verified* credential. Caveat: human-delivered, and its trust wound is deceptive
  billing — which Avee's transparent dashboard and honest pricing can flip (SIG-07).
- **Deliverables strengthen cross-agent usage (inference).** Multi-owner compare is a
  native reason to use several agents, which legitimises the all-access price and
  spreads the creator pool — addressing v1's "the split rarely spreads" weakness. Run
  deliverables on credits so they add margin, not cost.

**What is still weak (evidence confirms, not relieves):**
- **The AI-delivery demand leap is unproven** — SIG-05 and SIG-11 are active
  disconfirmers; the deliverables premium over Gamma/Beautiful.ai is inference-only.
- **Star-expert economics stay unattractive** — ~$3–5/engaged-sub vs 85–90% keep
  elsewhere (research §3); GPT Store is the cautionary precedent (research §7).
- **The headline "≥ $5" promise isn't free** — it needs $24.99 pricing or a 60% split
  (§3); at a round $20 the expert gets ~$3.20–4.50.
- **Long-tail payout friction** — $25 minimum + ~$2/account/month Stripe fees mean
  audience-less experts net ~$0 for months before discovery traffic exists (the SIG-18
  cold-start problem), which can sour supply before liquidity builds.

**Single change that would most raise the score:** Lead the creator pitch with the
**credential-fronted, small-expert** segment where Avee's economics beat Delphi
(free vs $79–299/mo sunk cost, SIG-06), plus a high-share private-agent / paid-escalation
/ paid-deliverable layer (expert keeps ~80%). Demote the ~$3–5 all-access pool to passive
upside. This aligns the offer with the only experts the evidence says Avee can out-compete
today, and attacks both the thin-payout risk and cold start.

---

## Top recommendation

There is one idea this run and it does not clear the gate: **IDEA-01 is Parked at
5.9** — a 0.8-point rise from v1 and a genuine near-miss (within 0.1 of the Iterate
floor), no longer a thesis kill. The new `signals.md` clears K6 and the one-to-one,
credential-first reframe aligns the idea with proven WTP for single trusted experts
(SIG-03, SIG-12) and credential-gated recurring payment (SIG-16); the "deliverables"
bullet is a clever strengthener of the cross-agent payout story but is **inference only**
and lands in a crowded market (Gamma/Beautiful.ai), so it does not move the gate. What
still holds the idea under the line is that every strong signal proves WTP for the
**human**, while SIG-05/SIG-11 disconfirm paying for the **AI** — and the founder has no
warm channel into either side. Highest-priority validation step: recruit 3–5 credentialed
experts from one named niche (e.g. r/consulting, SIG-18), publish credential-fronted agents
with one paid deliverable, and pre-sell their own audiences on the one-to-one subscription —
capturing first-hand WTP for AI delivery *and* expert payout-acceptance before building the
automated credential asset. Resolving that single unknown is what moves IDEA-01 from Park
toward Advance.
