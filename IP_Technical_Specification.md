# WATCHDOG AI
## ENTERPRISE TECHNICAL ARCHITECTURE & SOFTWARE SPECIFICATION
**Type of Work:** Computer Software / AI Biometric Authentication System  
**Field of Application:** Workforce Management (WFM) and Live Casino Security  

---

### 1. ABSTRACT & PURPOSE OF THE SOFTWARE
Watchdog AI is an enterprise-grade, **passive biometric verification system** designed for high-density live broadcasting environments (e.g., Live Casinos). Operating entirely as a "Headless" (invisible) software layer, it eliminates the need for physical hardware authentication (RFID, PIN pads, or dealer-facing screens). The software bridges raw Workforce Management (WFM) scheduling data with live network camera feeds, autonomously verifying dealer identities across hundreds of tables and alerting security personnel via a centralized command dashboard.

### 2. CORE ARCHITECTURE & MODULES
The software relies on a dynamically scalable microservices architecture (Python, FastAPI, React, Redis, DeepFace/InsightFace) divided into three proprietary engines:

#### A. Dynamic WFM Synchronization Engine
- **Function:** Autonomous parsing of human resources shift schedules (Excel/CSV).
- **Algorithmic Logic:** Unlike static systems, this engine utilizes a proprietary regex-based matrix to dynamically read and generate a "Digital Twin" of the casino floor. Whether a studio has 10 or 1,000 tables, the engine automatically populates the database structure based solely on the ingested WFM file.
- **State Management:** Writes the parsed state into an ultra-low-latency Redis in-memory database, mapping expected employee IDs to spatial coordinates (e.g., Table 8.1 expects Employee ID 43286 at 22:30).

#### B. Headless AI Vision & RTSP Core
- **Function:** Autonomous, background visual authentication from network cameras.
- **Algorithmic Logic:** 
  1. *Automated Network Capture:* The system connects directly to the studio's existing network IP cameras (via RTSP protocols) or capture cards. It does not require manual video input or dealer interaction.
  2. *Edge Frame Extraction:* A watchdog background daemon extracts keyframes at optimized intervals to preserve CPU/GPU bandwidth.
  3. *Biometric Embedding & L2 Distance:* Extracts 512-dimensional facial embeddings using deep neural networks, comparing the live feed against the HR reference image in under 100 milliseconds.

#### C. Centralized CCTV Security Matrix (Dashboard)
- **Function:** The sole human-machine interface, designed strictly for Security/Pitboss oversight.
- **Algorithmic Logic:** A React-based, WebSocket-driven real-time grid. Instead of single-table monitoring, the UI renders a massive matrix of all active tables. Tables maintain a "SAFE" (Green) status passively. Upon biometric mismatch, the specific node instantly triggers a "DANGER/UNAUTHORIZED" (Red) alert, allowing instantaneous intervention.

### 3. INNOVATION & ORIGINALITY (IP CLAIM)
The core intellectual property of Watchdog AI lies in its **Zero-Hardware, Headless Enforcement Loop**. Traditional systems demand active input (scanning a badge) which disrupts operations. Watchdog AI is highly original in its method of taking two completely disparate, unstructured data sources—static HR Excel schedules and raw network CCTV streams—and autonomously bridging them via an AI cross-referencing loop. The ability to dynamically scale this verification across hundreds of nodes without introducing a single piece of physical hardware or dealer-facing screen constitutes the unique trade secret and architectural novelty of this software.

### 4. DATA FLOW DIAGRAM (TEXTUAL)
1. `WFM_SPREADSHEET` -> `DYNAMIC_PARSER` -> `REDIS_DIGITAL_TWIN`
2. `NETWORK_RTSP_STREAMS` -> `HEADLESS_WATCHDOG_DAEMON` -> `EMBEDDING_EXTRACTOR`
3. `COMPARISON_ENGINE` (Matches `REDIS_DIGITAL_TWIN` vs `LIVE_EMBEDDING`)
4. `RESULT` -> `CCTV_SECURITY_MATRIX_GRID`

---
**AUTHOR / CREATOR:** [Your Name / Company]
**DATE OF COMPLETION:** August 2026
**DEPLOYMENT ENVIRONMENT:** Secure Docker Containerization (On-Premise / Edge)
