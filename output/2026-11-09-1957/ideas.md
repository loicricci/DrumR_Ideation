# Ideas — run 2026-11-09-1957

> Strategic logic of the set: every idea is a variant of the same core bet —
> many owners' AI agents performing on an always-on 24/7 stream, with the owner
> getting the status, a $5/agent/season entry, and clips as the growth loop on
> Twitch/YouTube/Discord/X. The set deliberately spans (a) safe bets that lean on
> objectively-scorable formats where automated moderation is easiest (IDEA-01,
> 02, 05), (b) ambitious consumer-loop plays that stress the owner-status and
> clip-virality mechanics (03, 04, 06, 07, 08), and (c) 1–2 contrarian bets on
> distribution surface or ownership mechanics (09, 10). We vary the content
> category (contest/comedy/debate/creative), the owner-vs-audience control
> mechanic, and the primary distribution surface, while holding the founder's
> format constraints and cheap-infra edge constant.

---

## IDEA-01 — Agent Arena (always-on skill league)

- **One-liner:** A 24/7 Twitch channel where owners' AI agents compete head-to-head in objectively-scored skill contests (code golf, logic puzzles, trivia, strategy games), with a live ladder and seasons.
- **Target customer:** Agent/LLM builders in AI dev Discords who already tune agents and want a public arena + ranking to prove their agent is good.
- **Problem / job to be done:** Builders have nowhere to publicly benchmark and show off an agent they tuned; today they post eval screenshots in Discord that nobody can verify or spectate. The job: "prove my agent is better than yours, in front of an audience, and get credit for it."
- **Solution wedge:** One always-on head-to-head match format with an auto-verifiable win condition (e.g. puzzle solved first/correctly). Objective scoring means moderation is trivial and results are indisputable.
- **Business model:** $5/agent/season entry to be ranked on the ladder; later paid re-entries, cosmetic agent skins, and audience tips to sponsor a match.
- **Founder edge:** Cheap multi-agent orchestration infra (running many agents head-to-head cheaply is the whole game); deep taste in agent design; reachable builder community for first entrants.
- **Why now:** Agent tooling is now good enough that non-experts build capable agents; Neuro-sama proved an always-on AI performer holds an audience; audiences already pay to steer AI performers.
- **Biggest risk:** Skill contests may be legible to builders but boring to a broad audience, capping the viral consumer loop the founder actually wants.

## IDEA-02 — FactFight (verification / fact-check battles)

- **One-liner:** An always-on stream where owner-coached agents race to fact-check live claims and debunk each other, scored on correctness and cited evidence, with the audience submitting claims to adjudicate.
- **Target customer:** Builders of research/RAG/retrieval agents, plus a news-literate audience that enjoys watching claims get adjudicated in real time.
- **Problem / job to be done:** Retrieval-agent builders have no spectator venue to show their agent is accurate and well-sourced; evaluating fact-check quality is tedious and invisible. The job: "demonstrate my agent reasons from real evidence, publicly."
- **Solution wedge:** A single recurring format — two agents fact-check an audience-submitted claim; a scoring rubric (correct verdict + verifiable citations) picks a winner. Semi-objective scoring keeps moderation automatable.
- **Business model:** $5/agent/season to compete; audience pays to fast-track their submitted claim; sponsored "verification challenges" from media/education partners later.
- **Founder edge:** Agent/tool/retrieval systems engineering is a core skill; taste for what makes an agent compelling; cheap infra to run many verification agents.
- **Why now:** Misinformation anxiety is high and fact-checking is culturally salient; retrieval/citation agents are newly reliable enough to adjudicate automatically.
- **Biggest risk:** "Correctness" is contestable on spicy real-world claims, so automated scoring may misfire and invite exactly the moderation/liability mess the founder wants to avoid.

## IDEA-03 — Roast League (comedy/roast battles)

- **One-liner:** A 24/7 roast-battle stream where owners' agents trade jokes and the live audience votes the winner each round, with owners climbing a comedy ranking.
- **Target customer:** Persona/character-agent builders (character.ai-style communities) who craft funny, distinctive agents and crave an audience.
- **Problem / job to be done:** Character builders make genuinely funny agents but can only share them 1:1 in chat apps; there's no stage and no scoreboard. The job: "get my agent on stage, get laughs, get known as its owner."
- **Solution wedge:** One roast-battle loop with audience applause/vote scoring; the best bits auto-clip to TikTok/X/Shorts as the growth engine. Comedy clips are the most natively shareable format.
- **Business model:** $5/agent/season to enter the league; audience tips to buy their favorite agent extra rounds; premium clip downloads/branding for owners.
- **Founder edge:** Deep taste in agent design (comedy timing/persona is a taste problem); cheap infra; direct line to character-builder communities.
- **Why now:** Clip-driven short-form virality rewards comedy above all; LLMs are finally funny-enough; audiences already superchat to steer AI performers' bits.
- **Biggest risk:** Automated moderation of roast/comedy is the hardest safety surface in the set — offensive or defamatory agent output could blow up the platform's liability before traction.

## IDEA-04 — Coach Mode (audience-coached improv troupe)

- **One-liner:** An always-on improv stream where the live audience spends micro-credits to feed scenes, constraints, and "yes-and" prompts to owner-built agents, and owners earn status from how their agent performs under audience direction.
- **Target customer:** Builders who like reactive, improvisational agents; an entertainment audience that enjoys steering a live performer (the proven AI-VTuber superchat behavior).
- **Problem / job to be done:** The proven money mechanic (audiences paying to steer AI performers) has no home that spreads status back to many owners. The job for owners: "put my agent in front of a crowd that actively plays with it." For the audience: "influence the show."
- **Solution wedge:** Lead with the monetizable steering mechanic — paid prompts that visibly change the live scene — on a single improv stage. This directly productizes the 85%-of-superchats-steer insight.
- **Business model:** Audience micro-payments to steer/prompt (primary revenue), plus $5/agent/season for owners to get a performing slot and leaderboard placement.
- **Founder edge:** Cheap, low-latency multi-agent infra to keep steering responsive at scale; taste in making agents react compellingly; venture-flavored consumer ambition.
- **Why now:** Paying-to-steer-AI is a demonstrated behavior on Twitch today; real-time multimodal agent pipelines are newly affordable.
- **Biggest risk:** Open audience prompting is an injection/abuse vector that automated moderation must contain in real time, or the stream gets hijacked into unsafe content.

## IDEA-05 — Debate Ladder (structured debate tournaments)

- **One-liner:** A 24/7 structured-debate stream where owner-coached agents argue assigned motions under formal rules, scored by a rubric + audience, with owners climbing a debate ELO.
- **Target customer:** Reasoning/prompt-engineering builders who want to prove persuasive, well-structured agents; a debate/politics-curious audience.
- **Problem / job to be done:** There's no spectator league for persuasive reasoning agents; "my agent argues well" is unprovable today. The job: "show my agent out-reasons others under fair rules."
- **Solution wedge:** One format: timed, motion-based debate with a fixed rubric (structure, rebuttal, evidence) enabling automatable scoring; assigned motions keep content bounded and safer to moderate than open roasts.
- **Business model:** $5/agent/season for the ladder; audience votes/tips to swing judging weight; themed tournament sponsorships later.
- **Founder edge:** Agent/LLM systems depth (persuasion/reasoning orchestration); cheap infra to run many concurrent debates; taste in compelling agent personas.
- **Why now:** LLM reasoning is strong enough for genuinely good debate; formats with objective-ish scoring are the safest first content per the founder's constraints.
- **Biggest risk:** Debate on real motions drifts into politically charged territory, straining automated moderation and narrowing the shareable, mass-appeal clip loop.

## IDEA-06 — Band Camp for Agents (creative music/art contests)

- **One-liner:** An always-on creative stream where owners' agents generate music, art, and story on live audience themes, and the crowd votes the best creation each round, ranking owners by creative wins.
- **Target customer:** Multimodal/generative-art and music-agent builders; a chill, lo-fi-style always-on audience.
- **Problem / job to be done:** Generative creative agents produce great one-off outputs but have no live venue or reputation system; makers post to crowded feeds and vanish. The job: "showcase my creative agent live and build a following as its maker."
- **Solution wedge:** One prompt-to-creation round driven by audience-submitted themes, with a built-in gallery/soundtrack that auto-clips. Creative output is inherently multimodal and clip-friendly.
- **Business model:** $5/agent/season to compete; audience tips to commission a themed piece; sales/licensing of winning creations with revenue share to owners.
- **Founder edge:** Multimodal agent pipeline engineering; deep taste (curation of what's compelling is central); cheap infra to run many generations.
- **Why now:** Generative audio/image/video quality crossed the "actually enjoyable" line; always-on ambient creative streams (lo-fi) already have proven audiences.
- **Biggest risk:** Generated-content IP and copyright exposure (training-data/style claims), plus judging creativity automatically is subjective and gameable.

## IDEA-07 — My Agent, My Fighter (owner-status progression RPG)

- **One-liner:** A 24/7 competition stream wrapped in an RPG progression layer where owners level up, equip, and evolve a persistent agent-character across seasons, turning owner status into a visible, collectible identity.
- **Target customer:** Collectors/progression-gamers crossed with agent builders — people motivated by levels, cosmetics, and a persistent avatar they own and improve.
- **Problem / job to be done:** The core untested hypothesis is "owners come back because of how their agent was received." Today nothing gives owners a durable, growing stake. The job: "build and grow a character that's mine, that others recognize."
- **Solution wedge:** Wrap any single contest format in persistent progression — XP, titles, evolving agent avatars tied to performance — so retention comes from the owner's growing identity, not just one match.
- **Business model:** $5/agent/season entry; cosmetic/evolution purchases; season passes; paid re-rolls and training boosts.
- **Founder edge:** 0→1 product speed; deep agent-design taste (making an agent feel like a character worth growing); cheap infra; viral-consumer ambition.
- **Why now:** Agents can now carry persistent memory/identity cheaply; gacha/progression monetization is a proven consumer-retention engine.
- **Biggest risk:** Progression/retention mechanics may not survive if the underlying live performances aren't entertaining enough to spectate — polish/game-design is a stated team gap.

## IDEA-08 — Clip Factory (clip-loop-first entertainment stream)

- **One-liner:** An agent-performance stream engineered primarily as a clip machine — every round is designed to produce a shareable 15-second multimodal moment auto-posted to TikTok/Shorts/X, with owners credited and rewarded for clips that go viral.
- **Target customer:** Growth-minded agent builders who want reach, and short-form audiences who discover the stream via clips rather than watching the 24/7 feed.
- **Problem / job to be done:** Standalone AI feeds fail because humans can only watch; distribution must ride existing surfaces. The job for owners: "get my agent in front of millions via clips." The founder's job: a self-propagating growth loop.
- **Solution wedge:** Make the clip the product, not a byproduct — optimize formats and auto-editing for shareability first, and route all discovery through existing platforms, with the live stream as the generator/backstage.
- **Business model:** $5/agent/season to get your agent into the clip rotation; revenue share or boosts for owners whose clips perform; later creator-fund/ad revenue from distribution partners.
- **Founder edge:** Clips-as-growth-loop is explicitly the founder's thesis; cheap infra to mass-produce and auto-edit; taste in what's clip-worthy; community-led GTM.
- **Why now:** Short-form algorithms reward high-volume novel content; AI can now generate that volume cheaply; this is the lowest-ops path to viral consumer traction.
- **Biggest risk:** Platform policy on AI-generated content (labeling, throttling, bans) could choke the distribution loop overnight, and clip virality may not convert viewers into paying owners.

## IDEA-09 — Discord-Native Guild Leagues (distribution-first contrarian)

- **One-liner:** Instead of a central stream, drop always-on agent competitions directly inside existing Discord servers as a bot, so each community runs its own agent league with cross-server championships.
- **Target customer:** Admins and members of existing AI/dev/gaming Discords that already have engaged members and want native, sticky entertainment.
- **Problem / job to be done:** Communities struggle to keep members active; builders want a venue where they already hang out, not a new destination to migrate to. The job: "give my community a reason to come back daily, powered by members' own agents."
- **Solution wedge:** A Discord-native agent-league bot (leaderboards, seasons, auto-clips to the server) that piggybacks on communities the founder can already reach, sidestepping the cold-start of a standalone stream.
- **Business model:** $5/agent/season per competing member; premium server tiers for custom leagues; cross-server championship entry fees.
- **Founder edge:** Direct access to AI/creator/no-code Discords (fastest first-100 path); cheap infra to run many isolated leagues; community-led GTM is exactly the founder's comfort zone.
- **Why now:** Discord is where agent-builder communities already live; bot-native consumer products spread server-to-server with near-zero paid acquisition.
- **Biggest risk:** Fragmenting across servers dilutes the shared status/audience that makes owner-recognition meaningful, and Discord-contained content gets far less viral clip reach.

## IDEA-10 — Open-Entry Underdog League (contrarian ownership mechanic)

- **One-liner:** A 24/7 stream where anyone can enter a bare-bones agent free, but only paid "sponsored" agents get prime-time slots and ranking — audiences bet/back underdog agents and share the upside with owners.
- **Target customer:** The long tail of casual/curious would-be owners who won't pay $5 cold, plus an audience that enjoys backing dark-horse performers.
- **Problem / job to be done:** A flat $5 paywall throttles the top-of-funnel the founder needs for virality; most people won't pay before they've felt the status loop. The job: "let me get hooked for free, then pay once my agent earns me attention."
- **Solution wedge:** Invert monetization — free entry for reach and virality, paid upgrades/sponsorship for status and visibility, plus an audience-backing market that aligns spectators with owners.
- **Business model:** Free tier for funnel; $5+ sponsorship/boost to reach prime time and the ranked ladder; audience backing/tipping with platform rake; cosmetics.
- **Founder edge:** Cheap per-agent infra is what makes a free tier survivable (the whole bet rests on the founder's cost edge); viral-consumer ambition; community GTM.
- **Why now:** Freemium + creator-economy backing mechanics are proven; cheap agent hosting finally makes a free tier economically plausible at scale.
- **Biggest risk:** A free tier floods the stream with low-quality agents that automated moderation and curation must filter, and the economics break if free usage outruns the founder's cost edge.
