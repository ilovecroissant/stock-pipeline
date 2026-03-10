from sqlalchemy import Column, Integer, String, Date, Numeric, BigInteger
from .database import Base

class StockPrice(Base):
    __tablename__ = "stock_prices"
    id      = Column(Integer, primary_key=True)
    ticker  = Column(String(10))
    date    = Column(Date)
    open    = Column(Numeric(12,4))
    close   = Column(Numeric(12,4))
    high    = Column(Numeric(12,4))
    low     = Column(Numeric(12,4))
    volume  = Column(BigInteger)
