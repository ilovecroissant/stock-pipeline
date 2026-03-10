from app.models.database import SessionLocal
from app.models.stock import StockPrice

def save_to_db(df):
    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            price = StockPrice(**row.to_dict())
            db.merge(price)   # insert or update
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
