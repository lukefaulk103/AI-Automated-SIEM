from flask import Flask, jsonify, request
from datetime import datetime, UTC
from elasticsearch import Elasticsearch
from detection import analyze_event
from correlation import check_bruteforce
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



# --------------------------------
# Incident Deduplication Function
# --------------------------------

def check_existing_incident(username, source_ip):

    try:

        # Prevent crash if index does not exist
        if not es.indices.exists(index="security-incidents"):

            return None


        response = es.search(

            index="security-incidents",

            size=1,

            query={

                "bool": {

                    "must": [

                        {
                            "match": {
                                "username": username
                            }
                        },

                        {
                            "match": {
                                "source_ip": source_ip
                            }
                        },

                        {
                            "match": {
                                "status": "open"
                            }
                        }

                    ]

                }

            }

        )


        hits = response["hits"]["hits"]


        if hits:

            return hits[0]


        return None


    except Exception as e:

        print(
            f"Incident lookup failed: {e}"
        )

        return None




@app.route("/")
def home():

    return jsonify({

        "message":
            "AI SIEM API Running",

        "version":
            "Milestone 6 - AI Threat Analysis + Correlation + Deduplication"

    })





@app.route("/health")
def health():

    return jsonify({

        "status":
            "healthy"

    })





@app.route("/logs", methods=["POST"])
def receive_log():


    data = request.get_json()


    if not data:

        return jsonify({

            "error":
                "Invalid JSON payload"

        }),400



    # --------------------------------
    # AI Detection Pipeline
    # --------------------------------

    analysis = analyze_event(data)


    event_id = str(uuid.uuid4())



    log_entry = {


        "id":
            event_id,


        "timestamp":
            datetime.now(UTC).isoformat(),


        "source":
            data.get("source"),


        "event_type":
            data.get("event_type"),


        "severity":
            data.get("severity"),



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



            "machine_learning": {


                "anomaly":
                    analysis["ml_analysis"]["anomaly"],


                "confidence":
                    analysis["ml_analysis"]["confidence"]

            },



            "mitre": {


                "technique":
                    analysis["mitre_technique"],


                "name":
                    analysis["mitre_name"]

            }

        },


        "details":
            data

    }




    # --------------------------------
    # Store Event
    # --------------------------------

    es.index(

        index="security-logs",

        document=log_entry

    )




    # --------------------------------
    # Real-Time Correlation
    # --------------------------------

    recent_events = es.search(

        index="security-logs",

        size=50,

        query={

            "match_all": {}

        }

    )



    events = []


    for hit in recent_events["hits"]["hits"]:

        events.append(

            hit["_source"]

        )



    incident = check_bruteforce(events)



    incident_created = False

    incident_updated = False




    if incident.get("incident"):


        existing_incident = check_existing_incident(

            incident.get("username"),

            incident.get("source_ip")

        )



        # --------------------------------
        # Update Existing Incident
        # --------------------------------

        if existing_incident:


            incident_id = existing_incident["_id"]


            current_count = existing_incident["_source"].get(

                "event_count",

                1

            )



            es.update(

                index="security-incidents",

                id=incident_id,

                doc={

                    "event_count":
                        current_count + 1,


                    "last_updated":
                        datetime.now(UTC).isoformat()

                }

            )


            incident_updated = True




        # --------------------------------
        # Create New Incident
        # --------------------------------

        else:


            incident_document = {


                "timestamp":
                    datetime.now(UTC).isoformat(),


                "status":
                    "open",


                "event_count":
                    incident.get("event_count", 1),


                **incident

            }



            es.index(

                index="security-incidents",

                document=incident_document

            )


            incident_created = True





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


        "incident_created":
            incident_created,


        "incident_updated":
            incident_updated,


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


    logs=[]


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

            "term":{

                "analysis.alert":True

            }

        }

    )


    alerts=[]


    for hit in response["hits"]["hits"]:

        alerts.append(

            hit["_source"]

        )


    return jsonify(alerts)






@app.route("/incidents")
def incidents():


    # Return empty list if index does not exist

    if not es.indices.exists(index="security-incidents"):

        return jsonify([])



    response = es.search(

        index="security-incidents",

        size=100,

        query={

            "match_all":{}

        }

    )


    incidents=[]


    for hit in response["hits"]["hits"]:

        incidents.append(

            hit["_source"]

        )


    return jsonify(incidents)






@app.route("/stats")
def stats():


    total = es.count(

        index="security-logs"

    )



    critical = es.count(

        index="security-logs",

        query={

            "term":{

                "analysis.risk.keyword":"critical"

            }

        }

    )



    high = es.count(

        index="security-logs",

        query={

            "term":{

                "analysis.risk.keyword":"high"

            }

        }

    )



    incident_count = 0


    if es.indices.exists(index="security-incidents"):

        incident_count = es.count(

            index="security-incidents"

        )["count"]



    return jsonify({


        "total_events":
            total["count"],


        "critical_alerts":
            critical["count"],


        "high_alerts":
            high["count"],


        "security_incidents":
            incident_count

    })






if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000

    )
