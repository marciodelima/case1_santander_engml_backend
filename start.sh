#!/bin/bash
#export NUM_WORKERS=1
uvicorn app.main:app
#gunicorn app.main:app -k uvicorn.workers.UnicornWorker --bind=0.0.0.0:8000 --workers=$NUM_WORKERS
