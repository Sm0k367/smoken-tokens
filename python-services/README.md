# Python Services for Epic Agent Fabric

This folder contains all the core Python microservices that power the agent system.

## Services

| Service            | Port   | Description |
|--------------------|--------|-------------|
| memory-manager     | 8100   | Long-term vector memory using Chroma |
| llm-gateway        | 8200   | Unified interface for Groq, OpenAI, Ollama |
| tool-registry      | 8300   | Tool discovery and management |
| agent-runner       | 8400   | Main agent execution engine |

## How to Run

```bash
# Start all Python services
docker compose -f docker-compose.python.yml up -d
```

## Architecture

- All services communicate via HTTP
- They connect to the existing Executor Gateway for external tools
- Memory is shared via Chroma
- LLM calls go through the LLM Gateway for consistency
