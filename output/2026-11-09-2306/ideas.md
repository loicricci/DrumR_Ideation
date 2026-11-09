# Ideas — run 2026-11-09-2306

> **Strategic logic of the set.** Focus is agent-creation tooling for freelancers
> and small businesses — self-serve, credit-card, no sales calls — leaning on the
> founder's deepest edge: cheap agent infra plus observability and cost control.
> I deliberately spread across the agent lifecycle (build/debug → cost → deploy →
> monetize → maintain → sell) so the ideas compete on angle, not flavor, and I
> anchored every idea on at least one strongly-evidenced signal (SIG-01–09),
> using the weaker search-surfaced signals only as corroboration. Three ideas
> (ProofKit, GroundWire, Checkpoint) touch the SIG-09/10 reliability pain but are
> framed strictly as **builder-side infra** — I never operate a customer-facing
> agent — so the K7 liability the scout flagged is structurally removed. Risk
> spans safe dev-tools (AgentProbe, BudgetWall), ambitious lifecycle plays
> (Aftercare, Hatch, ProofKit), and a contrarian anti-autonomy bet (Checkpoint).

---

## IDEA-01 — AgentProbe

- **One-liner:** Snapshot regression testing and step-level trace replay for solo builders so a prompt edit can't silently break a live agent.
- **Target customer:** Indie/solo developers and technical freelancers running LLM agents in production, nights-and-weekends to small-agency scale.
- **Problem / job to be done:** Once an agent is live, failures are silent and surface downstream days later; builders hand-roll eval scripts, keep a folder of "frozen" example inputs re-run on every change, and read raw logs — hours per change and still missing regressions.
- **Solution wedge:** A drop-in SDK wrapper that records real agent runs as reusable test cases, then on every prompt/model change replays them and flags per-step behavior diffs (not just final-output diffs) — the "frozen inputs" folder as a product, with a trace viewer of what the agent decided at each step.
- **Business model:** Self-serve SaaS, free tier by run volume, $19–49/mo paid; usage-metered trace retention. Credit-card, no sales call.
- **Founder edge:** Agent/LLM systems engineering and observability pipelines are the founder's core skill; cheap infra keeps trace storage margin-positive.
- **Why now:** Agent frameworks shipped fast in 2025; observability/evals lagged, so solo builders are hitting the "is it working?" wall right now.
- **Biggest risk:** "Good evals are just testing" — some builders believe CI + unit tests already cover it, so this could be a feature, not a company.
- **Signals:** SIG-01, SIG-04.
- **Thesis check:** passes K1–K7.
- **Parent:** none

---

## IDEA-02 — BudgetWall

- **One-liner:** A cost firewall that sits between an agent and the LLM APIs, enforcing per-task budgets and killing runaway loops before the bill, not after.
- **Target customer:** Solo builders and freelancers shipping agents that loop, retry and call tools.
- **Problem / job to be done:** An agent silently burns 5–10× expected API spend on one task ("$80 on a task I thought would cost $8"), discovered only at the bill; builders hand-build hard token caps, kill-switches and preflight checks after getting burned.
- **Solution wedge:** A proxy endpoint (swap the base URL) that enforces a per-task/per-agent budget, auto-kills loops over a call ceiling, does a cheap preflight cost estimate, and shows a live spend dashboard — the hard-won DIY guardrails as a one-line integration.
- **Business model:** Self-serve; free below a spend threshold, then a small % of routed spend or a flat $15–39/mo tier. Positions as net-savings so it pays for itself.
- **Founder edge:** Cost-efficient agent infra and multi-agent orchestration are explicit founder strengths — the one person most credible building a cost-control proxy cheaply.
- **Why now:** Multi-step tool-calling agentic workloads became common in 2025, multiplying token spend versus single-shot prompts.
- **Biggest risk:** Hard caps + preflight checks are easy to self-build and partly solve it already — the counter-signal says it's a feature; also proxying every call raises latency/trust objections.
- **Signals:** SIG-02, SIG-14.
- **Thesis check:** passes K1–K7.
- **Parent:** none

---

## IDEA-03 — Aftercare

- **One-liner:** A health monitor for deployed client agents that catches drift and breakage early and auto-generates the branded monthly report that justifies a maintenance retainer.
- **Target customer:** Freelancers and one-person AI-automation agencies maintaining agents for SMB clients.
- **Problem / job to be done:** Agents that work at launch degrade within weeks; by day 30 someone on the client side quietly reverts to manual work and the client churns by month four. Freelancers sustain it with manual check-ins and ad-hoc monitoring — labor that doesn't scale and is hard to bill for.
- **Solution wedge:** Point it at the deployed agent's logs/endpoints; it watches success/error rates, output drift and stale context, alerts the freelancer first, and on a schedule emits a white-labeled "your agent did X, caught Y" health report the freelancer forwards — turning silent rot into a visible, billable service.
- **Business model:** Self-serve per-agent/per-client pricing ($10–25/agent/mo), billed to the freelancer who marks it up into their retainer. Recurring.
- **Founder edge:** Observability + cheap infra; the monitoring and drift-detection pipeline is squarely the founder's systems-engineering wheelhouse.
- **Why now:** The 2025 wave of AI-automation agencies is hitting its first month-4 retention cliff as early builds age.
- **Biggest risk:** The practitioner's own fix is organizational ("require a named internal owner"), so part of the pain may be process, not a tool — adoption could stall if freelancers won't change how they sell.
- **Signals:** SIG-03, SIG-15, SIG-04.
- **Thesis check:** passes K1–K7 (monitors the freelancer's own deployment; no customer-facing operation → no K7 exposure).
- **Parent:** none

---

## IDEA-04 — Hatch

- **One-liner:** Turn a custom GPT or agent into a hosted, metered, Stripe-paywalled endpoint with a public page in minutes — the monetization layer OpenAI never shipped.
- **Target customer:** Independent creators who build useful custom GPTs/assistants and want recurring income without building a full app.
- **Problem / job to be done:** There's no built-in way to charge for an agent where it was built; "sharing a link is the only access control." Creators rebuild on the Assistants API, hack in affiliate links, or bolt on third-party paywalls — infra and coding they often lack.
- **Solution wedge:** Import an agent (prompt + tools + knowledge), get a hosted endpoint and a clean public page with Stripe subscriptions or pay-as-you-go credits, access control and usage metering baked in — creator keeps the majority of revenue. The public page is the growth loop (every shared agent markets the platform).
- **Business model:** Self-serve; free to publish, platform takes a small % of creator revenue plus a paid tier for custom domains/higher limits.
- **Founder edge:** Cheap per-agent infra (makes a low entry price viable) and the founder's stated pull toward building the missing monetization layer for agent makers.
- **Why now:** OpenAI's revenue-share stayed invite-only/US-only through 2026 and GPTs still can't be embedded elsewhere — a durable, dated monetization gap.
- **Biggest risk:** "Not much value to people outside your org" — supply of agents may exceed real paying demand, so creators publish but few buyers convert.
- **Signals:** SIG-05.
- **Thesis check:** passes K1–K7 (pure hosting/payments infra for the creator's own agent; no human-in-loop ops at scale).
- **Parent:** none

---

## IDEA-05 — KeyRoom

- **One-liner:** An embeddable OAuth-and-credentials onboarding flow so a builder's customer clicks "connect" instead of pasting a dozen API keys that silently expire.
- **Target customer:** Builders deploying multi-integration agents into a client's or customer's stack.
- **Problem / job to be done:** Going live means the customer collects and pastes ~8–12 API keys (half OAuth, half PATs, some rotating every 90 days) — "the silent killer" of adoption; builders run setup calls, write per-integration guides and redo auth on rotation.
- **Solution wedge:** A hosted, brandable "connect your tools" page the builder drops in; it handles the OAuth dance for common SaaS tools, stores and auto-rotates tokens, and exposes them to the agent via one secure call — replacing the paste-12-keys ritual with clickable buttons.
- **Business model:** Self-serve; free for a couple of connections, $29–79/mo by number of end-customers/connectors. Recurring.
- **Founder edge:** Secure infra and integration plumbing are core; a solo founder can ship a focused connector set cheaply.
- **Why now:** Agents now routinely touch 8–12 third-party tools; credential sprawl is a 2025–26 side-effect of multi-tool agents.
- **Biggest risk:** Overlaps established connector/auth infra (Nango and similar), and the person who raised the pain sells an auth product — differentiation and whether solo-builders will pay are open.
- **Signals:** SIG-07.
- **Thesis check:** passes K1–K7.
- **Parent:** none

---

## IDEA-06 — ShipAgent

- **One-liner:** One-click managed hosting that turns an agent repo or template into a running, shareable agent URL — no env vars, no terminal, no weekend lost to networking.
- **Target customer:** Small-agency owners and semi-/non-technical operators who want to run an agent but not learn infrastructure.
- **Problem / job to be done:** Self-hosted agents look appealing then collapse "the moment someone meets their first env var"; buyers either pay a managed-hosting premium or abandon. "Self-hosting kills adoption unless your ICP is literally a solo dev."
- **Solution wedge:** Deploy-from-template (or connect a repo) to a hosted runtime with secrets, scheduling and a public endpoint handled for you — the narrow wedge is a curated gallery of popular open-source agents that deploy in one click with guided config, not a general PaaS.
- **Business model:** Self-serve usage-based hosting with a flat floor ($9–29/mo); margin from the founder's cheap-infra edge.
- **Founder edge:** Cost-efficient, scalable agent infra is the single strongest founder advantage — this is the most direct expression of it.
- **Why now:** 2026 "self-hosting agents went mainstream" chatter collided with the reality that the buyers are non-technical.
- **Biggest risk:** Managed agent hosting is crowded (many "we built an agent hosting platform" posts); differentiation and margin at a low price point are the open questions.
- **Signals:** SIG-08.
- **Thesis check:** passes K1–K7 (K4 is the one to watch — cheap infra must keep per-user cost under the floor price).
- **Parent:** none

---

## IDEA-07 — ProofKit

- **One-liner:** A reliability-proof layer that pre-tests an agent against realistic scenarios and issues a shareable, continuously-updated trust score builders show buyers — "proof the agent works" without a sales call.
- **Target customer:** Indie builders with a working agent trying to sell it, who hit distribution-and-trust as the wall.
- **Problem / job to be done:** Building the agent was easy; the hard part is that buyers "want proof the agent works" and won't trust an unknown agent. Sellers rely on manual free trials and done-with-you setup calls that don't scale for a solo founder.
- **Solution wedge:** The builder runs their agent through a battery of domain scenarios; ProofKit produces a public "trust report" (pass rates, example transcripts, live accuracy over time) at a shareable link the builder puts on their landing page — standardized proof that replaces the trust-me pitch. Deliberately a proof/trust tool, **not** a marketplace (avoids the parked Agent Creators Marketplace failure mode).
- **Business model:** Self-serve; free basic badge, $39–99/mo for live monitoring, custom scenarios and verified reports.
- **Founder edge:** Eval/observability engineering and agent-design taste (knowing what a "convincing" proof looks like) are founder strengths.
- **Why now:** A 2025–26 surge of solo-built agents with no neutral way to demonstrate reliability to buyers.
- **Biggest risk:** A self-issued trust score may not actually move buyer trust; and the "distribution" framing in the source thread is partly self-serving from people selling marketplaces.
- **Signals:** SIG-06, SIG-09.
- **Thesis check:** passes K1–K7 (tests the builder's own agent in a sandbox; never operates a customer conversation → the SIG-09 K7 exposure is structurally removed).
- **Parent:** none

---

## IDEA-08 — MeterMark

- **One-liner:** Usage metering plus a white-label client billing portal so freelancers can price agent work in "runs/credits" the client understands and never eat a token overage again.
- **Target customer:** Freelance devs and small AI-automation shops who quote clients a flat price for an agent build + run.
- **Problem / job to be done:** They quote flat, then real usage (loops, retries, retrieval) runs 2–5× the estimate and eats margin; they hand-build retry ceilings, bill in opaque credits, and guess at markup.
- **Solution wedge:** Wrap the client's agent to meter real token/tool usage, convert it into marked-up "credits" or "runs," enforce the client's allowance, and show the client a branded usage portal with an auto-generated monthly invoice line — pricing and billing infra freelancers currently improvise in spreadsheets.
- **Business model:** Self-serve; flat $19–49/mo per freelancer plus small per-client fee. Recurring, aligned to the retainer norm the signals describe.
- **Founder edge:** Metering/cost-attribution is a direct offshoot of the founder's cost-control infra strength.
- **Why now:** Agentic multi-step workloads in 2025–26 made per-job cost far harder to predict than single-prompt calls, breaking flat quotes.
- **Biggest risk:** The pain may be solved by pricing discipline rather than a tool, and usage-metering/billing is a crowded infra space — SIG-14 itself is weak/search-surfaced.
- **Signals:** SIG-14, SIG-02, SIG-15.
- **Thesis check:** passes K1–K7.
- **Parent:** none

---

## IDEA-09 — GroundWire

- **One-liner:** A grounding guardrail API that forces an agent's answers to stay inside vetted sources, gates low-confidence replies, and auto-escalates to a human path — sold to the builder, so hallucinations stop embarrassing the business that deployed it.
- **Target customer:** Freelancers and small agencies building AI support/chat (and front-desk) agents for SMB clients.
- **Problem / job to be done:** Bots invent answers and "policies," frustrate customers, and get quietly switched off a few weeks after launch; builders DIY source-restriction, weekly chat reviews and human-handoff paths as ongoing manual QA.
- **Solution wedge:** A middleware call that constrains responses to the client's approved documents, returns a confidence/grounding score, blocks or rewrites ungrounded answers, and triggers a handoff when uncertain — the "only answer from vetted docs" discipline as a reusable guardrail, with an audit log of every answer.
- **Business model:** Self-serve; metered per-checked-message with a flat floor ($29–99/mo), billed to the builder.
- **Founder edge:** Retrieval/grounding and multimodal agent pipelines are core founder skills; cheap infra keeps per-message checks margin-positive.
- **Why now:** 2026 reporting on chatbots inventing policies and merchant-liability concern makes "accurate, safe answers" a live buying criterion.
- **Biggest risk:** Accuracy is table-stakes being chased by every incumbent (Intercom Fin, Shopify, Tidio); SIG-10 is weak/search-surfaced and a guardrail may not fully stop hallucination.
- **Signals:** SIG-10, SIG-09, SIG-04.
- **Thesis check:** passes K1–K7 — K7 is the one to watch: structurally removed because the product is a guardrail library the builder embeds (it *reduces* liability and keeps a human-escalation path); the founder never operates the customer conversation.
- **Parent:** none

---

## IDEA-10 — Checkpoint

- **One-liner:** An approval inbox for risky agent actions — the agent pauses, pings the owner's phone for a one-tap yes/no, then resumes — turning "never let AI run loose" from an objection into a feature.
- **Target customer:** Freelancers/solo agencies who sold "autonomous" agents and non-technical owners nervous about unattended AI.
- **Problem / job to be done:** Full autonomy creates silent failures and an unpaid-support trap: a bad value "sat there for 2 days because the agent kept running," and the lesson practitioners draw is to keep agents narrow and never let them run loose. Today they hand-build kill-switches and bespoke alerting.
- **Solution wedge:** A one-line SDK that marks sensitive steps (send email, charge card, post publicly, write to CRM) as gated; the agent suspends, sends a mobile/Slack approval card with context, and only proceeds on approval — plus a timeout-to-safe-default. A human-in-the-loop checkpoint without the freelancer babysitting logs.
- **Business model:** Self-serve; free below an approvals/month cap, then $15–39/mo by volume. Recurring.
- **Founder edge:** Orchestration/state-management of multi-step agents (pause/resume, durable steps) is core founder engineering; contrarian bet that leans into the autonomy backlash rather than against it.
- **Why now:** The first cohort of 2025 autonomous client builds is hitting months-later breakage and silent failures, and builders are actively concluding autonomy needs guardrails.
- **Biggest risk:** Adding human approval re-introduces latency and defeats the "autonomous" selling point — buyers may want fewer interruptions, not more, so the sweet spot of which steps to gate is narrow.
- **Signals:** SIG-04, SIG-15, SIG-09.
- **Thesis check:** passes K1–K7 (approvals routed to the builder/owner, automated — no founder-run moderation queue; customer-facing operation stays with the builder → no K7 exposure).
- **Parent:** none

---

## Round 2

> **Refill logic.** Governance returned 0 Advance / 8 Iterate / 2 Park and flagged
> two things: the whole set is dev-tooling with almost no consumer/viral growth
> loop (the founder's headline goal), and the two top Iterate ideas each hinge on
> one unproven assumption. This round removes those assumptions and deliberately
> pulls toward the founder's preferences — a built-in growth loop and the cheap
> agent-infra edge. **IDEA-11** reframes Aftercare so its value no longer depends
> on the freelancer *selling* a report (it recovers billable revenue the
> freelancer is already losing). **IDEA-12** reframes AgentProbe off the crowded
> free-OSS tracing/eval floor into a CI-native PR review bot with a public-repo
> growth loop. **IDEA-13/14/15** open three previously-unused signals (SIG-11
> no-code lock-in, SIG-12 non-dev automation complexity, SIG-13 the dated June-15
> Zapier AI-step repricing), each built around a sharing/SEO loop and, for
> IDEA-15, squarely on the cheap-infra edge.

---

## IDEA-11 — Billback

- **One-liner:** A monitor for deployed client agents that turns every silent breakage into a scoped, client-approvable fix ticket — converting the freelancer's unpaid firefighting into billable maintenance revenue.
- **Target customer:** Freelancers and one-person AI-automation agencies who sold agents to SMB clients and are now on the hook for them.
- **Problem / job to be done:** Agents break months later (API change, auth expiry, drift) and the freelancer becomes the "on-call dev, integration janitor" doing unpaid fixes, or the client silently reverts and churns. Today the freelancer eats the support time or chases a retainer conversation they keep losing. The value here does **not** depend on them selling a new "health report" line item (the thing Round 1 couldn't de-risk) — it attaches to work they are already forced to do, and makes it billable.
- **Solution wedge:** Point it at the client's deployed agent; when it detects a failure or drift it auto-drafts a plain-English incident + a scoped fix estimate and pushes a **branded client-approval page** ("your Invoicing Agent stopped reading POs on Nov 3 — approve a 2-hour fix?"). The client taps approve; the freelancer bills the fix. The product monetizes recovered revenue, not a report the freelancer must upsell.
- **Business model:** Self-serve, billed to the freelancer: flat $19–39/mo + a small per-agent monitoring fee; optionally a tiny % of fixes approved through the page. Recurring, and pays for itself on the first recovered fix.
- **Founder edge:** Drift/breakage detection and monitoring pipelines are the founder's observability wheelhouse; cheap infra keeps per-agent monitoring margin-positive. The branded approval page is a growth loop — every client who approves a fix sees the platform, and clients with multiple freelancers surface the tool to them.
- **Why now:** The 2025 cohort of "autonomous agent" client builds is hitting its first wave of months-later breakage (SIG-15) exactly as agencies feel the month-4 churn cliff (SIG-03).
- **Biggest risk:** Clients may balk at per-incident "approve a fix" charges (feeling nickel-and-dimed), or breakage frequency is too low to generate meaningful recovered revenue — making the monitoring fee hard to justify.
- **Signals:** SIG-15, SIG-03, SIG-04.
- **Thesis check:** passes K1–K7 (monitors the freelancer's own deployment, approvals routed to the client automatically; no founder-run ops queue, no customer-facing conversation → no K7 exposure).
- **Parent:** IDEA-03

---

## IDEA-12 — Rehearse

- **One-liner:** A CI-native review bot that replays recorded scenarios on every pull request that touches an agent and posts a plain-English "here's what changed in your agent's behavior" diff as a check — like a preview deploy, but for agent behavior.
- **Target customer:** Indie/solo developers and small teams shipping LLM agents from a Git repo, who already run CI and review PRs.
- **Problem / job to be done:** A prompt or model change silently alters behavior and nobody notices until downstream breakage; builders either read raw traces by hand or wire up free OSS eval libraries (Langfuse/Phoenix) into their own CI — setup nobody maintains. The Round 1 version competed head-on with that free tracing/eval floor. This reframes onto a surface the OSS libraries *don't* own: the PR review itself.
- **Solution wedge:** Install a GitHub/GitLab app; on each PR that changes prompts/agent code it replays a recorded scenario set and posts a required check + a human-readable behavioral diff comment ("3 of 20 scenarios now escalate to human where they used to auto-resolve"). Zero CI wiring. Free for public repos — the branded check and comment appear in public OSS agent repos, which is the SEO/word-of-mouth growth loop (the Codecov/Vercel-bot playbook); paid for private repos and larger scenario sets.
- **Business model:** Self-serve; free for public repos (growth), $15–49/mo per private repo or small team. Recurring.
- **Founder edge:** Record/replay + behavioral-diff engineering is the founder's eval/observability core; cheap infra makes free public-repo runs sustainable. The public-PR footprint is the built-in growth loop governance said Round 1 lacked.
- **Why now:** Agent code moved into normal Git/CI workflows in 2025–26, but the review surface still treats a prompt change like any text diff — the behavioral-diff gap is open and OSS evals live offline, not in the PR.
- **Biggest risk:** "CI + unit tests already cover it" — teams may fold scenario replay into their existing test step for free, and the public-repo loop only pays off if enough agent code is actually open-source.
- **Signals:** SIG-01, SIG-04.
- **Thesis check:** passes K1–K7.
- **Parent:** IDEA-01

---

## IDEA-13 — Eject

- **One-liner:** A plain-English agent builder whose whole promise is that you own the result — build an agent by describing it, then export clean, runnable source to your own repo anytime, no lock-in.
- **Target customer:** Indie hackers and semi-technical makers who want to ship an agent without hand-coding, but refuse to be trapped in a platform they can't leave.
- **Problem / job to be done:** Tools marketed as "no-code" still demand webhooks/JSON to get working, and once it works you don't own it — "you're renting a prettier box." Makers abandon platform after platform and say they'd pay only for a tool that lets them export and own the code.
- **Solution wedge:** Describe the agent in plain English → get a working, hosted agent **and** a one-click "eject" that hands you the full source (prompts, tools, orchestration) as a standard repo you can run anywhere. The anti-lock-in export is the wedge and the headline, not a buried feature. Shared/published agents carry a lightweight "built with Eject" public page — the growth loop.
- **Business model:** Self-serve; $19/mo starter (matching the stated WTP anchor) with hosted runs, higher tiers for more agents/usage; export included on paid plans. Recurring, with the founder's cheap infra giving margin on hosted runs.
- **Founder edge:** Agent-design taste (what makes an agent good) plus cheap orchestration infra directly serve "generate a genuinely good agent AND run it cheaply"; the "built with" share page fits the founder's community-led, build-in-public growth comfort.
- **Why now:** The 2025–26 flood of "build an agent in plain English" tools has produced an open backlash about hidden complexity and lock-in — a switching moment the incumbents created.
- **Biggest risk:** "No-code agent builder" is a crowded, well-funded category; ownership/export may be a nice-to-have that doesn't overcome incumbents' distribution, and codegen quality good enough to actually own is hard to nail in a 4-week MVP.
- **Signals:** SIG-11, SIG-08, SIG-12.
- **Thesis check:** passes K1–K7 (MVP scoped to a narrow template/export set to stay inside the 4-week window; self-serve, automatable, cheap-infra margin).
- **Parent:** none

---

## IDEA-14 — PlainFlow

- **One-liner:** A plain-English automation builder for non-technical business owners where you never see JSON, expressions, or a webhook node — describe what you want, answer a couple of questions, and it runs.
- **Target customer:** Non-technical small-business owners (salon, clinic, trades, small agency) who want to build their own automations/agents but bounce off n8n/Make.
- **Problem / job to be done:** The leading automation tools assume comfort with JSON, expressions and self-hosting, so non-developers hit a syntax or webhook step they can't configure and give up — falling back to Zapier's guardrailed templates, hiring a freelancer, or abandoning. They already pay for Zapier/Make, so WTP and switching intent exist.
- **Solution wedge:** A chat-first builder that turns a plain-English request into a working, guardrailed automation, asks clarifying questions in business terms (never JSON), and self-explains/self-heals when something changes — plus a **vertical template gallery** (e.g. "missed-call text-back for salons") that is the SEO/growth loop and community-seeded content. The wedge is one or two high-demand verticals, not a universal builder.
- **Business model:** Self-serve subscription ($15–39/mo) undercutting a freelancer and competing on simplicity, not feature count. Recurring.
- **Founder edge:** Agent orchestration + cheap infra make a "just works, we run it" experience viable at a low price; the shareable vertical template gallery is a built-in SEO/growth loop and fits the founder's community-led GTM.
- **Why now:** Agent features bolted onto automation tools in 2025–26 raised the skill floor further for non-devs, widening the gap between "powerful" and "usable by an owner."
- **Biggest risk:** The safe-template incumbents (Zapier) may already serve this persona "well enough," and SIG-12 is a weak/search-surfaced signal — the non-dev owner's pain may not be acute enough to switch for.
- **Signals:** SIG-12, SIG-11, SIG-13.
- **Thesis check:** passes K1–K7 (narrow-vertical MVP keeps build ≤4 weeks; K2 watch — automation must self-heal, not become a founder support queue).
- **Parent:** none

---

## IDEA-15 — SwapStep

- **One-liner:** A free "audit your Zapier AI bill" tool plus a drop-in cheaper AI action that replaces expensive AI-by-Zapier steps by routing to low-cost models at a flat price.
- **Target customer:** Prosumer and small-business no-code automators who added AI steps to their Zaps and just got repriced.
- **Problem / job to be done:** On June 15 2026 AI by Zapier moved to model-tier pricing with AI steps defaulting to the most expensive tier (confirmed on Zapier's official help page), so task-based AI bills are climbing faster than expected and teams "haven't adjusted." Today they manually audit Zaps to strip AI steps, route to cheaper models by hand, or shop for Make/Pabbly/n8n alternatives.
- **Solution wedge:** A free, shareable web tool that scans a connected Zapier account, flags the expensive AI steps and estimates the monthly overspend (the migration-intent SEO/growth loop) — then a one-click swap to **SwapStep's own AI action** (a Zapier app) that runs the same prompt on a cheap-routed model at a flat, predictable price. Stay inside Zapier; just make the AI step cheap.
- **Business model:** Self-serve; the audit is free (lead/growth loop), then a flat $9–29/mo subscription (or tiny markup on routed calls) for the cheaper AI action. Recurring; the founder's cheap-infra edge is the margin.
- **Founder edge:** Cheap, cost-efficient multi-model routing is the founder's single strongest advantage — this idea *is* that edge pointed at a dated pricing event. The free audit tool is an SEO/shareable growth loop aimed at active "Zapier AI pricing" search intent.
- **Why now:** The June-15-2026 AI-step repricing is a concrete, dated "losers" event creating live migration intent in exactly this buyer base — a time-boxed switching window.
- **Biggest risk:** Dependence on Zapier's platform (they could cut app-store AI actions out or re-price again), and migration volume is unverified — the switching intent may be loud in competitor blogs but thin in practice.
- **Signals:** SIG-13, SIG-02, SIG-14.
- **Thesis check:** passes K1–K7 (Zapier app + routing endpoint is a ≤4-week MVP; self-serve, cheap-infra margin, reachable via r/Zapier and no-code newsletters).
- **Parent:** none

---

## Round 3

> **Refill logic.** Round 2 landed 1 new Iterate / 3 Park, with Billback (IDEA-11)
> tying Aftercare for the lead but swapping in a new unproven conversion, and
> ProofKit (IDEA-07) still resting on the single unproven claim that a self-issued
> trust score moves buyers. This round does two things. **Reframes** remove the
> exact assumption the scorecard named: **IDEA-16** rebuilds Billback so the
> founder's revenue is a flat subscription riding the existing maintenance-retainer
> norm (SIG-15) — it no longer depends on per-incident client approvals or on how
> often agents break; **IDEA-17** rebuilds ProofKit so trust comes from the
> buyer's *own* data plus a real, enforced money-back guarantee, not a vendor
> badge. **New ideas** open the strongest unused Round-3 signals: **IDEA-18** on
> SIG-16 (the strongest, directly-fetched MCP-server pain) as hosted
> protocol-specialised infra, not a library; **IDEA-19** on SIG-19 (buyers already
> paying for templates) as a one-sided, creator-seeded storefront with automated
> verification — deliberately *not* the parked two-sided Agent Creators
> Marketplace; and **IDEA-20** on SIG-17 (solo-operator agent memory) as a
> portable, cross-tool memory layer that native per-platform memory structurally
> can't be. Every new idea leans on the cheap agent-infra edge and carries a
> built-in distribution surface.

---

## IDEA-16 — Keepwell

- **One-liner:** A flat-rate "agent care plan" toolkit that auto-detects and auto-fixes the routine breakages in a freelancer's whole client-agent portfolio and gives every client a branded uptime status page — so maintenance is sold as a predictable retainer, never a per-incident charge.
- **Target customer:** Freelancers and one-person AI-automation agencies maintaining a portfolio of agents for SMB clients.
- **Problem / job to be done:** Agents break months later (auth/token expiry, API/schema changes, drift) and the freelancer becomes the unpaid "on-call dev, integration janitor," or the client silently reverts and churns by month four. The Round-2 Billback framing tried to recover revenue *per incident*, which only pays off if breakage is frequent and clients approve each "approve-a-fix" charge — neither is evidenced. Freelancers already charge a "fixed build fee + monthly maintenance retainer" (SIG-15), so the real job is to make that flat retainer cheap to deliver and easy to justify, not to invent new per-incident billing.
- **Solution wedge:** Point it at the freelancer's whole portfolio; it watches each agent, **auto-remediates the routine failure classes** (re-runs OAuth re-auth, patches known schema shifts, restarts on timeout), escalates only the rest to the freelancer with a one-click scoped fix, and publishes a **branded per-client uptime status page** ("your agents: 99.4% this month, 3 issues auto-resolved"). The status page is what the client sees — reassurance that kills silent churn — not a nickel-and-dime invoice. Value to the founder is a flat per-agent subscription; value to the freelancer is less unpaid firefighting plus a retainer they can defend. Revenue depends on portfolio size, not breakage count or client sign-off.
- **Business model:** Self-serve, billed to the freelancer: flat $12–29/agent/mo (or a portfolio tier). Recurring and breakage-independent — one prevented churn or a few hours of saved firefighting per month pays for it.
- **Founder edge:** Drift/breakage detection, auto-remediation and monitoring pipelines are the founder's observability wheelhouse; cheap infra keeps per-agent monitoring margin-positive. The branded status page is the growth loop — every client (and any other freelancer they work with) sees the platform on a page that carries its mark.
- **Why now:** The 2025 cohort of autonomous client builds is hitting its first wave of months-later breakage (SIG-15) exactly as agencies feel the month-4 churn cliff (SIG-03), and 2026 agency incident-playbook content is framing "turn silent failures into loud ones" as the fix.
- **Biggest risk:** Auto-remediation that is too shallow leaves the freelancer still firefighting (so the flat fee feels unearned); and if freelancers don't already run a maintenance retainer, Keepwell has to create that habit rather than ride it.
- **Signals:** SIG-15, SIG-03, SIG-04.
- **Thesis check:** passes K1–K7 (monitors/remediates the freelancer's own deployments, status pages auto-generated; no founder-run ops queue, no customer-facing conversation → no K7 exposure; K2 watch — remediation must be automated, not a founder support channel).
- **Parent:** IDEA-11

---

## IDEA-17 — Backstop

- **One-liner:** A drop-in "try it on your own data, money-back if it fails" layer a builder puts on their agent's landing page — so buyers trust results they watched run on their *own* inputs and a refund they'll actually get, not a self-issued score.
- **Target customer:** Indie builders with a working agent (lead-qualifier, support bot, back-office automation) trying to sell it self-serve, who hit the distribution-and-trust wall.
- **Problem / job to be done:** Buyers "want proof the agent works" and won't trust an unknown agent; SMBs have been burned paying real money ($299, $1,428) for voice/support agents that turned out "inconsistent, unreliable… unusable," then fought strict refund policies. The Round-2 ProofKit answered this with a builder-supplied trust score — but "today the badge is just a badge" and benchmark scores "overstated reliability," so the value hinged on buyers trusting a self-issued number. This reframes trust onto two things buyers *do* believe: their own eyes and an enforced refund.
- **Solution wedge:** The builder embeds a Backstop flow on their page. The buyer uploads a handful of their **own** real examples (their emails, their tickets, their records); the agent runs them transparently in a sandbox and the buyer sees the actual outputs on their actual data — proof the buyer inherently trusts because it isn't a vendor benchmark. The builder optionally attaches a **money-back guarantee tied to an agreed pass bar on those inputs**, which Backstop tracks and auto-triggers as a refund through the builder's own Stripe if the bar isn't met. Trust is backed by something real (the buyer's data + a refund they'll actually receive), not a score.
- **Business model:** Self-serve, billed to the builder: flat $39–99/mo for the trial-on-your-data flow and guarantee automation, higher tier for volume/custom scenarios. Recurring.
- **Founder edge:** Sandbox-run-on-arbitrary-inputs plus eval/transcript tooling is the founder's observability + agent-design core; cheap infra keeps per-trial sandbox runs margin-positive. The "powered by Backstop · money-back if it fails your test" badge on every seller's page is the distribution surface.
- **Why now:** A 2025–26 surge of solo-built agents hit a buyer base (SIG-09) now actively burned by unreliable agents and aggressive billing — a money-back-on-your-own-data guarantee is the precise antidote to that complaint, and self-issued trust scores are visibly failing to move buyers.
- **Biggest risk:** Builders may refuse to stake a real refund (fear of abuse or of their agent genuinely failing on messy real data), so adoption could stall at the guarantee step even though the "run on your own data" proof still has standalone value.
- **Signals:** SIG-06, SIG-09.
- **Thesis check:** passes K1–K7 (tests the builder's own agent on buyer-supplied inputs in a sandbox; the founder never operates a customer conversation → SIG-09 K7 exposure stays removed). K7 finance watch: Backstop never custodies funds — refunds run on the *builder's own* Stripe via delayed capture / refund API, so there is no money-transmission exposure.
- **Parent:** IDEA-07

---

## IDEA-18 — Pier

- **One-liner:** A hosted home for MCP servers that catches the silent protocol failures before production — deploy once, and Pier runs cross-client conformance tests and keeps it up, so "15 minutes to deploy, 15 hours a week to keep running" becomes a subscription.
- **Target customer:** Solo/indie developers and technical freelancers building and maintaining MCP servers that connect agents (their own or clients') to tools and APIs.
- **Problem / job to be done:** The MCP protocol fails silently — a `console.log` to stdout corrupts the JSON-RPC stream with no error, a wrong error-shape gets swallowed, and clients parse schema fields with different strictness — so "errors are silent, the protocol is unforgiving, and most issues only show up after you've connected everything… invisible until production." Cross-client testing "is killing me," and keeping a handful of servers running reportedly eats ~15 hours/week. Today builders log-to-file by hand, add SIGTERM handlers, and print-spelunk per client.
- **Solution wedge:** Push an MCP server to Pier and it (1) runs a **cross-client conformance suite** that replays the server against the real client parsers and flags exactly the silent killers — stdout framing corruption, malformed error responses, schema fields a stricter client will reject — *before* deploy; (2) hosts it on cheap infra with the stdio/transport plumbing and SIGTERM/restart handling done for you; (3) monitors it in production and surfaces protocol-level failures as loud, readable alerts. Every hosted server gets a public "conformance-verified" install page. Narrow and protocol-specialised — not a general agent PaaS (that's the parked ShipAgent/Agntable space).
- **Business model:** Self-serve; free for one server/dev, $19–49/mo by server count or traffic. Recurring; the cheap-infra edge is the margin on hosted servers.
- **Founder edge:** Hosting multi-process agent/tool infra cheaply and reliably is the founder's single strongest advantage; the protocol-conformance harness is exactly the kind of systems problem that energises him. The public verified-install pages (and a directory of conformance-verified servers) are the distribution loop — each shared server markets Pier, and corroborates the "would people pay for vetted MCP servers vs free GitHub repos?" demand (SIG-19).
- **Why now:** MCP adoption exploded in 2025–26 and the reference servers ship breaking changes often, so building and *keeping* servers running is a fresh, recurring chore with no specialised home yet.
- **Biggest risk:** Much of the pain is "learn the protocol's gotchas once," so the fix could be an open-source linter/library + docs rather than a paid host — Pier must prove the *keeping-it-running* (conformance + uptime + monitoring) recurring value is worth paying for, not just the one-time lint.
- **Signals:** SIG-16, SIG-19.
- **Thesis check:** passes K1–K7 (self-serve, automatable hosting; K3 watch — MVP scoped to host + one cross-client conformance check + uptime alert to stay in the 4-week window; K4 rides the cheap-infra edge; reachable in r/mcp, r/ClaudeAI, MCP Discords).
- **Parent:** none

---

## IDEA-19 — Runnable

- **One-liner:** A "Gumroad for working automations" where creators sell n8n/agent templates that Runnable auto-verifies actually run before listing, delivers instantly, and backs with a money-back guarantee — fixing the non-delivery and "doesn't work as stated" trap buyers keep hitting.
- **Target customer:** Primary (the seeded side): community creators who build and sell agent/automation templates and "build-and-sell AI automations" packs. Their buyers — semi-/non-technical makers already paying for these templates — come from each creator's own audience, not from the founder.
- **Problem / job to be done:** Buyers already pay for templates (e.g. a "$29 Build and Sell AI Automations" pack) but "paid for a template and got nothing after payment, no email, no instructions," or the template "doesnt work as stated by it's creator" — with no buyer protection because the sale is creator-to-buyer, not platform-backed. Sellers, meanwhile, note a bare template "rarely carries much price on its own because buyers can't easily judge quality before purchase." Both sides are bleeding trust the current Gumroad/forum path can't provide.
- **Solution wedge:** A storefront infra tool sold to creators. On upload, Runnable **test-imports and runs the template in a sandbox** to verify it works and captures a "verified working" proof (a dry-run transcript/screens) buyers see before paying — automated, so no human review queue. Checkout + **instant, guaranteed delivery** fixes the non-delivery payments bug, and purchases carry an auto-enforced money-back guarantee if the verified template fails on import. Optional one-click deploy (spin up a running copy on the founder's cheap infra) turns the "template-plus-setup sells better" counter-signal into an upsell. One-sided by design: the founder recruits *creators only* from the no-code/agent communities he can reach; buyers arrive through each creator's own following — so it is **not** the parked two-sided Agent Creators Marketplace and satisfies the thesis "one side seeded by the founder alone."
- **Business model:** Self-serve; small transaction fee per sale (+ optional creator subscription for a custom storefront/higher verification volume, and a margin on one-click-deploy hosting). Recurring-leaning via repeat creator sales and hosted deploys.
- **Founder edge:** The sandbox that safely imports and runs an arbitrary n8n workflow / agent template to verify it is an agent-infra problem the founder solves cheaply; one-click deploy rides the same cheap-hosting edge. Each creator's branded storefront + "verified on Runnable" badge is the distribution loop — buyers discover Runnable through sellers they already follow, and some convert to sellers.
- **Why now:** A 2025–26 cottage industry of selling n8n/agent templates and skill packs sprang up faster than any trust, delivery or verification layer — buyer complaints are clustering on the n8n forum and Gumroad right now.
- **Biggest risk:** Automated verification can confirm a template *imports and runs* but not that it does what the creator *claims* on the buyer's real stack, so "doesn't work as stated" disputes may persist; and the market may resolve toward done-for-you setup, making the pure storefront a thin wedge.
- **Signals:** SIG-19, SIG-11.
- **Thesis check:** passes K1–K7 (marketplace one-sided → creators seeded by founder alone; verification automated so no manual moderation queue → K2 holds; self-serve, credit-card; K7 fine — no regulated content, and the money-back is tracked on the creator's/platform's standard payments rail, not fund custody).
- **Parent:** none

---

## IDEA-20 — Throughline

- **One-liner:** A portable, cross-tool memory layer for solo operators — one place your context lives that every agent and assistant reads and writes via MCP, so you stop re-briefing a fresh agent every morning and your memory isn't locked to one vendor.
- **Target customer:** Solo operators and indie builders running AI agents / coding assistants day-to-day on their own project or business (often non-team, across more than one tool).
- **Problem / job to be done:** Agents have no persistent memory across sessions, so the operator "re-explains everything" every morning — "that's not automation, that's babysitting" — burning ~10 minutes per session plus weekly upkeep of hand-maintained CONTEXT.md / CLAUDE.md files; vector DBs are rejected as "too much setup for a solo operator." Native platform memory is appearing, but it is siloed per vendor — it doesn't follow you from Claude to Cursor to a custom agent, and it doesn't let you own or export what it knows.
- **Solution wedge:** A zero-setup hosted memory the operator fills once (or that auto-captures from sessions), exposed as an **MCP server any client can connect** — so the same memory is read/written by every agent and assistant the operator uses, no vector-DB plumbing. The defensible position against "native memory will close this" is exactly what native memory can't be: **cross-tool, portable, and exportable** — your context is Switzerland, it follows you between vendors and you own it. Ends the daily re-brief without the operator maintaining a context file by hand.
- **Business model:** Self-serve; free below a memory-size/connected-client cap, $9–19/mo for more. Recurring; the founder's cheap memory/retrieval-infra edge is the margin.
- **Founder edge:** Agent memory, retrieval and orchestration pipelines are named founder strengths ("orchestration, tools, memory, multimodal pipelines"), and serving a fast, cheap memory store is squarely the cheap-infra edge. Shipping as an MCP server rides the exploding MCP ecosystem (SIG-16) as a distribution surface — every client it plugs into is a place it is discovered.
- **Why now:** Agents moved from single-shot prompts to multi-session, days-long work in 2025–26, so the lack of cross-session memory became a daily productivity tax — and MCP arrived as the standard way to plug one memory into every client at once.
- **Biggest risk:** Native per-platform memory keeps improving and may be "good enough" for operators who live in one tool, and the cheap workaround (a single CONTEXT.md file) is good enough for many — so the cross-tool/portability wedge has to be felt as a real, not theoretical, benefit; the built-in growth loop here is also thinner than the other Round-3 ideas.
- **Signals:** SIG-17, SIG-16.
- **Thesis check:** passes K1–K7 (self-serve, automatable; memory store + MCP server is a ≤4-week MVP; cheap per-user infra keeps margin positive under a low price; reachable in Indie Hackers, r/AI_Agents, AI-coding Discords).
- **Parent:** none
