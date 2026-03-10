# app/api/health.py
from fastapi import APIRouter, Depends
from datetime import datetime
from app.models.database import SessionLocal
from app.models.stock import StockPrice

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/health/detailed")
def detailed_health(db = Depends(get_db)):
    row_count = db.query(StockPrice).count()
    return {
        "status":    "ok",
        "timestamp": datetime.now().isoformat(),
        "db_rows":   row_count,
    }