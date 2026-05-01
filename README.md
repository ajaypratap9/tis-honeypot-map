# CyberWatch

> Real-Time Cyber Attack Visualization Dashboard

A full-stack web application that simulates T-Pot honeypot attack logs and renders them as live animated threats on an interactive world map. Built for academic demonstration and cybersecurity education.

---

## Overview

CyberWatch provides real-time visibility into simulated cyber attack patterns — showing attacker origins, attack types, severity levels, and live statistics through an interactive dark-themed dashboard. The backend generates realistic honeypot log data modeled after T-Pot's Elasticsearch output, making it safe to run on any personal computer without exposing real infrastructure.

---

## Features

| Feature | Description |
|---|---|
| Live Attack Map | Animated attack arcs rendered on a world map using Leaflet.js and OpenStreetMap |
| Geolocation Engine | Real ISP/datacenter IP ranges mapped to 15 countries with weighted distributions |
| Attack Classifier | 14 attack types auto-classified by destination port and protocol |
| Country Leaderboard | Live-ranked attacker countries with animated bar charts |
| Honeypot Services | Simulates Cowrie, Dionaea, Glastopf, and Honeytrap with individual counters |
| Real-Time Feed | Live attack log with IP, payload, severity, country, and timestamp |
| Sound Alerts | Web Audio API alerts for CRITICAL and HIGH severity events |
| WebSocket Delivery | Zero-latency push updates via Socket.IO — no polling, no page refresh |

---

## Quick Start

**Prerequisites:** Python 3.9 or higher, pip

```bash
# 1. Clone the repository
git clone https://github.com/ajaypratap9/tis-honeypot-map
cd cyberwatch

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Project Structure

```
cyberwatch/
├── app.py                  # Flask server + honeypot attack simulator
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Single-page dashboard (map, feed, panels)
└── README.md
```

---

## How the Simulator Works

The attack simulator in `app.py` generates realistic log events that closely mimic what a live T-Pot honeypot would send to Elasticsearch. No real network exposure is required.

**Traffic modeling:**

- Real ISP and datacenter IP subnets from 15 countries (China, Russia, US, Netherlands, Germany, and more)
- Weighted country distribution matching observed real-world honeypot statistics
- Burst pattern simulation — models scanner sweeps with short high-frequency bursts mixed into normal background traffic
- Port-to-attack-type mapping (e.g. `:22 TCP` → SSH Brute Force, `:3389 TCP` → RDP Brute Force, `:445 TCP` → SMB Exploit)
- Real-world payload strings per attack type (credential pairs, SQL strings, directory paths, exploit names)

---

## Connecting to a Real T-Pot Instance

To replace the simulator with live data from a T-Pot deployment on Oracle Cloud or any VPS, swap the `simulate_attacks()` function with an Elasticsearch polling loop:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(
    "http://your-tpot-ip:64298",
    http_auth=("elastic", "changeme")
)

def fetch_real_attacks():
    res = es.search(
        index="logstash-*",
        body={
            "query": {
                "range": {
                    "@timestamp": {"gte": "now-1m"}
                }
            }
        }
    )
    for hit in res["hits"]["hits"]:
        # Map T-Pot fields to CyberWatch attack schema and emit via socketio
        pass
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.9, Flask 3.0 |
| Real-time Transport | Flask-SocketIO 5.3, Socket.IO 4.7 |
| Map Rendering | Leaflet.js 1.9, OpenStreetMap (no API key required) |
| Attack Arc Animation | HTML5 Canvas API |
| Sound Alerts | Web Audio API |
| Typography | IBM Plex Mono, IBM Plex Sans |

---

## Requirements

```
flask>=3.0.0
flask-socketio>=5.3.6
eventlet>=0.35.2
```

---

## Team

| Name | Role |
|---|---|
| Ajay Pratap Singh | Core Architecture & System Design |
| Abhay Pratap Singh | Backend Simulation & Map Integration |
| Akshay Pratap Singh | Frontend Development & Research |
| Dev Kumar | Frontend Development & Research |
| Shritika | UI/UX & Interface Design |

---

## License

This project is built for academic purposes. Not intended for use in production environments or against real systems.
