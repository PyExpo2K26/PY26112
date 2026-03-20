# 💧 Water Surveillance Portal (WSP)
**Active Predictive Logistics & Intelligence Engine for Waterborne Diseases**

WSP is an advanced, AI-powered "Smart Health Surveillance and Early Warning System" designed specifically for rural and remote regions with limited connectivity. It pivots from traditional passive data logging into an **Active Predictive Logistics Engine**. 

Instead of relying on expensive, physical IoT hardware sensors (which are unsustainable in difficult terrain), WSP leverages **Human Sensor Networks** (Primary Health Centres), **Proxy Data** (Weather forecasts), and **Machine Learning** to predict contamination outbreaks before they happen, and surgically optimize the deployment of government resources (Mobile Testing Vans).

---

## 🔬 Methodology & Core Architecture

The system is built on a multi-layered intelligence architecture that correlates environmental chemistry with community health data.

### 1. The 18-Parameter Chemical Analysis
Field officers collect and submit water samples across 18 distinct physical, chemical, oxygen, biological, and heavy metal parameters:
*   **Physical:** Turbidity (NTU)
*   **Chemical:** pH Level, Nitrates, Nitrites, Ammonia, Fluoride, Chloride, Sulphate
*   **Oxygen:** Dissolved Oxygen (DO), Biological Oxygen Demand (BOD), Chemical Oxygen Demand (COD)
*   **Heavy Metals (Critical Triggers):** Lead, Arsenic, Mercury, Cadmium, Iron
*   **Biological:** Presence of E.coli (Fecal coliforms)

### 2. The Hybrid AI Risk Engine
The core intelligence (`risk_engine.py`) uses a two-pronged approach to assess danger:

**A. Deterministic Contamination Index (CI)**
A strict rules-based engine calculates a base CI score (0-100). Crucial safety thresholds inherently boost the CI:
*   Turbidity > 5 NTU (+10 CI)
*   pH outside 6.5–8.5 (+10 CI)
*   E.coli present (+30 CI)
*   Dangerous Heavy Metals (Lead > 0.01mg/L, Arsenic > 0.01, Mercury > 0.001) trigger an instant **Emergency Risk Boost (+50 CI)**.

**B. Probabilistic Machine Learning (Logistic Regression)**
The 18 environmental parameters, combined with the calculated CI, are fed into a trained Machine Learning model (`LogisticRegression`). The ML model predicts the absolute probability (0% to 100%) of a severe waterborne disease outbreak occurring if the water source is consumed.

### 3. Asymmetric Context Modifiers (The "Hackathon Pivot")
Because chemical data alone cannot predict human behavior or sudden environmental shifts, the Risk Engine ingests two external "proxy" data streams to modify the base ML prediction:

*   **PHC Health-Sync (Human Sensor Network):** The system integrates with local Primary Health Centres (PHCs). If a PHC reports a sudden, localized spike in gastrointestinal infections (e.g., >5 cases in a week), the Risk Engine registers an "Active Outbreak". It overrides the chemical baseline, forcefully injecting a **+40.0% Risk Boost** to that village's water sources, instantly tagging it as a red-zone emergency.
*   **Early Warning Weather Triggers:** Integrating with external APIs (like OpenWeather), the system monitors for severe impending rainfall (>100mm). Heavy rain drastically increases agricultural runoff and sewage overflow. The engine pre-emptively assigns a **+15.0% Risk Boost**, issuing proactive warnings *before* the contamination even reaches the water supply.

---

## 🚑 Smart Dispatch & Logistics Platform

The ultimate goal of WSP is actionable government response. High-risk predictions feed directly into the **Smart Dispatch Dashboard**.

### The Triage Algorithm
With limited government resources (Mobile Testing Vans), deployments must be optimized. The system uses a specialized **Triage Algorithm**:
`Triage Score = (AI Risk Probability * Associated Village Population) / 1000`

A village with 10,000 people at 80% risk will rightfully be prioritized over a village of 500 people at 90% risk, ensuring maximum life-saving efficiency.

### The 3-Phase Dispatch Lifecycle
1.  🔴 **Pending Dispatch:** Triage-ranked emergencies are listed. An admin clicks "Dispatch Van".
2.  🟡 **Dispatched (Awaiting Resolution):** The system notes the deployment time and automatically fires an **SMS via Twilio** to the specific Recovery Team lead:  
    *"URGENT WSP Dispatch: Mobile Testing Van dispatched to [Village]. Contamination Risk: 98%. Report to site immediately."*
3.  🟢 **Resolved (Public Notified):** Once the engineering team fixes the water source, the admin marks it "Resolved". The system triggers a **Mass SMS Broadcast** to the registered public in that village:  
    *"WSP Safety Update: Water contamination in [Village] has been RESOLVED. Water is now SAFE for consumption."*

---

## 🛠️ Technology Stack

*   **Backend Server:** Django 5.0 (Python 3.12)
*   **Database:** PostgreSQL (Production) / SQLite (Local Dev)
*   **Machine Learning:** Scikit-Learn (`LogisticRegression`, `RandomForestClassifier`), NumPy, Pandas
*   **Frontend UI:** Pure Vanilla HTML/CSS with Glassmorphism principles, Flexbox, and CSS Grid. Zero frontend frameworks for maximum load speed in low-bandwidth rural areas.
*   **Data Visualization:** Chart.js (Interactive Radar, Line, and Bar charts)
*   **External APIs:** Twilio (SMS Fallback infrastructure)
*   **Hosting Architecture:** Gunicorn WSGI, WhiteNoise (Static Files), Render (Cloud Platform)

---

## 🌟 Application Flow & Features

1.  **Dashboard:** A panoramic view of public health. Tracks total samples, active emergencies, safe water ratios, month-over-month outbreak trends, and a Risk Radar mapping the average concentration of contaminants across the state.
2.  **Submit Sample:** A secure portal for field officers to input the 18-parameter lab results.
3.  **Alerts Intelligence:** Automatically segregates water sources into Safe (Green), Moderate Risk (Yellow), and High Risk (Red).
4.  **Smart Insights:** The AI generates an English-language analysis for every sample, detailing the **Cause** (e.g., "Agricultural runoff"), **Effect** (e.g., "Blue baby syndrome"), and **Immediate Remedy** (e.g., "Implement Reverse Osmosis").
5.  **Offline SMS Fallback:** In deep rural pockets with no 4G internet, officers can submit sample data via a formatted syntax SMS (simulated via Twilio Webhook), ensuring zero drop-off in surveillance capabilities.

---

## 🚀 Installation & Deployment

### Local Development Setup

1. **Clone and Virtual Environment:**
   ```bash
   git clone https://github.com/PyExpo2K26/PY26112.git
   cd PY26112
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Database Migrations:**
   ```bash
   cd source
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Run Server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/`

### Production Deployment (Render)

The repository is fully configured for one-click deployment on Render.com's PaaS infrastructure.

1.  Connect your GitHub repository to Render as a new **Web Service**.
2.  **Build Command:** `./build.sh`
3.  **Start Command:** `cd source && gunicorn water_portal.wsgi:application`
4.  **Environment Variables:**
    *   `PYTHON_VERSION` = `3.12.3`
    *   `DJANGO_SECRET_KEY` = `(Generate Random)`
    *   `DJANGO_DEBUG` = `False`
    *   `DJANGO_ALLOWED_HOSTS` = `.onrender.com`
5.  Deploy. The system uses `whitenoise` to serve static files instantly and securely.
