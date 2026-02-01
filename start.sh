#!/bin/bash

python -m worker.worker &
python -m uvicorn api.main:app --host 0.0.0.0 --port 10000
