from apscheduler.schedulers.background import BackgroundScheduler
from app.pipeline.run import run_pipeline

scheduler = BackgroundScheduler()

# Run every weekday at 5:30 PM (after market close)
scheduler.add_job(
    run_pipeline,
    trigger="cron",
    day_of_week="mon-fri",
    hour=17,
    minute=30
)

# In app/main.py — start/stop with the app:
@app.on_event("startup")
def start_scheduler():
    scheduler.start()

@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()
