def analyze_event(event):

    threat_score = 0
    alerts = []


    severity = event.get("severity")

    event_type = event.get("event_type")

    source = event.get("source")



    # Severity scoring

    if severity == "critical":

        threat_score += 90
        alerts.append("Critical severity event")


    elif severity == "high":

        threat_score += 70
        alerts.append("High severity event")


    elif severity == "medium":

        threat_score += 40



    # Event detection

    if event_type == "failed_login":

        threat_score += 30

        alerts.append(
            "Possible brute force attempt"
        )



    if event_type == "malware_detected":

        threat_score += 80

        alerts.append(
            "Malware detected"
        )



    if event_type == "blocked_connection":

        threat_score += 20

        alerts.append(
            "Firewall blocked connection"
        )



    # Source analysis

    if source == "windows_event_log":

        threat_score += 10




    if threat_score >= 80:

        risk = "critical"

        recommendation = "Immediate investigation required"



    elif threat_score >= 50:

        risk = "high"

        recommendation = "Review event and investigate source"



    elif threat_score >= 25:

        risk = "medium"

        recommendation = "Monitor activity"



    else:

        risk = "low"

        recommendation = "No immediate action required"




    return {

        "threat_score": threat_score,

        "risk": risk,

        "alerts": alerts,

        "recommendation": recommendation

    }
