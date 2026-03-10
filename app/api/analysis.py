# app/api/analysis.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.models.database import SessionLocal
from app.services.rag import ask_about_stock

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class QuestionRequest(BaseModel):
    question: str

@router.post("/{ticker}/ask")
def ask_ai(ticker: str, body: QuestionRequest, db = Depends(get_db)):
    """Ask the AI a question about a specific stock using real DB data."""
    answer = ask_about_stock(ticker, body.question, db)
    return {"ticker": ticker, "question": body.question, "answer": answer}

# Example call:
# POST /api/analysis/AAPL/ask
# Body: {"question": "What was the trend over the last 2 weeks?"}
