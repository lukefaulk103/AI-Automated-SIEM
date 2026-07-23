# AI SIEM Platform

A containerized AI-powered Security Information and Event Management (SIEM) platform designed to collect, normalize, store, analyze, and visualize security events.

The project uses Docker-based microservices to replicate the core architecture of a modern Security Operations Center (SOC) environment.

---

# Current Architecture

             Security Events
                   |
                   v
          Nginx Reverse Proxy
              Port 8080
                   |
                   v
            Flask API Container
              Port 5000
                   |
                   v
      Validation + Normalization
                   |
                   v
      AI Detection Engine
                   |
                   v
      Elasticsearch Log Storage
              Port 9200
                   |
                   v
          Kibana Visualization
              Port 5601

---

# Technologies Used

## Infrastructure

- Docker
- Docker Compose
- Nginx
- Container networking
- Persistent Docker volumes

## Backend

- Python
- Flask
- REST API
- Elasticsearch Python Client

## Security Analytics

- Elasticsearch 8.15.0
- Kibana 8.15.0
- Security event indexing
- Log searching
- Threat visualization
- Risk scoring

---

# Security Concepts Implemented

- Security event ingestion
- Log validation
- Event normalization
- Severity classification
- Unique event identification
- UTC timestamp normalization
- Centralized security event storage
- SIEM-style event indexing
- REST-based log collection
- Threat scoring
- Alert classification
- SOC dashboard development

---

# Current Features

## Completed

✅ Containerized Flask API service  
✅ Nginx reverse proxy  
✅ Docker networking between services  
✅ Health monitoring endpoint  
✅ Security event ingestion API  
✅ JSON event validation  
✅ SIEM normalized event schema  
✅ UUID event tracking  
✅ UTC timestamp formatting  
✅ Elasticsearch integration  
✅ Persistent security log storage  
✅ Elasticsearch indexing  
✅ Kibana integration  
✅ Security event searching  
✅ Security event filtering  
✅ Kibana dashboards  
✅ Risk score visualization  
✅ AI detection engine  
✅ Automated event risk classification  
✅ Alert generation  

---

# Current Data Flow


Security Event
|
v
POST /api/logs
|
v
Flask API
|
v
Input Validation
|
v
AI Detection Engine
|
v
Risk Score + Alert Classification
|
v
Elasticsearch Index
(security-logs)
|
v
Kibana Dashboard
|
v
SOC Event Analysis


---

# AI Detection Engine

Incoming events are analyzed automatically.

The detection engine evaluates:

- Event severity
- Event type
- Event source
- Suspicious activity indicators

Example:

```json
{
    "source": "windows_event_log",
    "event_type": "failed_login",
    "severity": "high",
    "username": "admin",
    "ip": "192.168.1.55"
}

The AI analysis produces:

{
    "alert": true,
    "alert_type": "brute_force_attempt",
    "risk_score": 80
}
Example Security Event

Input:

{
    "source": "firewall",
    "event_type": "blocked_connection",
    "severity": "high",
    "source_ip": "10.10.50.23",
    "destination_ip": "192.168.1.10",
    "port":443,
    "action":"deny"
}

Stored event:

{
    "id": "event-uuid",
    "timestamp": "UTC timestamp",
    "source": "firewall",
    "event_type": "blocked_connection",
    "severity": "high",
    "alert": true,
    "risk_score": 70,
    "details": {
        "source_ip":"10.10.50.23",
        "destination_ip":"192.168.1.10",
        "port":443,
        "action":"deny"
    }
}
API Endpoints
Health Check
GET /api/health

Response:

{
    "status":"healthy"
}
Submit Security Event
POST /api/logs

Example:

{
    "source":"firewall",
    "event_type":"blocked_connection",
    "severity":"high",
    "source_ip":"10.10.50.23",
    "destination_ip":"192.168.1.10",
    "port":443
}
Retrieve Security Events
GET /api/logs

Returns Elasticsearch security events.

Security Statistics
GET /api/stats

Returns:

{
    "total_events":25
}
Elasticsearch

Elasticsearch provides centralized security event storage.

External access:

http://localhost:9200

Index:

security-logs
Kibana Dashboard

Kibana provides visualization and investigation capabilities.

Access:

http://localhost:5601

Current capabilities:

✅ Security event searching
✅ Event filtering
✅ Timestamp analysis
✅ Severity visualization
✅ Risk score monitoring
✅ Alert investigation
✅ SOC dashboard foundation

Running the Project

Clone repository:

git clone <repository-url>

cd ai-siem

Start containers:

docker compose up --build
Access

Application:

http://localhost:8080

API:

http://localhost:8080/api/health

Logs:

http://localhost:8080/api/logs

Elasticsearch:

http://localhost:9200

Kibana:

http://localhost:5601
Testing

Example PowerShell test:

Invoke-RestMethod `
-Uri "http://localhost:8080/api/logs" `
-Method POST `
-Headers @{
    "Content-Type"="application/json"
} `
-Body '{"source":"firewall","event_type":"blocked_connection","severity":"high","source_ip":"10.10.50.23","destination_ip":"192.168.1.10","port":443,"action":"deny"}'

Expected:

{
    "message":"Log stored",
    "id":"generated-uuid",
    "risk_score":70
}
Development Roadmap
Milestone 1 — Container Infrastructure

✅ Docker environment
✅ Docker Compose setup
✅ Nginx service

Milestone 2 — API Development

✅ Flask API container
✅ API routing
✅ Health monitoring

Milestone 3 — SIEM Event Pipeline

✅ Security log ingestion
✅ Validation layer
✅ Event normalization
✅ UUID tracking

Milestone 4 — Elasticsearch Integration

✅ Elasticsearch deployment
✅ Persistent log storage
✅ Security event indexing
✅ Elasticsearch API integration

Milestone 5 — Kibana Dashboard

✅ Kibana deployment
✅ Elasticsearch connection
✅ Security event visualization
✅ Severity monitoring panels
✅ Risk score visualization
✅ SOC dashboard foundation

Milestone 6 — AI Threat Analysis

🟨 Current Phase

⬜ Machine learning anomaly detection
⬜ Behavioral analysis
⬜ Advanced threat scoring
⬜ Threat intelligence integration

Milestone 7 — Automated Response

⬜ Threat notifications
⬜ Security playbooks
⬜ Automated remediation actions
⬜ Incident response workflows

Future Development

Planned features:

SOC-style dashboards
Machine learning anomaly detection
Threat intelligence feeds
Real-time detection rules
Attack pattern recognition
Automated incident response
Network monitoring agents
Windows event collectors
Linux audit log collectors
Cloud security integrations
Project Goal

The goal of this project is to build a fully containerized AI-assisted SIEM platform capable of ingesting security events, analyzing threats, and providing actionable security intelligence similar to enterprise SOC environments.

This project demonstrates practical experience with:

SIEM architecture
Security monitoring
Docker deployments
REST API development
Elasticsearch pipelines
Security analytics
Threat detection
SOC dashboard development
Cloud-native security architecture

---

## Before pushing to GitHub, I recommend one final cleanup:

Run:

```powershell
docker compose down

Then:

docker compose up --build

Make sure a fresh deployment works.

Then:

git status

You should see:

modified:
 README.md
 api/app.py
 api/detection.py
 compose.yml

Then:

git add .
git commit -m "Completed AI SIEM pipeline with Elasticsearch, Kibana, and threat scoring"
git push

This is a very solid milestone. Your project has moved past being a "Docker Flask app" and is now legitimately resembling a small SOC platform. The next logical milestone is Milestone 6: improving the AI detection engine — moving from static rules into anomaly detection and threat intelligence enrichment.
