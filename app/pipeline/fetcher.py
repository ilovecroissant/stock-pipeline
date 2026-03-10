import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Dowload historical OHLCV data from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    df.reset_index(inplace=True) # make Date a regular column
    df["ticker"] = ticker
    return df

# Test it 
if __name__ == "__main__":
    df = fetch_stock_data("AAPL")
    print(df.head())