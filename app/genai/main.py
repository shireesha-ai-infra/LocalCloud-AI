from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="LocalCloud-AI GenAI API")

OLLAMA_BASE = os.getenv(
    "OLLAMA_BASE_URL",
    "http://host.docker.internal:11434"
)

OLLAMA_URL = f"{OLLAMA_BASE}/api/generate"
MODEL = "phi3"

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_llm(payload: Question):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": payload.question,
            "stream": False
        },
        timeout=60
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Ollama error: {response.text}")
    
    data = response.json()
    return{
        "answer": data.get("response", "")
    }