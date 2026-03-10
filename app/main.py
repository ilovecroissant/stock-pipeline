from fastapi import FastAPI
from app.api import stocks, pipeline, analysis

app = FastAPI(
    title="Stock Intelligence API",
    description="ML pipeline API for stock market data",
    version="1.0.0"
)

app.include_router(stocks.router,   prefix="/api/stocks")
app.include_router(pipeline.router, prefix="/api/pipeline")
app.include_router(analysis.router, prefix="/api/analysis")

@app.get("/health")
def health_check():
    return {"status": "ok"}
