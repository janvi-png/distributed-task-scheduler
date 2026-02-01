from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from db.database import SessionLocal, engine
from db.models import Base, Job, JobStatus

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Distributed Task Scheduler")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/jobs")
def create_job(task_type: str, payload: str, db: Session = Depends(get_db)):
    job = Job(task_type=task_type, payload=payload, status=JobStatus.pending)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

@app.get("/stats")
def stats(db: Session = Depends(get_db)):
    return {
        "pending": db.query(Job).filter(Job.status == JobStatus.pending).count(),
        "running": db.query(Job).filter(Job.status == JobStatus.running).count(),
        "done": db.query(Job).filter(Job.status == JobStatus.done).count(),
        "failed": db.query(Job).filter(Job.status == JobStatus.failed).count(),
    }
