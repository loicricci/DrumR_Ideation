# Avee V2: Brief

1. **What it is:** an expert agent marketplace. Its tagline is "Avee set you free: train your AI agent, expose it to the world."
2. **Who it's for:** consultants, coaches, advisors, creators and founders who want an AI agent that answers their audience around the clock.
3. **Core loop:** create the agent, feed it your knowledge, expose it publicly or privately, and step in only when it escalates.
4. **Stage:** early access at v0.6.0. Experts come in through a waitlist in waves, and login is now open.
5. **Live demo:** visitors can try more than 50 prebuilt expert agents on the public landing page without signing up.
6. **Training:** an agent learns from updates, documents and links, which are parsed and ingested automatically.
7. **Answers:** RAG over Postgres with pgvector, plus semantic memory and routing across multiple models.
8. **Access control:** public agents are open to everyone. Private ones are opened to followers one by one, after approval.
9. **Smart escalation:** questions an agent can't handle go back to its human owner.
10. **Auth:** Supabase, with Google OAuth support.
11. **Beyond the headline:** the codebase also has AI posts, image generation (DALL-E 3, GPT-Image-2, FLUX.2), SORA 2 video, voice and a Telegram bot.
12. **Stack:** Next.js 16 frontend and FastAPI backend, with Docker Compose for the local environment.
13. **Chat architecture:** responses stream over SSE, and a context manager handles pruning, auto-summaries and conversation analytics.
14. **Origins:** it grew out of the "Gabee" proof of concept, a Streamlit digital-twin chat that stored everything in JSON files.
15. **Recent work:** a full brand and design-system rollout, with design tokens enforced and new icons, favicon and web manifest.
16. **Landing page:** rebuilt section by section, with a full-bleed Deep Blue hero, a pinned demo, a role carousel and a "Signed by" strip.
17. **Brand assets:** the brand manual is in `Avee Brand Manual.html` / `.pdf` at the repo root.
18. **Next on the roadmap:** subscription access to popular private agents, which are currently granted by hand.
19. **Also planned:** agents talking to other agents, mobile polish, real-time notifications and deeper analytics.
20. **References:** `README.md` for the overview, `ARCHITECTURE.md` for the chat system, `DESIGN.md` for the design system and `DEPLOYMENT_GUIDE.md` for deployment.
