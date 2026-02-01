# Distributed Task Scheduler

A fault-tolerant background job processing system built with FastAPI, SQLAlchemy, and worker processes.

This project demonstrates how production systems:

manage asynchronous workloads

persist state in SQL databases

recover from worker crashes

retry failed jobs safely

expose monitoring endpoints

#🧠 Architecture Overview

The system is composed of two main services:

1. API Server

2. Accepts job submissions via REST

3. Persists jobs in a SQL database

4. Exposes /stats endpoint for monitoring

5. Worker Process(es)

6. Poll the database for pending jobs

7. Atomically claim jobs

8. Execute tasks
9.  Retry failures
10.   Mark jobs DONE or FAILED

  # 🏗️ High-Level Flow
  
Client
   |
   v
FastAPI Server  --->  SQL Database (jobs table)
                           ^
                           |
                    Worker Processes

🧩 Components
distributed-task-scheduler/
├── api/              # REST API service
│   └── main.py
├── worker/           # Background workers
│   └── worker.py
├── db/               # Database models + engine
│   ├── database.py
│   └── models.py
├── requirements.txt
├── .env.example
└── README.md

⚙️ Tech Stack

Python 3.10+

FastAPI

SQLAlchemy

SQLite (local) / PostgreSQL (prod)

Uvicorn

REST APIs

▶️ How To Run Locally
1️⃣ Clone repo
git clone https://github.com/<your-username>/distributed-task-scheduler.git
cd distributed-task-scheduler

2️⃣ Create virtual env
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

3️⃣ Install deps
pip install -r requirements.txt

4️⃣ Run API server
python -m uvicorn api.main:app --reload


Swagger UI:

http://127.0.0.1:8000/docs

5️⃣ Run worker

In another terminal:

python -m worker.worker

6️⃣ Submit jobs

Using curl:

curl -X POST "http://127.0.0.1:8000/jobs?task_type=test&payload=hello"


Or via Swagger UI.

7️⃣ Monitor
curl http://127.0.0.1:8000/stats

💥 Failure Handling

This system intentionally simulates failures to test reliability.

Workers fail the first attempt

Jobs are re-queued

Retries capped at MAX_ATTEMPTS

After limit → marked FAILED

This validates:

✔ idempotent processing
✔ retry safety
✔ crash recovery
✔ persistent job state

📊 What This Project Demonstrates

This project showcases real backend engineering fundamentals:

distributed worker architecture

SQL-backed queues

concurrency handling

transactional job claiming

retry logic

fault tolerance

RESTful service design

observability via stats endpoint

🚀 Resume-Ready Description

Built a fault-tolerant background job scheduler with FastAPI and SQL, supporting concurrent workers, automatic retries, and crash recovery. Designed persistent job state tracking and monitoring endpoints to analyze system throughput and failures.



Both services operate independently and can scale horizontally.
