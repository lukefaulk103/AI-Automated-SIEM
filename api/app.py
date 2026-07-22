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

    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "source": data.get("source"),
        "event_type": data.get("event_type"),
        "severity": data.get("severity"),
        "details": data
    }

    es.index(
        index="security-logs",
        document=log_entry
    )

    return jsonify({
        "message": "Log stored",
        "id": log_entry["id"]
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
