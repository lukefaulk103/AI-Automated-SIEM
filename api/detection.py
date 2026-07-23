def analyze_event(event):
    """
    AI SIEM detection engine.
    Evaluates incoming security events and assigns risk.
    """

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



    # Event detection rules

    if event_type == "failed_login":
        threat_score += 30
        alerts.append("Possible brute force attempt")


    if event_type == "malware_detected":
        threat_score += 80
        alerts.append("Malware detected")


    if event_type == "blocked_connection":
        threat_score += 20
        alerts.append("Firewall blocked connection")



    # Source detection

    if source == "windows_event_log":
        threat_score += 10



    # Risk calculation

    if threat_score >= 80:
        risk = "critical"

    elif threat_score >= 50:
        risk = "high"

    elif threat_score >= 25:
        risk = "medium"

    else:
        risk = "low"



    # SIEM formatted output
    return {

        "risk_score": threat_score,

        "alert": len(alerts) > 0,

        "alert_type": alerts,

        "risk": risk
    }
