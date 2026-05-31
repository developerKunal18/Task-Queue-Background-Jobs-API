from flask import Flask, jsonify
import threading
import time
import uuid

app = Flask(__name__)


# Store jobs
jobs = {}


# ---------- Background Task ----------
def process_job(job_id):

    jobs[job_id]["status"] = "Processing"

    # simulate heavy work
    time.sleep(10)

    jobs[job_id]["status"] = "Completed"


# ---------- Create Job ----------
@app.route(
    "/create-job",
    methods=["POST"]
)
def create_job():

    job_id = str(uuid.uuid4())


    jobs[job_id] = {
        "status": "Pending"
    }


    thread = threading.Thread(
        target=process_job,
        args=(job_id,)
    )


    thread.start()


    return jsonify(
        {
            "job_id": job_id,
            "message": "Job started"
        }
    )


# ---------- Check Status ----------
@app.route(
    "/status/<job_id>"
)
def check_status(job_id):

    if job_id in jobs:

        return jsonify(
            {
                "job_id": job_id,
                "status": jobs[job_id]["status"]
            }
        )


    return jsonify(
        {
            "message": "Job not found"
        }
    ), 404



# ---------- All Jobs ----------
@app.route("/jobs")
def all_jobs():

    return jsonify(jobs)



# ---------- Run ----------
if __name__ == "__main__":

    app.run(debug=True)
