# AI SIEM Platform

A containerized AI-powered Security Information and Event Management (SIEM) platform designed to collect, normalize, analyze, correlate, and visualize security events.

The project uses Docker-based microservices to replicate the architecture and workflow of a modern Security Operations Center (SOC) environment.

The platform ingests security events, performs automated threat analysis, applies machine learning anomaly detection, correlates activity patterns, creates incidents, and provides SOC-style visualization through Elasticsearch and Kibana.

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
            AI Detection Pipeline
                       |
        +--------------+--------------+
        |                             |
        v                             v
 Rule-Based Detection        ML Anomaly Detection
        |                             |
        +--------------+--------------+
                       |
                       v
              Threat Scoring Engine
                       |
                       v
             MITRE ATT&CK Enrichment
                       |
                       v
             Correlation Engine
                       |
                       v
          Incident Creation + Deduplication
                       |
                       v
        Elasticsearch Security Storage
                  Port 9200
                       |
                       v
             Kibana SOC Dashboard
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

## Security Analytics

- Elasticsearch 8.15.0
- Kibana 8.15.0
- Security event indexing
- Log searching
- Threat visualization
- Risk scoring
- Alert classification
- Incident management

## Machine Learning

- Scikit-learn
- Isolation Forest anomaly detection
- Behavioral anomaly scoring
- ML confidence scoring

---

# Security Concepts Implemented

- Security event ingestion
- Log validation
- Event normalization
- Severity classification
- UUID event tracking
- UTC timestamp normalization
- Centralized security logging
- SIEM event indexing
- REST-based log collection
- Threat scoring
- Alert generation
- Machine learning anomaly detection
- MITRE ATT&CK mapping
- Real-time event correlation
- Incident creation
- Incident deduplication
- SOC dashboard development

---

# Current Features

## Completed

✅ Containerized Flask API service  
✅ Nginx reverse proxy  
✅ Docker service networking  
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
✅ Risk visualization  
✅ AI threat detection engine  
✅ Automated risk classification  
✅ Alert generation  
✅ Machine learning anomaly detection  
✅ Confidence scoring  
✅ MITRE ATT&CK enrichment  
✅ Real-time event correlation  
✅ Brute force detection  
✅ Incident generation  
✅ Incident deduplication  
✅ Incident tracking API  

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

Input Validation

      |
      v

AI Detection Engine

      |
      +----------------+
      |                |
      v                v

Rule Analysis     ML Detection

      |
      v

Threat Score + Classification

      |
      v

MITRE ATT&CK Mapping

      |
      v

Correlation Engine

      |
      v

Incident Management

      |
      v

Elasticsearch Index

      |
      v

Kibana Dashboard

      |
      v

SOC Investigation
```

---

# AI Detection Engine

Incoming events are automatically analyzed.

The detection engine evaluates:

- Event severity
- Event type
- Event source
- Suspicious indicators
- Machine learning anomaly score
- MITRE ATT&CK techniques

Example Input:

```json
{
    "source": "windows_event_log",
    "event_type": "failed_login",
    "severity": "high",
    "username": "admin",
    "ip": "192.168.1.55"
}
```

AI Analysis Output:

```json
{
    "alert": true,
    "risk": "critical",
    "risk_score": 100,
    "recommendation": "Immediate investigation required",
    "mitre": {
        "technique": "T1110",
        "name": "Brute Force"
    }
}
```

---

# Machine Learning Detection

The platform uses an Isolation Forest model to identify anomalous security activity.

The ML engine evaluates:

- Event severity
- Event type
- Suspicious activity patterns

Example:

```
Failed Login Attempts
        +
High Severity
        +
Unknown Behavior Pattern

        |

Machine Learning Detection

        |

Anomaly Identified
```

---

# Real-Time Correlation Engine

The correlation engine analyzes multiple events together to identify attack patterns.

Current correlation:

## Brute Force Detection

Example:

```
Multiple Failed Login Attempts

        |

Same Username

        |

Same Source IP

        |

Incident Created
```

Generated Incident:

```json
{
    "incident_type": "Brute Force Attack",
    "severity": "critical",
    "event_count": 5,
    "status": "open",
    "recommendation": "Investigate possible credential compromise"
}
```

---

# Incident Management

The platform automatically:

- Creates incidents
- Tracks repeated activity
- Prevents duplicate incidents
- Updates existing investigations

Incident lifecycle:

```
Security Event

      |

Detection

      |

Correlation

      |

Incident Created

      |

Additional Events

      |

Existing Incident Updated
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
    "status":"healthy"
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
    "source":"firewall",
    "event_type":"blocked_connection",
    "severity":"high",
    "source_ip":"10.10.50.23",
    "destination_ip":"192.168.1.10",
    "port":443
}
```

---

## Retrieve Security Events

```
GET /api/logs
```

Returns indexed security events.

---

## Retrieve Alerts

```
GET /api/alerts
```

Returns detected security alerts.

---

## Retrieve Incidents

```
GET /api/incidents
```

Returns correlated security incidents.

---

## Security Statistics

```
GET /api/stats
```

Example:

```json
{
    "total_events":100,
    "critical_alerts":20,
    "high_alerts":35,
    "security_incidents":5
}
```

---

# Elasticsearch

Elasticsearch provides centralized security event storage.

Access:

```
http://localhost:9200
```

Indexes:

```
security-logs
security-incidents
```

---

# Kibana Dashboard

Kibana provides visualization and investigation capabilities.

Access:

```
http://localhost:5601
```

Current capabilities:

✅ Security event searching  
✅ Event filtering  
✅ Timestamp analysis  
✅ Severity visualization  
✅ Risk score monitoring  
✅ Alert investigation  
✅ Incident tracking  
✅ SOC dashboard foundation  

---

# Running the Project

Clone repository:

```powershell
git clone <repository-url>

cd ai-siem
```

Start containers:

```powershell
docker compose up --build
```

---

# Access

Application:

```
http://localhost:8080
```

API:

```
http://localhost:8080/api/health
```

Logs:

```
http://localhost:8080/api/logs
```

Alerts:

```
http://localhost:8080/api/alerts
```

Incidents:

```
http://localhost:8080/api/incidents
```

Elasticsearch:

```
http://localhost:9200
```

Kibana:

```
http://localhost:5601
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
✅ UUID tracking  

---

## Milestone 4 — Elasticsearch Integration

✅ Elasticsearch deployment  
✅ Persistent storage  
✅ Security event indexing  

---

## Milestone 5 — Kibana Visualization

✅ Kibana deployment  
✅ Elasticsearch connection  
✅ SOC dashboard creation  
✅ Security visualization  

---

## Milestone 6 — AI Threat Analysis

✅ Rule-based detection  
✅ Machine learning anomaly detection  
✅ Threat scoring  
✅ Confidence scoring  
✅ MITRE ATT&CK enrichment  
✅ Alert classification  

---

## Milestone 6.5 — Correlation & Incident Management

✅ Real-time correlation  
✅ Brute force detection  
✅ Incident creation  
✅ Incident deduplication  
✅ Incident tracking  

---

## Milestone 7 — Threat Intelligence & Automated Response

⬜ Threat intelligence feeds  
⬜ IOC enrichment  
⬜ Automated notifications  
⬜ Security playbooks  
⬜ Automated remediation actions  
⬜ Incident response workflows  

---

# Future Development

Planned features:

- Threat intelligence integration
- IOC reputation checking
- Automated response actions
- Windows event collectors
- Linux audit collectors
- Network monitoring agents
- Cloud security integrations
- Advanced behavioral analytics
- SOC automation workflows

---

# Project Goal

The goal of this project is to build a fully containerized AI-assisted SIEM platform capable of ingesting security events, analyzing threats, correlating attack patterns, and providing actionable security intelligence similar to enterprise SOC environments.

This project demonstrates practical experience with:

- SIEM architecture
- Security monitoring
- Detection engineering
- Docker deployments
- REST API development
- Elasticsearch pipelines
- Machine learning security analytics
- Threat detection
- Incident management
- SOC dashboard development
- Cloud-native security architecture
