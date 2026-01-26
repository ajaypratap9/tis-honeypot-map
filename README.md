# 🌍 Real-Time Cyber Attack Visualization Dashboard

<p align="center">
  <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b" width="85%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/T--Pot-Honeypots-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Elasticsearch-Logs-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Leaflet.js-Map-yellow?style=for-the-badge">
</p>

---

## 📌 Problem Statement

Every day, the internet faces millions of automated cyber attacks such as bots and scanners searching for vulnerable systems.  
Most people and organizations do not have **clear, real-time visibility** into these threats.

They cannot easily see:
- How many attacks are happening
- Where attacks are coming from
- What type of attacks are most common

Most security tools focus mainly on defense. They lack an **intuitive visual representation** of global cyber threats in real time.

---

## 💡 Solution Overview

This project builds a **real-time cyber attack visualization dashboard** that displays live attacks on an interactive world map.

We deploy **honeypots** that behave like real vulnerable servers. Real attackers interact with these systems, and their activities are captured and visualized.

The dashboard helps users understand global attack patterns and raises cybersecurity awareness.

---

## ⚙️ How the System Works

1. **Honeypots Deployment**
   - Uses **T-Pot**, an open-source honeypot platform.
   - Simulates common services like SSH and SMB.
   - Deployed on **Oracle Cloud Free Tier**.

2. **Attack Data Collection**
   - Real attackers interact with the honeypots.
   - All attack attempts are logged automatically.

3. **Log Storage**
   - Logs are stored in **Elasticsearch** for fast querying.

4. **Live Visualization**
   - Web dashboard built using **Flask** and **Leaflet.js**.
   - Shows animated attack markers on a live world map.

5. **Analysis & Alerts**
   - Displays top attacking countries and attack statistics.
   - Sound alerts for new attacks.
   - Basic machine learning classifies attack types.

---

## 🖥️ Live Dashboard Inspiration

<p align="center">
  <img src="https://cybermap.kaspersky.com/assets/img/share.jpg" width="45%">
  <img src="https://threatmap.fortiguard.com/img/map.png" width="45%">
</p>

<p align="center">
  <img src="https://www.checkpoint.com/wp-content/uploads/threatcloud-map.jpg" width="70%">
</p>

> *Images shown above are for inspiration only.  
The actual dashboard will generate live attack data from deployed honeypots.*

---

## 🚀 Key Features

- 🌍 Live global cyber attack map
- 🔴 Animated real-time attack markers
- 📊 Live attack statistics and leaderboards
- 🔔 Sound alerts for new attacks
- 🧠 Basic AI-based attack classification
- 🗂️ Centralized log management
- 🧪 Safe and isolated research environment

---

## 🧰 Technology Stack

### Backend
- Python
- Flask
- Elasticsearch
- Docker
- T-Pot Honeypot Suite

### Frontend
- HTML5
- CSS
- JavaScript
- Leaflet.js

### Machine Learning
- Scikit-learn

---

## 🧱 System Architecture

```mermaid
graph TD
    A[Internet Attackers]
    B[T-Pot Honeypots]
    C[Log Collection]
    D[Elasticsearch]
    E[Flask Backend]
    F[Web Dashboard - Leaflet.js]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
