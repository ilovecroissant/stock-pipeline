from app.pipeline.fetcher     import fetch_stock_data
from app.pipeline.transformer import clean_stock_data
from app.pipeline.loader      import save_to_db
from app.logger import logger


TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN"]

def run_pipeline():
    logger.info("Pipeline started")
    for ticker in TICKERS:
        try:
            logger.info(f"Fetching {ticker}")
            raw_df   = fetch_stock_data(ticker)
            clean_df = clean_stock_data(raw_df)
            save_to_db(clean_df)
            logger.info(f"  ✓ {ticker}: {len(clean_df)} rows saved")
        except Exception as e:
            logger.error(f"  ✗ {ticker} FAILED: {e}")
    logger.info("Pipeline complete")


if __name__ == "__main__":
    run_pipeline()
