# Epic Agent Fabric

**The local-first, token-native operating system for autonomous agents.**

Run powerful workflows on your hardware. Plug agents into your own tools. Never get trapped in another expensive subscription.

---

## Real-World Use Case

Epic Agent Fabric is now a **production-ready, self-hostable platform** that unifies 12+ powerful open-source projects into one coherent agent operating system.

### What you get today

- **5 production pillars** with real Docker services
- **One-command local bootstrap** (`./scripts/setup.sh`)
- **Secure Executor Gateway** (no leaked keys)
- **TokenOS** economic layer with usage metering + forecasting
- **Living memory brain** (`.kortix/memory/`)
- **World-class landing page** ready for Vercel

### The 12 integrated tools (all wired)

| Pillar | Tools |
|--------|-------|
| **Media Fabric** | Open Montage, OpenCut, Voicebox, FluidVoice, Penpot |
| **Agent OS** | Codebase Memory MCP, Zapier MCP, Agent Reach, kortix-executor |
| **Intelligence** | TimesFM, Daily Stock Analysis, World Monitor |
| **TokenOS** | Burn forecasting, budget guardrails, token-native billing |
| **Prompt Layer** | System Prompt Leaks + guardrails |

---

## Quick Start (Real Deployment)

### 1. Clone & Bootstrap

```bash
git clone https://github.com/Sm0k367/smoken-tokens.git
cd smoken-tokens
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### 2. Add your keys

Edit `.env`:

```env
STRIPE_API_KEY=sk_test_...
GROQ_API_KEY=gsk_...
OPENAI_API_KEY=sk-...
ZAPIER_API_KEY=...
```

### 3. Run the full stack

```bash
docker compose up -d
```

Core services (Executor + TokenOS) start immediately.

Full stack (Media + Intelligence + everything):

```bash
docker compose --profile full up -d
```

### 4. Access points

- Landing page: `http://localhost:3000` (or your Vercel URL)
- Executor Gateway: `http://localhost:8787`
- TokenOS Dashboard: `http://localhost:7777`
- Voicebox: `http://localhost:5001`
- Penpot: `http://localhost:9001`
- TimesFM: `http://localhost:6001`
- World Monitor: `http://localhost:6002`

---

## Architecture (Production)

```
┌─────────────────────────────────────────────────────────────┐
│                    EPIC AGENT FABRIC                        │
├─────────────────────────────────────────────────────────────┤
│  Media Fabric     Agent OS       Intelligence   TokenOS     │
│  ────────────     ────────       ───────────    ──────      │
│  Open Montage     Executor GW    TimesFM        Metering    │
│  OpenCut          Zapier MCP     Stock Analysis Forecasting │
│  Voicebox         Agent Reach    World Monitor  Guardrails  │
│  FluidVoice       Memory MCP                    Billing     │
│  Penpot                                              │
├─────────────────────────────────────────────────────────────┤
│                    Prompt Layer (Research)                  │
└─────────────────────────────────────────────────────────────┘
```

Every service is:
- Containerized
- TokenOS-metered
- Agent-callable via MCP
- Self-hostable
- Gracefully degrades when offline

---

## Security & Ownership

- No API keys ever reach agents
- All external calls go through `kortix-executor`
- Human-reviewed Change Requests for every memory/code change
- TokenOS gives you real-time visibility into every compute cost
- Everything runs on **your** hardware by default

---

## Future-Proof Roadmap (already in the code)

- Q3 2026: Full TokenOS dashboard + per-agent cost attribution
- Q4 2026: Agent Marketplace
- 2027: Enterprise multi-tenant + on-prem
- Ongoing: 12+ new connectors

---

## Philosophy

> "I don't chase trends. I chase leverage."

The best tools disappear. The best platforms give you ownership.

Epic Agent Fabric is the foundation for the next decade of agent-native software — local when it matters, autonomous when it should be, owned by design.

---

**Contact**  
epictechai@gmail.com · @EpicTechAI

**Repo**  
https://github.com/Sm0k367/smoken-tokens

Built with curiosity • 2026
