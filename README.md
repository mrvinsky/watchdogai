# 🐺 ArgusCas AI
### *Autonomous Biometric Security & WFM Integrity Layer for Live Casino Operations*

---

## 📌 Executive Overview
**ArgusCas AI** is an enterprise-grade, zero-hardware security and workforce verification platform built specifically for high-density live broadcast studios and casino gaming floors. 

By autonomously bridging human resources shift schedules (WFM) with live broadcast CCTV camera streams, ArgusCas AI continuously authenticates personnel at every table in real-time. The platform operates completely **headless and invisible** to dealers—eliminating physical badge-scanning bottlenecks while protecting operators from unauthorized substitutions, collusion, and compliance breaches.

---

## ⚡ Core Value & Operational Metrics

* **Zero-Hardware Footprint:** Connects directly to existing broadcast infrastructure (Sony Cinema Line, RTSP IP cameras, Capture Cards). No RFID scanners, PIN pads, or dealer-facing screens required.
* **Frictionless Velocity:** Eliminates the standard 5-second physical badge-scanning pause per rotation. On a 100-table floor, this recovers **101 full working days** of lost table time annually, translating to **14.6M+ additional game rounds**.
* **Zero Disruption to Live Action:** Operates passively in the background. Dealers focus 100% on game integrity and player interaction.
* **Audit-Proof Compliance:** Creates an irrefutable, cryptographically timestamped biometric record of every shift rotation to satisfy strict regulatory authorities (MGA, UKGC, Gibraltar).

---

## 🛡️ Key Architectural Pillars

### 1. Hierarchical Anti-False-Positive Engine
Unlike naive computer vision systems that trigger false alarms whenever multiple individuals enter the camera frame, ArgusCas AI incorporates a proprietary 4-tier contextual validation filter:
1. **Primary Dealer Check:** Validates against the active shift schedule for that specific table.
2. **Shift Rotation Grace Period:** Automatically recognizes the incoming dealer during shift handover windows (configurable $\pm 2\text{ minutes}$) without triggering multi-face alarms.
3. **Studio Shuffler Whitelist:** Contextually validates roving card-shuffling personnel assigned to the active studio.
4. **Global Floor Supervisor Whitelist:** Silently authenticates roaming pitbosses and floor supervisors conducting table checks.

### 2. Dynamic WFM Digital Twin Engine
The system dynamically scales to any studio layout. Upon ingesting raw shift spreadsheets, the parsing engine autonomously constructs a real-time **Digital Twin** of the casino floor in memory—instantly mapping hundreds of tables, assigned dealers, and scheduled rotations across multiple studio buildings and floor levels.

### 3. Centralized CCTV Security Matrix
Designed exclusively for security control rooms and floor supervisors:
* **Live Status Matrix:** Real-time visibility across all active tables with sub-100ms status transitions.
* **Smart Alerting:** Immediate visual and telemetry alerts upon detection of unauthorized individuals, unknown faces, or shift overtime violations.
* **Session Tracking:** Autonomous watchdog daemon monitors dealer table duration and flags rotation fatigue.

---

## 🏗️ High-Level System Architecture

```text
┌────────────────────────┐      ┌────────────────────────┐
│  WFM Shift Schedules   │      │  Broadcast RTSP Feeds  │
│      (Excel / CSV)     │      │   (Live Studio Cameras)│
└───────────┬────────────┘      └───────────┬────────────┘
            │                               │
            ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐
│ Dynamic Parser Engine  │      │ Edge Keyframe Capture  │
└───────────┬────────────┘      └───────────┬────────────┘
            │                               │
            ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐
│  Redis In-Memory State │      │ 512-D Neural Embedding │
│  (Active Table Matrix) │      │  (DeepFace / Insight)  │
└───────────┬────────────┘      └───────────┬────────────┘
            │                               │
            └───────────────┬───────────────┘
                            ▼
            ┌───────────────────────────────┐
            │  Hierarchical Whitelist &     │
            │   Cross-Referencing Engine    │
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │ CCTV Security Matrix Grid UI  │
            │  (Real-Time WebSocket Alerts) │
            └───────────────────────────────┘
```

---

## 🔒 Security & Data Privacy

* **Edge Processing:** Biometric facial vectors (512-dimensional embeddings) are computed on-premise and processed entirely in memory.
* **Encrypted State:** Shift schedules, reference vectors, and session metadata are stored in isolated, access-controlled in-memory caches.
* **Automated Retention Lifecycles:** Snapshot evidence generated during compliance checks is governed by automated purging daemons to adhere strictly to enterprise data protection policies.

---

## ⚖️ Intellectual Property & Proprietary Rights

> **PROPRIETARY AND CONFIDENTIAL**  
> All software architecture, algorithmic flows, and integration designs contained within this repository are the exclusive intellectual property of the author. Registered and deposited in accordance with the Law on Copyright and Related Rights (Zavod za intelektualnu svojinu / Intellectual Property Office). Unauthorized copying, distribution, decompilation, or commercial exploitation is strictly prohibited.
