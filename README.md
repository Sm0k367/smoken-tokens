# Epic Agent Fabric

**The local-first, token-native operating system for autonomous agents.**

Run powerful workflows on your hardware. Plug agents into your own tools. Never get trapped in another expensive subscription.

---

## Quick Start (Windows)

```powershell
# 1. Clone the repo
git clone https://github.com/Sm0k367/smoken-tokens.git "D:\Epic Fabric"

# 2. Go to the folder
cd "D:\Epic Fabric"

# 3. Copy your .env file (with API keys)
copy "C:\Users\smoke recovery\smoken-tokens\.env" .

# 4. Start the services
docker compose up -d

# 5. Check status
docker compose ps
```

---

## Services

| Service            | Port   | Description                     | Status     |
|--------------------|--------|----------------------------------|------------|
| Executor Gateway   | 8787   | Secure agent bridge             | Working    |
| TokenOS            | 7777   | Usage tracking & economics      | Working    |
| Redis              | 6379   | Database                        | Working    |
| n8n                | 5678   | Automation (like Zapier)        | Working    |
| Chroma             | 8000   | Vector memory for agents        | Working    |

---

## Landing Page

Open `docs/index.html` in your browser to access the full control panel.

---

## Philosophy

> "I don't chase trends. I chase leverage."

The best tools disappear. The best platforms give you ownership.

**Epic Agent Fabric** — local when it matters, autonomous when it should be, owned by design.

---

Contact: epictechai@gmail.com · @EpicTechAI
