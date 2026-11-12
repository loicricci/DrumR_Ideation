# Revenue model stress test: usage-based expert payouts

> Run `2026-11-12-1205-fast`. Written by the orchestrator to stress-test the
> founder's model before scoring. Every number here is an **estimate**: card
> fees are Stripe's published standard rate (2.9% + $0.30), and inference
> costs are illustrative per-message blends for a RAG chat turn (~3k tokens
> in, ~500 out). Replace them with Avee's real metered costs.

## 1. The model as stated

User B pays **$20/month**. 50% of B's usage goes to agent K (owned by A). The
platform "always makes at least 50% net margin on usage", and A earns **at least
$5** from B's use of K.

## 2. The contradiction

The example makes two promises:

1. **Creator gets 50% of the gross** attributed to their agent: $10 × 50% = $5.
2. **Platform keeps ≥ 50% net margin.**

Promise 1 gives away half the gross before any cost is paid. The platform's
half then has to cover card fees, refunds, payout fees and **all inference**,
so its net margin is always below 50%. At high usage it goes negative:

| B's usage (msgs/mo) | Model tier | Inference C | A's payout from K | Platform net | Platform margin on gross |
|---|---|---|---|---|---|
| 400 (typical) | mid ($0.006/msg) | $2.40 | $5.00 | $6.52 | 33% |
| 400 (typical) | frontier ($0.02/msg) | $8.00 | $5.00 | $0.92 | 5% |
| 1,500 (heavy) | mid | $9.00 | $5.00 | −$0.08 | 0% |
| 5,000 (power) | cheap ($0.002/msg) | $10.00 | $5.00 | −$1.08 | −5% |

Under the literal model, the platform's profit depends on the subscriber's
behaviour, and a single power user on a frontier-model agent loses $20–90/month.

**Verdict on the model as stated: not bulletproof.** Usage-based payouts work;
paying them out of gross revenue doesn't.

## 3. Bulletproof version: user-centric net contribution share

Compute this per subscriber, per month, after the billing period closes:

```
N  = price − sales tax − payment fees − refund/chargeback reserve   (net revenue)
C  = metered inference + media cost of THIS subscriber's usage      (direct cost)
P  = max(N − C, 0)                                                  (contribution)

Creator pool  = 50% × P
Platform keep = 50% × P   (+ absorbs any N − C < 0, which the cost cap prevents)

Agent payout  = Creator pool × (agent's share of this subscriber's billable units)
```

What each rule does:

- **"50% margin" becomes structural.** The platform keeps half of the
  contribution on every subscriber, every month. That's a hard rule, not a hope.
- **User-centric, not pro-rata pool.** Each subscriber's money goes only to the
  agents *that subscriber* used. That's the opposite of Spotify's pooled
  pro-rata model, and it matters for fraud (section 5).
- **Creators share cost.** An agent that burns frontier tokens shrinks its own
  pool, so experts are pushed to pick cost-efficient models. That plays to
  Avee's routing edge.
- **Billable units, not "time".** Attribute by messages weighted by model tier
  (or by tokens). Time-on-agent is gameable (idle tabs) and unrelated to cost.

### The cost cap (required)

The formula only holds if C stays below N. Add a **fair-use cost cap** per
subscriber (e.g. $3–6 of inference per month at cost). Above the cap:

1. Route to a cheaper model.
2. Image, video (SORA 2, FLUX) and voice are **never** included in the flat
   subscription. They run on **credits** priced at cost × 2 or more.
3. Hard stop at a monthly ceiling, with an upgrade prompt.

### What A actually earns (50% usage on K, 50/50 contribution split)

| Price | Inference C (capped) | Contribution P | **A's payout from K** | Platform keep | Platform margin on gross |
|---|---|---|---|---|---|
| $20.00 | $1 | $17.92 | **$4.48** | $8.96 | 45% |
| $20.00 | $3 | $15.92 | **$3.98** | $7.96 | 40% |
| $20.00 | $6 | $12.92 | **$3.23** | $6.46 | 32% |
| $24.99 | $3 | $20.72 | **$5.18** | $10.36 | 41% |

**The honest trade-off:** at $20 and a 50/50 split of contribution, A earns
**about $3.20–4.50**, not $5. To guarantee "≥ $5 at 50% usage", either price at
**$24.99** with a cost cap of about $3, or give creators 60% of contribution and
accept a platform keep of about 26–38% of gross. You can lock price, creator
payout or platform margin, but only two of the three.

## 4. Edge cases the model has to answer

| Case | Rule |
|---|---|
| Subscriber uses nothing this month | Contribution goes to the agents they **follow** (pro rata), or the platform keeps it. Pick one and publish it. Recommended: followed agents, which rewards experts who brought the user. |
| Usage on Avee's 50+ prebuilt demo agents | Platform is the owner, so the creator share goes to the platform. |
| Expert's own audience (brought by their link) | Pay a **referral bonus** (e.g. +10% of that subscriber's contribution for 12 months). This is the growth loop, so experts market Avee for you. |
| Free users | Earn nothing for creators. Only paid subscriptions fund payouts, which keeps bot traffic worthless. |
| Human escalation (expert answers personally) | Not in the $20 pool. Make it a **paid escalation** set by the expert (e.g. $X per answer, 80/20). Otherwise experts do unpaid work. |
| Private agents (roadmap) | A second layer: expert-priced add-on subscription, with the expert keeping ~80% of net and inference passed through. The all-access pool alone won't satisfy experts who already have a paying audience (Patreon/Substack take 8–12%). |
| Refunds and chargebacks | Hold payouts 30–60 days (the card chargeback window). Claw back from the next payout. |
| Tiny payouts | Minimum payout threshold of $25–50, paid monthly. Stripe Connect charges about $2 per active account per month plus per-payout fees, which would eat $5 payouts. |
| Taxes | Tax-exclusive pricing, or a merchant of record (Paddle / Lemon Squeezy, ~5% + $0.50) to handle global VAT. Stripe Connect Express handles creator KYC and 1099/DAC7 reporting. Mobile in-app purchase would take 15–30% more, so sell on the web. |

## 5. Fraud resistance: the model's best property

With user-centric attribution, **self-dealing always loses money**. An expert
who buys a $20 subscription and spams their own agent gets back at most
50% × P ≈ $8–9. Collusion rings (A uses B's agent, B uses A's) lose the same way.
Bot farms on free accounts generate $0. The remaining attack is stolen-card
subscriptions, which the 30–60 day payout hold and Stripe Radar cover.

The pro-rata pool model Spotify uses is vulnerable to streaming farms precisely
because a fake account's money is spread across everyone. **Don't switch to a
pooled model.**

## 6. What the model doesn't solve (business risk, not math)

- **Why does B pay $20?** That's the price of ChatGPT Plus / Claude Pro. A
  subscriber buys access to *specific experts* they already trust, not "50 AI
  agents". With under 50 users and no named expert segment, demand is unproven.
- **Is $3–5 per subscriber-equivalent worth an expert's effort?** An expert needs
  about 250 fully engaged subscriber-equivalents to earn ~$1,000/month from the
  pool. Early on, payouts will be cents. Pitch it as passive upside, not income.
- **Expert-advice liability (K7).** Health, finance and legal agents give advice
  as the expert. Exclude regulated categories in the wedge, or require disclaimers.
- **Payout ops (K2).** Stripe Connect automates KYC and payouts, so this stays
  solo-operable if thresholds and holds are automated from day one.

## 7. Recommended spec, v1

1. **$24.99/month All-Access** (tax-exclusive, web checkout), or $20 if you
   accept ~$4 payouts.
2. **User-centric net contribution share, 50/50**, attributed by tier-weighted
   messages, calculated monthly per subscriber.
3. **Fair-use inference cap** of $3/subscriber/month at cost; media on credits.
4. **Referral bonus** for experts who bring their own subscribers.
5. **Paid escalations** and **expert-priced private agents** as separate,
   higher-share layers.
6. **Stripe Connect Express**, $25 minimum payout, 45-day hold, a public payout
   formula and a per-agent earnings dashboard (transparency is the trust feature).
