import pandas as pd
import numpy as np

def calculate_metrics(df: pd.DataFrame) -> dict:
    """Calculate key financial stats for a stock."""
    df = df.sort_values("date")
    df["daily_return"] = df["close"].pct_change()
    df["7d_ma"]        = df["close"].rolling(7).mean()   # 7-day moving avg
    df["30d_ma"]       = df["close"].rolling(30).mean()
    df["volatility"]   = df["daily_return"].rolling(30).std() * np.sqrt(252)
    return {
        "latest_close":   float(df["close"].iloc[-1]),
        "7d_avg":         float(df["7d_ma"].iloc[-1]),
        "30d_avg":        float(df["30d_ma"].iloc[-1]),
        "annualised_vol": float(df["volatility"].iloc[-1]),
        "30d_return":     float(df["daily_return"].tail(30).sum()),
    }
