from flask import Flask, jsonify, request
from datetime import datetime, UTC
from elasticsearch import Elasticsearch
from detection import analyze_event
import uuid


app = Flask(__name__)


# Elasticsearch connection
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

    data = request.get_json()


    if not data:

        return jsonify({
            "error": "Invalid JSON payload"
        }), 400



    # Run event through AI detection pipeline
    analysis = analyze_event(data)



    event_id = str(uuid.uuid4())


    log_entry = {


        # -------------------------
        # Event Metadata
        # -------------------------

        "id": event_id,


        "timestamp":
            datetime.now(UTC).isoformat(),



        # -------------------------
        # Original SIEM Fields
        # -------------------------

        "source":
            data.get("source"),


        "event_type":
            data.get("event_type"),


        "severity":
            data.get("severity"),




        # -------------------------
        # AI Threat Assessment
        # -------------------------

        "analysis": {


            "alert":
                analysis["alert"],



            "risk":
                analysis["risk"],



            "risk_score":
                analysis["threat_score"],



            "confidence_score":
                analysis["confidence_score"],



            "findings":
                analysis["alerts"],



            "recommendation":
                analysis["recommendation"],



            # ML results

            "machine_learning": {

                "anomaly":
                    analysis["ml_analysis"]["anomaly"],


                "confidence":
                    analysis["ml_analysis"]["confidence"]

            },



            # MITRE ATT&CK enrichment

            "mitre": {

                "technique":
                    analysis["mitre_technique"],


                "name":
                    analysis["mitre_name"]

            }


        },



        # -------------------------
        # Original Event Payload
        # -------------------------

        "details":
            data

    }



    # Store analyzed security event

    es.index(

        index="security-logs",

        document=log_entry

    )



    return jsonify({


        "message":
            "Log stored",


        "id":
            event_id,


        "alert":
            analysis["alert"],


        "risk":
            analysis["risk"],


        "risk_score":
            analysis["threat_score"],


        "ml_anomaly":
            analysis["ml_analysis"]["anomaly"],


        "recommendation":
            analysis["recommendation"]

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

        logs.append(
            hit["_source"]
        )


    return jsonify(logs)




@app.route("/alerts")
def alerts():


    response = es.search(

        index="security-logs",

        size=100,

        query={

            "term": {

                "analysis.alert": True

            }

        }

    )


    alerts = []


    for hit in response["hits"]["hits"]:

        alerts.append(
            hit["_source"]
        )


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

                "analysis.risk.keyword": "critical"

            }

        }

    )



    high = es.count(

        index="security-logs",

        query={

            "term": {

                "analysis.risk.keyword": "high"

            }

        }

    )



    return jsonify({

        "total_events":
            total["count"],


        "critical_alerts":
            critical["count"],


        "high_alerts":
            high["count"]

    })




if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000

    )
