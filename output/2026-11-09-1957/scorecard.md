# Scorecard — run 2026-11-09-1957

> Scored by the Governance agent against `ideas.md` and `market-research.md`,
> judged against `founder-profile.md` (solo, bootstrapped, deeply technical
> agent/infra founder; part-time; cheap per-agent infra is the edge; has ruled
> out heavy manual trust & safety; virality is the headline goal).
> **Weights (CLAUDE.md default):** `Composite = 0.40×Desirability + 0.35×Viability + 0.25×Feasibility`.
> **Gate thresholds:** Advance ≥ 7.5 · Iterate 6.0–7.4 · Park < 6.0.
>
> **Headline:** No idea clears the Advance bar. That is the honest read of the
> evidence, not timidity — the one best-proven mechanic (pay-to-steer a live AI
> performer with a known human owner) is strong on *demand* but every candidate
> is gated by one of three recurring constraints: real-time multimodal
> **inference cost vs. $5/season**, **automated moderation** of open/subjective
> output, or **legal exposure** (defamation, music-IP, gambling). The top cluster
> is a tight Iterate band; the task now is to run the single cheapest experiment
> that de-risks the leader.

## Ranked summary

| Rank | ID | Title | Desirability | Viability | Feasibility | Composite | Gate |
|------|----|-------|:---:|:---:|:---:|:---:|------|
| 1 | IDEA-04 | Coach Mode (audience-coached improv) | 8 | 7 | 5 | **6.90** | Iterate |
| 2 | IDEA-09 | Discord-Native Guild Leagues | 7 | 6 | 7 | **6.65** | Iterate |
| 3 | IDEA-01 | Agent Arena (skill league) | 6 | 6 | 7 | **6.25** | Iterate |
| 4 | IDEA-07 | My Agent, My Fighter (progression RPG) | 6 | 7 | 5 | **6.10** | Iterate |
| 5 | IDEA-05 | Debate Ladder | 6 | 6 | 6 | **6.00** | Iterate |
| 6 | IDEA-03 | Roast League (comedy/roast) | 6 | 6 | 5 | **5.75** | Park |
| 7 | IDEA-06 | Band Camp for Agents (creative) | 6 | 6 | 5 | **5.75** | Park |
| 8 | IDEA-10 | Open-Entry Underdog League | 6 | 5 | 5 | **5.40** | Park |
| 9 | IDEA-08 | Clip Factory (clip-loop-first) | 5 | 5 | 6 | **5.25** | Park |
| 10 | IDEA-02 | FactFight (fact-check battles) | 4 | 4 | 5 | **4.25** | Park |

---

## Detailed cards (ranked order)

### IDEA-04 — Coach Mode (audience-coached improv)  ·  Composite: 6.90  ·  Gate: Iterate

**Desirability — 8**
- Pain intensity: 7 — Real two-sided pull: owners want a crowd that plays with their agent; the audience wants to influence the show. More painkiller than vitamin for the audience-engagement side.
- Demand evidence: 8 — Strongest in the set. "85% of AI-VTuber superchats introduce new topics/actions" and the arXiv fandom study make pay-to-steer a *demonstrated recurring behaviour*, not a hypothesis (research Confidence: Medium-High).
- Willingness to pay: 8 — Audiences already pay to steer live AI performers today; monetization sits on proven behaviour rather than a flat $5 guess.
- Founder–market resonance: 7 — Agent-design taste + reachable builder communities fit; latency-sensitive multi-agent infra is squarely the founder's strength.

**Viability — 7**
- Market size & growth: 7 — AI-performer category is fundable (a16z led Shizuku AI ~$75M, Feb 2026); audience side is mass-consumer, not just the ~285-builder niche.
- Monetization & unit economics: 6 — Pay-to-steer revenue is proven but *highly unequal* (arXiv income-inequality study: a few channels capture most superchat income) — a structural warning for a many-owners tipping economy; concurrent steered streams multiply the ~$3–30/hr real-time multimodal cost.
- Defensibility / moat: 5 — Neuro-sama owns single-performer steering; the many-owner troupe is open whitespace but not inherently defensible beyond the infra-cost edge.
- Go-to-market realism: 7 — Community-led growth across AI/creator Discords and X is exactly the founder's comfort zone.
- Timing: 8 — Validated: pay-to-steer is live on Twitch today and real-time multimodal pipelines are newly affordable.

**Feasibility — 5**
- Technical complexity vs. capability: 5 — Low-latency, responsive multi-agent steering at scale is genuinely hard for a solo, part-time founder, even a strong one.
- Capital / resources vs. runway: 5 — Inference cost is load-bearing; $5/season covers very little real-time multimodal compute. Directly presses the anti-goal "unit economics that break at scale."
- Time to testable MVP: 6 — A working prototype exists; a single improv stage with paid prompts is scoped, but "responsive at scale" is the hard part.
- External dependencies: 4 — Open audience prompting is a live prompt-injection/abuse vector; Kick (Mar 2026) now mandates AI labelling and bans harmful AI content. Automated real-time moderation is the founder's stated *gap*, not strength.

**Composite:** `0.40×8 + 0.35×7 + 0.25×5` = **6.90**
**Gate decision:** Iterate — best-evidenced demand mechanic in the set, gated by whether abuse moderation can be automated and whether concurrent-stream economics survive $5/season.
**Biggest unknown:** Does status/payment behaviour *spread across many owners*, or does a winner-take-most dynamic (the superchat inequality finding) concentrate it onto one star agent — collapsing the multi-owner thesis?
**De-risking step:** Run one always-on improv stage with 10–20 owner agents and paid audience steering for 2–4 weeks; measure (a) whether >1 owner accrues durable followers/repeat steering, and (b) steering revenue per stream-hour vs. inference cost per stream-hour.

### IDEA-09 — Discord-Native Guild Leagues  ·  Composite: 6.65  ·  Gate: Iterate

**Desirability — 7**
- Pain intensity: 6 — Community admins have a real, recurring job ("give members a reason to come back daily"); solid but closer to vitamin than acute pain.
- Demand evidence: 7 — Leveling/leaderboard bots (MEE6, Arcane, Tatsu) are a large, established, monetized category — proven appetite for gamified server activity.
- Willingness to pay: 6 — Premium server tiers at $8–12/mo are an existing precedent; $5/agent/season is plausible against it.
- Founder–market resonance: 8 — Direct access to AI/dev/no-code Discords is the founder's explicitly fastest first-100 path; bot-native GTM is exactly the stated comfort zone.

**Viability — 6**
- Market size & growth: 6 — Crowded with incumbents (a sign the space is real), but the agent-vs-agent-league wedge is open.
- Monetization & unit economics: 6 — Server-to-server spread with near-zero CAC; isolated leagues let matches batch cheaply (helps the cost edge vs. always-on multimodal).
- Defensibility / moat: 5 — Bot category is crowded and low-barrier; moat is community lock-in, not tech.
- Go-to-market realism: 8 — Cheapest cold-start in the set; sidesteps the standalone-feed cold-start that the prior run showed kills AI destinations.
- Timing: 6 — Discord is where builders live now; no acute "why now" beyond that.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — A Discord bot running isolated text/light-multimodal leagues is well within a solo infra founder's reach.
- Capital / resources vs. runway: 7 — Batched, non-always-on matches are far cheaper than a 24/7 multimodal stream — friendly to a tight budget.
- Time to testable MVP: 8 — Fastest MVP in the set; a league bot can ship in weeks into servers the founder already reaches.
- External dependencies: 6 — Discord platform/ToS risk and bot-API limits, but no novel legal exposure.

**Composite:** `0.40×7 + 0.35×6 + 0.25×7` = **6.65**
**Gate decision:** Iterate — cheapest, fastest, most-reachable path to a live signal, but structurally in tension with the founder's headline virality goal.
**Biggest unknown:** Does fragmenting across servers dilute the shared status/audience that makes owner-recognition meaningful — and does Discord-contained content starve the viral clip loop the founder actually wants?
**De-risking step:** Ship the league bot into 3–5 friendly Discords and measure daily-active-member lift *and* whether auto-clips escape the server (cross-posts/shares to X/TikTok). If clips stay trapped, the virality goal needs a different surface.

### IDEA-01 — Agent Arena (skill league)  ·  Composite: 6.25  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — Builders genuinely lack a public, verifiable benchmark venue; real but a professional-pride pain, not acute.
- Demand evidence: 6 — Strong *builder-side* signal (Kaggle Game Arena, AgentArena, TinyAIArena, LMArena culture), but the research flags skill contests as "legible to builders, boring to a broad audience" — the consumer loop the founder needs is unproven.
- Willingness to pay: 5 — $5 to be ranked is plausible for serious builders but unvalidated; no spectator-monetization proof here.
- Founder–market resonance: 8 — Founder reaches builder communities directly and has deep agent-design taste; closest founder–customer fit in the set.

**Viability — 6**
- Market size & growth: 6 — Beachhead is a few-thousand-builder niche [inference]; no mass TAM evidenced yet.
- Monetization & unit economics: 6 — Objective, short, batchable matches are the *cheapest* format to run — best alignment with the infra cost edge.
- Defensibility / moat: 5 — Crowded with adjacent, well-funded players (Kaggle Game Arena is Google-backed); differentiation is persistent owner-status/seasons.
- Go-to-market realism: 7 — Reachable first entrants via dev Discords/hackathons.
- Timing: 8 — "Why now" validated: agent tooling matured, arenas are a live 2026 trend, and this maps cleanest onto the skill-contest legal safe harbour.

**Feasibility — 7**
- Technical complexity vs. capability: 8 — Objective win-conditions make scoring and moderation trivial to automate; squarely the founder's strength.
- Capital / resources vs. runway: 7 — Short batched contests keep inference cost low; $5/season is more defensible here than anywhere else.
- Time to testable MVP: 7 — Prototype exists; a single head-to-head format with a ladder is tightly scoped.
- External dependencies: 7 — Skill-predominance safe harbour is the cleanest legal footing in the set; automatable moderation.

**Composite:** `0.40×6 + 0.35×6 + 0.25×7` = **6.25**
**Gate decision:** Iterate — the safest, cheapest, most-buildable idea, but its demand ceiling is a narrow builder audience, not the viral consumer traction the founder is chasing.
**Biggest unknown:** Can an objectively-scored skill ladder attract a *spectating* audience beyond the competing builders — or does the "boring to a broad audience" risk cap it as a dev tool?
**De-risking step:** Stand up a minimal always-on head-to-head ladder, auto-clip the most dramatic finishes, and measure non-builder viewer retention and clip pickup — i.e. test the entertainment ceiling before investing in seasons/cosmetics.

### IDEA-07 — My Agent, My Fighter (progression RPG)  ·  Composite: 6.10  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 6 — Directly attacks the founder's core hypothesis (owners return for durable, growing status), but the pain is aspirational, not yet felt.
- Demand evidence: 6 — Gacha/progression is battle-tested in gaming and AI-VTuber fans bond with persistent characters (arXiv), but the specific "owners come back for their agent's reception" loop is the untested hypothesis itself.
- Willingness to pay: 7 — Progression monetization (cosmetics, season passes, re-rolls) is among the most proven consumer spend engines.
- Founder–market resonance: 6 — Agent-as-character taste fits, but consumer game-design polish is a stated team gap for a solo technical founder.

**Viability — 7**
- Market size & growth: 7 — Gacha/progression is a proven large-scale retention and monetization engine.
- Monetization & unit economics: 7 — Richest monetization surface in the set (cosmetics + passes + re-rolls layered on $5 entry).
- Defensibility / moat: 6 — Persistent, owned, evolving agent-identity creates real switching cost if it takes hold.
- Go-to-market realism: 6 — Community-led, but needs the base contest to be entertaining first.
- Timing: 7 — Cheap persistent agent memory/identity + proven gacha retention; the open question is content quality, not timing.

**Feasibility — 5**
- Technical complexity vs. capability: 5 — Progression layer is doable, but it only works atop a *fun, spectate-able* base game — the research's key risk.
- Capital / resources vs. runway: 5 — Builds on whichever live format it wraps, inheriting that format's inference cost.
- Time to testable MVP: 5 — More to build than the leaner ideas: a working contest *and* a progression/identity system.
- External dependencies: 6 — Paid re-rolls/boosts brush the paid-entry/chance legal line; manageable with a skill-predominant base.

**Composite:** `0.40×6 + 0.35×7 + 0.25×5` = **6.10**
**Gate decision:** Iterate — the most direct test of the founder's retention thesis with the strongest monetization, but hostage to base-game entertainment quality and a design-polish gap.
**Biggest unknown:** Is the underlying live performance entertaining enough to spectate at all? Progression retention cannot rescue a boring base loop.
**De-risking step:** Reframe as a thin progression layer over whichever format wins the leader's experiment (IDEA-04 or IDEA-01); A/B whether XP/evolving avatars measurably lift owner D7/D30 return vs. a no-progression control.

### IDEA-05 — Debate Ladder  ·  Composite: 6.00  ·  Gate: Iterate

**Desirability — 6**
- Pain intensity: 5 — "Prove my agent reasons persuasively" is a real but mild, builder-centric itch.
- Demand evidence: 6 — Clashboard (debate arena with spectator staking) is a working analogue showing built-in betting demand; debate-curious audiences exist.
- Willingness to pay: 5 — $5 ladder plausible; no direct WTP proof.
- Founder–market resonance: 7 — Reasoning/persuasion orchestration is core founder depth.

**Viability — 6**
- Market size & growth: 6 — Adjacent to agent-arenas; no mass TAM evidenced.
- Monetization & unit economics: 6 — Rubric-scored debates are batchable and moderately cheap.
- Defensibility / moat: 5 — Clashboard and general arenas are adjacent; differentiation is persistent owner ELO.
- Go-to-market realism: 6 — Debate is less natively shareable than comedy, narrowing the clip loop.
- Timing: 7 — LLM reasoning is strong enough; objective-ish scoring is the safest content per founder constraints.

**Feasibility — 6**
- Technical complexity vs. capability: 7 — Fixed rubric (structure/rebuttal/evidence) makes scoring automatable; bounded motions keep content contained.
- Capital / resources vs. runway: 6 — Batchable, moderate cost.
- Time to testable MVP: 7 — A timed, motion-based format is well-scoped.
- External dependencies: 5 — Real motions drift into politically charged territory, straining automated moderation.

**Composite:** `0.40×6 + 0.35×6 + 0.25×6` = **6.00**
**Gate decision:** Iterate — a safe, buildable middle between "boring skill contest" and "unsafe roast," but limited viral/clip upside caps the founder's headline goal.
**Biggest unknown:** Can motion-constrained debate clips be made *shareable* to a mass audience without drifting into charged political content that breaks automated moderation?
**De-risking step:** Run a short season on deliberately neutral/absurd motions, auto-clip the best exchanges, and measure clip shareability vs. the comedy baseline — decide whether debate can ever feed the virality loop.

### IDEA-03 — Roast League (comedy/roast)  ·  Composite: 5.75  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — Character builders genuinely lack a stage + scoreboard; real craving.
- Demand evidence: 6 — Comedy is the most shareable category and AI-performer bits clip well, but the audience-pull signal is [inference from clip culture], not measured here.
- Willingness to pay: 6 — $5 entry plus tips plausible for passionate character builders.
- Founder–market resonance: 7 — Direct line to character.ai-style communities and comedy-is-a-taste-problem fits the founder's edge.

**Viability — 6**
- Market size & growth: 7 — Short-form comedy is the largest natively viral content category — best fit for the growth thesis.
- Monetization & unit economics: 6 — Tips + clip downloads + $5 entry; cost moderate.
- Defensibility / moat: 5 — Open whitespace but low technical barrier.
- Go-to-market realism: 7 — Clip-driven virality is exactly the founder's growth engine.
- Timing: 6 — Virality mechanics validated, but the AI-defamation frontier is unsettled and actively litigated — timing cuts both ways.

**Feasibility — 5**
- Technical complexity vs. capability: 6 — Generation is feasible; the problem is governing output, not producing it.
- Capital / resources vs. runway: 6 — Moderate cost.
- Time to testable MVP: 6 — Format is simple to stand up.
- External dependencies: 3 — The hardest moderation/liability surface in the set: AI roast output risks defamation, Section 230 likely does *not* shield the party publishing AI output, and private-figure targets need only prove negligence. Structural mismatch with a solo founder who has ruled out manual T&S.

**Composite:** `0.40×6 + 0.35×6 + 0.25×5` = **5.75**
**Gate decision:** Park — best viral fit in the set, but its defamation/moderation exposure is the worst match for a solo, no-manual-T&S founder; revisit only if automated safety filtering proves reliable.
**Biggest unknown:** Can automated moderation reliably prevent defamatory/offensive roast output at 24/7 volume without a human in the loop?
**De-risking step:** Before any launch, red-team an automated roast-safety filter against an adversarial claim/target set; measure false-negative rate on defamatory output. A non-trivial miss rate kills it for this team.

### IDEA-06 — Band Camp for Agents (creative)  ·  Composite: 5.75  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — Creative-agent makers lack a live venue/reputation system; real but mild.
- Demand evidence: 6 — Large generative-maker communities (Suno/Udio-scale) and clip-friendly output, but no measured spectator-contest demand.
- Willingness to pay: 5 — The "sell/license winning creations" revenue line is undermined because fully AI-generated tracks are often not copyrightable.
- Founder–market resonance: 6 — Multimodal pipeline engineering fits; curation taste helps.

**Viability — 6**
- Market size & growth: 7 — Generative quality crossed the "enjoyable" line; ambient creative streams have proven audiences.
- Monetization & unit economics: 4 — Licensing revenue is legally shaky (uncopyrightable AI output) and generation cost is non-trivial.
- Defensibility / moat: 5 — Creation tools dominate; only the venue is open.
- Go-to-market realism: 6 — Clip-friendly, community-led.
- Timing: 6 — Validated on quality; challenged on legal/monetization footing.

**Feasibility — 5**
- Technical complexity vs. capability: 6 — Multimodal generation pipeline is the founder's strength.
- Capital / resources vs. runway: 5 — High-volume generation cost on a tight budget.
- Time to testable MVP: 6 — Theme-to-creation round is scoped.
- External dependencies: 3 — Live RIAA Suno/Udio litigation (damages could top $9B; Suno admitted training on copyrighted recordings) makes music IP a serious, unresolved exposure.

**Composite:** `0.40×6 + 0.35×6 + 0.25×5` = **5.75**
**Gate decision:** Park — good content fit, but unresolved music-IP litigation and uncopyrightable output undercut both safety and the monetization line.
**Biggest unknown:** Can the format sidestep training-data/IP liability (e.g. licensed or clearly-original generation) while keeping output enjoyable and monetizable?
**De-risking step:** Scope to non-music modalities (image/story) with cleaner IP posture and test whether a live creative-contest venue retains both makers and a spectating crowd before touching generated music.

### IDEA-10 — Open-Entry Underdog League  ·  Composite: 5.40  ·  Gate: Park

**Desirability — 6**
- Pain intensity: 6 — Correctly identifies that a flat $5 cold wall throttles the viral top-of-funnel the founder needs.
- Demand evidence: 6 — Audience backing/betting on AI competitors is demonstrated (Doppel/Kash on X; $6.1M crypto bot contest; Clashboard staking).
- Willingness to pay: 5 — Free entry defers revenue; paid sponsorship/backing WTP is adjacent-proven but unvalidated for this funnel.
- Founder–market resonance: 6 — Cost edge is what makes a free tier even conceivable; GTM fits.

**Viability — 5**
- Market size & growth: 6 — Freemium + creator-economy backing mechanics are proven.
- Monetization & unit economics: 4 — A free tier floods low-quality agents and the economics break if free real-time compute outruns the founder's cost edge — hits the anti-goal head-on.
- Defensibility / moat: 5 — Betting-on-AI space is forming; differentiation is the free funnel + owner upside-share.
- Go-to-market realism: 6 — Free reach aids virality, but curation burden rises.
- Timing: 5 — Freemium proven, but the gambling-adjacent backing market can't launch globally without licensing.

**Feasibility — 5**
- Technical complexity vs. capability: 6 — Tiering and backing markets are buildable.
- Capital / resources vs. runway: 4 — Subsidizing free real-time multimodal compute on a bootstrap budget is the most dangerous economics in the set.
- Time to testable MVP: 6 — Buildable, but needs funnel + backing + curation.
- External dependencies: 3 — Highest regulatory risk in the set: audience betting/backing on outcomes trips the prize+chance+consideration lottery/gambling test; coverage of Doppel/Kash explicitly flags exposure.

**Composite:** `0.40×6 + 0.35×5 + 0.25×5` = **5.40**
**Gate decision:** Park — the funnel insight is correct, but free-tier compute economics and gambling-law exposure compound against a bootstrapped solo founder.
**Biggest unknown:** Can a free tier be curated and compute-capped so it doesn't bankrupt the cost edge — and can "backing" be structured to avoid gambling licensing?
**De-risking step:** Model free-tier unit economics at 10×/100× agent load against the cost edge, and strip the backing market to non-monetary points before considering any real-money layer.

### IDEA-08 — Clip Factory (clip-loop-first)  ·  Composite: 5.25  ·  Gate: Park

**Desirability — 5**
- Pain intensity: 5 — Serves the founder's distribution job more than a felt customer pain.
- Demand evidence: 4 — Strong *disconfirming* evidence: "Nothing, Forever" (AI Seinfeld) spiked to ~11.6k avg viewers then declined; modern genAI needs cherry-picking the best outputs, which a 24/7 feed can't do; novelty fatigue is documented (MIDiA).
- Willingness to pay: 4 — Clip-virality-to-paying-owner conversion is explicitly unproven.
- Founder–market resonance: 7 — This is literally the founder's own clips-as-growth thesis.

**Viability — 5**
- Market size & growth: 6 — Short-form reach is huge, but commoditized.
- Monetization & unit economics: 4 — Revenue depends on viewers→paying owners, which is unvalidated.
- Defensibility / moat: 3 — Low barrier, everyone chasing AI short-form; thin differentiation ("make the clip the product").
- Go-to-market realism: 6 — Rides existing platforms.
- Timing: 5 — genAI volume is cheap now, but platform enforcement is tightening *against* exactly this high-volume AI content.
- Timing: 5 — Mixed per above.

**Feasibility — 6**
- Technical complexity vs. capability: 7 — Auto-editing agent performances into clips is squarely feasible for this founder.
- Capital / resources vs. runway: 6 — Generation volume cost, but manageable.
- Time to testable MVP: 7 — A clip pipeline is quick to stand up.
- External dependencies: 3 — YouTube's inauthentic-content policy already terminated AI-slop channels (late 2025); Kick requires labelling; algorithms can throttle AI content overnight — the whole loop can be choked by platform policy.

**Composite:** `0.40×5 + 0.35×5 + 0.25×6` = **5.25**
**Gate decision:** Park — runs straight into documented novelty fatigue and tightening anti-slop enforcement; it is a growth *tactic* for a stronger idea, not a standalone product.
**Biggest unknown:** Do clips convert viewers into *paying owners*, or just into transient views that fatigue and get throttled?
**De-risking step:** Fold clip-generation in as the growth loop for the IDEA-04/IDEA-01 experiment and measure clip→owner-signup conversion there, rather than building a standalone clip stream.

### IDEA-02 — FactFight (fact-check battles)  ·  Composite: 4.25  ·  Gate: Park

**Desirability — 4**
- Pain intensity: 4 — A niche builder itch; no acute customer pain evidenced.
- Demand evidence: 3 — Weakest in the set: no evidence of spectator appetite for watching fact-checks as entertainment; "no entertainment competitor" is a red flag, not whitespace (research Confidence: Medium-Low).
- Willingness to pay: 4 — No WTP signal.
- Founder–market resonance: 6 — Retrieval/tool engineering fits the founder, but the audience doesn't.

**Viability — 4**
- Market size & growth: 5 — Fact-check tooling is topical but accuracy-competitive, not entertainment.
- Monetization & unit economics: 4 — Thin; sponsored verification challenges are speculative.
- Defensibility / moat: 4 — Competes against accuracy-focused tools with no entertainment moat.
- Go-to-market realism: 5 — Unclear audience to grow into.
- Timing: 4 — "Why now" is challenged: hallucination rates run 22%–94% by task and ≥45% of AI news answers had a significant flaw (BBC/EBU) — models can't reliably adjudicate contested claims.

**Feasibility — 5**
- Technical complexity vs. capability: 4 — Correctness is contestable; automated scoring will misfire on spicy claims.
- Capital / resources vs. runway: 5 — Moderate cost.
- Time to testable MVP: 6 — Format is simple to prototype.
- External dependencies: 4 — Adjudicating real-world claims invites the moderation/liability mess the founder wants to avoid.

**Composite:** `0.40×4 + 0.35×4 + 0.25×5` = **4.25**
**Gate decision:** Park — weakest demand *and* the underlying tech is unreliable enough to make automated adjudication risky; lowest-conviction idea in the set.
**Biggest unknown:** Is there any spectator audience for watching fact-checks at all — and can models adjudicate contested claims reliably enough to score fairly?
**De-risking step:** Do not build. If revisited, first measure whether fact-check content clips/retains any audience, and whether an automated judge agrees with human verdicts above a usable threshold.

---

## Top 3 recommendation

No idea clears Advance, so the recommendation is to **pursue the top cluster as fast, cheap validation experiments**, not to greenlight a build.

1. **IDEA-04 — Coach Mode (6.90).** Highest-conviction because it sits on the single best-evidenced mechanic (pay-to-steer). **Highest-priority validation:** run a small always-on improv stage with 10–20 owner agents + paid audience steering and prove that status/payment *spreads across more than one owner* while steering revenue/hour beats inference cost/hour. This directly tests the run's untested leap.
2. **IDEA-09 — Discord-Native Guild Leagues (6.65).** The cheapest, fastest, most-reachable live signal and the best fit for a solo bootstrapper. **Highest-priority validation:** ship a league bot into 3–5 friendly Discords and measure daily-active-member lift *and* whether auto-clips escape the server — i.e. whether this path can ever feed the founder's virality goal.
3. **IDEA-01 — Agent Arena (6.25).** The safest, cheapest-to-moderate, most-buildable option (clean skill-contest legal footing). **Highest-priority validation:** stand up a minimal head-to-head ladder, auto-clip the dramatic finishes, and test whether a *non-builder* audience retains — probing the "legible but boring" ceiling before investing in seasons.

Run IDEA-04 and IDEA-09 in parallel (different surfaces, both within the founder's reach), use IDEA-08's clip loop as the shared growth instrument rather than a separate product, and treat IDEA-07's progression layer as the retention wrapper to add *after* a base format proves spectate-able.
