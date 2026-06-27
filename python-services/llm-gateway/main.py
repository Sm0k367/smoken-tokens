# LLM Gateway Service

from fastapi import FastAPI
from pydantic import BaseModel
import os
import httpx

app = FastAPI(title="LLM Gateway")

class LLMRequest(BaseModel):
    provider: str = "groq"  # groq, openai, ollama
    model: str
    prompt: str
    max_tokens: int = 1000
    temperature: float = 0.7

@app.post("/generate")
async def generate(req: LLMRequest):
    if req.provider == "groq":
        return await call_groq(req)
    elif req.provider == "openai":
        return await call_openai(req)
    elif req.provider == "ollama":
        return await call_ollama(req)
    else:
        return {"error": "Unknown provider"}

async def call_groq(req: LLMRequest):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {"error": "GROQ_API_KEY not set"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": req.model,
                "messages": [{"role": "user", "content": req.prompt}],
                "max_tokens": req.max_tokens,
                "temperature": req.temperature
            }
        )
        return response.json()

async def call_openai(req: LLMRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": req.model,
                "messages": [{"role": "user", "content": req.prompt}],
                "max_tokens": req.max_tokens,
                "temperature": req.temperature
            }
        )
        return response.json()

async def call_ollama(req: LLMRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://ollama:11434/api/generate",
            json={
                "model": req.model,
                "prompt": req.prompt,
                "stream": False
            }
        )
        return response.json()

@app.get("/health")
def health():
    return {"status": "healthy", "service": "LLM Gateway"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8200)
