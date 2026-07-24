import numpy as np

from sklearn.ensemble import IsolationForest


# Training data representing normal activity
training_data = np.array([
    [1,0,0],
    [2,0,0],
    [1,1,0],
    [2,1,0],
    [3,1,0],
    [1,0,1],
    [2,0,1]
])


model = IsolationForest(
    contamination=0.15,
    random_state=42
)


model.fit(training_data)



def detect_anomaly(event):

    """
    Machine learning anomaly detection
    """

    severity = event.get("severity")

    event_type = event.get("event_type")


    failed_login = 1 if event_type == "failed_login" else 0

    malware = 1 if event_type == "malware_detected" else 0


    severity_score = {

        "low":1,
        "medium":2,
        "high":3,
        "critical":4

    }.get(severity,1)



    features = np.array([[
        severity_score,
        failed_login,
        malware
    ]])


    prediction = model.predict(features)


    anomaly_score = model.decision_function(features)[0]


    if prediction[0] == -1:

        return {

            "anomaly": True,

            "confidence": float(
                abs(anomaly_score)
            )

        }


    else:

        return {

            "anomaly": False,

            "confidence": float(
                abs(anomaly_score)
            )

        }
