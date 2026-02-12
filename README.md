<!-- ========================================================= -->
<!--                 GLOBAL CYBER ATTACK MAP                   -->
<!-- ========================================================= -->



<h1 align="center">🌍 Global Cyber Attack Visualization Platform</h1>

<p align="center">
  Real-Time Cyber Threat Intelligence Dashboard Powered by Live Honeypot Data
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/Honeypot-T--Pot-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Frontend-MapLibre-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Security-Hardened-critical?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Deployment-Vercel-black?style=for-the-badge&logo=vercel"/>
</p>

---

# 📖 Project Overview

The modern internet is continuously targeted by automated scanners, brute-force tools, and malicious actors. Within minutes of connecting a system to the internet, it begins receiving probing traffic.

This project presents a **real-time global cyber attack visualization system** that:

- Captures live attack telemetry using a honeypot
- Streams structured event data securely
- Visualizes global attacks on an animated interactive map
- Provides immersive, real-time threat awareness

---

# 🖼 Dashboard Preview

<img width="1296" height="922" alt="image" src="https://github.com/user-attachments/assets/6a88dc0f-ec03-41b4-bcfe-bf173de3c98d" />


---

# 🎯 Problem Statement

Traditional cybersecurity tools:

- Display raw logs without intuitive visualization
- Lack real-time geographic threat mapping
- Are limited to enterprise security teams
- Do not provide interactive threat awareness dashboards

There is a need for a system that makes global attack data:

- 🌍 Visually understandable  
- ⚡ Real-time  
- 📊 Interactive  
- 🔐 Secure  

---

# 💡 Solution Architecture

```mermaid
flowchart LR
    A[Internet Attackers] --> B[T-Pot Honeypot VM]
    B --> C[Logstash Processing Layer]
    C --> D[Node.js Secure Backend]
    D --> E[Cloudflare Tunnel]
    E --> F[Frontend Visualization Interface]

    style A fill:#111111,stroke:#ff0040,stroke-width:2px,color:#ffffff
    style B fill:#111111,stroke:#00ffff,stroke-width:2px,color:#ffffff
    style C fill:#111111,stroke:#00ffff,stroke-width:2px,color:#ffffff
    style D fill:#111111,stroke:#00ff99,stroke-width:2px,color:#ffffff
    style E fill:#111111,stroke:#ffaa00,stroke-width:2px,color:#ffffff
    style F fill:#111111,stroke:#ff00ff,stroke-width:2px,color:#ffffff
