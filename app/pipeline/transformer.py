import pandas as pd

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove bad rows, rename columns, cast types."""
    df = df.dropna(subset=["Close", "Volume"])  # remove empty rows
    df = df[df["Volume"] > 0]                    # remove zero-volume days
    df = df.rename(columns={
        "Open": "open", "High": "high",
        "Low": "low",   "Close": "close",
        "Volume": "volume", "Date": "date"
    })
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df[["date", "open", "high", "low", "close", "volume", "ticker"]]
