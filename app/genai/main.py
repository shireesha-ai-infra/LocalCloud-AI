from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="LocalCloud-AI GenAI API")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment")

# Initialize openai client
client = OpenAI(api_key=OPENAI_API_KEY)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_llm(payload: Question):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "user", "content":payload.question}
            ]
        )
        return {
            "answer" : response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"OpenAI error: {str(e)}"
        )