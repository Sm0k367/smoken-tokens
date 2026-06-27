# Agent Runner Service

from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="Agent Runner")

class AgentRequest(BaseModel):
    prompt: str
    model: str = "llama3"
    provider: str = "ollama"
    use_memory: bool = True

@app.post("/run")
async def run_agent(req: AgentRequest):
    # 1. Get context from memory (if enabled)
    context = ""
    if req.use_memory:
        async with httpx.AsyncClient() as client:
            memory_response = await client.post(
                "http://memory-manager:8100/query",
                json={"collection": "agent_memory", "query": req.prompt, "n_results": 3}
            )
            if memory_response.status_code == 200:
                results = memory_response.json()
                context = "\n".join(results.get("documents", [[]])[0])

    # 2. Build full prompt
    full_prompt = f"Context:\n{context}\n\nQuestion: {req.prompt}" if context else req.prompt

    # 3. Call LLM Gateway
    async with httpx.AsyncClient() as client:
        llm_response = await client.post(
            "http://llm-gateway:8200/generate",
            json={
                "provider": req.provider,
                "model": req.model,
                "prompt": full_prompt
            }
        )
        result = llm_response.json()

    # 4. Save to memory
    if req.use_memory:
        async with httpx.AsyncClient() as client:
            await client.post(
                "http://memory-manager:8100/add",
                json={
                    "collection": "agent_memory",
                    "text": f"Q: {req.prompt}\nA: {result}",
                    "metadata": {"type": "agent_interaction"}
                }
            )

    return {"response": result, "used_memory": req.use_memory}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Agent Runner"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8400)
