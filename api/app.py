try:
    from flask import Flask, jsonify, request  # type: ignore[import]
except ImportError:
    raise ImportError("Flask is not installed. Run: pip install flask")

from datetime import datetime, UTC
import uuid

app = Flask(__name__)

# Temporary log storage
logs = []


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

    # Validate required fields
    required_fields = [
        "source",
        "event_type",
        "severity"
    ]

    missing_fields = [
        field for field in required_fields 
        if field not in data
    ]

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing": missing_fields
        }), 400


    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "source": data["source"],
        "event_type": data["event_type"],
        "severity": data["severity"],
        "details": data
    }


    logs.append(log_entry)

    return jsonify({
        "message": "Log received",
        "log_id": log_entry["id"]
    }), 201



@app.route("/logs", methods=["GET"])
def get_logs():

    return jsonify(logs)



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
