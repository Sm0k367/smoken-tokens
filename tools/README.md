# Epic Agent Fabric — Tools Directory

This folder contains thin, production-ready adapters and CLI helpers that connect the 12 core open-source projects into the Fabric.

## Current tools (stubs ready for real integration)

- `agent-reach` — X/Reddit/YouTube/GitHub/web
- `timesfm` — forecasting
- `world-monitor` — geopolitics/risk
- `prompt-layer` — system prompt research

## How to add a new tool

1. Create `tools/<tool-name>/`
2. Add `adapter.py` or `index.js` that exposes MCP-compatible endpoints
3. Register in `docker-compose.yml`
4. Update `kortix.toml` connector list
5. Document in `integrations/<tool-name>/README.md`

All tools must:
- Never expose raw credentials to agents
- Go through the Executor Gateway when external
- Be metered by TokenOS
- Support graceful degradation when offline
