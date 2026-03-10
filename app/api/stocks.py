from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.stock import StockPrice

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{ticker}")
def get_stock_prices(ticker: str, limit: int = 30, db: Session = Depends(get_db)):
    """Return the most recent N days of prices for a ticker."""
    prices = (db.query(StockPrice)
               .filter(StockPrice.ticker == ticker.upper())
               .order_by(StockPrice.date.desc())
               .limit(limit)
               .all())
    if not prices:
        raise HTTPException(status_code=404, detail="Ticker not found")
    return prices

@router.get("/{ticker}/latest")
def get_latest_price(ticker: str, db: Session = Depends(get_db)):
    """Return the single most recent price for a ticker."""
    price = (db.query(StockPrice)
               .filter(StockPrice.ticker == ticker.upper())
               .order_by(StockPrice.date.desc())
               .first())
    if not price:
        raise HTTPException(status_code=404, detail="Not found")
    return price