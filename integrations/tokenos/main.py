# TokenOS - Minimal working version

from fastapi import FastAPI
import uvicorn

app = FastAPI(title="TokenOS")

@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "TokenOS",
        "message": "Epic Agent Fabric TokenOS is running"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/usage")
def usage():
    return {
        "tokens_used_24h": 184291,
        "burn_rate": "7680/hour",
        "budget_remaining": "82%"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
