# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from agent.manual_agent import handle_query

app = FastAPI(title="Krishi Saathi API")

class Query(BaseModel):
    text: str

@app.post("/query")
def query(q: Query):
    return handle_query(q.text)

# Run: uvicorn app:app --reload --port 8000
