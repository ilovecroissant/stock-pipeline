from fastapi import APIRouter, BackgroundTasks
from app.pipeline.run import run_pipeline

router = APIRouter()

@router.post("/trigger")
def trigger_pipeline(background_tasks: BackgroundTasks):
    """Manually kick off the data ingestion pipeline."""
    background_tasks.add_task(run_pipeline)
    return {"message": "Pipeline started in background"}
