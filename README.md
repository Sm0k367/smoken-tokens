# Epic Agent Fabric

**The local-first, token-native operating system for autonomous agents.**  
Run powerful workflows on your hardware, plug agents into your own tools, and never get trapped in another expensive subscription.

Contact: epictechai@gmail.com · x.com/@EpicTechAI

---

## Why Epic Agent Fabric exists

Most agent platforms lock you into their cloud, their models, and their pricing. Epic Agent Fabric flips the script:

- Everything runs **locally or self-hosted** by default
- Agents get real power through a secure **Executor Gateway** (no leaked keys)
- A living **project memory brain** survives every session
- **TokenOS** makes compute costs visible, forecastable, and controllable
- 12+ battle-tested open-source tools are unified into one agent-native stack

This is not another chatbot wrapper. This is the foundation for production-grade, revenue-generating, anti-subscription agent workflows.

---

## The Five Pillars

### 1. Media Fabric — Generative production you control
End-to-end local pipelines for video, audio, and design:

| Tool | Purpose |
|------|---------|
| **Open Montage** | Research → script → stock footage → render |
| **OpenCut** | Agentic video editing (CapCut alternative) |
| **Voicebox** | Local voice cloning & TTS (ElevenLabs alternative) |
| **FluidVoice** | Offline dictation on Mac (Wispr Flow alternative) |
| **Penpot** | Self-hosted Figma with design-to-code handoff |

### 2. Agent OS Layer — The real leverage
Deep integrations that make agents actually useful:

| Tool | Purpose |
|------|---------|
| **Codebase Memory MCP** | Persistent repo memory & navigation for coding agents |
| **Zapier MCP** | One-click connections to Gmail, Calendar, Notion, etc. |
| **Agent Reach** | Live context from X, Reddit, YouTube, GitHub, web |
| **kortix-executor** | Secure MCP gateway for Stripe, models, and any API |

### 3. Intelligence Fabric — Context & forecasting
Agents that understand time, markets, and global events:

| Tool | Purpose |
|------|---------|
| **TimesFM** (Google Research) | Zero-shot time-series forecasting for sales, demand, token burn |
| **Daily Stock Analysis** | Automated watchlist summaries & buy/sell/hold signals |
| **World Monitor** | Self-hosted geopolitics, risk, and live event dashboard |

### 4. TokenOS — The economic layer (core moat)
Usage-based metering, real-time forecasting, and budget guardrails across every tool. Pay with compute credits or fiat. Quarterly "compute P&L" reports. Never get surprised by a bill again.

### 5. Prompt & Knowledge Layer
**System Prompt Leaks** as a living research dataset for better agent instructions, guardrails, and behavior libraries.

---

## Architecture that actually ships

### Executor Gateway (kortix-executor)
Agents never see raw API keys. They call a single MCP server:

| Tool | Purpose |
|------|---------|
| `connectors` | List every integration |
| `discover` | Intent search ("create a charge", "send slack message") |
| `describe` | Full JSON schema + risk level |
| `call` | Execute with server-side credential injection |

### Memory Brain (`.kortix/memory/`)
Every project has a living knowledge base curated by the `memory-reflector` agent. Durable facts only. Human-reviewed via Change Requests.

### Change Requests — the only way to land work
No agent merges its own code. Every memory edit, connector addition, or workflow change goes through human review.

### Permission Model
Agents declare exactly what they can do. The `mcp: "kortix-executor": allow` line is the on-ramp to every external tool — no raw `curl`, no bearer tokens in prompts.

---

## Quick start (secure by default)

1. Clone this repo
2. Add secrets in the Machine dashboard (`STRIPE_API_KEY`, model keys, etc.)
3. Grant agents the executor permission
4. Enable the memory-reflector trigger
5. Run locally or self-host with Docker
6. Ship — every action is audited, every key stays secret

---

## Security posture (non-negotiable)

- No API keys in git, prompts, or agent memory
- Everything external goes through the Executor Gateway
- Narrowest possible auth scopes on every connector
- Memory edits require human review via CR
- All calls logged and attributable

This is how you run autonomous agents that are powerful **and** safe.

---

## Philosophy

> I don't chase trends. I chase leverage.

The best tools disappear. The best platforms give you ownership.

Epic Agent Fabric is built for people who want:
- Local-first by default
- Agent-native everything
- Token-economical visibility and control
- A stack they actually own

No more renting your creativity. No more surprise bills. No more vendor lock-in.

---

## Files that matter

| Path | Purpose |
|------|---------|
| `kortix.toml` | Manifest, triggers, connectors |
| `.kortix/opencode/agents/` | Agent definitions + permissions |
| `.kortix/opencode/skills/kortix-executor/` | The four MCP tools |
| `.kortix/opencode/skills/kortix-memory/` | Memory rubric & tool |
| `.kortix/memory/` | The living project brain |
| `README.md` | This file |

---

**Epic Agent Fabric — local when it matters, autonomous when it should be, owned by design.**

Contact: epictechai@gmail.com · x.com/@EpicTechAI
