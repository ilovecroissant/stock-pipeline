# pip install ollama

# app/services/rag.py
import ollama
from app.models.stock import StockPrice

def build_context_from_db(ticker: str, db) -> str:
    """Pull recent data from DB and format as LLM context."""
    prices = (db.query(StockPrice)
               .filter(StockPrice.ticker == ticker)
               .order_by(StockPrice.date.desc())
               .limit(30).all())
    rows = [f"{p.date}: close={p.close}, volume={p.volume}" for p in prices]
    return "\n".join(rows)

def ask_about_stock(ticker: str, question: str, db) -> str:
    """Send a question + real DB data to Llama3 and get an answer."""
    context = build_context_from_db(ticker, db)
    prompt  = f"""You are a financial analyst.
Here is recent data for {ticker}:
{context}

Question: {question}
Answer concisely and cite specific numbers from the data."""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
