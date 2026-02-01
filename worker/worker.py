import time
from sqlalchemy.orm import Session
from datetime import datetime
from db.database import SessionLocal
from db.models import Job, JobStatus

POLL_INTERVAL = 3
MAX_ATTEMPTS = 3

def claim_job(db: Session):
    job = (
        db.query(Job)
        .filter(Job.status == JobStatus.pending)
        .order_by(Job.updated_at)
        .first()
    )
    if not job:
        return None
    job.status = JobStatus.running
    job.attempts += 1
    job.updated_at = datetime.utcnow()
    db.commit()
    return job

def process(job: Job):
    print(f"Processing job {job.id}")
    time.sleep(5)
    if job.attempts < 2:
        raise RuntimeError("Simulated failure")

def main():
    print("Worker started...")
    while True:
        db = SessionLocal()
        try:
            job = claim_job(db)
            if not job:
                time.sleep(POLL_INTERVAL)
                continue
            try:
                process(job)
                job.status = JobStatus.done
            except Exception:
                if job.attempts >= MAX_ATTEMPTS:
                    job.status = JobStatus.failed
                else:
                    job.status = JobStatus.pending
            job.updated_at = datetime.utcnow()
            db.commit()
        finally:
            db.close()

if __name__ == "__main__":
    main()
