from ml_detection import detect_anomaly


def analyze_event(event):
    """
    AI SIEM Detection Engine

    Performs:
    - Rule-based threat detection
    - ML anomaly detection
    - Threat scoring
    - SOC metadata enrichment
    """

    threat_score = 0
    alerts = []

    severity = event.get("severity", "").lower()
    event_type = event.get("event_type", "").lower()
    source = event.get("source", "").lower()

    confidence_score = 50

    mitre_technique = "Unknown"
    mitre_name = "Unknown"


    # -------------------------
    # Rule-Based Severity Scoring
    # -------------------------

    if severity == "critical":
        threat_score += 90
        confidence_score += 30
        alerts.append("Critical severity event")


    elif severity == "high":
        threat_score += 70
        confidence_score += 20
        alerts.append("High severity event")


    elif severity == "medium":
        threat_score += 40
        confidence_score += 10



    # -------------------------
    # Event Detection Rules
    # -------------------------

    if event_type == "failed_login":

        threat_score += 30
        confidence_score += 15

        alerts.append(
            "Possible brute force attempt"
        )

        mitre_technique = "T1110"
        mitre_name = "Brute Force"



    elif event_type == "malware_detected":

        threat_score += 80
        confidence_score += 25

        alerts.append(
            "Malware detected"
        )

        mitre_technique = "T1204"
        mitre_name = "User Execution"



    elif event_type == "blocked_connection":

        threat_score += 20
        confidence_score += 5

        alerts.append(
            "Firewall blocked connection"
        )

        mitre_technique = "T1046"
        mitre_name = "Network Service Discovery"



    elif event_type == "powershell_execution":

        threat_score += 60
        confidence_score += 20

        alerts.append(
            "Suspicious PowerShell execution"
        )

        mitre_technique = "T1059.001"
        mitre_name = "PowerShell"



    # -------------------------
    # Source Weighting
    # -------------------------

    if source == "windows_event_log":

        threat_score += 10


    elif source == "endpoint_security":

        threat_score += 20


    elif source == "firewall":

        threat_score += 5



    # -------------------------
    # ML Anomaly Detection
    # -------------------------

    ml_result = detect_anomaly(event)


    if ml_result["anomaly"]:

        threat_score += 20

        alerts.append(
            "Machine learning detected anomalous behavior"
        )

        confidence_score += 15



    # -------------------------
    # Normalize Scores
    # -------------------------

    threat_score = min(threat_score, 100)

    confidence_score = min(
        confidence_score,
        100
    )



    # -------------------------
    # Final Risk Classification
    # -------------------------

    if threat_score >= 80:

        risk = "critical"

        recommendation = (
            "Immediate investigation required"
        )


    elif threat_score >= 60:

        risk = "high"

        recommendation = (
            "Review event immediately"
        )


    elif threat_score >= 30:

        risk = "medium"

        recommendation = (
            "Monitor activity"
        )


    else:

        risk = "low"

        recommendation = (
            "No immediate action required"
        )



    return {


        "alert": threat_score >= 60,


        "alert_type": event_type,


        "threat_score": threat_score,


        "confidence_score": confidence_score,


        "risk": risk,


        "alerts": alerts,


        "recommendation": recommendation,


        "mitre_technique": mitre_technique,


        "mitre_name": mitre_name,


        "ml_analysis": {

            "anomaly": ml_result["anomaly"],

            "confidence":
                ml_result["confidence"]

        },


        "threat_analysis": {

            "recommended_action":
                recommendation,

            "confidence":
                confidence_score

        }

    }
