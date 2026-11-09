# Signals verification — run 2026-11-09-2215

Checked on 2026-11-09. Each cited URL in `signals.md` was opened with a plain
HTTP request and the quote was searched for in the page text (allowing only
punctuation/quote-mark differences). No bot-check workarounds or mirrors were
used: pages that refused a plain request are marked **could not open**.

**Result:** 28 cited pages, 25 opened. Of the quoted claims with a URL,
**14 are confirmed on the page**, **14 are not on the page** (reworded,
misattributed, or absent), and **5 could not be checked** because the page
refused or no longer exists. 7 quotes had no URL at all.

Legend: ✅ confirmed · ⚠️ on page but wording/context differs · ❌ not on page ·
🚫 could not open · — no URL given

---

## Per-signal results

### SIG-01 — Freelancer late-invoice chasing → **weak** (was medium)
- 🚫 "I track everything in a spreadsheet…" — indiehackers.com returns a
  Cloudflare "enable JavaScript and cookies" challenge. Also note: the signal
  labels this Reddit, but the URL is Indie Hackers.
- ❌ "I didn't want to seem difficult… So I waited and hoped." — dev.to page
  opens (Landolio, Mar 25) but this sentence is not on it.
- Net: no first-hand quote confirmed.

### SIG-02 — Local owners skip Google review replies → **medium** (unchanged)
- ✅ "only 9.8% of one-star reviews ever got a reply" — ueni.com. The 229,882
  reviews, 19.5 days and 606 characters figures are all on the page too.
- ✅ "there is not enough time" — replient.ai, verbatim: *"The main reason is
  simple: there is not enough time."*
- ❌ "the owner is busy running the business" — not on the replient page.

### SIG-03 — Solo practitioners overpay for scheduling tools → **weak** (unchanged; quotes now solid)
- ✅ "As a sole staff member perhaps a cheaper version for individual use" —
  Capterra vcita reviews.
- ✅ "The cost of Acuity scheduling to access all premium features is high
  compared to alternatives for small businesses and small non-profits." —
  Capterra Acuity reviews.
- ❌ Counter-signal "great value for the cost" — not on the Acuity page
  fetched (may be on a later review page).

### SIG-04 — Teachers pay out of pocket for worksheet/AI tools → **weak** (was medium)
- ⚠️ The "keeps paying" quote is real but **about a different tool**. Verbatim:
  *"Willow Voice ($15/mo, my money) dictation… $15/mo out of a teacher salary
  isn't nothing but it saves me enough time that I keep paying."* It is a
  dictation app, not a worksheet/differentiation tool. The thread is
  **r/teaching**, not r/Teachers.
- ✅ Counter quote, verbatim: *"I refuse outright to pay for anything
  work-related out of my pocket. I've been firm with the school and told them
  they have to cough up if they require anything specific in the classroom."*
- ⚠️ "most teachers using paid tiers pay out of pocket" — not on
  aitoolsbakery.com. The page says: *"In a category where most teachers are
  spending their own money, what you get for nothing may matter more than what
  the paid tier costs."*
- Net: out-of-pocket spend is real, but no quote ties it to the worksheet job.

### SIG-05 — Clip-tool credit pricing → **unverified** (medium on hold)
- 🚫 Both Trustpilot quotes — trustpilot.com returns 403 to automated requests.
  Needs a manual check in a browser.

### SIG-06 — Resume re-tailoring burnout → **weak** (unchanged)
- ❌ "Anyone else exhausted by tweaking resumes for every JD?" — not on the
  smartcvs.ai page.
- ❌ "every application felt like 30 to 45 minutes of rework…" — not on that
  page either. The page is dated 2 Oct 2025 (signal said 2026).

### SIG-07 — Self-publishers dread book descriptions → **weak** (unchanged)
- ❌ "Authors often write descriptions from the author's point of view…" — not
  on vappingo "book-description-hate-marketing" (page updated Sept 2026; it
  says *"Many authors dislike description writing because it feels like
  turning a book into hype."*).
- ❌ "AI descriptions tend to be generic and weak…" — not on the KDP listing
  generator page.

### SIG-08 — Freelancer tax-time receipt scramble → **weak** (was medium)
- 🚫 community.tofu.com thread returns **410 Gone** — the page was deleted.
- — "tax season turns into a multi-day scramble" has no URL.
- Net: no evidence confirmed.

### SIG-09 — Podcast show notes take hours → **weak** (was medium)
- ⚠️ castmagic.io, close but longer: *"manually creating quality show notes for
  a single episode can consume two to four hours (or more!)"*. Vendor selling
  the fix.
- ❌ "timestamps… can drift by 30-60 seconds" — not on the codewords.ai page.

### SIG-10 — Shopify per-order app pricing → **strong** (unchanged, one caveat)
- ✅ "it's crazy expensive due to its per order pricing model" — MESA review,
  Pixie Wing, 1/5, Feb 7 2025.
- ✅ "upgraded us from $12 Basic plan to $99 per month" — same review.
  Small fix: the wording is *"considered each order 'a task'"*, not "counted".
  Note the reviewer frames it as *"if you're a high-volume store that just
  needs a tiny portion of the app's functionality"*.
- ⚠️ community.shopify.com thread exists with that title and $105, but it is
  about **Shopify's own plan** ($5 Starter → $105 to send customer data via
  API), not app pricing. Doesn't support this signal.
- ✅ "usage fees are ridiculous" — Kaktus pre-order review.
- — Counter quote ("only makes sense for stores earning upwards of 10k…") has
  no URL and is not on the Kaktus page.

### SIG-11 — Newsletter/blog repurposing eats an evening → **medium**, now with clean verbatim
- ✅ Upgraded from paraphrase to verbatim (Reddit post by u/Icy-Suggestion3512,
  snapshot May 15 2026, 16 points, 21 comments): *"Every time I publish a blog
  post I lose an entire evening just adapting it for Substack, LinkedIn,
  Medium, and X."* … *"The original post took me two hours. The adaptation
  takes another two."* … *"The worst part is the mental load. I finish the
  'distribution session' and I'm drained."* (Blogger, not strictly a
  newsletter writer.)
- ❌ "5 hours every week manually reformatting…" — not on the levelupwithai
  Substack post (Aug 5 2026). It only says *"hours of manual posting every
  single week"*.

### SIG-12 — YouTube "inauthentic content" demonetization → **medium** (unchanged)
- ❌ "a minor update to our longstanding guideline" — not on the cited
  tubefilter article. That article does say *"To be clear, this is not a new
  policy. The update is a communications fix."*
- ✅ cxotoday.com, verbatim: *"That appeal was auto-rejected on a Sunday evening
  within an hour of submission. Backend analytics confirmed the proof video had
  received zero views."* (Describes a team, not a solo creator.)

### SIG-13 — Bloggers losing traffic to AI Overviews → **strong pain** (unchanged)
- ❌ "I used to employ 10 people. Today? Zero." — not on the NichePursuits page.
  What the page does say: traffic fell from ~1M page views/month (2022) to
  about 200,000; ad revenue was $20–30k/month via Mediavine; *"Carrie is still
  full-time, still publishing, and still earning"*. Title: "Losing 80% of Her
  Traffic". Less dramatic than the quote.
- ✅ storyboard18.com headline matches exactly.

### SIG-14 — DM prep time → **weak** (unchanged)
- — Both quotes have no URL. Cannot verify.

### SIG-15 — Photographer culling backlog → **weak** (was medium)
- ❌ Shotkit "nearly two hours at their desk editing" stat — not on the
  narrative.so page (no mention of Shotkit at all).
- 🚫 share.aftershoot.com — host does not resolve.
- Net: no evidence confirmed.

### SIG-16 — Fitness coach spreadsheet check-ins → **weak** (unchanged)
- ❌ The hubfit URL now **redirects** to a different article ("The ultimate
  guide to online coaching check-ins"); the Google Sheets/Excel quote is not
  there.
- — r/personaltraining quote has no URL.

### SIG-17 — Agents dislike writing listing descriptions → **weak** (unchanged)
- ✅ Upgraded from paraphrase to verbatim (u/nofishies): *"If you don't like
  writing listing descriptions, it's worth training an AI agent to write in
  your voice and put in highlights and let it turn it into a description.
  You'll usually wanna polish it one more time, because AI uses the same 10
  words and it's so incredibly obvious."*
- ✅ Extra counter-signal on the same thread: *"Please stop using AI for this.
  We are better than that, set yourself apart."*

---

## What changes

| Signal | Before | After | Why |
|---|---|---|---|
| SIG-01 | medium | weak | No quote confirmed |
| SIG-04 | medium | weak | Pay quote is about a dictation app, not worksheets |
| SIG-08 | medium | weak | Source page deleted (410) |
| SIG-09 | medium | weak | Only a vendor stat confirmed |
| SIG-15 | medium | weak | Neither source confirmed |
| SIG-05 | medium | on hold | Trustpilot blocks automated access — check by hand |
| SIG-10 | strong | strong | 3 of 4 quotes confirmed; drop the Shopify-community item |
| SIG-11 | medium | medium | First-hand verbatim now confirmed |

**Best-evidenced signals after verification:** SIG-10 (Shopify per-order app
pricing), SIG-11 (repurposing eats an evening), SIG-02 (review replies), SIG-13
(AI Overview traffic loss — pain confirmed, quote overstated).

**Needs a human in a browser:** SIG-05 (Trustpilot) and SIG-01 (Indie Hackers).
