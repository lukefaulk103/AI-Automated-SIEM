# AI SIEM Platform

A containerized AI-powered Security Information and Event Management (SIEM) platform designed to collect, normalize, store, analyze, and visualize security events.

The project is built using Docker-based microservices and is designed to replicate the core architecture of a modern Security Operations Center (SOC) environment.

---

# Current Architecture

```
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
          Elasticsearch Log Storage
                  Port 9200
                       |
                       v
          Persistent Docker Volume
                       |
                       v
              Kibana Visualization
                  Port 5601
```

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

## Data Storage and Analytics

- Elasticsearch 8.15.0
- Kibana 8.15.0
- Indexed security event storage
- Searchable log database
- Security event visualization

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
- Security event visualization
- SOC-style dashboard foundation

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
✅ Elasticsearch integration  
✅ Persistent security log storage  
✅ Elasticsearch event indexing  
✅ Log retrieval from Elasticsearch  
✅ Kibana integration  
✅ Security event searching and filtering  
✅ Kibana data visualization foundation  

---

# Current Data Flow

```
Security Event
      |
      v
POST /api/logs
      |
      v
Flask API
      |
      v
Validation + Normalization
      |
      v
Elasticsearch Index
(security-logs)
      |
      v
Kibana Dashboard
      |
      v
Security Event Analysis
```

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
```

The system normalizes and stores events as:

```json
{
    "id": "ad8d943f-d1c4-4615-8cf9-ad71d1ba2810",
    "timestamp": "2026-07-22T17:46:21.121628+00:00",
    "source": "firewall",
    "event_type": "blocked_connection",
    "severity": "high",
    "details": {
        "source_ip": "10.10.50.23",
        "destination_ip": "192.168.1.10",
        "port": 443,
        "action": "deny"
    }
}
```

---

# API Endpoints

## Health Check

```
GET /api/health
```

Response:

```json
{
    "status": "healthy"
}
```

---

## Submit Security Event

```
POST /api/logs
```

Example:

```json
{
    "source": "windows_event_log",
    "event_type": "failed_login",
    "severity": "high",
    "username": "admin",
    "ip": "192.168.1.55"
}
```

Response:

```json
{
    "message": "Log stored",
    "id": "event-uuid"
}
```

---

## Retrieve Security Events

```
GET /api/logs
```

Returns stored Elasticsearch security events.

---

# Elasticsearch

Elasticsearch provides centralized security event storage.

Internal container access:

```
http://elasticsearch:9200
```

External testing:

```
http://localhost:9200
```

Index:

```
security-logs
```

---

# Kibana Dashboard

Kibana provides visualization and analysis of collected security events.

Access:

```
http://localhost:5601
```

Current capabilities:

✅ Security event search  
✅ Log filtering  
✅ Timestamp analysis  
✅ Event investigation  
⬜ SOC dashboards  
⬜ Automated security visualizations  

---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>

cd ai-siem
```

---

## Build and Start Containers

```bash
docker compose up --build
```

---

# Access Application

## Web Interface

```
http://localhost:8080
```

## API Health Check

```
http://localhost:8080/api/health
```

## View Security Logs

```
http://localhost:8080/api/logs
```

## Elasticsearch

```
http://localhost:9200
```

## Kibana

```
http://localhost:5601
```

---

# Testing

Example PowerShell request:

```powershell
Invoke-RestMethod `
-Uri "http://localhost:8080/api/logs" `
-Method POST `
-Headers @{
    "Content-Type"="application/json"
} `
-Body '{"source":"firewall","event_type":"blocked_connection","severity":"high","source_ip":"10.10.50.23","destination_ip":"192.168.1.10","port":443,"action":"deny"}'
```

Expected response:

```json
{
    "message": "Log stored",
    "id": "generated-uuid"
}
```

---

# Development Roadmap

## Milestone 1 — Container Infrastructure

✅ Docker environment  
✅ Docker Compose setup  
✅ Nginx service  

---

## Milestone 2 — API Development

✅ Flask API container  
✅ API routing  
✅ Health monitoring  

---

## Milestone 3 — SIEM Event Pipeline

✅ Security log ingestion  
✅ Validation layer  
✅ Event normalization  
✅ UUID event tracking  

---

## Milestone 4 — Elasticsearch Integration

✅ Elasticsearch deployment  
✅ Persistent log storage  
✅ Security event indexing  
✅ Elasticsearch API integration  

---

## Milestone 5 — Kibana Dashboard

✅ Kibana deployment  
✅ Elasticsearch connection  
✅ Security event visualization foundation  
⬜ SOC dashboards  
⬜ Severity monitoring panels  
⬜ Attack timeline visualization  

---

## Milestone 6 — AI Threat Analysis

⬜ Machine learning anomaly detection  
⬜ Threat scoring engine  
⬜ Automated alert classification  
⬜ Behavioral analysis  

---

## Milestone 7 — Automated Response

⬜ Threat notifications  
⬜ Security playbooks  
⬜ Automated remediation actions  

---

# Future Development

Planned features:

- SOC-style Kibana dashboards
- AI-powered threat analysis
- Automated alert classification
- Threat scoring engine
- Real-time detection rules
- Attack pattern recognition
- Security analytics dashboard
- Automated incident response
- Local network monitoring agents

---

# Project Goal

The goal of this project is to build a fully containerized AI-assisted SIEM platform capable of ingesting security events, storing and analyzing threats, and providing actionable security intelligence similar to enterprise SOC environments.

This project demonstrates practical experience with:

- Security monitoring architecture
- SIEM design concepts
- Containerized deployments
- REST API development
- Log management
- Elasticsearch-based data pipelines
- Security event analysis
- SOC dashboard development
- Cloud-native security architecture
