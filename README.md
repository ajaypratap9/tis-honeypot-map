# Real-Time Cyber Attack Visualization Dashboard 🗺️🔥

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)
[![Leaflet.js](https://img.shields.io/badge/Leaflet.js-199900?style=for-the-badge&logo=leaflet&logoColor=white)](https://leafletjs.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status: In Progress](https://img.shields.io/badge/Status-In_Progress-orange?style=for-the-badge)]()

> A live global attack map that visualizes real-world cyber threats in real-time using a network of honeypots. Watch bots and scanners from around the world attack your fake servers — just like famous Kaspersky/FortiGuard maps! 🌍⚔️

## Demo / Live Visualization Preview

![Real-Time Cyber Attack Globe Map](https://cdn2.picryl.com/photo/2017/06/03/real-time-cyber-attacks-including-information-on-the-2466dc-1024.jpg)

![Global Cyber Threat Report Map Example](https://sharevault.com/wp-content/uploads/2025/05/annual-security-report-2025-img-3.jpg)

![Cyber Attack Visualization Example](https://sharevault.com/wp-content/uploads/2025/05/four-costly-cyber-breaches-that-youve-already-forgotten-about-img-1.png)

![Interactive Threat Map Example](https://threatmap.checkpoint.com/images/threatmap.jpg)

*(These are real examples of global cyber attack maps. Your project will create a similar live, animated dashboard — replace with your own screenshots/GIFs when ready!)*

## Project Overview 🚀

The internet faces millions of automated attacks daily from bots and scanners. This project deploys a multi-honeypot network to attract real attackers, collects logs, and visualizes attacks in real-time on an interactive world map.

**Wow Factor**: Within 24-48 hours of deployment, thousands of real attacks appear live on the map!

## Key Features ✨

- **Real-time Global Map** — Interactive world map with animated attack markers and geolocation (Leaflet.js).
- **Multiple Honeypots** — T-Pot suite (Cowrie for SSH, Dionaea for SMB, etc.) — 20+ simulated services.
- **Data Storage** — Elasticsearch for efficient log management.
- **Extra Features**:
  - Leaderboard of top attacking countries
  - Sound alerts for new attacks
  - Basic ML attack classification (scikit-learn)
- **Live Stats** — Attack count, types, timestamps, tried usernames/passwords.

## Architecture Diagram

```mermaid
graph TD
    A[Internet Attackers] --> B[Honeypots (T-Pot Suite)]
    B --> C[Log Collection]
    C --> D[Elasticsearch]
    D --> E[Web Dashboard (Flask/Node.js + Leaflet.js)]
    E --> F[Live World Map Visualization]
