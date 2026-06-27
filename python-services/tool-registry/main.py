# Tool Registry Service

from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI(title="Tool Registry")

class ToolCall(BaseModel):
    tool: str
    action: str
    parameters: dict = {}

@app.post("/call")
async def call_tool(req: ToolCall):
    # Route to Executor Gateway
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://executor-gateway:8787/call",
            json={
                "tool": req.tool,
                "action": req.action,
                "parameters": req.parameters
            }
        )
        return response.json()

@app.get("/tools")
def list_tools():
    return {
        "available_tools": [
            "executor-gateway",
            "n8n",
            "chroma"
        ]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Tool Registry"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8300)
