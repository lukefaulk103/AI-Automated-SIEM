# AI SIEM Platform

A containerized AI-powered Security Information and Event Management (SIEM) platform designed to collect, normalize, analyze, and visualize security events.

The project is built using Docker-based microservices and is designed to replicate the core architecture of a modern SIEM solution.

## Current Architecture
                 Security Logs
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
             Temporary Log Storage


# Technologies Used

## Infrastructure
- Docker
- Docker Compose
- Nginx
- Container networking

## Backend
- Python
- Flask
- REST API

## Security Concepts Implemented
- Security event ingestion
- Log normalization
- Event validation
- Severity classification
- Unique event identification
- UTC timestamp normalization

---

# Current Features

## Completed

✅ Containerized Flask API service  
✅ Nginx reverse proxy  
✅ Docker networking between services  
✅ Health monitoring endpoint  
✅ Security event ingestion API  
✅ JSON event validation  
✅ SIEM-style normalized event schema  
✅ Unique event IDs using UUID  
✅ UTC timestamp formatting  
✅ Multiple security event testing  

---

# Example Security Event

The API accepts security events such as:

```json
{
    "source": "firewall",
    "event_type": "blocked_connection",
    "severity": "medium",
    "source_ip": "10.10.50.23",
    "destination_ip": "192.168.1.10",
    "port": 443,
    "action": "deny"
}

The system normalizes events into:

{
    "id": "27963af6-4d5d-4ea6-bff4-60773165d741",
    "timestamp": "2026-07-22T16:08:32.124961+00:00",
    "source": "firewall",
    "event_type": "blocked_connection",
    "severity": "medium",
    "details": {
        "source_ip": "10.10.50.23",
        "destination_ip": "192.168.1.10",
        "port": 443,
        "action": "deny"
    }
}
API Endpoints
Health Check
GET /api/health

Response:

{
    "status": "healthy"
}
Submit Security Event
POST /api/logs

Example:

{
    "source": "windows_event_log",
    "event_type": "failed_login",
    "severity": "high",
    "username": "admin",
    "ip": "192.168.1.55"
}
Retrieve Logs
GET /api/logs

Returns all collected security events.

Running the Project
Clone Repository
git clone <repository-url>

cd ai-siem
Build and Start Containers
docker compose up --build
Access Application

Web Interface:

http://localhost:8080

API Health Check:

http://localhost:8080/api/health

View Logs:

http://localhost:8080/api/logs

Testing

Example PowerShell request:

Invoke-RestMethod `
-Uri "http://localhost:8080/api/logs" `
-Method POST `
-Headers @{
    "Content-Type"="application/json"
} `
-Body '{"source":"firewall","event_type":"blocked_connection","severity":"medium","source_ip":"10.10.50.23","destination_ip":"192.168.1.10","port":443,"action":"deny"}'


Future Development

Planned features:

Elasticsearch log storage
Kibana security dashboards
AI-powered threat analysis
Automated alert classification
Threat scoring engine
Real-time detection rules
Security analytics dashboard
Project Goal

The goal of this project is to build a fully containerized AI-assisted SIEM platform capable of ingesting security events, analyzing threats, and providing actionable security intelligence similar to enterprise SOC environments.
