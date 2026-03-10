from app.pipeline.fetcher     import fetch_stock_data
from app.pipeline.transformer import clean_stock_data
from app.pipeline.loader      import save_to_db

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN"]

def run_pipeline():
    for ticker in TICKERS:
        print(f"Fetching {ticker}...")
        raw_df   = fetch_stock_data(ticker)
        clean_df = clean_stock_data(raw_df)
        save_to_db(clean_df)
        print(f"  ✓ {ticker} saved ({len(clean_df)} rows)")

if __name__ == "__main__":
    run_pipeline()
