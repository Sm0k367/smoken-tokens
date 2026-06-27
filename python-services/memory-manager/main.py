# Memory Manager Service

from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from chromadb.config import Settings
import uuid

app = FastAPI(title="Memory Manager")

# Connect to Chroma
client = chromadb.HttpClient(host="chroma", port=8000)

class MemoryRequest(BaseModel):
    collection: str
    text: str
    metadata: dict = {}

class QueryRequest(BaseModel):
    collection: str
    query: str
    n_results: int = 5

@app.post("/add")
def add_memory(req: MemoryRequest):
    collection = client.get_or_create_collection(req.collection)
    doc_id = str(uuid.uuid4())
    collection.add(
        documents=[req.text],
        metadatas=[req.metadata],
        ids=[doc_id]
    )
    return {"status": "success", "id": doc_id}

@app.post("/query")
def query_memory(req: QueryRequest):
    collection = client.get_or_create_collection(req.collection)
    results = collection.query(
        query_texts=[req.query],
        n_results=req.n_results
    )
    return results

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Memory Manager"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)
