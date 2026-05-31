# Background Job API
A Flask API implementing a simple task queue system.

## Features
- Create background jobs
- Async processing
- Job ID generation
- Track job status
- View all jobs


## Technologies Used
- Python
- Flask
- Threading


## Installation
pip install flask


## Run
python app.py


## API Endpoints

Create Job:
POST /create-job

Check Status:
GET /status/<job_id>

View Jobs:
GET /jobs
## Purpose

focuses on asynchronous backend processing.
