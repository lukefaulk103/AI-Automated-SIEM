import sys
import subprocess

try:
    from flask import Flask, jsonify, request  # type: ignore[import]
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask, jsonify, request  # type: ignore[import]


from datetime import datetime, UTC


try:
    from elasticsearch import Elasticsearch  # type: ignore[import]
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "elasticsearch"])
    from elasticsearch import Elasticsearch  # type: ignore[import]


import uuid


# AI SIEM Detection Engine
from detection import analyze_event


app = Flask(__name__)


# Connect to Elasticsearch container
es = Elasticsearch(
    "http://elasticsearch:9200"
)


# Verify Elasticsearch connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Failed to connect to Elasticsearch")



@app.route("/")
def home():

    return jsonify({
        "message": "AI SIEM API Running"
    })



@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })



@app.route("/logs", methods=["POST"])
def receive_log():

    data = request.json


    # Validate JSON input
    if not data:

        return jsonify({
            "error": "Invalid JSON payload"
        }), 400



    # Run security event through AI detection engine
    analysis = analyze_event(data)



    log_entry = {

        # Unique event identifier
        "id": str(uuid.uuid4()),


        # UTC timestamp
        "timestamp": datetime.now(UTC).isoformat(),


        # Core SIEM fields
        "source": data.get("source"),
        "event_type": data.get("event_type"),
        "severity": data.get("severity"),


        # AI Detection Results
        "alert": analysis["alert"],
        "alert_type": analysis["alert_type"],
        "risk_score": analysis["risk_score"],


        # Original event data
        "details": data
    }



    # Store normalized event in Elasticsearch
    es.index(
        index="security-logs",
        document=log_entry
    )



    return jsonify({

        "message": "Log stored",

        "id": log_entry["id"],

        "alert": analysis["alert"],

        "alert_type": analysis["alert_type"],

        "risk_score": analysis["risk_score"]

    })



@app.route("/logs", methods=["GET"])
def get_logs():

    response = es.search(
        index="security-logs",
        size=100,
        query={
            "match_all": {}
        }
    )


    logs = []


    for hit in response["hits"]["hits"]:

        logs.append(hit["_source"])


    return jsonify(logs)



@app.route("/stats")
def stats():

    response = es.count(
        index="security-logs"
    )


    return jsonify({

        "total_events": response["count"]

    })



if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000

    )
