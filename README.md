# CyberWatch — Live Cyber Attack Visualization Dashboard

A real-time honeypot attack visualization dashboard that simulates T-Pot honeypot logs
and displays global threats on an interactive world map. Built for academic/demo purposes.

---

## Features

- 🗺️  **Live animated attack arcs** on a dark world map (Leaflet.js + OpenStreetMap, 100% free)
- 🌍  **Geolocation** — real-world IP ranges mapped to 15 countries
- 📊  **Country leaderboard** with live bar charts
- 🔴  **Attack type classifier** — 14 attack types (SSH Brute Force, SQL Injection, SMB Exploit, etc.)
- 📡  **4 simulated honeypot services** — Cowrie, Dionaea, Glastopf, Honeytrap
- 🔊  **Sound alerts** for CRITICAL/HIGH severity attacks
- ⚡  **WebSocket real-time updates** via Socket.IO
- 🎨  **Professional dark UI** — IBM Plex Mono, minimal claude.ai-inspired design

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the dashboard

```bash
python app.py
```

### 3. Open in browser

```
http://localhost:5000
```

---

## How the Simulation Works

The honeypot simulator (`app.py`) generates realistic attack logs that mimic what
T-Pot's Elasticsearch output looks like:

- **Realistic IP ranges** from actual ISP/datacenter subnets in each country
- **Burst patterns** — mimics scanner sweeps (short intense bursts + normal flow)
- **Attack profiles** — port → attack type mapping (e.g. port 22 = SSH brute force)
- **Payloads** — common real-world attack strings per attack type
- **Weighted country distribution** — China & Russia see higher weights (matching real stats)

---

## Project Structure

```
cyber-dashboard/
├── app.py              # Flask backend + attack simulator
├── requirements.txt
├── templates/
│   └── index.html      # Full single-page dashboard
└── README.md
```

---

## Extending for Real T-Pot Integration

To connect a real T-Pot Elasticsearch backend, replace the `simulate_attacks()`
function with an ES query loop:

```python
from elasticsearch import Elasticsearch
es = Elasticsearch("http://your-tpot-ip:64298", http_auth=("elastic","password"))

def fetch_real_attacks():
    res = es.search(index="logstash-*", body={"query": {"range": {"@timestamp": {"gte": "now-1m"}}}})
    for hit in res['hits']['hits']:
        # map fields and emit via socketio
        pass
```

---

## Tech Stack

| Component     | Technology               |
|---------------|--------------------------|
| Backend       | Python + Flask           |
| Real-time     | Flask-SocketIO           |
| Map           | Leaflet.js + OpenStreetMap |
| Arc animation | HTML5 Canvas             |
| Sound         | Web Audio API            |
| Fonts         | IBM Plex Mono/Sans       |
