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


# Elasticsearch connection
es = Elasticsearch(
    "http://elasticsearch:9200"
)


if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Failed to connect to Elasticsearch")



@app.route("/")
def home():

    return jsonify({
        "message": "AI SIEM API Running",
        "version": "Milestone 6 - AI Threat Analysis"
    })



@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })



@app.route("/logs", methods=["POST"])
def receive_log():

    data = request.json


    if not data:

        return jsonify({
            "error": "Invalid JSON payload"
        }), 400



    # Run AI detection engine
    analysis = analyze_event(data)



    log_entry = {


        # Unique event ID
        "id": str(uuid.uuid4()),


        # Timestamp
        "timestamp": datetime.now(UTC).isoformat(),



        # SIEM fields
        "source": data.get("source"),

        "event_type": data.get("event_type"),

        "severity": data.get("severity"),



        # AI Analysis Results
        "alert": len(analysis["alerts"]) > 0,

        "alert_type": analysis["risk"],

        "risk_score": analysis["threat_score"],


        "threat_analysis": {

            "classification": analysis["risk"],

            "findings": analysis["alerts"],

            "recommended_action": analysis["recommendation"]

        },


        # Original event
        "details": data

    }



    # Store in Elasticsearch
    es.index(
        index="security-logs",
        document=log_entry
    )



    return jsonify({

        "message": "Log stored",

        "id": log_entry["id"],

        "alert": log_entry["alert"],

        "risk": analysis["risk"],

        "risk_score": analysis["threat_score"]

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






@app.route("/alerts")
def alerts():


    response = es.search(

        index="security-logs",

        size=100,

        query={

            "term": {

                "alert": True

            }

        }

    )


    alerts = []


    for hit in response["hits"]["hits"]:

        alerts.append(hit["_source"])



    return jsonify(alerts)






@app.route("/stats")
def stats():


    total = es.count(

        index="security-logs"

    )



    critical = es.count(

        index="security-logs",

        query={

            "term": {

                "alert_type": "critical"

            }

        }

    )



    high = es.count(

        index="security-logs",

        query={

            "term": {

                "alert_type": "high"

            }

        }

    )



    return jsonify({


        "total_events": total["count"],

        "critical_alerts": critical["count"],

        "high_alerts": high["count"]

    })

