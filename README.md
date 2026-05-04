# CyberWatch

> Real-Time Cyber Attack Visualization & Threat Intelligence Dashboard

A full-stack web application that simulates T-Pot honeypot attack logs and renders them as live animated threats on an interactive world map — with per-country drill-down analytics, audit report generation, and session-wide PDF exports.

---

## Overview

CyberWatch provides real-time visibility into simulated cyber attack patterns across 15 countries. Beyond live visualization, it offers deep per-country threat intelligence: click any country in the leaderboard to open a full-screen analytics dashboard showing that country's attack timeline, IP address log, port targets, and attack type breakdown. Generate a signed audit report PDF for any country or export the entire session as a global threat report — all from the browser.

The backend simulates realistic honeypot log data modeled after T-Pot's Elasticsearch output, making it safe to run on any personal computer without real network exposure.

---

## Features

| Feature | Description |
|---|---|
| Live Attack Map | Animated attack arcs on a world map via Leaflet.js and OpenStreetMap |
| Geolocation Engine | Real ISP/datacenter IP ranges mapped to 15 countries with weighted distributions |
| Attack Classifier | 14 attack types auto-classified by destination port and protocol |
| Country Leaderboard | Click any country to open its full-screen threat intelligence dashboard |
| Country Dashboard | Per-country analytics: attack timeline chart, IP log table, port targets, attack type breakdown |
| Attack Detail Popup | Click any feed item for a full modal with IP, payload, port, severity, honeypot, and timestamp |
| Country Audit Report | Generate a signed PDF audit report for any country with full attack log and IP intelligence |
| Global Export PDF | Export all captured session attacks as a global threat report PDF |
| Real-Time Feed | Live attack log with severity badges, payloads, and country flags |
| Honeypot Services | Tracks Cowrie, Dionaea, Glastopf, and Honeytrap with individual live counters |
| Sound Alerts | SVG icon toggle for Web Audio API alerts on CRITICAL and HIGH severity events |
| WebSocket Delivery | Zero-latency push updates via Socket.IO |

---

## Quick Start

**Prerequisites:** Python 3.9 or higher, pip

```bash
# 1. Clone the repository
git clone https://github.com/your-username/cyberwatch.git
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
├── app.py                  # Flask server, attack simulator, PDF report generation
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Single-page dashboard — map, panels, modals, country dashboard
└── README.md
```

---

## How It Works

### Attack Simulator

The simulator in `app.py` runs in a background thread and generates realistic attack events modeled after T-Pot honeypot logs. No real network exposure is required.

- Real ISP and datacenter IP subnets from 15 countries
- Weighted country distribution matching observed real-world honeypot statistics (China ~18%, Russia ~14%, US ~10%, etc.)
- Burst pattern simulation — models scanner sweeps with short high-frequency bursts mixed into normal background traffic
- Port-to-attack-type mapping for 14 attack categories
- Real-world payload strings per attack type

### Country Drill-Down Dashboard

Clicking any country in the left panel leaderboard replaces the main view with a full-screen country dashboard. The Socket.IO connection stays active in the background — new attacks from that country are tracked silently and a notification bar appears if new data arrives while the dashboard is open. The back button returns to the main map view with all existing data intact.

The country dashboard shows:
- 4 stat cards: total attacks, unique IPs, most used attack type, last seen
- Attack timeline chart (last 20 minutes, drawn with Canvas API — no chart libraries)
- IP address log table with sort-by-column support
- Attack type breakdown with percentage bars
- Port targets ranked by frequency
- Raw attack log (last 50 attacks from that country)

### Report Generation

Both the country audit report and the global session export are generated server-side using ReportLab and streamed directly to the browser as a PDF download — nothing is written to disk.

**Country Audit Report** includes:
- Cover page with report ID, classification, and metadata
- Executive summary with severity breakdown
- Attack type analysis table
- IP address intelligence table
- Full attack log

**Global Session Report** includes:
- Cover page with session stats
- Top 10 countries table
- Attack severity and type distribution
- Full session attack log

All reports include a CyberWatch digital signature stamp on every page.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the dashboard |
| GET | `/api/recent` | Returns last 50 attack events as JSON |
| GET | `/api/stats` | Returns current totals, leaderboard, and attack type counts |
| POST | `/api/report/country` | Generates and downloads a country audit report PDF. Body: `{"country": "China"}` |
| POST | `/api/report/all` | Generates and downloads a global session report PDF |

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
| Attack Arc Animation | HTML5 Canvas API (no external libraries) |
| Timeline Chart | HTML5 Canvas API (no external chart library) |
| PDF Generation | ReportLab 4.x |
| Sound Alerts | Web Audio API |
| Typography | IBM Plex Mono, IBM Plex Sans |

---

## Requirements

```
flask>=3.0.0
flask-socketio>=5.3.6
eventlet>=0.35.2
reportlab>=4.0.0
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

This project is built for academic purposes under GLA University, Mathura. Not intended for use against real systems or in production environments without proper authorization.
